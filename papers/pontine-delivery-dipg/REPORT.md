# Methods of delivery to the pons in DIPG and related diseases

Synthesis of **1,066** curated records (1989–2026) on physical delivery of therapeutics to
the pons/brainstem. Per-modality detail is in `notes/`; this report compares routes,
grades their evidence, and states what is missing.

## 1. The problem statement

DIPG/DMG fails treatment for reasons that are at least partly logistical rather than
pharmacological:

- The pontine blood–brain and blood–tumour barrier is largely preserved. Tumours are
  often non-enhancing, the neurovascular unit is comparatively intact
  (El-Khouly 2021, PMID 37284626), and there is evidence the tumour actively maintains
  barrier function (Angpt1 upregulation in H3K27M models, HGG-22 2021 abstract).
- ABCB1/ABCG2 efflux removes what does cross, so nominal brain concentrations overstate
  unbound exposure and delivery method and efflux status are not separable variables
  (Power 2023, PMID 37128506; Tsvankin 2020, PMID 31225627).
- The target has no mechanical tolerance. A few hundred microlitres of infusate deform
  the pons measurably (Bander 2020, PMID 31896089); oedema that would be trivial
  supratentorially is symptomatic here.
- Disease is diffuse and often extends beyond the pons or seeds the CSF, so a focal route
  cannot be the whole answer.

Consequence: trials that do not measure delivery cannot distinguish drug failure from
delivery failure — the single most consistent theme across this literature.

## 2. Route-by-route assessment

| Route | Best pontine evidence | Maturity | Main limitation |
|---|---|---|---|
| Convection-enhanced delivery (CED) | Phase 1/2 trials: ¹²⁴I-omburtamab (Souweidane 2025, PMID 39969230), IL13-PE (Heiss 2019, PMID 30544335), MTX110 (Mueller 2023, PMID 37318058), carboplatin/valproate intermittent CED (Szychot 2021, PMID 33575829), ACNU phase 2 (Saito 2025, PMID 40150841) | **Highest** — repeated dosing via implanted catheters is achievable | Coverage of a diffuse target, reflux, short residence time, infusion-related toxicity (Hollingworth 2022, PMID 35933568) |
| Focused ultrasound BBB opening (FUS-BBBO) | Preclinical brainstem series (Alli 2018, PMID 29753957; Englander 2021, PMID 33753753; Ishida 2021, PMID 33188825; Martinez 2023, PMID 37795179), with RT (Tazhibi 2024, PMID 38555449); pediatric DMG trials (Wu 2025, PMID 41223245) | **Rising fast** — non-invasive and repeatable | Skull/acoustic access to the posterior fossa, transient opening window, does not defeat efflux, oedema budget |
| Intra-arterial ± osmotic BBB disruption | Historical pontine series (Fujiwara 1994, PMID 8108006; Hall 2006, PMID 16314949), balloon-assisted SIACI bevacizumab (Riina 2010, PMID 20377982), SIACI with BBBD in children (McCrea 2021, PMID 34359048), MSC-virus delivery (Carceller 2014, PMID 24327128) | **Feasible but stalled** | Posterior-circulation catheterisation risk, non-selective barrier opening, modern data are mostly supratentorial |
| CSF routes (intrathecal / ICV / fourth ventricle / cisternal) | Fourth-ventricle infusion in piglet and NHP (Sandberg 2008, PMID 18447671; 2012, PMID 22546032); human brainstem CSF tracer distribution (Melin 2023, PMID 38063195); reservoirs/ports in practice | **Mature as hardware, indirect for parenchyma** | Penetration into pontine parenchyma is shallow; best for CSF-adjacent, disseminated disease and cell therapy |
| Locoregional cellular therapy | ICV B7-H3 CAR-T phase 1 in DIPG (Vitanza 2025, PMID 39775044) and non-pontine DMG (Ronsley 2026, PMID 42503899); IV→ICV GD2-CAR (Monje 2025, PMID 39537919; Jiang 2026, PMID 40682569) | **Clinically active, route now standard-of-design** | Local inflammatory neurotoxicity in the pons (Ronsley 2026, PMID 41798119), trafficking, anti-CAR immunity |
| Oncolytic viruses / vectors | Intratumoural DNX-2401 into the pons (Gállego Pérez-Larraya 2022, PMID 35767439); Ad-TD-nsIL12 (Qian 2025, PMID 40721414); MSC carriers (Chastkofsky 2021, PMID 33272983) | **Proof of feasibility in patients** | Single injection distribution, immune clearance, uncertain intratumoural spread |
| Nanocarriers | CED nanofiber depot (Bellat 2020, PMID 32301996); micellar panobinostat CED (Singleton 2017, PMID 28260886); exosomal panobinostat/PPM1D-siRNA (Shan 2022, PMID 35585670) | **Preclinical** | Reach patients only through another route; no pontine clinical trial of a nanocarrier per se |
| Intranasal | Nanoliposomal SN-38 (Sasaki 2023, PMID 36599085); intranasal MSCs; FUS-assisted intranasal focusing (Ye 2020, PMID 32871204) | **Preclinical** | No quantitative human pontine exposure data; poor spatial selectivity alone |
| Implants/depots/devices | Intermittent-CED catheter-port systems; ventricular reservoirs and programmable shunts; skull-implanted FUS arrays (Habashy 2026); osmotic pumps | **Access hardware clinical; depots not pontine** | No cavity for a wafer; infection/revision burden; volume neutrality |
| Systemic BBB-penetrant pharmacology | Panobinostat PBTC phase 1 + CNS PK (Monje 2023, PMID 37526549; Zhang 2023, PMID 37827699); imipridones | **Standard comparator** | Efflux ceiling; whole-body toxicity pays for pontine exposure |
| Radiation-coupled delivery | CED radioisotopes; BNCT salvage in recurrent DMG (Huang 2023, PMID 36821007); FUS + hypofractionated RT (Tazhibi 2024) | **Radiation itself mature; couplings early** | Shared oedema/tolerance budget; re-irradiation constraints (Hug 2026, PMID 41488407) |

