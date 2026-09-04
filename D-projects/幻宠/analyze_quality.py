import pandas as pd
import numpy as np

df = pd.read_excel('creative_final.xlsx', sheet_name='素材表现汇总')

# Column mapping
c = {df.columns[i]: df.columns[i] for i in range(20)}
MONTH_C = df.columns[0]
MAT_C = df.columns[1]
TYPE_C = df.columns[2]
BID_C = df.columns[3]
INSTALLS_C = df.columns[4]
SPEND_C = df.columns[5]
CPI_C = df.columns[6]
IMPR_C = df.columns[7]
CLICKS_C = df.columns[8]
CTR_C = df.columns[9]
CPM_C = df.columns[10]
CVR_C = df.columns[11]
NOTES_C = df.columns[12]
DNU_C = df.columns[13]
R1_CNT_C = df.columns[14]
R2_CNT_C = df.columns[15]
R3_CNT_C = df.columns[16]
R1_C = df.columns[17]
R2_C = df.columns[18]
R3_C = df.columns[19]

# Filter to real data rows
data = df[df[MONTH_C].isin(['4月', '6月'])].copy()
data = data[~data[MAT_C].str.contains('合计', na=False)].copy()
data['DNU_num'] = pd.to_numeric(data[DNU_C], errors='coerce')
data['idx'] = data.index

results = []

# =====================================================
# ANALYSIS 1: Small Sample Warnings
# =====================================================
results.append("="*80)
results.append("1. SMALL SAMPLE WARNINGS (DNU < 30)")
results.append("="*80)

below30 = data[data['DNU_num'] < 30].sort_values('DNU_num')
results.append("\nTotal rows with DNU < 30: {} out of {} data rows ({:.1f}%)".format(
    len(below30), len(data), len(below30)/len(data)*100))
results.append("Rows with DNU < 10: {}".format(len(below30[below30['DNU_num'] < 10])))
results.append("Rows with DNU >= 30: {}".format(len(data[data['DNU_num'] >= 30])))

results.append("\n--- Worst offenders: DNU < 10 ---")
worst = below30[below30['DNU_num'] < 10].sort_values('DNU_num')
for _, row in worst.iterrows():
    results.append(
        "  DNU={:>2d} | {} | {:7s} | R1={:.1%} R2={:.1%} R3={:.1%} | Spend=${:.0f} | notes={}".format(
            int(row['DNU_num']), row[MAT_C], row[BID_C],
            row[R1_C], row[R2_C], row[R3_C],
            row[SPEND_C], row[NOTES_C])
    )

results.append("\n--- All DNU < 30, sorted ---")
for _, row in below30.iterrows():
    flag = "*** DNU<10" if row['DNU_num'] < 10 else "   DNU<30"
    results.append(
        "  {} | {} | DNU={:>2d} | {:35s} | {:7s} | R1={:.1%} R2={:.1%} R3={:.1%}".format(
            flag, row[MONTH_C], int(row['DNU_num']), row[MAT_C][:35], row[BID_C],
            row[R1_C], row[R2_C], row[R3_C])
    )

# =====================================================
# ANALYSIS 2: Anomalous Retention Patterns
# =====================================================
results.append("\n" + "="*80)
results.append("2. ANOMALOUS RETENTION PATTERNS")
results.append("="*80)

# R2 > R1
results.append("\n--- R2 > R1 (retention increasing - usually data error) ---")
r2_gt_r1 = data[(data[R2_C] > data[R1_C]) & data['DNU_num'].notna()]
if len(r2_gt_r1) > 0:
    for _, row in r2_gt_r1.iterrows():
        results.append(
            "  *** ANOMALY: {} | {} | {} | DNU={} | R1={:.1%} R2={:.1%} | R2 > R1 by {:.1%}".format(
                row[MONTH_C], row[MAT_C], row[BID_C], int(row['DNU_num']),
                row[R1_C], row[R2_C], row[R2_C]-row[R1_C])
        )
else:
    results.append("  None found.")

