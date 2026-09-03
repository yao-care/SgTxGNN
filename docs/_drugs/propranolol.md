---
layout: default
title: Propranolol
parent: 僅模型預測 (L5)
nav_order: 827
evidence_level: L5
indication_count: 10
---

# Propranolol
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

# Propranolol: From Beta-Blocker Cardiovascular Therapy to Infantile Hemangioma (Breast Capillary Subtype)

## One-Sentence Summary

Propranolol is a non-selective beta-adrenergic receptor antagonist classically used in cardiovascular and neurological conditions. This Evidence Pack contains **10 TxGNN-predicted indications**; the highest raw TxGNN score points to an ultra-rare hereditary myopathy with no mechanistic or clinical support, but the most **evidence-backed and actionable** candidate is **breast capillary hemangioma**, part of the well-established infantile hemangioma spectrum for which propranolol is already an approved first-line therapy (Hemangiol®). This candidate is supported by **2 clinical trials** (including a completed n=500 post-marketing surveillance study) and **substantial published literature** (10+ relevant papers, including 1 RCT), earning an **L2 evidence level** and a **Proceed with Guardrails** recommendation.

> ⚠️ Note: TxGNN's single highest-scoring prediction in this pack ("distal myopathy, Tateyama type," score 99.40%) has **zero supporting clinical trials or literature** and is scored **L5 / Hold** — a reminder that raw model score alone does not indicate clinical plausibility. See "Full List of Predicted Indications" below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is not currently registered/marketed in Singapore (0 licenses on file); classically known as a non-selective beta-adrenergic antagonist |
| Predicted New Indication | Breast capillary hemangioma (infantile hemangioma spectrum) |
| TxGNN Prediction Score | 98.90% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed structured mechanism-of-action data for this record is flagged as a gap (see DG002). However, the evidence pack's own repurposing rationales consistently describe propranolol's mechanism as **non-selective β-adrenergic receptor blockade**, which in vascular endothelial tissue produces vasoconstriction, downregulation of VEGF/bFGF-driven angiogenesis, and induction of endothelial apoptosis. This anti-angiogenic mechanism is already **FDA-approved and clinically established for infantile hemangioma** (branded Hemangiol®), following its serendipitous discovery in this population.

Breast capillary hemangioma, along with two related predictions in this pack (intramuscular hemangioma, breast epithelioid hemangioma), represents the same underlying disease biology — infantile/capillary hemangioma occurring at different anatomic sites — rather than three independent novel indications. This convergence across multiple TxGNN outputs strengthens confidence: the model is consistently recognizing propranolol's established anti-angiogenic profile, and the "new" element is anatomic-site specificity (breast) rather than an unprecedented biological mechanism.

