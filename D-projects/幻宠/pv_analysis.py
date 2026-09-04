import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 300)

df = pd.read_excel('creative_final.xlsx', sheet_name='素材表现汇总')
df = df[df['月份'].isin(['4月','6月'])].copy()

for month in ['4月', '6月']:
    m = df[df['月份'] == month]
    print(f'\n{"="*60}')
    print(f'  {month} P(图片) vs V(视频) 对比')
    print(f'{"="*60}')
    for t in ['P', 'V']:
        subset = m[m['类型'] == t]
        valid = subset[subset['DNU'] >= 5]
        if len(subset) == 0:
            continue
        print(f'\n  [{t}] 总{len(subset)}个, DNU>=5: {len(valid)}个')
        if len(valid) > 0:
            print(f'    CPI:    均值=${valid["CPI"].mean():.2f}  中位=${valid["CPI"].median():.2f}')
            print(f'    R1:     均值={valid["R1"].mean():.1%}  中位={valid["R1"].median():.1%}')
            print(f'    R3:     均值={valid["R3"].mean():.1%}  中位={valid["R3"].median():.1%}')
            print(f'    次留成本: 均值=${valid["次留成本"].mean():.2f}  中位=${valid["次留成本"].median():.2f}')
            print(f'    CTR:    均值={valid["CTR"].mean():.4f}  中位={valid["CTR"].median():.4f}')
            print(f'    CVR:    均值={valid["CVR"].mean():.4f}  中位={valid["CVR"].median():.4f}')
            print(f'    DNU合计: {valid["DNU"].sum()}  花费合计: ${valid["花费(USD)"].sum():.0f}')

print(f'\n{"="*60}')
print(f'  双月合计 P vs V (DNU>=5)')
print(f'{"="*60}')
for t in ['P', 'V']:
    subset = df[(df['类型'] == t) & (df['DNU'] >= 5)]
    print(f'\n  [{t}] {len(subset)}个素材  DNU合计:{subset["DNU"].sum()}  花费合计:${subset["花费(USD)"].sum():.0f}')
    print(f'    CPI:    均值=${subset["CPI"].mean():.2f}  中位=${subset["CPI"].median():.2f}')
    print(f'    R1:     均值={subset["R1"].mean():.1%}  中位={subset["R1"].median():.1%}')
    print(f'    R3:     均值={subset["R3"].mean():.1%}  中位={subset["R3"].median():.1%}')
    print(f'    次留成本: 均值=${subset["次留成本"].mean():.2f}  中位=${subset["次留成本"].median():.2f}')

# Detail: list all P and V with DNU>5 for reference
print(f'\n{"="*60}')
print(f'  明细: 所有 DNU>=5 素材 (按类型+月份)')
print(f'{"="*60}')
detail = df[df['DNU'] >= 5][['月份','类型','素材名称','出价方式','DNU','CPI','R1','R3','次留成本','花费(USD)']].copy()
detail = detail.sort_values(['月份','类型','CPI'])
for _, r in detail.iterrows():
    print(f'  {r["月份"]} {r["类型"]} {r["素材名称"]:<25s} {r["出价方式"]:<8s} DNU={int(r["DNU"]):>3d} CPI=${r["CPI"]:.2f} R1={r["R1"]:.1%} R3={r["R3"]:.1%} 次留=${r["次留成本"]:.2f}')
