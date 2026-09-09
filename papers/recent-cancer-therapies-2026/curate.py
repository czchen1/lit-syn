#!/usr/bin/env python3
"""Score, classify and index the harvested six-month cancer-therapy corpus.

Retention: a record is kept when it (a) is about a therapeutic intervention against a
cancer, (b) reports primary evidence — either patients treated (clinical) or a disease
model treated (preclinical) — or is a systematic review / meta-analysis of such
evidence, and (c) is not a narrative review, editorial, comment, erratum, protocol,
single case report, or a purely descriptive / prognostic-signature / epidemiology paper.

Each kept record gets one primary `category` (therapeutic modality), one `evidence`
level (clinical_phase3, clinical_phase2, clinical_phase1, clinical_other,
evidence_synthesis, preclinical), disease `topics`, a journal `tier`, and a `priority`
score used to pick the records discussed in the notes.

Writes index.tsv (sorted by category, evidence, date desc) and curated.json.
"""
import html
import json
import re
from collections import Counter

BASE = "/home/ubuntu/repos/lit-syn/papers/recent-cancer-therapies-2026"

# ---------------------------------------------------------------- cancer context
CANCER = re.compile(
    r"\b(cancer|cancers|tumou?rs?|carcinom\w+|adenocarcinom\w+|leuk?a?emi\w+|lymphom\w+|"
    r"myelom\w+|sarcom\w+|gliom\w+|glioblastom\w+|melanom\w+|neoplas\w+|malignan\w+|"
    r"oncolog\w+|neuroblastom\w+|mesotheliom\w+|blastom\w+|myelodysplas\w+|"
    r"myelofibrosis|metasta\w+|(?-i:\bAML\b|\bALL\b|\bCLL\b|\bCML\b|\bMDS\b|\bDLBCL\b|"
    r"\bNSCLC\b|\bSCLC\b|\bHCC\b|\bTNBC\b|\bGBM\b|\bDIPG\b|\bDMG\b|\bHNSCC\b|\bRCC\b|"
    r"\bCRC\b|\bPDAC\b|\bHGSOC\b|\bMPM\b|\bNMIBC\b|\bMIBC\b|\bmCRPC\b|\bCRPC\b|\bNHL\b|"
    r"\bMCL\b|\bFL\b|\bHL\b|\bMM\b|\bNB\b))", re.I)

THERAPY = re.compile(
    r"\b(therap\w+|treat\w+|inhibitor\w*|antibod\w+|CAR[- ]?T|chimeric antigen receptor|"
    r"vaccin\w+|chemotherap\w+|radiotherap\w+|radiation|immunotherap\w+|blockade|"
    r"regimen|drug|agent|compound|conjugate|engager|bispecific|degrader|PROTAC|"
    r"oncolytic|nanoparticle\w*|nanomedicine|delivery|dose|dosing|efficacy|"
    r"anti-?tumou?r|anti-?cancer|antiproliferative|response rate|remission|cytotox\w+|targeting|"
    r"transplant\w*|ablation|photothermal|photodynamic|sonodynamic|radioligand|"
    r"derivatives|analog\w*|ligand\w*|payload|maintenance|consolidation|induction|"
    r"neoadjuvant|adjuvant|perioperative|first-line|second-line|salvage|"
    r"phase (1|2|3|I|II|III)|randomi[sz]ed|trial|"
    r"[a-z]{4,}(mab|nib|tinib|ciclib|parib|lisib|rasib|stat|platin|taxel|rubicin|tecan|"
    r"leukin|cept|vec|zomib|domide|tostat|metostat|degib|rafenib|sertib|clax|"
    r"fusp|tamig|tafusp|tuximab|zumab|ximab|umab)\b)", re.I)
# Concrete anticancer-agent vocabulary; used to keep clinical reports in the
# catch-all modality bucket from being dominated by behavioural/supportive RCTs.
SPECIFIC_THERAPY = re.compile(
    r"\b(inhibitor\w*|antibod\w+|CAR[- ]?T|vaccin\w+|chemotherap\w+|radiotherap\w+|"
    r"immunotherap\w+|blockade|drug|agent|compound|conjugate|engager|bispecific|degrader|"
    r"oncolytic|nanoparticle\w*|anti-?tumou?r|anti-?cancer|cytotox\w+|transplant\w*|"
    r"ablation|photothermal|photodynamic|sonodynamic|radioligand|payload|"
    r"[a-z]{4,}(mab|nib|tinib|ciclib|parib|lisib|rasib|platin|taxel|rubicin|tecan|"
    r"leukin|cept|vec|zomib|domide|tostat|degib|rafenib|sertib|clax|fusp|tamig)|"
    r"\d+ ?mg|first-in-human|dose[- ](escalation|finding|expansion))\b", re.I)

# ---------------------------------------------------------------- exclusions
EXCLUDE_TITLE = re.compile(
    r"\b(erratum|corrigendum|correction to|correction:|retraction|retracted|withdrawn|"
    r"expression of concern|author'?s? (reply|response)|^(reply|response|in reply)( to)?:|"
    r"(reply|response) to (the )?(letter|comment|editor|editorial|dr\.?|prof)|"
    r"letter to the editor|editorial|commentary|comment on|highlights? (from|of)|news|"
    r"perspectives? (on|from|of)|: an? [a-z]+ perspective$|viewpoint|"
    r"podcast|infographic|abstracts? of the|conference report|meeting report|"
    r"proceedings|congress|symposium|study protocol|trial protocol|protocol for|"
    r"protocol of|statistical analysis plan|rationale and design|design and rationale|"
    r"trial in progress|study design|a systematic review protocol|scoping review|"
    r"narrative review|mini-?review|an? (updated |comprehensive |critical |brief |concise |state-of-the-art |systematic literature )?review|"
    r"review of|overview|what's new|state of the art|current (landscape|status|perspectives?|"
    r"understanding|advances)|recent (advances|progress|developments)|"
    r"advances in|progress in|lessons (from|learned)|"
    r"roadmap|consensus (statement|guideline|recommendation)|guidelines?|recommendations|"
    r"expert (opinion|panel|consensus)|position (paper|statement)|white paper|"
    r"case report|a case of|case series|case presentation|unusual case|rare case|"
    r"cost[- ]effectiveness|cost[- ]utility|budget impact|health technology assessment|"
    r"economic evaluation|willingness to pay|bibliometric|scientometric|altmetric|"
    r"nursing|nurses'?|caregiver|patient education|patient-reported experience|"
    r"questionnaire|survey of|interview study|qualitative study|focus group|"
    r"Mendelian randomi[sz]ation|prognostic (signature|model|nomogram|index)|"
    r"risk (signature|model|score) (for|predict\w*)|nomogram|"
    r"(lncRNA|ferroptosis|cuproptosis|pyroptosis|disulfidptosis|anoikis|m6A|"
    r"immune|metabolism|glycolysis|hypoxia|autophagy|senescence|stemness)-related "
    r"(gene|lncRNA|signature)|gene signature|pan-cancer analysis|bioinformatic\w*|"
    r"in silico (analysis|study)|network pharmacology|molecular docking (study|analysis)|"
    r"screening (program|uptake|adherence)|incidence (and|of)|epidemiolog\w+|"
    r"burden of|trends in|global burden|disparit\w+|socioeconomic|"
    r"machine learning (model|approach) (for|to) predict|radiomic\w*|"
    r"deep learning (model|approach|for) (the )?(diagnos\w+|detect\w+|segment\w+|classif\w+)|"
    r"diagnostic (accuracy|performance|value)|imaging (features|findings)|"
    r"quality of life|financial toxicity|survivorship|palliative care|end-of-life|"
    r"hospice|fertility preservation|sexual (function|health)|"
    r"exercise (intervention|program)|physical activity|psychological|"
    r"mindfulness|acupuncture|traditional Chinese medicine|herbal (medicine|formula)|"
    r"decoction|Ayurved\w+|homeopath\w+|molecular dynamics|density functional|"
    r"DFT (study|calculation)|synthesis, characterization|"
    r"crystal structure|X-ray (diffraction|crystallograph)|"
    r"veterinary|canine (cancer|tumou?r|lymphoma|osteosarcoma)|feline|equine|bovine|"
    r"SARS-CoV-2|COVID|influenza vaccin\w+|\bpain\b|analgesi\w+|an?aesthe\w+|nerve block|"
    r"plane block|nausea|vomiting|anxiety|depressi\w+|insomnia|sleep|kinesiophobia|"
    r"rehabilitation|lymph(o)?edema|dental|oral health|cross-sectional|"
    r"(prediction|predictive|risk prediction) model|machine learning|deep learning|"
    r"artificial intelligence|\bAI[- ]based\b|prognostic (value|significance|marker|factor|"
    r"role|impact|utility|relevance|implication)|prognosis (of|in|for)|biomarkers? (of|for)|"
    r"treatment patterns(?! and (clinical |survival |real-world )?outcomes)|health system costs|"
    r"utili[sz]ation|adherence|"
    r"circulating tumou?r (cells|DNA) (and|as)|ctDNA (as|and) (a )?(prognostic|predictor)|"
    r"association (of|between)|associated with (survival|prognosis|outcome)|"
    r"as an? (early|independent|novel|potential|prognostic|predictive) (biomarker|marker|predictor)|"
    r"detection of|diagnosis of|for the diagnosis|diagnostic|biopsy|colonoscopy|endoscop\w+|"
    r"screening for|surveillance|imaging agent|contrast agent|PET[/-]CT|PET imaging|tracer|"
    r"anticoagul\w+|thromboemboli\w+|thrombosis|grief|coping|bereave\w+|self-management|"
    r"catheter|vascular access|trial (initiation|enrol\w+|participation|recruitment)|"
    r"non-completion|smartphone|mobile app|telehealth|digital health|"
    r"screening (attitudes|uptake|participation|behavio\w+)|self-sampling|overdiagnosis|"
    r"shared decision|decision aid|genetic counsel\w+|counsel(l)?ing|smoking|tobacco|"
    r"varenicline|foot bath|fatigue|summary of research|plain language summary|"
    r"\bprotocol\b|interval design|adaptive design|Bayesian design|trial design|"
    r"knowledge (of|and attitudes)|attitudes|awareness|documentation|liver transplantation for|"
    r"mucositis|constipation|periodontal|febrile neutropenia|thromboprophylaxis|"
    r"antibiotic (selection|timing|prophylaxis)|empirical antibiotics|empiric antibiotic|"
    r"probiotic|prebiotic|synbiotic|multivitamin|vitamin (C|D) (supplementation|deficiency)|"
    r"positive end-expiratory|sedation|scalp cooling|hot flush\w+|night sweats|"
    r"hearing (outcomes|loss)|ototoxicit\w+|cardiotoxic\w+|cardiac (dysfunction|events)|"
    r"bone health|hierarchical composite|psychometric|patient-reported outcome monitoring|"
    r"mailed outreach|text messaging|computer-aided|robot-assisted radical|"
    r"robotic (partial nephrectomy|prostatectomy)|Retzius|cognitive (function|behavioural)|"
    r"rheumatoid arthritis|psoriatic arthritis|atopic dermatitis|ulcerative colitis|"
    r"inflammatory bowel|Parkinson|weight (loss|change)|body mass index|cachexia|"
    r"post-embolization syndrome|peripheral neuropathy|bowel preparation|"
    r"exercise|resistance training|moxibustion|transfusion|hair (loss|growth)|"
    r"ischemic stroke|lower urinary tract|ileus|septic shock|myocardial injury|"
    r"anemia|anaemia|dietary (inflammatory )?(index|pattern)|Mediterranean diet|protein intake|"
    r"prehabilitation|neuropsychological|late effects|interobserver|inter-rater|"
    r"trial eligibility|prescreening|recruitment (strateg|of)|enrolment strateg|"
    r"censoring|effect sizes?|endpoints? in (phase|randomi|oncology)|"
    r"trial design|dose[- ]finding (design|trials?)|generalized pairwise|"
    r"shared decision|decision aid|self-?efficacy|self-?care|body image|"
    r"informed consent|health literacy|large language model|"
    r"nurse[- ]led|nurse navigation|patient navigation|"
    r"segmentectomy|lobectomy|lymph node dissection|anastomotic leak|"
    r"parastomal hernia|oncoplastic|reconstruction|"
    r"biliary (drainage|obstruction)|stent|"
    r"axillary staging|multicancer detection|biomarker validation)",
    re.I)
