# Safety engineering for GD2 CAR-T

GD2's expression on healthy peripheral nerves, central nervous system astrocytes, and skin melanocytes makes on-target / off-tumor toxicity a recurring concern. The collection documents the following safety-engineering strategies.

## 1. Inducible caspase-9 (iCasp9 / iC9)

The dominant clinical safety switch. iCasp9 is a FKBP-FRB(F36V) dimer with truncated active-site domain of caspase-9; binding of the small-molecule dimerizer **rimiducid (AP1903)** forces dimerization and triggers apoptosis. Documented use:

- **Heczey 2017 (PMID 28602436)** — first inclusion of iC9 in a GD2 CAR clinical product (GD2-CAR3 + iC9 in SFG). Cloned 5' of the GD2-CAR3 cassette.
- **Quintarelli 2018 (PMID 29872565)** — preclinical demonstration that iC9 added to GD2-CD28-4-1BB-CD3ζ does not impair CAR expression or anti-tumor activity, and that rimiducid eliminates iC9-CAR T cells in vitro.
- **Del Bufalo 2023 (NEJM)** clinical **GD2-CART01** product — third-generation GD2-CD28-4-1BB-CD3ζ + iC9. iC9 was not triggered during the trial but provides a safety net against CRS/neurotoxicity.
- **Majzner 2022 (PMID 35130560)** and **Monje 2025 (PMID 39537919)** — Stanford DIPG/DMG product carries an iCasp9 from Bellicum Pharmaceuticals upstream of the GD2-4-1BB-CD3ζ CAR.
- **Caforio 2021 (PMID 33737337)** — same construct in medulloblastoma preclinical models.
- **Quintarelli 2025 (PMID 39815015)** — allogeneic ALLO_GD2-CART01: iC9 expressly cited as the GvHD-mitigation mechanism enabling donor-derived use.

Practical observations across papers: rimiducid in vitro eliminates ≥90% of iC9-expressing CAR-T cells within 4–6 h; in-vivo activation in NSG models eliminates infused human cells within 24 h. No GD2 CAR-T trial has reported on-protocol iCasp9 activation, suggesting either (a) toxicity has been manageable without the switch, or (b) the iC9 cassette has not been tested under fully ablative conditions in patients.

## 2. RQR8 (CD20-epitope-containing safety tag)

- Used in a minority of GD2 CAR papers in the collection as an alternative to iCasp9. RQR8 is a chimeric peptide containing CD34 and CD20 epitopes; rituximab triggers complement-/ADCC-mediated lysis of cells carrying the tag.
- Provides additional benefit of selection: RQR8+ cells can be enriched on CD34 columns.

## 3. EGFRt (truncated EGFR)

- Truncated EGFR lacks the intracellular signaling domain but retains the extracellular cetuximab epitope; cetuximab binds and triggers cell killing by ADCC. Appears in a handful of preclinical GD2 CAR papers, especially those originating from the Seattle Children's lineage.

## 4. HSV thymidine kinase (HSV-TK)

- Historical safety switch (Bonini, Bordignon 1997 lineage); used in some early GD2 CAR-NKT designs. Triggered by ganciclovir, which is phosphorylated by HSV-TK and incorporated into proliferating cells' DNA. Now largely replaced by iCasp9 due to faster kinetics of caspase-9-mediated apoptosis (hours vs days) and lack of dependence on cell proliferation.

## 5. Affinity tuning to spare healthy tissue

### 5.1 Standard-affinity 14g2a as the safer choice

- Mount 2018 (PMID 29662203): standard-affinity 14g2a-CD8TM-4-1BB-CD3ζ CAR T cells eradicate H3K27M+ DIPG without overt CNS toxicity in murine models.
- Majzner 2022 (PMID 35130560): same standard-affinity 14g2a CAR drives strong efficacy in patients with H3K27M-DMG with manageable, ICP-managed neurotoxicity.

### 5.2 Affinity-matured 14g2a-E101K is unsafe with CD28

