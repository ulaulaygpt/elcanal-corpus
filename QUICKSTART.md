# El Canal Corpus — Quick start

This repository is the machine-readable map of the public El Canal corpus.

If you only need to browse the project as a person, start at [elcanal.es](https://elcanal.es). Use this repository when you want to inspect the corpus as data.

## The four useful files

- `corpus-index.yml` — the 62-DOI perimeter represented on the public website snapshot.
- `metadata/zenodo-records.json` — public archival metadata fetched from Zenodo for those same DOI records.
- `generated/catalog.json` — joined website + Zenodo view.
- `generated/relations.json` — explicit DOI-to-DOI relations declared in Zenodo metadata, restricted to the public corpus perimeter.

## Example: list DOI and titles

No external Python packages are required:

```bash
python - <<'PY'
import json
d=json.load(open("generated/catalog.json", encoding="utf-8"))
for r in d["records"]:
    print(r["doi"], "—", r["public_title"])
PY
```

## Example: inspect one DOI

```bash
python - <<'PY'
import json
doi="10.5281/zenodo.22977400"
d=json.load(open("generated/catalog.json", encoding="utf-8"))
for r in d["records"]:
    if r["doi"] == doi:
        print(json.dumps(r, ensure_ascii=False, indent=2))
        break
PY
```

## Example: show outgoing relations

```bash
python - <<'PY'
import json
doi="10.5281/zenodo.22977400"
g=json.load(open("generated/relations.json", encoding="utf-8"))
for e in g["edges"]:
    if e["source_doi"] == doi:
        print(e["relation"], "→", e["target_doi"])
PY
```

## Important distinction

The repository deliberately keeps separate:

1. what the public website displays;
2. what Zenodo preserves as archival metadata;
3. what the curated registry marks as current.

Do not treat a title mismatch or version drift as an error by default. See [METHODOLOGY.md](METHODOLOGY.md) and `generated/consistency.json`.

## Wider ecosystem

- [CAP](https://github.com/ulaulaygpt/elcanal-cap)
- [PTC/CTP](https://github.com/ulaulaygpt/ptc-ctp)
- [Validator](https://github.com/ulaulaygpt/ptc-validator)
- [GitHub profile map](https://github.com/ulaulaygpt)
