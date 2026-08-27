---
layout: default
title: Potassium Bicarbonate
parent: 僅模型預測 (L5)
nav_order: 671
evidence_level: L5
indication_count: 10
---

# Potassium Bicarbonate
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

Using the evidence pack as provided (no fabricated data), here is the evaluation report:

---

# Potassium Bicarbonate: From Electrolyte/Alkalinizing Supplement to Gastroduodenitis

## One-Sentence Summary

> Potassium bicarbonate is a potassium salt / systemic-urinary alkalinizing agent; no approved-indication record exists in this evidence pack because the drug is **not currently registered or marketed in Singapore**.
> The TxGNN model's top-ranked prediction is **Gastroduodenitis**, with a very high similarity score (**99.72%**), but this prediction is currently supported by **0 clinical trials** and **0 publications**.
> Given the complete absence of clinical or literature corroboration, this is a pure knowledge-graph link prediction that has not yet been validated by any external evidence source.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no HSA/TFDA license or approved-indication record found (drug not marketed) |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for potassium bicarbonate in this evidence pack. Based on the drug's known pharmacological class, potassium bicarbonate is a potassium salt used as an electrolyte supplement and as a systemic/urinary alkalinizing agent; this general classification is consistent with how it appears elsewhere in this same evidence pack (e.g., as the mechanistic basis cited for the "acute urate nephropathy" candidate, rank 9).

No original indication data could be extracted either, because the drug has no active license or registration record in this jurisdiction (0 total licenses, market status "not marketed"). This means there is no regulatory-approved indication to anchor a mechanistic comparison against the predicted new indication.

For Gastroduodenitis specifically, the TxGNN model assigns the highest similarity score among all ten candidates (99.72%, global rank 4,366), but this is a pure knowledge-graph link prediction with **no supporting clinical trials or literature** (0 results returned from ClinicalTrials.gov, ICTRP, and PubMed queries). The only plausible mechanistic narrative that can be constructed is a weak "gastric acid neutralization / antacid-like" hypothesis — i.e., potassium bicarbonate, like other bicarbonate salts, could theoretically provide transient buffering of gastric acid. However, this is not a recognized or evidence-based treatment pathway for gastroduodenitis, and no external data source corroborates it. This is reflected in the evidence-level classification of L5 (model prediction only, no actual studies) and decision stage S0.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Potassium bicarbonate (DrugBank ID: DB11098) currently has **no registered product licenses in Singapore** (total licenses: 0; market status: not marketed). No authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: the drug-level data gap log flags this as a blocking issue — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (Gastroduodenitis) has a high TxGNN similarity score (99.72%) but **zero clinical trial or literature support** — this is evidence level L5 (model prediction only), decision stage S0, which does not meet the bar to advance toward any development or research pathway.
- Two data gaps block further progression: **DG001 (Blocking)** — TFDA/HSA package insert warnings and contraindications are missing, which prevents entry into the S1 safety pre-screen; and **DG002 (High)** — mechanism of action data is missing, which prevents any meaningful mechanistic-relevance analysis.

**To proceed, the following is needed:**
- Obtain the official HSA/TFDA package insert (warnings, contraindications, drug interactions) to resolve DG001 and unblock the S1 safety pre-screen
- Obtain DrugBank/primary-literature mechanism of action (MOA) data to resolve DG002
- Generate at least preliminary clinical or literature evidence specifically linking potassium bicarbonate to gastroduodenitis before any evidence-level upgrade is considered
- Confirm current and historical Singapore (HSA) registration status, since no license record currently exists
- Consider re-evaluating other TxGNN candidates in this evidence pack with stronger supporting rationale — notably **rank 9, "acute urate nephropathy"** (evidence level L4, decision stage S1, recommendation "Research Question"), which has an established pharmacological basis (potassium bicarbonate as a urinary alkalinizer to increase uric acid solubility), unlike the top-ranked Gastroduodenitis candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

