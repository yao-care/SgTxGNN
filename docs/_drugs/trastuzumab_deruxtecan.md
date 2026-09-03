---
layout: default
title: Trastuzumab Deruxtecan
parent: 僅模型預測 (L5)
nav_order: 1003
evidence_level: L5
indication_count: 10
---

# Trastuzumab Deruxtecan
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

# Trastuzumab Deruxtecan: From HER2-Targeted Oncology Use to Drug-Induced Osteoporosis (Low-Confidence Signal)

## One-Sentence Summary

Trastuzumab deruxtecan (T-DXd) is a HER2-targeted antibody-drug conjugate (ADC); its original approved oncology indication is not recorded in this evidence pack.
TxGNN's top-ranked prediction is **Drug-Induced Osteoporosis**, but the model's own rationale flags this as a likely noise prediction, and there is currently **no clinical trial or literature evidence** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no Singapore license on record; not specified in evidence pack) |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured MOA field. However, the evidence pack's own repurposing rationale consistently describes trastuzumab deruxtecan as a HER2-targeted ADC carrying a topoisomerase I inhibitor payload (deruxtecan).

There is no established pharmacological link between HER2/topoisomerase I inhibition and bone remodeling or osteoclast pathways. The evidence pack explicitly characterizes this specific prediction as a high-scoring but mechanistically unsupported output of the TxGNN model — i.e., likely embedding noise rather than a biologically grounded repurposing hypothesis. No clinical trial or literature evidence has been found to corroborate a therapeutic role for T-DXd in osteoporosis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Trastuzumab deruxtecan is not currently marketed in Singapore; no registration records are available (total licenses: 0).

---

## Cytotoxicity

Trastuzumab deruxtecan is an antineoplastic antibody-drug conjugate, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ADC) with cytotoxic topoisomerase I inhibitor payload (deruxtecan) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All top 10 TxGNN-predicted indications for this drug (osteoporosis, diabetic retinopathy variants, bronchitis, diabetic cataract, rare pediatric/testicular tumors, ductular proliferation) lack clinical trial or literature support, and most are explicitly flagged in the evidence pack as lacking any mechanistic plausibility. One prediction ("ductal or ductular proliferation") returned 20 literature hits, but only one is drug-relevant — a case report of deruxtecan-induced Fanconi syndrome (PMID 37492824), which is a **safety signal, not efficacy evidence**, and argues against rather than for this indication.

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001: HSA/manufacturer package insert warnings and contraindications
- Resolve High-priority data gap DG002: confirmed mechanism of action from DrugBank
- Confirmed original approved indication(s), since none are currently on record
- If any repurposing signal is pursued, a dedicated safety review of ADC-related renal/tubular toxicity (Fanconi syndrome) given the case report identified above
- Re-screen this candidate once safety and MOA data gaps are closed, as current evidence does not support advancing beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

