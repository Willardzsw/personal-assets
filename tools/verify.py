"""Offline validation only; does not execute vendor code."""
import hashlib,json,pathlib,re,sys,urllib.parse,zipfile,struct
ROOT=pathlib.Path(__file__).resolve().parent.parent
BASE='https://raw.githubusercontent.com/Willardzsw/TVBOX/main/'
errors=[]
manifest=json.loads((ROOT/'sources.json').read_text(encoding='utf8'))
config=json.loads((ROOT/'config.json').read_text(encoding='utf8'))
keys=[s['key'] for s in config['sites']]
if len(keys)!=len(set(keys)):errors.append('duplicate site keys')
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
 for match in re.finditer(re.escape(BASE)+r'''[^\s"'`<>\\]+''',text):
  suffix=match[0][len(BASE):].split(';md5;')[0].split('?')[0].split('#')[0]
  dest=ROOT/urllib.parse.unquote(suffix)
  if not dest.is_file():errors.append(path+': missing own reference '+suffix)
  own_refs+=1
inspect(json.dumps(config,ensure_ascii=False),'config.json')
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
print(json.dumps({'files':len(manifest['files']),'jars':jar_count,'sites':len(keys),'live_lists':len(config['lives']),'own_file_references':own_refs,'errors':errors,'playback_verified':False},ensure_ascii=False,indent=2))
sys.exit(bool(errors))
