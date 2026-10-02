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

## 2026-10-02 合并第一配置 A

第三配置合并当前已发布的第一配置，保留原 C 的 27 个站点及 606 条 XJ/XHZ 直播线路。新增 77 个站点，共 104 个站点、10 份直播清单、15 个解析入口。按站点类型、API、ext、有效 JAR 和 header 去重；共享插件 API 但 ext 不同的站点继续保留。C 原有站点顺序与 key 保持不变，A 插件绑定原有 JAR。

本次是完整配置合并，不能将所有继承的插件和直播都标为本次播放验证通过。A/B 原文件和 C 的既有直播资产未改。原第三配置链接继续使用。

新增 assets/c/merge-a-audit.json（合并证据）；修改 profile-c.json、profiles.json、PROFILE-C.md 和 assets/c/manifest.json；无删除文件。

## 2026-10-02 泥巴影院 Python 源

综合配置 C 新增“泥巴影院”，共 105 个站点，订阅链接保持不变。
通过网站公开 HTML 和 /d0vod JSON 播放接口提供首页、电影/电视剧/综艺/动漫、搜索、详情及选集。支持自动线路和按提供商区分的备用线路；播放时实时取得地址，未保存临时播放地址到配置。

分类分页是对网站当前返回的目录去重后每页 24 条展示，不代表全站片库；可通过搜索找其他影片。详情保留网站的选集名称与年份。线路列表根据第一集生成，其他集缺少该线路时会提示切换；自动线路选择网站返回的第一条地址，不承诺自动检测线路可用性。

验证：四分类分别返回 86/88/67/52 部去重影片，分页无重复；“魔方”搜索返回 7 部影片。电影《魔方小姐》《盗梦空间》和电视剧《魔方游戏之罪杀》各通过两轮五秒 FFmpeg 音视频解码（148/124/119 帧，详细值以审计 JSON 为准）。电视剧首集、第二集、末集取得播放地址。Windows 0.7.0 实际加载首页/搜索，样本播放解码 380 帧、5.309 秒。Android/OK影视未实机验证；需客户端支持 Python Spider。不保证所有影片或线路都可播放。

文件变更：新增 assets/c/nbyy.py（源）、assets/c/nbyy-audit.json（检测证据）、tools/audit_nbyy.py（可重复检测脚本）；修改 profile-c.json（加入站点）、PROFILE-C.md（说明）、assets/c/manifest.json（校验）。删除文件：无。A/B、原有站点和直播清单保持不变。
