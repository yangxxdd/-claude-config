# -*- coding: utf-8 -*-
"""生成 幻宠 9/10-9/13 方案二（开AEO）广告架构脑图 (.xmind)"""
import json
import uuid
import zipfile

OUT = r"D:\claude-projects\projects\幻宠\Palkie广告架构-方案二-9.10-9.13.xmind"


def tid(prefix):
    return f"{prefix}-{uuid.uuid4().hex[:10]}"


def topic(title, style_id, children=None):
    t = {"id": tid("topic"), "class": "topic", "title": title, "style": {"id": style_id}}
    if children:
        t["children"] = {"attached": children}
    return t


def creative(title):
    return topic(title, "s-creative")


# ---------- 素材清单 ----------
CONFIRM_8 = ["V-帕萌战斗-雪地竞品", "V-帕萌战斗-群殴打鸡", "V-抓宠战斗", "P-抓宠经营-幽飘",
             "P-抓宠经营-超梦", "V-抓宠经营-捕捞竞品", "P-宠物展示-合成 3D", "P-宠物展示-二阶进化"]
ITER_5 = ["P-宠物展示-二阶进化-迭代", "P-抓宠经营-皮卡丘", "P-抓宠经营-耿鬼", "P-宠物展示-合成 3D迭代", "V-宠物展示-宠物融合迭代"]
NEW_8_MAIN = ["P-宠物展示-融合恶搞", "P-宠物展示-融合炫酷", "P-宠物展示-融合擦边", "V-幽飘法庭剧情",
              "V-宠物展示-蹭超能勇士变身", "V-抓宠经营-砸蛋", "V-抓宠经营-售卖帕基改片头重口味"]
NEW_8_NEWACCT = ["V-宠物展示-宠物进化蹭数码宝贝"]
POKEMON_3 = ["宝可梦图片1", "宝可梦图片2", "宝可梦视频1"]
SHOP_4 = ["P-宠物展示-合成 3D", "P-抓宠经营-超梦", "V-宠物展示-宠物合成", "V-抓宠战斗"]

# 三组素材（C2/C4 复用）
GROUP_EXCELLENT = CONFIRM_8
GROUP_ITER = ITER_5
GROUP_NEW = NEW_8_MAIN


# ---------- C1: PH 拆2 camp ----------
c1_shop = topic("Camp1a · INSTALL-PH-商店图测试 (1,000量@$1=$1,000)", "s-camp", [
    topic("[参数] 4素材×新/旧商店图2adset", "s-param"),
    topic("Adset · 新商店图(500量)", "s-group", [creative(x) for x in SHOP_4]),
    topic("Adset · 旧商店图(500量)", "s-group", [creative(x) for x in SHOP_4]),
])

c1_dir = topic("Camp1b · INSTALL-PH-方向验证 (1,000量@$1=$1,000)", "s-camp", [
    topic("[参数] 3adset = 6月优秀/迭代/新方向素材", "s-param"),
    topic("Adset · 6月测试优秀素材组", "s-group", [creative(x) for x in GROUP_EXCELLENT]),
    topic("Adset · 6月优秀迭代组", "s-group", [creative(x) for x in GROUP_ITER]),
    topic("Adset · 新方向素材组", "s-group", [creative(x) for x in GROUP_NEW]),
])

# ---------- C2: MX/ID/BR ----------
c2 = topic("Camp2 · INSTALL-T3(MX/ID/BR)-方向验证 (750量@$1=$750)", "s-camp", [
    topic("[参数] CBO · 3adset = 6月优秀/迭代/新方向素材", "s-param"),
    topic("Adset · 6月测试优秀素材组", "s-group", [creative(x) for x in GROUP_EXCELLENT]),
    topic("Adset · 6月优秀迭代组", "s-group", [creative(x) for x in GROUP_ITER]),
    topic("Adset · 新方向素材组", "s-group", [creative(x) for x in GROUP_NEW]),
])

# ---------- C3: US ----------
c3_main = topic("Camp3 · INSTALL-US (900量@$5=$4,500)", "s-camp", [
    topic("[参数] CBO筛选 · 8确认+5迭代+7新方向(主户) · 蹭数码宝贝在新户", "s-param"),
    topic("Adset · 8确认素材组", "s-group", [creative(x) for x in CONFIRM_8]),
    topic("Adset · 5迭代储备组", "s-group", [creative(x) for x in ITER_5]),
    topic("Adset · 新方向素材组(7条主户)", "s-group", [creative(x) for x in NEW_8_MAIN]),
])

c3_new = topic("Camp3-新户 · INSTALL-US (100量@$5=$500)", "s-camp", [
    topic("[参数] 新账户单独camp · 宝可梦视频1+侵权BGM蹭数码宝贝 · IP风险隔离", "s-param"),
    topic("Adset · 宝可梦视频1+蹭数码宝贝", "s-group",
          [creative("宝可梦视频1"), creative("V-宠物展示-宠物进化蹭数码宝贝")]),
])

