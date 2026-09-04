---
name: gts-daily-workflow
description: GTS 3留测试日报工作流：Base结构、字段映射、公式、简报模板、关停规则、样本量豁免
metadata: 
  node_type: memory
  type: project
  originSessionId: f94c6671-c0c4-4944-8005-9b4c8ba02b4e
  modified: 2026-08-09T10:01:24.423Z
---

# GTS 日报工作流

## 核心资源

| 资源 | 链接 |
|------|------|
| Base | https://my.feishu.cn/base/AB1bbDRrSaioVas5w07cr7qInth |
| 简报文档（精简版·汇报用） | https://my.feishu.cn/docx/NBRWdtCdZoQK8cxBb7JcT6BHnVg |
| 规划文档（基准线/关停规则） | https://my.feishu.cn/docx/EAfodj2sxoH0qExR9Jlc1M0JnWg |

## Base 4 张表

| 表名 | Table ID | 用途 |
|------|----------|------|
| 素材日报 | tblpZCaUwU1nQ7Jg | 23素材×N天，每日每条素材 Meta+BI 数据 |
| 每日汇总 | tblaU00Y2nJoAVWq | 每天 Install/AEO 两行汇总 |
| 问题追踪 | tblQrYvO1LzcVDzi | 关停/异常素材追踪 |
| 每日结论 | tblG6HfYXINFln1N | 给王总/秦总/制作人的汇报浓缩版 |

## 素材日报字段

### 手工填写字段

| 字段 | Field ID | 来源 |
|------|----------|------|
| 花费 | fldDWbuq8I | Meta 报表 |
| 展示 | fldQ8kAbDp | Meta 报表 |
| 点击 | fldHtgOnSN | Meta 报表 |
| 安装_Meta | fldINgBUhw | Meta 报表 |
| 安装_BI | fldqMAYZWJ | BI/Singular 后台 dnu |
| D1次留率(BI) | fldqnoLVJI | BI/Singular 后台 R1 |
| D3三留率(BI) | fldlg6lSVu | BI/Singular 后台 R3 |
| 标记 | fldfFlWDgG | 🟢正常/🟡观察/🔴关停 |
| 备注 | fldFhol1Fn | 需要解释的异常 |

### 公式字段（自动计算）

| 字段 | Field ID | 公式 |
|------|----------|------|
| CTR % | fldhx3ZKXh | ROUND(点击/展示*100,2) |
| CVR % | fldrjY0zqn | ROUND(安装_Meta/点击*100,2) |
| CPC | fldgPsQ7l2 | ROUND(花费/点击,2) |
| CPM | fldqDK6Dmo | ROUND(花费/展示*1000,2) |
| CPI_Meta | fld2wgjBfo | ROUND(花费/安装_Meta,2) |
| CPI_BI | fldOKculwE | ROUND(花费/安装_BI,2) |

### 静态字段（已预填，不动）

日期 fldDdARvIl、素材名称 fld2zpLyGj、出价方式 fldwqRJsxa、优先级 fldluFIoJx、Meta素材文件名 fldxapOjmf、4月CPI fld6RHdxpH、4月CPM fldpQAJ25v、4月CTR fldLQytnmO、4月CVR fldshXlHDM

## 每日汇总字段

- 总花费 fldJt6Q6jJ、总安装 fldKe2LwXX
- CPM_Meta fld2zxSbgm、CTR_Meta fldS9wRqJ6、CVR_Meta fldNP4BjfN
- 核心结论 fldH1Ldzez、D1次留率 fldq6kluZE
- 公式字段 CPI fldX2xDX6x 自动计算

## KPI 基准

### Install

| 指标 | 优秀 | 合格 | 待改进 | 4月基线 |
|------|------|------|--------|---------|
| CPI | ≤$1.50 | $1.50-2.80 | >$2.80 | $1.58 |
| D1次留 | ≥30% | 25-30% | <25% | 21.29% |
| D3三留 | ≥13% | 10-13% | 8-10% | 7.68% |

### AEO

| 指标 | 优秀 | 合格 | 待改进 | 4月基线 |
|------|------|------|--------|---------|
| CPI | ≤$2.00 | $2.00-2.60 | >$2.60 | $2.30 |
| D1次留 | ≥35% | 30-35% | <30% | 30.14% |
| D3三留 | ≥15% | 12-15% | 10-12% | 10.42% |

## 标记规则

| 标记 | 判断条件 |
|------|----------|
| 🟢 正常 | CPI 合格 + D1次留合格或以上；或样本<20 DNU无法下结论 |
| 🟡 观察 | CPI 接近超标边界 或 D1次留擦线；默认状态 |
| 🔴 关停 | 素材已关闭，停止投放 |
| ⚠️ 0激活 | 花费>阈值（Install $50 / AEO $80）且激活=0 |

> 标记是用户手动判断的运营决策，不是自动计算。导入数据时默认标 🟡，用户自己改。

## 关停规则

| 出价 | 条件 | 动作 |
|------|------|------|
| Install | 花费>$50 且 激活=0 | 关停 |
| Install | CPI>$3.50 达到一定量级 | 关停 |
| AEO | 花费>$80 且 激活=0 | 关停 |
| AEO | CPI>$4.00 达到一定量级 | 关停 |
| AEO | D1次留 < 同素材 Install D1次留 | 关停（AEO 无增益） |

