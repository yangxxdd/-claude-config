---
name: huanchong-daily-report-template
description: 幻宠9月日报模板 Base（复刻GTS模板）：URL、5表+仪表盘+简报结构、字段口径、待办（素材方向待用户清单）
metadata:
  type: project
  related: [[huanchong-project-master]], [[huanchong-9月-test-plan]], [[huanchong-611-test]]
---

# 幻宠 9月测试日报模板 Base

## Base 信息
- 名称：幻宠9月测试日报
- URL：https://my.feishu.cn/base/MPN4b2YpKa9pdAshFcucTIAEnnd
- base_token：`MPN4b2YpKa9pdAshFcucTIAEnnd`
- 来源：2026-09-03 用 `base +base-copy --without-content` 从 GTS「9月测试日报」（`Th4mbjeijaa24Ls0Afsc9HjMnZb`）复制结构，再适配幻宠。

## 结构（7 块，与 GTS 模板一致）
| 块 | 类型 | 说明 |
|----|------|------|
| 素材日报 | table | 45字段，视图按 `[日期,出价方式]` 两级分组 |
| 每日汇总 | table | 日期×国家，m_9+b_11+s_11+ID |
| 财务汇总 | table | 同每日汇总 + 备注 |
| 问题追踪 | table | 8维度（编号/素材/发现日期/问题类型/严重度/状态/处理措施/问题描述） |
| 每日结论 | table | 日期+一句话结论+环比+达标+向好+警惕+明日动作 |
| install投放日报总览 | dashboard | 6图：总花费/总安装/花费by素材/安装by素材/CPIby素材/次留R1by素材 |
| 每日简报 | docx | 骨架已写好，3天占位 |

## 三口径字段命名（沿用 GTS 规范）
- 前缀 `m_`(Meta)/`b_`(BI)/`s_`(Singular)；率字段带 `%`；公式字段自动算（全部 `ROUND(...,2)`）。
- 花费只看 m_；留存/成本以 b_ 为主、s_ 辅助；`b_CPI=ROUND([m_花费]/[b_安装],2)`。

## 已适配幻宠
- 历史基线 6 字段：`7月→6月`（6月CPI/CPM/CTR%/CVR%/D1%/D3%），依据测试计划「以6月为参照」。
- 国家=美国/菲律宾、出价方式=install/AEO、素材类型=V视频/P图片、标记=🟢🟡🔴 沿用。

## ⏳ 待办
- **素材方向 9 值**：仍是 GTS 黑帮方向（视频-黑帮入会/氛围…），待用户发 9 月素材清单后替换。
- 简报目标线/关停规则：见测试计划文档（用户 9/17–9/19 最终定）。

## 测试时间（2026-09-03 更新）
- 由「9/7-9/9 冒烟 + 9/10-9/12 方案」改为 **9/17–9/19 三天**。
- 测试计划文档：https://my.feishu.cn/wiki/UDqOwXaumizZzdk2o6icKLAjnCd
