---
name: ad-creative-research-workflow
description: 竞品广告素材调研完整SOP——广大大登录→搜索→API抓取视频/图片→去重排序→Qwen分析→飞书同步（含图片+视频嵌入）
metadata: 
  node_type: memory
  type: feedback
  originSessionId: fcd4c290-cbef-46cd-99fc-2da60e574539
---

# 竞品广告素材调研 — 端到端工作流

## 一、工具链与分工

| 步骤 | 工具 | 说明 |
|------|------|------|
| 登录广大大 | Playwright browser | `guangdada.net` → 账号预填 → `page.click('button:has-text("登 录")')` |
| 搜索游戏 | Playwright browser | iframe 内 input → fill → Enter |
| **获取素材数据（含视频URL）** | **浏览器 Network 面板 / API 抓包** | 关键突破：视频不在 DOM 里，在 API 返回体里 |
| 下载素材文件 | Bash curl | 图片 JPG + 视频 MP4 |
| 画面分析 | Qwen Vision | `python C:/Users/yangxd/qwen-vision-mcp/analyze.py` |
| 写入飞书 | lark-cli | XML格式插入文本+图片，media-insert上传视频，block_move移动到正确位置 |

## 二、广大大完整操作流程

### Step 1: 登录
```js
// Playwright code
await page.goto('https://guangdada.net/modules/creative/display-ads');
// 页面会重定向到 login，账号 huangjl01@ume.life 已预填
await page.click('button:has-text("登 录")');
// 登录成功后跳转到展示广告页
```

### Step 2: 搜索目标游戏
```js
// 在页面搜索框输入游戏名
const inputs = await page.$$('input');
// 找到搜索 input → fill → Enter
// URL变成: /modules/creative/search-global?headerSearch=游戏名
```

### Step 3: 获取素材数据（核心突破）
**⚠️ 视频URL不在页面DOM里，在API返回体里！**

1. 先切换到"广告创意"tab（在 iframe 内点击）
2. 打开浏览器 Network 面板监控请求
3. 找到 `get-ecom-ads` API 请求（URL 包含 `search_type=1`）
4. 从返回 JSON 提取每条素材的完整数据：

```json
{
  "advertiser_name": "傭兵小鎮",
  "message": "广告文案",
  "heat": 821,
  "impression": 1034092,
  "days_count": 100,
  "platform": 1,  // 1=FB, 5=IG, 8=Messenger, 9=AN
  "video_duration": 39,
  "preview_img_url": "https://sp2cdn-idea-global.zingfront.com/sp_opera/xxx.jpg",
  "resource_urls": [
    {
      "type": 2,  // 1=图片, 2=视频
      "image_url": "https://sp2cdn-idea-global.zingfront.com/sp_opera/xxx.jpg",
      "video_url": "https://sp2cdn-idea-global.zingfront.com/sp_opera/xxx.mp4"  // ← 视频直链!
    }
  ]
}
```

**关键字段：**
- `resource_urls[].video_url` → 视频文件直链（CDN，无需cookie）
- `resource_urls[].image_url` → 封面图/素材图直链
- `preview_img_url` → 缩略图（可能带 `?x-oss-process=image/resize` 参数，去掉即可得原图）
- `type: 1` = 纯图片素材，`type: 2` = 视频素材
- `platform` → 投放渠道
- `heat` → 热度，`impression` → 展示估值

**在 Playwright 中获取 API 数据的方法：**
```
1. browser_network_requests 列出所有请求
2. 找到 get-ecom-ads 的请求 index
3. browser_network_request --index N --part response-body 获取返回体
```

### Step 4: 去重与排序

**去重规则：** 按 `preview_img_url` 去重（同一素材跨渠道投放会有相同的封面图）
- 同一素材在 FB/IG/Messenger/AN 各出现一次 = 4条记录但1套创意
- 去重后按以下指标排序

**排序规则：** 按 `heat`（热度）降序，`impression`（展示估值）为辅助
- 热度高 = 互动率好（点赞/评论/分享）
- 展示高 = 曝光量大
- 两个指标都要看：有些素材展示高但热度低（铺量型），有些则相反（精准型）

### Step 5: 下载素材文件

```bash
# 图片 — 去掉 resize 参数获取原图
curl -L -o "素材名.jpg" "https://sp2cdn-idea-global.zingfront.com/sp_opera/xxx.jpg"

# 视频 — 直接用 API 返回的 video_url
curl -L -o "素材名.mp4" "https://sp2cdn-idea-global.zingfront.com/sp_opera/xxx.mp4"
```

素材保存到 `C:\temp\<游戏名>_ads\` 目录。

### Step 6: 画面分析（Qwen Vision）

```bash
/c/Users/yangxd/AppData/Local/Programs/Python/Python312/python.exe \
  C:/Users/yangxd/qwen-vision-mcp/analyze.py \
  "图片路径" \
  "描述问题，用中文回复。"
