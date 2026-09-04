---
name: huanchong-project-master
description: 幻宠项目总索引 — 所有数据源位置、Token、子表结构和业务理解
metadata: 
  node_type: memory
  type: project
  space_id: "7656641498817301704"
  space_name: 幻宠
  space_url: https://my.feishu.cn/wiki/space/7656641498817301704
  originSessionId: f63dd5e3-cd6e-49fc-ade6-70e0e7f3f19a
  modified: 2026-07-22T06:36:35.573Z
---

# 幻宠项目 — 完整索引

## 项目概要

产品名：幻宠帝国 / Palkie Empire / Monster Survival: Palkie Empire
包名：com.umi.palkie
发行：UMI Game (service@umi.game)
类型：宠物养成 + 模拟经营 + 战斗 RPG
引擎：Unity (推测)
目标市场：美国为主，巴西/印尼/法国/泰国/德国为辅
Android 最低要求：6.0+, 4GB RAM+

## 版本迭代线 (25.8 — 26.7)

| 时期 | 版本 | 关键内容 |
|------|------|---------|
| 25.8-11月 | 早期开发 | 核心系统搭建 |
| 25.12月 | 模拟经营一期 | 经营玩法引入 |
| 26.1月 | 模拟经营二期 | 经营深化 |
| 26.2月 | 模拟经营完善期 | 优化打磨 |
| 26.3月 | 次留测试版 | 留存验证 |
| 26.4-5月 | 商业化测试版 | 首次投放测试(v4) |
| 26.5月 | v5.8/v5.15 | 版本迭代(bug修复) |
| **26.6月** | **商业化测试** | **⭐ 6/11测试(v6)** |
| 26.7月 | 商业化测试 | 当前版本 |

## 核心业务数据（已读入记忆）

### 投放KPI摘要 (6/11测试)
- 总花费 $12,910 / 1,708安装 / CPI $7.56 / R1 26-29% / R4 8-10%
- Install出价: 26条素材 / 5方向 / CPI $7.25
- AEO出价: 5条通用素材 / CPI $8.50
- 最佳素材: P-宠物展示-合成3D ($4.37 CPI / 292安装 / R1 25.72%)
- 详见 [[huanchong-611-test]]

### 竞品矩阵
- 19款竞品，核心对标: Palmon Survival(莉莉丝), 曙光重临(4399), Monmate Master, Kingshot(点点), 无尽冬日
- 详见 [[huanchong-competitors]]

### 早期投放测试 (1-4月)
- 1月吸量测试 → 2月画风测试 → 4月留存测试，三次完整报告
- 核心结论: 最佳素材「剧情抓宠→战斗升级→打BOSS」、新画风>旧画风、美国CPI $3.91
- ⭐ 完整飞书文档: https://my.feishu.cn/wiki/SUoOwHLUTi6DNIkt2mAc25OJnuL
- 详见 [[huanchong-early-tests]]

### V1 首测运营总结 (1月)
- DNU 943 / R1 16.76% / SDK漏斗98.3% / Icon AB小火熊胜出 / 本地化4.8w字
- 运营视角，非UA投放视角
- 详见 [[huanchong-v1-launch]]

### 宠物编号体系
- 帕基: 策划编号(30xxx/20xxx) + 美术编号(10xxx) + UI资源路径
- 啾啾: 盾兵/矛兵/弓兵 3类
- 训练师: 6人(Luna/Michel/Bob/Frank/Diana/Tracey)
- 建筑: 民居/木材厂/石矿厂/水晶厂/弓兵营/竞技场等
- 详见 [[huanchong-palkie-numbering]]

---

## 数据源导航（按需查询时使用）

### 1. 6月11日幻宠测试 (核心投放数据)
Token: Bnkpsh602hZL49t39cTcT1f4nBq
12子表:

