# -*- coding: utf-8 -*-
import json, subprocess, sys

# 1. 从 V3b 文件提取提示词
with open('store_sheet/01A_prompt_v3b.md', encoding='utf-8') as f:
    content = f.read()
en_start = content.find('## AI提示词-EN (V3b)')
en_end = content.find('## AI提示词-中文 (V3b)')
en_prompt = content[en_start:en_end].replace('## AI提示词-EN (V3b)', '').strip()
zh_prompt = content[en_end:].replace('## AI提示词-中文 (V3b)', '').strip()

# 2. 注入到 JSON 的 K(10)/L(11) 列
with open('store_sheet/01A_cells.json', encoding='utf-8') as f:
    cells = json.load(f)
cells[0][10]['value'] = zh_prompt   # 列K (0-indexed 10)
cells[0][11]['value'] = en_prompt   # 列L (0-indexed 11)

# 3. 保存最终 payload
with open('store_sheet/01A_final.json', 'w', encoding='utf-8') as f:
    json.dump(cells, f, ensure_ascii=False)

print("01-A 最终 payload 生成完成")
print(f"K列(中文提示词)长度: {len(zh_prompt)}")
print(f"L列(英文提示词)长度: {len(en_prompt)}")
