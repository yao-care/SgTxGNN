# Imatinib: From CML/GIST to Fibroblastic Neoplasm

## One-Sentence Summary

Imatinib (Gleevec/Glivec) is a first-in-class tyrosine kinase inhibitor originally developed for Chronic Myeloid Leukemia (CML) and Gastrointestinal Stromal Tumors (GIST), acting through inhibition of BCR-ABL, c-KIT, and PDGFR kinases.
The TxGNN model predicts activity across **10 rare oncological and non-oncological conditions**, with the strongest mechanistic and clinical evidence supporting **Fibroblastic Neoplasm** (particularly Dermatofibrosarcoma Protuberans/DFSP), backed by FDA approval since 2006, a 2025 European interdisciplinary guideline, and multiple Phase 2 trials.
Imatinib is **not currently registered in Singapore**, and evidence quality across the 10 predictions varies substantially from L2 (Proceed with Guardrails) to L5 (Hold).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Myeloid Leukemia (CML), Gastrointestinal Stromal Tumor (GIST) |
| Top Predicted Indication (by TxGNN score) | Heart Fibrosarcoma (Rank 1, 99.94%) |
| Most Actionable Predicted Indication | Fibroblastic Neoplasm / DFSP (Rank 2, 99.94%) |
| TxGNN Prediction Score (Rank 1) | 99.94% |
| Highest Evidence Level Achieved | L2 (Fibroblastic Neoplasm) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Proceed with Guardrails** (Fibroblastic Neoplasm/DFSP) |

---

## All 10 Predicted Indications — Summary

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|----------------|----------------|
| 1 | Heart Fibrosarcoma | 99.94% | L4 | Hold |
| **2** | **Fibroblastic Neoplasm (DFSP)** | **99.94%** | **L2** | **Proceed with Guardrails** |
| 3 | Conventional Fibrosarcoma | 99.93% | L3 | Research Question |
| 4 | Kidney Fibrosarcoma | 99.93% | L3 | Research Question |
| 5 | Low Grade Fibromyxoid Sarcoma | 99.93% | L5 | Hold |
| 6 | Liposarcoma | 99.88% | L3 | Research Question |
| 7 | Liver Fibrosarcoma | 99.86% | L4 | Hold |
| 8 | Autosomal Recessive Familial Mediterranean Fever | 99.86% | L5 | Hold |
| 9 | Ovarian Myxoid Liposarcoma | 99.85% | L5 | Hold |
| 10 | Familial Rhabdoid Tumor | 99.83% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current dataset. Based on well-established pharmacological knowledge, Imatinib is a small-molecule tyrosine kinase inhibitor (TKI) that competitively inhibits three key kinases: **BCR-ABL** (the oncogenic fusion kinase driving CML), **c-KIT** (CD117, mutated in GIST and other tumours), and **PDGFR-α/β** (platelet-derived growth factor receptors). Its clinical success in CML and GIST established the paradigm of molecularly targeted oncology.

For **Fibroblastic Neoplasm**, particularly Dermatofibrosarcoma Protuberans (DFSP), the mechanistic link is among the strongest in soft tissue oncology. DFSP is defined by a chromosomal translocation t(17;22)(q22;q13) that fuses the **COL1A1** gene with **PDGFB**, creating a fusion protein that drives **constitutive PDGFR-β activation**. This is a direct, specific molecular target for imatinib. The FDA approved imatinib for unresectable and/or metastatic DFSP in 2006, and the 2025 European interdisciplinary guideline (PMID 39904126) continues to endorse this use.

