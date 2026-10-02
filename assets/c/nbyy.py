"""泥巴影院 TVBox Python Spider. Uses public HTML and the site's player API.

Requires requests and lxml (standard TVBox Python Spider dependencies).
Category/search pagination slices the site's complete returned catalog; it does
not claim that the upstream website provides an exhaustive paged database.
"""
import re
import time
from urllib.parse import urljoin
from lxml import etree
from base.spider import Spider as BaseSpider


class Spider(BaseSpider):
    HOST = 'https://www.nbyy.cc'
    HEADERS = {'User-Agent': 'Mozilla/5.0', 'Referer': HOST + '/'}
    CLASSES = [('movie', '电影'), ('tv', '电视剧'), ('show', '综艺'), ('anime', '动漫')]

    def getName(self):
        return '泥巴影院'

    def init(self, extend=''):
        self._pages = {}

    def _get(self, path, params=None):
        response = self.fetch(urljoin(self.HOST, path), params=params,
                              headers=self.HEADERS, timeout=12)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response

    @staticmethod
    def _text(node):
        return ' '.join(''.join(node.itertext()).split()) if node is not None else ''

    def _items(self, html):
        root = etree.HTML(html)
        items, seen = [], set()
        for anchor in root.xpath('//a[contains(@href,"/detail/")][@title]'):
            match = re.search(r'/detail/(\d+)\.html', anchor.get('href', ''))
            if not match or match[1] in seen:
                continue
            seen.add(match[1])
            card = anchor
            while card.getparent() is not None:
                classes = card.get('class', '').split()
                if 'qy-mod-li' in classes or 'qy-list-img' in classes:
                    break
                card = card.getparent()
            image = card.xpath('.//img')
            pic = (image[0].get('data-original') or image[0].get('src')) if image else ''
            if not pic:
                styles = ' '.join(card.xpath('.//@style'))
                m = re.search(r'background-image:\s*url\([\'\"]?([^\)\'\"]+)', styles)
                pic = m[1] if m else ''
            remarks = card.xpath('.//*[contains(@class,"icon-br")]')
            items.append({'vod_id': match[1], 'vod_name': anchor.get('title') or self._text(anchor),
                          'vod_pic': urljoin(self.HOST, pic) if pic else '',
                          'vod_remarks': self._text(remarks[0]) if remarks else ''})
        return items

    def _page(self, path, params, page):
        key = path + repr(sorted(params.items()))
        if key not in self._pages or time.monotonic() - self._pages[key][0] > 300:
            self._pages[key] = (time.monotonic(), self._items(self._get(path, params).text))
        items = self._pages[key][1]
        pg, size = max(1, int(page)), 24
        return {'page': pg, 'pagecount': max(1, (len(items) + size - 1) // size),
                'limit': size, 'total': len(items), 'list': items[(pg-1)*size:pg*size]}

    def homeContent(self, filter):
        return {'class': [{'type_id': k, 'type_name': v} for k, v in self.CLASSES],
                'list': self._items(self._get('/').text)[:24]}

    def homeVideoContent(self):
        return {'list': self._items(self._get('/').text)[:24]}

    def categoryContent(self, tid, pg, filter, extend):
        if tid not in dict(self.CLASSES):
            raise ValueError('未知分类')
        return self._page('/class.html', {'channel': tid}, pg)

    def searchContent(self, key, quick, pg='1'):
        return self._page('/search.html', {'keyword': key}, pg)

    def _routes(self, vid, slug):
        if not re.fullmatch(r'\d+', vid) or not re.fullmatch(r'[\w-]+', slug):
            raise ValueError('无效选集')
        data = self._get('/d0vod/' + vid + '-' + slug).json()
        routes, counts = [], {}
        for row in data.get('aps', []):
            url, source = row.get('pd', ''), str(row.get('ss', '线路'))
            if not url.startswith(('https://', 'http://')):
                continue
            counts[source] = counts.get(source, 0) + 1
            routes.append((source + '-' + str(counts[source]), url))
        return routes

    def detailContent(self, ids):
        vid = str(ids[0])
        if not re.fullmatch(r'\d+', vid):
            raise ValueError('无效影片')
        root = etree.HTML(self._get('/detail/' + vid + '.html').text)
        titles, covers = root.xpath('//h1'), root.xpath('//img[@id="cover"]/@src')
        episodes = [(n.get('slug'), self._text(n)) for n in root.xpath('//ul[@id="play_list_0"]//li[@slug]')]
        episodes = [(slug, name) for slug, name in episodes if slug and name]
        if not episodes:
            raise ValueError('网站未提供选集')
        # Provider + occurrence preserves duplicate providers as distinct routes.
        routes = self._routes(vid, episodes[0][0])
        flags = ['自动'] + [name for name, _ in routes]
        lists = ['#'.join(name.replace('$', '＄').replace('#', '＃') + '$' +
                         '~'.join((vid, slug, flag)) for slug, name in episodes) for flag in flags]
        vod = {'vod_id': vid, 'vod_name': self._text(titles[0]) if titles else vid,
               'vod_pic': urljoin(self.HOST, covers[0]) if covers else '',
               'vod_play_from': '$$$'.join(flags), 'vod_play_url': '$$$'.join(lists)}
        tags = root.xpath('//div[contains(@class,"qy-player-tag")]//span[contains(@class,"tag-item")]')
        for node in tags:
            text = self._text(node)
            if re.fullmatch(r'\d{4}', text):
                vod['vod_year'] = text
        if tags:
            vod['vod_area'] = self._text(tags[0])
        for node in root.xpath('//li[contains(@class,"intro-detail-item")]'):
            text = self._text(node)
            for label, field in [('导演:', 'vod_director'), ('主演:', 'vod_actor'), ('简介:', 'vod_content')]:
                if text.startswith(label):
                    vod[field] = text[len(label):].strip()
        return {'list': [vod]}

    def playerContent(self, flag, id, vipFlags):
        vid, slug, route = id.split('~', 2)
        rows = self._routes(vid, slug)
        if not rows:
            raise ValueError('该集暂无播放源')
        if route == '自动':
            url = rows[0][1]
        else:
            url = next((url for name, url in rows if name == route), None)
            if not url:
                raise ValueError('该集不提供所选线路，请切换自动或其他线路')
        return {'parse': 0, 'url': url, 'header': dict(self.HEADERS)}