# R3 > R2
results.append("\n--- R3 > R2 (retention increasing) ---")
r3_gt_r2 = data[(data[R3_C] > data[R2_C]) & data['DNU_num'].notna()]
if len(r3_gt_r2) > 0:
    for _, row in r3_gt_r2.iterrows():
        results.append(
            "  *** ANOMALY: {} | {} | {} | DNU={} | R2={:.1%} R3={:.1%} | R3 > R2 by {:.1%}".format(
                row[MONTH_C], row[MAT_C], row[BID_C], int(row['DNU_num']),
                row[R2_C], row[R3_C], row[R3_C]-row[R2_C])
        )
else:
    results.append("  None found.")

# R1 = 0% with non-trivial DNU
results.append("\n--- R1 = 0% with DNU >= 3 ---")
r1_zero = data[(data[R1_C] == 0) & (data['DNU_num'] >= 3)]
if len(r1_zero) > 0:
    for _, row in r1_zero.iterrows():
        results.append(
            "  *** ANOMALY: {} | {} | {} | DNU={} | R1=0% | R2={:.1%} R3={:.1%} | r1_cnt={:.0f}".format(
                row[MONTH_C], row[MAT_C], row[BID_C], int(row['DNU_num']),
                row[R2_C], row[R3_C], row[R1_CNT_C])
        )
else:
    results.append("  None found.")

# R1 = 100% with non-trivial DNU
results.append("\n--- R1 = 100% with DNU > 1 ---")
r1_100 = data[(data[R1_C] == 1.0) & (data['DNU_num'] > 1)]
if len(r1_100) > 0:
    for _, row in r1_100.iterrows():
        results.append(
            "  *** ANOMALY: {} | {} | {} | DNU={} | R1=100%".format(
                row[MONTH_C], row[MAT_C], row[BID_C], int(row['DNU_num']))
        )
else:
    results.append("  None found.")

# Extreme R3 with tiny DNU
results.append("\n--- High R3 (>20%) with DNU < 5 ---")
extreme = data[(data[R3_C] > 0.20) & (data['DNU_num'] < 5)]
if len(extreme) > 0:
    for _, row in extreme.iterrows():
        results.append(
            "  SUSPICIOUS: {} | {} | {} | DNU={} | R3={:.1%} | r3_cnt={:.0f} | R1={:.1%} R2={:.1%}".format(
                row[MONTH_C], row[MAT_C], row[BID_C], int(row['DNU_num']),
                row[R3_C], row[R3_CNT_C], row[R1_C], row[R2_C])
        )
else:
    results.append("  None found.")

# R3 > R1 (all rows where this happens and have non-zero R1)
results.append("\n--- R3 > R1 (R3 higher than R1, with R1 > 0) ---")
r3_gt_r1 = data[(data[R3_C] > data[R1_C]) & data['DNU_num'].notna() & (data[R1_C] > 0)]
if len(r3_gt_r1) > 0:
    for _, row in r3_gt_r1.iterrows():
        results.append(
            "  {} | {} | {} | DNU={} | R1={:.1%} R3={:.1%} | R3 > R1 by {:.1%}".format(
                row[MONTH_C], row[MAT_C], row[BID_C], int(row['DNU_num']),
                row[R1_C], row[R3_C], row[R3_C]-row[R1_C])
        )
else:
    results.append("  None found.")

# All rows with weird patterns (R1, R2, R3 not strictly decreasing)
results.append("\n--- Non-monotonic retention (R1 -> R2 -> R3 not strictly decreasing) ---")
non_mono = data[(data[R1_C].notna()) & (data['DNU_num'].notna())].copy()
all_non_mono = non_mono[(non_mono[R2_C] > non_mono[R1_C]) | (non_mono[R3_C] > non_mono[R2_C])]
for _, row in all_non_mono.iterrows():
    dnu = int(row['DNU_num'])
    issue = ""
    if row[R2_C] > row[R1_C]:
        issue += "R2>R1 "
    if row[R3_C] > row[R2_C]:
        issue += "R3>R2 "
    results.append(
        "  {} | {} | {} | DNU={:>3d} | R1={:.1%} R2={:.1%} R3={:.1%} | ISSUE: {}".format(
            row[MONTH_C], row[MAT_C], row[BID_C], dnu,
            row[R1_C], row[R2_C], row[R3_C], issue)
    )

