---
name: gts-wiki-overview
description: GTS飞书Wiki空间概览：关键文档节点、文档树、节点ID、数据源
metadata: 
  node_type: memory
  type: reference
  originSessionId: f94c6671-c0c4-4944-8005-9b4c8ba02b4e
  modified: 2026-08-09T10:02:28.196Z
---

# GTS Wiki 空间概览

## 关键 Wiki 文档

| 文档 | Wiki URL | 类型 | 说明 |
|------|---------|------|------|
| 2月吸量测试报告 | https://my.feishu.cn/wiki/B9B2wh7FiiSaWYkkJcicSYY9nmd | wiki | 含美国/菲律宾/播放数据嵌入表格 |
| 4月留存测试报告 | https://my.feishu.cn/wiki/ODfjwxHSyimE6mk7pz3cHWionvd | wiki | 含国家/出价/素材/用户属性嵌入表格 |
| 2月吸量测试计划 | https://my.feishu.cn/wiki/ONZ8wTKkaitwj3kUilNcC0rxnZd | wiki | 预算 $1500，美国+菲律宾 |
| 留存投放计划 | https://my.feishu.cn/wiki/K29ew2ZB7iSgBxkwi50cVqBynpL | wiki | 预算 $2400，美国 1000 + 菲律宾 150 |

## 关键 Docx 文档

| 文档 | URL | 用途 |
|------|-----|------|
| 规划文档（基准线/关停规则） | https://my.feishu.cn/docx/EAfodj2sxoH0qExR9Jlc1M0JnWg | 7月二测计划 |
| 简报文档（精简版） | https://my.feishu.cn/docx/NBRWdtCdZoQK8cxBb7JcT6BHnVg | 日报汇报 |
| 题材扩展研判 v3 | https://my.feishu.cn/docx/Zk8vdgyapopXsYxb8nJc0qdcnDg | 丧尸/废土/海洋/监狱扩展 |
| 两次测试对比分析 | https://my.feishu.cn/docx/LIEzdD14uoTSwPxDTvCcns37nad | 2月vs4月素材分析 |
| 素材规划 v2 | https://my.feishu.cn/docx/GybJdcyV8ozSsOxhmhUc4lS4nOh | 素材规划 |
| 竞品调研 | https://my.feishu.cn/docx/SuIOdqowQo4qUXxAtbUccXepnMf | 竞品分析 |
| 留存测试规划 | https://my.feishu.cn/docx/OZ6jd5jdaomY6Kxb836caxLtnXe | 测试规划 |

## 数据源 Sheet

| 报告 | Spreadsheet Token | 关键 Sheet ID |
|------|-------------------|---------------|
| 2月吸量报告 | HljIsZhGOhiccAt2vnpcJU3Kn4c | erKbRv(美国)、YU1hV6(菲律宾)、hacBnh(播放数据) |
| 4月留存报告 | JhDasabrthuYLht2ECwcpVXxnRb | CfgROC(install)、wb9oM0(aeo)、o2aVka(国家)、PUSvOb(出价) |

## 文档树待补充

> 完整的 Wiki 空间结构和节点 ID 待从飞书 API 读取后补充。
> 可使用 `lark-cli wiki +node-list` 获取子节点列表。

## 本地备份

- 题材扩展研判：`C:/Users/yangxd/Desktop/GTS投放支持文档_20260525.md`
- 发行运作模式：`C:/Users/yangxd/Desktop/GTS发行运作模式-破圈长留变现-v1.md`
- 素材方向脑图：`C:/Users/yangxd/Desktop/GTS素材方向脑图-整理版-v2.md`

**Why**: GTS 的关键信息分散在多个飞书 wiki/docx/sheet 中，需要统一索引避免每次都重新搜索。
**How to apply**: 需要下钻读取飞书原始数据时，先从本文件拿到 token/sheet-id，再切到 lark-sheets/lark-doc 技能。
