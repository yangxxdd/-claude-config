#!/usr/bin/env python3
"""Build the creative performance table for 4月/6月 tests, US only."""

import json

# ============================================================
# April US - AEO per-creative data (from sheet 8HCs2U)
# Source: spreadsheet Z0l2s2bs1he1TotM2ERcgBNHnEf
# Singular: attribution data | Facebook: platform data
# ============================================================
april_aeo = [
    # 素材名称, 类型, 次留, 激活_Singular, 花费_Singular, 激活_FB, CPI_FB, CVR, CTR
    ("V-抓宠战斗",     "V", "38.71%", 62,  459.97, 80,  5.75, "40.61%", "0.85%"),
    ("P-海啸",        "P", "40.00%", 60,  441.36, 81,  5.45, "23.48%", "2.04%"),
    ("V-场景展示",     "V", "20.00%", 10,   93.31, 11,  8.48, "34.38%", "1.04%"),
    ("P-幻想宠物3",    "P", "20.00%",  5,   50.98,  9,  5.66, "21.95%", "1.45%"),
    ("V-核心玩法",     "V", "20.00%",  5,   42.51,  7,  6.07, "33.33%", "1.09%"),
    ("V-天灾重建-长版", "V", "50.00%",  4,   34.48,  4,  8.62, "23.53%", "1.61%"),
]

# April US Install - only AGGREGATE data available
# From sheet CcOUZ6: 541 installs (FB), CPI $3.91, 次留 28.90%
# Per-creative breakdown NOT available in source data

# ============================================================
# April US - Install creatives mentioned in doc text (no exact numbers)
# ============================================================
april_install_creatives = [
    # 素材名称 (per doc: 留存最佳 >35%), 类型
    ("V-核心玩法",       "V"),
    ("V-高效抓宠",       "V"),
    ("P-灾后重建",       "P"),
    # 留存最差 (~15%)
    ("P-幻想宠物3",      "P"),
    ("帕基世界冒险",     "V"),  # pixel art
    # 吸量最佳 (CPI $3.3-$3.5)
    ("V-场景展示",       "V"),
    ("V-抓宠战斗",       "V"),
]

