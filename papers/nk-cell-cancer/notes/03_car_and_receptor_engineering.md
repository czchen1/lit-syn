# CAR-NK and receptor engineering

## NK cells need NK signalling modules

The single most transferable design lesson is that CAR-T architectures do not port cleanly:

- **Li et al. (2018, PMID 30082067)** screened CAR constructs in iPSC-NK cells and found a CAR combining the
  **NKG2D transmembrane domain, 2B4 costimulatory domain and CD3ζ** gave the strongest antigen-specific NK
  signalling and outperformed the standard CD28-CD3ζ CAR-T design in NK cells.
- DAP10/DAP12-based two-chain receptors exploit native NK adaptors; a KIRS2/DAP12 CAR improved safety and
  efficacy in r/r B-ALL (PMID 34703879), showing the concept is clinically viable.
- Counterintuitively, **CD28 — absent from mature NK cells — is a potent NK costimulatory module**: a CD70-CAR
  with a CD28 domain augmented signalling through an LCK/CD3ζ/ZAP70 axis (PMID 38900051). The lesson is that
  costimulatory domains must be screened empirically in NK cells, not inherited from T-cell dogma.
- Integration site is a design variable: knocking ζ-deficient CARs into the endogenous *CD3ζ* locus conveys
  potent cytotoxicity in both T and NK cells (PMID 38493479).

Reviews that map the design space usefully: Gong et al. (PMID 33933160) on CAR-NK design and engineering,
Xie et al. (PMID 32853984) on the CAR-NK rationale, and the receptor-engineering review at PMID 38443448.

## Targets and disease context

- Haematological: CD19 (PMID 32023374, PMID 38238616, PMID 40251398), CD33 (PMID 39349459), CD38
  (PMID 33375774, PMID 35135865), CS1/SLAMF7 in myeloma (PMID 24067492), CD123, CD70.
- Solid tumours: HER2/ErbB2 (PMID 25373520 → glioblastoma trial PMID 37148198), EGFR and EGFRvIII in GBM
  (PMID 26155832), mesothelin (PMID 40025022; CAR-CIML NK in ovarian cancer, PMID 38996027), NKG2D-ligand
  targeting (PMID 30396908 in T cells, informing NK use).
- Solid-tumour CAR-NK reviews: PMID 38245520, PMID 39134804 — both converge on trafficking, persistence and
  TME suppression rather than antigen choice as the limiting factors.

## Failure modes discovered by engineering

- **Trogocytosis-driven fratricide and antigen loss.** CAR activation transfers cognate antigen from tumour to
  NK cell, lowering tumour antigen density and causing CAR-NK cells to kill each other; a **KIR-based
  inhibitory CAR** rescues both problems (Li et al. 2022, PMID 36175679). This is arguably the most important
  NK-specific CAR failure mode described to date.
- **Self-antigen fratricide.** CD38-CAR NK cells kill each other because NK cells upregulate CD38 during
  expansion; CD38 knockout plus an affinity-optimised CAR resolves it (PMID 33375774), and CD38 deletion also
  eliminates daratumumab-induced fratricide (PMID 32603414).
- **Loss of metabolic fitness, not antigen escape, drives relapse.** Single-cell profiling of CAR-NK cells
  after adoptive transfer showed relapse coincides with metabolic collapse, reversible by cytokine engineering
  (PMID 37494448).

## Gene delivery into NK cells

NK cells are refractory to conventional transduction; delivery method is a manufacturing-critical choice.

| Method | Evidence | Notes |
|---|---|---|
| Baboon envelope pseudotyped lentivirus (BaEV) | CD19-BBz CAR-NK phase 1 (PMID 40251398) | High efficiency in primary/CB NK without feeders |
| Alpharetroviral / lentiviral | PMID 32117200 | Direct comparison for CD19 CAR-NK in ALL |
| Retroviral | TRACK NK sIL-15 (PMID 38572955) | Used in clinical CB-NK products |
| Electroporation of plasmid/mRNA | PMID 31114587 | Non-viral, transient; CAR + CCR7 co-delivery |
| CRISPR RNP (Cas9 protein) | PMID 32528479, PMID 31704085 | Avoids DNA toxicity; up to ~90% editing of primary NK |
| AAV-SB (Sleeping Beauty) | in vivo CRISPR screens in primary NK (PMID 38918616) | Screening platform, also a delivery template |
| Site-specific knock-in | *CD38* locus knock-in of high-affinity CD16 (PMID 35135865); *CD3ζ* locus (PMID 38493479) | Combines knockout and knock-in in one edit |

**Feeders interact with transduction efficiency**: feeder-based activation raises both proliferation and
transduction (PMID 35222382, PMID 28810809, PMID 40325497), so delivery method and expansion platform must be
co-optimised rather than chosen independently.

## Synthetic-biology layer (mostly preclinical)

- **Inhibitory/logic-gated CARs**: KIR-based iCAR against trogocytosis (PMID 36175679); synNotch-programmed
  iPSC-NK cells that convert TIGIT/CD73 engagement into activation in glioblastoma (PMID 38429294).
- **Inducible switches**: rimiducid-controlled MyD88/CD40 (iMC) plus IL-15 enhances CAR-NK growth and
  cytotoxicity (PMID 32384544).
- **Cytokine-secreting "armoured" designs**: IL-15 (PMID 28725044), neoleukin-2/15 mutein driving c-Myc/NRF1
  (PMID 40025022), decoy-resistant IL-18 delivered in trans by engineered bacteria (PMID 39367093),
  oncolytic-virus-delivered IL-15/IL-15Rα combined with EGFR-CAR NK cells.
- **Engager-secreting effectors**: CAR-T cells that secrete BiKEs to recruit endogenous NK cells
  (PMID 40659834) — an explicit bet that combining effector classes beats optimising one.

## Design checklist

1. Use NK-native signalling modules (NKG2D-TM/2B4/DAP10/DAP12) **and** empirically test non-native
   costimulation (CD28, 4-1BB).
2. Anticipate trogocytosis and self-antigen fratricide; plan an inhibitory CAR or a knockout of the target on
   the effector.
3. Co-express or supply IL-15 — an unarmoured CAR-NK product will not persist.
4. Choose the delivery method with the expansion platform, not after it.
5. Assume the TME will suppress the product: add TGF-β resistance, checkpoint deletion or metabolic armouring
   in the same construct generation.
