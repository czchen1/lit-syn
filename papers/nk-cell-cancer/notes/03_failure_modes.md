# Failure modes, ranked

Ranked by how often they determine the outcome and by how expensive they are to discover late. The first four are
the ones that have actually sunk products or explained disappointing trials; the rest are real but narrower.

## 1. Metabolic collapse after infusion (the dominant efficacy failure)

**Mechanism.** Effector function depends on glycolysis/OXPHOS with amino-acid-dependent cMyc as the checkpoint
(PMID 29904050). The tumour removes exactly those inputs: hypoxia via HIF-1α (PMID 32445619) and SHP-1-mediated
attenuation of STAT3/ERK (PMID 33123602); TGF-β repression of mTOR (PMID 26884601) and metabolic dysfunction in
human metastatic breast cancer (PMID 33568351); lactate-driven lysine **lactylation** of NK proteins
(PMID 40494934); vitamin B6 restriction by pancreatic cancer (PMID 37931287); myCAF exosome-driven glutamine
deprivation in colorectal liver metastasis (PMID 39696364); PPAR-driven lipid accumulation in obesity
(PMID 30420624); C/EBPβ-dependent autophagy inhibition (PMID 39609420). Mitochondrial apoptotic priming sets
killing efficiency at physiological E:T ratios (PMID 35447071).

**Why it is #1.** In vivo single-cell profiling showed CAR-NK relapse coincided with metabolic collapse — not
antigen loss — and cytokine engineering reversed it (PMID 37494448).

**Mitigations, in order of evidence:** cell-intrinsic IL-15; *CISH* knockout to raise cytokine-signalling gain
(PMID 32531207, PMID 32902645); TGF-β resistance (PMID 40119192); expansion platforms that raise metabolic
activation (mbIL-21, PMID 31624330); non-genetic levers such as DHA (PMID 38526128) or fasting-induced niche
remodelling (PMID 38878769). And measure it — see failure mode #4.

## 2. Cryopreservation damage that release testing cannot see

**Mechanism.** Cryopreserved NK cells retain degranulation and 2-D chromium-release activity while losing **3-D
migration and cytotoxicity in tissue-like matrices** (Mark 2020, PMID 33067467); fresh-versus-thawed comparison of
clinical-grade expanded NK cells confirms functional loss (PMID 32536506). Recent mechanism: lysosomal damage
triggering programmed cell death, alleviated by induced stress granules (PMID 42098076), and
composition/temperature/granule-dependent post-thaw survival (PMID 42564981); a dedicated damage-mechanism study
appeared in Cytotherapy (PMID 39918490).

**Why it is #2.** It is silent. A product can meet every release specification and be inert in tissue, and because
clinical papers rarely report post-thaw function, its contribution to weak solid-tumour results is unquantified.

**Mitigations:** DMSO-minimised or DMSO-free formulations benchmarked properly (PMID 41208818, PMID 42098076,
PMID 42564981); intracellular nanoparticle-mediated cryoprotection (PMID 32382476); post-thaw rescue by brief
co-culture restoring motility and killing (PMID 40966444); and — non-negotiable — a **3-D post-thaw potency
assay** (`05_potency_and_release.md`). Note that complex products can be frozen: engager-precomplexed NK cells
retain activity and specificity after cryopreservation (PMID 35225870).

## 3. CD16 shedding and the serial-killing ceiling

**Mechanism.** Activation triggers ADAM17-mediated CD16A cleavage, which limits serial killing
(PMID 41116262) — the killing that matters at the low E:T ratios found in tumours. Antibody- and
engager-dependent designs are hit hardest.

**Mitigations:** hnCD16 (PMID 31856277, clinically deployed in FT596, PMID 39798981); CD16-158V knock-in
(PMID 35135865); *ADAM17* knockout (PMID 31704085); ADAM17 inhibition, which additionally enhances IL-15-driven
activation (PMID 39053944). Donor/variant choice matters too (FcγRIIIA L48-H/R, PMID 39666369).

## 4. Trogocytosis-driven fratricide and antigen dilution (CAR-specific, easy to miss)

**Mechanism.** CAR engagement transfers cognate antigen from tumour to NK cell. The tumour's antigen density
falls *and* the antigen-decorated NK cells become targets for each other. Li 2022 (PMID 36175679) demonstrated
both and rescued them with a **KIR-based inhibitory CAR**.

