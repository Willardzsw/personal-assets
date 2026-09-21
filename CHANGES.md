# 文件变更清单

## 修改

- README.md：替换建仓说明，加入配置地址、使用方法、维护方式和运行时依赖限制。

## 新增

- config.json：引用本仓库依赖的 入口配置。
- sources.json：依赖文件来源、大小和 SHA-256 校验清单。
- MIGRATION.md：无法获取及 JAR 内部仍存在的第三方引用。
- tools/verify.py：离线完整性、路径和凭据特征检查；不执行上游代码。
- .gitignore：忽略常见本地凭据、环境文件和 Python 缓存。
- CHANGES.md：本文件。

| 新增依赖文件 | 用途 |
|---|---|
| vendor/external/c5edfeb6a943/tv.txt | 直播列表或辅助配置数据快照 |
| vendor/external/7cf5f79339b0/interfaceTXT.txt | 直播列表或辅助配置数据快照 |
| vendor/external/c0d0d9cf2328/gggg.nzk.txt | 直播列表或辅助配置数据快照 |
| vendor/external/26c6cd5d3ed5/fm.png.jar | 原配置对应的 Android 爬虫或扩展插件（保持二进制原样） |
| vendor/external/1d13e46a6f76/69e0b8deadf7f_1776335070.gif | 界面图片 |
| vendor/external/7d6a4531644c/ipv6.m3u | 直播频道列表快照 |
| vendor/external/4a83ea463e6a/iptv4.txt | 直播列表或辅助配置数据快照 |
| vendor/external/b1d8aea9361b/1fe667cd217a0c314b8ca59310dbf45d.jpg.jar | 原配置对应的 Android 爬虫或扩展插件（保持二进制原样） |
| vendor/external/efc0ae7f021e/bff9d4583388a55afb15a8e3c509af9b.png.jar | 原配置对应的 Android 爬虫或扩展插件（保持二进制原样） |
| vendor/external/f63740a048dd/9c6f4eee384d4e9184f7a751c4d10b16.png.jar | 原配置对应的 Android 爬虫或扩展插件（保持二进制原样） |
| vendor/external/77e9ddfe6b7c/1d9136626610437ab0cac0dbe262d1ed.png.jar | 原配置对应的 Android 爬虫或扩展插件（保持二进制原样） |
| vendor/external/bc1f8e40b84a/d064709f380b4075ac3a4ec302d4244d.png.jar | 原配置对应的 Android 爬虫或扩展插件（保持二进制原样） |
| vendor/external/93fd4f873c3a/56d0b667615145949789418bff9f22a5.png.jar | 原配置对应的 Android 爬虫或扩展插件（保持二进制原样） |
| vendor/external/1ee02d7eb2a5/4f195a9210254fbbb6ade0cb28fd8e17.png.jar | 原配置对应的 Android 爬虫或扩展插件（保持二进制原样） |
| vendor/external/ba201e511abd/a7d0606f7915430eb4482f63649d6ce2.png.jar | 原配置对应的 Android 爬虫或扩展插件（保持二进制原样） |
| vendor/external/6a51bfccf3fa/c540eb4719b24fb9bea28987527b5152.png.jar | 原配置对应的 Android 爬虫或扩展插件（保持二进制原样） |
| vendor/external/b3b3a3386055/yb.js | 站点脚本或 JavaScript 辅助库 |
| vendor/external/1969a85d2d49/yins.json | 站点规则或扩展数据快照 |
| vendor/external/92e9fde3dde9/Internet_iTV.m3u | 直播频道列表快照 |
| vendor/external/2615dcf76d09/LiTV.m3u | 直播频道列表快照 |
| vendor/one/XBPQ/养生堂.json | 站点规则或扩展数据快照 |
| vendor/one/js/一哥.js | 站点脚本或 JavaScript 辅助库 |
| vendor/one/js/咖啡直播.js | 站点脚本或 JavaScript 辅助库 |
| vendor/one/js/ITV.txt | 直播列表或辅助配置数据快照 |
| vendor/one/js/jys.js | 站点脚本或 JavaScript 辅助库 |
| vendor/one/json/动漫巴士.json | 站点规则或扩展数据快照 |
| vendor/one/json/番茶动漫.json | 站点规则或扩展数据快照 |
| vendor/one/json/路漫漫.json | 站点规则或扩展数据快照 |
| vendor/one/json/韩剧在线.json | 站点规则或扩展数据快照 |
| vendor/one/json/韩剧看看.json | 站点规则或扩展数据快照 |
| vendor/one/json/age.json | 站点规则或扩展数据快照 |
| vendor/one/json/aha.json | 站点规则或扩展数据快照 |
| vendor/one/json/bili.json | 站点规则或扩展数据快照 |
| vendor/one/json/bilijihe.json | 站点规则或扩展数据快照 |
| vendor/one/json/bilims.json | 站点规则或扩展数据快照 |
| vendor/one/json/bilirt.json | 站点规则或扩展数据快照 |
| vendor/one/json/biliyy.json | 站点规则或扩展数据快照 |
| vendor/one/json/czkt.json | 站点规则或扩展数据快照 |
| vendor/one/json/douban.json | 站点规则或扩展数据快照 |
| vendor/one/json/gzkt.json | 站点规则或扩展数据快照 |
| vendor/one/json/mtv.json | 站点规则或扩展数据快照 |
| vendor/one/json/sejy.json | 站点规则或扩展数据快照 |
| vendor/one/json/video_data.json | 站点规则或扩展数据快照 |
| vendor/one/json/xxkt.json | 站点规则或扩展数据快照 |
| vendor/one/json/yely.json | 站点规则或扩展数据快照 |
| vendor/one/lib/douyu.js | 站点脚本或 JavaScript 辅助库 |
| vendor/one/lib/huya.js | 站点脚本或 JavaScript 辅助库 |
| vendor/one/lib/ipv4.m3u | 直播频道列表快照 |
| vendor/one/lib/lvse.txt | 直播列表或辅助配置数据快照 |
| vendor/one/py/七星.py | 站点 Python 脚本 |
| vendor/one/py/华数TV.py | 站点 Python 脚本 |
| vendor/one/py/可可影视.py | 站点 Python 脚本 |
| vendor/one/py/哇哇APP.py | 站点 Python 脚本 |
| vendor/one/py/央视.py | 站点 Python 脚本 |
| vendor/one/py/威视TV.py | 站点 Python 脚本 |
| vendor/one/py/枫叶.py | 站点 Python 脚本 |
| vendor/one/py/短剧聚合.py | 站点 Python 脚本 |
| vendor/one/py/马猴.py | 站点 Python 脚本 |
| vendor/one/py/dsystv.py | 站点 Python 脚本 |
| vendor/one/py/yunduo.py | 站点 Python 脚本 |
| vendor/external/70074563c3ab/version.txt | 直播列表或辅助配置数据快照 |
| vendor/external/5988074c6e10/version.txt | 直播列表或辅助配置数据快照 |
| vendor/external/965ccc2c89f6/version.txt | 直播列表或辅助配置数据快照 |
| vendor/external/2c2d998fefa9/mobile.json | 站点规则或扩展数据快照 |
| vendor/one/js/模板.js | 站点脚本或 JavaScript 辅助库 |
| vendor/one/js/gbk.js | 站点脚本或 JavaScript 辅助库 |
| vendor/one/js/jinja.js | 站点脚本或 JavaScript 辅助库 |
| vendor/one/js/jsencrypt.js | 站点脚本或 JavaScript 辅助库 |
| vendor/one/js/json5.js | 站点脚本或 JavaScript 辅助库 |
| vendor/one/js/node-rsa.js | 站点脚本或 JavaScript 辅助库 |
| vendor/one/js/pako.min.js | 站点脚本或 JavaScript 辅助库 |
| vendor/one/js/uri.min.js | 站点脚本或 JavaScript 辅助库 |

## 删除

无。

本地下载缓存和原始分析材料不在公开仓库内。

## 命名调整

- README.md：改用中性标题和说明。
- config.json、tools/verify.py 及资源内的自有地址：同步新仓库路径。
- sources.json：更新修改过的资源校验值。
- CHANGES.md：记录此次改名。
- 未删除资源文件。
