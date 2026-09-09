# 08 — RNA and gene therapy, nanomedicine and delivery

Buckets: `rna_gene_therapy` and `nanomedicine_delivery` (~1,500 records, >90% preclinical). This is the most preclinical-skewed part of the corpus and the part where the gap between mouse data and clinical plausibility is widest.

## 1. What is actually in the clinic

Very little, and mostly early-phase:

- **mRNA immunotherapy:** LNP-encapsulated mRNA-2752 (OX40L/IL-23/IL-36γ) intratumorally with durvalumab (*Clin Cancer Res*, PMID 42149124) — the clearest example of in-situ cytokine engineering with a delivery vehicle.
- **Aptamer:** L-RNA aptamer CXCL12 inhibition with radiotherapy and bevacizumab in newly diagnosed glioblastoma (*Nat Commun*, PMID 41951573).
- **Gene-mediated cytotoxic immunotherapy:** CAN-2409 (aglatimagene besadenovec) with prodrug plus radiotherapy in localised prostate cancer, phase 3 (PMID 42225101) — a rare positive randomised gene-therapy result, discussed further in note 05.
- **TCR/CAR gene therapy** (KRAS-G12V TCR-T, PMID 41814655; in-vivo CAR generation) is covered in notes 01 and 06.
- **Prodrug and nanoformulation trials:** OBI-3424 AKR1C3-activated DNA alkylator phase 2 expansion (PMID 42390142); pegylated liposomal doxorubicin in refractory desmoid tumours, phase 3 (PMID 41504634); drug-eluting/uniform-caliber microsphere embolization (PMID 41889406).
- **siRNA/ASO** entries in the window are almost entirely preclinical; clinical siRNA oncology remains limited to earlier-phase safety work not captured as a randomised readout here.

## 2. Preclinical themes worth tracking

1. **Beyond-liver LNP targeting.** A large fraction of the LNP literature in this window is ionisable-lipid and helper-lipid screening for extrahepatic tropism (lung, spleen, tumour-associated myeloid cells) using SORT-like charge tuning and peptide/antibody decoration. Cross-reference the repository's existing `papers/lnp-cancer-payloads/` collection, which covers this axis in depth.
2. **mRNA payload classes.** Cytokines (IL-12, IL-15, IL-18, IL-21), costimulatory ligands (OX40L, 4-1BBL), bispecific-encoding mRNA, mRNA-encoded CAR for in-vivo T-cell engineering, and mRNA-encoded neoantigen vaccines. In-vivo CAR generation via targeted LNP is the highest-consequence idea in this bucket.
3. **Circular RNA and self-amplifying RNA** for prolonged expression at lower dose; several papers report improved therapeutic index in syngeneic models.
4. **CRISPR in vivo:** base/prime editing to disrupt immunosuppressive genes, PD-1 knockout in adoptive cells, epigenetic editing (CRISPRoff) of oncogenic drivers; delivery, not editing chemistry, is the limiting step in nearly all of them.
5. **Oncolytic and viral vectors** overlap with note 05; AAV capsid engineering for tumour delivery appears but with weak efficacy data.
6. **Stimuli-responsive and biomimetic carriers:** enzyme-, pH-, ROS-, ultrasound- and hypoxia-responsive nanoparticles; cell-membrane-coated and exosome carriers; hydrogels and implantable depots for local sustained release; bacterial and outer-membrane-vesicle delivery (overlaps `microbiome`).
7. **Immunogenic cell death as an endpoint.** A very large number of nanomedicine papers report CRT exposure/HMGB1 release plus abscopal effects in bilateral-tumour mice. This endpoint has poor clinical predictive value; treat it as mechanistic support, not efficacy.

## 3. How to read this bucket critically

The dominant failure mode is a single subcutaneous syngeneic model, small n, tumour-volume-only endpoints, and no pharmacokinetics or biodistribution in a second species. Practical filters when mining `index.tsv`:

- prefer `tier` 1–2 with `topics` containing `in_vivo`;
- prefer papers reporting orthotopic or metastatic models, or non-rodent PK;
- treat "first-in-human evidence" claims in low-tier venues (e.g. carbon-nanoparticle multidrug-resistance reversal, PMID 42249319) with caution — they are usually small uncontrolled cohorts;
- for delivery papers, the transferable content is usually the *vehicle characterisation*, not the therapeutic claim.

Given the volume, this bucket is best used as a screening index: filter by `category` plus a payload keyword in `topics`/title rather than reading linearly.