- Richman 2018 (PMID 29180536): introducing the **VH-CDR3 E101K** mutation increases affinity ~10× but, in the CD28-CD3ζ format, causes lethal CNS toxicity in mice. The same scFv in a 4-1BB-CD3ζ form retains potency without lethality (Richman 2018, Fig. 4–5).
- Counter-letters (Esengül Yildirim et al., PMID 29610423 / 29610424) re-examine and confirm the encephalitis observation, sparking the broader policy of restricting affinity-matured 14g2a variants to non-CD28 costimulation backbones.

### 5.3 GD2 vs OAcGD2

- 8B6 / OAcGD2-targeting CARs (preclinical OAcGD2 papers in collection) selectively recognize O-acetyl-GD2, which is more tumor-restricted than GD2 itself, with reduced expression on peripheral nerves; aim is to preserve efficacy with less neurotoxicity.

## 6. Costimulation-only or "1G safety" CARs

- Fisher 2017 (PMID 28341563) explores a costimulation-only CAR (no ITAMs) paired with a separate signal-1 receptor (e.g., TCR or a low-affinity activating CAR) to avoid on-target tonic signaling-driven activation in tissues with low antigen. Not yet in clinical use for GD2.

## 7. Antibody-coupled / SUPRA / DARPin switchable CARs

- A small set of 2024–2026 collection papers use **SUPRA** (split universal programmable receptor) and DARPin-switchable architectures, in which a universal "zipCAR" T cell is paired with a soluble GD2-binding adapter ("zipFv"). The adapter has a short serum half-life, providing an OFF switch via dose interruption.

## 8. mRNA-electroporated CARs (transient by design)

- Singh 2014 (PMID 25104548) and several subsequent papers — IVT mRNA electroporation gives 7–10 days of CAR expression then decay. Used as a built-in safety mechanism: any toxicity is self-limited.

## 9. Logic gates (AND / NOT)

- Moghimi 2021 (PMID and venue cited in `index.tsv`) — **synNotch B7-H3 → GD2 AND-gate**: anti-B7-H3 synNotch receptor induces transcription of a GD2 CAR only in B7-H3+ tumor cells, sparing B7-H3− healthy GD2+ tissue.
- A handful of 2024–2026 papers use KIR/SIGLEC-based **NOT gates** to repress activation in tissues expressing healthy-specific antigens.

## 10. Antigen-density-gated / tuned CARs

- Several 2024–2026 papers report engineering CAR signaling thresholds (via hinge length, ITAM number, costimulation strength) so that the CAR triggers above a tumor-relevant antigen density but is silent below the lower density on healthy GD2+ tissue. Cited rationale invokes Lim lab antigen-density-gated CAR work.

## 11. CRS / ICANS / TIAN management as built-in product features

- Majzner 2022 (PMID 35130560, lines 1167–1200): the trial protocol explicitly anticipates **TIAN** (tumor inflammation-associated neurotoxicity), instituting routine and symptom-prompted ICP monitoring, mandatory Ommaya reservoir placement in DIPG patients, prophylactic anti-cytokine agents (tocilizumab + anakinra + corticosteroids), and the iCasp9 switch as a last-resort rescue. These are documented as design features of the **product+protocol**, not just clinical management.
- Tian 2025 (PMID 40044579 / 39800376): hyperleukocytosis at the highest CAR-NKT dose triggered the implementation of additional safety measures, including an inducible safety switch as part of the IL-15-expressing construct.

## 12. Cytokine-armoring and persistence trade-offs

- IL-15 co-expression (Heczey 2020/2023 CAR-NKT.15; Tian 2025; Bodden 2023 RD-IL15) extends persistence but raises the risk of unrestrained proliferation. Safety switches (iC9, RQR8) are particularly emphasized in armored designs.
- Glienke 2022 (PMID 35401506) IL-18 TRUCK design places IL-18 under an NFAT-responsive promoter so the cytokine is only secreted upon CAR engagement; not constitutive.