# Medicinal-chemistry papers mention the clinical stage of comparators; they are preclinical.
MEDCHEM_TITLE = re.compile(
    r"\b(discovery of|design, synthesis|synthesis and (biological )?evaluation|"
    r"structure-activity relationship|structure-based design|scaffold hopping|"
    r"lead optimi[sz]ation|hit-to-lead|cryo-EM|crystal structure)", re.I)

PUBTYPE_EXCLUDE = re.compile(
    r"(Review|Editorial|Comment|Letter|News|Published Erratum|Retraction|Case Reports|"
    r"Practice Guideline|Guideline|Consensus Development Conference|Historical Article|"
    r"Biography|Interview|Lecture|Address|Congress|Video-Audio Media|Clinical Trial Protocol)",
    re.I)
PUBTYPE_SR = re.compile(r"(Systematic Review|Meta-Analysis)", re.I)

# ---------------------------------------------------------------- evidence level
EXPLICIT3 = re.compile(r"\bphase[- ](3|III|2/3|II/III)\b", re.I)
# "clinical_phase3" = phase 3 OR any randomised controlled trial report
PHASE3 = re.compile(
    r"\b(phase (3|III|2/3|II/III)\b|phase[- ](3|III)|randomi[sz]ed,? (controlled|double-blind|"
    r"open-label|phase|multicent|placebo|clinical|non-?inferiority|trial)|"
    r"double-blind,? placebo|placebo-controlled|non-?inferiority trial|"
    r"randomized clinical trial|randomised clinical trial|RCT\b)", re.I)
PHASE2 = re.compile(
    r"\b(phase (2|II|1b/2|Ib/II|1/2|I/II)\b|phase[- ](2|II)|single-arm|single arm|"
    r"basket trial|umbrella trial|platform trial|window[- ]of[- ]opportunity|"
    r"multicenter,? (open-label|single-arm)|expansion cohort)", re.I)
PHASE1 = re.compile(
    r"\b(phase (1|I|Ia|Ib|1a|1b)\b|phase[- ](1|I)\b|first[- ]in[- ]human|first in human|"
    r"dose[- ]escalation|dose[- ]finding|dose[- ]expansion|recommended phase 2 dose|"
    r"maximum tolerated dose|dose[- ]limiting toxicit\w+|\bRP2D\b|\bMTD\b|\bDLT\w?\b)", re.I)
CLINICAL = re.compile(
    r"\b(patients? (were|was|who|with|receiv\w+|underw\w+|treated|enrolled|had|"
    r"aged)|\d+ (patients|participants|subjects|women|men|children|adults|cases)|"
    r"we (treated|enrolled|infused|randomi[sz]ed|analy[sz]ed .{0,40}patients)|"
    r"clinical trial|clinical study|trial\b|cohort|retrospective|prospective|"
    r"real[- ]world|registry|propensity|median (follow-up|OS|PFS|overall survival|"
    r"progression-free survival|duration of response)|"
    r"objective response rate|overall response rate|\bORR\b|complete response|"
    r"partial response|pathologic(al)? complete response|\bpCR\b|"
    r"progression-free survival|overall survival|event-free survival|"
    r"disease-free survival|recurrence-free survival|hazard ratio|\bHR\b \d|"
    r"\bHR,? ?0\.\d|95% CI|adverse events|grade [3-5]|treatment-related|"
    r"NCT0?\d{7}|ClinicalTrials\.gov|ChiCTR|jRCT|EudraCT|ISRCTN|UMIN)", re.I)
PRECLINICAL = re.compile(
    r"\b(mice|mouse|murine|\bNSG\b|\bNOG\b|xenograft\w*|\bPDX\w*\b|patient-derived xenograft|"
    r"orthotopic|syngeneic|allograft|rats?\b|zebrafish|canine model|non[- ]human primate|"
    r"macaque|rhesus|cynomolgus|in vitro|in vivo|ex vivo|cell lines?|organoids?|"
    r"spheroids?|humani[sz]ed (mouse|mice)|genetically engineered mouse|\bGEMM\b|"
    r"tumou?r[- ]bearing|CDX model|preclinical|pre-clinical|knock-?out|knockdown|"
    r"CRISPR|shRNA|siRNA|western blot|flow cytometry|RNA-seq|single-cell RNA|"
    r"transcriptom\w+|proteom\w+|co-culture|cytotoxicity assay|IC50|IC₅₀|"
    r"molecular docking|structure-activity|\bSAR\b|pharmacokinetic\w* in (mice|rats)|"
    r"tumou?r growth inhibition|tumou?r regression|tumou?r volume)", re.I)
INVIVO = re.compile(
    r"\b(mice|mouse|murine|\bNSG\b|xenograft\w*|\bPDX\w*\b|orthotopic|syngeneic|"
    r"allograft|rats?\b|zebrafish|non[- ]human primate|macaque|cynomolgus|in vivo|"
    r"humani[sz]ed (mouse|mice)|genetically engineered mouse|tumou?r[- ]bearing|"
    r"tumou?r growth inhibition|tumou?r regression|tumou?r volume|"
    r"patient-derived organoid|organoids?)", re.I)
SR_MA = re.compile(
    r"\b(systematic review|meta[- ]analy\w+|network meta|pooled analysis|umbrella review|"
    r"individual patient data|individual participant data|PRISMA)", re.I)
