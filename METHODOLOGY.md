# Methodology

This repository separates four different public views of El Canal instead of forcing them into a single source.

## 1. Public website perimeter

`corpus-index.yml` is a snapshot of the DOI-bearing records represented on the public corpus page at elcanal.es.

It preserves:
- the section used by the website;
- the title displayed to human readers;
- the DOI.

The website title is treated as a presentation label. It is not silently substituted for Zenodo metadata.

## 2. Archival metadata

`metadata/zenodo-records.json` is generated from the public Zenodo REST API for exactly the 62 DOI records in `corpus-index.yml`.

Zenodo provides the archival metadata layer: canonical record title, publication date, version, resource type, license, creators, ORCID data when present, keywords, concept DOI and declared related identifiers.

## 3. Merged machine-readable catalogue

`generated/catalog.json` joins the website perimeter and Zenodo metadata by DOI while preserving both title fields.

A title difference is recorded, not corrected automatically.

`generated/consistency.json` currently reports:
- 62 records;
- 30 exact website-title / Zenodo-title matches;
- 32 title differences.

Most differences are editorial shortening, multilingual expansion, punctuation or version wording. The file is a diagnostic surface, not an assertion that either source is wrong.

## 4. Explicit relation graph

`generated/relations.json` contains only relations explicitly declared in Zenodo metadata where both endpoints belong to the 62-DOI public perimeter.

Current graph:
- 62 nodes;
- 237 internal directed relation edges.

No semantic relation is invented by the repository.

## Curated current layer

`registry.yml` is different from the 62-DOI website snapshot. It is a curated layer for current versions, repository links and statuses that have already been normalized.

Because publication surfaces do not always update at the same moment, a current public Zenodo object may appear in `registry.yml` before it appears on the public corpus page. Such divergence must be recorded rather than hidden.

## Source precedence

For archival identity, DOI metadata and preserved releases: **Zenodo**.

For public presentation and conceptual grouping: **elcanal.es**.

For versionable structure, machine-readable joins, validations and derived graphs: **GitHub**.

The repository never silently reconciles disagreements between those layers.