```

**视频内容分析：** Qwen Vision 支持视频输入，可直接传入 mp4 文件分析视频实际内容（而非仅封面）。
```bash
python analyze.py "素材.mp4" "描述这个广告视频的内容、节奏、转场、文案。用中文。"
```

## 三、飞书文档同步

### 通用规则
- **先读 `--scope outline`** 确定插入位置 → 再 `--scope section` 获取目标 block ID
- **用 XML 格式插入图片**（markdown 的 `<img width>` 会被飞书 API 丢弃）
- **图片必须同时指定 width 和 height**（素材图通常是正方形 1:1）
- **不要插入空的 `<p/>` 标签**，会导致多余空白

### 插入文本+图片
```bash
cd /c/temp
# 先写 XML 内容到文件
# 再用 @文件路径 插入
lark-cli docs +update --api-version v2 \
  --doc "文档token" \
  --command block_insert_after \
  --block-id "目标block_id" \
  --content @feishu_content.xml
```

XML 中图片格式（必须带 width + height）：
```xml
<img href="https://sp2cdn-idea-global.zingfront.com/sp_opera/xxx.jpg" 
     width="400" height="400" 
     caption="素材描述"/>
```

### 插入视频文件
视频必须先用 `media-insert` 上传（会 append 到文档末尾），再用 `block_move_after` 移动到正确位置：

```bash
# 1. 上传视频 → 记录返回的 block_id
cd /c/temp/素材目录
lark-cli docs +media-insert --doc "token" --file "video.mp4" --type file
# 返回: {"data": {"block_id": "doxcnXXXX"}}

# 2. 移动到正确位置（放在描述段落后）
lark-cli docs +update --api-version v2 --doc "token" \
  --command block_move_after \
  --block-id "目标段落的block_id" \
  --src-block-ids "doxcnXXXX"
```

### 内容结构模板
```xml
<h3>广大大实测数据（查询日期）</h3>
<table><!-- 数据总览表 --></table>
<callout emoji="💡" background-color="light-yellow" border-color="yellow">
  <p>核心发现摘要</p>
</callout>

<!-- 每条素材：h4标题 + 图片 + 描述段落 + 视频 -->
<h4>素材N — 名称（类型 | 热度 | 展示）</h4>
<img href="图片URL" width="400" height="400" caption="描述"/>
<p>画面分析描述。</p>
<!-- 视频文件通过 block_move_after 移动到这里 -->

<callout emoji="⚠️" background-color="light-red" border-color="red">
  <p>数据声明：来源、日期、局限</p>
</callout>
```

## 四、规模化策略

素材 ≤ 20 条时全量分析；素材 > 50 条时分三轮：

1. **第一轮（低 token）：** 只提取 API 文本数据 → 按封面URL去重 → 按热度排序 → 输出 Top 20 给用户选
2. **第二轮（中 token）：** 用户选 3-5 条 → 下载图片+视频 → Qwen Vision 分析
3. **第三轮：** 写入飞书文档（仅用户确认的内容）

## 五、关键教训

- **17173/游戏库截图 ≠ 买量素材**：那是官方 KV，和实际广告素材完全不同
- **视频 URL 在 API 里不在 DOM 里**：这是最大的坑，不要试图在页面上找下载按钮
- **先确认正确文档再插入**：用户可能有多个飞书文档，用 `--scope outline` 先看结构再动手
- **海外素材放海外章节**：国内/海外策略分开，不要混插
- **图片 width 只在 XML 格式生效**：markdown 格式的 width 会被飞书 API 丢弃
- **media-insert 总是插入文档末尾**：需要配合 block_move_after 定位
- **lark-cli 文件路径必须是相对路径**：需要 `cd` 到文件所在目录再执行
- **`team_id` 是必须的**：所有需要 token 的操作都要带 team_id
- **`...` 省略号语法**可用于匹配并替换大段 markdown 内容
- **广大大 CDN 无需认证**：素材 URL 是公开的，curl 直接下载即可

## 六、常见错误速查

| 错误 | 原因 | 解决 |
|------|------|------|
| 登录后看不到搜索结果 | 内容在 iframe 里 | `page.frames()` 找 `iframe/search-global` |
| 找不到下载按钮 | 视频URL在API里 | 监控 Network → get-ecom-ads → video_url |
| 飞书图片太大 | 用了 markdown 格式 | 改用 XML + `width="400" height="400"` |
| 图片下面大段空白 | 插入了空 `<p/>` 标签 | 删除所有空段落 |
| 视频插入后不在正确位置 | media-insert 只往末尾插 | 用 block_move_after 移动 |
| lark-cli 报 file not found | 用了绝对路径 | cd 到文件目录，用相对路径 |
| str_replace 找不到匹配 | XML插入的内容需用XML匹配 | markdown str_replace 只能匹配 markdown 插入的内容 |
