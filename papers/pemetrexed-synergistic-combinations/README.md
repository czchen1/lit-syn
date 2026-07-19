# Combinations synergistic with pemetrexed — literature synthesis

Curated collection of clinical and preclinical literature on **agents and modalities that synergize with pemetrexed**, spanning the standard platinum backbone, immunotherapy, antiangiogenics, EGFR/ALK/MET TKIs, DNA-damage-response and cell-cycle-checkpoint inhibitors, signaling/apoptosis-pathway drugs, folate-pathway/thymidylate-synthase modulators, radiosensitization, and repurposed agents.

Pemetrexed is a multitargeted antifolate (inhibits thymidylate synthase, dihydrofolate reductase, and GARFT), depleting thymidine and purine pools and killing cells in **S phase**. This mechanism makes it a productive partner for drugs that (a) raise its intracellular activation or target expression, (b) block the DNA-repair/checkpoint responses that let cells survive nucleotide depletion, or (c) attack complementary survival pathways — the recurring logic across this collection.

## Scope and organization

The collection is organized by **partner class**, and each paper is additionally tagged by **evidence type**:
- `preclinical_synergy` — explicit demonstration of synergy/sensitization/potentiation (combination index / Chou-Talalay / isobologram, or resistance reversal). **307 papers.**
- `clinical_landmark` — practice-defining or registrational clinical combination trials (Phase III / randomized / KEYNOTE / registrational). **82 papers.**

Partner-class categories (see notes for detail):

| Category | n | Notes file |
|---|---|---|
| immunotherapy | 70 | `02_immunotherapy.md` |
| chemo_partner (platinum/gemcitabine/taxane backbone) | 59 | `01_chemotherapy_backbone.md` |
| folate_ts_modulation | 53 | `07_folate_pathway_and_ts.md` |
| egfr_tki | 52 | `04_egfr_alk_met_tki.md` |
| targeted_signaling | 47 | `06_signaling_and_apoptosis.md` |
| antiangiogenic | 27 | `03_antiangiogenic.md` |
| ddr_inhibitor | 24 | `05_ddr_and_cell_cycle.md` |
| radiosensitization | 18 | `08_radiosensitization.md` |
| alk_ros1_met_tki | 9 | `04_egfr_alk_met_tki.md` |
| repurposed_natural | 6 | `09_repurposed_agents.md` |
| onc201_imipridone | 11 | `10_report_onc201_gallium_and_synergy_landscape.md` |
| gallium_iron_rnr | 10 | `10_report_onc201_gallium_and_synergy_landscape.md` |
| rnr_inhibition | 3 | `10_report_onc201_gallium_and_synergy_landscape.md` |

## Directory structure

- `index.tsv` — curated metadata for all **389** papers (category, evidence, authors, title, venue, year, PMID, DOI, PMCID, URL, topic tags, download status).
- `fulltext/` — Europe PMC open-access full-text XML (**157** papers) retrieved via the EBI REST `fullTextXML` endpoint.
- `notes/` — synthesis reports (see index below).

## Notes index

- `notes/00_overview.md` — synergy logic, landscape, taxonomy, cross-cutting themes.
- `notes/01_chemotherapy_backbone.md` — platinum (cisplatin/carboplatin), gemcitabine, taxanes; scheduling and mechanism.
- `notes/02_immunotherapy.md` — anti-PD-(L)1 + pemetrexed/platinum (KEYNOTE-189 and beyond).
- `notes/03_antiangiogenic.md` — bevacizumab, nintedanib, anlotinib, ramucirumab.
- `notes/04_egfr_alk_met_tki.md` — EGFR-TKI + chemo (FLAURA2, aumolertinib), amivantamab, ALK/MET combinations.
- `notes/05_ddr_and_cell_cycle.md` — WEE1, CHK1, ATR, PARP, and other checkpoint/DNA-repair synergies.
- `notes/06_signaling_and_apoptosis.md` — BCL-XL/MCL-1, mTOR/PI3K, HSP90, SRC, PLK1, HDAC, NAMPT, arginine deprivation.
- `notes/07_folate_pathway_and_ts.md` — thymidylate synthase, PCFT/RFC transport, folate metabolism, resistance reversal.
- `notes/08_radiosensitization.md` — pemetrexed as radiosensitizer and combinations that enhance it.
- `notes/09_repurposed_agents.md` — metformin, ferroptosis inducers, natural products, delivery-enabled combinations.
- `notes/10_report_onc201_gallium_and_synergy_landscape.md` — **report**: mechanistic evaluation of ONC201/ONC206 (imipridone/ClpP/DRD2) and gallium maltolate (iron-mimetic RNR inhibitor) with pemetrexed, integrated with the full synergy landscape.

## Identification strategy

Eleven PubMed E-utils queries (pemetrexed × synergy; × immunotherapy; × antiangiogenic; × EGFR-TKI; × ALK/MET; × DDR; × platinum/mechanism; × signaling/apoptosis; × folate/TS; × radiation; × repurposed) were combined and deduplicated (**2,560** candidates). Records were scored by regex classification into partner classes; papers were retained if they showed **explicit synergy/sensitization evidence** or were **landmark clinical combination trials**, then off-topic records were pruned, yielding an initial **365** papers (2001–2026; 174 from 2018 onward); KEYNOTE-189 was added explicitly as the foundational IO + pemetrexed trial. A targeted follow-up search (six queries on ONC201/ONC206 imipridones, gallium/iron/RNR, and RNR-inhibitor × antimetabolite biology; 752 dedup candidates) added **24** papers to ground the ONC201/206 and gallium maltolate report — bringing the total to **389**.

## Full-text status

- `fulltext_xml`: **157** papers (Europe PMC open-access XML).
- `metadata_only`: **232** papers (catalogued from title + abstract + DOI/PMID/PMCID).

## Conventions

- `status` — `fulltext_xml` (Europe PMC XML in `fulltext/`) or `metadata_only`.
- `category` — primary partner class; `evidence` — `preclinical_synergy` or `clinical_landmark`; `topics` — all applicable tags (semicolon-separated).
- Papers are referenced in notes by first author, year, and PMID; see `index.tsv` for canonical links.
