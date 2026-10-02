# XJ 独立配置分支

上游： https://github.com/xiongjian83/TvBox ，快照 `fcff6d4d6764e6449fb0cd0576be9dc248367d6c`。

单配置导入： `https://raw.githubusercontent.com/Willardzsw/personal-assets/source/xiongjian83/profile-c.json`

支持多仓的客户端可导入： `https://raw.githubusercontent.com/Willardzsw/personal-assets/source/xiongjian83/profiles.json`

保留 234 条直播线路（220 个原始频道名称）、27 个点播接口。直播全部通过两轮 FFmpeg 音视频解码，每轮五秒、至少 25 帧、无检测到的损坏错误。点播每接口仅测试一个普通影视样本，两轮通过；不代表整个片库可播。未在 Android/OK影视实际运行。

仅检查仓库内可识别的普通电视频道和 X.json 的 JSON 点播接口。Android 插件、XML 接口、YZ/XJ 外部配置集合及非 HTTP 协议未完成播放验证，不导入。未导入成人清单、账号链接及带鉴权参数的直播地址。原 config.json、profile-b.json 和 sources.json 的 SHA-256 保持不变。可用性仅代表本次电脑网络的检测结果。

新增文件及用途：
- profile-c.json：独立的点播和直播入口。
- profiles.json：三份配置的选择入口。
- assets/c/channels.m3u：过滤、去重后的直播线路。
- assets/c/audit.json：验证范围、结果及每个保留条目的解码记录。
- assets/c/manifest.json：交付文件校验值。
- PROFILE-C.md：使用方式及验证限制。

修改文件：无。删除文件：无。

## 2026-10-02 XHZ 合并

从用户提供的 https://xhztv.top/xhz 检查，HTTPS 返回错误网页，改用同站 HTTP 地址取得配置和直播清单。

新增 372 条直播线路（371 个不同频道标签），均通过两轮五秒 FFmpeg 音视频解码，每轮至少 25 帧。原有 234 条直播线路、27 个点播接口保留；本次没有重新验证原有条目。现有第三个配置链接保持不变，新增内容按 XHZ 分组显示。

54 个插件点播入口和 6 个解析入口未完成 Android 播放验证，没有导入。插件 ZIP 完整性和来源 MD5 匹配仅代表文件完整，不代表播放验证。检查结果仅代表本次网络环境，不保证后续可用性。

文件变更：
- 修改 profile-c.json：直播列表名称标明 XHZ 合并。
- 修改 assets/c/channels.m3u：追加验证通过且不与原配置重复的线路。
- 修改 assets/c/manifest.json：更新交付校验值。
- 修改 PROFILE-C.md：记录合并范围和验证限制。
- 新增 assets/c/xhz-audit.json：保存本次筛选范围及解码证据。
- 删除文件：无。原 A、B 配置不变。
