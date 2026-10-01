# Scope boundary: excluded and adjacent records

The 4 PubMed queries returned **80 unique records**; **21** are in scope (see `index.tsv`) and **59** were excluded during abstract triage. This note documents the exclusion rationale so the scope is reproducible. The recurring reason is that the query terms (`plasmid`, `DNA`, `vaccine`, `immunization`) match a large body of work that uses a plasmid only as a **laboratory tool** or pursues **non-vaccine** strategies.

## Exclusion categories

### A. Plasmid used purely as a research tool (no vaccination intent)
Transfection/overexpression, cloning, reporters, bioinformatics, modeling — the plasmid is incidental.
- 41982811 (2026) single-cell GSH metabolism, GSTA4 (siRNA/plasmid models)
- 41389249 (2026) TLR7 overexpression via pcDNA-TLR7
- 40864860 (2025) TBEV NS1 plasmid transfection in neuroblastoma/GBM cells
- 40647519 (2025) review of preclinical pediatric-glioma models
- 39777911 (2025) Sleeping Beauty plasmid tumor-modeling protocol
- 37427920 (2023) electroporation plasmid tumor-modeling (patient mutation signatures)
- 37627528 (2023) bradykinin B1R overexpression
- 32306002 (2020) GIMAP2 subcellular localization (expression vector)
- 32000905 (2020) immune-cell isolation from SB transposon glioma models
- 31819973 (2020) PD-L1 expression survey (transient transfection control)
- 21815198 (2011) STAT1/STAT3 reporter/decoy study
- 18703592 (2008) HIF-1 luciferase/NIS reporter imaging
- 18677476 (2009) IL-13Rα2 cDNA cloning/prokaryotic expression
- 15151753 (2003) MAGE-E1 cloning/E. coli expression
- 17409515 (2007) cationic liposome–pDNA cytotoxicity (delivery biophysics)
- 7531687 (1994) inducible NOS cDNA cloning from a GBM line
- 1653364 (1991) MDR-gene-transfected GBM line, interferon phenotype
- 26592196 (2016) chlorpromazine / tissue-factor apoptosis (CNS, not glioma vaccine)
- 25054228 (2014) IL-1β/inflammasome expression in gliomas
- 8548582 (1995) T7 cytoplasmic gene-expression system (delivery tech)

### B. Non-immunizing gene therapy / gene delivery (cytokine, suicide, antisense, shRNA, p53)
Therapeutic transgene delivery to tumor/cells without an antigen-specific vaccination aim.
- 39931861 (2025) attenuated *Salmonella* siRNA-PD-L1 + endostatin + radiation (knockdown/anti-angiogenic, not antigen vaccine)
- 40213677 (2025) engineered-bacteria thermal in-situ cytolysin production
- 34481020 (2021) PAMAM/shRNA (CD47) hydrogel
- 33188941 (2021) photochemical internalization gene transfection of macrophages (GDEPT)
- 30288347 (2018) SGT-53 (p53 plasmid nanoparticle) + anti-PD1
- 18176109 (2008) IL-12 transgene via PPC polymer + BCNU
- 17684491 (2008) shRNA against TGF-β type II receptor
- 17639883 (2007) nonviral gene transfer efficacy in canine brain (delivery study)
- 15059028 (2004) TNF-α/Bax gene therapy + proton radiation
- 14695218 (2003) MICA/NKG2D immunogene therapy (tumor-cell transfection to sensitize to NK/T)
- 11810046 (2002) intratumoral pGL1-TNF-α gene therapy
- 10490773 (1999) IFN-β gene transfer (cationic liposome)
- 9990062 (1999) IM plasmid IFN-α — DNA-based cytokine gene therapy (no antigen); glioma 261 among models

