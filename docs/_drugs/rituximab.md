---
layout: default
title: Rituximab
parent: 僅模型預測 (L5)
nav_order: 868
evidence_level: L5
indication_count: 10
---

# Rituximab
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

# Rituximab: From [Original Indication Data Unavailable] to Follicular Lymphoma

## One-Sentence Summary

> Rituximab is a chimeric anti-CD20 monoclonal antibody; its original approved indication is not captured in this Evidence Pack (Singapore registration and label data are both absent).
> The TxGNN model predicts it may be effective for **Follicular Lymphoma**, with **50 clinical trials** and **20 publications** currently identified as supporting evidence.
> Notably, the underlying rationale itself indicates this is not a truly novel indication — rituximab is already the established anti-CD20 backbone therapy for follicular lymphoma — making this the strongest mechanism-to-clinical-evidence match among all 10 candidates in this pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — Rituximab is not currently registered in Singapore; no local label/indication text was captured in this Evidence Pack |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 96.08% |
| Evidence Level | L1 |
| Singapore Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in the structured drug record. Based on the supporting rationale provided with this prediction, rituximab is a chimeric monoclonal antibody directed against the CD20 antigen expressed on the surface of normal and malignant B lymphocytes. It is understood to eliminate CD20-positive B cells through antibody-dependent cellular cytotoxicity (ADCC), complement-dependent cytotoxicity (CDC), and direct induction of apoptosis.

Follicular lymphoma is a CD20-positive B-cell malignancy in more than 90% of cases, so the anti-CD20 mechanism maps directly onto the biology of this disease. The evidence pack's own rationale explicitly notes that this is **not a novel repurposing hypothesis but rather a confirmation of an already well-established, guideline-standard use of rituximab** — it represents the strongest and most internally consistent mechanism-to-clinical-evidence case among the candidates reviewed.

