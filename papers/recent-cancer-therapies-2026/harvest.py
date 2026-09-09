#!/usr/bin/env python3
"""Harvest cancer-therapy literature published in the last six months (2026-03-09 to
2026-09-09), clinical and preclinical, across every major therapeutic modality.

Europe PMC REST search, restricted to PubMed / PMC / preprint sources and to the
publication-date window via FIRST_PDATE. Query groups are therapeutic modalities plus
three modality-agnostic sweeps (clinical-trial vocabulary, preclinical-model vocabulary,
and high-impact journals) so that important papers are caught even when their title and
abstract do not name a modality keyword. Records are serialized to raw_harvest.json for
downstream scoring/classification by curate.py.
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
OUT = "/home/ubuntu/repos/lit-syn/papers/recent-cancer-therapies-2026/raw_harvest.json"
LOG = "/home/ubuntu/repos/lit-syn/papers/recent-cancer-therapies-2026/harvest.log"

DATE_FROM = "2026-03-09"
DATE_TO = "2026-09-09"
WINDOW = f'FIRST_PDATE:[{DATE_FROM} TO {DATE_TO}] AND (SRC:MED OR SRC:PMC OR SRC:PPR)'

CANCER = ('(cancer OR cancers OR tumor OR tumour OR tumors OR tumours OR carcinoma OR '
          'adenocarcinoma OR leukemia OR leukaemia OR lymphoma OR myeloma OR sarcoma OR '
          'glioma OR glioblastoma OR melanoma OR neoplasm OR malignancy OR malignancies OR '
          'oncology OR neuroblastoma OR mesothelioma)')
TRIAL = ('("phase 1" OR "phase I" OR "phase 2" OR "phase II" OR "phase 3" OR "phase III" OR '
         '"phase 1/2" OR "phase 2/3" OR randomized OR randomised OR "first-in-human" OR '
         '"clinical trial" OR "single-arm" OR "open-label" OR "dose-escalation" OR '
         '"dose escalation" OR "real-world" OR "retrospective" OR "prospective")')
INVIVO = ('(mice OR mouse OR murine OR xenograft OR "patient-derived xenograft" OR PDX OR '
          'syngeneic OR orthotopic OR "in vivo" OR "mouse model" OR organoid OR "non-human primate")')

QUERIES = {
    # ------------------------------------------------ adoptive cell therapy
    "cell_therapy": [
        f'("CAR T" OR "CAR-T" OR "CAR T-cell" OR "CAR T cell" OR "chimeric antigen receptor") AND {CANCER}',
        f'("CAR NK" OR "CAR-NK" OR "CAR macrophage" OR "CAR-M" OR "CAR-macrophage" OR "CAR NKT" OR "CAR-NKT" OR "CAR Treg") AND {CANCER}',
        f'("TCR-T" OR "TCR-engineered" OR "T-cell receptor therapy" OR "TCR therapy" OR afamitresgene OR "tumor-infiltrating lymphocyte" OR "tumour-infiltrating lymphocyte" OR "TIL therapy" OR lifileucel OR "adoptive cell therapy" OR "adoptive cell transfer" OR "adoptive T cell") AND {CANCER}',
        f'("gamma delta T" OR "γδ T" OR "gammadelta T" OR "Vδ1" OR "Vδ2" OR "Vγ9Vδ2" OR "NK cell therapy" OR "natural killer cell therapy" OR "iPSC-derived NK" OR "iNK cell" OR "cytokine-induced killer" OR "NKT cell therapy" OR "invariant NKT") AND {CANCER} AND (therapy OR treatment OR "adoptive")',
        f'("in vivo CAR" OR "in situ CAR" OR "in vivo CAR-T" OR "in vivo generation of CAR" OR "lentiviral in vivo" OR ("targeted lipid nanoparticle" AND "T cell")) AND {CANCER}',
        f'("allogeneic CAR" OR "off-the-shelf CAR" OR "universal CAR" OR "armored CAR" OR "armoured CAR" OR "logic-gated CAR" OR "synthetic notch" OR synNotch OR "CAR exhaustion" OR "CAR T persistence") AND {CANCER}',
        '("chimeric antigen receptor" OR "CAR T") AND ("solid tumor" OR "solid tumour" OR glioma OR glioblastoma OR "diffuse midline glioma" OR neuroblastoma OR sarcoma OR mesothelioma OR "pancreatic" OR "ovarian" OR "hepatocellular" OR "gastric")',
        '("CAR T" OR "chimeric antigen receptor") AND (lupus OR autoimmune) AND (cancer OR lymphoma OR B-cell)',
    ],
    # ------------------------------------------------ bispecifics / T-cell engagers
    "bispecific_tce": [
        f'("bispecific antibody" OR "bispecific antibodies" OR bispecific OR "T-cell engager" OR "T cell engager" OR "T-cell-engaging" OR BiTE OR trispecific OR "tri-specific" OR "multispecific antibody") AND {CANCER}',
        f'(blinatumomab OR teclistamab OR talquetamab OR elranatamab OR linvoseltamab OR glofitamab OR epcoritamab OR mosunetuzumab OR odronextamab OR tarlatamab OR tebentafusp OR "ImmTAC" OR brenetafusp OR xaluritamig OR "AMG 193" OR obexelimab) AND {CANCER}',
        f'(ivonescimab OR cadonilimab OR amivantamab OR zanidatamab OR zenocutuzumab OR "PD-1/VEGF" OR "PD-1 x VEGF" OR "PD-L1/4-1BB" OR acasunlimab OR volrustomig OR rilvegostomig OR "PD-1/CTLA-4" OR "PD-1/TIGIT") AND {CANCER}',
    ],
    # ------------------------------------------------ antibody-drug conjugates
    "adc": [
        f'("antibody-drug conjugate" OR "antibody drug conjugate" OR "antibody-drug conjugates" OR "ADC" OR "immunoconjugate" OR "bispecific ADC" OR "radioconjugate" OR "peptide-drug conjugate") AND {CANCER}',
        f'("trastuzumab deruxtecan" OR "T-DXd" OR "sacituzumab govitecan" OR "datopotamab deruxtecan" OR "Dato-DXd" OR "enfortumab vedotin" OR "tisotumab vedotin" OR "mirvetuximab soravtansine" OR "telisotuzumab vedotin" OR "patritumab deruxtecan" OR "ifinatamab deruxtecan" OR "sacituzumab tirumotecan" OR "raludotatug deruxtecan" OR "trastuzumab emtansine" OR "brentuximab vedotin" OR "polatuzumab vedotin" OR "loncastuximab tesirine" OR "inotuzumab ozogamicin" OR "gemtuzumab ozogamicin" OR "disitamab vedotin" OR "zilovertamab vedotin" OR "sigvotatug vedotin" OR "emiltatug ledadotin" OR "puxitatug samrotecan" OR "trastuzumab rezetecan" OR deruxtecan OR vedotin OR govitecan OR "-tecan" OR rezetecan) AND {CANCER}',
    ],
    # ------------------------------------------------ immune checkpoint blockade
    "checkpoint": [
        f'("immune checkpoint inhibitor" OR "immune checkpoint inhibitors" OR "immune checkpoint blockade" OR "checkpoint inhibitor" OR "anti-PD-1" OR "anti-PD-L1" OR "PD-1 blockade" OR "PD-L1 blockade") AND {CANCER} AND {TRIAL}',
        f'("immune checkpoint inhibitor" OR "immune checkpoint blockade" OR "anti-PD-1" OR "anti-PD-L1" OR "PD-1 blockade" OR "PD-L1 blockade" OR "PD-1 antibody") AND {CANCER} AND {INVIVO}',
        f'(pembrolizumab OR nivolumab OR atezolizumab OR durvalumab OR ipilimumab OR cemiplimab OR avelumab OR tislelizumab OR toripalimab OR sintilimab OR camrelizumab OR serplulimab OR penpulimab OR dostarlimab OR retifanlimab OR tremelimumab OR relatlimab OR fianlimab OR "subcutaneous nivolumab" OR "subcutaneous pembrolizumab") AND {CANCER}',
        f'("LAG-3" OR "TIGIT" OR "TIM-3" OR "VISTA" OR "NKG2A" OR monalizumab OR tiragolumab OR domvanalimab OR vibostolimab OR "CD47" OR magrolimab OR "SIRPα" OR "B7-H3" OR "B7-H4" OR "CD73" OR "adenosine A2A" OR "CCR8" OR "ILT4" OR "LILRB" OR "PVRIG" OR "CD96" OR "novel immune checkpoint") AND {CANCER} AND (therapy OR blockade OR antibody OR inhibitor)',
        f'("neoadjuvant immunotherapy" OR "perioperative immunotherapy" OR "neoadjuvant chemoimmunotherapy" OR "perioperative" OR "adjuvant immunotherapy") AND {CANCER} AND (PD-1 OR PD-L1 OR nivolumab OR pembrolizumab OR durvalumab OR atezolizumab OR toripalimab OR tislelizumab)',
        f'("immunotherapy resistance" OR "resistance to immune checkpoint" OR "primary resistance" OR "acquired resistance") AND (PD-1 OR PD-L1 OR "checkpoint") AND {CANCER} AND {INVIVO}',
        f'("immune-related adverse event" OR "immune-related adverse events" OR irAE OR "checkpoint inhibitor toxicity" OR "checkpoint inhibitor colitis" OR "checkpoint inhibitor myocarditis" OR "immune checkpoint inhibitor-associated") AND {CANCER}',
    ],
    # ------------------------------------------------ cancer vaccines
    "cancer_vaccine": [
        f'("cancer vaccine" OR "cancer vaccines" OR "tumor vaccine" OR "tumour vaccine" OR "neoantigen vaccine" OR "personalized vaccine" OR "personalised vaccine" OR "individualized neoantigen" OR "individualised neoantigen" OR "mRNA vaccine" OR "mRNA-4157" OR "V940" OR intismeran OR "autogene cevumeran" OR "BNT122" OR "dendritic cell vaccine" OR "peptide vaccine" OR "DNA vaccine" OR "in situ vaccination" OR "in situ vaccine" OR "therapeutic vaccine" OR "tumor lysate vaccine" OR "whole-cell vaccine" OR "neoantigen" OR "shared antigen vaccine" OR "KRAS vaccine" OR "ELI-002") AND {CANCER}',
    ],
    # ------------------------------------------------ oncolytic viruses
    "oncolytic_virus": [
        f'("oncolytic virus" OR "oncolytic viruses" OR oncolytic OR "oncolytic virotherapy" OR virotherapy OR "talimogene laherparepvec" OR "T-VEC" OR "RP1" OR vusolimogene OR "oncolytic adenovirus" OR "oncolytic herpes" OR "oncolytic HSV" OR "oncolytic vaccinia" OR "oncolytic reovirus" OR pelareorep OR "oncolytic measles" OR "oncolytic vesicular stomatitis" OR "oncolytic Newcastle" OR "nadofaragene" OR "cretostimogene" OR "CG0070" OR "Delta-24" OR DNX-2401 OR teserpaturev OR "olvimulogene" OR "oncolytic bacteria" OR "bacterial cancer therapy" OR "engineered bacteria" OR ("Salmonella typhimurium" AND tumor)) AND {CANCER}',
    ],
    # ------------------------------------------------ targeted small molecules — RAS/RAF/MAPK
    "targeted_ras_mapk": [
        f'("KRAS G12C" OR "KRAS G12D" OR "KRAS G12V" OR "KRAS inhibitor" OR "KRAS-mutant" OR "KRAS mutant" OR "pan-RAS" OR "pan-KRAS" OR "RAS(ON)" OR "RAS inhibitor" OR sotorasib OR adagrasib OR divarasib OR olomorasib OR glecirasib OR garsorasib OR fulzerasib OR "MRTX1133" OR zoldonrasib OR daraxonrasib OR elironrasib OR "RMC-6236" OR "RMC-6291" OR "RMC-9805" OR "SHP2 inhibitor" OR "SOS1 inhibitor") AND {CANCER}',
        f'("BRAF inhibitor" OR "BRAF V600" OR "MEK inhibitor" OR "ERK inhibitor" OR dabrafenib OR trametinib OR encorafenib OR binimetinib OR vemurafenib OR cobimetinib OR tovorafenib OR "pan-RAF" OR "RAF inhibitor" OR naporafenib OR avutometinib OR defactinib OR mirdametinib OR selumetinib) AND {CANCER}',
    ],
    # ------------------------------------------------ targeted small molecules — kinase inhibitors
    "targeted_kinase": [
        f'("tyrosine kinase inhibitor" OR "tyrosine kinase inhibitors" OR "TKI" OR osimertinib OR lazertinib OR furmonertinib OR aumolertinib OR befotertinib OR sunvozertinib OR zipalertinib OR "EGFR exon 20" OR "EGFR-mutant" OR "EGFR mutant" OR "EGFR mutation" OR "EGFR inhibitor" OR "fourth-generation EGFR" OR "HER2-mutant" OR zongertinib OR "BAY 2927088" OR sevabertinib OR neratinib OR tucatinib OR pyrotinib OR lapatinib) AND {CANCER}',
        f'("ALK inhibitor" OR "ALK-positive" OR alectinib OR lorlatinib OR brigatinib OR ensartinib OR iruplinalkib OR "ROS1" OR repotrectinib OR taletrectinib OR entrectinib OR crizotinib OR "RET inhibitor" OR "RET fusion" OR selpercatinib OR pralsetinib OR "MET inhibitor" OR "MET exon 14" OR "MET amplification" OR capmatinib OR tepotinib OR savolitinib OR "NTRK" OR larotrectinib OR "FGFR inhibitor" OR "FGFR2" OR erdafitinib OR pemigatinib OR futibatinib OR lirafugratinib OR "HER3") AND {CANCER}',
        f'("PI3K inhibitor" OR "PIK3CA" OR "AKT inhibitor" OR "mTOR inhibitor" OR capivasertib OR inavolisib OR alpelisib OR ipatasertib OR gedatolisib OR "RLY-2608" OR everolimus OR ("PTEN" AND inhibitor)) AND {CANCER} AND (therapy OR treatment OR inhibitor)',
        f'("CDK4/6 inhibitor" OR "CDK4/6" OR palbociclib OR ribociclib OR abemaciclib OR dalpiciclib OR atirmociclib OR "CDK4 inhibitor" OR "CDK2 inhibitor" OR "CDK7 inhibitor" OR "CDK9 inhibitor" OR "CDK12" OR "Aurora kinase" OR alisertib OR "PLK1" OR "WEE1 inhibitor" OR adavosertib OR azenosertib OR "ATR inhibitor" OR ceralasertib OR camonsertib OR "CHK1 inhibitor" OR "PKMYT1" OR lunresertib OR "DNA-PK inhibitor") AND {CANCER}',
        f'("multikinase inhibitor" OR lenvatinib OR sorafenib OR regorafenib OR cabozantinib OR axitinib OR sunitinib OR pazopanib OR anlotinib OR apatinib OR fruquintinib OR surufatinib OR "VEGFR inhibitor" OR "VEGFR-2" OR "anti-angiogenic" OR antiangiogenic OR bevacizumab OR ramucirumab OR "HIF-2α" OR belzutifan OR "HIF-2 alpha") AND {CANCER} AND {TRIAL}',
        f'("BTK inhibitor" OR ibrutinib OR acalabrutinib OR zanubrutinib OR pirtobrutinib OR nemtabrutinib OR "BTK degrader" OR "BCL-2 inhibitor" OR "BCL2 inhibitor" OR venetoclax OR sonrotoclax OR lisaftoclax OR "MCL-1 inhibitor" OR "MCL1" OR "FLT3 inhibitor" OR gilteritinib OR quizartinib OR midostaurin OR "JAK inhibitor" OR ruxolitinib OR momelotinib OR fedratinib OR pacritinib OR "JAK2" OR "XPO1" OR selinexor OR "IRAK4" OR emavusertib OR "SYK inhibitor" OR "PI3Kδ") AND {CANCER}',
    ],
    # ------------------------------------------------ DNA damage response / synthetic lethality
    "targeted_ddr": [
        f'("PARP inhibitor" OR "PARP inhibitors" OR olaparib OR niraparib OR rucaparib OR talazoparib OR saruparib OR "AZD5305" OR senaparib OR fuzuloparib OR pamiparib OR "PARP1-selective" OR "PARP1 selective" OR ("homologous recombination deficiency" AND (inhibitor OR therapy)) OR "synthetic lethality" OR "synthetic lethal" OR "POLQ inhibitor" OR "Polθ" OR "WRN inhibitor" OR "WRN helicase" OR "USP1 inhibitor" OR "RAD51 inhibitor" OR "ATM inhibitor") AND {CANCER}',
    ],
    # ------------------------------------------------ hormonal / endocrine
    "endocrine": [
        f'("endocrine therapy" OR "aromatase inhibitor" OR letrozole OR anastrozole OR exemestane OR fulvestrant OR tamoxifen OR "selective estrogen receptor degrader" OR SERD OR elacestrant OR imlunestrant OR camizestrant OR giredestrant OR vepdegestrant OR palazestrant OR "oral SERD" OR "ESR1 mutation" OR "ESR1-mutant" OR "androgen deprivation therapy" OR "androgen receptor pathway inhibitor" OR "androgen receptor inhibitor" OR enzalutamide OR apalutamide OR darolutamide OR abiraterone OR relugolix OR "AR degrader" OR "AR antagonist" OR "castration-resistant" OR "hormone-sensitive prostate") AND {CANCER} AND ({TRIAL} OR {INVIVO})',
    ],
    # ------------------------------------------------ hematology-specific targeted agents
    "targeted_heme": [
        '("menin inhibitor" OR revumenib OR ziftomenib OR bleximenib OR enzomenib OR "KMT2A-rearranged" OR "NPM1-mutant" OR "IDH inhibitor" OR "IDH1" OR "IDH2" OR ivosidenib OR enasidenib OR olutasidenib OR vorasidenib OR "CELMoD" OR iberdomide OR mezigdomide OR "cereblon E3 ligase modulator" OR "proteasome inhibitor" OR bortezomib OR carfilzomib OR ixazomib OR "hypomethylating agent" OR azacitidine OR decitabine OR "oral azacitidine" OR ("TP53-mutant" AND (AML OR MDS)) OR "anti-CD38" OR daratumumab OR isatuximab OR "anti-CD20" OR obinutuzumab OR "anti-CD19" OR tafasitamab OR ("TIM-3" AND sabatolimab) OR "GPRC5D" OR "BCMA" OR "CD123" OR "CD33" OR "CLL-1" OR "CD70" OR ("CD7" AND CAR)) AND (leukemia OR leukaemia OR lymphoma OR myeloma OR myelodysplastic OR "AML" OR "MDS" OR "ALL" OR "CLL" OR "CML" OR myelofibrosis OR "Waldenström")',
        f'("acute myeloid leukemia" OR "acute myeloid leukaemia" OR "acute lymphoblastic leukemia" OR "acute lymphoblastic leukaemia" OR "multiple myeloma" OR "diffuse large B-cell lymphoma" OR "chronic lymphocytic leukemia" OR "mantle cell lymphoma" OR "follicular lymphoma" OR "Hodgkin lymphoma" OR "myelodysplastic" OR myelofibrosis OR "T-cell lymphoma") AND {TRIAL} AND (treatment OR therapy OR regimen)',
    ],
    # ------------------------------------------------ targeted protein degradation
    "degrader": [
        f'(PROTAC OR PROTACs OR "proteolysis-targeting chimera" OR "proteolysis targeting chimera" OR "targeted protein degradation" OR "protein degrader" OR "molecular glue" OR "molecular glue degrader" OR "bifunctional degrader" OR "degrader" OR "BRD9 degrader" OR "IKZF" OR "GSPT1" OR "ARV-471" OR "ARV-110" OR bavdegalutamide OR "NX-5948" OR "BGB-16673" OR "KT-333" OR "STAT3 degrader" OR "STAT5 degrader" OR "AR degrader" OR ("ER degrader" AND PROTAC) OR "hydrophobic tag" OR "LYTAC" OR "AUTAC" OR "molecular glue") AND {CANCER}',
    ],
    # ------------------------------------------------ epigenetic therapy
    "epigenetic": [
        f'("EZH2 inhibitor" OR tazemetostat OR valemetostat OR tulmimetostat OR "EZH1/2" OR "HDAC inhibitor" OR "histone deacetylase inhibitor" OR vorinostat OR panobinostat OR romidepsin OR tucidinostat OR chidamide OR entinostat OR "BET inhibitor" OR "BRD4 inhibitor" OR "bromodomain" OR pelabresib OR "DNMT inhibitor" OR "LSD1 inhibitor" OR bomedemstat OR iadademstat OR "PRMT5 inhibitor" OR "MTA-cooperative" OR "MAT2A inhibitor" OR "DOT1L" OR "KAT6" OR "KAT6A" OR "KAT6 inhibitor" OR "SETD2" OR "KDM" OR "menin-MLL" OR "epigenetic therapy" OR "epigenetic drug" OR "epigenetic inhibitor" OR ("chromatin remodeling" AND inhibitor) OR ("SWI/SNF" AND (inhibitor OR degrader)) OR "SMARCA2 degrader") AND {CANCER}',
        f'(ONC201 OR dordaviprone OR ONC206 OR "imipridone" OR "ClpP agonist" OR ("DRD2 antagonist" AND glioma)) AND {CANCER}',
    ],
    # ------------------------------------------------ radiopharmaceuticals / radiotherapy
    "radiopharm_radiotherapy": [
        f'("radioligand therapy" OR "radioligand" OR radiopharmaceutical OR radiopharmaceuticals OR "177Lu" OR "Lu-177" OR "lutetium-177" OR "lutetium Lu 177" OR "PSMA-617" OR vipivotide OR "PSMA radioligand" OR "225Ac" OR "actinium-225" OR "actinium" OR "targeted alpha therapy" OR "alpha emitter" OR "212Pb" OR "lead-212" OR "radium-223" OR "radioimmunotherapy" OR "peptide receptor radionuclide therapy" OR PRRT OR "DOTATATE" OR "FAP radioligand" OR "FAPI" OR "theranostic" OR theranostics OR "radiolabeled antibody" OR "radiolabelled antibody" OR "boron neutron capture" OR "BNCT") AND {CANCER}',
        f'("stereotactic body radiotherapy" OR "stereotactic body radiation" OR SBRT OR SABR OR "stereotactic radiosurgery" OR "hypofractionated" OR "FLASH radiotherapy" OR "FLASH radiation" OR "proton therapy" OR "proton beam" OR "carbon ion" OR "chemoradiotherapy" OR chemoradiation OR "radiosensitizer" OR radiosensitization OR "radiation therapy" OR radiotherapy OR "brachytherapy" OR "total body irradiation" OR "radiation dose de-escalation" OR "adaptive radiotherapy" OR "MR-guided radiotherapy") AND {CANCER} AND ({TRIAL} OR {INVIVO})',
    ],
    # ------------------------------------------------ RNA / gene / LNP therapeutics
    "rna_gene_therapy": [
        f'("lipid nanoparticle" OR "lipid nanoparticles" OR LNP OR LNPs OR "mRNA therapy" OR "mRNA therapeutics" OR "mRNA-encoded" OR "mRNA-LNP" OR "circular RNA" OR circRNA OR "self-amplifying RNA" OR saRNA OR "siRNA" OR "small interfering RNA" OR "antisense oligonucleotide" OR "antisense oligonucleotides" OR ASO OR "RNA interference" OR "microRNA therapy" OR "miRNA mimic" OR "RNA therapeutics" OR "RNA therapy" OR "aptamer") AND {CANCER} AND (therapy OR treatment OR delivery OR "in vivo")',
        f'("gene therapy" OR "gene editing" OR CRISPR OR "Cas9" OR "Cas12" OR "Cas13" OR "base editing" OR "base editor" OR "prime editing" OR "epigenome editing" OR ("CRISPR screen" AND therapy) OR ("adeno-associated virus" AND cancer) OR ("AAV" AND tumor) OR "suicide gene" OR "gene-directed enzyme prodrug" OR "TP53 gene therapy" OR "p53 reactivation" OR rezatapopt OR "PC14586" OR "eprenetapopt" OR "MDM2 inhibitor" OR "MDM2 degrader" OR "MDM2 antagonist" OR "MDM2-p53" OR "MDM2 inhibitors" OR brigimadlin OR navtemadlin OR milademetan OR "mutant p53 reactivator") AND {CANCER}',
    ],
    # ------------------------------------------------ cytokines, innate agonists, immunomodulators
    "cytokine_innate": [
        f'("interleukin-2" OR "IL-2" OR "IL-2 variant" OR "engineered IL-2" OR "IL-15" OR "interleukin-15" OR "N-803" OR "nogapendekin alfa" OR "nogapendekin" OR Anktiva OR "IL-12" OR "interleukin-12" OR "IL-18" OR "interleukin-18" OR "IL-21" OR "IL-7" OR ("IL-10" AND (agonist OR "pegilodecakin")) OR "IL-15 superagonist" OR "cytokine therapy" OR "immunocytokine" OR "cytokine fusion" OR "engineered cytokine" OR ("interferon" AND therapy) OR "STING agonist" OR "cGAS-STING" OR "cGAS/STING" OR "TLR agonist" OR "TLR7" OR "TLR9" OR "TLR3" OR "CD40 agonist" OR "4-1BB agonist" OR "OX40 agonist" OR "GITR" OR "CD27" OR "NKG2D" OR "innate immune agonist" OR "RIG-I agonist" OR "IL-2Rβγ" OR "IL-2Rα" OR "PD-1-IL2" OR "PD1-IL2v" OR "eciskafusp" OR "efineptakin" OR "bempegaldesleukin" OR "nemvaleukin") AND {CANCER}',
        f'("intravesical" OR "BCG-unresponsive" OR "non-muscle-invasive bladder cancer" OR "non-muscle invasive bladder cancer" OR NMIBC) AND (therapy OR treatment) AND {TRIAL}',
    ],
    # ------------------------------------------------ monoclonal antibodies (non-checkpoint)
    "antibody_other": [
        f'(trastuzumab OR pertuzumab OR cetuximab OR panitumumab OR rituximab OR "anti-HER2" OR "anti-EGFR antibody" OR "anti-EGFR" OR "anti-GD2" OR naxitamab OR dinutuximab OR "hu14.18" OR "anti-Claudin" OR "claudin 18.2" OR "claudin18.2" OR "CLDN18.2" OR zolbetuximab OR "anti-TROP2" OR "TROP2" OR "anti-DLL3" OR "DLL3" OR "anti-CD47" OR "anti-Nectin-4" OR "Nectin-4" OR "anti-B7-H3" OR "anti-CEACAM5" OR "anti-CD70" OR "anti-CD30" OR "anti-TIGIT" OR "Fc-engineered" OR "Fc-enhanced" OR "afucosylated" OR "ADCC" OR "antibody-dependent cellular cytotoxicity" OR "monoclonal antibody therapy" OR "therapeutic antibody" OR "antibody therapy" OR "anti-TGF-β" OR "TGF-β trap" OR "bintrafusp" OR "anti-IL-8" OR "anti-CSF1R" OR "anti-CCR8" OR "anti-IL-1β" OR "anti-LIF") AND {CANCER} AND (therapy OR treatment OR trial OR "in vivo")',
    ],
    # ------------------------------------------------ chemotherapy / conventional regimens
    "chemo_conventional": [
        f'(chemotherapy OR "chemo-immunotherapy" OR chemoimmunotherapy OR "neoadjuvant chemotherapy" OR "adjuvant chemotherapy" OR "total neoadjuvant therapy" OR "total neoadjuvant" OR "watch-and-wait" OR "organ preservation" OR "de-escalation" OR "treatment de-escalation" OR "dose de-escalation" OR "dose-dense" OR "metronomic" OR "HIPEC" OR "hyperthermic intraperitoneal" OR "PIPAC" OR "intraperitoneal chemotherapy" OR "hepatic arterial infusion" OR "transarterial chemoembolization" OR TACE OR "transarterial radioembolization" OR "Y-90" OR "yttrium-90" OR "FOLFIRINOX" OR "NALIRIFOX" OR "FOLFOX" OR "FOLFIRI" OR "gemcitabine" OR "nab-paclitaxel" OR "cisplatin" OR "carboplatin" OR "oxaliplatin" OR "capecitabine" OR "temozolomide" OR "lurbinectedin" OR "trabectedin" OR "eribulin" OR "irinotecan" OR "docetaxel" OR "cabazitaxel" OR "pemetrexed" OR "liposomal irinotecan" OR "liposomal doxorubicin" OR "mitomycin" OR "vincristine" OR "cyclophosphamide") AND {CANCER} AND {TRIAL} AND (survival OR response OR outcome OR efficacy)',
        f'("hematopoietic stem cell transplantation" OR "hematopoietic cell transplantation" OR "allogeneic transplant" OR "autologous stem cell transplant" OR "allo-HCT" OR "allo-HSCT" OR "conditioning regimen" OR "graft-versus-host" OR "post-transplant cyclophosphamide" OR ("maintenance therapy" AND (transplant OR myeloma OR leukemia))) AND {TRIAL}',
    ],
    # ------------------------------------------------ nanomedicine / drug delivery / physical therapies
    "nanomedicine_delivery": [
        f'(nanoparticle OR nanoparticles OR nanomedicine OR nanocarrier OR nanocarriers OR "nano-drug" OR nanodrug OR liposome OR liposomes OR liposomal OR micelle OR micelles OR "polymeric nanoparticle" OR "hydrogel" OR "injectable hydrogel" OR "exosome" OR exosomes OR "extracellular vesicle" OR "extracellular vesicles" OR "cell membrane-coated" OR "biomimetic nanoparticle" OR "metal-organic framework" OR "nanozyme" OR "prodrug nanoassembl*" OR "self-assembling peptide" OR "microneedle" OR "implantable" OR "drug-eluting") AND {CANCER} AND (therapy OR treatment OR "drug delivery") AND {INVIVO}',
        f'("photodynamic therapy" OR "photothermal therapy" OR "sonodynamic therapy" OR "chemodynamic therapy" OR "photoimmunotherapy" OR "photo-immunotherapy" OR "near-infrared photoimmunotherapy" OR cetuximab-sarotalocan OR "focused ultrasound" OR "high-intensity focused ultrasound" OR HIFU OR histotripsy OR "tumor treating fields" OR "tumour treating fields" OR TTFields OR "irreversible electroporation" OR "electrochemotherapy" OR "cryoablation" OR "radiofrequency ablation" OR "microwave ablation" OR "magnetic hyperthermia" OR "thermal ablation" OR "ferroptosis inducer" OR "ferroptosis-inducing" OR ("pyroptosis" AND (nanoparticle OR "in vivo")) OR ("cuproptosis" AND therapy) OR ("immunogenic cell death" AND (inducer OR nanoparticle))) AND {CANCER}',
    ],
    # ------------------------------------------------ tumour microenvironment, metabolic, microbiome
    "tme_metabolic_microbiome": [
        f'("tumor-associated macrophage" OR "tumour-associated macrophage" OR "tumor-associated macrophages" OR "myeloid-derived suppressor" OR "regulatory T cell depletion" OR "Treg depletion" OR "cancer-associated fibroblast" OR "cancer-associated fibroblasts" OR "fibroblast activation protein" OR "tertiary lymphoid structure" OR "tertiary lymphoid structures" OR ("neutrophil" AND tumor AND targeting) OR "macrophage reprogramming" OR "CSF1R" OR "CD40" OR "TREM2" OR "MARCO" OR "SIGLEC" OR "myeloid checkpoint" OR "CXCR4 antagonist" OR "CXCL12" OR "TGF-β inhibitor" OR "TGF-beta inhibitor" OR "IDO1" OR "arginase inhibitor" OR ("adenosine" AND (CD39 OR CD73 OR A2AR)) OR "glutaminase inhibitor" OR "glutamine antagonist" OR "DON prodrug" OR ("lactate" AND (inhibitor OR "MCT1")) OR ("fatty acid oxidation" AND inhibitor) OR "OXPHOS inhibitor" OR "metabolic vulnerability" OR ("dietary intervention" AND (tumor OR cancer)) OR "ketogenic diet" OR "fasting-mimicking" OR "methionine restriction") AND {CANCER} AND {INVIVO}',
        f'("gut microbiome" OR "gut microbiota" OR microbiome OR microbiota OR "fecal microbiota transplantation" OR "faecal microbiota transplantation" OR FMT OR "probiotic" OR "Akkermansia" OR "engineered probiotic" OR "live biotherapeutic" OR "CBM588" OR "intratumoral bacteria" OR "intratumoral microbiome") AND {CANCER} AND (immunotherapy OR chemotherapy OR "checkpoint" OR treatment OR therapy OR response) AND ({TRIAL} OR {INVIVO})',
        f'("drug repurposing" OR "repurposed drug" OR "repurposed drugs" OR metformin OR statin OR statins OR aspirin OR "beta-blocker" OR propranolol OR "GLP-1 receptor agonist" OR semaglutide OR ivermectin OR mebendazole OR disulfiram OR itraconazole OR "antihistamine" OR "vitamin D" OR "omega-3" OR "high-dose vitamin C" OR "ascorbate" OR hydroxychloroquine OR chloroquine OR "cannabinoid" OR "cannabidiol" OR "psilocybin" OR "antipsychotic") AND {CANCER} AND (treatment OR therapy OR survival OR "in vivo" OR trial) AND ({TRIAL} OR {INVIVO})',
    ],
    # ------------------------------------------------ paediatric and CNS tumours (all modalities)
    "pediatric_cns": [
        f'(pediatric OR paediatric OR childhood OR children OR adolescent OR "young adult" OR "AYA") AND (cancer OR tumor OR tumour OR leukemia OR leukaemia OR lymphoma OR sarcoma OR neuroblastoma OR glioma OR medulloblastoma OR "Wilms" OR retinoblastoma OR hepatoblastoma OR "Ewing") AND (therapy OR treatment OR "clinical trial" OR immunotherapy OR "targeted therapy") AND ({TRIAL} OR {INVIVO})',
        f'(glioblastoma OR "glioma" OR "diffuse midline glioma" OR "diffuse intrinsic pontine glioma" OR DIPG OR "H3K27M" OR "H3 K27M" OR "H3.3 G34" OR "H3G34" OR "diffuse hemispheric glioma" OR medulloblastoma OR ependymoma OR "atypical teratoid" OR "ATRT" OR "brain metastases" OR "brain metastasis" OR "leptomeningeal" OR "primary CNS lymphoma" OR "IDH-mutant glioma" OR "low-grade glioma" OR "pediatric low-grade glioma" OR "pilocytic astrocytoma" OR "craniopharyngioma" OR "meningioma") AND (therapy OR treatment OR "clinical trial" OR immunotherapy OR "targeted therapy" OR "CAR T" OR vaccine OR radiotherapy OR "convection-enhanced" OR "intratumoral" OR ("blood-brain barrier" AND delivery) OR "focused ultrasound") AND ({TRIAL} OR {INVIVO})',
        f'(neuroblastoma OR osteosarcoma OR "Ewing sarcoma" OR rhabdomyosarcoma OR "soft tissue sarcoma" OR "synovial sarcoma" OR "desmoplastic small round cell" OR "Wilms tumor" OR "Wilms tumour" OR retinoblastoma OR hepatoblastoma OR "germ cell tumor" OR "Langerhans cell histiocytosis" OR "neurofibromatosis" OR "plexiform neurofibroma" OR ("NF1" AND tumor)) AND (therapy OR treatment OR "clinical trial" OR immunotherapy OR "targeted therapy") AND ({TRIAL} OR {INVIVO})',
    ],
    # ------------------------------------------------ modality-agnostic sweeps
    "sweep_clinical_trials": [
        f'("phase 3" OR "phase III" OR "phase 2/3" OR "randomized phase" OR "randomised phase" OR "randomized controlled trial" OR "randomised controlled trial" OR "randomized, controlled" OR "double-blind") AND {CANCER} AND ("overall survival" OR "progression-free survival" OR "event-free survival" OR "disease-free survival" OR "pathologic complete response" OR "pathological complete response" OR "objective response rate" OR "primary endpoint" OR "primary end point" OR "recurrence-free survival" OR "complete remission" OR "minimal residual disease")',
        f'("phase 1" OR "phase I" OR "phase 1/2" OR "phase I/II" OR "first-in-human" OR "first in human" OR "dose-escalation" OR "dose escalation" OR "dose-finding" OR "dose-expansion" OR "recommended phase 2 dose" OR "maximum tolerated dose" OR "dose-limiting toxicity") AND {CANCER} AND (safety OR tolerability OR "adverse events" OR efficacy OR "antitumor activity" OR "antitumour activity" OR pharmacokinetics)',
        f'("phase 2" OR "phase II" OR "single-arm" OR "single arm" OR "open-label" OR "multicenter" OR "multicentre" OR "basket trial" OR "umbrella trial" OR "platform trial" OR "window-of-opportunity" OR "investigator-initiated") AND {CANCER} AND ("objective response" OR "overall response rate" OR "progression-free survival" OR "pathologic complete response" OR "complete response" OR "clinical benefit" OR "disease control")',
        f'(PUB_TYPE:"Clinical Trial, Phase III" OR PUB_TYPE:"Clinical Trial, Phase II" OR PUB_TYPE:"Clinical Trial, Phase I" OR PUB_TYPE:"Randomized Controlled Trial" OR PUB_TYPE:"Clinical Trial") AND {CANCER}',
        f'("real-world" OR "real world" OR "registry" OR "population-based cohort" OR "nationwide cohort" OR "propensity" OR "target trial emulation" OR "comparative effectiveness") AND {CANCER} AND (immunotherapy OR "targeted therapy" OR "CAR T" OR chemotherapy OR "checkpoint inhibitor" OR "bispecific" OR "antibody-drug conjugate" OR radiotherapy OR "endocrine therapy") AND (survival OR outcome OR effectiveness OR toxicity)',
        f'("systematic review" OR "meta-analysis" OR "network meta-analysis" OR "pooled analysis" OR "umbrella review" OR "individual patient data") AND {CANCER} AND (immunotherapy OR "targeted therapy" OR "CAR T" OR chemotherapy OR "checkpoint inhibitor" OR "bispecific" OR "antibody-drug conjugate" OR radiotherapy OR "endocrine therapy" OR "PARP inhibitor" OR "tyrosine kinase inhibitor")',
        f'("NCT0" OR "NCT1" OR "NCT2" OR "NCT3" OR "NCT4" OR "NCT5" OR "NCT6" OR ClinicalTrials.gov OR "ChiCTR" OR "EudraCT" OR "jRCT" OR "CTRI" OR "ISRCTN" OR "UMIN") AND {CANCER} AND (treatment OR therapy)',
    ],
    "sweep_preclinical": [
        f'("patient-derived xenograft" OR "patient-derived xenografts" OR PDX OR xenograft OR xenografts OR "orthotopic" OR "syngeneic" OR "genetically engineered mouse model" OR "GEMM" OR "humanized mouse" OR "humanised mouse" OR "immunocompetent mice" OR "tumor-bearing mice" OR "tumour-bearing mice" OR "patient-derived organoid" OR "tumor organoid" OR "tumour organoid" OR "organoid" OR "zebrafish xenograft" OR "in vivo efficacy" OR "antitumor efficacy" OR "antitumour efficacy" OR "tumor regression" OR "tumour regression" OR "complete regression" OR "tumor growth inhibition" OR "tumour growth inhibition") AND {CANCER} AND (treatment OR therapy OR inhibitor OR antibody OR "CAR T" OR vaccine OR "combination")',
        f'("mechanism of action" OR "novel inhibitor" OR "novel compound" OR "small molecule" OR "small-molecule" OR "first-in-class" OR "lead compound" OR "structure-activity relationship" OR "drug candidate" OR "preclinical candidate" OR "preclinical development" OR "IND-enabling" OR "covalent inhibitor" OR "allosteric inhibitor" OR "selective inhibitor" OR "dual inhibitor" OR "brain-penetrant" OR "blood-brain barrier penetrant" OR "orally bioavailable") AND {CANCER} AND {INVIVO}',
        f'("combination therapy" OR "combination treatment" OR "synergistic" OR synergy OR "synergize" OR "synergise" OR "sensitizes" OR "sensitises" OR "overcomes resistance" OR "overcome resistance" OR "resistance mechanism" OR "acquired resistance" OR "drug resistance" OR "therapy resistance" OR "chemoresistance" OR "radioresistance") AND {CANCER} AND (treatment OR therapy OR inhibitor OR antibody) AND {INVIVO}',
        f'("CRISPR screen" OR "genome-wide CRISPR" OR "in vivo CRISPR" OR "functional genomics" OR "synthetic lethal" OR "dependency" OR "cancer dependency" OR "high-throughput screen" OR "drug screen" OR "pharmacogenomic" OR "AI-designed" OR ("machine learning" AND ("drug discovery" OR "drug response")) OR ("deep learning" AND ("drug response" OR "drug discovery" OR "drug combination")) OR ("generative" AND ("drug design" OR "molecule"))) AND {CANCER} AND (therapy OR therapeutic OR inhibitor OR target OR "drug")',
    ],
    "sweep_high_impact": [
        f'(JOURNAL:"N Engl J Med" OR JOURNAL:"Lancet" OR JOURNAL:"Lancet Oncol" OR JOURNAL:"J Clin Oncol" OR JOURNAL:"JAMA Oncol" OR JOURNAL:"JAMA" OR JOURNAL:"Ann Oncol" OR JOURNAL:"Nat Med" OR JOURNAL:"Lancet Haematol" OR JOURNAL:"Blood" OR JOURNAL:"J Hematol Oncol" OR JOURNAL:"Cancer Discov" OR JOURNAL:"Clin Cancer Res" OR JOURNAL:"Eur J Cancer" OR JOURNAL:"BMJ" OR JOURNAL:"Nat Rev Clin Oncol" OR JOURNAL:"J Immunother Cancer" OR JOURNAL:"Blood Cancer J" OR JOURNAL:"Leukemia" OR JOURNAL:"Haematologica" OR JOURNAL:"Br J Cancer" OR JOURNAL:"J Thorac Oncol" OR JOURNAL:"Eur Urol" OR JOURNAL:"Gynecol Oncol" OR JOURNAL:"Int J Radiat Oncol Biol Phys" OR JOURNAL:"Cancer") AND {CANCER} AND (therapy OR treatment OR trial OR immunotherapy OR chemotherapy OR inhibitor OR antibody OR radiotherapy)',
        f'(JOURNAL:"Nature" OR JOURNAL:"Science" OR JOURNAL:"Cell" OR JOURNAL:"Cancer Cell" OR JOURNAL:"Nat Cancer" OR JOURNAL:"Nat Biotechnol" OR JOURNAL:"Sci Transl Med" OR JOURNAL:"Immunity" OR JOURNAL:"Nat Immunol" OR JOURNAL:"Nat Commun" OR JOURNAL:"Cancer Immunol Res" OR JOURNAL:"Cancer Res" OR JOURNAL:"Mol Cancer" OR JOURNAL:"J Clin Invest" OR JOURNAL:"Proc Natl Acad Sci U S A" OR JOURNAL:"Cell Rep Med" OR JOURNAL:"Mol Ther" OR JOURNAL:"Nat Chem Biol" OR JOURNAL:"J Exp Med" OR JOURNAL:"Sci Adv" OR JOURNAL:"Adv Mater" OR JOURNAL:"ACS Nano" OR JOURNAL:"J Med Chem" OR JOURNAL:"Signal Transduct Target Ther" OR JOURNAL:"Cell Metab" OR JOURNAL:"Cancer Lett" OR JOURNAL:"Oncogene" OR JOURNAL:"Neuro Oncol" OR JOURNAL:"Nat Nanotechnol" OR JOURNAL:"J Control Release" OR JOURNAL:"Biomaterials" OR JOURNAL:"Mol Cancer Ther") AND {CANCER} AND (therapy OR treatment OR therapeutic OR immunotherapy OR inhibitor OR antibody OR "CAR T" OR vaccine OR "in vivo")',
    ],
}

PAGE = 500
MAX_PAGES = 16  # up to 8,000 records per query


def epmc_search(query, page_size=PAGE, max_pages=MAX_PAGES):
    out = []
    cursor = "*"
    hit_count = None
    for _ in range(max_pages):
        params = urllib.parse.urlencode({
            "query": query, "format": "json", "pageSize": page_size,
            "resultType": "core", "cursorMark": cursor,
        })
        url = f"{EPMC}?{params}"
        data = None
        for attempt in range(5):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "lit-syn/1.0"})
                with urllib.request.urlopen(req, timeout=180) as resp:
                    data = json.load(resp)
                break
            except Exception as exc:
                sys.stderr.write(f"  retry {attempt}: {exc}\n")
                time.sleep(5 + 5 * attempt)
        if data is None:
            break
        if hit_count is None:
            hit_count = data.get("hitCount", 0)
        results = data.get("resultList", {}).get("result", [])
        out.extend(results)
        nxt = data.get("nextCursorMark")
        if not results or not nxt or nxt == cursor:
            break
        cursor = nxt
        time.sleep(0.4)
    return out, hit_count


def clean(text):
    if not text:
        return ""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", text)).strip()


def venue_of(rec):
    ji = rec.get("journalInfo", {}) or {}
    return (ji.get("journal", {}).get("title", "")
            or ji.get("journal", {}).get("medlineAbbreviation", "")
            or rec.get("journalTitle", "")
            or (rec.get("bookOrReportDetails", {}) or {}).get("publisher", ""))


def main():
    seen = {}
    log = open(LOG, "a")
    for domain, queries in QUERIES.items():
        for q in queries:
            q_full = f"({q}) AND {WINDOW}"
            results, hits = epmc_search(q_full)
            new = 0
            for rec in results:
                key = rec.get("pmid") or rec.get("doi") or rec.get("id")
                if not key:
                    continue
                if key in seen:
                    seen[key]["also_domains"].add(domain)
                    continue
                new += 1
                seen[key] = {
                    "domain": domain,
                    "also_domains": set(),
                    "pmid": rec.get("pmid", ""),
                    "pmcid": rec.get("pmcid", ""),
                    "doi": rec.get("doi", ""),
                    "title": clean(rec.get("title", "")).rstrip("."),
                    "abstract": clean(rec.get("abstractText", "")),
                    "authors": rec.get("authorString", ""),
                    "venue": venue_of(rec),
                    "year": rec.get("pubYear", ""),
                    "date": rec.get("firstPublicationDate", ""),
                    "isOA": rec.get("isOpenAccess", "N"),
                    "inEPMC": rec.get("inEPMC", "N"),
                    "hasPDF": rec.get("hasPDF", "N"),
                    "cited": rec.get("citedByCount", 0),
                    "pubType": (rec.get("pubTypeList", {}) or {}).get("pubType", []),
                    "src": rec.get("source", ""),
                }
            msg = f"{domain}: '{q[:80]}' -> hits={hits} fetched={len(results)} new={new} total={len(seen)}\n"
            sys.stderr.write(msg)
            log.write(msg)
            log.flush()
            time.sleep(0.4)

    out = []
    for v in seen.values():
        v["also_domains"] = "|".join(sorted(v["also_domains"]))
        v["pubType"] = "|".join(v["pubType"]) if isinstance(v["pubType"], list) else str(v["pubType"])
        out.append(v)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=0)
    print(f"total unique records: {len(out)}")
    log.write(f"total unique records: {len(out)}\n")
    log.close()


if __name__ == "__main__":
    main()
