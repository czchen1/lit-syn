# Antigen-encoding DNA vaccines for glioma

Studies here administer a plasmid (or DNA-launched replicon) encoding a defined tumor antigen/epitope to prime an anti-glioma T-cell response. Full text was available for Pearson 2024, Bausart 2022, Lopes 2021, and Adhikari 2022 (OA); the others are summarized from abstracts.

## Melanoma-associated antigens: TRP-2 and gp100

GL261 — the workhorse mouse glioblastoma line — aberrantly expresses melanin-biosynthesis enzymes, which is why melanoma differentiation antigens recur as glioma DNA-vaccine targets.

- **O et al. 2003 (PMID 12944987, *Cancer Gene Therapy*; abstract only).** Foundational study: a plasmid encoding **human (xenogeneic) TRP-2** primed CD8⁺ T cells that recognized TRP-2 on GL261. Vaccinated mice were **partially protected** against subcutaneous, intravenous, and intracerebral GL261 challenge. Established the xenogeneic-antigen tactic to break tolerance to a self differentiation antigen.
- **Kim et al. 2005 (PMID 16052205, *Gene Therapy*; abstract only).** Co-administered a **DC-specific (CD11c-promoter) Bcl-xl "survival gene"** with a **TRP2-hsp70** DNA construct. Prolonging dendritic-cell lifespan in vivo augmented TRP2-specific IFN-γ⁺ CD8 responses and gave therapeutic immunity to GL-26 glioma (and B16). Illustrates "genetic adjuvant" co-delivery to address the short lifespan of antigen-bearing DCs.
- **Pearson et al. 2024 (PMID 38954031, OA).** **SCIB1 ImmunoBody®** is a DNA vaccine encoding a human IgG1 antibody framework engineered to carry **TRP-2 and gp100** CD8/CD4 epitopes in its CDR loops (targeting the construct to Fc receptors on APCs). It generated a strong TRP-2-specific response (high IFN-γ ELISpot, pentamer⁺ T cells) and vaccine-induced T cells killed B16HHDII/DR1 targets. Because GBM expresses **PD-L1 and IDO1** (PD-L1 correlating with worse survival in the mesenchymal subtype), SCIB1 was combined with **anti-PD-1**; this **significantly prolonged time-to-death** of mice bearing intracranial TRP-2/gp100⁺ tumors and increased CD4⁺/CD8⁺ infiltration in the TME. The paper also notes IDO as an additional resistance node, motivating triple combinations.

## The pTOP epitope-carrier platform (UCLouvain)

A generalizable design in which an **engineered vesicular stomatitis virus glycoprotein (VSV-G)** acts as a carrier scaffold into which tumor T-cell epitopes are inserted, so the viral protein's intrinsic immunogenicity provides innate co-stimulation that naked epitope DNA lacks.

- **Lopes et al. 2021 (PMID 33795383, OA).** Introduces **pTOP** ("plasmid to deliver T-cell epitopes"). Tested in B16F10-OVA melanoma and **GL261 glioblastoma (subcutaneous and orthotopic)**, pTOP drove processing/presentation of both MHC-I and MHC-II epitopes and higher antigen-specific CTL killing than traditional epitope DNA vaccines, inducing both CD4 and CD8 responses.
- **Bausart et al. 2022 (PMID 35631612, OA).** Showed that the **insertion position** of a GBM CD8 epitope (TRP2₁₈₀–₁₈₈) within the VSV-G sequence governs MHC presentation — "permissive" insertion sites must be chosen (e.g. pTOP_TRP2(18)). Combining pTOP with **dual immune-checkpoint blockade** in an **orthotopic, unresectable GL261** model increased intracranial CD8 T-cell frequency; survival benefit was present but limited, underscoring the difficulty of the orthotopic setting.
- **Bausart et al. 2023 (PMID 37105343, abstract only).** Combined a pTOP-type vaccine with **local immunogenic-cell-death chemotherapy** — mitoxantrone in PEGylated PLGA nanoparticles (NP-MTX). Intratumoral NP-MTX raised IFN-γ⁺ CD8 frequency; the chemo+DNA-vaccine combination improved survival of GBM-bearing mice.

## Other defined antigens

- **Yamanaka et al. 2005 (PMID 15869409, abstract only).** A **Sindbis "layered" DNA** expression vector (pSin) given **intramuscularly**, encoding **human gp100 + mouse IL-18**, induced antigen-specific responses against B16-gp100 intracranial brain tumors. Demonstrates the **DNA-launched alphavirus replicon** approach (self-amplifying RNA produced from injected DNA) and xenogeneic-antigen + cytokine co-encoding.
- **Ueda et al. 2008 (PMID 18224680, abstract only).** A plasmid encoding full-length murine **SOX6** (a cancer-testis-type glioma antigen identified by serological screening) induced SOX6-specific CTLs and gave both **protective and therapeutic** immunity against glioma, without destroying normal SOX6-expressing tissue — an argument that SOX6 is a tolerable self/lineage target.
- **Chen et al. 2011 (PMID 22032907, abstract only).** A combination vaccine of an **EphA2(883–891) peptide + a LIGHT (TNFSF14) plasmid** immunized HLA-A2 transgenic (HHD) and trimera mice and induced robust CTL activity against human glioma **U251** cells without lysing autologous lymphocytes. LIGHT is used here as a genetically encoded co-stimulatory adjuvant.

## Multi-antigen and platform vaccines

- **Adhikari et al. 2022 (PMID 35651802, OA).** **ITI-1001** is a single **multi-antigen DNA vaccine** encoding three **HCMV** proteins (**pp65, gB, IE-1**) — antigens expressed by GBM cells — built on the **UNITE platform**, which fuses **LAMP1** (lysosome-associated membrane protein 1) to each antigen to route it through the endolysosomal pathway and boost **both MHC-I and MHC-II** presentation. In a syngeneic orthotopic GBM model, therapeutic ITI-1001 gave **~56% survival** of tumor-bearing mice; antitumor activity correlated with activated **IFN-γ⁺ CD4** T cells (the paper emphasizes CD4 help), alongside humoral responses.

## Cross-cutting design lessons

1. **Break tolerance to self-antigens** via xenogeneic orthologs (human TRP-2/gp100 in mice), CT antigens (SOX6), or viral antigens (HCMV).
2. **Add danger/co-stimulation** the naked plasmid lacks — viral glycoprotein carriers (VSV-G/pTOP), hsp70 fusion, LIGHT plasmid, IL-18 co-encoding, or DC-survival genes (Bcl-xl).
3. **Epitope engineering matters** — insertion position within a carrier (Bausart 2022) and epitope length/composition (see Derouazi 2010 in `02`) change immunogenicity and protection.
4. **Route to MHC-II/CD4 help** (LAMP1 in UNITE) is repeatedly tied to efficacy.
5. **Monotherapy is insufficient** in orthotopic GBM; checkpoint blockade and ICD chemo are added to convert immunogenicity into survival.