# Vocabulary that only appears when patients were actually treated in the study.
STRONG_CLIN = re.compile(
    r"\b(\d+ (patients|participants|pts|women|men|children|adults) (were|with|received|"
    r"underwent|enrolled|treated|randomi[sz]ed|aged)|patients (were|received|underwent|"
    r"enrolled|treated|randomi[sz]ed)|we (treated|enrolled|infused|randomi[sz]ed)|"
    r"NCT0?\d{7}|ChiCTR|jRCT|EudraCT|ISRCTN|UMIN|median follow-up|objective response rate|"
    r"overall response rate|\bORR\b|dose[- ]limiting toxicit\w+|\bRP2D\b|"
    r"recommended phase 2 dose|maximum tolerated dose|were enrolled|were randomi[sz]ed|"
    r"were treated|were assigned|randomly assigned|primary end ?point|"
    r"treatment-related adverse events|\bTRAEs?\b|grade [3-5] (adverse|toxicit|TRAE))", re.I)
MODEL_ONLY = re.compile(r"\b(mice|mouse|murine|xenograft\w*|in vivo|in vitro|cell lines?)\b", re.I)

# ---------------------------------------------------------------- modality classification
MODALITY = {
    "cell_therapy": r"\b(CAR[- ]?T\b|CAR[- ]?T[- ]cells?|chimeric antigen receptor|CAR[- ]NK|"
        r"CAR[- ]NKT|CAR[- ]M\b|CAR[- ]macrophage|CAR[- ]Treg|TCR[- ]T\b|TCR[- ]engineered|"
        r"T[- ]cell receptor[- ](engineered|therapy|gene)|"
        r"tumou?r[- ]infiltrating lymphocyte\w* (therapy|product|infusion|treatment|transfer)|"
        r"(autologous|adoptive|expanded|engineered) tumou?r[- ]infiltrating lymphocyte\w*|"
        r"\bTILs?\b (therapy|product|infusion)|lifileucel|afamitresgene|afami-cel|obecabtagene|axicabtagene|"
        r"tisagenlecleucel|lisocabtagene|idecabtagene|ciltacabtagene|brexucabtagene|"
        r"cilta-cel|ide-cel|axi-cel|liso-cel|tisa-cel|anitocabtagene|zevorcabtagene|"
        r"equecabtagene|satri-cel|satricabtagene|relmacabtagene|adoptive (cell|T[- ]cell|"
        r"NK[- ]cell) (therapy|transfer|immunotherapy)|adoptively transferred|"
        r"γδ T|gamma[- ]?delta T|gammadelta T|Vδ[12]|Vγ9Vδ2|Vdelta[12]|"
        r"NK[- ]cell (therapy|immunotherapy|product|infusion)|natural killer cell (therapy|"
        r"immunotherapy|infusion)|iPSC-derived (NK|T)|\biNK\b|cytokine-induced killer|"
        r"\bCIK\b|\bNKT\b cells?|invariant NKT|in vivo CAR|in situ CAR|engineered T cells?|"
        r"armou?red CAR|allogeneic CAR|universal CAR|off-the-shelf CAR|synNotch|"
        r"logic[- ]gated|virus-specific T cells?|EBV-specific T|donor lymphocyte infusion|"
        r"cell therapy|cellular (therapy|immunotherapy))",
    "bispecific_tce": r"\b(bispecific|bi-specific|trispecific|tri-specific|multispecific|"
        r"T[- ]cell[- ]engag\w+|T[- ]cell[- ]redirect\w+|\bBiTEs?\b|\bTCEs?\b|"
        r"blinatumomab|teclistamab|talquetamab|elranatamab|linvoseltamab|glofitamab|"
        r"epcoritamab|mosunetuzumab|odronextamab|tarlatamab|tebentafusp|ImmTAC|"
        r"brenetafusp|xaluritamig|ivonescimab|cadonilimab|amivantamab|zanidatamab|"
        r"zenocutuzumab|acasunlimab|volrustomig|rilvegostomig|tobemstomig|"
        r"PD-1[/×x ]VEGF|PD-L1[/×x ]4-1BB|PD-1[/×x ]CTLA-4|PD-1[/×x ]TIGIT|"
        r"CD3[- ]?(bispecific|engager)|[a-z]+tamig\b|[a-z]+fusp\b|"
        r"[a-z]+stomig\b|catumaxomab|emicizumab-like|DART\b|TandAb|BiKE|TriKE|"
        r"NK[- ]cell engager|NKCE|myeloid engager)",
    "adc": r"\b(antibody[- ]drug conjugates?|\bADCs?\b|immunoconjugate|drug conjugate|"
        r"deruxtecan|T-DXd|govitecan|vedotin|soravtansine|tesirine|ozogamicin|"
        r"emtansine|T-DM1|tirumotecan|rezetecan|samrotecan|ledadotin|mafodotin|"
        r"pelidotin|duocarmazine|(?!irinotecan|topotecan|belotecan|lurtotecan)[a-z]+tecan\b|"
        r"[a-z]+dotin\b|[a-z]+tansine\b|"
        r"peptide[- ]drug conjugate|\bPDCs?\b|bispecific ADC|payload|"
        r"topoisomerase I payload|linker[- ]payload|drug-to-antibody ratio|(?-i:\bDAR\b)|"
        r"radioconjugate|antibody[- ]oligonucleotide conjugate)",
    "checkpoint": r"\b(immune checkpoint|checkpoint (inhibitor|blockade|therapy)|\bICIs?\b|"
        r"\bICB\b|anti-PD-?1|anti-PD-?L1|PD-?1 (blockade|inhibitor|antibody|inhibition)|"
        r"PD-?L1 (blockade|inhibitor|antibody|inhibition)|PD-?1/PD-?L1|CTLA-?4|"
        r"pembrolizumab|nivolumab|atezolizumab|durvalumab|ipilimumab|cemiplimab|avelumab|"
        r"tislelizumab|toripalimab|sintilimab|camrelizumab|serplulimab|penpulimab|"
        r"dostarlimab|retifanlimab|tremelimumab|relatlimab|fianlimab|zimberelimab|"
        r"sugemalimab|envafolimab|adebrelimab|benmelstobart|socazolimab|pucotenlimab|"
        r"LAG-?3|TIGIT|TIM-?3|VISTA|NKG2A|monalizumab|tiragolumab|domvanalimab|"
        r"vibostolimab|belrestotug|CD47|magrolimab|SIRPα|SIRPa|B7-H[34]|CD73|"
        r"A2A(R)? (antagonist|receptor)|CCR8|ILT[24]|LILRB[124]|PVRIG|CD96|"
        r"immune-related adverse|irAEs?\b|[a-z]+limab\b)",
    "cancer_vaccine": r"\b(cancer vaccin\w+|tumou?r vaccin\w+|neoantigen|neo-antigen|"
        r"personali[sz]ed (cancer )?vaccin\w+|individuali[sz]ed neoantigen|mRNA[- ]vaccin\w+|"
        r"mRNA-4157|V940|intismeran|autogene cevumeran|BNT1\d\d|dendritic cell vaccin\w+|"
        r"DC vaccin\w+|peptide vaccin\w+|DNA vaccin\w+|therapeutic vaccin\w+|"
        r"in situ vaccin\w+|whole[- ]cell vaccin\w+|tumou?r lysate|vaccination|"
        r"ELI-002|cevumeran|antigen-specific T[- ]cell (induction|response)|"
        r"vaccine)",
    "oncolytic_virus": r"\b(oncolytic|virotherapy|talimogene|T-VEC|RP1\b|vusolimogene|"
        r"nadofaragene|cretostimogene|CG0070|DNX-2401|Delta-24|teserpaturev|"
        r"olvimulogene|pelareorep|reovirus|vaccinia|Newcastle disease virus|"
        r"vesicular stomatitis virus|measles virus|adenovirus|herpes simplex virus|"
        r"HSV-1|\bHSV\b|engineered bacteri\w+|bacterial (cancer |immuno)?therapy|"
        r"Salmonella|Listeria|Clostridium novyi|tumou?r-targeting bacteri\w+|"
        r"bacteria-mediated|bacteriotherapy|Coley)",
    "targeted_ras_mapk": r"\b(KRAS|\bRAS\b|NRAS|HRAS|G12C|G12D|G12V|G13D|Q61|pan-RAS|"
        r"RAS\(ON\)|sotorasib|adagrasib|divarasib|olomorasib|glecirasib|garsorasib|"
        r"fulzerasib|MRTX1133|zoldonrasib|daraxonrasib|elironrasib|RMC-\d+|"
        r"[a-z]+rasib\b|SHP2|SOS1|BRAF|V600E|V600|MEK|\bERK\b|MAPK|dabrafenib|"
        r"trametinib|encorafenib|binimetinib|vemurafenib|cobimetinib|tovorafenib|"
        r"pan-RAF|RAF inhibitor|naporafenib|avutometinib|defactinib|mirdametinib|"
        r"selumetinib|[a-z]+rafenib\b|[a-z]+metinib\b|\bFAK\b)",
    "targeted_kinase": r"\b(tyrosine kinase inhibitor\w*|\bTKIs?\b|kinase inhibitor|"
        r"EGFR|osimertinib|lazertinib|furmonertinib|aumolertinib|befotertinib|"
        r"sunvozertinib|zipalertinib|gefitinib|erlotinib|afatinib|dacomitinib|"
        r"HER2-mutant|zongertinib|sevabertinib|BAY 2927088|neratinib|tucatinib|pyrotinib|"
        r"lapatinib|\bALK\b|alectinib|lorlatinib|brigatinib|ensartinib|iruplinalkib|"
        r"crizotinib|ROS1|repotrectinib|taletrectinib|entrectinib|\bRET\b|selpercatinib|"
        r"pralsetinib|\bMET\b (exon|amplif|inhibitor)|c-MET|capmatinib|tepotinib|"
        r"savolitinib|NTRK|TRK inhibitor|larotrectinib|FGFR\d?|erdafitinib|pemigatinib|"
        r"futibatinib|lirafugratinib|HER3|PI3K\w*|PIK3CA|\bAKT\b|mTOR|capivasertib|"
        r"inavolisib|alpelisib|ipatasertib|gedatolisib|RLY-2608|everolimus|"
        r"CDK4/6|CDK[0-9]{1,2}\b|palbociclib|ribociclib|abemaciclib|dalpiciclib|"
        r"atirmociclib|[a-z]+ciclib\b|Aurora kinase|alisertib|PLK1|WEE1|adavosertib|"
        r"azenosertib|\bATR\b|ceralasertib|camonsertib|CHK1|PKMYT1|lunresertib|DNA-PK|"
        r"lenvatinib|sorafenib|regorafenib|cabozantinib|axitinib|sunitinib|pazopanib|"
        r"anlotinib|apatinib|fruquintinib|surufatinib|VEGFR|anti-?angiogen\w+|"
        r"bevacizumab|ramucirumab|HIF-?2α|HIF-?2 ?alpha|belzutifan|\bBTK\b|ibrutinib|"
        r"acalabrutinib|zanubrutinib|pirtobrutinib|nemtabrutinib|BCL-?2|venetoclax|"
        r"sonrotoclax|lisaftoclax|MCL-?1|FLT3|gilteritinib|quizartinib|midostaurin|"
        r"\bJAK\d?\b|ruxolitinib|momelotinib|fedratinib|pacritinib|XPO1|selinexor|"
        r"IRAK4|emavusertib|\bSYK\b|\bSRC\b inhibitor|\bABL\b|imatinib|dasatinib|"
        r"nilotinib|ponatinib|asciminib|bosutinib|olverembatinib|(?-i:\bKIT\b)|avapritinib|"
        r"ripretinib|\bCSF1R\b|pexidartinib|vimseltinib|[a-z]+tinib\b|[a-z]+lisib\b|"
        r"[a-z]+sertib\b|[a-z]+anib\b|[a-z]+zomib\b|kinase)",
    "targeted_ddr": r"\b(PARP\d?|PARPi|olaparib|niraparib|rucaparib|talazoparib|saruparib|"
        r"AZD5305|senaparib|fuzuloparib|pamiparib|[a-z]+parib\b|homologous recombination|"
        r"\bHRD\b|\bBRCA[12]?\b|synthetic lethal\w*|POLQ|Polθ|Pol theta|\bWRN\b|USP1|"
        r"RAD51|\bATM\b inhibitor|DNA damage response|\bDDR\b|DNA repair|"
        r"replication stress|PARP inhibitor)",
    "targeted_heme": r"\b(menin|revumenib|ziftomenib|bleximenib|enzomenib|[a-z]+menib\b|"
        r"KMT2A|NPM1|IDH[12]?\b|ivosidenib|enasidenib|olutasidenib|vorasidenib|"
        r"[a-z]+sidenib\b|CELMoD|iberdomide|mezigdomide|golcadomide|[a-z]+domide\b|"
        r"lenalidomide|pomalidomide|thalidomide|cereblon|proteasome inhibitor|bortezomib|"
        r"carfilzomib|ixazomib|hypomethylating|azacitidine|decitabine|venetoclax|"
        r"anti-CD38|daratumumab|isatuximab|anti-CD20|rituximab|obinutuzumab|"
        r"anti-CD19|tafasitamab|sabatolimab|BCMA|GPRC5D|CD123|CD33|CLL-1|CLEC12A|CD70|"
        r"\bCD7\b|FcRH5|\bTP53\b-mutant (AML|MDS)|luspatercept|imetelstat|"
        r"(?-i:\bAML\b|\bMDS\b|\bALL\b|\bCLL\b|\bCML\b)|myelom\w+|lymphom\w+|leuk?a?emi\w+|"
        r"myelofibrosis|myelodysplastic|Waldenstr[öo]m)",
    "degrader": r"\b(PROTACs?|proteolysis[- ]targeting chimer\w+|targeted protein degradation|"
        r"protein degrader|degrader|molecular glue|bifunctional degrader|ARV-\d+|"
        r"bavdegalutamide|vepdegestrant|NX-5948|BGB-16673|KT-\d+|LYTAC|AUTAC|"
        r"hydrophobic tag|E3 ligase|cereblon|VHL)",
    "epigenetic": r"\b(EZH[12]|tazemetostat|valemetostat|tulmimetostat|[a-z]+metostat\b|"
        r"HDAC\d?|histone deacetylase|vorinostat|panobinostat|romidepsin|tucidinostat|"
        r"chidamide|entinostat|[a-z]+inostat\b|\bBET\b (inhibitor|protein)|BRD[2-4]|"
        r"bromodomain|pelabresib|DNMT\d?|DNA methyltransferase|LSD1|KDM1A|bomedemstat|"
        r"iadademstat|PRMT5|MTA-cooperative|MAT2A|DOT1L|KAT6[AB]?|SETD2|\bKDM\d|"
        r"epigenetic|chromatin|SWI/SNF|SMARCA[24]|ARID1A|histone (methyl|acetyl)\w+|"
        r"H3K27|H3K36|EED\b|PRC2|ONC201|dordaviprone|ONC206|imipridone|ClpP)",
    "endocrine": r"\b(endocrine therapy|aromatase inhibitor|letrozole|anastrozole|exemestane|"
        r"fulvestrant|tamoxifen|SERDs?\b|estrogen receptor degrader|oestrogen receptor|"
        r"elacestrant|imlunestrant|camizestrant|giredestrant|vepdegestrant|palazestrant|"
        r"[a-z]+estrant\b|ESR1|androgen deprivation|androgen receptor|\bADT\b|\bARPI\b|"
        r"enzalutamide|apalutamide|darolutamide|abiraterone|relugolix|[a-z]+lutamide\b|"
        r"castration-resistant|hormone[- ]sensitive|hormone therapy|antiandrogen|"
        r"GnRH|LHRH|goserelin|leuprolide|degarelix|hormone receptor-positive|\bHR\+)",
    "radiopharm": r"\b(radioligand|radiopharmaceutical\w*|radionuclide|177Lu|Lu-?177|"
        r"lutetium|PSMA-617|vipivotide|PSMA (radioligand|therapy|targeted)|225Ac|"
        r"actinium|targeted alpha|alpha[- ]emit\w+|212Pb|lead-212|radium-223|Ra-223|"
        r"radioimmunotherapy|peptide receptor radionuclide|\bPRRT\b|DOTATATE|"
        r"DOTATOC|FAP[- ]?(radioligand|targeted)|FAPI|theranostic\w*|radiolabel\w+|"
        r"131I|iodine-131|90Y|yttrium-90|Y-?90|radioembolization|boron neutron|BNCT|"
        r"radiotracer|PET imaging|radiotheranostic|auger)",
    "radiotherapy": r"\b(radiotherapy|radiation therapy|radiation oncology|irradiation|"
        r"stereotactic|SBRT|SABR|SRS\b|hypofractionat\w+|fractionation|FLASH|proton|"
        r"carbon[- ]ion|heavy[- ]ion|chemoradi\w+|radiosensiti\w+|radioresist\w+|"
        r"brachytherapy|total body irradiation|(?-i:\bTBI\b)|IMRT|VMAT|MR-guided|"
        r"adaptive radiotherapy|whole[- ]brain radiotherapy|\bWBRT\b|craniospinal|"
        r"(?-i:\bGy\b)|dose (escalation|de-escalation) radiotherapy|radiation)",
    "rna_gene_therapy": r"\b(lipid nanoparticles?|\bLNPs?\b|mRNA(-|\s)(therap\w+|encoded|"
        r"LNP|based|delivery)|\bmRNA\b|circular RNA|circRNA|self-amplifying RNA|saRNA|"
        r"siRNA|small interfering RNA|antisense oligonucleotide\w*|\bASOs?\b|"
        r"RNA interference|RNAi|microRNA|miRNA|miR-\d+|RNA therap\w+|aptamer|"
        r"gene therapy|gene editing|genome editing|CRISPR|Cas9|Cas12|Cas13|base edit\w+|"
        r"prime edit\w+|epigenome edit\w+|adeno-associated virus|\bAAV\b|lentivir\w+|"
        r"suicide gene|gene-directed enzyme|GDEPT|TP53 gene|p53 reactivat\w+|"
        r"rezatapopt|PC14586|eprenetapopt|APR-246|MDM2|brigimadlin|navtemadlin|"
        r"milademetan|idasanutlin|alrizomadlin|mutant p53|oligonucleotide|"
        r"nucleic acid (therap\w+|delivery)|plasmid|DNA delivery|non-viral (vector|delivery))",
    "cytokine_innate": r"\b(interleukin-?\d+|\bIL-?\d+\b|IL-?2 (variant|receptor|agonist)|"
        r"N-803|nogapendekin|Anktiva|IL-15 superagonist|cytokine (therapy|fusion|engineering)|"
        r"immunocytokine|engineered cytokine|interferon|IFN-?[αβγ]|IFN-?(alpha|beta|gamma)|"
        r"STING|cGAS|TLR\d?\b|toll-like receptor|CD40|4-1BB|CD137|OX40|CD134|GITR|"
        r"CD27|NKG2D|RIG-I|innate immun\w+ agonist|bempegaldesleukin|nemvaleukin|"
        r"eciskafusp|efineptakin|PD1-IL2v|IL-2Rβγ|IL-2Rβ|aldesleukin|"
        r"intravesical|\bBCG\b|Bacillus Calmette|NMIBC|non-muscle[- ]invasive|"
        r"[a-z]+leukin\b|[a-z]+kafusp\b|imiquimod|resiquimod|CpG|poly\(I:C\)|"
        r"inflammasome|GM-CSF|sargramostim|thymosin|immunostimula\w+|immunomodulat\w+)",
    "antibody_other": r"\b(monoclonal antibod\w+|\bmAbs?\b|therapeutic antibod\w+|"
        r"antibody therapy|trastuzumab|pertuzumab|margetuximab|cetuximab|panitumumab|"
        r"necitumumab|anti-HER2|anti-EGFR|anti-GD2|GD2|naxitamab|dinutuximab|hu14\.18|"
        r"ch14\.18|claudin ?18\.2|CLDN18\.2|zolbetuximab|osemitamab|TROP-?2|DLL3|"
        r"Nectin-?4|CEACAM5|CD30|Fc-?engineered|Fc-?enhanced|afucosylated|\bADCC\b|"
        r"antibody-dependent cell\w* cytotoxicity|\bADCP\b|(?-i:\bCDC\b)|complement-dependent|"
        r"TGF-?β|TGF-?beta|bintrafusp|anti-IL-?8|anti-IL-?1β|anti-LIF|denosumab|"
        r"RANKL|anti-CD38|daratumumab|isatuximab|rituximab|obinutuzumab|ofatumumab|"
        r"ublituximab|tafasitamab|anti-CD19|anti-CD20|brentuximab|alemtuzumab|"
        r"mogamulizumab|CCR4|siltuximab|tocilizumab|elotuzumab|SLAMF7|[a-z]+mab\b|"
        r"nanobod\w+|single-domain antibod\w+|\bsdAb\b|\bVHH\b|scFv|antibody fragment|"
        r"biosimilar)",
    "chemo_conventional": r"\b(chemotherap\w+|chemo-?immunotherapy|neoadjuvant|adjuvant|"
        r"perioperative|total neoadjuvant|watch[- ]and[- ]wait|organ preservation|"
        r"de-?escalation|dose-dense|metronomic|HIPEC|hyperthermic intraperitoneal|PIPAC|"
        r"intraperitoneal|hepatic arterial infusion|\bHAIC\b|chemoembolization|\bTACE\b|"
        r"\bTARE\b|FOLFIRINOX|NALIRIFOX|FOLFOX|FOLFIRI|CAPOX|XELOX|gemcitabine|"
        r"nab-paclitaxel|paclitaxel|docetaxel|cabazitaxel|cisplatin|carboplatin|"
        r"oxaliplatin|capecitabine|5-fluorouracil|5-FU|fluorouracil|S-1\b|TAS-102|"
        r"trifluridine|temozolomide|lurbinectedin|trabectedin|eribulin|irinotecan|"
        r"topotecan|etoposide|pemetrexed|doxorubicin|epirubicin|daunorubicin|"
        r"idarubicin|liposomal (irinotecan|doxorubicin)|mitomycin|vincristine|"
        r"vinorelbine|vinblastine|cyclophosphamide|ifosfamide|bendamustine|"
        r"melphalan|busulfan|fludarabine|cytarabine|methotrexate|CPX-351|"
        r"anthracycline|platinum|taxane|alkylating|antimetabolite|"
        r"R-CHOP|CHOP|Pola-R-CHP|ABVD|BEACOPP|hyper-CVAD|7\+3|induction chemotherapy|"
        r"consolidation|maintenance)",
    "transplant": r"\b(h?a?ematopoietic (stem )?cell transplant\w*|stem cell transplant\w*|"
        r"\bHSCT\b|\bHCT\b|allo-?HSCT|allo-?HCT|allogeneic transplant\w*|"
        r"autologous (stem cell )?transplant\w*|\bASCT\b|\bAuto-?SCT\b|conditioning regimen|"
        r"graft-versus-host|GVHD|GvHD|post-transplant cyclophosphamide|PTCy|"
        r"haploidentical|cord blood|donor|engraftment|graft-versus-leuk?a?emia|"
        r"reduced-intensity conditioning|myeloablative)",
    "nanomedicine_delivery": r"\b(nanoparticles?|nanomedicine|nanocarrier\w*|nano-?drug\w*|"
        r"nanoplatform|nanosystem|nanoassembl\w+|nanotherap\w+|nanoformulation|"
        r"nanovaccine|nanozyme|nanosheet|nanorod|nanocage|nanogel|nanofiber|"
        r"nanocluster|nanomotor|nanoreactor|nanoprodrug|liposom\w+|micell\w+|"
        r"polymeric|polymersome|dendrimer|hydrogel|exosom\w+|extracellular vesicle\w*|"
        r"\bEVs\b|cell membrane-coated|biomimetic|metal-organic framework|\bMOFs?\b|"
        r"mesoporous silica|gold nano\w*|iron oxide|quantum dot|upconversion|"
        r"self-assembl\w+|microneedle|implant\w+|drug-eluting|drug delivery|"
        r"controlled release|sustained release|targeted delivery|tumou?r-targeted delivery|"
        r"stimuli-responsive|pH-responsive|ROS-responsive|GSH-responsive|"
        r"enzyme-responsive|prodrug|albumin-bound|PEGylat\w+|"
        r"blood-brain barrier (penetrat\w+|crossing|permeab\w+)|BBB-penetra\w+|"
        r"convection-enhanced|intranasal|intratumou?ral (injection|delivery|administration))",
    "physical_ablative": r"\b(photodynamic|photothermal|sonodynamic|chemodynamic|"
        r"photoimmunotherapy|photo-?immunotherapy|near-infrared|\bNIR\b|photosensiti\w+|"
        r"sonosensiti\w+|focused ultrasound|\bHIFU\b|histotripsy|tumou?r treating fields|"
        r"TTFields|irreversible electroporation|(?-i:\bIRE\b)|electrochemotherapy|cryoablation|"
        r"cryotherapy|radiofrequency ablation|\bRFA\b|microwave ablation|"
        r"magnetic hyperthermia|hyperthermia|thermal ablation|ablation|laser|"
        r"ultrasound-?(triggered|mediated|guided)|electric field|"
        r"ferroptosis|pyroptosis|cuproptosis|disulfidptosis|immunogenic cell death|(?-i:\bICD\b)|"
        r"photothermal therapy|\bPTT\b|\bPDT\b|\bSDT\b|\bCDT\b)",
    "tme_metabolic": r"\b(tumou?r microenvironment|\bTME\b|tumou?r-associated macrophage\w*|"
        r"(?-i:\bTAMs?\b)|myeloid-derived suppressor|\bMDSCs?\b|regulatory T cells?|\bTregs?\b|"
        r"cancer-associated fibroblast\w*|\bCAFs?\b|fibroblast activation protein|\bFAP\b|"
        r"tertiary lymphoid|\bTLSs?\b|neutrophil\w*|(?-i:\bTANs?\b|\bNETs?\b)|"
        r"macrophage (reprogramming|repolari[sz]ation|polari[sz]ation)|M2 macrophage|"
        r"CSF-?1R|TREM2|MARCO|Siglec|myeloid checkpoint|CXCR[24]|CXCL12|CXCL13|CCL2|CCR2|"
        r"TGF-?β|IDO1?\b|arginase|ARG1|adenosine|CD39|CD73|A2AR|glutamin\w+|"
        r"glutamine antagonist|DON prodrug|DRP-104|sirpiglenastat|lactate|LDHA?\b|MCT[14]|"
        r"fatty acid (oxidation|synthesis)|FASN|CPT1|OXPHOS|oxidative phosphorylation|"
        r"mitochondrial|metabolic (vulnerabilit\w+|reprogramming|therapy)|metabolism|"
        r"glycolysis|Warburg|dietary|diet\b|ketogenic|fasting|methionine|serine|"
        r"cystine|SLC7A11|xCT|GPX4|NAD\+|nicotinamide|PD-L1 expression|"
        r"immunosuppressive|immune evasion|immune escape|T cell exhaustion|exhausted T|"
        r"cold tumou?rs?|hot tumou?rs?|T cell infiltration|antigen presentation|MHC|HLA|"
        r"cancer stem cells?|\bCSCs?\b|stemness|senescence|senolytic|hypoxia|angiogenesis)",
    "microbiome": r"\b(microbiom\w+|microbiota|fecal microbiota|faecal microbiota|\bFMT\b|"
        r"probiotic\w*|prebiotic\w*|postbiotic\w*|Akkermansia|Bifidobacterium|"
        r"Lactobacillus|Faecalibacterium|live biotherapeutic|CBM588|intratumou?ral "
        r"(bacteria|microbiome|microbiota)|gut bacteria|commensal|dysbiosis|"
        r"short-chain fatty acid|butyrate|bacterial metabolite|antibiotic exposure)",
    "repurposed": r"\b(drug repurposing|repurposed|repositioning|metformin|statins?\b|"
        r"atorvastatin|simvastatin|aspirin|beta-?blocker|propranolol|GLP-1|semaglutide|"
        r"tirzepatide|ivermectin|mebendazole|disulfiram|itraconazole|antihistamine|"
        r"vitamin [CD]|omega-3|ascorbate|hydroxychloroquine|chloroquine|cannabinoid|"
        r"cannabidiol|\bCBD\b|psilocybin|antipsychotic|antidepressant|fluoxetine|"
        r"sertraline|celecoxib|NSAID|digoxin|niclosamide|nitroglycerin|losartan|"
        r"ACE inhibitor|angiotensin|anticoagulant|heparin|warfarin|denosumab|"
        r"bisphosphonate|zoledronic|dexamethasone|corticosteroid|antibiotic\w*|"
        r"antiviral|antifungal|artesunate|thalidomide|melatonin|curcumin|resveratrol|"
        r"quercetin|berberine|natural product|phytochemical|flavonoid|polyphenol)",
}
MODALITY_RE = {k: re.compile(v + r"\b", re.I) for k, v in MODALITY.items()}