### 样本量豁免

- 单条 DNU < 20：不下 🔴，标 🟡
- 不基于 DNU<20 的数据做关停决策
- 简报里可以提"样本太小不判断"

## 完整工作流（三步）

### 第一步：填数据

1. 用户发 Excel
2. 读 install 素材层级数据 + AEO 素材层级数据 sheet
3. 逐条填入素材日报：
   - 花费、展示、点击、安装_Meta（Meta 报表）
   - 安装_BI（BI/Singular 留存数据，通过 BI媒体id素材映射 桥接）
4. 读每日汇总 → 填总花费/总安装/CPM_Meta/CTR_Meta/CVR_Meta

### 第二步：写简报 → 和用户对齐

在精简简报文档追加当日段落。**先写简报，确认后再回填表格。**

### 第三步：回填表格（简报确认后）

- 每日汇总 → 核心结论字段
- 问题追踪 → 触发关停/异常的素材建记录
- 每日结论 → 一句话结论 + 向好信号 + 警惕信号 + 明日动作
- 素材日报 → 补「备注」

## 简报模板（精简汇报版）

```xml
<h1>7月X日（US DayN）</h1>
<p><b>总结：[一句话核心判断]</b></p>
<p><b>vs 前日：[环比关键指标变化]</b></p>
<callout emoji="💡">
<p><b>投放操作：</b>[当天做了什么投放调整/为什么/预期效果]</p>
</callout>
<h2>概览</h2>
<p>[2-3句：花费/安装/预算执行率/数据缺口]</p>
<h2>达标</h2>
<p><b>Install CPI $X.XX。</b>[判断]</p>
<p><b>AEO CPI $X.XX。</b>[判断]</p>
<h2>异常</h2>
<ul><li>...</li></ul>
<h2>排名</h2>
<h3>Install</h3>
<p><b>Top：</b>① 名(T层) $CPI/DNU ② ... ③ ...</p>
<p><b>Bottom：</b>名(T层) $CPI · 名 $CPI · 名 $CPI</p>
<h3>AEO</h3>
<p><b>Top：</b>...</p>
<p><b>Bottom：</b>...</p>
<h2>版位</h2>
<p><b>Install：</b>[1-2句]</p>
<p><b>AEO：</b>[1-2句]</p>
<h2>人群</h2>
<p>[1段]</p>
<h2>动作</h2>
<ol><li>...</li></ol>
```

### 写作风格

- **短句**：一句一个意思，不超过 30 字
- **观点先行**：先结论再数据
- **数据只支撑观点**：不列数字清单
- **排名格式**：素材名(T层) $CPI/DNU，按出价方式分开 Install/AEO
- **禁用**：AI 套话（"值得关注""表现尚可"）、模板化结构、模糊词
- **样本不够就说样本不够**

## 问题追踪建记录规则

触发关停规则 → 必须建记录：

| 字段 | 填法 |
|------|------|
| 发现日期 | 当天 |
| 出价方式 | Install/AEO |
| 素材名称 | 与素材日报一致 |
| 问题类型 | CPI超标/0激活/留存不达标/CTR-CVR异常/环比波动大/其他 |
| 问题描述 | 用数据说话，如"花费$62，激活0，Install CPI无法计算" |
| 处理措施 | 关停/降预算/设spend limit/观察 |
| 状态 | 🔴待解决 → 🟡处理中 → 🟢已解决 |

## 每日结论字段

| 字段 | 内容 | 长度 |
|------|------|------|
| 一句话结论 | 当天最核心的判断 | 1-2句 |
| 向好信号 | 正面数据、超出预期、优于4月 | 2-4条 |
| 警惕信号 | CPI失控、留存垮、0激活、漏斗异常 | 2-4条 |
| 明日动作 | 按优先级排，每条一句话 | 3-5条 |

## 特殊判断规则

### Day1 特殊处理

- 冷启动第一天，FB 算法还在探索期
- CPI 偏高、0激活素材多是正常的
- Day1 关停判断更宽松，除非严重超标（CPI>$5+）

### D3 数据延迟

- Singular 留存数据通常延迟 1-2 天
- Day1 简报大概率没有 Singular 留存数据
- 明确标注"Singular 留存尚未回传，D1/D3 判断暂缺"

### 环比口径

- CPI 环比 = (当天CPI - 4月CPI) / 4月CPI
- D1 环比 = (当天D1 - 4月D1) / 4月D1
- 用直观方向描述："CPI 比 4 月高 20%"

## 7月二测日报模板补充

针对 7月测试，另有专门的日报模板 Excel：

- 文件：`C:/Users/yangxd/Desktop/GTS_第二次测试_日报模板.xlsx`
- 规则：`C:/Users/yangxd/Desktop/GTS_日报模板_生成规则.md`
- 分析逻辑对齐：`C:/Users/yangxd/Downloads/GTS3测试日报-分析逻辑对齐文档.md`

**Why**: 日报是 GTS 日常工作的核心交付物，需要把 Base 字段、公式、标记规则、简报模板、关停逻辑统一成可复用的 SOP。
**How to apply**: 收到 Excel 后按「填数据→写简报→回填表格」三步执行；所有定性判断先写简报对齐再入库。