The high TxGNN scores for rarer fibrosarcoma variants (heart, kidney, liver) and mechanistically unrelated conditions (familial Mediterranean fever, familial rhabdoid tumour) reflect **topological similarity in the knowledge graph** — these nodes share fibroblastic or sarcoma classification edges — rather than direct molecular driver matching. For FMF (MEFV/pyrin/inflammasome pathway), low grade fibromyxoid sarcoma (FUS-CREB3L2 fusion), and familial rhabdoid tumour (SMARCB1 loss), the known oncogenic drivers have no established connection to imatinib's target kinases.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00085475](https://clinicaltrials.gov/study/NCT00085475) | Phase 2 | Completed | 17 | Imatinib in locally advanced/metastatic DFSP and Giant Cell Fibroblastoma carrying the t(17;22) COL1A1/PDGF-β translocation; directly validates the fusion-driven PDGFR-β mechanism |
| [NCT00154388](https://clinicaltrials.gov/study/NCT00154388) | Phase 2 | Completed | 185 | Basket trial of imatinib across rare malignancies associated with imatinib-sensitive tyrosine kinases; potential coverage of kidney fibrosarcoma and other rare subtypes, though subgroup data are limited |
| [NCT00006357](https://clinicaltrials.gov/study/NCT00006357) | Phase 1/2 | Completed | 91 | STI571 (imatinib) in advanced soft tissue sarcomas including liposarcoma; provides dose-finding, safety and preliminary efficacy data |
| [NCT00031915](https://clinicaltrials.gov/study/NCT00031915) | Phase 2 | Completed | N/A | Gleevec in metastatic/unresectable soft tissue and bone sarcomas; multi-disciplinary North American Sarcoma Study Group trial covering multiple histological subtypes |

---

## Literature Evidence (Fibroblastic Neoplasm — Top 10)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39904126](https://pubmed.ncbi.nlm.nih.gov/39904126/) | 2025 | Clinical Practice Guideline | European Journal of Cancer | 2025 EADO/EDF/UEMS/EADV European interdisciplinary guideline update for DFSP; recommends imatinib for unresectable/advanced DFSP based on accumulated evidence |
| [33449152](https://pubmed.ncbi.nlm.nih.gov/33449152/) | 2021 | Review | Cell Mol Life Sci | Comprehensive review of PDGFRA/PDGFRB mutations across diseases; PDGFRB mutations drive myofibroma; directly supports PDGFR-targeted therapy rationale in fibroblastic neoplasms |
| [28795284](https://pubmed.ncbi.nlm.nih.gov/28795284/) | 2017 | Review | Current Treatment Options in Oncology | DFSP management review; outlines role of imatinib in locally advanced or metastatic/unresectable cases where surgical cure is not feasible |
| [31466588](https://pubmed.ncbi.nlm.nih.gov/31466588/) | 2019 | Review | Dermatologic Clinics | DFSP pathology, behaviour and treatment; systemic imatinib therapy for advanced disease described alongside Mohs surgery |
| [26027711](https://pubmed.ncbi.nlm.nih.gov/26027711/) | 2015 | Review | Expert Review of Anticancer Therapy | Current treatment options for DFSP; t(17;22) as critical event creating PDGFB autocrine/paracrine driver; imatinib role in unresectable disease |
| [30297237](https://pubmed.ncbi.nlm.nih.gov/30297237/) | 2018 | Review | Bulletin du Cancer | DFSP management highlighting COL1A1-PDGFB translocation; imatinib recommendation for unresectable/metastatic relapse |
| [35038826](https://pubmed.ncbi.nlm.nih.gov/35038826/) | 2022 | Phase 2 Trial | Cancer Research and Treatment | Phase 2 trial identifying NOTCH2 and HES1 as potential molecular markers of imatinib response in desmoid tumour (aggressive fibromatosis); extends understanding of imatinib activity in fibroblastic conditions |
| [25852058](https://pubmed.ncbi.nlm.nih.gov/25852058/) | 2015 | Translational/Mechanistic | Molecular Cancer Therapeutics | CDKN2A/p16 loss implicates CDK4 as a therapeutic target in imatinib-resistant DFSP; provides insight into acquired resistance mechanisms |
| [36999599](https://pubmed.ncbi.nlm.nih.gov/36999599/) | 2023 | Review | Journal of Surgical Oncology | DFSP surgical management review; NCCN guidelines now prefer Mohs micrographic surgery; imatinib confirmed for advanced/unresectable disease |
| [39580648](https://pubmed.ncbi.nlm.nih.gov/39580648/) | 2025 | Genetics/Case Series | Genetics in Medicine | Novel germline PDGFRB splice variant in infantile myofibromatosis associated with resistance to imatinib; critical for understanding imatinib limitations in PDGFRB-driven conditions |

---

## Singapore Market Information

Imatinib is **not currently registered with the Health Sciences Authority (HSA) of Singapore**. There are no recorded product licences in the current dataset.

> Imatinib (Gleevec/Glivec, Novartis) holds regulatory approval in multiple major markets — US (FDA, 2001), EU (EMA), Japan (PMDA), and Taiwan (TFDA). Its absence from the Singapore HSA registry should be verified directly with HSA prior to any clinical consideration. Named patient or compassionate use programmes may represent an access pathway for eligible patients.

---

## Cytotoxicity

Imatinib is an antineoplastic drug used for malignant conditions (CML, GIST, DFSP). It qualifies for cytotoxicity classification as a targeted antineoplastic agent.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Tyrosine Kinase Inhibitor (BCR-ABL / c-KIT / PDGFR-α/β inhibitor); not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Moderate — neutropenia, thrombocytopenia, and anaemia are commonly reported, particularly in the first months of treatment |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (neutrophils, platelets), liver function tests (ALT, AST, bilirubin), renal function (creatinine), body weight and signs of fluid retention/oedema |
| Handling Protection | Follow cytotoxic drug handling regulations for preparation, dispensing, and disposal |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (key warnings, contraindications, drug-drug interactions) are not available in the current dataset. A full safety review from the official SmPC (FDA/EMA) or package insert is mandatory before any clinical application. Literature signals of note include: severe hepatotoxicity, clinically significant fluid retention/oedema, cardiac toxicity in patients with pre-existing cardiac disease, and DRESS syndrome (drug reaction with eosinophilia and systemic symptoms; PMID 30096127).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Fibroblastic Neoplasm / DFSP)

**Rationale:**
Imatinib has FDA approval (2006) for unresectable/metastatic DFSP driven by the COL1A1-PDGFB t(17;22) translocation, supported by Phase 2 clinical trials and endorsed by the 2025 European interdisciplinary guideline. This is one of the most mechanistically validated examples of TKI repurposing in soft tissue oncology. The principal barrier to use in Singapore is the absence of local HSA registration.

**To proceed, the following is needed:**

- **Singapore regulatory pathway**: Verify HSA registration status or initiate a compassionate use / named patient programme for DFSP indication
- **Full safety review**: Obtain and review the complete imatinib SmPC/package insert (FDA or EMA) for warnings, contraindications, and drug interactions before any clinical application
- **Molecular pre-screening**: Confirm COL1A1-PDGFB t(17;22) translocation by FISH or RT-PCR in all DFSP patients prior to initiating imatinib therapy, as response is translocation-dependent
- **MOA documentation**: Complete DrugBank/literature-based formal documentation of mechanism of action (currently a data gap)
- **Indications for further research** (L3 — Research Question): Conventional fibrosarcoma, kidney fibrosarcoma, and liposarcoma each require dedicated molecular profiling and feasibility assessment before any therapeutic consideration
- **Hold indications**: Low grade fibromyxoid sarcoma (FUS-CREB3L2 driven), familial Mediterranean fever (MEFV/pyrin driven), ovarian myxoid liposarcoma (FUS-DDIT3 driven), and familial rhabdoid tumour (SMARCB1 loss driven) lack mechanistic justification for imatinib use and should not be pursued without substantial new evidence

---
*This report is for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application. Data cutoff: 2026-04-04.*