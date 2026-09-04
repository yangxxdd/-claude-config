# 凭证清单 — 到家后需要配置

到家运行 `download.bat` 时会自动引导你配置，这里只是提前告知你需要准备什么。

## 1. DeepSeek API Key（最重要）

你需要准备好你的 DeepSeek API Key（就是你在公司用的那个，sk- 开头的一串字符）。
找不到的话，在公司电脑上打开 `C:\Users\yangxd\.claude\settings.json`，搜索 `ANTHROPIC_AUTH_TOKEN`，冒号后面引号里的就是。

到家运行 `download.bat` 时，脚本会问你，输入即可自动写入所有配置文件。

## 2. Qwen Vision（图片/视频分析）

如果家里也需要分析图片和视频：
- 把公司 `C:\Users\yangxd\qwen-vision-mcp\` 整个目录拷贝回家
- 在 MCP 配置里设置 API Key

## 3. 飞书 / 企业微信

到家后按需重新登录：
- 飞书：`lark-cli auth login`
- 企业微信：根据实际情况重新登录

## 4. 可能需要手动安装的软件

| 工具 | 说明 |
|------|------|
| Python 3.12 | mcp-server-browser-use 需要 |
| Node.js | Playwright MCP 需要 |
| Git | 下载脚本需要（如未安装，脚本会提示你） |

到家运行 `download.bat` 后会自动检测缺少什么。