**Related, simpler case:** self-antigen fratricide. NK cells upregulate CD38 during expansion, so CD38-CAR NK
cells kill each other (fixed by CD38 knockout plus affinity-tuned CAR, PMID 33375774) and daratumumab kills the
product (fixed by CD38 knockout, PMID 32603414).

**Design rule this implies:** before committing to a CAR target, check whether the antigen is expressed on
activated NK cells or transferable by trogocytosis. If yes, plan a knockout or an inhibitory CAR from the start —
not after the in vivo experiment fails.

## 5. TME reprogramming of the infused product

**Mechanism.** TGF-β converts effector NK cells into ILC1-like cells (PMID 28759001), a lineage-level loss of
function, and drives it through SMAD3/E4BP4 (PMID 28262747); CXCR3-driven infiltration produces ILC1-like
plasticity in liver metastasis (PMID 40168086). Beyond TGF-β: Tregs suppress NK cells TGF-β-dependently
(PMID 16230475), MDSCs via NKp30 in HCC (PMID 19551844), CAFs act as cytotoxicity decoys in breast cancer
(PMID 40052789) and reshape NK phenotype in melanoma (PMID 19934056), αv-integrin/TGF-β limits activity against
GBM stem cells (PMID 34138753). Infused NK cells can even become counterproductive — tumour-associated NK cells
driving MDSC-mediated tolerance via IL-6/STAT3 (PMID 38748775). Most sobering: NK cells become functionally
impaired **within hours** of entering a tumour (PMID 38267402).

**Mitigations:** TGF-β/activin resistance (*SMAD4* knockout, PMID 40119192; required for iPSC-NK efficacy against
HCC, PMID 38986609); NKG2A/KLRC1 deletion for HLA-E-high tumours (PMID 39349459, PMID 36706761); sensitising the
tumour instead of the cell (bortezomib lowering HLA-E, PMID 30713790; BET inhibition, PMID 38519469; STING
agonists, PMID 35371622; *CHMP2A* loss making GBM stem cells NK-sensitive, PMID 35393416); or bypassing
trafficking altogether with locoregional delivery (intracranial CAR-NK-92, PMID 37148198).

## 6. Trafficking failure in solid tumours

Distinct from #5: cells that never arrive cannot be reprogrammed. Chemokine-receptor engineering is the direct
answer — CCR7 by trogocytosis for lymph-node homing (PMID 22498742), CCR7 co-delivered with a CAR
(PMID 31114587), CXCR3 in liver metastasis (PMID 40168086); homing biology is reviewed at PMID 35768424. The
pragmatic answer, where anatomy allows, is intratumoral or intracavitary dosing (PMID 37148198).

## 7. Persistence ceiling, and the cost of raising it

Even armoured products persist weeks, not months. Raising it has a documented cost: IL-15/4-1BBL-activated NK
cells were associated with **acute GvHD** after T-cell-depleted HSCT (PMID 25452614) — the clearest reminder that
cytokine armouring is not free. Repeat dosing (PMID 40251398) is the pragmatic mitigation; inducible cytokine
circuits (PMID 32384544) are the engineered one.

## 8. Manufacturing-induced failures that are entirely self-inflicted

- **Feeder residuals and irradiation validation** — a controllable but real CMC burden; PM21 particles
  (PMID 27059202) or feeder-free processes (PMID 41089682) remove it.
- **Medium/supplement switching silently changing potency and phenotype** (PMID 39570247).
- **Editing-related genomic risk outrunning its characterisation.** Multiplex editing raises translocation and
  clonality questions; safety-assessment frameworks for CRISPR-modified NK cells are only now being formalised
  (PMID 41425600). This — not editing efficiency — is what limits edit count.
- **Irradiated cell lines cannot persist by construction.** NK-92 products are safe (PMID 18836917,
  PMID 24094496) but the irradiation that makes them safe removes the variable that drives efficacy.
- **Autologous starting material that is already impaired**: patient NK cells show diminished cytotoxicity
  (PMID 20849361) and marrow NK deficits predict worse daratumumab response in myeloma (PMID 40019438).

## The pattern

Six of the eight failure modes are **fitness** failures rather than recognition failures, and four of them are at
least partly created or fixed in manufacturing. That is the strongest argument in this collection for treating
process development and biology as one problem.
