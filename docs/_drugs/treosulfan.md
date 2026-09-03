---
layout: default
title: Treosulfan
parent: 僅模型預測 (L5)
nav_order: 1008
evidence_level: L5
indication_count: 10
---

# Treosulfan
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

# Treosulfan: From No Approved Indication to Diabetic Cataract (Unsupported Prediction)

## One-Sentence Summary

Treosulfan is an alkylating agent with no approved indication currently recorded in this evidence pack (typically used as conditioning chemotherapy prior to stem cell transplant). The TxGNN model predicts possible efficacy for **Diabetic Cataract** and several other cataract subtypes, but **no clinical trials, no literature, and no mechanistic support** exist for this direction — and it conflicts with known alkylating-agent toxicology (alkylating agents are a recognized *cause* of drug-induced cataracts, not a treatment).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in current data) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| Singapore Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Treosulfan in this evidence pack. Based on known pharmacology, treosulfan is a bifunctional alkylating agent, a drug class generally used for its cytotoxic/myeloablative effects (e.g., pre-transplant conditioning), not for ocular or metabolic disease.

Critically, this prediction runs counter to established toxicology: alkylating agents are a **known risk factor for drug-induced cataract formation**, not a treatment for it. The model's rationale field explicitly flags this as a likely graph-embedding false positive — the predicted direction is opposite to the drug's known toxicological effect. The same caveat applies to all ten ranked predictions (diabetic cataract, cortical cataract, nuclear senile cataract, craniostenosis cataract, diabetes-associated cataract, tetanic cataract, mature/immature cataract, diabetic retinopathy, senile cataract) — none have any supporting mechanistic, clinical, or literature evidence.

There is no basis at this time to support a plausible pharmacological link between treosulfan and any cataract or retinopathy indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Treosulfan currently has no registered products in Singapore (0 licenses on file); market status is 未上市 (Not marketed).

---

## Cytotoxicity

Treosulfan is a conventional cytotoxic alkylating agent, warranting inclusion of this section despite the absence of a confirmed indication in this dataset.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Alkylating agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications are TxGNN score-only (L5) with zero clinical trials, zero literature, and no plausible mechanistic rationale — several directly contradict treosulfan's known toxicological profile as a cataractogenic alkylating agent. This candidate should not advance past S0.

**To proceed, the following is needed:**
- Confirmed original/approved indication text for treosulfan (currently missing from regulatory data)
- Verified MOA data from DrugBank (DG002)
- TFDA/HSA package insert warnings and contraindications (DG001, Blocking)
- Independent toxicological review addressing the drug-induced cataract risk before any further evaluation of ophthalmic indications
- If this candidate is to be pursued at all, prioritize re-scoring or excluding predictions that contradict known adverse-effect profiles
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