# The harvest domain is the tie-breaker; sweeps and paediatric/CNS groups are not
# modalities and so carry no vote.
DOMAIN_TO_CATEGORY = {
    "cell_therapy": "cell_therapy", "bispecific_tce": "bispecific_tce", "adc": "adc",
    "checkpoint": "checkpoint", "cancer_vaccine": "cancer_vaccine",
    "oncolytic_virus": "oncolytic_virus", "targeted_ras_mapk": "targeted_ras_mapk",
    "targeted_kinase": "targeted_kinase", "targeted_ddr": "targeted_ddr",
    "endocrine": "endocrine", "targeted_heme": "targeted_heme", "degrader": "degrader",
    "epigenetic": "epigenetic", "radiopharm_radiotherapy": "radiotherapy",
    "rna_gene_therapy": "rna_gene_therapy", "cytokine_innate": "cytokine_innate",
    "antibody_other": "antibody_other", "chemo_conventional": "chemo_conventional",
    "nanomedicine_delivery": "nanomedicine_delivery",
    "tme_metabolic_microbiome": "tme_metabolic",
}

# Specific-before-generic ordering used when scores tie.
CATEGORY_ORDER = [
    "cell_therapy", "bispecific_tce", "adc", "checkpoint", "cancer_vaccine",
    "oncolytic_virus", "cytokine_innate", "antibody_other",
    "targeted_ras_mapk", "targeted_kinase", "targeted_ddr", "degrader", "epigenetic",
    "targeted_heme", "endocrine", "rna_gene_therapy", "radiopharm", "radiotherapy",
    "chemo_conventional", "transplant", "nanomedicine_delivery", "physical_ablative",
    "microbiome", "repurposed", "tme_metabolic", "other_therapy",
]
# Generic categories only win when nothing specific matched in the title.
GENERIC = {"tme_metabolic", "nanomedicine_delivery", "chemo_conventional",
           "targeted_heme", "antibody_other", "radiotherapy", "physical_ablative",
           "repurposed", "targeted_kinase"}

