# -*- coding: utf-8 -*-
"""构建所有方向（02-10，含A/B）的飞书写入 cells"""
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from directions_base import DIRECTIONS
from prompt_generator import build_prompt

# 从 V3b 文件读取 01-A 提示词（已写入飞书，这里用于对比格式）
def load_01a():
    with open('store_sheet/01A_prompt_v3b.md', encoding='utf-8') as f:
        content = f.read()
    en_start = content.find('## AI提示词-EN (V3b)')
    en_end = content.find('## AI提示词-中文 (V3b)')
    en = content[en_start:en_end].replace('## AI提示词-EN (V3b)', '').strip()
    zh = content[en_end:].replace('## AI提示词-中文 (V3b)', '').strip()
    return zh, en

ORDER = ["02", "03-A", "03-B", "04-A", "04-B", "05-A", "05-B", "06-A", "06-B",
         "07-A", "07-B", "08-A", "08-B", "09-A", "09-B", "10-A", "10-B"]

def build_row(code):
    d = DIRECTIONS[code]
    zh_prompt, en_prompt = build_prompt(code)
    return {
        "A": code,
        "B": d["subject"],
        "C": "商店图",
        "D": d["zh"],
        "E": d["en"],
        "F": f"【制作人意图】{d['producer_intent']}\n【场景落地】{d['scene']}",
        "G": d["style"],
        "H": d["ui"],
        "I": d["assets"],
        "J": d["ref"],
        "K": zh_prompt,
        "L": en_prompt,
        "M": d["accept"],
        "N": d["note"],
    }

def main():
    rows = []
    for code in ORDER:
        rows.append(build_row(code))

    # 生成 cells JSON（供飞书写入，每行一个 dict 数组）
    headers = ['图号','方向主题','素材类型','中文文案','英文文案','画面构成拆解','视觉风格关键词','UI元素映射','可用物料映射','参考图','AI提示词-中文','AI提示词-EN','验收自查','备注']
    cells = []
    for r in rows:
        cells.append([{'value': r[chr(65+j)] if r.get(chr(65+j)) else ''} for j in range(14)])

    with open('store_sheet/all_directions_cells.json', 'w', encoding='utf-8') as f:
        json.dump(cells, f, ensure_ascii=False, indent=1)

    print(f"生成完成：{len(cells)} 行")
    # 输出每行长度摘要
    for r in rows:
        print(f"  {r['A']} | {r['B']} | 中文提示词{len(r['K'])}字 | 英文{len(r['L'])}字")

    # 也保存一份纯数据用于后续校验
    with open('store_sheet/all_directions_data.json', 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)

if __name__ == '__main__':
    main()
