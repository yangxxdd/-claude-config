import shutil, os

DST = 'GTS商店图参考图'
os.makedirs(DST, exist_ok=True)

copies = []

pdf_map = {
    'tmp_pdf_imgs/p06_img0.png': '01-PDF构图-炸鸡双面.png',
    'tmp_pdf_imgs/p07_img0.png': '02-PDF构图-城市游乐场.png',
    'tmp_pdf_imgs/p08_img0.png': '03-PDF构图-美钞解锁.png',
    'tmp_pdf_imgs/p09_img0.png': '04-PDF构图-涂鸦招募.png',
    'tmp_pdf_imgs/p10_img0.png': '05-PDF构图-街区火并.png',
    'tmp_pdf_imgs/p11_img0.png': '06-PDF构图-犯罪地图.png',
    'tmp_pdf_imgs/p12_img0.png': '07-PDF构图-宠物协战.png',
    'tmp_pdf_imgs/p13_img0.png': '08-PDF构图-营救情人.png',
    'tmp_pdf_imgs/p14_img0.png': '09-PDF构图-三人门徒.png',
    'tmp_pdf_imgs/p15_img0.png': '10-PDF构图-豪宅升级.png',
}

excel_map = {
    # 01
    'tmp_excel_imgs/新版商店五图_15_r299c5.png': '01-研发参考-炸鸡双面身份.png',
    # 03
    'tmp_excel_imgs/新版商店五图_00_r7c4.png': '03-研发参考-美钞解锁A.png',
    'tmp_excel_imgs/新版商店五图_01_r8c10.png': '03-研发参考-美钞解锁B.png',
    'tmp_excel_imgs/新版商店五图_05_r8c16.png': '03-研发参考-美钞解锁C.png',
    # 04
    'tmp_excel_imgs/新版商店五图_03_r103c4.png': '04-研发参考-涂鸦招募A.png',
    'tmp_excel_imgs/新版商店五图_04_r123c11.png': '04-研发参考-涂鸦招募B.png',
    # 05
    'tmp_excel_imgs/新版商店五图_10_r192c5.png': '05-研发参考-街区火并A.png',
    'tmp_excel_imgs/新版商店五图_11_r192c11.png': '05-研发参考-街区火并B.png',
    'tmp_excel_imgs/新版商店五图_12_r193c16.png': '05-研发参考-街区火并C.png',
    # 06
    'tmp_excel_imgs/新版商店五图_13_r236c5.jpeg': '06-研发参考-犯罪地图A.jpg',
    'tmp_excel_imgs/新版商店五图_14_r236c12.png': '06-研发参考-犯罪地图B.png',
    # 07
    'tmp_excel_imgs/新版商店五图_07_r61c4.png': '07-研发参考-宠物-杰克罗素梗犬.png',
    'tmp_excel_imgs/新版商店五图_06_r62c9.jpeg': '07-研发参考-宠物-德牧.jpg',
    'tmp_excel_imgs/新版商店五图_08_r81c4.png': '07-研发参考-宠物-德牧B.png',
    'tmp_excel_imgs/新版商店五图_02_r77c15.png': '07-研发参考-宠物-战斗场景.png',
    # 08
    'tmp_excel_imgs/新版商店五图_09_r159c4.png': '08-研发参考-营救情人.png',
}

# Copy PDF images
for src, dst_name in pdf_map.items():
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(DST, dst_name))
        copies.append(dst_name)
    else:
        print(f'  MISSING PDF: {src}')

# Copy Excel images
for src, dst_name in excel_map.items():
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(DST, dst_name))
        copies.append(dst_name)
    else:
        print(f'  MISSING Excel: {src}')

print(f'\n共 {len(copies)} 个文件 -> {DST}/')

# Group by direction
dirs = {}
for name in copies:
    d = name[:2]
    dirs.setdefault(d, []).append(name)

for d in sorted(dirs):
    print(f'\n【{d}】({len(dirs[d])}张)')
    for f in dirs[d]:
        print(f'  {f}')

print('\n——— 仅PDF构图，研发sheet3无对应 ———')
print('02: PDF构图1张 + PDF引用旧Excel(image9城市氛围/image10霓虹街区，sheet1-2)')
print('09: PDF构图1张 + PDF引用旧Excel(image23/24阵容/image25女牛仔，sheet2)')
print('10: PDF构图1张 + PDF引用旧Excel(image32/33豪宅/image34升级入口，sheet2)')
print('\n这3个方向的旧Excel参考图需要你手动从原表里找。')
