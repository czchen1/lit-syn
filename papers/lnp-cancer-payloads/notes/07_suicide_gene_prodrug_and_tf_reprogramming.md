# 07 — Suicide-gene / prodrug-enzyme / toxin payloads and transcription-factor reprogramming

This note covers two payload families that share a "rewire the cell's fate" logic: (a) enzymes/toxins that make tumour cells kill themselves, and (b) transcription factors / master regulators that reprogram tumour or immune cells.

## Suicide gene, prodrug-enzyme, and toxin payloads (8 papers)

Gene-directed enzyme-prodrug therapy (GDEPT) has long been attractive for its low systemic toxicity but stuck on delivery; LNP-encoded enzymes revive it:
- Niu 2026 (PMID 41027739): circRNA-encoded **cytosine-deaminase–uracil-phosphoribosyltransferase (CD-UPRT)** delivered intratumourally; with the prodrug 5-fluorocytosine it gives sustained intratumoural conversion with minimal systemic toxicity, boosted by a co-delivered IL-15 circRNA (also notes/02, notes/06).
- Marschhofer 2026 (PMID 41506374): the KRAS-G12S CRISPR-LNP (notes/05) reads out through downstream apoptosis/pyroptosis as the cytotoxic mechanism.
- Several tumour-suppressor and CRISPR papers carry the suicide/pyroptosis tag because the therapeutic endpoint is induced apoptosis/pyroptosis (e.g. Hu 2026 PTEN/PARP1, PMID 41696631; Zeng 2026 p21 intravesical, PMID 42144924).

Toxin payloads proper are rare in the curated set — the field favours conditional enzyme/prodrug systems and editing-induced death over constitutive toxins, presumably for the same localisation/safety reasons that dominate the cytokine work.

## Transcription-factor and reprogramming payloads (30 papers)

Two sub-modes:

### Enforcing a beneficial TF in immune/effector cells
- Ge 2026 (PMID 42245679): enforced **BATF** expression via clinically approved LNPs enhances adoptive T-cell therapy — improving expansion, persistence, and resistance to exhaustion.
- Gupta 2026 (*Nat Biotechnol*, PMID 42129506): "immune-remodelling mRNAs" encoding **IRF8** or **NF-κB-inducing kinase (NIK)** delivered by LNP activate intratumoural antigen-presenting cells, expand cDC1s, and prime CD8 T cells across multiple cancer models.

### Reprogramming tumour cells or the microenvironment
- **Macrophage M2→M1 repolarisation** is the most common reprogramming endpoint, achieved by encoding CAR/switch receptors (notes/01), IFN-γ (notes/02), or by silencing the master M2 TF: Ko 2026 (PMID 42173448) co-encapsulates a TLR9 agonist (CpG) + **STAT3 siRNA** in a biomimetic (chylomicron/apoptotic-body-mimetic) macrophage-targeted LNP.
- **β-catenin axis reset**: Lehrich 2025 (*Nat Commun*, PMID 40442146) — LNP-siRNA against CTNNB1 in Wnt-active HCC drives zonal/cellular reprogramming, re-engages IRF2/POU2F1 and type-I/II IFN, and synergises with ICI; an LA-like signature is prognostic in the IMbrave150 trial.
- **Competitive-peptide reprogramming**: Wang 2026 (PMID 42212318) delivers a tumour-targeted LNP carrying a lactylation-deficient CREB1-K122R competitive peptide to reverse a lactylation-driven transcriptional program of cisplatin resistance in ovarian cancer.

## Why these payloads suit LNPs

TF/reprogramming and suicide-enzyme payloads are intracellular-acting and dose-sensitive, so they benefit from the same LNP advantages exploited throughout the collection: transient, tunable, re-dosable expression confined (by route or by targeting ligand) to the cell population that needs rewiring — APCs, macrophages, or the tumour cell itself. Reviews framing in-situ cell reprogramming: Wang 2023 (PMID 39574564) and Zhang 2023 (*Nat Nanotechnol*, PMID 37500773, the "CATCH" CD40L/CD40 mRNA-LNP + DC platform).

See notes/01 (CAR/switch-receptor reprogramming), notes/02 (cytokine-driven repolarisation), notes/04 (suppressor restoration), and notes/06 (circRNA-encoded CD-UPRT).
