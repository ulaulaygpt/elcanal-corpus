# El Canal — Public Corpus Registry

Machine-readable and auditable registry of the public **El Canal / Applied Cognitive Symbology (ACS)** corpus.

The public corpus currently represented on elcanal.es contains **62 unique DOIs** spanning technical protocols, software, conceptual research, ACS/LEA/MOA materials, validations, observatory outputs and narrative or historical works.

## Current machine-readable state

The repository now exposes four complementary layers:

- `corpus-index.yml` — the complete deduplicated **62-DOI website perimeter**;
- `metadata/zenodo-records.json` — archival metadata fetched from Zenodo for the same 62 records;
- `generated/catalog.json` — merged website + Zenodo catalogue preserving both source views;
- `generated/relations.json` — explicit internal relation graph derived only from Zenodo-declared relations.

The current graph contains **62 nodes and 237 internal directed relation edges**.

`generated/consistency.json` preserves source differences rather than erasing them. At the present snapshot, **30 titles match Zenodo exactly and 32 differ** because of public-facing shortening, multilingual expansion, punctuation or version wording.

## Curated current layer

`registry.yml` remains the normalized current layer for records whose version, status, repository or role has already been curated.

It is intentionally distinct from the website snapshot. For example, **CAP v0.3 (10.5281/zenodo.23138399)** is already a public Zenodo release with its two canonical ZIP artefacts, while the current website corpus snapshot still represents CAP v0.2. That divergence is recorded in `reports/curated-vs-web-corpus.json` rather than silently reconciled.

## Purpose

This repository is not a replacement for Zenodo or elcanal.es.

- **Zenodo** preserves and cites closed artefacts.
- **GitHub** exposes versionable structure, DOI lineage, machine-readable joins and explicit relationships.
- **elcanal.es** presents the corpus to human readers and provides conceptual navigation.

See `METHODOLOGY.md` for source precedence and derivation rules.

## Publication rule

Only public, closed and unambiguous records should enter the registry. Private material, drafts, sensitive Observatorio data, SERATA internals and operator memory are excluded.

## Provenance

Maintainer: **Manuel Barrera Anglada**  
ORCID: https://orcid.org/0009-0000-8891-7021  
Project: **El Canal — Applied Cognitive Symbology (ACS)**  
Website: https://elcanal.es

> El Canal propone. El humano decide.
