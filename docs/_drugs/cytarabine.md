---
layout: default
title: Cytarabine
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 10
---

# Cytarabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Cytarabine: From Acute Leukemia to Small Cell Lung Carcinoma

## One-Sentence Summary

Cytarabine (Ara-C) is a well-established S-phase–specific antimetabolite, classically used in the treatment of acute leukemias and high-dose lymphoma conditioning regimens.
The TxGNN model predicts it may be effective for **Small Cell Lung Carcinoma (SCLC)**, supported by **20 publications** — though the most directly relevant clinical evidence dates from the 1970s–1990s, and the 3 retrieved clinical trials are only indirectly related.
Overall evidence is rated **L3**, reflecting historical observational and phase II data rather than modern controlled trials.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute leukemia (established clinical use; not registered in Singapore) |
| Predicted New Indication | Small Cell Lung Carcinoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cytarabine (cytosine arabinoside, Ara-C) is a pyrimidine antimetabolite that competitively inhibits DNA polymerase by substituting for deoxycytidine triphosphate during DNA replication. Because it acts specifically during S phase, it is most potent against tumours with a high proportion of actively dividing cells — precisely the biological profile of small cell lung carcinoma.

SCLC is one of the most rapidly proliferating solid tumours known, with extremely high S-phase fractions and doubling times measured in days rather than weeks. This biological overlap with classical Ara-C targets — acute leukaemias — forms the mechanistic backbone of the TxGNN prediction, and was indeed recognised by oncologists in the 1970s and 1980s. Several early clinical series combined Ara-C with cisplatin, cyclophosphamide, or etoposide in SCLC, reporting partial remissions. One multicentre study of 20 untreated SCLC patients achieved a 78% combined response rate with a cyclophosphamide/Adriamycin/Ara-C regimen plus radiotherapy (PMID 232239).

Despite this early promise, the platinum/etoposide doublet ultimately became the standard of care for SCLC due to superior reproducibility and tolerability, displacing Ara-C–based regimens from mainstream practice. The most defensible contemporary role for Cytarabine in SCLC is intrathecal administration for leptomeningeal metastasis — an established use in haematological malignancies that has been extrapolated to solid-tumour CNS complications — and potentially in refractory or multiply relapsed settings where conventional options are exhausted.

---

## Clinical Trial Evidence