Because no formal MOA field or original indication field was populated for this drug in the current pack, this section should be read as a description of known pharmacology inferred from the supporting literature/trial rationale rather than a verified structured drug attribute.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01476787](https://clinicaltrials.gov/study/NCT01476787) | Phase 3 | Completed | 1030 | RELEVANCE trial: rituximab + lenalidomide vs. rituximab + chemotherapy in previously untreated follicular lymphoma (Grade A direct evidence) |
| [NCT01650701](https://clinicaltrials.gov/study/NCT01650701) | Phase 3 | Completed | 1030 | RELEVANCE companion study (combined N=1000+ analysis) of rituximab-lenalidomide vs. rituximab-chemotherapy in untreated FL |
| [NCT00460109](https://clinicaltrials.gov/study/NCT00460109) | Phase 2 | Completed | 24 | Denileukin diftitox + rituximab in previously untreated follicular B-cell NHL (Grade B) |
| [NCT01701232](https://clinicaltrials.gov/study/NCT01701232) | Phase 3 | Completed | 174 | Biosimilar rituximab (BCD-020) vs. MabThera monotherapy in CD20+ indolent NHL |
| [NCT01938001](https://clinicaltrials.gov/study/NCT01938001) | Phase 3 | Completed | 358 | Rituximab + lenalidomide vs. rituximab + placebo in relapsed/refractory indolent lymphoma (incl. FL) |
| [NCT06097364](https://clinicaltrials.gov/study/NCT06097364) | Phase 3 | Active, not recruiting | 733 | OLYMPIA-2: odronextamab + chemo vs. rituximab + chemo in untreated follicular lymphoma |
| [NCT05409066](https://clinicaltrials.gov/study/NCT05409066) | Phase 3 | Active, not recruiting | 549 | EPCORE FL-1: epcoritamab + rituximab/lenalidomide (R2) vs. R2 alone in relapsed/refractory FL |
| [NCT04224493](https://clinicaltrials.gov/study/NCT04224493) | Phase 3 | Recruiting | 612 | Symphony-1: tazemetostat vs. placebo added to lenalidomide + rituximab in relapsed/refractory FL |
| [NCT00006721](https://clinicaltrials.gov/study/NCT00006721) | Phase 3 | Active, not recruiting | 571 | CHOP + rituximab vs. CHOP + tositumomab in newly diagnosed follicular NHL |
| [NCT00363636](https://clinicaltrials.gov/study/NCT00363636) | Phase 3 | Terminated | 340 | Galiximab + rituximab vs. rituximab + placebo in relapsed/refractory follicular NHL |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40306831](https://pubmed.ncbi.nlm.nih.gov/40306831/) | 2025 | RCT | The Lancet Haematology | Long-term results: early rituximab monotherapy vs. watchful waiting improved time to next treatment in advanced, asymptomatic, low-tumour-burden FL |
| [33249059](https://pubmed.ncbi.nlm.nih.gov/33249059/) | 2021 | Guideline/Review | Annals of Oncology | ESMO Clinical Practice Guidelines for newly diagnosed and relapsed follicular lymphoma |
| [28628883](https://pubmed.ncbi.nlm.nih.gov/28628883/) | 2017 | Review | Cancer Treatment Reviews | Review of arguments for and against rituximab maintenance therapy in FL |
| [23233615](https://pubmed.ncbi.nlm.nih.gov/23233615/) | 2012 | Review | Hematology ASH Education Program | Role of "watch and wait" for low-tumor-burden FL in the rituximab era |
| [36345167](https://pubmed.ncbi.nlm.nih.gov/36345167/) | 2022 | Systematic Review/Meta-analysis | J Clin Pharm Ther | Efficacy/safety of rituximab biosimilars vs. reference product as first-line treatment in low-tumour-burden FL |
| [21958083](https://pubmed.ncbi.nlm.nih.gov/21958083/) | 2012 | Review | Leukemia & Lymphoma | Facts and controversies of rituximab maintenance in follicular NHL |
| [31831752](https://pubmed.ncbi.nlm.nih.gov/31831752/) | 2019 | Review (Primer) | Nature Reviews Disease Primers | Comprehensive overview of follicular lymphoma biology and treatment |
| [36255040](https://pubmed.ncbi.nlm.nih.gov/36255040/) | 2022 | Review | American Journal of Hematology | 2023 update on FL diagnosis and management |
| [37061956](https://pubmed.ncbi.nlm.nih.gov/37061956/) | 2023 | Review | Leukemia & Lymphoma | Update on FL biology and optimal therapy |
| [35908982](https://pubmed.ncbi.nlm.nih.gov/35908982/) | 2023 | Review | Blood Reviews | Review of the path toward curative treatment approaches for FL |

---

## Singapore Market Information

Rituximab currently has **no marketing authorization records in Singapore** in this Evidence Pack (market status: 未上市 / Not Marketed; total registrations: 0). No product name, dosage form, or approved indication text is available for local review.

---

## Cytotoxicity

**This drug is antineoplastic** — rituximab is used to treat CD20-positive B-cell malignancies (e.g., follicular lymphoma) and is classified as a targeted biologic anticancer agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy (anti-CD20 monoclonal antibody) — not a conventional cytotoxic chemotherapeutic |
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
Multiple completed and ongoing Phase 3 trials (including the pivotal RELEVANCE trial, n=1030) directly support rituximab-based regimens as standard care in follicular lymphoma, and the drug's mechanism (anti-CD20 targeting) maps precisely onto FL biology. The evidence itself indicates this is a confirmatory finding of an already-established indication rather than a novel hypothesis, which strengthens confidence but also means the primary value here is validation, not discovery of a new use.

**To proceed, the following is needed:**
- TFDA/HSA product label (warnings, contraindications) — currently a **Blocking** data gap preventing any formal safety (S1) assessment
- Structured mechanism of action (MOA) data from DrugBank
- Singapore-specific registration and dosage form information, since the drug is currently unregistered locally
- Drug-drug interaction (DDI) data, currently unavailable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

