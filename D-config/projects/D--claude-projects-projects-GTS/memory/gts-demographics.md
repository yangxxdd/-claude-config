---
name: gts-demographics
description: 7月install男女/平台占比基线(campaign层级) + 9月数据异常时男女/平台对比分析的处理方式
metadata: 
  node_type: memory
  type: project
  originSessionId: 2bbc92dd-b0de-4136-87f6-f540cb053eb7
  modified: 2026-09-01T09:40:07.050Z
---

# GTS 男女/平台占比基线 + 异常对比处理

## 7月 Install 男女/平台占比基线（campaign 层级）

⚠️ 7月源文件 `7月汇总日报.xlsx` 的男女/平台数据是**广告系列(campaign)层级**，不是素材层级。只有 install campaign（`GTS-FB-MS-US-install-0709`）整体占比，无逐素材男女/平台拆分。

| 平台 | 安装 | 占比 |
|------|------|------|
| Facebook | 559 | 59.3% |
| Audience Network | 244 | 25.9% |
| Instagram | 137 | 14.5% |

| 性别 | 安装 | 占比 |
|------|------|------|
| male | 746 | 79.2% |
| female | 184 | 19.5% |
| unknown | 12 | 1.3% |

周期 7/9-7/12，总安装 942。核心画像：**男 79%、FB 59%**（男性策略玩家、FB 为主）。

## 9月数据异常时的对比处理（预留）

**触发场景**：某素材数据异常，尤其 vs 7月老素材差距大。

**用户会导出**：媒体端男女数据 + 平台数据（FB/Instagram/Audience Network）。

**我怎么处理**：
1. 对比该素材（或 campaign）的男女占比 vs 7月基线（男79%/女20%）
2. 对比平台占比 vs 7月基线（FB59%/AN26%/IG15%）
3. 判断异常根因：
   - 性别异常：女性占比暴涨 → 可能素材偏女性向，但留存/CPI 变了
   - 平台异常：AN 占比异常高 → AN 误触多 CVR 低（7月 AN CVR 仅 7% vs FB 29%）
4. 结论写进问题追踪的「问题描述」+ 每日结论「警惕信号」

**口径提醒**：7月基线是 campaign 整体，9月用户可能导出素材层级，对比时标注口径差异（整体 vs 逐素材）。

**Why**: 数据异常时需要用男女/平台占比定位根因，7月基线是锚点。
**How to apply**: 9月素材异常、用户给男女/平台数据时，调出本基线对比分析。关联 [[gts-july-baseline]]。
