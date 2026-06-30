# Extrahepatic / organ-targeted LNP engineering literature synthesis

Curated collection of published literature on **extrahepatic and organ-targeted lipid nanoparticle (LNP) engineering** — the platform science that enables delivery of mRNA, gene-editing, and other payloads to organs and cell types beyond the liver. Complements the companion `lnp-cancer-payloads` collection, which catalogues the therapeutic payloads; this collection addresses **how to get them to the right place**.

## Scope

This collection covers studies in which the **central contribution is LNP formulation, lipid design, or delivery engineering for non-liver tissues**. Included topics:

- **Selective organ targeting (SORT)** — charged-lipid additives that redirect LNPs to lung, spleen, or other organs.
- **Ionizable lipid design** — structure–activity relationships, combinatorial libraries, linker/tail/headgroup engineering for organ tropism.
- **Lung-targeted delivery** — systemic IV formulations targeting lung endothelium; inhaled/nebulized LNPs for direct pulmonary delivery.
- **Spleen and immune-cell targeting** — anionic/zwitterionic formulations for splenic delivery; DC, macrophage, T cell, NK cell, and HSC specificity.
- **Brain / CNS delivery** — BBB-crossing ionizable lipids, receptor-mediated transcytosis, intrathecal/intranasal routes.
- **ML/AI-driven lipid discovery** — machine learning for ionizable lipid design, Bayesian optimization, graph neural networks, high-throughput in vivo barcoded screening.
- **Endosomal escape engineering** — pKa optimization, membrane-fusogenic lipid design, organ-dependent escape mechanisms.
- **Active targeting / surface engineering** — antibody-conjugated LNPs, peptide-targeted LNPs, ligand-targeted delivery, PEG-lipid engineering.
- **Biodistribution and protein corona** — corona-mediated organ tropism, in vivo fate, clearance mechanisms.

Pure infectious-disease vaccines (COVID, influenza, etc.) are excluded. Pure hepatocyte-only delivery papers are excluded unless they establish fundamental principles relevant to extrahepatic work.

## Directory structure

- `index.tsv` — curated metadata for all **189** papers, with category, topic tags, download status, and DOI/PMID/PMCID links.
- `fulltext/` — Europe PMC full-text XML (**58** papers) retrieved via the EBI REST `fullTextXML` endpoint.
- `pdfs/` — open-access PDFs (when available from publisher/PMC hosts without browser challenge).
- `notes/` — synthesis reports organized by topic (see index below).

## Notes index

- `notes/00_overview.md` — landscape, taxonomy, year distribution, recurring design themes.
- `notes/01_sort_and_organ_selective_formulation.md` — SORT mechanism, quaternary ammonium/charge-tuning, helper-lipid contributions, multi-organ targeting.
- `notes/02_ionizable_lipid_design_and_sar.md` — headgroup chemistry, linker chemistry, tail architecture, combinatorial libraries.
- `notes/03_lung_targeted_delivery.md` — systemic IV lung targeting, inhalation/nebulization challenges and formulation solutions.
- `notes/04_ml_and_hts_lipid_discovery.md` — DNA/mRNA barcoding, Bayesian optimization, graph neural networks, generative models.
- `notes/05_spleen_and_immune_cell_targeting.md` — anionic SORT, headgroup pKa tuning, DC/macrophage/T cell/HSC specificity.
- `notes/06_brain_and_cns_delivery.md` — BBB challenge, ionizable-lipid-intrinsic crossing, receptor-mediated transcytosis, AI-validated brain targeting.
- `notes/07_endosomal_escape_and_intracellular_delivery.md` — H_II phase transition, pKa as central parameter, organ-dependent escape, enhancement strategies.
- `notes/08_active_targeting_and_surface_engineering.md` — antibody-conjugated LNPs, peptide codes, small-molecule ligands, PEG engineering.
- `notes/09_biodistribution_and_protein_corona.md` — corona as biological identity, measuring biodistribution, particle vs functional delivery.

## Identification strategy

Eight complementary PubMed E-utils queries targeting the extrahepatic/organ-targeted LNP engineering space were combined and deduplicated, returning **1,998** candidate records. Records were scored for relevance using regex classification across title and abstract with topic-specific patterns; papers scoring ≥ 3 (evidence of LNP formulation novelty + organ/tissue targeting) were retained, yielding **189** papers (2013–2026, heavily weighted to 2024–2026). Papers already in the `lnp-cancer-payloads` collection (157 records) were excluded.

Queries:
1. LNP + extrahepatic/organ-targeted/tissue-selective + cancer/therapeutic
2. LNP + specific organs (lung/spleen/brain/lymph/muscle/bone/kidney) + targeting/tropism/biodistribution
3. LNP + SORT/ionizable lipid/lipid library/lipid screen + organ/tissue/cell-selective
4. LNP + immune cells (T cell/macrophage/DC/NK/HSC) + targeting/cell-selective
5. LNP + ML/AI/deep learning/HTS + lipid/formulation + delivery/targeting
6. LNP + inhalation/nebulization/intrathecal/intramuscular/subcutaneous + mRNA
7. LNP + endosomal escape/intracellular delivery/pKa + optimization/engineering
8. LNP + antibody-conjugated/peptide-targeted/ligand-targeted/aptamer + mRNA/siRNA/gene therapy

## Full-text status

- `fulltext_xml`: **58** papers (Europe PMC open-access XML via EBI REST endpoint).
- `metadata_only`: **131** papers (catalogued from title + abstract + DOI/PMID/PMCID; full text not freely accessible).

## Conventions

- `status` — `downloaded` (OA PDF in `pdfs/`), `fulltext_xml` (Europe PMC XML in `fulltext/`), or `metadata_only`.
- `category` — primary topic bucket (first matched); `topics` — all applicable tags (semicolon-separated).
- Papers are referenced in notes by first author, year, and PMID; see `index.tsv` for canonical DOI/PMID/PMCID links.
