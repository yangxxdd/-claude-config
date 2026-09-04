import json
out = {}
fm=json.load(open('sync_dump/fields_material.json',encoding='utf-8'))
for f in fm['data']['fields']:
    if f['name'] in ('出价方式',):
        out['出价方式'] = f
fi=json.load(open('sync_dump/fields_issue.json',encoding='utf-8'))
for f in fi['data']['fields']:
    if f['name'] in ('严重度',):
        out['严重度'] = f
json.dump(out, open('sync_dump/new_field_defs.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
print("saved")