# =====================================================
# ANALYSIS 3: Month-over-Month Comparison
# =====================================================
results.append("\n" + "="*80)
results.append("3. MONTH-OVER-MONTH COMPARISON")
results.append("="*80)

apr_materials = set(data[data[MONTH_C] == '4月'][MAT_C])
jun_materials = set(data[data[MONTH_C] == '6月'][MAT_C])
common = apr_materials & jun_materials

results.append("\nMaterials in both months: {}".format(len(common)))
for mat in sorted(common):
    apr_rows = data[(data[MAT_C] == mat) & (data[MONTH_C] == '4月')]
    jun_rows = data[(data[MAT_C] == mat) & (data[MONTH_C] == '6月')]

    for _, apr in apr_rows.iterrows():
        bid = apr[BID_C]
        jun_match = jun_rows[jun_rows[BID_C] == bid]
        if len(jun_match) == 0:
            results.append("  {} | {}: in 4月 only (no 6月 match)".format(mat, bid))
            continue
        jun = jun_match.iloc[0]

        apr_dnu = int(apr['DNU_num']) if pd.notna(apr['DNU_num']) else 0
        jun_dnu = int(jun['DNU_num']) if pd.notna(jun['DNU_num']) else 0

        r1_diff = jun[R1_C] - apr[R1_C]
        r3_diff = jun[R3_C] - apr[R3_C]

        flag = ""
        if abs(r1_diff) > 0.20:
            flag += " *** R1 SWING={:+.1%}".format(r1_diff)
        if abs(r3_diff) > 0.20:
            flag += " *** R3 SWING={:+.1%}".format(r3_diff)

        sample_note = ""
        if apr_dnu < 30 or jun_dnu < 30:
            if apr_dnu < 10 or jun_dnu < 10:
                sample_note = " [UNRELIABLE: DNU too small]"
            else:
                sample_note = " [CAUTION: modest sample]"

        results.append(
            "  {:35s} | {:7s} | 4月:DNU={:>3d} R1={:.1%} R3={:.1%} | 6月:DNU={:>3d} R1={:.1%} R3={:.1%} | dR1={:+.1%} dR3={:+.1%}{}{}".format(
                mat, bid, apr_dnu, apr[R1_C], apr[R3_C],
                jun_dnu, jun[R1_C], jun[R3_C],
                r1_diff, r3_diff, flag, sample_note)
        )

# =====================================================
# ANALYSIS 4: Bid Type Comparison
# =====================================================
results.append("\n" + "="*80)
results.append("4. BID TYPE COMPARISON (Install vs AEO)")
results.append("="*80)

for month_name in ['4月', '6月']:
    month_data = data[data[MONTH_C] == month_name]
    results.append("\n--- {} ---".format(month_name))

    mat_bids = month_data.groupby(MAT_C)[BID_C].apply(set)
    dual_bid_mats = mat_bids[mat_bids.apply(lambda x: len(x) >= 2)].index

    results.append("Materials with both bid types: {}".format(len(dual_bid_mats)))

    for mat in sorted(dual_bid_mats):
        install_rows = month_data[(month_data[MAT_C] == mat) & (month_data[BID_C] == 'Install')]
        aeo_rows = month_data[(month_data[MAT_C] == mat) & (month_data[BID_C] == 'AEO')]

        if len(install_rows) == 0 or len(aeo_rows) == 0:
            continue

        inst = install_rows.iloc[0]
        aeo = aeo_rows.iloc[0]

        inst_dnu = int(inst['DNU_num']) if pd.notna(inst['DNU_num']) else 0
        aeo_dnu = int(aeo['DNU_num']) if pd.notna(aeo['DNU_num']) else 0

        r1_diff = inst[R1_C] - aeo[R1_C]
        r3_diff = inst[R3_C] - aeo[R3_C]

        winner_r1 = "Install" if r1_diff > 0 else "AEO"
        winner_r3 = "Install" if r3_diff > 0 else "AEO"

        sample_warning = ""
        if inst_dnu < 20 or aeo_dnu < 20:
            sample_warning = " [SMALL SAMPLE]"

        results.append(
            "  {:35s} | Inst:DNU={:>3d} R1={:.1%} R3={:.1%} CPI=${:.2f} | AEO:DNU={:>3d} R1={:.1%} R3={:.1%} CPI=${:.2f} | R1_win={} R3_win={}{}".format(
                mat, inst_dnu, inst[R1_C], inst[R3_C], inst[CPI_C],
                aeo_dnu, aeo[R1_C], aeo[R3_C], aeo[CPI_C],
                winner_r1, winner_r3, sample_warning)
        )

