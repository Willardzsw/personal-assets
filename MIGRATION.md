# 迁移边界

未执行任何下载的 JAR、JS 或 Python。静态扫描不是完整运行时依赖证明。

保存依赖文件：72；当前站点：78；直播列表：10。

## JAR 内部的外部引用

二进制保持原样；以下地址中有更新、原生库和业务接口，部分下载已失败。即使某个文件已另存，本次也没有重定向 JAR 内硬编码地址。

### vendor/external/f63740a048dd/9c6f4eee384d4e9184f7a751c4d10b16.png.jar

- https://api.bilibili.com/x/v1/dm/list.so
- https://by1.430520.xyz/version.txt
- https://cik07-cos.7moor-fs2.com/im/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/d99c254440ab0274/string.txt
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1715230161845/hxq32.txt
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1715230162455/hxq64.txt
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1719584739844/libnative-lib.txt
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1722525666225/mediaProxy32.txt
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1722525666372/mediaProxy64.txt
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1722525702210/mediaProxyv8.txt
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1722525702368/mediaProxyv7.txt
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1725100071958/mediaProxy-v7a.txt
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1725100072122/mediaProxy-v8a.txt
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1725100072300/mediaProxy-x86.txt
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1725100072468/mediaProxy-x8664.txt
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1733391081056/libLoadNiMa64.txt
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1733391081242/libLoadNiMa32.txt
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1733391081407/libLoadNiMax8632.txt
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1733391081567/libLoadNiMax8664.txt
- https://m.wwgz.cn/js/playerconfig.js
- https://pizazz.s3.bitiful.net/pvideoV7.json
- https://pizazz.s3.bitiful.net/version.txt
- https://wget.la/https://raw.githubusercontent.com/FongMi/Release/fongmi/apk/mobile.json

### vendor/external/93fd4f873c3a/56d0b667615145949789418bff9f22a5.png.jar

- http://www.fmys.top/go/version.txt
- https://6446.kstore.vip/go/version.txt
- https://api.bilibili.com/x/v1/dm/list.so
- https://gitee.com/fmysup/fmys/raw/master/go/version.txt

### vendor/external/1ee02d7eb2a5/4f195a9210254fbbb6ade0cb28fd8e17.png.jar

- https://api.bilibili.com/x/v1/dm/list.so

### vendor/external/ba201e511abd/a7d0606f7915430eb4482f63649d6ce2.png.jar

- https://api.bilibili.com/x/v1/dm/list.so

## 未获得的静态引用

包含示例代码、打包库内部路径和条件分支中的地址，不能把每一项都视为启动必需文件。

- https://fastlink.cokey.xyz/f/5lO2Fd/%E6%9E%81%E5%BD%B1.js — HTTP Error 567
- https://fastlink.cokey.xyz/f/XB4Oik/Acfun.py — HTTP Error 567
- https://fastlink.cokey.xyz/f/nLaNhm/get.js — HTTP Error 567
- https://fastlink.cokey.xyz/f/oPJvI9/Appfox.min.js — HTTP Error 567
- https://im5k.fun/vip.m3u — HTTP Error 500
- https://pan.szfx.top/down.php/56ac2028f2dd8336dccad017927cbef1.py — 下载失败或需要进一步核对
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/py/%E9%9F%A9%E5%B0%8F%E5%9C%88.py — HTTP Error 404
- https://yydsys.top/bg.php — 下载失败或需要进一步核对
- https://api.bilibili.com/x/v1/dm/list.so — HTTP Error 400
- https://by1.430520.xyz/version.txt — 下载失败或需要进一步核对
- https://cik07-cos.7moor-fs2.com/im/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/d99c254440ab0274/string.txt — HTTP Error 514
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1715230161845/hxq32.txt — HTTP Error 403
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1715230162455/hxq64.txt — HTTP Error 403
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1719584739844/libnative-lib.txt — HTTP Error 403
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1722525666225/mediaProxy32.txt — HTTP Error 403
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1722525666372/mediaProxy64.txt — HTTP Error 403
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1722525702210/mediaProxyv8.txt — HTTP Error 403
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1722525702368/mediaProxyv7.txt — HTTP Error 403
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1725100071958/mediaProxy-v7a.txt — HTTP Error 403
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1725100072122/mediaProxy-v8a.txt — HTTP Error 403
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1725100072300/mediaProxy-x86.txt — HTTP Error 403
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1725100072468/mediaProxy-x8664.txt — HTTP Error 403
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1732707176882/jiduo.txt — HTTP Error 403
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1733391081056/libLoadNiMa64.txt — HTTP Error 403
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1733391081242/libLoadNiMa32.txt — HTTP Error 403
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1733391081407/libLoadNiMax8632.txt — HTTP Error 403
- https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1733391081567/libLoadNiMax8664.txt — HTTP Error 403
- https://gitee.com/api/v5/repos/aycapp/openapi/contents/wawaconf.txt — HTTP Error 404
- https://m.wwgz.cn/js/playerconfig.js — 下载失败或需要进一步核对
- https://pizazz.s3.bitiful.net/pvideoV7.json — HTTP Error 403
- https://pizazz.s3.bitiful.net/version.txt — HTTP Error 403
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/js/nbmovie_wasm_bg.js — HTTP Error 404
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/js/lib/JSEncrypt.js — HTTP Error 404
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/js/lib/JSEncryptRSAKey.js — HTTP Error 404
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/js/lib/index.js — HTTP Error 404
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/js/lib/lib/asn1js/asn1.js — HTTP Error 404
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/js/lib/lib/asn1js/base64.js — HTTP Error 404
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/js/lib/lib/asn1js/hex.js — HTTP Error 404
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/js/lib/lib/asn1js/int10.js — HTTP Error 404
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/js/lib/lib/jsbn/base64.js — HTTP Error 404
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/js/lib/lib/jsbn/jsbn.js — HTTP Error 404
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/js/lib/lib/jsbn/prng4.js — HTTP Error 404
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/js/lib/lib/jsbn/rng.js — HTTP Error 404
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/js/lib/lib/jsbn/rsa.js — HTTP Error 404
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/js/lib/lib/jsbn/util.js — HTTP Error 404
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/js/lib/lib/jsrsasign/asn1-1.0.js — HTTP Error 404
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/js/lib/lib/jsrsasign/yahoo.js — HTTP Error 404
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/js/node_modules/process/browser.js — HTTP Error 404
- https://mpimg.cn/down.php/e02034214f0705bfe1e5f4d936f0925f.py — 含凭据或私钥材料，未发布
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/js/drpy2.min.js — 含凭据或私钥材料，未发布
- https://raw.githubusercontent.com/leevi0709/one/0b3e372b9cfb365a27e9a72fd53fccdf137b7b9b/py/%E7%93%9C%E5%AD%90APP.py — 含凭据或私钥材料，未发布

