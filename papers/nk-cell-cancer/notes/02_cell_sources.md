# Cell sources: blood, cord blood, iPSC and cell lines

Source choice fixes the ceiling on expansion, editability, homogeneity and scale, and it interacts with every
downstream manufacturing decision.

## Peripheral blood (PB-NK)

- Haploidentical PB-NK infusions established the modern field: **Miller et al. (2005, PMID 15632206)**
  demonstrated safe adoptive transfer with in vivo expansion after lymphodepletion, following on
  **Ruggeri et al. (2002, PMID 11896281)**, which showed donor-versus-recipient NK alloreactivity eliminates
  AML relapse and graft rejection without GvHD.
- Strengths: mature, educated, fully cytotoxic cells; KIR/HLA donor selection possible.
- Limits: low starting frequency (~10% of lymphocytes), donor-to-donor variability, one-donor-one-patient
  economics unless expansion is very high, and T-cell depletion required for allogeneic use.
- Patient-derived (autologous) NK cells are frequently dysfunctional — reduced CD16+ cytotoxic NK cells in
  myeloma marrow predict worse daratumumab responses (PMID 40019438), and NK cells from cancer patients show
  diminished cytotoxicity versus healthy donors (PMID 20849361), which is the core argument for allogeneic
  products.

## Cord blood (CB-NK)

- The dominant substrate for engineered clinical products: cord blood supports lentiviral transduction plus
  IL-15 armouring and log-scale expansion, and units are banked, HLA-typed and immediately available
  (Liu 2018, PMID 28725044 → the CD19 CAR-NK trials, PMID 32023374 and PMID 38238616).
- **Shah et al. (2013, PMID 24204673)** achieved ~1,800–2,400-fold expansion from fresh or cryopreserved CB
  using aAPC feeders in gas-permeable vessels — demonstrating that a single unit can yield multiple doses.
- CB-NK are more immature (higher CD56bright fraction, lower KIR), which is partly compensated by cytokine
  preactivation and armouring, and CB-derived TRACK NK cells (PD-L1+, sIL-15-secreting) have reached the
  clinic in NSCLC (PMID 38572955; PMID 39903538).
- Selective-thaw devices allow a small aliquot of a banked unit to be used for NK expansion while preserving
  the unit for transplant (PMID 26432560).

## iPSC-derived NK cells (iNK)

The route to a genuinely homogeneous, multi-edited, off-the-shelf product:

- **Knorr et al. (2013, PMID 23515118)** established clinical-scale derivation of NK cells from human
  pluripotent stem cells; **Zhu & Kaufman (2019, PMID 31396935)** improved the process to clinical scale
  without stromal feeders.
- **Li et al. (2018, PMID 30082067)** engineered iPSC-NK cells with an NK-optimised CAR (NKG2D TM + 2B4 +
  CD3ζ) that outperformed a CAR-T-derived architecture in NK cells.
- Multiplex editing is where iNK cells differentiate themselves: CISH knockout improves persistence and
  IL-15-independent function (Zhu 2020, PMID 32531207); TGF-β pathway disruption is *required* for effective
  killing of hepatocellular carcinoma (PMID 38986609); high-affinity non-cleavable CD16a improves ADCC
  (PMID 31856277); adaptive-NK features can be built in (PMID 34525347); synNotch programming converts TIGIT
  and CD73 into activating inputs for glioblastoma (PMID 38429294).
- Differentiation protocol matters: two iPSC-NK differentiation strategies produce distinct signatures and
  cytotoxicity (PMID 39445004) — a manufacturing choice with a phenotypic readout.
- Clinical proof of principle: **FT596** (CD19 CAR + hnCD16 + IL-15/IL-15Rα fusion) in B-cell lymphoma,
  phase 1 (PMID 39798981).

## NK-92 and other cell lines

- NK-92 (Gong 1994, PMID 8152260) offers unlimited, consistent supply; infusions are safe in phase I
  (Arai 2008, PMID 18836917; Tonn 2013, PMID 24094496) but the cells are irradiated before infusion, so they
  cannot persist — potency must come from dose and frequency.
- Engineered NK-92 remains clinically relevant: ErbB2/HER2-CAR NK-92 (NK-92/5.28.z) went from GMP-compliant
  clonal line (PMID 25373520) to intracranial administration in recurrent glioblastoma (PMID 37148198).
- Line-specific improvements: CRISPR RNP editing enhances NK-92 cytotoxicity (PMID 32528479); expansion and
  cryopreservation workflows for clinical NK-92 manufacture are now published (PMID 38394177).
- Trade-off summary: unlimited scale and cheap consistency, at the cost of persistence, an aneuploid
  EBV+ lymphoma-derived genome and mandatory irradiation.

## Making allogeneic sources truly universal

- **HLA class I knockout** converts allogeneic primary NK cells into off-the-shelf effectors by removing
  host-T-cell recognition (PMID 33584651); the mirror-image problem — host NK rejection of HLA-null cells —
  is why HLA-E/single-chain-HLA retention strategies appear in iPSC products.
- Placental/decidual NK cells (PMID 23641243) and CD34+ progenitor-derived NK cells widen the donor pool;
  microtransplantation delivers G-CSF-mobilised donor mononuclear cells containing large NK numbers
  (PMID 42035877).

## Choosing a source

| | PB-NK | CB-NK | iPSC-NK | NK-92 |
|---|---|---|---|---|
| Doses per donor/lot | low–medium | medium–high | effectively unlimited | unlimited |
| Editability | moderate | moderate–good | best (clonal, multiplex) | good |
| Persistence in vivo | days–weeks (with IL-15/lymphodepletion) | weeks when IL-15-armoured | weeks when armoured | none (irradiated) |
| Maturity/education | mature, educated | immature, needs priming | protocol-dependent | line-fixed |
| Main risk | variability, T-cell contamination | immaturity | differentiation drift, tumourigenicity testing | no persistence, genomic background |