# =====================================================
# SUMMARY
# =====================================================
results.append("\n" + "="*80)
results.append("5. SUMMARY STATISTICS")
results.append("="*80)

for month_name in ['4月', '6月']:
    month_data = data[data[MONTH_C] == month_name]
    results.append("\n{}:".format(month_name))
    results.append("  Total data rows: {}".format(len(month_data)))
    results.append("  DNU < 30 rows: {}".format(len(month_data[month_data['DNU_num'] < 30])))
    results.append("  DNU < 10 rows: {}".format(len(month_data[month_data['DNU_num'] < 10])))

    large_sample = month_data[month_data['DNU_num'] >= 30]
    if len(large_sample) > 0:
        results.append("  Large sample (>=30) R1 avg: {:.1%} (n={})".format(
            large_sample[R1_C].mean(), len(large_sample)))
        results.append("  Large sample (>=30) R3 avg: {:.1%} (n={})".format(
            large_sample[R3_C].mean(), len(large_sample)))

    for bid_type in ['AEO', 'Install']:
        bd = month_data[month_data[BID_C] == bid_type]
        bd_large = bd[bd['DNU_num'] >= 30]
        results.append("  {}: {} rows, {} with DNU>=30".format(bid_type, len(bd), len(bd_large)))
        if len(bd_large) > 0:
            results.append("    Large-sample R1: {:.1%}, R3: {:.1%}".format(
                bd_large[R1_C].mean(), bd_large[R3_C].mean()))

# Overall data quality
results.append("\n" + "="*80)
results.append("6. OVERALL DATA QUALITY ASSESSMENT")
results.append("="*80)

total_rows = len(data)
rows_with_retention = len(data[data[R1_C].notna()])
rows_without_retention = len(data[data[R1_C].isna()])
rows_dnu_lt_30 = len(data[data['DNU_num'] < 30])
rows_dnu_lt_10 = len(data[data['DNU_num'] < 10])
rows_dnu_ge_30 = len(data[data['DNU_num'] >= 30])

results.append("\nTotal data rows: {}".format(total_rows))
results.append("Rows with retention data: {}".format(rows_with_retention))
results.append("Rows without retention data (DNU='需BI计算' etc): {}".format(rows_without_retention))
results.append("Rows DNU < 30 (unreliable retention): {} ({:.0f}%)".format(
    rows_dnu_lt_30, rows_dnu_lt_30/total_rows*100))
results.append("Rows DNU < 10 (very unreliable): {} ({:.0f}%)".format(
    rows_dnu_lt_10, rows_dnu_lt_10/total_rows*100))
results.append("Rows DNU >= 30 (usable for decisions): {} ({:.0f}%)".format(
    rows_dnu_ge_30, rows_dnu_ge_30/total_rows*100))

# Write results
with open('data_quality_analysis.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

print("Analysis complete. Written to data_quality_analysis.txt")
print("Total data rows: {}, DNU<30: {}, DNU<10: {}, DNU>=30: {}".format(
    total_rows, rows_dnu_lt_30, rows_dnu_lt_10, rows_dnu_ge_30))