# ---------- C4: AEO ----------
c4 = topic("Camp4 · AEO-US-purchase (1,250量@$20=$25,000)", "s-camp", [
    topic("[参数] CBO · 三组素材 · 首日剔除C1/C2/C3表现差素材 · 让AEO自己收敛 · 注意PH/T3与美国AEO用户群不同需人工核对", "s-param"),
    topic("Adset · 6月测试优秀素材组", "s-group", [creative(x) for x in GROUP_EXCELLENT]),
    topic("Adset · 6月优秀迭代组", "s-group", [creative(x) for x in GROUP_ITER]),
    topic("Adset · 新方向素材组", "s-group", [creative(x) for x in GROUP_NEW]),
])

# ---------- 总览 ----------
overview = [
    topic("[总览] Meta Ads · Android · 9/10-9/13(4天) · 开AEO · 测留存+付费", "s-param"),
    topic("[预算] 总 $32,750 · 5,000量 · 平均单价$6.55", "s-param"),
    topic("[分日] 9/10 1500量/$2,500 · 9/11 1125量/$9,250 · 9/12 1125量/$9,250 · 9/13 1250量/$11,750", "s-param"),
    topic("[配比] PH40%/T315%/US-install20%/AEO25% · 消耗 6%/2%/15%/76%", "s-param"),
]

us = topic("美国 · 2,250量/$30,000", "s-lv1", [c3_main, c3_new, c4])
ph = topic("菲律宾 · 2,000量/$2,000", "s-lv1", [c1_shop, c1_dir])
t3 = topic("T3(MX/ID/BR) · 750量/$750", "s-lv1", [c2])
android = topic("Android", "s-lv1", overview + [ph, t3, us])

root = topic("Palkie广告架构-方案二(开AEO) 9/10-9/13", "s-center", [android])
root["structureClass"] = "org.xmind.ui.logic.right"

# ---------- sheet / content ----------
sheet_id = tid("sheet")
content = [{
    "id": sheet_id,
    "class": "sheet",
    "title": "Palkie广告架构-方案二 9/10-9/13",
    "coreVersion": "3.0",
    "rev": 1,
    "rootTopic": root,
}]

styles = [
    {"id": "s-center", "type": "topic", "properties": {
        "fo:color": "#FFFFFF", "fo:font-size": "18pt", "fo:font-weight": "bold",
        "svg:fill": "#2E75B6", "shape-class": "org.xmind.topicShape.roundedRect"}},
    {"id": "s-lv1", "type": "topic", "properties": {
        "fo:color": "#1F1F1F", "fo:font-size": "13pt", "fo:font-weight": "bold",
        "svg:fill": "#BFBFBF", "shape-class": "org.xmind.topicShape.roundedRect"}},
    {"id": "s-camp", "type": "topic", "properties": {
        "fo:color": "#1F1F1F", "fo:font-size": "12pt", "fo:font-weight": "bold",
        "svg:fill": "#D9D9D9", "shape-class": "org.xmind.topicShape.roundedRect"}},
    {"id": "s-group", "type": "topic", "properties": {
        "fo:color": "#1F1F1F", "fo:font-size": "11pt", "fo:font-weight": "bold",
        "svg:fill": "#EDEDED", "shape-class": "org.xmind.topicShape.roundedRect"}},
    {"id": "s-param", "type": "topic", "properties": {
        "fo:color": "#C55A11", "fo:font-size": "10pt", "fo:font-style": "italic",
        "svg:fill": "#FDEBD0", "shape-class": "org.xmind.topicShape.roundedRect"}},
    {"id": "s-creative", "type": "topic", "properties": {
        "fo:color": "#1F1F1F", "fo:font-size": "10pt",
        "svg:fill": "#FFFFFF", "shape-class": "org.xmind.topicShape.roundedRect"}},
    {"id": "s-placeholder", "type": "topic", "properties": {
        "fo:color": "#808080", "fo:font-size": "10pt", "fo:font-style": "italic",
        "svg:fill": "#FAFAFA", "shape-class": "org.xmind.topicShape.roundedRect"}},
]

metadata = {
    "creator": {"name": "XMind", "version": "23.11.6538"},
    "metadata": [{"metadata-id": "default", "o:default-rev": 1}],
}

manifest = {
    "file-entries": [
        {"full-path": "content.json", "media-type": "application/json"},
        {"full-path": "metadata.json", "media-type": "application/json"},
        {"full-path": "styles.json", "media-type": "application/json"},
    ]
}

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for name, obj in [("content.json", content), ("metadata.json", metadata),
                      ("styles.json", styles), ("manifest.json", manifest)]:
        data = json.dumps(obj, ensure_ascii=False, indent=2).encode("utf-8")
        z.writestr(name, data)

# ---------- 校验 ----------
with zipfile.ZipFile(OUT, "r") as z:
    names = z.namelist()
    for name in ["content.json", "metadata.json", "styles.json", "manifest.json"]:
        assert name in names, f"missing {name}"
        json.loads(z.read(name).decode("utf-8"))
    print("zip entries:", names)
    print("valid json: OK")


def count(topics):
    n = 0
    for t in topics:
        n += 1
        if "children" in t:
            n += count(t["children"]["attached"])
    return n


print("总节点数:", count([root]))
print("输出文件:", OUT)
