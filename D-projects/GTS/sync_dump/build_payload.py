import json
tables = ["material","daily","finance","issue","conclusion"]
for n in tables:
    recs=json.load(open(f"sync_dump/norm_{n}.json",encoding="utf-8"))
    if not recs:
        continue
    # canonical field order = first record's key order
    fields=list(recs[0]["fields"].keys())
    rows=[]
    for r in recs:
        row=[r["fields"].get(f) for f in fields]
        rows.append(row)
    payload={"fields":fields,"rows":rows}
    json.dump(payload, open(f"sync_dump/payload_{n}.json","w",encoding="utf-8"), ensure_ascii=False)
    print(f"{n}: {len(rows)} rows, {len(fields)} fields")
    print("  fields:", fields)
