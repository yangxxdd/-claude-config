# -*- coding: utf-8 -*-
"""根据 day1_rows.json 构建素材日报/每日汇总/财务汇总/问题追踪/每日结论 的写入 payload"""
import json

rows = json.load(open("day1_rows.json", encoding="utf-8"))

DATE = "2026-09-22"

# ---------- 素材日报 batch-create ----------
FIELDS = ["日期", "出价方式", "国家", "素材类型", "素材名称", "素材方向", "标记",
          "m_花费", "m_展示", "m_点击", "m_CTR%", "m_CPC", "m_CVR%", "m_CPM", "m_安装", "m_CPI",
          "b_安装",
          "7月CPI", "7月CPM", "7月CTR%", "7月CVR%", "7月D1%", "7月D3%",
          "备注"]

mat_rows = []
for r in rows:
    mark = "🔴 关停" if (r["inst"] == 0 and r["cost"] > 50) else "🟡 观察"
    b = r["base"]
    note = ""
    if r["inst"] == 0 and r["cost"] > 50:
        note = "9/22 0激活，关停"
    elif r["cpi"] is not None and r["cpi"] > 4.75:
        note = f"CPI ${r['cpi']} 超 $4.75，量级<15 暂观察"
    mat_rows.append([
        DATE, "install", "美国", r["typ"], r["name"], r["direc"], mark,
        r["cost"], r["imp"], r["click"], r["ctr"], r["cpc"], r["cvr"], r["cpm"], r["inst"], r["cpi"],
        r["dnu"],
        b[0] if b else None, b[1] if b else None, b[2] if b else None,
        b[3] if b else None, b[4] if b else None, b[5] if b else None,
        note or None,
    ])

mat_payload = {"fields": FIELDS, "rows": mat_rows}

# ---------- 每日汇总 batch-create ----------
tot_cost = sum(r["cost"] for r in rows)
tot_imp = sum(r["imp"] for r in rows)
tot_click = sum(r["click"] for r in rows)
tot_inst = sum(r["inst"] for r in rows)
tot_dnu = sum(r["dnu"] for r in rows)
m_ctr = round(tot_click/tot_imp*100, 2)
m_cpc = round(tot_cost/tot_click, 2)
m_cvr = round(tot_inst/tot_click*100, 2)
m_cpm = round(tot_cost/tot_imp*1000, 2)
m_cpi = round(tot_cost/tot_inst, 2)

DAILY_FIELDS = ["日期", "国家", "m_花费", "m_展示", "m_点击", "m_CTR%", "m_CPC", "m_CVR%", "m_CPM", "m_安装", "m_CPI", "b_安装"]
daily_rows = [[DATE, "美国", tot_cost, tot_imp, tot_click, m_ctr, m_cpc, m_cvr, m_cpm, tot_inst, m_cpi, tot_dnu]]
daily_payload = {"fields": DAILY_FIELDS, "rows": daily_rows}

# ---------- 财务汇总 batch-create ----------
FIN_FIELDS = DAILY_FIELDS + ["备注"]
fin_rows = [[DATE, "美国", tot_cost, tot_imp, tot_click, m_ctr, m_cpc, m_cvr, m_cpm, tot_inst, m_cpi, tot_dnu,
             "9月模拟·美国install·未含税/退款/汇率"]]
fin_payload = {"fields": FIN_FIELDS, "rows": fin_rows}

# ---------- 问题追踪 batch-create ----------
ISSUE_FIELDS = ["编号", "素材名称", "发现日期", "问题类型", "严重度", "状态", "处理措施", "问题描述"]
issue_rows = [[
    "GTS-001", "地盘争夺", DATE, "0激活", "🔴 严重", "🔴 待解决", "关停",
    "9/22 花费 $52、安装 0（激活=0），触发关停线（花费>$50 且激活=0）"
]]
issue_payload = {"fields": ISSUE_FIELDS, "rows": issue_rows}

# ---------- 每日结论 batch-create ----------
CONC_FIELDS = ["日期", "一句话结论", "环比", "达标情况", "向好信号", "警惕信号", "明日动作"]
conc_rows = [[
    DATE,
    "Day1 冷启动：花费 $1895（预算94.8%），CPI $3.54 高于计划假设 $2.5，DNU 471 只到目标59%；CBO 开始强者吃量",
    "首日无前日",
    "CPI $3.54 落在合格线内($3.0-3.8)但偏高，未达计划 $2.5 假设；D1 次留待 9/23 回传",
    "晋级失败被捕 CPI $2.75、美漫分镜 $2.59、炸鸡店 $2.65 三支达优秀线($≤3.0)，CBO 已倾斜放量",
    "地盘争夺 0激活关停；图片组帮派火拼$4.13、美漫分镜-角色升级$4.83 多支 CPI 超 $3.8 线",
    "1. 关停地盘争夺 2. 美漫分镜-角色升级量级<15 暂观察、续投到 15 再判 3. 晋级失败被捕、美漫分镜、炸鸡店加量 4. 等 9/23 D1 回传再定标记",
]]
conc_payload = {"fields": CONC_FIELDS, "rows": conc_rows}

# ---------- 提取待删除的 roster 记录 ID ----------
rec = json.load(open("rec_素材日报.json", encoding="utf-8"))
d = rec.get("data", {})
roster_ids = d.get("record_id_list") or []
print("待删除 roster 记录数:", len(roster_ids))

# ---------- 保存 ----------
out = {
    "material": mat_payload,
    "daily": daily_payload,
    "finance": fin_payload,
    "issue": issue_payload,
    "conclusion": conc_payload,
    "delete_material_ids": roster_ids,
}
json.dump(out, open("day1_payloads.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

print("=== 每日汇总/财务汇总 汇总值 ===")
print(f"花费={tot_cost} 展示={tot_imp} 点击={tot_click} 安装={tot_inst} dnu={tot_dnu}")
print(f"CTR={m_ctr}% CPC={m_cpc} CVR={m_cvr}% CPM={m_cpm} CPI={m_cpi}")
print("素材日报行数:", len(mat_rows), "| 问题追踪:", len(issue_rows), "| 每日结论:", len(conc_rows))
print("已保存 day1_payloads.json")
