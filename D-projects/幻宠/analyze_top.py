import pandas as pd
import numpy as np
import sys
sys.stdout.reconfigure(encoding='utf-8')

cf = pd.read_excel('creative_final.xlsx', sheet_name='素材表现汇总')

cf['mat_name'] = cf['素材名称'].astype(str).str.strip()
cf['bid'] = cf['出价方式'].astype(str).str.strip()
cf['month'] = cf['月份'].astype(str).str.strip().str[:2]
cf['dnu'] = pd.to_numeric(cf['DNU'], errors='coerce')

data = cf[(cf['mat_name'].notna()) & (cf['mat_name'] != 'nan') &
          (~cf['月份'].astype(str).str.startswith('◆')) & (cf['R1'].notna())].copy()

# ============================================================
# PART 1: Materials in BOTH months with GOOD data (DNU >= 30 in both)
# ============================================================
pivot = data.groupby(['mat_name', 'bid']).agg(
    months=('month', 'nunique'),
    m4_dnu=('dnu', lambda x: x[data.loc[x.index, 'month'] == '4月'].sum()),
    m6_dnu=('dnu', lambda x: x[data.loc[x.index, 'month'] == '6月'].sum()),
).reset_index()

both = pivot[pivot['months'] == 2].copy()

print("=" * 120)
print("PART 1: 两次测试都数据好的素材 (DNU >= 30 in both months)")
print("=" * 120)

found_both_good = False
for _, bm in both.iterrows():
    name, bid = bm['mat_name'], bm['bid']
    r4 = data[(data['mat_name'] == name) & (data['bid'] == bid) & (data['month'] == '4月')]
    r6 = data[(data['mat_name'] == name) & (data['bid'] == bid) & (data['month'] == '6月')]

    if len(r4) == 0 or len(r6) == 0:
        continue

    dnu4, dnu6 = r4.iloc[0]['dnu'], r6.iloc[0]['dnu']
    r1_4, r3_4 = r4.iloc[0]['R1'], r4.iloc[0]['R3']
    r1_6, r3_6 = r6.iloc[0]['R1'], r6.iloc[0]['R3']
    cpi4, cpi6 = r4.iloc[0]['CPI'], r6.iloc[0]['CPI']

    both_reliable = dnu4 >= 30 and dnu6 >= 30
    status = "✅双月可靠" if both_reliable else ("⚠4月不足" if dnu4 < 30 else "⚠6月不足")

    if both_reliable:
        found_both_good = True
        print(f"\n{'='*80}")
        print(f"  {name} | {bid}")
        print(f"{'='*80}")
        print(f"           │    4月    │    6月    │  变化")
        print(f"  CPI      │  ${cpi4:<7.2f} │  ${cpi6:<7.2f} │  {cpi6-cpi4:+.2f}")
        print(f"  R1       │  {r1_4:>6.1%}   │  {r1_6:>6.1%}   │  {r1_6-r1_4:+.1%}")
        print(f"  R3       │  {r3_4:>6.1%}   │  {r3_6:>6.1%}   │  {r3_6-r3_4:+.1%}")
        print(f"  DNU      │  {dnu4:>6.0f}    │  {dnu6:>6.0f}    │")
        print(f"{'='*80}")

if not found_both_good:
    print("\n⚠ 没有素材在两次测试中都达到 DNU >= 30")

# Show all both-month materials regardless of DNU threshold
print(f"\n\n--- 所有跨月素材总览 (含小样本) ---")
print(f"{'素材名称':<22s} {'出价':<8s} {'4月DNU':>7s} {'4月CPI':>7s} {'4月R1':>7s} {'4月R3':>7s} │ {'6月DNU':>7s} {'6月CPI':>7s} {'6月R1':>7s} {'6月R3':>7s} │ {'R1变化':>7s} {'R3变化':>7s} {'状态':<12s}")
print("-" * 120)

for _, bm in both.iterrows():
    name, bid = bm['mat_name'], bm['bid']
    r4 = data[(data['mat_name'] == name) & (data['bid'] == bid) & (data['month'] == '4月')]
    r6 = data[(data['mat_name'] == name) & (data['bid'] == bid) & (data['month'] == '6月')]
    if len(r4) == 0 or len(r6) == 0: continue

    dnu4, dnu6 = r4.iloc[0]['dnu'], r6.iloc[0]['dnu']
    r1_4, r3_4 = r4.iloc[0]['R1'], r4.iloc[0]['R3']
    r1_6, r3_6 = r6.iloc[0]['R1'], r6.iloc[0]['R3']
    cpi4, cpi6 = r4.iloc[0]['CPI'], r6.iloc[0]['CPI']

    reliable = dnu4 >= 30 and dnu6 >= 30
    status = "✅可靠" if reliable else ("⚠小样本" if (dnu4 + dnu6) >= 20 else "❌噪音")

    dr1 = (r1_6 - r1_4) * 100
    dr3 = (r3_6 - r3_4) * 100

    print(f"{name:<22s} {bid:<8s} {dnu4:>7.0f} {cpi4:>7.2f} {r1_4:>7.1%} {r3_4:>7.1%} │ {dnu6:>7.0f} {cpi6:>7.2f} {r1_6:>7.1%} {r3_6:>7.1%} │ {dr1:>+6.1f}pp {dr3:>+6.1f}pp {status:<12s}")

