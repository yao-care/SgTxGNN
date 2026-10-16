---
layout: default
title: Carfilzomib
parent: Low Evidence (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Carfilzomib: predicted new indication CMM7 (evidence level L5). Approved use: Plasma cell myeloma"
monitor_inn: "Carfilzomib"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "vulvar melanoma (disease)", "melanoma", "indolent plasma cell myeloma", "intellectual disability, autosomal dominant 55, with seizures", "myeloid leukemia", "neutrophil immunodeficiency syndrome", "central nervous system melanocytic neoplasm"]
---

# Carfilzomib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Carfilzomib: From Plasma Cell Myeloma to Melanoma

## One-Sentence Summary

Carfilzomib is a proteasome inhibitor originally used to treat plasma cell myeloma.
The TxGNN model's top-ranked prediction is **CMM7** (a melanoma-related condition), but no clinical trials or publications support it. The best-supported prediction is **melanoma** (rank 5), which has only **4 preclinical or computational publications** and **no clinical trials**. A separate prediction, **myeloid leukemia**, has the strongest clinical support (**1 directly relevant Phase 1 trial of carfilzomib** and several preclinical studies).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plasma cell myeloma (the Singapore licence records contain no indication text) |
| Predicted New Indication | CMM7 (top-ranked prediction) |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

**Other predictions in the top 10 (for context):**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|---|------|------|------|------|
| 2 | Pediatric leptomeningeal melanoma | 99.30% | L5 | Hold |
| 3 | Epithelioid cell uveal melanoma | 99.23% | L5 | Hold |
| 4 | Vulvar melanoma | 99.19% | L5 | Hold |
| 5 | Melanoma | 99.03% | L4 | Research Question |
| 6 | Indolent plasma cell myeloma | 97.94% | L4 | Research Question |
| 7 | Intellectual disability, autosomal dominant 55, with seizures | 97.82% | L5 | Hold |
| 8 | Myeloid leukemia | 97.01% | L3 | Research Question |
| 9 | Neutrophil immunodeficiency syndrome | 95.11% | L5 | Hold |
| 10 | Central nervous system melanocytic neoplasm | 93.29% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Carfilzomib is known to be a selective, irreversible proteasome inhibitor. Blocking the proteasome causes misfolded proteins to accumulate, producing proteotoxic stress and apoptosis (programmed cell death) in cancer cells. Its efficacy in plasma cell myeloma is established.

**Melanoma-related predictions (CMM7, pediatric leptomeningeal, uveal, vulvar, CNS melanocytic):** these are prediction-only, with no trials or publications retrieved. For melanoma itself, the only support is preclinical. An in vitro study (PMID 33671902) found that carfilzomib plus bortezomib enhanced apoptosis in B16-F1 melanoma cells. Carfilzomib has limited CNS penetration, which is a major barrier for the leptomeningeal and CNS-related predictions.

**Myeloid leukemia:** this is the best-supported new direction. The proteasome is a recognised vulnerability in AML (PMID 27911437). A completed Phase 1 trial of carfilzomib in relapsed AML/ALL (NCT01137747, n=18) supports initial safety and feasibility, but not efficacy.

**Indolent plasma cell myeloma:** this is better viewed as an extension of the existing indication than as true repurposing.

**Not mechanistically supported:** autosomal dominant intellectual disability with seizures has no apparent rationale for a cytotoxic proteasome inhibitor. Neutrophil immunodeficiency syndrome raises a safety concern because carfilzomib can cause myelosuppression and neutropenia.

---

## Clinical Trial Evidence

