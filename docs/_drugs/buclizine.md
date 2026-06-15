---
layout: default
title: Buclizine
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
---

# Buclizine
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

# Buclizine: From Antihistaminic Applications to Allergic Urticaria

## One-Sentence Summary

Buclizine is a first-generation piperazine-class H1 antihistamine historically used for motion sickness, nausea, and allergic conditions, though no approved indications are on record in the Singapore regulatory database.
The TxGNN model predicts it may be effective for **Allergic Urticaria**,
with **0 clinical trials** and **1 publication** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Singapore regulatory records (drug not marketed) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 98.08% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological information, Buclizine is a piperazine-class first-generation antihistamine whose antihistaminic activity was documented as early as 1956. Its H1 receptor antagonism underlies its historic uses in motion sickness, nausea control, and allergic pruritus.

Allergic urticaria is driven by mast cell degranulation and subsequent histamine release, making H1 receptor blockade the cornerstone of first-line treatment according to international guidelines (e.g., EAACI/GA²LEN). The mechanistic alignment between buclizine's antihistaminic action and the histamine-dependent pathophysiology of allergic urticaria is direct and strong — this is effectively a class effect with robust external support from the broader antihistamine literature, even though buclizine-specific modern controlled data is absent.

However, it is critical to note that the TxGNN score of 98.08% reflects algorithmic confidence driven largely by pharmacological class membership. The absence of modern randomised controlled trials and the drug's unavailability in the Singapore market mean that the prediction, while mechanistically sound, requires dedicated clinical evaluation before it can be considered actionable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [13294975](https://pubmed.ncbi.nlm.nih.gov/13294975/) | 1956 | Early Clinical Evaluation | The Journal of Allergy | Initial toxicologic and clinical appraisal of buclizine as a new antihistaminic compound (non-controlled; no abstract available) |

---

## Singapore Market Information

Buclizine has no registered products in Singapore. No authorisation records are available from the Health Sciences Authority (HSA).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
Although the mechanistic basis for buclizine in allergic urticaria is scientifically plausible — H1 antagonism directly counters the histamine-mediated cascade responsible for urticarial wheals — the totality of evidence consists of a single early-stage, non-controlled clinical paper from 1956, and the drug carries no Singapore regulatory registration, leaving safety documentation incomplete.

**To proceed, the following is needed:**
- Retrieval and review of the full prescribing information / package insert for buclizine to assess safety warnings, contraindications, and drug interactions
- Detailed mechanism of action data via DrugBank API query (DG002 remediation)
- Modern comparative observational studies or systematic reviews evaluating buclizine versus second-generation H1 antihistamines (e.g., cetirizine, loratadine) in urticaria
- Assessment of whether buclizine's sedating (first-generation) profile offers any clinical advantage or disadvantage over currently marketed antihistamines in Singapore
- Regulatory pathway assessment for HSA market entry, contingent on accumulation of sufficient clinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

