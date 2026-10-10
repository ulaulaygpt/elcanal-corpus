#!/usr/bin/env python3
from pathlib import Path
import json, re, unicodedata

INDEX = Path("corpus-index.yml")
META = Path("metadata/zenodo-records.json")
OUT = Path("generated")

def parse_index(text):
    entries=[]
    current={}
    for raw in text.splitlines():
        line=raw.strip()
        m=re.match(r'-\s+section:\s+"(.*)"$', line)
        if m:
            if current:
                entries.append(current)
            current={"section":m.group(1)}
            continue
        m=re.match(r'title:\s+"(.*)"$', line)
        if m and current is not None:
            current["public_title"]=m.group(1)
            continue
        m=re.match(r'doi:\s+"(.*)"$', line)
        if m and current is not None:
            current["doi"]=m.group(1)
    if current:
        entries.append(current)
    return entries

def norm(s):
    s=unicodedata.normalize("NFKC", s or "")
    s=re.sub(r"\s+", " ", s).strip().casefold()
    return s

index=parse_index(INDEX.read_text(encoding="utf-8"))
meta=json.loads(META.read_text(encoding="utf-8"))["records"]
meta_by_doi={r["doi"]:r for r in meta}
index_dois=[e["doi"] for e in index]

if len(index)!=62 or len(set(index_dois))!=62:
    raise SystemExit(f"Index perimeter invalid: {len(index)} entries / {len(set(index_dois))} unique DOIs")
if set(index_dois)!=set(meta_by_doi):
    missing_meta=sorted(set(index_dois)-set(meta_by_doi))
    missing_index=sorted(set(meta_by_doi)-set(index_dois))
    raise SystemExit(f"Index/metadata DOI mismatch. Missing metadata={missing_meta}; missing index={missing_index}")

catalog=[]
for e in index:
    z=meta_by_doi[e["doi"]]
    catalog.append({
        "section": e["section"],
        "doi": e["doi"],
        "public_title": e["public_title"],
        "zenodo_title": z.get("title"),
        "title_exact_match": e["public_title"] == z.get("title"),
        "title_normalized_match": norm(e["public_title"]) == norm(z.get("title")),
        "record_id": z.get("record_id"),
        "concept_doi": z.get("conceptdoi"),
        "publication_date": z.get("publication_date"),
        "version": z.get("version"),
        "resource_type": z.get("resource_type"),
        "resource_subtype": z.get("resource_subtype"),
        "license": z.get("license"),
        "language": z.get("language"),
        "creators": z.get("creators") or [],
        "keywords": z.get("keywords") or [],
        "zenodo_url": z.get("zenodo_url"),
    })

corpus=set(index_dois)
edges=[]
for source in meta:
    sdoi=source["doi"]
    for rel in source.get("related_identifiers") or []:
        target=rel.get("identifier")
        if target in corpus:
            edges.append({
                "source_doi": sdoi,
                "relation": rel.get("relation"),
                "target_doi": target,
                "resource_type": rel.get("resource_type"),
                "scheme": rel.get("scheme"),
            })

dedup=[]
seen=set()
for edge in edges:
    key=(edge["source_doi"],edge["relation"],edge["target_doi"])
    if key not in seen:
        seen.add(key)
        dedup.append(edge)

mismatches=[
    {
        "doi":x["doi"],
        "public_title":x["public_title"],
        "zenodo_title":x["zenodo_title"],
        "normalized_match":x["title_normalized_match"],
    }
    for x in catalog if not x["title_exact_match"]
]

OUT.mkdir(exist_ok=True)
(OUT/"catalog.json").write_text(
    json.dumps({
        "schema_version":1,
        "record_count":len(catalog),
        "sources":["corpus-index.yml","metadata/zenodo-records.json"],
        "records":catalog
    },ensure_ascii=False,indent=2)+"\n", encoding="utf-8"
)
(OUT/"relations.json").write_text(
    json.dumps({
        "schema_version":1,
        "node_count":len(corpus),
        "edge_count":len(dedup),
        "scope":"Relations explicitly declared in Zenodo metadata where both endpoints are in the 62-DOI public corpus perimeter.",
        "edges":dedup
    },ensure_ascii=False,indent=2)+"\n", encoding="utf-8"
)
(OUT/"consistency.json").write_text(
    json.dumps({
        "schema_version":1,
        "record_count":len(catalog),
        "index_metadata_doi_sets_match":True,
        "exact_title_match_count":len(catalog)-len(mismatches),
        "title_mismatch_count":len(mismatches),
        "title_mismatches":mismatches
    },ensure_ascii=False,indent=2)+"\n", encoding="utf-8"
)

print(f"PASS: built {len(catalog)} records, {len(dedup)} internal relation edges, {len(mismatches)} title mismatches.")