# ---------------------------------------------------------------- disease tags
DISEASE = {
    "heme_leukemia": r"\b(leuk?a?emi\w+|(?-i:\bAML\b|\bALL\b|\bCLL\b|\bCML\b|\bMDS\b)|myelodysplas\w+|"
        r"myeloproliferative|myelofibrosis|polycythemia|B-ALL|T-ALL|blast crisis)",
    "heme_lymphoma": r"\b(lymphom\w+|\bDLBCL\b|\bNHL\b|Hodgkin|follicular|mantle cell|"
        r"\bMCL\b|marginal zone|Burkitt|T-cell lymphoma|\bPTCL\b|\bCTCL\b|mycosis fungoides|"
        r"Waldenstr[öo]m|primary CNS lymphoma|\bPCNSL\b)",
    "heme_myeloma": r"\b(myelom\w+|(?-i:\bMM\b)|plasma cell|amyloidosis|plasmacytoma|"
        r"smoldering|smouldering)",
    "breast": r"\b(breast|\bTNBC\b|triple-negative|HER2-positive|HER2-low|HR-positive|"
        r"hormone receptor-positive|luminal)",
    "lung": r"\b(lung|\bNSCLC\b|\bSCLC\b|small[- ]cell|non-small[- ]cell|mesotheliom\w+|"
        r"\bMPM\b|thymic|thymoma|pulmonary)",
    "gi": r"\b(colorectal|\bCRC\b|colon|rectal|rectum|gastric|stomach|gastroesophageal|"
        r"gastro-oesophageal|\bGEJ\b|esophag\w+|oesophag\w+|pancrea\w+|\bPDAC\b|"
        r"hepatocellular|\bHCC\b|liver cancer|biliary|cholangiocarcinom\w+|gallbladder|"
        r"\bGIST\b|gastrointestinal stromal|anal (cancer|carcinoma|canal)|small bowel|appendiceal|neuroendocrine|"
        r"(?-i:\bNETs?\b|\bNEC\b)|peritoneal|MSI-H|mismatch repair|dMMR)",
    "gu": r"\b(prostat\w+|\bmCRPC\b|\bCRPC\b|\bmHSPC\b|bladder|urothelial|\bNMIBC\b|"
        r"\bMIBC\b|renal cell|\bRCC\b|kidney cancer|testicular|germ cell|penile|"
        r"upper tract|urothelial)",
    "gyn": r"\b(ovarian|\bHGSOC\b|fallopian|cervical|cervix|endometrial|uterine|"
        r"vulvar|gynecolog\w+|gynaecolog\w+|gestational trophoblastic)",
    "cns": r"\b(glioma\w*|glioblastom\w+|\bGBM\b|astrocytom\w+|oligodendrogliom\w+|"
        r"diffuse midline glioma|\bDMG\b|\bDIPG\b|pontine|H3 ?K27M|H3\.3 ?G34|H3G34|"
        r"diffuse hemispheric|medulloblastom\w+|ependymom\w+|\bATRT\b|atypical teratoid|"
        r"brain (tumou?r|metasta\w+|cancer)|intracranial|leptomening\w+|\bCNS\b|"
        r"central nervous system|meningiom\w+|craniopharyngiom\w+|pituitary|"
        r"neuro-?oncolog\w+|spinal cord|IDH-mutant)",
    "pediatric": r"\b(p(a)?ediatric|childhood|children|child\b|infants?|adolescents?|"
        r"young adults?|\bAYA\b|neuroblastom\w+|Wilms|retinoblastom\w+|hepatoblastom\w+|"
        r"Ewing|rhabdomyosarcom\w+|osteosarcom\w+|\bDIPG\b|medulloblastom\w+|"
        r"juvenile|Langerhans|pediatric low-grade)",
    "melanoma_skin": r"\b(melanom\w+|uveal|cutaneous squamous|basal cell|Merkel|"
        r"skin cancer|non-melanoma skin)",
    "sarcoma": r"\b(sarcom\w+|\bGIST\b|osteosarcom\w+|Ewing|rhabdomyosarcom\w+|"
        r"leiomyosarcom\w+|liposarcom\w+|synovial|desmoid|chordom\w+|\bDSRCT\b|"
        r"soft[- ]tissue|bone (tumou?r|cancer)|tenosynovial giant cell)",
    "head_neck": r"\b(head and neck|\bHNSCC\b|\bSCCHN\b|oropharyn\w+|nasopharyn\w+|\bNPC\b|"
        r"laryn\w+|oral (cancer|squamous|cavity)|salivary|thyroid|\bATC\b|\bDTC\b|"
        r"medullary thyroid|adenoid cystic)",
    "pan_tumor": r"\b(solid tumou?rs?|advanced (solid )?(cancers?|malignanc\w+)|"
        r"pan-cancer|pan-tumou?r|tumou?r-agnostic|tissue-agnostic|multiple (tumou?r|cancer) types|"
        r"various (tumou?r|cancer) types|refractory (solid )?tumou?rs?|metastatic (cancer|"
        r"solid))",
}
DISEASE_RE = {k: re.compile(v + r"\b", re.I) for k, v in DISEASE.items()}