> **Note:** All three retrieved trials have Grade C (indirect) relevance. They study Pemetrexed — not Cytarabine — as the primary intrathecal agent for NSCLC leptomeningeal metastases, or adjuvant regimens in early NSCLC without SCLC-specific endpoints. No prospective trial directly evaluating Cytarabine in SCLC was identified in the current search.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03101579](https://clinicaltrials.gov/study/NCT03101579) | Phase 1 | Completed | 13 | Intrathecal pemetrexed for recurrent NSCLC leptomeningeal metastases; Cytarabine cited as one of the current standard IT agents, providing background context for IT chemotherapy design in thoracic oncology |
| [NCT03507244](https://clinicaltrials.gov/study/NCT03507244) | Phase 1/2 | Completed | 34 | IT pemetrexed + involved-field radiotherapy for LM from solid tumours; offers a reference treatment design framework for CNS-directed chemotherapy in lung cancer |
| [NCT00863512](https://clinicaltrials.gov/study/NCT00863512) | Phase 3 | Terminated | 34 | Adjuvant chemotherapy (vinorelbine, cisplatin, docetaxel, gemcitabine, pemetrexed) in early NSCLC; terminated early due to slow accrual; no SCLC arms, no Cytarabine — low reference value |

---

## Literature Evidence

Prioritised by direct relevance to Cytarabine in SCLC or lung cancer, then by study design tier:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [232239](https://pubmed.ncbi.nlm.nih.gov/232239/) | 1979 | Clinical Series | Med Pediatr Oncol | 20 untreated SCLC patients received cyclophosphamide + Adriamycin + cytosine arabinoside q28d + radiotherapy; 78% combined response rate, median survival 49+ weeks for complete responders — earliest direct evidence for Ara-C in SCLC |
| [6095640](https://pubmed.ncbi.nlm.nih.gov/6095640/) | 1984 | Clinical Study | Am J Clin Oncol | Continuous-infusion Ara-C (100 mg/m²/d) in SCLC: no responses in 10 heavily pre-treated patients (monotherapy); Ara-C added to CAV in 25 extensive-stage patients with evaluation of additive benefit |
| [2841844](https://pubmed.ncbi.nlm.nih.gov/2841844/) | 1988 | Clinical Study | Am J Clin Oncol | VP-16 + infusional Ara-C (45 mg/m²/d × 72 h) in 17 SCLC patients refractory to combination chemotherapy; limited objective responses, 3 early deaths from progressive disease |
| [9363869](https://pubmed.ncbi.nlm.nih.gov/9363869/) | 1997 | RCT | J Clin Oncol | Randomised trial of chemo + radiation ± warfarin in limited-stage SCLC (CALGB); provides a benchmark for multimodality regimens in limited-stage disease — comparator context for historic Ara-C combinations |
| [6264785](https://pubmed.ncbi.nlm.nih.gov/6264785/) | 1981 | Case Series | Am J Med | Meningeal carcinomatosis in SCLC: 60 patients, intensive systemic chemotherapy without prophylactic cranial irradiation; 78% overall response rate, supports relevance of Cytarabine in CNS complication management |
| [28223673](https://pubmed.ncbi.nlm.nih.gov/28223673/) | 2017 | Case Report | Gan To Kagaku Ryoho | SCLC (Stage IV) with meningeal carcinomatosis effectively managed with multidisciplinary approach including IT chemotherapy; illustrates a contemporary clinical scenario where IT Cytarabine remains an active option |
| [2157307](https://pubmed.ncbi.nlm.nih.gov/2157307/) | 1990 | Phase II | Tumori | Ara-C + cisplatin + vindesine in 32 advanced NSCLC patients; 18% response rate (5/28 evaluable); cross-tumour evidence for Ara-C + platinum activity in lung malignancies |
| [2156598](https://pubmed.ncbi.nlm.nih.gov/2156598/) | 1990 | Phase II | Cancer | High-dose Ara-C (3 g/m²) + cisplatin (100 mg/m²) in 37 chemotherapy-naive NSCLC patients; 14% overall response; Grade IV myelosuppression in 32%, 4 treatment-related deaths — significant toxicity signal |
| [2820740](https://pubmed.ncbi.nlm.nih.gov/2820740/) | 1987 | Pilot Study | Eur J Cancer Clin Oncol | Cisplatin + Cytarabine combination in advanced NSCLC pilot study; early safety and feasibility assessment for the Ara-C + platinum backbone |
| [348088](https://pubmed.ncbi.nlm.nih.gov/348088/) | 1978 | Review | Antibiotics Chemother | Ara-C analogues: mechanism of rapid inactivation by cytidine deaminase, rationale for cytidine deaminase inhibitors and longer-acting Ara-C derivatives — mechanistic context for resistance and formulation development |

---

## Singapore Market Information

Cytarabine is **not currently registered** in Singapore. No product authorisation records are on file, and there is no approved indication text available from local regulatory sources.

---

## Cytotoxicity

Cytarabine is a conventional cytotoxic antimetabolite. Its indication in acute leukemia and lymphoma conditioning regimens clearly classifies it as an antineoplastic agent subject to cytotoxic handling requirements.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Pyrimidine antimetabolite (S-phase specific) |
| Myelosuppression Risk | High — Neutropenia and thrombocytopenia are dose-limiting; Grade IV myelosuppression reported in approximately 32% of patients receiving high-dose regimens (3 g/m²); standard-dose regimens carry moderate-to-high bone marrow suppression risk |
| Emetogenicity Classification | Low to moderate at standard doses; moderate to high at high doses (≥1 g/m²) |
| Monitoring Items | CBC with differential count (before each cycle and at nadir, typically days 7–14); liver function tests; renal function (creatinine, BUN); neurological assessment for cerebellar toxicity (especially high-dose and intrathecal administration); ophthalmological review with high-dose therapy |
| Handling Protection | Must be prepared in a certified biological safety cabinet; full personal protective equipment (gloves, gown, eye protection) required; cytotoxic waste disposal per institutional and regulatory guidelines |

---

## Safety Considerations

No Singapore-specific package insert data, TFDA prescribing information, or drug interaction data is currently available for this evaluation. Please refer to the reference country SmPC or manufacturer's package insert for complete warnings, contraindications, and drug interaction information before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the mechanistic rationale for Ara-C in SCLC is biologically plausible — both share a high S-phase fraction — the available direct clinical evidence is historical (1970s–1990s), characterised by small sample sizes, no randomised controlled comparisons, and significant haematological toxicity. Modern SCLC first-line treatment (platinum/etoposide ± immunotherapy) and second-line options (topotecan, lurbinectedin) have rendered Ara-C–based regimens non-competitive as a standard approach. Cytarabine is also not registered in Singapore, presenting a regulatory barrier.

**To proceed, the following is needed:**

- **Niche indication definition:** Identify a specific clinical scenario where Cytarabine offers differentiated value — most likely refractory/relapsed SCLC with leptomeningeal metastasis — and scope a hypothesis-driven protocol accordingly
- **Contemporary preclinical validation:** Updated in vitro and patient-derived xenograft (PDX) data in modern SCLC models, including assessment of cytidine deaminase expression (a key resistance mechanism) in SCLC versus AML
- **Mechanism of action documentation:** Obtain complete MOA and pharmacokinetic data from DrugBank or primary literature to strengthen the mechanistic rationale section for any regulatory or ethics submission
- **Safety review:** Compile full warnings, contraindications, and drug interaction profile from reference country SmPC (e.g., EMA, FDA) before any clinical programme design
- **Singapore regulatory pathway assessment:** Evaluate requirements for clinical trial import authorisation and potential registration pathway through HSA if evidence supports progression
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

