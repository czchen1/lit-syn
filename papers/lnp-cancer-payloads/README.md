# LNP novel-payload cancer literature synthesis

Curated collection of published literature on **lipid-nanoparticle (LNP) delivery of novel, non-vaccine payloads for cancer**, with an explicit focus on *what is encoded and why* — mRNA/RNA/DNA cargoes that turn the patient's own cells into a therapeutic factory — rather than on tumour-antigen vaccines. Includes commentary extracted from main texts and Europe PMC full-text XML wherever open access permitted.

## Scope

This collection is restricted to studies in which an **LNP (or closely related lipid/lipidoid/lipopolyplex nanoparticle) delivers a genetically-encoded payload with a cancer therapeutic intent**, where the payload is something other than a tumour-antigen / neoantigen vaccine. Included payload classes:

- **In vivo / in situ CAR and immune-cell engineering** — LNP-mRNA (or mcDNA/transposon) that generates CAR-T, CAR-macrophage, or CAR-NK cells directly inside the patient.
- **Cytokine and immunomodulator payloads** — IL-12, IL-15, IL-18, IL-21, IL-23, IL-36γ, IFN-α/γ, OX40L, 4-1BBL, STING/RIG-I agonist proteins encoded as mRNA/saRNA/circRNA for intratumoural or organ-targeted expression.
- **Secreted antibody, nanobody and T-cell-engager payloads** — mRNA/saRNA encoding bispecific T-cell engagers (BiTEs), macrophage engagers, nanobody-BiTEs, and full antibodies expressed *in situ*.
- **Tumour-suppressor restoration** — mRNA encoding p53, PTEN, p21/CDKN1A, LATS1, NDRG2 and other suppressors as a replacement-therapy strategy.
- **Gene editing** — CRISPR-Cas9/Cas12/Cas13, base editing, prime editing, RNA/3′UTR editing, epigenetic editing delivered as mRNA+gRNA, RNP, or pDNA.
- **Self-amplifying / replicon RNA and small-activating RNA (saRNA/srRNA/RNAa)**.
- **Circular RNA (circRNA) and circular single-stranded DNA (cssDNA)** coding payloads.
- **Suicide-gene / prodrug-enzyme / toxin payloads** (e.g. cytosine deaminase–UPRT, gasdermin, HSV-TK).
- **Transcription-factor and cell-reprogramming payloads** (BATF, IRF8, NF-κB-inducing kinase, β-catenin modulation, M2→M1 macrophage reprogramming).
- **Payload-agnostic LNP engineering** papers (ionizable-lipid libraries, organ-/cell-targeting, extrahepatic tropism) are included when the demonstrated application is a cancer payload above.

Bulk **prophylactic / therapeutic mRNA cancer vaccines** (tumour-antigen or neoantigen LNP vaccines) are *excluded* except for a small number of seminal reviews that frame the payload landscape. Pure siRNA/ASO knockdown papers are excluded unless co-delivered with one of the payloads above.

## Directory structure

- `index.tsv` — curated metadata for all **157** papers, with topic tags, download status, and DOI/PMID/PMCID links.
- `pdfs/` — open-access PDFs of main texts (**14** papers; publisher/PMC hosts reachable without a browser challenge).
- `fulltext/` — Europe PMC full-text XML (**73** papers) retrieved via the EBI REST `fullTextXML` endpoint, used as the text source for synthesis where no OA PDF was available.
- `notes/` — synthesis reports extracting payload design, delivery/targeting, and translational commentary, organised by topic.

## Notes index