# ============================================================
# June US - per-creative data from 详细的 sheet (FfBRvO)
# Combined Install + AEO (not separated by bidding)
# ============================================================
june_detailed = [
    # 广告名称, 花费, 安装量, CPI, CTR, CVR, R1, R1人数
    ("P-宠物展示-合成 3D",    1277.41, 292, 4.37,  "1.65%", "19.76%", "25.72%", 71),
    ("V-宠物展示-宠物合成",    976.48, 142, 6.88,  "1.02%", "26.01%", "25.22%", 29),
    ("P-模拟经营-冬日写实",   1351.30, 130, 10.39, "1.27%", "14.67%", "18.52%", 20),
    ("V-帕萌战斗-杀宠复刻",    912.48,  83, 10.99, "1.58%", "18.32%", "25.00%", 16),
    ("P-抓宠经营-超梦",        374.38,  79,  4.74, "1.42%", "25.65%", "28.13%", 18),
    ("V-抓宠经营-捕捞竞品",    272.44,  70,  3.89, "1.59%", "32.26%", "21.82%", 12),
    ("P-抓宠经营-幽飘",        473.00,  54,  8.76, "0.94%", "21.77%", "34.09%", 15),
    ("V-抓宠经营-售卖帕基",    383.06,  43,  8.91, "1.23%", "23.89%", "30.77%", 12),
    ("V-帕萌战斗-雪地竞品",    276.61,  37,  7.48, "3.06%", "12.17%", "33.33%", 13),
    ("P-宠物展示-二阶进化",    106.65,  29,  3.68, "2.40%", "15.85%", "31.03%",  9),
    ("P-抓宠经营-虐待",        150.37,  20,  7.52, "1.81%", "13.61%", "37.50%",  6),
    ("V-帕萌战斗-出狱打鸡",    153.22,  17,  9.01, "1.07%", "25.37%", "40.00%",  6),
    ("V-帕萌战斗-群殴打鸡",    114.96,  14,  8.21, "3.44%", "11.86%", "52.94%",  9),
    ("V-模拟经营-温馨",        100.78,  12,  8.40, "1.23%", "23.08%", "37.50%",  3),
    ("P-宠物展示-帕基战斗",     76.26,  11,  6.93, "1.12%", "18.33%", "10.00%",  1),
    ("P-模拟经营-建造成长",    156.68,  11, 14.24, "1.34%", "10.78%", "25.00%",  2),
    ("V-模拟经营-帕基玩法寒霜", 192.73,  10, 19.27, "1.90%",  "7.58%", "40.00%",  4),
    ("V-抓宠经营-拯救可达鸭",  168.85,   9, 18.76, "3.41%",  "6.08%", "20.00%",  2),
    ("P-宠物展示-巨物",         77.95,   7, 11.14, "1.51%", "13.21%", "33.33%",  2),
    ("V-宠物展示-二阶合成",     32.92,   6,  5.49, "1.26%", "27.27%", "16.67%",  1),
    ("V-模拟经营-七日建造",     84.70,   6, 14.12, "1.63%", "13.95%",  "0.00%",  0),
    ("V-模拟经营-砍树",        115.65,   5, 23.13, "0.72%",  "7.69%",  "0.00%",  0),
    ("V-抓宠经营-狐狸",         77.60,   5, 15.52, "2.73%",  "7.69%", "20.00%",  1),
    ("V-抓宠经营-虐待",         19.89,   5,  3.98, "4.43%", "15.63%", "50.00%",  2),
    ("V-帕萌战斗-合成狙击",     24.95,   4,  6.24, "2.41%", "17.39%",  "0.00%",  0),
    ("P-抓宠经营-血腥",         42.37,   2, 21.19, "1.71%",  "7.41%",  "0.00%",  0),
]

# ============================================================
# June - AEO-specific per-creative data (from z89zqR rows 35-40)
# These creatives ran AEO campaigns
# ============================================================
june_aeo_creatives = [
    # 广告名称, 花费, 安装量, CPI, CTR, CVR
    ("P-海啸",          1407.25, 166,  8.48, "1.23%", "25.00%"),
    ("V-场景展示",       142.27,  16,  8.89, "1.06%", "47.06%"),
    ("V-核心玩法",        76.73,   8,  9.59, "0.85%", "32.00%"),
    ("V-天灾重建-长版",   260.86,  31,  8.41, "0.96%", "43.06%"),
    ("V-抓宠战斗",       850.65, 101,  8.42, "0.70%", "40.08%"),
]

# ============================================================
# June - creatives identified as AEO from campaign names (z89zqR rows 54-63)
# ============================================================
# Campaigns:
# US-核心用户-AEO-tutorial_5_achieved: V-天灾重建-长版, V-抓宠战斗, P-海啸, V-场景展示, V-核心玩法
# US-核心用户-AEO-level_4_achieved: V-场景展示, V-抓宠战斗, V-核心玩法, V-天灾重建-长版, P-海啸

# ============================================================
# June retention by segment (from azRg8b)
# ============================================================
june_retention = {
    "US-AAA-install":       {"R1": "23.20%", "R2": "8.40%",  "R3": "8.40%"},
    "素材方向测试-0611":    {"R1": "26.35%", "R2": "15.04%", "R3": "9.34%"},
    "AEO":                  {"R1": "29.67%", "R2": "16.48%", "R3": "12.09%"},
}

