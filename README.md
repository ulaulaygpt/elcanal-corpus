# El Canal — Public Corpus Registry

Machine-readable and auditable registry of the public **El Canal / Applied Cognitive Symbology (ACS)** corpus.

The public corpus currently represented on elcanal.es contains **62 unique DOIs** spanning technical protocols, software, conceptual research, ACS/LEA/MOA materials, validations, observatory outputs and narrative or historical works.

## Complete DOI inventory

`corpus-index.yml` now contains the **complete deduplicated 62-DOI inventory** represented on the public corpus page of elcanal.es. It preserves the public section and displayed title for each DOI and acts as the machine-readable perimeter of the public corpus.

`registry.yml` remains the richer curated layer for records whose versions, status, repositories and relations have already been normalized. The two files therefore have different roles: **inventory first, semantic enrichment second**.

## Purpose

This repository is not a replacement for Zenodo or elcanal.es.

- **Zenodo** preserves and cites closed artefacts.
- **GitHub** exposes versionable structure, DOI lineage and machine-readable relationships.
- **elcanal.es** presents the corpus to human readers and provides conceptual navigation.

## Publication rule

Only public, closed and unambiguous records should enter the registry. Private material, drafts, sensitive Observatorio data, SERATA internals and operator memory are excluded.

## Planned machine-readable fields

Each record may expose:

- stable internal id;
- title;
- version;
- publication date;
- resource type;
- language(s);
- DOI;
- concept DOI when applicable;
- status (current / historical / superseded);
- repository, site or implementation links;
- relations to other El Canal artefacts.

## Provenance

Maintainer: **Manuel Barrera Anglada**  
ORCID: https://orcid.org/0009-0000-8891-7021  
Project: **El Canal — Applied Cognitive Symbology (ACS)**  
Website: https://elcanal.es

> El Canal propone. El humano decide.
