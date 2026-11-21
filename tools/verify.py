"""Offline validation only; does not execute vendor code."""
import hashlib,json,pathlib,re,sys,urllib.parse,zipfile,struct
ROOT=pathlib.Path(__file__).resolve().parent.parent
BASE='https://raw.githubusercontent.com/Willardzsw/personal-assets/main/'
BASES=(BASE,'https://raw.githubusercontent.com/Willardzsw/personal-assets/source/xiongjian83/')
errors=[]
manifest=json.loads((ROOT/'sources.json').read_text(encoding='utf8'))
configs={name:json.loads((ROOT/name).read_text(encoding='utf8')) for name in ('config.json','profile-b.json','profile-c.json')}
config=configs['config.json']; keys=[s['key'] for s in config['sites']]
for name,cfg in configs.items():
 site_keys=[s['key'] for s in cfg['sites']]
 if len(site_keys)!=len(set(site_keys)):errors.append(name+': duplicate site keys')
def strings(d):
 if not d.startswith(b'dex\n'):return []
 u=lambda p:struct.unpack_from('<I',d,p)[0];values=[]
 for i in range(u(56)):
  p=u(u(60)+4*i)
  while d[p]&128:p+=1
  p+=1;values.append(d[p:d.index(b'\0',p)].decode('utf8','replace'))
 return values
secret=re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----\s*(?:[A-Za-z0-9+/=]|\\n|\s){80,}')
own_refs=0
def inspect(text,path):
 global own_refs
 if secret.search(text):errors.append(path+': credential/private-key pattern')
 if re.search(r'https?://[^\s"\']*leevi0709/one/',text):errors.append(path+': original repository reference')
 for base in BASES:
  for match in re.finditer(re.escape(base)+r'''[^\s"'`<>\\]+''',text):
   suffix=match[0][len(base):].split(';md5;')[0].split('?')[0].split('#')[0]
   dest=ROOT/urllib.parse.unquote(suffix)
   if not dest.is_file():errors.append(path+': missing own reference '+suffix)
   own_refs+=1
for name,cfg in configs.items():inspect(json.dumps(cfg,ensure_ascii=False),name)
inspect((ROOT/'profiles.json').read_text(encoding='utf8'),'profiles.json')
jar_count=0
for item in manifest['files']:
 p=ROOT/item['path']
 if not p.is_file():errors.append(item['path']+': missing');continue
 b=p.read_bytes()
 if hashlib.sha256(b).hexdigest()!=item['sha256']:errors.append(item['path']+': hash mismatch')
 if b.startswith(b'PK'):
  jar_count+=1
  with zipfile.ZipFile(p) as z:
   if z.testzip():errors.append(item['path']+': ZIP CRC failure')
   for name in z.namelist():
    if name.endswith('.dex'):inspect('\n'.join(strings(z.read(name))),item['path'])
 else:
  try:inspect(b.decode('utf8'),item['path'])
  except UnicodeDecodeError:pass
c_manifest=json.loads((ROOT/'assets/c/manifest.json').read_text(encoding='utf8'))
for item in c_manifest['files']:
 p=ROOT/item['path']
 if not p.is_file():errors.append(item['path']+': missing C delivery file');continue
 # C delivery hashes describe Git's LF text; Windows checkouts may use CRLF.
 b=p.read_bytes()
 if item['sha256'] not in (hashlib.sha256(b).hexdigest(),hashlib.sha256(b.replace(b'\r\n',b'\n')).hexdigest()):errors.append(item['path']+': C delivery hash mismatch')
 if p.suffix in ('.json','.md','.py','.m3u','.txt'):inspect(b.decode('utf8'),item['path'])
print(json.dumps({'files':len(manifest['files']),'c_delivery_files':len(c_manifest['files']),'jars':jar_count,'profiles':{name:{'sites':len(cfg['sites']),'live_lists':len(cfg.get('lives',[]))} for name,cfg in configs.items()},'own_file_references':own_refs,'errors':errors,'playback_verified':False},ensure_ascii=False,indent=2))
sys.exit(bool(errors))
