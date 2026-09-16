# Overview — NK cells for cancer: phenotype, engineering and manufacturing

## Scope

This collection curates **313 papers (1993–2026; 94 from 2024–2026, 166 from 2020 onward)** on what actually
makes an NK-cell cancer therapy work: which **cell state** you infuse, which **genetic modifications** you
install, and which **culture and manufacturing process** you use to get there. Manufacturing is treated as
primary evidence rather than a methods footnote — 58 papers are classified as process/method studies and
244 carry culture or manufacturing content.

| Evidence class | n |
|---|---|
| Preclinical (in vivo) | 105 |
| Process / manufacturing methods | 58 |
| Clinical trials | 50 |
| Reviews | 39 |
| Mechanistic / in vitro | 33 |
| Human translational | 28 |

Open-access full-text XML was retrieved for 153 records (prioritising trials, process papers and human
studies); the remainder are catalogued from title, abstract and identifiers.

## Topic axes

| Axis | n | Core question |
|---|---|---|
| `car_nk_engineering` | 32 | Receptor architecture, costimulation, gene delivery into NK cells |
| `expansion_feeders` | 30 | Feeders, media, vessels, bioreactors, GMP scale-up |
| `clinical_nk` | 28 | What has actually been observed in patients |
| `nk_phenotype_states` | 26 | Which NK state to select, expand or induce |
| `gene_editing_knockouts` | 24 | Which brakes to delete (CISH, NKG2A, TGF-β/SMAD, CD38, Regnase-1…) |
| `cytokine_support` | 24 | IL-15/IL-21/IL-12+15+18 priming and cytokine armouring |
| `general_nk_therapy` | 22 | Cross-cutting landscape and NK biology fundamentals |
| `nk_cell_sources` | 20 | Peripheral blood, cord blood, iPSC, NK-92 |
| `nk_engagers` | 20 | BiKE/TriKE/NKCE molecules that supply specificity without gene transfer |
| `metabolism_persistence` | 18 | Metabolic fitness, hypoxia, survival after infusion |
| `checkpoints_inhibitory` | 18 | NKG2A/HLA-E, TIGIT, PD-1, KIR, TIM-3 |
| `adcc_combinations` | 18 | CD16 biology, antibody and drug combinations |
| `trafficking_solid_tme` | 18 | Homing, infiltration, suppression inside solid tumours |
| `cryo_qc_manufacturing` | 15 | Cryopreservation damage, potency assays, release testing |

Disease context is dominated by platform/pan-cancer work (149), then AML/MDS (25), lymphoma/CLL (24),
gastrointestinal (16), myeloma (15), head-and-neck/melanoma (13) and glioblastoma (11).

## The ten claims this literature supports

1. **The infused cell state matters more than the donor.** Brief IL-12+IL-15+IL-18 preactivation converts
   resting NK cells into cytokine-induced memory-like (CIML) cells whose enhanced responsiveness persists for
   weeks (Romee 2012, PMID 22983442) and translates into remissions in AML (Romee 2016, PMID 27655849).
2. **CD56bright/CD56dim is an inadequate description of the product.** scRNA-seq/CITE-seq resolves multiple
   human NK states (Rebuffet 2024, PMID 38956378) and maps tumour-infiltrating states across cancers
   (Netskar 2024, PMID 38956379; Tang 2023, PMID 37607536); CD56bright cells become potently cytotoxic after
   IL-15 priming (Wagner 2017, PMID 28972539).
3. **The tumour actively reprogrammes the product after infusion** — TGF-β-driven conversion to ILC1-like
   cells (Gao 2017, PMID 28759001), hypoxia/HIF-1α (Ni 2020, PMID 32445619), lactylation
   (2025, PMID 40494934), nutrient competition — so engineering increasingly targets resistance to the
   microenvironment rather than target recognition alone.
4. **CAR-NK signalling is not CAR-T signalling.** NK-native transmembrane/costimulatory modules
   (NKG2D-TM + 2B4 + CD3ζ; Li 2018, PMID 30082067) and, surprisingly, non-native CD28 via LCK/CD3ζ/ZAP70
   (PMID 38900051) outperform naive CAR-T architectures ported into NK cells.
5. **Cytokine armouring is the difference between a transient and a persistent product.** IL-15-armoured
   cord-blood CAR-NK cells persist and control tumours (Liu 2018, PMID 28725044) and underpin the CD19
   CAR-NK trials; loss of metabolic fitness, not antigen loss, drives relapse in preclinical CAR-NK models
   (PMID 37494448).
6. **Deleting brakes is now as important as adding receptors.** CISH (PMID 32531207), NKG2A/KLRC1
   (PMID 39349459), SMAD4 (PMID 40119192), TGFBR2, CD38 (PMID 32603414), Regnase-1 (PMID 38821052) and
   genome-wide CRISPR screens (PMID 40845844; PMID 38918616) define an actionable edit list.
7. **Expansion platforms are converging on membrane-bound IL-21/4-1BBL feeders or their cell-free
   equivalents.** K562-mb15-41BBL (Imai/Fujisaki 2009, PMID 19383914), mbIL-21 aAPC and PM21 particles
   (PMID 27059202) give log-scale expansion; feeder-free media, G-Rex/gas-permeable vessels, CliniMACS
   Prodigy and stirred bioreactors carry it into GMP.
8. **Cryopreservation is a first-order efficacy variable, not a logistics detail.** Cryopreserved NK cells
   lose 3D migration and cytotoxicity even when degranulation assays look normal (Mark 2020, PMID 33067467);
   DMSO-free formulations and post-thaw rescue strategies are an active 2024–2026 workstream.
9. **Clinical activity is real but concentrated where the product is armoured and the target is
   haematological.** CD19 CAR-NK (Liu 2020, PMID 32023374; Marin 2024, PMID 38238616), iPSC-derived FT596
   (PMID 39798981), 4-1BB CAR-NK (PMID 40251398), CIML NK (PMID 35349491) and AFM13-loaded cord-blood NK
   (PMID 40186077) show responses without CRS/ICANS or GvHD; solid-tumour benefit remains sparse.
10. **Efficacy is a product of the whole chain.** The same edit or CAR gives different results depending on
    feeder, medium, cytokine schedule, cryopreservation and lymphodepletion — which is why the manufacturing
    literature in this collection is not separable from the biology.

## How to read the collection

- `notes/01`–`10` are the narrative synthesis, ordered from cell state to clinical translation.
- `REPORT.md` is auto-generated from `index.tsv` (never hand-edited) and lists every paper by axis and
  evidence class.
- Papers are cited as first author, year and PMID; `index.tsv` carries venue, citation count, DOI, PMCID and
  the local full-text path where available.
- Reproduce with `python3 harvest.py && python3 curate.py && python3 fetch_fulltext.py && python3 gen_report.py && python3 build_pdf.py`.