# ---------------------------------------------------------------- journal tiers
TIER1 = re.compile(
    r"^(N(ew)? Engl(and)? J(ournal of)? Med(icine)?|(The )?Lancet|(The )?Lancet\. Oncology|"
    r"(The )?Lancet Oncol(ogy)?|J(ournal of)? Clin(ical)? Oncol(ogy)?|JAMA Oncol(ogy)?|"
    r"JAMA|BMJ|Ann(als of)? Oncol(ogy)?|Nat(ure)? Med(icine)?|Nature|Science|Cell|"
    r"Cancer Cell|Cancer Discov(ery)?|Nat(ure)? Cancer|Nat(ure)? Biotechnol(ogy)?|"
    r"Sci(ence)? Transl(ational)? Med(icine)?|Immunity|Blood|Nat(ure)? Rev(iews)? "
    r"Clin(ical)? Oncol(ogy)?|(The )?Lancet\. Haematology|(The )?Lancet Haematol(ogy)?|"
    r"Nat(ure)? Immunol(ogy)?)\.?$", re.I)
TIER2 = re.compile(
    r"^(Nat(ure)? Commun(ications)?|J(ournal for)? Immunother(apy of)? Cancer|"
    r"Clin(ical)? Cancer Res(earch)?|Cancer Res(earch)?|J(ournal of)? Hematol(ogy)? "
    r"(&|and) Oncol(ogy)?|Mol(ecular)? Cancer|J(ournal of)? Clin(ical)? Invest(igation)?|"
    r"Proc(eedings of the)? Natl?(ional)? Acad(emy of)? Sci(ences)?( of the United States of "
    r"America)?( U S A)?|Cell Rep(orts)? Med(icine)?|Leukemia|Blood Cancer J(ournal)?|"
    r"Eur(opean)? J(ournal of)? Cancer|J(ournal of)? Thorac(ic)? Oncol(ogy)?|"
    r"Eur(opean)? Urol(ogy)?|Neuro-?Oncol(ogy)?|Sci(ence)? Adv(ances)?|Nat(ure)? Chem(ical)? "
    r"Biol(ogy)?|J(ournal of)? Exp(erimental)? Med(icine)?|Mol(ecular)? Ther(apy)?|"
    r"Signal Transduct(ion and)? Target(ed)? Ther(apy)?|Cancer Immunol(ogy)? Res(earch)?|"
    r"Haematologica|Br(itish)? J(ournal of)? Cancer|Cancer|ESMO Open|Lancet Reg(ional)? "
    r"Health.*|Adv(anced)? Mater(ials)?|ACS Nano|Adv(anced)? Sci(ence)?( \(Weinh\))?|"
    r"Nat(ure)? Nanotechnol(ogy)?|J(ournal of)? Med(icinal)? Chem(istry)?|Cell Metab(olism)?|"
    r"Nat(ure)? Genet(ics)?|Nat(ure)? Cell Biol(ogy)?|Genome Med(icine)?|EMBO Mol(ecular)? "
    r"Med(icine)?|Cancer Lett(ers)?|Oncogene|Mol(ecular)? Cancer Ther(apeutics)?|"
    r"J(ournal of)? Control(led)? Release|Biomaterials|Int(ernational)? J(ournal of)? "
    r"Radiat(ion)? Oncol(ogy,?)? Biol(ogy,?)? Phys(ics)?|Gynecol(ogic)? Oncol(ogy)?|"
    r"Radiother(apy and)? Oncol(ogy)?|J(ournal of)?( the)? Natl?(ional)? Cancer Inst(itute)?|"
    r"Nat(ure)? Rev(iews)?.*|Am(erican)? J(ournal of)? Hematol(ogy)?|"
    r"Lancet Digit(al)? Health|Lancet Glob(al)? Health|Lancet Respir(atory)? Med(icine)?|"
    r"Lancet Gastroenterol(ogy)? Hepatol(ogy)?|Hepatology|Gut|Gastroenterology|"
    r"J(ournal of)? Hepatol(ogy)?|Eur(opean)? Heart J(ournal)?|Ann(als of)? Intern(al)? "
    r"Med(icine)?|Cell Stem Cell|Cell Chem(ical)? Biol(ogy)?|Med|Nat(ure)? Aging|"
    r"Nat(ure)? Metab(olism)?|Cancer Immunol(ogy,)? Immunother(apy)?|Oncoimmunology|"
    r"Theranostics|Adv(anced)? Drug Deliv(ery)? Rev(iews)?|Nano Today|Small|"
    r"Nano Lett(ers)?|Angew(andte)? Chem(ie)?.*|J(ournal of the)? Am(erican)? Chem(ical)? "
    r"Soc(iety)?|Chem|Nat(ure)? Chem(istry)?|Nat(ure)? Mater(ials)?|Nat(ure)? Biomed(ical)? "
    r"Eng(ineering)?|Sci(ence)? Immunol(ogy)?|Cell Res(earch)?|Nucleic Acids Res(earch)?|"
    r"eLife|PLoS Med(icine)?|Nat(ure)? Struct(ural)? (&|and) Mol(ecular)? Biol(ogy)?|"
    r"Dev(elopmental)? Cell|Cancer Treat(ment)? Rev(iews)?|Leukemia (&|and) Lymphoma|"
    r"Br(itish)? J(ournal of)? Haematol(ogy)?|Bone Marrow Transplant(ation)?|"
    r"Transplant(ation and)? Cell(ular)? Ther(apy)?|J(ournal of)? Neurooncol(ogy)?|"
    r"Neuro Oncol(ogy)?|Acta Neuropathol(ogica)?|Pediatr(ic)? Blood (&|and) Cancer|"
    r"J(ournal of)? Pediatr(ic)? Hematol(ogy)?/Oncol(ogy)?|J(ournal of)? Urol(ogy)?|"
    r"Eur(opean)? Urol(ogy)? Oncol(ogy)?|Prostate Cancer Prostatic Dis(eases)?|"
    r"Breast Cancer Res(earch)?|NPJ Breast Cancer|NPJ Precis(ion)? Oncol(ogy)?|"
    r"Nat(ure)? Rev(iews)? Cancer|Nat(ure)? Rev(iews)? Drug Discov(ery)?)\.?$", re.I)


