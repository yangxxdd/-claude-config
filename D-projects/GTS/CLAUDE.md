# GTS 3留测试

## 项目定位
- 游戏项目 GTS 的 3 留测试，通过 Meta 广告投放验证素材效果
- 核心任务：每日填入素材数据 → 生成简报 → 汇报给王总/秦总/制作人

## 记忆体系

所有数据已存入本项目的记忆文件，启动后自动加载 MEMORY.md 索引。当前 4 个记忆文件：

| 文件 | 内容 |
|------|------|
| [[gts-dashboard-setup]] | ⭐ Base 结构/字段映射/公式/简报模板/工作流/关停规则 |
| [[gts-test-analysis]] | 2月+4月测试数据、17支素材方向分析、KPI 基准 |
| [[gts-competitive-analysis]] | 竞品分析：Mafia City/指尖无双/Gods Chaos 等 |
| [[gts-reference-files]] | 本地文件路径、飞书 URL、Sheet Token、lark-cli 命令 |

## 核心资源

| 资源 | 链接 |
|------|------|
| Base | https://my.feishu.cn/base/AB1bbDRrSaioVas5w07cr7qInth |
| 简报文档（汇报用） | https://my.feishu.cn/docx/NBRWdtCdZoQK8cxBb7JcT6BHnVg |
| 规划文档（基准线/关停规则） | https://my.feishu.cn/docx/EAfodj2sxoH0qExR9Jlc1M0JnWg |

## 4 张表
- 素材日报：23素材×N天，每日每条素材 Meta+BI 数据
- 每日汇总：每天 Install/AEO 两行汇总
- 问题追踪：关停/异常素材追踪
- 每日结论：给领导的汇报浓缩版

## 关键 KPI 基准

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

## 工作流
1. 收到 Excel → 读 install/AEO 素材层级数据 → 填入素材日报
2. 写简报（精简版文档 NBRWdtCdZoQK8cxBb7JcT6BHnVg）→ 和用户对齐
3. 确认后回填：每日汇总核心结论、问题追踪、每日结论

## 标记规则
- 🟡 观察：默认状态
- 🔴 关停：素材已关闭
- DNU < 20：不关停，标🟡

## 关停规则
- Install 花费>$50 且 激活=0 → 关停
- Install CPI>$3.50 → 关停
- AEO 花费>$80 且 激活=0 → 关停
- AEO CPI>$4.00 → 关停

## 注意事项
- 简报写作风格：短句、观点先行、禁用 AI 套话
- 详细字段映射和工作流见 memory/gts-dashboard-setup.md
