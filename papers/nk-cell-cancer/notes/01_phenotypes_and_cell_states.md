# NK phenotypes and cell states: what to infuse

## The classical dichotomy is a starting point, not a specification

CD56bright (cytokine-producing, CD16-low) versus CD56dim (cytotoxic, CD16-high, KIR/CD57-acquiring) remains
the working vocabulary, but the field has moved past it:

- **Freud, Mundy-Bosse & Caligiuri (2017, PMID 29166586)** argued that the human NK spectrum is far broader
  than the dichotomy, shaped by tissue localisation and differentiation stage.
- **Rebuffet et al. (2024, PMID 38956378)** used scRNA-seq + CITE-seq to resolve human NK heterogeneity into
  distinct transcriptional states with surface-protein correlates — including states not separable by the
  canonical marker panel.
- **Netskar et al. (2024, PMID 38956379)** built a single-cell transcriptional reference map of blood- and
  tissue-derived NK cells and used it to map tumour-infiltrating NK cells across cancers; **Tang et al.
  (2023, PMID 37607536)** provide the complementary pan-cancer single-cell panorama.
- **Horowitz et al. (2013, PMID 24154599)** established by mass cytometry that NK repertoire diversity is
  jointly genetically and environmentally determined — the reason donor-to-donor product variability is
  structural, not technical.
- **Dogra et al. (2020, PMID 32059780)** showed tissue imprinting of human NK development, function and
  residence, which is why blood-derived products behave differently from the tissue NK cells that a solid
  tumour actually contains.

**Practical consequence:** "CD56+CD3−, >90% pure" is not a product specification. Recent trials increasingly
report high-dimensional immunophenotypic and transcriptional characterisation of the infused product
(e.g. the CIML NK head-and-neck trial, PMID 39948608), and that is becoming the expected standard.

## Cytokine-induced memory-like (CIML) NK cells

The most reproducible phenotype-engineering result in the field:

- **Romee et al. (2012, PMID 22983442)** — a brief (12–16 h) preactivation with IL-12 + IL-15 + IL-18
  produces human NK cells with enhanced IFN-γ recall responses to cytokine or activating-receptor
  restimulation for weeks after the stimulus is withdrawn.
- **Romee et al. (2016, PMID 27655849)** — CIML NK cells show enhanced antileukaemic responses and, in a
  first-in-human trial in relapsed/refractory AML, expanded in vivo and produced remissions.
- **Berrien-Elliott et al. (2022, PMID 35349491)** — donor CIML NK cells infused for post-transplant relapse
  expand, persist and show efficacy, with detailed pharmacodynamics of expansion and persistence.
- **2024 mechanism (PMID 38941480)** — memory-like subsets form via **epigenetic rewiring** and
  transcriptional regulation, i.e. the phenotype is a stable differentiation state rather than a transient
  activation.
- **Combination-ready:** CIML differentiation stacks with engagers (AFM13 pre-complexing, PMID 33986022),
  with CARs (CAR-CIML NK against mesothelin in ovarian cancer, PMID 38996027), with IL-15 super-agonist plus
  CTLA-4 blockade in head-and-neck cancer (PMID 39948608), and with PM21-particle expansion (PMID 38711506),
  which reports memory-like characteristics plus enhanced survival from a single manufacturing process.

## Adaptive / NKG2C+ NK cells

- HCMV-driven **CD56dim CD57+ NKG2C+** adaptive NK expansions are associated with reduced leukaemia relapse
  after reduced-intensity transplant (Cichocki 2016, PMID 26416461); the drivers of that expansion include
  IL-12-producing monocytes and HLA-E (PMID 25384219).
- Adaptive-like features can be **engineered rather than waited for**: **Cichocki et al. (2021,
  PMID 34525347)** harnessed adaptive NK features (including FcεRIγ-low/CD16-driven signalling) to build
  iPSC-derived NK cells with enhanced antibody-dependent function.
- Practical caveat: adaptive expansions depend on donor CMV serostatus, making them a **donor-selection**
  lever for primary products and a **design target** for iPSC products.

## Priming state changes what a subset can do

**Wagner et al. (2017, PMID 28972539)** showed CD56bright NK cells — usually written off as non-cytotoxic —
mount potent antitumour responses after IL-15 priming. Combined with the observation that distinct
developmental pathways generate functionally distinct NK populations (PMID 38872000), the operative variable
is *state at the time of infusion*, which manufacturing controls directly.

## Dysfunction, exhaustion and plasticity

The product's phenotype does not survive contact with the tumour untouched:

- **NK→ILC1 conversion.** Gao et al. (2017, PMID 28759001) showed TGF-β-dependent conversion of effector NK
  cells into intermediate ILC1-like cells as a tumour immunoevasion mechanism; Cxcr3-driven infiltration also
  produces ILC1-like plasticity in liver metastasis (PMID 40168086).
- **Hypoxia.** Ni et al. (2020, PMID 32445619) profiled tumour-infiltrating NK cells by scRNA-seq and showed
  that deleting *Hif1a* unleashes NK activity; hypoxia impairs cytotoxicity via SHP-1/STAT3/ERK
  (PMID 33123602) and via autophagic granzyme B degradation in the target cell (PMID 24101526).
- **Intratumoral phenotype collapse.** Platonova et al. (2011, PMID 21708957) documented coordinated
  alterations of intratumoral NK phenotype and function in NSCLC; more recently, NK cells become functionally
  impaired *within hours* of tumour entry (PMID 38267402).
- **Checkpoint and epigenetic dysfunction.** High NKG2A marks exhaustion and poor prognosis in liver cancer
  (PMID 28197391); a PD-1-high NK subset exists in patients (PMID 27372564); BATF drives epigenetic
  dysfunction of NK cells in AML (PMID 39259809); NKG2A overexpression drives exhaustion in relapsed AML
  (PMID 40320412).
- **Reversibility.** Retinoic-acid-receptor activation reprogrammes the senescence response and improves NK
  antitumour activity (PMID 38428412); fasting reshapes tissue niches to improve NK-mediated immunity
  (PMID 38878769) — evidence that the dysfunctional state is pharmacologically addressable.

## Education, KIR and the donor-selection layer

Education/licensing still predicts clinical outcome: KIR B-haplotype donor selection improves survival after
unrelated transplant for AML (PMID 20581313), the **HLA-B −21 M/T dimorphism** shapes NK education and
immunotherapy outcome in AML (PMID 30647027), and DNAM-1/KIR receptor ratios have been proposed as
predictive biomarkers in solid tumours (PMID 30242020). For allogeneic products this is a cheap efficacy
lever available before any engineering.

## Summary — the phenotype checklist for a modern product

| Lever | Best-supported implementation |
|---|---|
| Differentiation state | CIML (IL-12/15/18, 12–16 h) or IL-15-primed |
| Adaptive features | CMV+ donor selection, or engineered FcεRIγ-low/adaptive-like iPSC-NK |
| Education | KIR B-haplotype / HLA-B −21 donor selection; KIR-ligand mismatch |
| Resistance to reprogramming | TGF-β/SMAD-resistant, HIF-1α-independent, metabolically armoured |
| Characterisation | scRNA-seq/CITE-seq or high-parameter flow of the *final* product, not the starting apheresis |
