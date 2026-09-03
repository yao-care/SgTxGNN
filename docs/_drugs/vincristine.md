---
layout: default
title: Vincristine
parent: 僅模型預測 (L5)
nav_order: 1059
evidence_level: L5
indication_count: 10
---

# Vincristine
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

# Vincristine: From Hematologic Malignancies to Ganglioneuroblastoma

## One-Sentence Summary

> Vincristine is a vinca alkaloid chemotherapy agent traditionally used as a backbone drug in combination regimens for hematologic malignancies and pediatric solid tumors.
> The TxGNN model predicts it may be effective for **Ganglioneuroblastoma**,
> with **4 clinical trials** and **6 publications** currently identified as supporting context, though none are drug-specific pivotal trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore — no local label text available. (Vincristine is a well-established cytotoxic agent used across hematologic malignancies and pediatric solid tumors; Singapore-specific indication text could not be sourced.) |
| Predicted New Indication | Ganglioneuroblastoma (disease) |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed original mechanism of action (MOA) data is currently marked as a data gap in this Evidence Pack. Based on the repurposing rationale accompanying the prediction, however, Vincristine is known to be a **vinca alkaloid** that inhibits tubulin polymerization, arresting cell division at metaphase. This antimitotic mechanism is the pharmacological basis for its long-standing role as a backbone agent in induction chemotherapy regimens for neuroblastic tumors (e.g., OPEC/CVP-type regimens containing "O/V").

Ganglioneuroblastoma is a tumor on the neuroblastic tumor spectrum — sharing lineage and biology with neuroblastoma, for which vincristine-containing regimens are already standard of care. Because ganglioneuroblastoma retains an undifferentiated, rapidly proliferating neuroblastic cell component alongside more mature ganglion cells, the antimitotic mechanism of vincristine is mechanistically applicable to the malignant fraction of the tumor, even though ganglioneuroblastoma itself is not a formally labeled indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03786783](https://clinicaltrials.gov/study/NCT03786783) | Phase 2 | Active, not recruiting | 42 | Pilot induction regimen adding dinutuximab + sargramostim to chemotherapy for newly diagnosed high-risk neuroblastoma; vincristine not the primary study drug (Grade C relevance) |
| [NCT03126916](https://clinicaltrials.gov/study/NCT03126916) | Phase 3 | Recruiting | 750 | Tests 131I-MIBG or lorlatinib added to intensive standard therapy for high-risk neuroblastoma/ganglioneuroblastoma; vincristine is part of the standard-therapy backbone (Grade B) |
| [NCT01798004](https://clinicaltrials.gov/study/NCT01798004) | Phase 1 | Completed | 150 | Busulfan/melphalan myeloablative consolidation following vincristine-containing induction chemotherapy for newly diagnosed high-risk neuroblastoma (Grade B) |
| [NCT06172296](https://clinicaltrials.gov/study/NCT06172296) | Phase 3 | Recruiting | 478 | Adds dinutuximab to intensive multimodal therapy (including vincristine-based induction) for high-risk neuroblastoma (Grade B) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31342649](https://pubmed.ncbi.nlm.nih.gov/31342649/) | 2019 | Cohort/prospective trial (JN-L-10) | Pediatric Blood & Cancer | Japan Children's Cancer Group study using image-defined risk factors to guide surgical timing in low-risk neuroblastoma |
| [8888754](https://pubmed.ncbi.nlm.nih.gov/8888754/) | 1996 | Case report | J Pediatr Hematol Oncol | Gastric involvement in an infant with multifocal ganglioneuroblastoma |
| [7421294](https://pubmed.ncbi.nlm.nih.gov/7421294/) | 1980 | Case report | J Thorac Cardiovasc Surg | 31 patients with intrathoracic ganglioneuroblastoma treated with resection, radiotherapy, and/or chemotherapy |
| [3071124](https://pubmed.ncbi.nlm.nih.gov/3071124/) | 1988 | Case report | Acta Urol Jpn | Multimodality treatment of adult adrenal ganglioneuroblastoma with regional lymph node metastasis |
| [8255850](https://pubmed.ncbi.nlm.nih.gov/8255850/) | 1993 | Case report | Postgrad Med J | Spinal ganglioneuroblastoma achieving complete remission with doxorubicin/vincristine/cyclophosphamide/etoposide/ifosfamide/cisplatin |
| [15701990](https://pubmed.ncbi.nlm.nih.gov/15701990/) | 2005 | Case report | J Pediatr Hematol Oncol | Ganglioneuroblastoma presenting with obstructive jaundice, treated with cisplatin/pirarubicin/cyclophosphamide/vincristine |

---

## Singapore Market Information

Currently no marketing authorizations registered in Singapore (`market_status`: 未上市, 0 licenses on file).

---

## Cytotoxicity

Vincristine is a conventional cytotoxic chemotherapy agent, meeting the antineoplastic classification criteria via its vinca alkaloid mechanism and its role as a standard chemotherapy backbone described in the repurposing rationale.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Vinca alkaloid class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between vincristine's antimitotic action and the proliferative neuroblastic component of ganglioneuroblastoma is well supported, and vincristine is already embedded as background therapy in ongoing/completed high-risk neuroblastoma trials — but no trial or publication directly and prospectively tests vincristine specifically for ganglioneuroblastoma as a standalone indication.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent package insert data (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Confirmed mechanism of action (MOA) documentation from DrugBank — currently a **High** severity data gap (DG002)
- Formal drug-disease interaction and toxicity data specific to ganglioneuroblastoma populations (pediatric neurotoxicity considerations)
- Clarification of Singapore regulatory pathway, given the drug is currently unmarketed locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