def score(text, patterns):
    hits = {}
    for name, pat in patterns.items():
        n = len(pat.findall(text))
        if n:
            hits[name] = n
    return hits


def evidence_level(title, text, pubtype):
    if PUBTYPE_SR.search(pubtype) or SR_MA.search(title):
        return "evidence_synthesis"
    t = title + " " + text[:1500]
    if MEDCHEM_TITLE.search(title) and not STRONG_CLIN.search(text):
        return "preclinical"
    clin = bool(CLINICAL.search(text))
    # explicit phase in the title wins; a randomised phase 2 stays phase 2
    if EXPLICIT3.search(title) or ("Phase III" in pubtype):
        return "clinical_phase3"
    if PHASE2.search(title) or ("Phase II" in pubtype):
        return "clinical_phase2"
    if PHASE1.search(title) or ("Phase I" in pubtype):
        return "clinical_phase1"
    if PHASE3.search(title) or ("Randomized Controlled Trial" in pubtype):
        return "clinical_phase3"
    if PHASE3.search(text) and clin and STRONG_CLIN.search(text) and not INVIVO.search(title):
        # abstract-level randomisation vocabulary with clinical evidence
        if re.search(r"\b(phase (3|III|2/3)|randomi[sz]ed)\b", text, re.I) and \
                re.search(r"\b(patients|participants|women|men)\b", text, re.I) and \
                not re.search(r"\b(mice|mouse|murine|xenograft)\b", text, re.I):
            return "clinical_phase3"
    strong = bool(STRONG_CLIN.search(text))
    if clin and not MODEL_ONLY.search(text):
        if strong and PHASE2.search(t):
            return "clinical_phase2"
        if strong and PHASE1.search(t):
            return "clinical_phase1"
        return "clinical_other"
    if PRECLINICAL.search(text):
        # a paper describing treated patients that also has model work is clinical
        if strong and re.search(r"\b(phase (1|2|3|I|II|III)\b|first[- ]in[- ]human|NCT0?\d{7}|"
                                r"\d+ patients (were|received|underwent|treated|enrolled)|"
                                r"objective response rate|median (progression-free|overall) survival)",
                                text, re.I):
            if PHASE2.search(t):
                return "clinical_phase2"
            if PHASE1.search(t):
                return "clinical_phase1"
            return "clinical_other"
        return "preclinical"
    if clin:
        return "clinical_other"
    return None


