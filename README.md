# 王小二的技术栈

个人站点，正式地址：https://kobewang126.github.io/

原生 HTML、CSS、JavaScript，无运行时依赖。中英文切换保留用户选择；JavaScript 不可用时提供完整中文内容。

## 本地预览

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

打开 http://127.0.0.1:8765/ 。

## 检查

```sh
node --check i18n.js
python3 scripts/check_site.py
```

修改 `index.html` 中的中文内容时，同步更新 `i18n.js` 的英文翻译。资源统一放在 `assets/`。

## 发布

仓库名称必须为 `kobewang126.github.io`，默认分支为 `main`。在 Settings → Pages 中选择从分支发布：`gh-pages` 分支、根目录 `/`。`main` 保存源码与设计资料；`gh-pages` 仅保存正式发布文件。

发布文件仅包含首页、样式、脚本、资源、robots.txt 与 sitemap.xml。可选的 Actions 发布配置保存在 `scripts/pages-workflow.yml.example`，当前使用 GitHub Pages 内置的分支发布。`design/` 是早期设计资料，不包含在发布产物中。

## 素材

掘金与 Bilibili 标志来自 [Simple Icons](https://github.com/simple-icons/simple-icons)（CC0）；简书使用平台公开 favicon；长截图助手图标来自作者提供的应用站点；公众号二维码由作者提供。相关品牌标志归各权利人所有。

作品图标与截图：Toucharium、长截图助手、抗炎记录使用各自产品站的公开资源；预览截图已缩小并压缩。Frame Lab、BinderABC、RPC、dumpsys 未提供独立图标，本站为其制作简洁 SVG 项目标识。

当前视觉主题：纸白 `#FAF9F6`、炭黑 `#272522`、赭红 `#994A32`，使用细边框与暖灰截图底，保留作品原有品牌色。