| 子表 | ID | 查什么 |
|------|-----|--------|
| 宏观数据 | f4df9b | 总KPI、分日/渠道/方向/广告系列汇总 |
| 素材详细 | g1B304 | 26条素材×渠道×v4v6对比(392行) |
| 详细的 | FfBRvO | **素材级R1+次留成本**(27行) |
| 整理表 | z89zqR | 素材级投放数据含广告组维度 |
| 新手通过率 | s0kcrV | 76步事件漏斗 |
| 宏观数据-留存 | azRg8b | DNU/R1-R4分渠道 |
| 素材ID | sdS2H6 | Creative ID ↔ 素材名映射(253行) |
| 素材数据 | wxeEC6 | 素材方向概览 |
| 商店图 | kzE5Vh | 商店页链接 |
| singular | 8Ywe0s | Singular归因数据(分日/分渠道R1-R3) |
| 工作表1 | UtRKCG | v4 vs v6历史对比 |
| 工作表2 | fQXwNe | 四类出价汇总 |

### 2. 帕基S编号表
Token: LveEspQ1KhngN9tbqO9cmmbYnuc

| 子表 | ID | 查什么 |
|------|-----|--------|
| 帕基编号 | 4fb51b | 宠物全量编号(策划号+美术号+UI路径+品阶) |
| 啾啾编号 | 4jdfEm | 盾兵/矛兵/弓兵编号 |
| 建筑编号 | qBBeOA | 129列, 全建筑编号 |
| 训练师编号 | urcKlR | 训练师ID+职业 |

### 3. Event埋点 (⚠️未读)
Token: RFhUseMOZhsHR3tY07CcEV8GnGc
7子表: 游戏自定义Event / 游戏_Event_info(746行) / Facebook_Event / Event_概念 / SDk预埋Event / Event_参数 / App启动
> 需要时用 lark-cli +csv-get 读取

### 4. 版本记录表
Token: JifOsRYWBhqHkWtbva8cfr9UnSb
3子表: 目录(版本历史) / 5.8(3个bug) / 5.15(1个bug)

### 5. 项目版本管理 (⚠️仅读结构)
Token: WSA4b6vvVa4A66sybEtchu4Knxh
17个表: 按月/功能划分的版本管理表
> 需要时用 lark-cli base +base-block-list 查看, +data-query 查具体内容

### 6. 商店信息收集
Token: WnDisE4RihNMnOte9xocXGiXn0b

| 子表 | ID | 查什么 |
|------|-----|--------|
| 商店信息收集对比 | abc4f6 | 竞品商店页对比(ICON/描述/卖场图) |
| 宝可梦常见使用名词 | fKT086 | 7个关键词(Evolution/Breeding等) |
| 幻宠帝国版本宠物 | 7wNqsg | 当前版本宠物清单(数据稀疏) |
| Icon宠物初筛 | PsVKH5 | 6只宠物推荐顺位(格林邦尼/呆呆噶/浪巴拉等) |

### 7. 商店素材需求
Token: JktrsDobKhhoyotDrb4cbzwznqi

| 子表 | ID | 查什么 |
|------|-----|--------|
| 素材需求 | 9eca31 | 9张商店图设计brief(含文案/尺寸) |
| 素材调整 | q3kcDJ | (未读) |

### 8. 美术需求
Token: HlDps8cRVhAPM0tqCl5cp1danzg

| 子表 | ID | 查什么 |
|------|-----|--------|
| 6月11日测试-视频 | 4e614e | 15条视频素材清单(含文件名/角色/标签) |
| 6月11日测试-图片 | phhotK | 10张图片素材需求brief(含文案/角色) |

### 9. 竞品说明
Token: T4u4smQCfhJZsst2hhFcgLFHnHf

| 子表 | ID | 查什么 |
|------|-----|--------|
| 目录 | 3805ec | 19款竞品总表(发行公司/收入/下载量) |
| 我的农场 | WfSnHc | 我的农场分析(经营原型参考) |
| 闪耀吧！噜咪 | TahdDj | (未读) |
| 曙光重临 | V5rVm2 | ⭐核心竞品: 4399曙光/Catch&Build, SLG+宠物, 国内次留45%/付费8.7% |
| Monmate Master | zF4JWb | 放置挂机版, 同4399发行 |
