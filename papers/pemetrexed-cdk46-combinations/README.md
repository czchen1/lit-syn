# Pemetrexed + CDK4/6 inhibitor combinations — literature synthesis

Curated collection of clinical and preclinical literature on combining the antifolate **pemetrexed** (and, more broadly, antimetabolite chemotherapy) with **CDK4/6 inhibitors** (palbociclib, ribociclib, abemaciclib, and the myeloprotective agent trilaciclib). The central question is whether — and *how* — CDK4/6 inhibition can be combined with pemetrexed-based chemotherapy, given that the two drug classes act on opposite phases of the cell cycle (CDK4/6i → G1 arrest; pemetrexed → S-phase blockade), which creates both **synergy** and **antagonism** opportunities depending on schedule and disease context.

## Scope

Direct pemetrexed + CDK4/6i evidence is sparse, so this collection is organized in concentric rings of relevance:

1. **Direct pemetrexed + CDK4/6i** — studies that actually combine pemetrexed with a CDK4/6 inhibitor (clinical and preclinical).
2. **CDK4/6i + chemotherapy in NSCLC / pleural mesothelioma** — the disease settings where pemetrexed is the standard chemotherapy backbone; establishes the clinical rationale and combination biology.
3. **Trilaciclib + chemotherapy (myeloprotection)** — trilaciclib is a CDK4/6i given transiently *before* cytotoxic chemotherapy (including platinum and gemcitabine regimens) to protect bone marrow and immune cells; a distinct but directly relevant "CDK4/6i + chemo" modality.
4. **CDK4/6i × antimetabolite mechanism** — preclinical work on how CDK4/6 inhibition interacts with antimetabolites (5-FU, cytarabine, gemcitabine, methotrexate, nucleoside/folate analogues), including the SAMHD1 axis, S-phase antagonism, and sequencing dependence — the mechanistic basis that governs whether a pemetrexed + CDK4/6i combination helps or hurts.

Pure endocrine-therapy breast-cancer CDK4/6i trials (letrozole/fulvestrant + palbociclib etc.), cost-effectiveness analyses, and papers where pemetrexed and a CDK4/6i merely co-occur in a drug list are excluded.

## Directory structure

- `index.tsv` — curated metadata for all **108** papers (category, authors, title, venue, year, PMID, DOI, PMCID, URL, topic tags, download status).
- `fulltext/` — Europe PMC open-access full-text XML (**53** papers) retrieved via the EBI REST `fullTextXML` endpoint.
- `notes/` — synthesis reports (see index below).

## Notes index

- `notes/00_overview.md` — landscape, the G1-vs-S-phase paradox, taxonomy, key takeaways.
- `notes/01_direct_pemetrexed_cdk46.md` — the direct clinical and preclinical pemetrexed + CDK4/6i evidence.
- `notes/02_cdk46_chemo_nsclc_mesothelioma.md` — CDK4/6i + chemotherapy in NSCLC and pleural mesothelioma (pemetrexed disease contexts).
- `notes/03_trilaciclib_myeloprotection.md` — trilaciclib given before chemotherapy for myelopreservation and immune enhancement.
- `notes/04_mechanism_antimetabolite_interactions.md` — CDK4/6i × antimetabolite mechanism, SAMHD1, S-phase antagonism, and schedule dependence.

## Identification strategy

Six complementary PubMed E-utils queries were combined and deduplicated (**1,299** candidate records), then scored by regex classification over title + abstract into the four relevance tiers above; obvious off-topic records (drug-list co-occurrences, cost/registry/pharmacovigilance studies, unrelated case reports, natural-product screens) were pruned, yielding **108** papers (2012–2026; 86 from 2020 onward, including 21 clinical trials / randomized studies).

Queries:
1. `pemetrexed` AND `CDK4/6 inhibitor` (all fields)
2. antimetabolite / antifolate / thymidylate synthase / nucleoside analogue AND CDK4/6 inhibitor
3. `pemetrexed` AND (palbociclib OR ribociclib OR abemaciclib OR trilaciclib OR dalpiciclib)
4. CDK4/6 inhibitor AND chemotherapy AND (sequence / schedule / antagonism / S-phase / cell-cycle arrest)
5. trilaciclib / Cosela / G1T28 AND (chemotherapy / pemetrexed / platinum / myeloprotection)
6. CDK4/6 inhibitor AND (NSCLC / lung adenocarcinoma / mesothelioma) AND (chemotherapy / pemetrexed / platinum / combination)

## Full-text status

- `fulltext_xml`: **53** papers (Europe PMC open-access XML via EBI REST endpoint).
- `metadata_only`: **55** papers (catalogued from title + abstract + DOI/PMID/PMCID; full text not freely accessible in this environment).

## Conventions

- `status` — `fulltext_xml` (Europe PMC XML in `fulltext/`) or `metadata_only`.
- `category` — primary relevance tier; `topics` — all applicable tags (semicolon-separated).
- Papers are referenced in notes by first author, year, and PMID; see `index.tsv` for canonical DOI/PMID/PMCID links.
