"""Verify the public NBY Y Spider catalog and representative media samples."""
import importlib.util
import json
import pathlib
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT.parent
sys.path.insert(0, str(WORK / 'windows-client/scripts'))
sys.path.insert(0, str(WORK / '.audit_deps'))
import imageio_ffmpeg

spec = importlib.util.spec_from_file_location('nbyy', ROOT / 'assets/c/nbyy.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
spider = module.Spider()
spider.init()
result = {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
          'site': spider.HOST, 'android_verified': False,
          'scope': 'Public catalog, search, movie and series samples; not the whole library.',
          'catalog': {}, 'samples': []}
home = spider.homeContent(True)
assert len(home['class']) == 4 and home['list']
result['home_items'] = len(home['list'])
for category in home['class']:
    first = spider.categoryContent(category['type_id'], '1', False, {})
    second = spider.categoryContent(category['type_id'], '2', False, {})
    assert first['list'] and first['total'] > 0
    assert not ({x['vod_id'] for x in first['list']} & {x['vod_id'] for x in second['list']})
    result['catalog'][category['type_name']] = {'total': first['total'], 'pages': first['pagecount'],
                                              'first_page': len(first['list']), 'second_page': len(second['list'])}
search = spider.searchContent('魔方', False)
assert any(x['vod_name'] == '魔方小姐' for x in search['list'])
result['search_items'] = len(search['list'])
ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
for vid in ['332416311', '325349206', '331859363']:
    detail = spider.detailContent([vid])['list'][0]
    flags = detail['vod_play_from'].split('$$$')
    lists = detail['vod_play_url'].split('$$$')
    sample = {'id': vid, 'title': detail['vod_name'], 'flags': flags,
              'episodes_per_flag': [len(x.split('#')) for x in lists], 'attempts': []}
    for flag, episodes in list(zip(flags, lists))[:5]:
        episode = episodes.split('#')[0].split('$', 1)[1]
        player = spider.playerContent(flag, episode, [])
        checks = []
        for repeat in range(2):
            args = [ffmpeg, '-nostdin', '-hide_banner', '-loglevel', 'warning', '-nostats',
                    '-threads', '1', '-rw_timeout', '7000000', '-user_agent', player['header']['User-Agent'],
                    '-referer', player['header']['Referer'], '-i', player['url'],
                    '-map', '0:v:0', '-map', '0:a:0?', '-t', '5', '-progress', 'pipe:1', '-f', 'null', '-']
            try:
                p = subprocess.run(args, capture_output=True, timeout=35)
                out, err = p.stdout.decode('utf8', 'replace'), p.stderr.decode('utf8', 'replace')
                frames = max([int(x) for x in re.findall(r'^frame=(\d+)', out, re.M)] or [0])
                errors = re.findall(r'error while decoding|Invalid data found|Packet corrupt|HTTP error|Server returned [45]\d\d|Connection timed out|Failed to resolve hostname', err, re.I)
                check = {'exit_code': p.returncode, 'frames': frames, 'errors': errors,
                         'passed': p.returncode == 0 and frames >= 25 and not errors}
            except subprocess.TimeoutExpired:
                check = {'passed': False, 'reason': '35 second timeout'}
            checks.append(check)
            if not check['passed']:
                break
        passed = len(checks) == 2 and all(x['passed'] for x in checks)
        sample['attempts'].append({'flag': flag, 'url': player['url'], 'checks': checks, 'passed': passed})
        print(detail['vod_name'], flag, passed, flush=True)
        if passed:
            break
    sample['passed'] = any(x['passed'] for x in sample['attempts'])
    result['samples'].append(sample)
    (ROOT / 'assets/c/nbyy-audit.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf8')
assert all(x['passed'] for x in result['samples']), 'Some representative samples did not decode'
