import json
d=json.load(open('sync_dump/formal_material_recs.json',encoding='utf-8'))['data']
fids=d.get('field_id_list',[]); recids=d.get('record_id_list',[]); rows=d.get('data',[])
fl=json.load(open('sync_dump/fields_material.json',encoding='utf-8'))
fmap={f['id']:f['name'] for f in fl['data']['fields']}
lines=[]
lines.append(f"formal material records: {len(recids)}")
for rid,row in zip(recids,rows):
    d2=dict(zip(fids,row))
    keep={fmap.get(k,k):v for k,v in d2.items() if fmap.get(k) in ('素材名称','标记','日期','素材类型')}
    lines.append(f"{rid} => {json.dumps(keep, ensure_ascii=False)}")
open('sync_dump/formal_material_summary.txt','w',encoding='utf-8').write('\n'.join(lines))
print('written', len(recids))
