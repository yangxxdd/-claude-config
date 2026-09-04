---
name: gts-dashboard-setup
description: GTS 3留测试 · 完整工作流、字段映射、公式、简报模板、关停规则、Day2 生成指南
metadata:
  type: project
  originSessionId: e06abfa0-2cb6-477e-ae0b-649868f29284
---

# GTS 3留测试 · 工作流 & 数据地图

## 一、资源链接

| 资源 | 链接 |
|------|------|
| **Base** | https://my.feishu.cn/base/AB1bbDRrSaioVas5w07cr7qInth |
| **简报文档（精简版·汇报用）** | https://my.feishu.cn/docx/NBRWdtCdZoQK8cxBb7JcT6BHnVg |
| **旧简报（废弃）** | KRUrdzBUFostRWxgAHpcYHtmnwg |
| **规划文档（基准线/关停规则）** | https://my.feishu.cn/docx/EAfodj2sxoH0qExR9Jlc1M0JnWg |

## 二、4 张表

| 表名 | Table ID | 用途 |
|------|----------|------|
| 素材日报 | tblpZCaUwU1nQ7Jg | 23素材×N天，每日每条素材的 Meta+BI 数据 |
| 每日汇总 | tblaU00Y2nJoAVWq | 每天 Install/AEO 两行汇总 |
| 问题追踪 | tblQrYvO1LzcVDzi | 关停/异常素材追踪 |
| 每日结论 | tblG6HfYXINFln1N | 给王总/秦总/制作人的汇报浓缩版 |

## 三、素材日报 · 字段 ID 速查

### 手工填写字段

| 字段 | Field ID | 类型 | 来源 |
|------|----------|------|------|
| 花费 | fldDWbuq8I | number | Meta 报表 |
| 展示 | fldQ8kAbDp | number | Meta 报表 |
| 点击 | fldHtgOnSN | number | Meta 报表 |
| 安装_Meta | fldINgBUhw | number | Meta 报表 |
| 安装_BI | fldqMAYZWJ | number | BI 后台 dnu |
| D1次留率(BI) | fldqnoLVJI | number(%) | BI 后台 R1 |
| D3三留率(BI) | fldlg6lSVu | number(%) | BI 后台 R3 |
| 标记 | fldfFlWDgG | select | 🟢正常/🟡观察/🔴关停 |
| 备注 | fldFhol1Fn | text | 需要解释的异常 |

### 公式字段（自动计算，不能手工填）

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

## 四、每日汇总 · 字段

- 总花费 fldJt6Q6jJ、总安装 fldKe2LwXX
- CPM_Meta fld2zxSbgm、CTR_Meta fldS9wRqJ6、CVR_Meta fldNP4BjfN
- 核心结论 fldH1Ldzez、D1次留率 fldq6kluZE
- 公式字段 CPI fldX2xDX6x 自动计算

## 五、素材文件名 → 素材名称映射

Excel 的 Meta 素材文件名与 Base 的 素材名称 对应关系（23 条）：

**Install (14条):**
| Excel 文件名关键字 | Base 素材名称 |
|-------------------|--------------|
| install-GTS-2026-1-20-GTS-模拟经营-wxh | V-模拟经营（原版） |
| install-GTS-20270706-KOG-晋级失败被捕 | V-晋级失败被捕 |
| install-GTS-GTS-黑帮炸鸡店-hxj | P-炸鸡店 |
| install-GTS-2026-4-14-GTS-浴血黑帮 | V-浴血黑帮 |
| install-GTS-20260706-KOG-跟谁混 | V-跟谁混 |
| install-GTS-20260616-GTS爽感战斗 | V-爽感战斗 |
| install-GTS-2026-6-16-GTS-鸡公大侠改 | V-鸡公大侠 |
| install-GTS-20260616-GTS-模拟经营2 | V-模拟经营（新版） |
| install-黑帮披萨店-hxj | P-披萨店 |
| install-GTS-罪恶之城-hxj | P-美漫分镜 |
| install-GTS-20260617-GTS-赌场博弈 | V-赌场博弈 |
| install-GTS-2026-5-13-GTS-无人机视角 | V-特殊设备视角 |
| install-GTS-2026-6-17-GTS-招募表演 | V-招募表演 |
| install-GTS-20260706角色展示 | V-立绘展示 |