There are no clinical trials for the top-ranked prediction (CMM7) or for melanoma. The trials below relate to **myeloid leukemia** (rank 8).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01137747](https://clinicaltrials.gov/study/NCT01137747) | Phase 1 | Completed | 18 | Escalating doses of carfilzomib in relapsed AML and ALL; directly relevant, small sample |
| [NCT01204164](https://clinicaltrials.gov/study/NCT01204164) | Phase 1 | Completed | 120 | TG02 citrate (a different drug) in advanced hematological malignancies; low relevance |
| [NCT03530683](https://clinicaltrials.gov/study/NCT03530683) | Phase 1 | Terminated | 189 | TTI-622/maplirpacept (a different agent) in hematologic malignancies; low relevance |

---

## Literature Evidence

**Melanoma (rank 5)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | In vitro study | Biology | Carfilzomib plus bortezomib enhanced apoptosis and caspase activation in B16-F1 melanoma cells |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | Computational study | J Biomol Struct Dyn | Docking and dynamics simulations for drug repurposing across ten cancer types, including melanoma |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Preclinical mechanistic study | Mol Cancer Res | ZFAND2A (AIRAP) regulates melanoma cell survival via cIAP2; indirect relevance |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Preclinical mechanistic study | Matrix Biol | Bortezomib and carfilzomib upregulate heparanase through NF-κB, which may promote an aggressive tumour phenotype |

**Myeloid leukemia (rank 8), selected publications**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26674111](https://pubmed.ncbi.nlm.nih.gov/26674111/) | 2016 | Phase 1 study | Leuk Lymphoma | Phase 1 study of carfilzomib in relapsed or refractory AML and ALL |
| [27911437](https://pubmed.ncbi.nlm.nih.gov/27911437/) | 2016 | Review | Blood Cancer J | Role of the proteasome in AML; proteasome inhibition is a promising strategy |
| [31785545](https://pubmed.ncbi.nlm.nih.gov/31785545/) | 2020 | Review | Drug Resist Updat | Targeting the ubiquitin-proteasome pathway to overcome anticancer drug resistance |
| [39285441](https://pubmed.ncbi.nlm.nih.gov/39285441/) | 2024 | Preclinical study | J Hematol Oncol | Proteasome inhibition enhances the anti-leukemic efficacy of CAR-NK cells against AML |
| [19275578](https://pubmed.ncbi.nlm.nih.gov/19275578/) | 2009 | In vitro study | Cardiovasc Hematol Disord Drug Targets | Proteasome inhibitors, alone and with HDAC inhibitors, are antiproliferative and proapoptotic in leukemia cells |
| [24590311](https://pubmed.ncbi.nlm.nih.gov/24590311/) | 2014 | Preclinical study | Oncogenesis | Carfilzomib synergises with tyrosine kinase inhibitors in imatinib-sensitive and -resistant CML models |
| [28340282](https://pubmed.ncbi.nlm.nih.gov/28340282/) | 2017 | Preclinical study | Br J Haematol | Carfilzomib induces leukaemia cell apoptosis via ELK1/CIP2A inhibition and PP2A activation, not related to proteasome inhibition |
| [24735925](https://pubmed.ncbi.nlm.nih.gov/24735925/) | 2014 | Preclinical study | Cancer Cell | Proteasome inhibitors evoke tumour suppression programmes in MLL-rearranged pro-B leukemias |
| [30374242](https://pubmed.ncbi.nlm.nih.gov/30374242/) | 2018 | Case report | Tex Heart Inst J | Bortezomib-induced cardiac tamponade; highlights cardiac risk with proteasome inhibitors |

**Indolent plasma cell myeloma (rank 6)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27291302](https://pubmed.ncbi.nlm.nih.gov/27291302/) | 2016 | Review | Am J Hematol | General update on myeloma diagnosis, risk stratification and management; indirect |
| [42719364](https://pubmed.ncbi.nlm.nih.gov/42719364/) | 2026 | Case report | Ther Adv Hematol | Fulminant extramedullary myeloma relapse with multivisceral involvement; indirect |

Several retrieved publications for myeloid leukemia are off-topic (for example, PMID 32566462 on peripheral artery disease and stroke, and PMID 41331127 on isatuximab dosing).

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15184P | KYPROLIS Powder for Solution for Infusion 60 mg/vial | Injection, powder, lyophilized, for solution | Not stated in the licence records |
| SIN15414P | KYPROLIS Powder for Solution for Infusion 30 mg/vial | Injection, powder, lyophilized, for solution | Not stated in the licence records |

Both licences are valid, and both are for the injectable (intravenous infusion) route only.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (proteasome inhibitor) with cytotoxic antineoplastic activity |
| Myelosuppression Risk | Medium to high (thrombocytopenia, neutropenia and anaemia are expected; please refer to the package insert warnings and precautions) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes, cardiac assessment |
| Handling Protection | Follow institutional cytotoxic drug handling regulations |

---

## Safety Considerations

**Drug Interactions:** The data compiled for this report list 100 interactions. The 20 reviewed include:
- **Major:** oxandrolone, oxymetholone, stanozolol, deferiprone, samarium (153Sm) lexidronam, and several haemostatic or coagulation products (recombinant antihemophilic factor, aminocaproic acid, von Willebrand factor, avatrombopag, human C1-esterase inhibitor, recombinant factor VIIa, factor X, conestat alfa)
- **Moderate:** metronidazole, naltrexone, rosuvastatin, simvastatin, tinidazole, palifermin, strontium chloride Sr-89

For other safety information, please refer to the package insert. The published literature also notes cardiac toxicity with proteasome inhibitors (for example, PMID 30374242).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (CMM7) and most other predictions are model outputs only, with no clinical trial or publication support (L5). Melanoma has only in vitro and computational evidence (L4). Myeloid leukemia has a single small Phase 1 trial showing feasibility but not efficacy (L3). Mechanistic and safety concerns also argue against several predictions: limited CNS penetration for leptomeningeal and CNS melanoma, myelosuppression risk for neutrophil immunodeficiency, and no rationale for a neurodevelopmental disorder. Myeloid leukemia and melanoma are worth pursuing as research questions, but the evidence does not yet justify moving forward.

**To proceed, the following is needed:**
- Mechanism of action data and the Singapore package insert warnings and contraindications (blocking for safety screening)
- For myeloid leukemia: efficacy results from NCT01137747 and a phase 2 trial design, ideally in combination regimens
- For melanoma: in vivo studies and a rationale for any combination partner
- A CNS penetration assessment before pursuing leptomeningeal or CNS melanoma
- Singapore-specific regulatory assessment of any new indication, since the current licences do not state an approved indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

