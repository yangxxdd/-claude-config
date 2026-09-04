---
name: gts-sept-base
description: 9月测试日报多维表格Base：token、5表ID、字段结构(m_/b_/s_口径)、公式、21支素材清单、工作流
metadata: 
  node_type: memory
  type: project
  originSessionId: 2bbc92dd-b0de-4136-87f6-f540cb053eb7
  modified: 2026-09-03T02:14:18.589Z
---

# GTS 9月测试日报 Base（已建）

## Base 信息

- URL：https://my.feishu.cn/base/Th4mbjeijaa24Ls0Afsc9HjMnZb
- Token：`Th4mbjeijaa24Ls0Afsc9HjMnZb`
- 时区：America/Los_Angeles
- 旧 7月 Base（保留历史）：`AB1bbDRrSaioVas5w07cr7qInth`

## 5 张表

| 表 | Table ID | View ID | 字段数 | 用途 |
|----|----------|---------|--------|------|
| 素材日报 | tblT4pnDbUijyPON | vewvhHvYSF | 45 | 每日素材明细（核心，按[日期,出价方式]分组） |
| 每日汇总 | tblVM5S1fzbLtlCV | vewTuCgvqq | 34 | 每日整体数据（无核心结论） |
| 财务汇总 | tblTeGaMJslljB02 | vewKZqChEW | 35 | 对财务（含备注） |
| 问题追踪 | tblIeXUbxOjZs2hb | vewpBKC6Q2 | 9 | 关停/异常（含严重度） |
| 每日结论 | tblbmSSTInGtwSL8 | vewJzTjBfK | 8 | 定性判断（含环比/达标情况） |

仪表盘：`blknu7znDEsBZIxd`（install投放日报总览，6 图表）

## 字段顺序（口径：m_ 最前 → b_ 中间 → s_ 最后）

**素材日报 45 字段：**
1. 维度 7：日期、出价方式(install/AEO)、国家(美国/菲律宾)、素材类型(V视频/P图片)、素材名称、素材方向(9值)、标记(🟢🟡🔴)（已删 Campaign/Ad Set，素材维度不需要）
2. m_ 媒体 9：m_花费、m_展示、m_点击、m_CTR、m_CPC、m_CVR、m_CPM、m_安装、m_CPI（均 Meta 源直接给）
3. b_ BI 11：b_安装(dnu)、b_CPI、b_r1_cnt、b_r3_cnt、b_r7_cnt、b_R1、b_R3、b_R7、b_次留成本、b_3留成本、b_7留成本
4. s_ Singular 11：s_安装(Installs)、s_CPI(eCPI)、s_r1_cnt、s_r3_cnt、s_r7_cnt、s_R1、s_R3、s_R7、s_次留成本、s_3留成本、s_7留成本
5. 7月基线 6：7月CPI、7月CPM、7月CTR、7月CVR、7月D1、7月D3
6. 备注 1

**每日汇总 34 字段** = 日期+国家 + m_9 + b_11 + s_11（已删核心结论，结论移到每日结论表）
**财务汇总 35 字段** = 每日汇总 + 备注

## 公式（飞书 Base 自动算）

- b_CPI = `ROUND([m_花费]/[b_安装],2)`
- b_R1/R3/R7 = `ROUND([b_r*_cnt]/[b_安装]*100,2)`
- b_次留/3留/7留成本 = `ROUND([m_花费]/[b_r*_cnt],2)`
- s_R1/R3/R7 = `ROUND([s_r*_cnt]/[s_安装]*100,2)`
- s_次留/3留/7留成本 = `ROUND([m_花费]/[s_r*_cnt],2)`

## 素材清单（21 支，已按 9月文档预填 + 标记🟡观察 + 素材方向）

**权威来源**：9月测试计划文档 https://my.feishu.cn/docx/LeB6dpLgJoiUy1xhxPPcf9PinFc （docx_token `LeB6dpLgJoiUy1xhxPPcf9PinFc`）

| 素材方向 | 素材 |
|---------|------|
| 视频-黑帮入会/氛围 | V-浴血黑帮、V-浴血黑帮-叙事迭代 |
| 视频-角色展示/招募 | V-招募表演、V-立绘展示-斩神片头 |
| 视频-复仇逆袭 | V-晋级失败被捕、V-无厘头擦边 |
| 视频-战斗 | V-玩法展示-打丧尸、V-鸡公大侠 |
| 图片-角色展示 | P-门徒立绘-单人、P-门徒立绘-多人 |
| 图片-美漫分镜 | P-美漫分镜、帮派火拼、地盘争夺 |
| 图片-幽默经营 | P-炸鸡店、P-披萨店、P-炸鸡店迭代 |
| 图片-擦边/命运反转 | P-黑帮经营-擦边、P-美漫分镜-角色升级 |
| 清洁复测 | V-模拟经营原版、V-爽感战斗、V-特殊设备视角 |

视频 8 + 图片 10 + 清洁复测 3 = 21 支。

⚠️ 命名已按 9月文档修正（vs 7月旧名）：
- 帮派火并 → **帮派火拼**
- 模拟经营(原版) → **模拟经营原版**（无括号）

**10 支有 7月基线**（7月CPI/CPM/CTR/CVR/D1/D3 已填，见 [[gts-july-baseline]]）：浴血黑帮、招募表演、晋级失败被捕、鸡公大侠、美漫分镜、炸鸡店、披萨店、模拟经营原版、爽感战斗、特殊设备视角
**11 支新素材**基线留空：其余

## 工作流（测试开始后每日）

1. 用户发 3 口径源 Excel（Meta/BI/Singular）
2. 我解析 → 映射素材名（新命名规范按位置截取）→ 填素材日报（m_/b_/s_ 数据 + 日期/国家/Campaign/Ad Set）
3. 填每日汇总（按日期×国家汇总）、财务汇总
4. 写简报对齐 → 回填每日结论、问题追踪
5. 留存 R1/R3/R7 当天可能无数据，后续回填

## 口径规则

- 花费看 m_（媒体账本）；安装三口径并列；留存/成本以 b_ 为主、s_ 辅助
- 本次只有 Install（无 AEO），国家大概率美国（可能菲律宾）
- 关停：CPI>$4.75($3.8×1.25)且量级≥15 → 关；花费>$50且激活0 → 关；DNU<20 不关

**Why**: 9月测试的日报 Base 已建好，后续每日填数据需要知道表 ID、字段映射、公式、口径规则。
**How to apply**: 收到 9月源数据后，按字段映射填素材日报；关联 [[gts-daily-workflow]]（旧工作流）、[[gts-july-baseline]]（7月基线）、[[gts-sept-test]]（测试计划）。
