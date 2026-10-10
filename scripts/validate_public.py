#!/usr/bin/env python3
"""Fail closed if public catalog contains unapproved source URLs/internal data."""
import json, pathlib, re
root=pathlib.Path(__file__).resolve().parents[1]
data=json.loads((root/"data/discovery_catalog.json").read_text(encoding="utf-8"))
assert data["publication"]=="CATEGORY_DISCOVERY_ONLY_NO_MEDICAL_ADVICE"
groups=data["groups"];cards=data["cards"]
ids=[x["id"] for x in groups]; assert len(ids)==len(set(ids))
card_ids=[x["id"] for x in cards]; assert len(card_ids)==len(set(card_ids))
assert all(x["group"] in ids for x in cards)
assert all(x["status"]=="검수 준비 중" for x in cards)
payload=json.dumps(data,ensure_ascii=False)
for pattern in (r"https?://",r"(?i)github\.com",r"(?i)(token|secret|api_key|source_url|original_url|private_path)"):
    assert not re.search(pattern,payload),f"Public data contains forbidden token: {pattern}"
html=(root/"index.html").read_text(encoding="utf-8")
for required in ('id="search"','id="groups"','id="cards"','id="filters"','119','noindex'):
    assert required in html,required
assert not re.search(r"https?://",html),"No external URL in published draft shell"
print(f"PASS: {len(groups)} categories, {len(cards)} records; no unsafe URL/internal tokens")
