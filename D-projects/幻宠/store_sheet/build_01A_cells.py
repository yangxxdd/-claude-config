# -*- coding: utf-8 -*-
import json

def read_v3b():
    """从 V3b 提示词文件提取中英文提示词"""
    with open('store_sheet/01A_prompt_v3b.md', encoding='utf-8') as f:
        content = f.read()
    # 提取英文段
    en_start = content.find('## AI提示词-EN (V3b)')
    en_end = content.find('## AI提示词-中文 (V3b)')
    en_prompt = content[en_start:en_end].replace('## AI提示词-EN (V3b)', '').strip()
    # 提取中文段
    zh_prompt = content[en_end:].replace('## AI提示词-中文 (V3b)', '').strip()
    return zh_prompt, en_prompt

zh, en = read_v3b()

# 01-A 行数据（14列）
row = {
    "A": "01-A",
    "B": "炸鸡店双面身份·女牛仔主角",
    "C": "商店图",
    "D": "从炸鸡店到犯罪帝国",
    "E": "FROM FRIED CHICKEN TO A CRIME EMPIRE",
    "F": "【制作人构图】现实参考图(写实生活化)↔游戏内俯视图(经营卡通)左右对照；核心叙事=炸鸡店是军火交易伪装。\n"
         "【前景·双面时刻】女牛仔主角(牛仔帽+牛仔背心+红围裙+腰间左轮)占35-45%：一手举金黄炸鸡腿(友好伪装)，一手从柜台下递手枪给战术夹克顾客；柜台下露出现金堆和另一武器枪口。\n"
         "【中景·店内】红黄"FRIED CHICKEN"霓虹招牌+玻璃展示柜+钢制炸炉；货架炸鸡盒藏枪管、暗门/后门、角落监控摄像头；金黄鸡腿飞舞(数字22/16)。\n"
         "【背景·夜城】透过玻璃窗：紫蓝天幕+棕榈树/高楼剪影+霓虹灯牌+警车警灯+黄色路线+红色事件针。\n"
         "【符号】炸鸡桶(题材记忆)+黄色路线(行为连贯)+红色事件针(犯罪城市感)。",
    "G": "美漫写实(American Comic Realism，类蝙蝠侠阿卡姆/看门狗)+明亮犯罪喜剧+霓虹复古；暖金/橙红前景 vs 冷紫蓝夜晚背景；非Q版非扁平卡通",
    "H": "顶部资源条(粉钻3K/银币200K/金币500K+/齿轮/邮件，黑底白字)；左上角头像+昵称+等级30+战斗力；右上角小地图+城堡图标；左侧ACTIVITY/PASS/STARTER；右侧RANKING/SHOP/OPSS/BAG；底部标题白粗体无衬线全大写，深色底衬占15-20%",
    "I": "角色:女牛仔官方立绘/3D模型(image25)；场景:炸鸡店内(研发参考-炸鸡双面身份.png)；武器:手枪/AK47(藏炸鸡箱)；UI:3-炸鸡店.jpg基准；背景:02_K霓虹夜城参考",
    "J": "01-PDF构图-炸鸡双面.png / 01-研发参考-炸鸡双面身份.png / image49双面身份 / image26游戏内经营",
    "K": zh,
    "L": en,
    "M": "180px缩略图3秒可读；女牛仔占35-45%；主体>60%；单图单命题=双面身份；UI占比<20%；标题2-7词全大写；无毒品/血腥",
    "N": "P0首屏|A/B：A版女牛仔强主角，B版弱化人物放大炸鸡店与秘密交易|禁区：无毒品用underground deal|画风V3b已与制作人对齐"
}

# 生成 cells 2D array
headers = ['图号','方向主题','素材类型','中文文案','英文文案','画面构成拆解','视觉风格关键词','UI元素映射','可用物料映射','参考图','AI提示词-中文','AI提示词-EN','验收自查','备注']
cells = [[{'value': row.get(chr(65+j), '')} for j in range(14)]]

with open('store_sheet/01A_cells.json', 'w', encoding='utf-8') as f:
    json.dump(cells, f, ensure_ascii=False, indent=1)

print("01-A cells JSON 生成完成")
print(f"中文提示词长度: {len(zh)} 字符")
print(f"英文提示词长度: {len(en)} 字符")