By contrast, several other high-scoring predictions in this pack (e.g., Tateyama-type distal myopathy, congenital myopathy with excess thin filaments, chondroma) involve structurally or embryologically unrelated tissue (skeletal muscle genetic disease, cartilage) with **no known mechanistic pathway** connecting them to beta-blockade — these are flagged Hold and should not be pursued without independent hypothesis generation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04105517](https://clinicaltrials.gov/study/NCT04105517) | N/A (post-marketing) | Completed | 500 | Post-marketing surveillance of Hemangiol (propranolol) prescribing in proliferative infantile hemangioma requiring systemic treatment — largest and most direct real-world dataset in this cluster |
| [NCT02732678](https://clinicaltrials.gov/study/NCT02732678) | Phase 1/2 | Unknown | 24 | Dose-finding of propranolol combined with metronomic cyclophosphamide in angiosarcoma/vascular tumors, based on beta-adrenergic receptor expression rationale shared with hemangioma biology |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34719577](https://pubmed.ncbi.nlm.nih.gov/34719577/) | 2022 | RCT | Biological & Pharmaceutical Bulletin | Randomized, double-blind trial of topical propranolol gel (0/1/5%) for infantile hemangioma; dose-dependent reduction in lesion redness |
| [38196847](https://pubmed.ncbi.nlm.nih.gov/38196847/) | 2024 | Cohort | Plastic and Reconstructive Surgery Global Open | Long-term outcomes of infantile hemangioma specifically in the breast — directly relevant to predicted site |
| [29333831](https://pubmed.ncbi.nlm.nih.gov/29333831/) | 2018 | Case Report | Archivos Argentinos de Pediatría | Case of mammary hemangioma presenting as apparent mastitis in an infant |
| [32647928](https://pubmed.ncbi.nlm.nih.gov/32647928/) | 2020 | Cohort/Meta-analysis | Pediatric Surgery International | Meta-analysis: beta-antagonist combined with laser therapy for infantile hemangioma |
| [35512856](https://pubmed.ncbi.nlm.nih.gov/35512856/) | 2022 | Cohort | Journal of Pharmacological Sciences | Prospective pilot study of topical propranolol cream, safety/efficacy in infantile hemangioma |
| [20615772](https://pubmed.ncbi.nlm.nih.gov/20615772/) | 2011 | Cohort | JPRAS | Determined minimal effective dose/duration of propranolol for accelerated hemangioma involution |
| [41266952](https://pubmed.ncbi.nlm.nih.gov/41266952/) | 2025 | Cohort | Pediatric Dermatology | Real-world evolution of trunk/extremity infantile hemangiomas, including breast-area lesions (n=449) |
| [23266923](https://pubmed.ncbi.nlm.nih.gov/23266923/) | 2013 | Consensus Guideline | Pediatrics | Landmark consensus conference establishing propranolol initiation/monitoring protocols for infantile hemangioma |
| [34419523](https://pubmed.ncbi.nlm.nih.gov/34419523/) | 2021 | Review | Journal of the American Academy of Dermatology | Management review confirming propranolol as first-line IH therapy |
| [36243426](https://pubmed.ncbi.nlm.nih.gov/36243426/) | 2022 | Review | Dermatologic Clinics | Overview of infantile hemangioma pathogenesis and propranolol's central treatment role |

## Singapore Market Information

Propranolol is currently **not marketed** in Singapore under this record (0 registered authorizations found in the evidence pack). No product listings are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

## Full List of Predicted Indications (Context)

For transparency, all 10 TxGNN-predicted indications in this pack are summarized below, ranked by model score:

| Rank | Predicted Disease | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 1 | Distal myopathy, Tateyama type | 99.40% | L5 | Hold |
| 2 | Congenital myopathy with excess of thin filaments | 99.30% | L5 | Hold |
| 3 | Hypertrophic cardiomyopathy (athletic training-induced) | 99.17% | L4 | Research Question |
| 4 | Chondroma | 99.14% | L5 | Hold |
| 5 | Cirrhotic cardiomyopathy | 99.12% | L3 | Research Question |
| 6 | Cardiomyopathy (general/HCM) | 99.12% | L2 | Proceed with Guardrails |
| 7 | Intramuscular hemangioma | 98.97% | L3 | Research Question |
| 8 | Maffucci syndrome | 98.97% | L4 | Research Question |
| 9 | Breast epithelioid hemangioma | 98.91% | L3 | Research Question |
| 10 | **Breast capillary hemangioma** | 98.90% | **L2** | **Proceed with Guardrails** |

Two candidates — cardiomyopathy (rank 6) and breast capillary hemangioma (rank 10) — reach L2/Proceed with Guardrails status and warrant priority follow-up over the raw top-ranked score.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Breast capillary hemangioma sits within propranolol's already-validated anti-angiogenic mechanism for infantile hemangioma, supported by a completed 500-patient real-world study and a body of cohort/RCT literature — but no trial has specifically isolated the breast anatomic site, so guardrails are warranted before treating this as a standalone new indication.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent package insert data (warnings, contraindications) — currently a blocking data gap (DG001)
- Formal MOA documentation from DrugBank (DG002)
- Site-specific case series or registry data confirming efficacy/safety of propranolol specifically for breast-localized capillary hemangioma (vs. extrapolation from generalized infantile hemangioma data)
- Given Singapore market status shows zero current registrations, confirm regulatory pathway/registration status before any clinical use planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