## 3. What determines success, independent of route

1. **Volume of distribution vs volume infused (Vd/Vi)** and infusion rate — the core CED
   parameters (Rechberger 2020, PMID 31896090), also implicitly limiting FUS and CSF routes.
2. **Reflux along the catheter track** and trajectory choice through safe entry zones
   (Mukherjee 2020, PMID 30136133 and the safe-entry-zone atlases).
3. **Residence time and clearance** — the failure mode Power 2023 identified and depots
   (Bellat 2020) attack.
4. **Efflux status of the payload** — determines whether opening the barrier is sufficient.
5. **Verification**: MR-visible surrogates (Krauze 2005, PMID 16181805; Saito 2005,
   PMID 16197944), radiolabelled agents (Kommidi 2018, PMID 29456798; ¹²⁴I-omburtamab),
   and cellular biodistribution imaging (Li 2026, PMID 42068336). Unverified delivery is
   the reason so many negative DIPG trials are uninterpretable.
6. **Repeatability** in a child with months of life: hardware (ports, reservoirs,
   implanted arrays) matters as much as pharmacology.

## 4. What related diseases contribute

Chronic ICV/intrathecal dosing in children is an established, years-long practice in CLN2,
MPS II, Sanfilippo, SMA and CLN7 (Hammon 2021, PMID 34076336; Seo 2023, PMID 37922836;
Greenberg 2026, PMID 41314141; Kwon 2026, PMID 41360995), and direct parenchymal infusion
under MRI guidance was developed for Gaucher disease and AADC deficiency (Lonser 2007,
PMID 17065591; Pearson 2021, PMID 34253733; intraputaminal-vs-ICV comparison in
Compton 2023, PMID 36472076). What transfers is operational: device longevity, infection
and immunogenicity management, and route-comparison methodology. What does not transfer is
the therapeutic geometry — these diseases want wide, low-concentration exposure of
non-cytotoxic agents, while a pontine tumour wants focal, high-concentration exposure of
agents that damage tissue if misplaced. See `notes/10_related_diseases_lessons.md`.

## 5. Gaps this collection makes visible

- **Verified dosimetry is rare.** Only 5 records classify primarily as
  imaging/dosimetry/modelling; patient-specific, prospectively validated pontine infusion
  planning (tract- and deformation-aware, with measured Vd/Vi) does not exist in this
  literature.
- **No head-to-head route comparisons in DIPG.** The only controlled route comparisons
  come from gene therapy in other diseases.
- **Residence time is under-engineered.** One clinical strategy (intermittent CED) and a
  handful of preclinical depots address the field's own stated limiting factor.
- **Combined-route protocols are conceptually obvious and empirically absent**: e.g. CED
  or FUS for the pontine bulk plus a CSF route for disseminated/leptomeningeal disease,
  with efflux inhibition for the payload.
- **Posterior-fossa FUS engineering** (skull aberration, implanted arrays, acoustic
  monitoring in the brainstem) is the highest-leverage technical gap, because it is the
  only non-invasive repeatable route.
- **Toxicity of local success.** Locoregional CAR-T shows that delivering enough agent to
  the pons creates its own dose-limiting inflammation; delivery research needs paired
  oedema-management strategies rather than better delivery alone.

## 6. Practical reading order

Start with `notes/00_overview.md`, then `01` (CED) and `02` (FUS) for the two routes with
clinical momentum, `05` for cellular therapy where the route has already changed practice,
`08` for why systemic dosing underperforms, and `09` for how delivery is verified.
