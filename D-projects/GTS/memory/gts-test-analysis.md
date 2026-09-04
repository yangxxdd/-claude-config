---
name: gts-test-analysis
description: GTS 两次测试数据（经Sheet逐单元格验证）、17支素材内容分析、素材方向结论
metadata:
  type: project
  originSessionId: a16f26ab-7427-49f0-bcdd-93494eadf471
---

# GTS 两次测试分析与素材方向

GTS (Gangland: Syndicate Rise) 是用户**唯一**负责海外投放的黑帮题材手游。

## 汇报结构
- 向**王总**(CEO)、**秦总**(COO)、**制作人**直接汇报
- 王总关注：战略方向、ROI、市场机会
- 秦总关注：执行进度、投放效率、成本控制
- 制作人关注：玩家数据、产品体验、用户反馈

## 数据来源（2026/05/12 经Sheet逐格验证）

- 2月吸量报告 Sheet：spreadsheet `HljIsZhGOhiccAt2vnpcJU3Kn4c`，sheet-id `erKbRv`(美国) `YU1hV6`(菲律宾) `hacBnh`(播放数据)
- 4月留存报告 Sheet：spreadsheet `JhDasabrthuYLht2ECwcpVXxnRb`，sheet-id `CfgROC`(install素材) `wb9oM0`(aeo素材) `o2aVka`(国家数据) `PUSvOb`(出价数据)
- **所有数字均从 Sheet 单元格直接读取，非正文概括，已逐格校对。**

## 买量效率（用户校对版）

| 指标 | 2月 | 4月 |
|------|-----|-----|
| 美国CPI | $1.89 | $1.86 |
| 美国激活 | 668 | 1,022 |
| 美国花费 | $1,260.85 | $1,905.59 |
| CVR | 19.6% | 23.3% |
| CPM | $8.37 | $18.49 |

## 留存（用户校对版）

| 指标 | 2月 | 4月 |
|------|-----|-----|
| 美国次留 | 19.36% | 27.56% |
| aeo次留 | — | 30.49% |
| 模拟经营aeo次留 | — | 36.44%（唯一达标） |
| 三留 | 9.12% | 12.27% |
| 衰减 | 52.89% | 55.47%（行业~41%） |
| 次留单价 | $10.42 | $7.28 |

## 素材方向结论（17支素材分析）

### 验证有效（两次都稳）
- **V-晋级失败被捕**：CPI $1.56-1.58，install次留25.81%。小丑等级命运反转剧情。
- **V-模拟经营**：2月CPI $1.47→4月$1.88，aeo次留36.44%。监狱→烹饪→抢劫荒诞循环。
- **P-炸鸡店**：2月CPI $1.37最低，4月install次留30.77%最高。图片素材，aeo次留19%→图片别走aeo。

### 4月新方向（信号强但量小）
- **V-浴血黑帮**：install CPI $1.14最低+次留30.23%，aeo CPI $1.40最低+次留50%。复古黑帮+赛博朋克。仅67 DNU。
- **V-爽感战斗**：install CPI $1.59，aeo次留30.36%。AOE+爆炸包装。≠战斗形式(录屏)。

### 淘汰
- **V-超速被抓**：install次留10.14%+aeo15.38%，量够。警匪追捕与核心玩法不匹配。
- **V-战斗形式**：2月CPI $2.64最贵，4月仅9 DNU。

### 待定
- V-场景展示：aeo次留28.21%不算差
- V-鸡公大侠：aeo次留29.41%但量小
- V-跟谁混：2月CPI $1.82吸量好但没测留存
- V-升级变装：CPI一直偏高

## 关键文件

- 测试对比+素材规划：`C:/Users/yangxd/友蜜/项目/gangland syndicate rise-GTS/两次测试对比与下一步素材规划.md`
- 飞书文档：https://my.feishu.cn/docx/LIEzdD14uoTSwPxDTvCcns37nad
- 测试素材目录：`C:/Users/yangxd/友蜜/项目/gangland syndicate rise-GTS/GTS测试素材/`（14视频+3图片）
- 素材分析：`analysis_batch1.md` `analysis_batch2.md` `analysis_batch3.md`

## 素材分析把握度
- 视频：Qwen VL 抽6帧分析，约75%把握度（漏节奏/转场/音效细节）
- 图片：完整读取，100%

## 用户写作偏好
- **反AI味**：不用"关键发现""核心结论""> 注"等公式化结构；短句口语化；观点先行
- **数据先验证再引用**：从Sheet单元格直接读取，不依赖正文概括

**Why:** 用户唯一负责的项目，所有工作围绕 GTS 展开。数据从 Sheet 逐格校对，Accuracy 是最高优先级。
**How to apply:** 当用户提到GTS、素材方向、测试数据时，先用这份已验证的数据，不要重新从飞书拉（可能再次读错表格）。素材内容参考 analysis_batch 文件。