- `notes/00_overview.md` — landscape, payload taxonomy, paper counts, eras, recurring design themes, and conventions used in this collection.
- `notes/01_in_vivo_car_and_immune_cell_engineering.md` — in situ CAR-T / CAR-M / CAR-NK generation: targeting ligands (anti-CD5/CD3/CD7/CD8 antibodies and VHH nanobodies), mRNA vs DNA/transposon cargo, transient vs integrating expression, and imaging/quality-control of the in-patient product.
- `notes/02_cytokine_and_immunomodulator_payloads.md` — encoded IL-12 and cytokine cocktails, interferons, OX40L/IL-23/IL-36γ (mRNA-2752), STING/innate agonists, and strategies to localise toxic cytokines.
- `notes/03_secreted_antibody_and_engager_payloads.md` — mRNA/saRNA-encoded BiTEs, macrophage engagers, nanobody-BiTEs and antibody fusions; organ-targeted *in situ* secretion.
- `notes/04_tumor_suppressor_restoration.md` — p53, PTEN, p21, LATS1, NDRG2 mRNA replacement; co-delivery with siRNA; route-specific (intravesical, intravitreal, transdermal, intratumoural) restoration.
- `notes/05_gene_editing_payloads.md` — CRISPR/Cas mRNA+gRNA, RNP, base/prime/RNA editing; targets (SOX2, PLK1, KRAS-G12S, CDK4/6, PD-1/TRAC/B2M); extrahepatic and cell-targeted editing.
- `notes/06_self_amplifying_and_circular_rna.md` — saRNA/srRNA replicons, alphavirus VLV systems, cascade amplification, RNAa small-activating RNA, and circRNA/cssDNA coding payloads.
- `notes/07_suicide_gene_prodrug_and_tf_reprogramming.md` — gene-directed enzyme-prodrug (CD-UPRT/5-FC) and toxin payloads, plus transcription-factor enforcement (BATF, IRF8, NIK) and macrophage/tumour reprogramming.
- `notes/08_lnp_engineering_and_targeting.md` — ionizable-lipid libraries, SORT/organ-selective and cell-targeted LNPs, extrahepatic (lung, spleen, brain, HSC) delivery, and co-delivery/co-encapsulation chemistry enabling these payloads.
- `notes/09_per_paper_extractions.md` — capsule entry per paper summarising construct, payload, delivery route/targeting, model, and headline result.

## Identification strategy

Five complementary PubMed E-utils queries (see below) targeting the novel-payload space were combined and deduplicated, returning **951** candidate records. Records were classified into payload buckets with regex over title+abstract and manually filtered to require (a) an explicit LNP/lipidoid carrier, (b) a cancer indication, and (c) a non-vaccine encoded payload, removing pure-siRNA, pure-vaccine, and non-LNP papers. This yielded **157** papers (2008–2026, heavily weighted to 2024–2026).

1. `(LNP OR "lipid nanoparticle*" OR mRNA) AND ("in vivo CAR" OR "in situ CAR" OR "in vivo chimeric antigen receptor" OR "in situ programming") AND (cancer OR tumor OR leukemia OR lymphoma OR "T cell" OR macrophage)`
2. `("lipid nanoparticle*" OR LNP) AND ("transcription factor" OR reprogramming OR "tumor suppressor" OR p53 OR PTEN OR "dominant negative" OR FOXP3 OR "master regulator") AND (cancer OR tumor OR oncolog*)`
3. `("lipid nanoparticle*" OR LNP) AND (CRISPR OR Cas9 OR Cas13 OR "base editing" OR "prime editing" OR "gene editing") AND (cancer OR tumor OR leukemia OR lymphoma)`
4. `("lipid nanoparticle*" OR LNP) AND ("self-amplifying RNA" OR saRNA OR "self-replicating RNA" OR replicon OR "circular RNA" OR circRNA) AND (cancer OR tumor OR oncolog*)`
5. `("lipid nanoparticle*" OR LNP) AND mRNA AND ("IL-12" OR cytokine OR bispecific OR "monoclonal antibody" OR nanobody OR "tumor suppressor" OR "suicide gene" OR enzyme) AND (tumor OR cancer OR intratumoral)`

PMCIDs were resolved via the NCBI PMC ID converter; DOIs were back-filled from NCBI EFetch XML for all 157 records (100% DOI coverage). Full text was obtained as OA PDFs (publisher/PMC hosts reachable directly) and as Europe PMC full-text XML via the EBI REST endpoint. Direct NCBI PMC PDF endpoints sit behind a browser proof-of-work challenge that is unreachable from the build environment, so the remaining papers are catalogued as `metadata_only` (index row + abstract + resolvable DOI/PMID/PMCID links). Status counts: **14 `downloaded`**, **60 `fulltext_xml`**, **83 `metadata_only`**.

## Conventions

- `status` — `downloaded` (OA PDF in `pdfs/`), `fulltext_xml` (Europe PMC XML in `fulltext/`), or `metadata_only`.
- `category` — primary payload bucket (first matched); `topics` — all payload tags (a paper co-encoding IL-12 + a suicide gene carries both).
- Papers are referenced in the notes by first author, year, and PMID; see `index.tsv` for canonical DOI/PMID/PMCID links.