def classify_modality(title, abstract, domain):
    th = score(title, MODALITY_RE)
    ah = score(abstract, MODALITY_RE)
    cats = set(th) | set(ah)
    if not cats:
        return "other_therapy", th, ah
    dom_cat = DOMAIN_TO_CATEGORY.get(domain)

    def key(c):
        s = 4 * th.get(c, 0) + ah.get(c, 0)
        if c == dom_cat:
            s += 2
        if c in GENERIC and c not in th:
            s -= 3
        if c in GENERIC:
            s -= 1
        return (-s, CATEGORY_ORDER.index(c))

    ranked = sorted(cats, key=key)
    best = ranked[0]
    # specific title match beats generic abstract chatter
    specific_title = [c for c in th if c not in GENERIC]
    if specific_title and best in GENERIC:
        best = sorted(specific_title, key=key)[0]
    return best, th, ah


def tier_of(venue):
    # Europe PMC venue strings carry suffixes ("... : official journal of ...",
    # "Lancet (London, England)") and a leading "The"; strip them before matching.
    v = re.sub(r"\s*[:(].*$", "", (venue or "").strip())
    v = re.sub(r"^The\s+", "", v, flags=re.I).strip()
    if TIER1.match(v):
        return 1
    if TIER2.match(v):
        return 2
    return 3


def main():
    with open(f"{BASE}/raw_harvest.json") as f:
        records = json.load(f)

    kept = []
    dropped = Counter()
    for rec in records:
        title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html.unescape(rec["title"]))).strip()
        abstract = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html.unescape(rec.get("abstract", "")))).strip()
        rec["title"], rec["abstract"] = title, abstract
        pubtype = rec.get("pubType", "") or ""
        if not title or len(title) < 15:
            dropped["no_title"] += 1
            continue
        if not abstract or len(abstract) < 200:
            dropped["no_abstract"] += 1
            continue
        text = f"{title} {abstract}"
        if EXCLUDE_TITLE.search(title):
            dropped["excluded_title"] += 1
            continue
        if PUBTYPE_EXCLUDE.search(pubtype) and not PUBTYPE_SR.search(pubtype) \
                and not re.search(r"Clinical Trial|Randomized", pubtype):
            dropped["excluded_pubtype"] += 1
            continue
        date = rec.get("date", "") or ""
        if not ("2026-03-09" <= date <= "2026-09-09"):
            dropped["out_of_window"] += 1
            continue
        if not (CANCER.search(title) or len(CANCER.findall(abstract)) >= 3):
            dropped["no_cancer"] += 1
            continue
        title_therapy = bool(THERAPY.search(title))
        if not title_therapy and len(THERAPY.findall(abstract)) < 4:
            dropped["no_therapy"] += 1
            continue
        evidence = evidence_level(title, text, pubtype)
        if evidence is None:
            dropped["no_evidence"] += 1
            continue
        # observational / synthesis records must name the intervention in the title;
        # otherwise they are almost always prognostic or descriptive studies
        if evidence in ("clinical_other", "evidence_synthesis") and not title_therapy:
            dropped["observational_no_title_therapy"] += 1
            continue
        # preclinical papers with no treated model at all (pure descriptive biology)
        if evidence == "preclinical":
            if not (INVIVO.search(text) or re.search(
                    r"\b(inhibitor|antibod\w+|CAR[- ]?T|vaccine|conjugate|degrader|"
                    r"nanoparticle\w*|treat(ed|ment)|therap\w+|cytotoxic\w*|IC50|"
                    r"compound|drug|agent)\b", text, re.I)):
                dropped["preclinical_no_treatment"] += 1
                continue

        category, th, ah = classify_modality(title, abstract, rec.get("domain", ""))
        if category == "other_therapy" and (
                not title_therapy or evidence in ("clinical_other", "evidence_synthesis")):
            dropped["other_no_title_therapy"] += 1
            continue
        if (category == "other_therapy" and evidence != "preclinical"
                and not SPECIFIC_THERAPY.search(title)):
            dropped["other_no_specific_agent"] += 1
            continue
        dhits = score(text, DISEASE_RE)
        topics = sorted(dhits)
        # secondary modalities present in the title
        for c in th:
            if c != category:
                topics.append(f"also:{c}")
        if rec.get("src") == "PPR" or "Preprint" in pubtype:
            topics.append("preprint")
        if INVIVO.search(text) and evidence == "preclinical":
            topics.append("in_vivo")
        if re.search(r"\b(combination|combined with|plus|in combination)\b", title, re.I):
            topics.append("combination")
        if re.search(r"\b(resistan\w+)\b", title, re.I):
            topics.append("resistance")
        if re.search(r"\b(safety|toxicit\w+|adverse event|tolerability)\b", title, re.I):
            topics.append("safety")
        if re.search(r"\b(neoadjuvant|perioperative|adjuvant)\b", title, re.I):
            topics.append("perioperative")
        if re.search(r"\b(first[- ]line|frontline|front-line|newly diagnosed|previously untreated|treatment-naive)\b", title, re.I):
            topics.append("first_line")
        if re.search(r"\b(relapsed|refractory|pretreated|previously treated|second[- ]line|later[- ]line)\b", title, re.I):
            topics.append("relapsed_refractory")

        tier = tier_of(rec.get("venue", ""))
        ev_w = {"clinical_phase3": 6, "clinical_phase2": 4, "clinical_phase1": 4,
                "evidence_synthesis": 2, "clinical_other": 1, "preclinical": 2}[evidence]
        priority = ev_w + {1: 8, 2: 4, 3: 0}[tier] + min(int(rec.get("cited") or 0), 10)
        if "preprint" in topics:
            priority -= 2
        if evidence == "clinical_other" and tier == 3:
            priority -= 1

        rec.update({
            "category": category, "evidence": evidence, "topics": ";".join(topics),
            "tier": tier, "priority": priority,
        })
        kept.append(rec)

    # dedupe on normalised title (preprint + journal version; duplicate indexing)
    by_title = {}
    for rec in kept:
        k = re.sub(r"[^a-z0-9]", "", rec["title"].lower())[:100]
        prev = by_title.get(k)
        if prev is None:
            by_title[k] = rec
        elif (rec.get("pmid") and not prev.get("pmid")) or \
                (rec.get("src") == "MED" and prev.get("src") == "PPR"):
            by_title[k] = rec
    kept = list(by_title.values())
    # same DOI indexed twice (online-first vs issue version with retitled characters)
    by_doi = {}
    for rec in kept:
        k = (rec.get("doi") or "").lower()
        if not k:
            by_doi[id(rec)] = rec
        elif k not in by_doi or rec.get("date", "") < by_doi[k].get("date", ""):
            by_doi[k] = rec
    kept = list(by_doi.values())

    EV_ORDER = ["clinical_phase3", "clinical_phase2", "clinical_phase1", "clinical_other",
                "evidence_synthesis", "preclinical"]
    kept.sort(key=lambda r: (CATEGORY_ORDER.index(r["category"]), EV_ORDER.index(r["evidence"]),
                             -r["priority"], r.get("date", ""), r["authors"][:20]))

    cols = ["category", "evidence", "tier", "authors", "title", "venue", "date", "year",
            "pmid", "doi", "pmcid", "url", "fulltext_xml", "topics", "status"]
    with open(f"{BASE}/index.tsv", "w") as f:
        f.write("\t".join(cols) + "\n")
        for r in kept:
            if r.get("pmcid"):
                url = f"https://pmc.ncbi.nlm.nih.gov/articles/{r['pmcid']}/"
            elif r.get("doi"):
                url = f"https://doi.org/{r['doi']}"
            elif r.get("pmid"):
                url = f"https://pubmed.ncbi.nlm.nih.gov/{r['pmid']}/"
            else:
                url = ""
            row = [r["category"], r["evidence"], str(r["tier"]), r["authors"], r["title"],
                   r["venue"], r.get("date", ""), r["year"], r.get("pmid", ""),
                   r.get("doi", ""), r.get("pmcid", ""), url, "", r["topics"], "metadata_only"]
            f.write("\t".join(c.replace("\t", " ").replace("\n", " ") for c in row) + "\n")

    slim = [{k: r[k] for k in ("category", "evidence", "tier", "priority", "authors", "title",
                               "venue", "date", "pmid", "doi", "pmcid", "topics", "abstract",
                               "cited", "src", "domain")} for r in kept]
    with open(f"{BASE}/curated.json", "w") as f:
        json.dump(slim, f, indent=0)

    print(f"kept {len(kept)} of {len(records)}")
    print("dropped:", dict(dropped))
    for c, n in Counter(r["category"] for r in kept).most_common():
        print(f"  {c}: {n}")
    print("evidence:", Counter(r["evidence"] for r in kept))
    print("tier:", Counter(r["tier"] for r in kept))


if __name__ == "__main__":
    main()
