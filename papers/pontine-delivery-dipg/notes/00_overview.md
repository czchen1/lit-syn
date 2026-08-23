# Overview: delivering therapeutics to the pons

## Why the pons is a delivery problem, not only a drug problem

Diffuse intrinsic pontine glioma (DIPG) / H3K27-altered diffuse midline glioma (DMG)
is the paradigmatic "right drug, wrong place" disease. Three properties dominate every
delivery decision:

1. **An intact or near-intact barrier.** Unlike glioblastoma, DIPG typically shows
   little contrast enhancement, and tissue-level work confirms a largely preserved
   neurovascular unit: El-Khouly 2021 (PMID 37284626) characterised the NVU in DIPG
   biopsy/autopsy material against age-matched pons; Haumann 2020 (PBTC/SNO abstract PATH-04)
   compared end-stage DMG pons to healthy controls. Consequently systemic exposure is the exception, not
   the rule, and drug concentrations achieved in the tumour are usually unmeasured.
2. **Active efflux.** ABCB1/ABCG2 at the pontine BBB restrict exactly the classes of
   agents that are otherwise active in vitro. Efflux inhibition changes the outcome of
   delivery experiments: Tsvankin 2020 (PMID 31225627) showed ABC-transporter inhibition
   plus dexamethasone improved CED dasatinib efficacy in H3.3K27M models, and Power's
   work (2020/2021, PMID 37128506 for the synthesis) frames pontine delivery as a
   *residence time* problem — drug that arrives is cleared before it can act.
3. **Anatomical intolerance.** The pons has no expendable volume: infusion, oedema,
   or immune-effector expansion translate directly into cranial-nerve and respiratory
   morbidity. Bander 2020 (PMID 31896089) quantified deformational change after
   brainstem CED; Hollingworth 2022 (PMID 35933568) catalogued infusion-related
   side-effects in brainstem CED. Safety in the pons is therefore route- and
   parameter-specific, not merely drug-specific.

## Route taxonomy used in this collection

| Route | Mechanism | Maturity in pons |
|---|---|---|
| Convection-enhanced delivery (CED) | Pressure-driven bulk flow through interstitium; bypasses BBB entirely | Multiple completed phase 1/2 trials in DIPG |
| Focused ultrasound + microbubbles (FUS-BBBO) | Transient, targeted, non-invasive BBB opening | Preclinical maturity; first pediatric DMG clinical reports |
| Intra-arterial ± osmotic BBB disruption | Regional first-pass concentration; mannitol-opened barrier | Historical brainstem series; modern SIACI experience mostly supratentorial |
| Intraventricular / intrathecal / intra-CSF | CSF as distribution compartment; ports and reservoirs | Strong for CSF-adjacent and disseminated disease; direct 4th-ventricle infusion modelled in large animals |
| Locoregional cellular therapy | Cells as both drug and carrier, delivered ICV or intratumourally | Phase 1 in DMG (B7-H3, GD2) |
| Viral vectors / oncolytic viruses | Intratumoural injection or vector tropism | Phase 1 DIPG (DNX-2401, Ad-TD-nsIL12) |
| Nanocarriers | Improve circulation/uptake, enable co-delivery, or act as depots for CED | Preclinical, plus nanocarrier+CED and nanocarrier+FUS combinations |
| Intranasal | Olfactory/trigeminal bypass of the BBB | Preclinical (nanoliposomal SN-38, MSCs), enhanced by FUS |
| Implants, depots, pumps, ports | Sustained local exposure; repeat access without repeat surgery | Extrapolated from GBM wafers/hydrogels; pontine use limited to catheter/port systems |
| Antibody conjugates and BBB shuttles | Receptor-mediated transcytosis or target-directed payloads | IL13Rα2 ADC/immunotoxin programmes; shuttle work largely non-pontine |
| Systemic BBB-penetrant pharmacology | Chemistry (Kp,uu, efflux avoidance) rather than device | Underpins ONC201, panobinostat, radiosensitiser trials |

## Cross-cutting determinants of success

Nearly every paper in this collection can be read as an intervention on one of six
variables, and this is the most transferable finding of the review:

- **Where the drug enters** (parenchyma, artery, CSF, nose, blood).
- **How much volume is delivered and how fast** — infusion rate, Vd/Vi ratio, reflux
  along the catheter track, backflow into CSF spaces.
- **How long it stays** — residence time, efflux, clearance; addressed by depots
  (Bellat 2020, PMID 32301996), repeat/intermittent infusion (Szychot 2021,
  PMID 33575829), and efflux blockade.
- **Whether distribution can be seen** — co-infused gadolinium and MR-visible
  liposomes (Saito 2005, PMID 16197944; Krauze 2005, PMID 16181805) make CED auditable; FUS BBBO uses
  contrast-enhancement and acoustic feedback.
- **What the anatomy tolerates** — safe entry zones, DTI-defined tracts, and the
  deformation/oedema budget of the pons.
- **Whether the target is focal or disseminated** — up to half of DIPG cases show
  leptomeningeal/subventricular spread; a purely focal route cannot address that
  compartment, which is the main argument for combined CSF + parenchymal strategies.

## How records were selected

See `../README.md`. In brief: brainstem/DIPG-specific delivery papers, plus
generalisable CNS delivery-technique papers, plus non-oncologic CNS diseases where a
*direct* administration route (catheter, CSF port, FUS, intra-arterial) has clinical
experience that transfers to the pons.