# ============================================================
# Bidding method mapping for June creatives
# From campaign names in z89zqR:
#   AEO campaigns: US-核心用户-AEO-*
#   Install campaigns: US-AAA-install-*, 素材集合-*, etc.
# Creatives in both AEO and Install: V-天灾重建-长版, V-抓宠战斗, P-海啸, V-场景展示, V-核心玩法
# ============================================================
june_both_bidding = {"V-天灾重建-长版", "V-抓宠战斗", "P-海啸", "V-场景展示", "V-核心玩法"}

# Creatives that were ONLY in AEO campaigns: none unique (all 5 above also run Install)
# Creatives in AEO campaigns that also ran Install:
#   P-海啸 (also in US-AAA-install rows 99, 104)
#   V-场景展示 (also in US-AAA-install rows 65, 100)
#   V-抓宠战斗 (also in US-AAA-install rows 102, 106)
#   V-核心玩法 (also in US-AAA-install rows 103, 107)
#   V-天灾重建-长版 (also in US-AAA-install rows 64, 101)

# ============================================================
# June AEO per-creative install counts (from z89zqR section 3)
# These are approximate splits from campaign-level data
# ============================================================
june_aeo_install_split = {
    # Creative: {AEO_installs, Install_installs}
    # From z89zqR: AEO campaigns total + Install campaigns total
    # AEO total (from z89zqR rows 54-63): ~322 installs
    # Install total (from z89zqR rows 64-107): ~1,103 installs (素材-install) + ~283 installs (留存素材-install)
    "V-天灾重建-长版": {"aeo_installs": 31, "install_installs": 17},
    "V-抓宠战斗":     {"aeo_installs": 101, "install_installs": 85},
    "P-海啸":        {"aeo_installs": 166, "install_installs": 146},
    "V-场景展示":     {"aeo_installs": 16, "install_installs": 28},
    "V-核心玩法":     {"aeo_installs": 8, "install_installs": 3},
}

# ============================================================
# Build the final table
# ============================================================

def pct(s):
    """Parse percentage string to float."""
    if not s or s in ("/", "-", "#DIV/0!"):
        return None
    return float(s.replace("%", ""))

def fmt_pct(v):
    """Format float as percentage string."""
    if v is None:
        return "-"
    return f"{v:.2f}%"

def fmt_cpi(v):
    """Format CPI value."""
    if v is None:
        return "-"
    return f"${v:,.2f}"

rows = []

# ---- April AEO ----
for name, ctype, r1, act_s, spend_s, act_fb, cpi_fb, cvr, ctr in april_aeo:
    rows.append({
        "月份": "4月",
        "素材名称": name,
        "素材类型": ctype,
        "出价方式": "AEO",
        "安装数": act_fb,
        "CPI": cpi_fb,
        "R1": r1,
        "R3": "-",
        "R7": "-",
        "备注": f"Singular激活={act_s}, 花费=${spend_s:.2f}",
    })

# ---- April Install (aggregate only, creative names from doc) ----
# Note: exact per-creative numbers not available
april_install_summary = [
    # name, type, note
    ("V-核心玩法",       "V", "留存最佳(>35%), CPI $3.3-3.5"),
    ("V-高效抓宠",       "V", "留存最佳(>35%)"),
    ("P-灾后重建",       "P", "留存最佳(>35%)"),
    ("V-场景展示",       "V", "CPI $3.3-3.5"),
    ("V-抓宠战斗",       "V", "CPI $3.3-3.5"),
    ("P-幻想宠物3",      "P", "留存最差(~15%)"),
    ("V-帕基世界冒险",   "V", "留存最差(~15%), 像素风"),
]
for name, ctype, note in april_install_summary:
    rows.append({
        "月份": "4月",
        "素材名称": name,
        "素材类型": ctype,
        "出价方式": "Install",
        "安装数": "-",
        "CPI": "-",
        "R1": "-",
        "R3": "-",
        "R7": "-",
        "备注": f"仅汇总数据(整体541安装,CPI$3.91,R1=28.9%); {note}",
    })