### C. Gene-modified whole-tumor-cell vaccines (ex-vivo modified cells, not in-vivo DNA)
Classic glioma immunotherapy but mechanistically distinct from administered nucleic-acid vaccines.
- 8610141 (1996) TGF-β antisense gene-modified 9L cell vaccine
- 9864741 (1998) TGF-β antisense gene-modified C6 (also abstract-only)
- 10871746 (2000) B7.1-transfected F98 cells
- 11302658 (2001) hygromycin-phosphotransferase-modified C6 tumorigenicity

### D. Dendritic-cell / ex-vivo cell vaccines (incl. mRNA-transfected DCs)
Cellular vaccines; the nucleic acid is transfected into DCs ex vivo, not administered as the vaccine.
- 19895199 (2010) DCs transfected with Il13ra2 **mRNA**
- 17432716 (2007) DCs transfected with RHAMM **mRNA**
- 19699331 (2009) glioma-lysate-pulsed DCs + IP-10 plasmid (DC vaccine; plasmid is a co-adjuvant)
- 18304655 (2008) NDV-infected tumor-cell vaccine + antisense-oligo nanoparticles (plasmid only a reporter)

### E. Other vaccine modalities (recombinant protein, viral-vectored, lysate nanovaccine)
Not DNA/nucleic-acid vaccines, though some target the same glioma antigens.
- 36999709 (2024) recombinant **MVA poxvirus** expressing IL-13Rα2
- 40270217 (2025) GBM cell-**lysate** CpG nanovaccine (GlioVac)
- 23640602 (2013) recombinant **protein** IP10-EGFRvIIIscFv + CTL
- 15853729 (2005) review of IL-13Rα2 cytotoxin/gene therapy

### F. Not glioma, or only incidental glioma mention
- 36543794 (2022) IONAID intradermal tattoo device — DNA vaccine delivery tested with **Ebola GP**, not glioma
- 19663697 (2009) DNA-immunization-derived mAbs against HAAH (hepatocellular)
- 27096896 (2016) MYCN-targeting vaccines (neuroblastoma/medulloblastoma)
- 15139525 (2004) **rabies** DNA-vaccine transfection in cell culture
- 17182597 (2007) BORIS cancer-testis DNA/protein vaccine (histologically unrelated tumors; glioma not a primary model)

### G. Broad reviews / immunogene therapy not centered on DNA vaccination
- 17087271 (2006) broad neurosurgical "molecular targeting" review (mentions DNA vaccine among many modalities)

## Borderline calls worth noting

- **9990062 (Horton 1999)** and **18176109 / 11810046 / 15059028 (cytokine/TNF gene therapy)**: DNA/plasmid-based and immunostimulatory, but framed as **gene therapy** (deliver a therapeutic cytokine transgene) rather than antigen-specific **vaccination** — excluded under B. A reader interested in "plasmid-encoded cytokine immunotherapy for glioma" should treat these as adjacent.
- **14618278 (2004) cationic lipid–noncoding-plasmid complexes**: stimulates a Th1 response and inhibits orthotopic GBM, i.e. **DNA-based innate immunostimulation**, but uses **non-coding** plasmid (no antigen) — excluded as not a defined-antigen vaccine.
- **32646187 (2017)**: primarily liposomal chemo, but contains an **in-vivo DC-targeted genetic immunization (TRP-2)** component — excluded as the paper's thrust is targeted chemotherapy.
- **38031775 (Trojan 2024, IGF-I anti-gene vaccine)**: **included** as a review despite being a gene-modified-cell vaccine, because it is explicitly framed as a GBM **vaccine** review and is useful context; flagged here for transparency.
- **21327126 (Derouazi 2010)** and the **Feng *Salmonella* series**: included even though delivery is via live bacteria, because the **intent and readout are antigen-specific vaccination** against glioma.

## Reproducibility note

DOIs/PMCIDs in `index.tsv` were extracted from each record's own `PubmedData/ArticleIdList` (an initial automated pass had mistakenly captured DOIs from reference lists). Counts: 80 screened → 21 included (8 OA PDFs + 13 `not_available_oa`) → 59 excluded across categories A–G.
