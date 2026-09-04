# -*- coding: utf-8 -*-
"""生成 9/22 Day1 模拟源数据 + 各类 payload，并做自洽校验"""
import json

# 21 支素材：(名称, 方向, 类型, 花费, 展示, 点击, 安装Meta)
# 方向取值须在9值内；类型 V视频/P图片
MATS = [
    # 视频主导量 8
    ("V-浴血黑帮",           "视频-黑帮入会/氛围", "V视频", 152, 5600, 210, 46),
    ("V-浴血黑帮-叙事迭代",  "视频-黑帮入会/氛围", "V视频", 118, 4300, 150, 33),
    ("V-招募表演",           "视频-角色展示/招募", "V视频", 135, 5100, 175, 35),
    ("V-立绘展示-斩神片头",  "视频-角色展示/招募", "V视频", 108, 3900, 130, 27),
    ("V-晋级失败被捕",       "视频-复仇逆袭",     "V视频", 168, 6800, 270, 61),
    ("V-无厘头擦边",         "视频-复仇逆袭",     "V视频", 102, 3700, 120, 25),
    ("V-玩法展示-打丧尸",    "视频-战斗",         "V视频",  92, 3200,  98, 20),
    ("V-鸡公大侠",           "视频-战斗",         "V视频", 128, 4900, 190, 40),
    # 图片主导量 10
    ("P-门徒立绘-单人",      "图片-角色展示",     "P图片",  72, 8600, 140, 22),
    ("P-门徒立绘-多人",      "图片-角色展示",     "P图片",  66, 7800, 120, 18),
    ("P-美漫分镜",           "图片-美漫分镜",     "P图片",  88, 11000, 210, 34),
    ("帮派火拼",             "图片-美漫分镜",     "P图片",  62, 7200, 105, 15),
    ("地盘争夺",             "图片-美漫分镜",     "P图片",  52, 5800,  60,  0),
    ("P-炸鸡店",             "图片-幽默经营",     "P图片",  82, 12000, 220, 31),
    ("P-披萨店",             "图片-幽默经营",     "P图片",  76, 9000, 160, 21),
    ("P-炸鸡店迭代",         "图片-幽默经营",     "P图片",  70, 8800, 155, 20),
    ("P-黑帮经营-擦边",      "图片-擦边/命运反转","P图片",  60, 6800, 100, 14),
    ("P-美漫分镜-角色升级",  "图片-擦边/命运反转","P图片",  58, 6200,  88, 12),
    # 清洁复测 3
    ("V-模拟经营原版",       "清洁复测",          "V视频",  72, 2600,  95, 19),
    ("V-爽感战斗",           "清洁复测",          "V视频",  70, 2700, 110, 26),
    ("V-特殊设备视角",       "清洁复测",          "V视频",  64, 2300,  80, 16),
]

# 7月基线（10支有）：名称 -> (CPI, CPM, CTR%, CVR%, D1%, D3%)
BASELINE = {
    "V-浴血黑帮":      (3.58, 20.39, 3.19, 17.85, 28.99, 9.47),
    "V-晋级失败被捕":  (2.97, 18.17, 3.34, 18.33, 24.57, 11.43),
    "P-披萨店":        (3.65, 2.97,  0.56, 14.55, 23.44, 4.69),
    "V-招募表演":      (3.95, 18.48, 3.73, 12.53, 39.58, 16.67),
    "V-鸡公大侠":      (3.34, 21.29, 4.70, 13.56, 27.45, 5.88),
    "V-模拟经营原版":  (3.66, 23.71, 6.03, 10.74, 12.50, 8.33),
    "P-炸鸡店":        (2.70, 2.43,  0.47, 18.99, 22.03, 10.17),
    "P-美漫分镜":      (2.62, 10.26, 2.07, 18.97, 25.58, 2.33),
    "V-爽感战斗":      (2.70, 25.10, 4.62, 20.09, 8.57,  8.57),
    "V-特殊设备视角":  (3.93, 27.42, 4.69, 14.86, 17.39, 8.70),
}

def r2(x):
    return round(x, 2)

rows = []
for (name, direc, typ, cost, imp, click, inst) in MATS:
    ctr = r2(click / imp * 100) if imp else None
    cpc = r2(cost / click) if click else None
    cvr = r2(inst / click * 100) if click else None
    cpm = r2(cost / imp * 1000) if imp else None
    cpi = r2(cost / inst) if inst else None
    dnu = round(inst * 0.88) if inst else 0
    rows.append({
        "name": name, "direc": direc, "typ": typ,
        "cost": cost, "imp": imp, "click": click, "inst": inst,
        "ctr": ctr, "cpc": cpc, "cvr": cvr, "cpm": cpm, "cpi": cpi, "dnu": dnu,
        "base": BASELINE.get(name),
    })

# 校验 + 汇总
tot_cost = sum(r["cost"] for r in rows)
tot_imp = sum(r["imp"] for r in rows)
tot_click = sum(r["click"] for r in rows)
tot_inst = sum(r["inst"] for r in rows)
tot_dnu = sum(r["dnu"] for r in rows)
print("=== 9/22 Day1 模拟源数据（21支素材） ===")
print(f"{'素材':<22}{'花费':>7}{'展示':>7}{'点击':>6}{'安装':>5}{'CTR%':>7}{'CPC':>6}{'CVR%':>7}{'CPM':>7}{'CPI':>7}{'dnu':>5}")
def f(v, w):
    return f"{v:>{w}}" if v is not None else f"{'':>{w}}"

for r in rows:
    print(f"{r['name']:<22}{r['cost']:>7}{r['imp']:>7}{r['click']:>6}{r['inst']:>5}"
          f"{f(r['ctr'],7)}{f(r['cpc'],6)}{f(r['cvr'],7)}{f(r['cpm'],7)}{f(r['cpi'],7)}{r['dnu']:>5}")
print("-" * 90)
print(f"{'合计':<22}{tot_cost:>7}{tot_imp:>7}{tot_click:>6}{tot_inst:>5}"
      f"{r2(tot_click/tot_imp*100):>7}{r2(tot_cost/tot_click):>6}{r2(tot_inst/tot_click*100):>7}"
      f"{r2(tot_cost/tot_imp*1000):>7}{r2(tot_cost/tot_inst):>7}{tot_dnu:>5}")
print(f"\n整体 m_CPI = {r2(tot_cost/tot_inst)}  整体 dnu = {tot_dnu}  (dnu/安装 = {r2(tot_dnu/tot_inst*100)}%)")
print(f"预算执行率 = {r2(tot_cost/2000*100)}%（预算 $2000）  DNU达成率 = {r2(tot_dnu/800*100)}%（目标 800）")

# 关停判断
print("\n=== 关停/观察判断 ===")
for r in rows:
    flag = ""
    if r["inst"] == 0 and r["cost"] > 50:
        flag = "🔴 关停（花费>$50 且 0激活）"
    elif r["cpi"] is not None and r["cpi"] > 4.75 and r["inst"] >= 15:
        flag = "🔴 关停（CPI>$4.75 且量级≥15）"
    elif r["cpi"] is not None and r["cpi"] > 4.75:
        flag = "🟡 观察（CPI>$4.75 但量级<15，不关）"
    elif r["inst"] == 0:
        flag = "🟡 观察（0激活但花费≤$50）"
    if flag:
        print(f"  {r['name']:<22} {flag}")

json.dump(rows, open("day1_rows.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("\n已保存 day1_rows.json")
