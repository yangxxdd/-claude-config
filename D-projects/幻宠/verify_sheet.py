import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import pandas as pd
pd.set_option('display.max_columns', 18)
pd.set_option('display.width', 400)
pd.set_option('display.max_colwidth', 30)
pd.set_option('display.max_rows', 120)

df = pd.read_excel('creative_final.xlsx', sheet_name='素材全量数据-按素材')
# Use column position instead of name
col_name = df.columns[0]
col_month = df.columns[3]

df2 = df[df[col_name].notna() | df[col_month].notna()]
print(f'Total data rows: {len(df2)}')
print(f'Unique 素材: {df2[col_name].dropna().nunique()}')
print(f'Columns: {list(df.columns)}')
print()
print('=== ALL data rows ===')
print(df2.to_string())
