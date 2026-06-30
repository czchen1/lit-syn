# SORT and organ-selective LNP formulation

The central framework for extrahepatic LNP targeting is **Selective ORgan Targeting (SORT)**, introduced by Cheng et al. (2020, PMID 32251383). SORT adds a fifth component — a permanently charged lipid — to the canonical four-component LNP (ionizable lipid, helper phospholipid, cholesterol, PEG-lipid) to redirect biodistribution from the default liver tropism toward lung, spleen, or other organs.

## Mechanism

Dilliard, Cheng & Siegwart (2021, PMID 34272381) and Dilliard et al. (2023, PMID 37527764) showed that SORT works by reshaping the **protein corona** — the layer of serum proteins that adsorbs onto LNPs in circulation. Cationic SORT molecules (e.g. DOTAP, DDAB at 20–50 mol%) recruit complement proteins and immunoglobulins that drive lung endothelial uptake. Anionic SORT lipids recruit alternative opsonins that redirect to splenic macrophages and B cells.

Key findings:
- The organ shift is gradual, not binary: increasing DOTAP from 0→50 mol% progressively shifts expression liver→lung, with a crossover near 20 mol%.
- Protein corona composition (measured by LC-MS/MS proteomics) differs reproducibly between liver- and lung-targeting formulations.
- SORT is compatible with multiple cargo types: Cas9/sgRNA, mRNA, saRNA.

## Quaternary ammonium and charge-tuning approaches

Beyond classical SORT, several groups have demonstrated that the charge state of the ionizable lipid headgroup itself — not just an additive fifth component — controls organ tropism:

- **Piperazine / morpholine headgroups** with permanently protonated quaternary amines shift delivery to lung (Dilliard et al. 2023, PMID 37527764).
- **Zwitterionic headgroups** (betaine-like) favor spleen (Li et al. 2025, PMID 40389003).
- **Cyclic tertiary amines** (Ugi-derived) enable spleen-selective delivery without SORT additives (Wang et al. 2025, PMID 40389004).
- **Imidazole-based lipids** with Zn(II) adjuvant provide spleen-targeted immune activation (Han et al. 2026).

## Phospholipid and helper-lipid contributions

Guerrero et al. (2026, PMID 42367940) and Somu Naidu et al. (2025, PMID 40284455) demonstrate that the **helper phospholipid** (DOPE, DSPC, DPPC) and **cholesterol analogue** (β-sitosterol, stigmasterol) also participate in organ selection:
- DOPE → higher endosomal escape, favors immune-cell transfection.
- DSPC → stabilizes lamellar phase, favors hepatocyte delivery.
- β-Sitosterol substitution for cholesterol increases overall expression without altering organ tropism.

## Multi-organ and programmable targeting

Several 2025–2026 papers report "tunable" systems:
- **Peptide codes** for organ-selective delivery (Chang et al. 2026): surface-displayed peptides can be swapped to redirect the same core LNP to liver, lung, or spleen.
- **FAP-synergistic** organ targeting (Wei et al. 2026): exploiting tumor-microenvironment fibroblast activation protein alongside organ-SORT for extrahepatic tumor delivery.
- **Magnetic LNPs** (Jin et al. 2026): superparamagnetic iron oxide co-encapsulated with mRNA, guided by external magnets to enhance organ-specific accumulation.

## Papers (selected)

- Cheng Q, Wei T, Farbiak L et al. (2020) PMID 32251383 — SORT mechanism, lung/spleen/liver targeting.
- Dilliard SA, Cheng Q, Siegwart DJ (2021) PMID 34272381 — Protein-corona mechanism of SORT.
- Dilliard SA et al. (2023) PMID 37527764 — Quaternary ammonium lipid + corona → lung targeting.
- Heredero J et al. (2025) PMID 40284454 — Predictive lung/spleen targeting, biodegradable ILs.
- Wang Y et al. (2025) — Ugi-derived cyclic amine heads → spleen-selective.
- Guerrero ED et al. (2026) PMID 42367940 — Phospholipid role in SORT.
- Hamilton AG et al. (2026) — HT barcoded in vivo screen for organ-selective LNPs.