**AEO (9条):**
| Excel 文件名关键字 | Base 素材名称 |
|-------------------|--------------|
| AEO-GTS-2026-1-20-GTS-模拟经营 | V-模拟经营（原版） |
| AEO-GTS-2026-4-14-GTS-浴血黑帮 | V-浴血黑帮 |
| AEO-GTS-20260616-GTS爽感战斗 | V-爽感战斗 |
| AEO-GTS-2026-6-16-GTS-鸡公大侠改 | V-鸡公大侠 |
| AEO-GTS-20260616-GTS-模拟经营2 | V-模拟经营（新版） |
| AEO-GTS-20260617-GTS-赌场博弈 | V-赌场博弈 |
| AEO-2026-5-13-GTS-无人机视角 | V-特殊设备视角 |
| AEO-GTS-2026-6-17-GTS-招募表演 | V-招募表演 |
| AEO-20260706角色展示 | V-立绘展示 |

## 六、BI 广告 ID → Base 素材名称 映射

通过 Excel 的「BI媒体id素材映射」sheet 桥接。FB 广告 ID 是纯数字（如 52502964040663），对应 Base 素材名称。

## 七、KPI 基准 & 标记规则

### Install
| 指标 | 优秀 | 合格 | 待改进 | 4月基线 |
|------|------|------|--------|---------|
| CPI | ≤$1.50 | $1.50-2.80 | >$2.80 | $1.58 |
| D1次留 | ≥30% | 25-30% | <25% | 21.29% |

### AEO
| 指标 | 优秀 | 合格 | 待改进 | 4月基线 |
|------|------|------|--------|---------|
| CPI | ≤$2.00 | $2.00-2.60 | >$2.60 | $2.30 |
| D1次留 | ≥35% | 30-35% | <30% | 30.14% |

### 标记 = 广告素材运营状态（不是绩效打分）

- **🟡 观察**：默认状态，正常跑量中
- **🔴 关停**：素材已关闭，停止投放

> ⚠️ 标记是用户手动判断的运营决策，不是自动计算的。导入数据时默认标 🟡，用户自己改。

### 关停规则
- Install 花费>$50 且 激活=0 → 关停
- Install CPI>$3.50 达到一定量级 → 关停
- AEO 花费>$80 且 激活=0 → 关停
- AEO CPI>$4.00 达到一定量级 → 关停

### 样本量豁免
单条 DNU < 20：不下🔴，标🟡，不基于此做关停决策。

## 八、完整工作流（三步）

### 第一步：填数据
用户发 Excel → 读 install素材层级数据 + AEO素材层级数据 sheet → 逐条填入素材日报：
- 花费、展示、点击、安装_Meta（来自 Meta 报表）
- 安装_BI（来自 BI素材层级留存数据，通过 BI媒体id素材映射 桥接）

再读 每日汇总 → 填总花费/总安装/CPM_Meta/CTR_Meta/CVR_Meta。

### 第二步：写简报 → 和用户对齐
在精简简报文档（NBRWdtCdZoQK8cxBb7JcT6BHnVg）追加当日段落。**先写简报，确认后再回填表格。**

### 第三步：回填表格（简报确认后）
- 每日汇总 → 核心结论字段
- 问题追踪 → 触发关停/异常的素材建记录
- 每日结论 → 一句话结论 + 向好信号 + 警惕信号 + 明日动作

## 九、简报模板（精简汇报版）

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
<p><b>CVR相关分析。</b>[如需]</p>
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
<ol>...</ol>
```

### 写作风格
- **短句**：一句一个意思，不超过 30 字
- **观点先行**：先结论再数据
- **数据只支撑观点**：不列数字清单
- **排名格式**：素材名(T层) $CPI/DNU，按出价方式分开 Install/AEO
- **禁用**：AI 套话（"值得关注""表现尚可"）、模板化结构、模糊词
- **样本不够就说样本不够**

**Why**: 用户工作日用公司 Claude，周末用家里 Claude。本记忆通过 GitHub 同步，让两边分析逻辑一致。
**How to apply**: 收到 Excel → 按 §八工作流执行 → 简报追加到精简版文档 → 确认后回填 Base 表格。所有定性判断先写简报对齐再入库。