# ============================================================
# PART 2: Small sample but OUTSTANDING - top 5 by R1, top 5 by R3
# ============================================================
print(f"\n\n{'=' * 120}")
print("PART 2: 样本不足但表现亮眼 — 建议重新测试")
print("=" * 120)

small_data = data[data['dnu'] < 30].copy()

# Top 5 by R1 (min DNU >= 5 to filter absolute noise)
small_r1 = small_data[small_data['dnu'] >= 5].nlargest(5, 'R1')
print(f"\n--- Top 5 R1 (小样本 DNU>=5, 次日留存最高) ---")
print(f"{'素材名称':<22s} {'出价':<8s} {'月份':<6s} {'R1':>7s} {'R2':>7s} {'R3':>7s} {'DNU':>6s} {'CPI':>8s} {'花费':>10s}")
print("-" * 85)
for _, r in small_r1.iterrows():
    print(f"{r['mat_name']:<22s} {r['bid']:<8s} {r['month']:<6s} {r['R1']:>7.1%} {r['R2']:>7.1%} {r['R3']:>7.1%} {r['dnu']:>6.0f} ${r['CPI']:>7.2f} ${r['花费(USD)']:>9.2f}")

# Top 5 by R3 (min DNU >= 5)
small_r3 = small_data[small_data['dnu'] >= 5].nlargest(5, 'R3')
print(f"\n--- Top 5 R3 (小样本 DNU>=5, 3日留存最高) ---")
print(f"{'素材名称':<22s} {'出价':<8s} {'月份':<6s} {'R1':>7s} {'R2':>7s} {'R3':>7s} {'DNU':>6s} {'CPI':>8s} {'花费':>10s}")
print("-" * 85)
for _, r in small_r3.iterrows():
    print(f"{r['mat_name']:<22s} {r['bid']:<8s} {r['month']:<6s} {r['R1']:>7.1%} {r['R2']:>7.1%} {r['R3']:>7.1%} {r['dnu']:>6.0f} ${r['CPI']:>7.2f} ${r['花费(USD)']:>9.2f}")

# Top 5 by CPI (cheapest, min DNU >= 5)
small_cpi = small_data[small_data['dnu'] >= 5].nsmallest(5, 'CPI')
print(f"\n--- Top 5 低CPI (小样本 DNU>=5, 获客成本最低) ---")
print(f"{'素材名称':<22s} {'出价':<8s} {'月份':<6s} {'CPI':>8s} {'R1':>7s} {'R2':>7s} {'R3':>7s} {'DNU':>6s} {'花费':>10s}")
print("-" * 85)
for _, r in small_cpi.iterrows():
    print(f"{r['mat_name']:<22s} {r['bid']:<8s} {r['month']:<6s} ${r['CPI']:>7.2f} {r['R1']:>7.1%} {r['R2']:>7.1%} {r['R3']:>7.1%} {r['dnu']:>6.0f} ${r['花费(USD)']:>9.2f}")

# Composite score: R1 * 0.5 + R3 * 0.5 with CPI penalty (lower CPI better)
small_data['composite'] = np.where(
    small_data['dnu'] >= 5,
    small_data['R1'] * 0.5 + small_data['R3'] * 0.5,
    np.nan
)
top_composite = small_data.nlargest(5, 'composite')
print(f"\n--- Top 5 综合 (R1+R3均衡, DNU>=5) ---")
print(f"{'素材名称':<22s} {'出价':<8s} {'月份':<6s} {'综合分':>7s} {'R1':>7s} {'R2':>7s} {'R3':>7s} {'DNU':>6s} {'CPI':>8s}")
print("-" * 85)
for _, r in top_composite.iterrows():
    print(f"{r['mat_name']:<22s} {r['bid']:<8s} {r['month']:<6s} {r['composite']:>7.1%} {r['R1']:>7.1%} {r['R2']:>7.1%} {r['R3']:>7.1%} {r['dnu']:>6.0f} ${r['CPI']:>7.2f}")

print(f"\n{'=' * 120}")
print("DONE")