# Add April Install aggregate row
rows.append({
    "月份": "4月",
    "素材名称": "【Install整体】",
    "素材类型": "-",
    "出价方式": "Install",
    "安装数": 541,
    "CPI": "$3.91",
    "R1": "28.90%",
    "R3": "-",
    "R7": "-",
    "备注": "541安装(FB), 436激活(Singular); 无每素材明细",
})

# Add April AEO aggregate row
rows.append({
    "月份": "4月",
    "素材名称": "【AEO整体】",
    "素材类型": "-",
    "出价方式": "AEO",
    "安装数": 192,
    "CPI": "$5.85",
    "R1": "36.99%",
    "R3": "-",
    "R7": "-",
    "备注": "AEO-tur7: R1=39.69%, CPI=$5.58; AEO-强制引导: R1=13.33%(已关停)",
})

# ---- June detailed ----
for name, spend, installs, cpi, ctr, cvr, r1, r1_count in june_detailed:
    # Determine bidding method
    bidding = "Install+AEO" if name in june_both_bidding else "Install"

    # For AEO-only, get the AEO-specific data
    aeo_data = next((a for a in june_aeo_creatives if a[0] == name), None)

    notes = []
    if name in june_both_bidding:
        split = june_aeo_install_split.get(name, {})
        aeo_i = split.get("aeo_installs", "?")
        ins_i = split.get("install_installs", "?")
        notes.append(f"AEO约{aeo_i}安装/Install约{ins_i}安装(合并行)")

    rows.append({
        "月份": "6月",
        "素材名称": name,
        "素材类型": name[0],  # P or V
        "出价方式": bidding,
        "安装数": installs,
        "CPI": f"${cpi:,.2f}",
        "R1": r1,
        "R3": "-",
        "R7": "-",
        "备注": "; ".join(notes) if notes else "",
    })

# Add June segment retention summary
rows.append({
    "月份": "6月",
    "素材名称": "【Install-旧商店页】",
    "素材类型": "-",
    "出价方式": "Install",
    "安装数": 250,
    "CPI": "-",
    "R1": "23.20%",
    "R3": "8.40%",
    "R7": "-",
    "备注": "R2=8.40%; US-AAA-install",
})
rows.append({
    "月份": "6月",
    "素材名称": "【Install-新商店页/素材方向】",
    "素材类型": "-",
    "出价方式": "Install",
    "安装数": 964,
    "CPI": "-",
    "R1": "26.35%",
    "R3": "9.34%",
    "R7": "-",
    "备注": "R2=15.04%; 素材方向测试-0611",
})
rows.append({
    "月份": "6月",
    "素材名称": "【AEO整体】",
    "素材类型": "-",
    "出价方式": "AEO",
    "安装数": 273,
    "CPI": "-",
    "R1": "29.67%",
    "R3": "12.09%",
    "R7": "-",
    "备注": "R2=16.48%; CPI $8.50预估",
})

# ============================================================
# Output
# ============================================================
print(f"Total rows: {len(rows)}")
print()

# Print summary
print("=" * 120)
print(f"{'月份':<4} {'素材名称':<24} {'类型':<4} {'出价方式':<10} {'安装数':>8} {'CPI':>10} {'R1':>8} {'R3':>8} {'备注'}")
print("-" * 120)

for r in rows:
    inst = r['安装数'] if isinstance(r['安装数'], str) else str(r['安装数'])
    cpi = r['CPI'] if isinstance(r['CPI'], str) else f"${r['CPI']}"
    print(f"{r['月份']:<4} {r['素材名称']:<24} {r['素材类型']:<4} {r['出价方式']:<10} {inst:>8} {cpi:>10} {r['R1']:>8} {r['R3']:>8} {r['备注']}")

print("=" * 120)

# Save as JSON for later xlsx creation
output = {"rows": rows}
with open(r"D:\claude-projects\projects\幻宠\creative_table_data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("\nData saved to creative_table_data.json")
