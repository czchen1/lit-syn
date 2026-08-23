# Delivery to the pons: DIPG and related diseases — literature synthesis

Curated collection of published literature on **how therapeutics are physically delivered
to the pons and brainstem**, centred on diffuse intrinsic pontine glioma (DIPG) /
H3K27-altered diffuse midline glioma (DMG) and extended to other CNS diseases whose
direct-delivery experience transfers technically.

The organising question is not *which drug* but *by what route, in what volume, with what
distribution, for how long, and how do you know it got there*.

## Scope

Included:

- **Disease-specific delivery work** in DIPG/DMG, brainstem glioma, and pediatric
  high-grade glioma — preclinical and clinical.
- **General CNS delivery technique** papers (mostly glioblastoma or large-animal work)
  when the technique is directly applicable to a pontine target.
- **Related-disease direct delivery** — kept only where a direct route (parenchymal
  infusion/CED, CSF/intrathecal/ICV, focused ultrasound, intra-arterial, implanted device)
  was used in humans or large animals: neuronopathic Gaucher disease, AADC deficiency,
  Parkinson disease, SMA, CLN2/CLN7, MPS II and related lysosomal disorders.

Excluded: pontine stroke/haemorrhage, central pontine myelinolysis, brainstem auditory
and brain-death literature, cerebrovascular thrombectomy, and health-services /
cost-effectiveness papers.

## Directory structure

- `index.tsv` — curated metadata for all **1,066** records (category, topics, PMID/DOI/PMCID, canonical URL, status).
- `fulltext/` — Europe PMC open-access full-text XML (**494** records) via the EBI REST `fullTextXML` endpoint.
- `notes/` — synthesis notes organised by delivery modality (index below).
- `REPORT.md` — cross-modality synthesis: comparison, evidence maturity, gaps.
- `pontine_delivery_review.pdf` — standalone 85-page review (report + all notes + full reference list), built by `build_pdf.py`.
- `harvest.py`, `harvest_seeds.py`, `harvest_gaps.py`, `harvest_related.py` — Europe PMC harvest scripts.
- `curate.py` — scoring/classification/deduplication, writes `index.tsv`.
- `fetch_fulltext.py` — full-text XML retrieval, updates `index.tsv` status.
- `raw_harvest.json` — deduplicated raw harvest (**7,195** records) before curation.

## Notes index

- `notes/00_overview.md` — why the pons is a delivery problem; route taxonomy; cross-cutting determinants.
- `notes/01_convection_enhanced_delivery.md` — CED: preclinical brainstem work, DIPG clinical trials, safety/mechanics, residence time.
- `notes/02_focused_ultrasound.md` — FUS-mediated BBB opening: preclinical DMG models, pediatric trials, posterior-fossa constraints.
- `notes/03_intra_arterial_and_bbb_disruption.md` — superselective intra-arterial infusion and osmotic BBB disruption; posterior-circulation risk.
- `notes/04_csf_and_intraventricular_routes.md` — intrathecal, intraventricular, fourth-ventricle and intracisternal delivery; reservoirs and CSF dynamics.
- `notes/05_cell_and_viral_vector_delivery.md` — locoregional/ICV CAR-T, cellular carriers, oncolytic viruses, AAV route comparisons.
- `notes/06_nanocarriers_and_intranasal.md` — nanocarriers as route modifiers; nose-to-brain and FUS-assisted intranasal delivery.
- `notes/07_implants_depots_and_devices.md` — depots, wafers, hydrogels, pumps, ports and access hardware.
- `notes/08_bbb_biology_and_systemic_pharmacology.md` — pontine BBB/BBTB biology, ABC efflux, BBB-penetrant systemic pharmacology.
- `notes/09_surgical_access_imaging_and_modeling.md` — biopsy, safe entry zones, trajectories, distribution imaging, dosimetry and modelling.
- `notes/10_related_diseases_lessons.md` — what CLN2/MPS/SMA/Gaucher/AADC direct-delivery experience does and does not transfer.
- `notes/11_radiation_as_delivery_partner.md` — radiotherapy as comparator and partner, including CED radioisotopes and BNCT.

## Identification strategy

Europe PMC REST `search` (core results, 100/page, throttled) across four harvest passes:

1. `harvest.py` — disease terms (DIPG, DMG, H3K27M, brainstem/pontine glioma, pediatric HGG) crossed with 14 modality groups (CED, FUS, intra-arterial, intrathecal/CSF, cell therapy, viral vectors, nanoparticles, intranasal, systemic BBB pharmacology, implants/devices, imaging/modelling, surgical access, radiation, antibody conjugates/BBB shuttles).
2. `harvest_seeds.py` — foundational/early literature (1980s–2000s CED, osmotic BBB disruption, intra-arterial chemotherapy, intraventricular therapy, surgical approaches).
3. `harvest_gaps.py` — gaps found by reading category digests: fourth-ventricle/cisternal infusion, named DIPG programmes and devices, intranasal delivery, antibody-conjugate/BBB-shuttle strategies, imaging/dosimetry/modelling, brainstem BBB biology.
4. `harvest_related.py` — related-disease direct delivery (MR-guided AAV, Gaucher CED, intrathecal ASO/enzyme replacement, FUS in Parkinson/Alzheimer disease).

Combined and deduplicated by PMID/DOI/PMCID and by normalised title (removing
journal/preprint and duplicate-abstract pairs) → **7,195** candidate records.

`curate.py` then scores each record over title+abstract for disease context and modality
evidence and keeps a record when one of three rules is satisfied:

- `brainstem_specific` (530) — DIPG/DMG or brainstem context **plus** delivery evidence.
- `cns_technique` (373) — route evidence in the **title**, strong modality score, and CNS-tumour context.
- `related_disease` (163) — non-oncologic CNS disease **plus** a direct route in the title **plus** explicit direct-administration language.

Retained: **1,066** records (1989–2026; 456 from 2024 onwards). Titles are HTML-unescaped
and tag-stripped; conference/meeting abstracts are kept but tagged `meeting_abstract`
(144 records) because much DIPG delivery work appears first in SNO/ISPNO abstracts.

## Category distribution

| Category | n |
|---|---|
| convection_enhanced_delivery | 225 |
| focused_ultrasound | 160 |
| nanoparticle | 117 |
| cell_therapy_delivery | 102 |
| intrathecal_csf | 82 |
| systemic_bbb_pharmacology | 74 |
| viral_vector | 72 |
| implant_depot_device | 65 |
| surgical_access | 63 |
| radiation_combined | 42 |
| intra_arterial | 24 |
| intranasal | 20 |
| antibody_conjugate_shuttle | 15 |
| imaging_dosimetry_modeling | 5 |

`category` is the primary (highest-scoring) modality; `topics` lists all matched
modalities plus disease tags, so totals in the notes exceed the table.

## Full-text status

- `fulltext_xml`: **494** records (Europe PMC open-access XML in `fulltext/`).
- `metadata_only`: **572** records (title/abstract/identifiers only — includes all meeting abstracts and non-OA articles).

## Conventions

- `status` — `fulltext_xml` (XML in `fulltext/`) or `metadata_only`.
- Full-text filenames: `fulltext/<firstauthor>_<year>_pmid<id>.xml`.
- Notes cite papers by first author, year and PMID; `index.tsv` holds canonical links.
  Meeting abstracts have no PMID and are cited by abstract number and year.
