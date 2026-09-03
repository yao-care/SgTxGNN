---
layout: default
title: Pralidoxime
parent: 僅模型預測 (L5)
nav_order: 807
evidence_level: L5
indication_count: 10
---

# Pralidoxime
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

# Pralidoxime: From Organophosphate/Carbamate Poisoning to Bronchitis

## One-Sentence Summary

Pralidoxime is an acetylcholinesterase (AChE) reactivator historically used as an antidote for organophosphate and carbamate poisoning. The TxGNN model predicts it may be effective for **Bronchitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags the mechanistic link as weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally registered; historically used as an antidote for organophosphate/carbamate poisoning (AChE reactivation) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 95.70% |
| Evidence Level | L5 |
| Singapore Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from DrugBank (marked as a data gap). However, based on the model's own repurposing rationale, Pralidoxime is known to act as an AChE reactivator: it reverses the phosphorylation of acetylcholinesterase caused by organophosphate or carbamate toxins, restoring normal enzyme function. It does not act directly on muscarinic receptors or bronchial smooth muscle.

The proposed link to bronchitis stems from the fact that organophosphate poisoning itself can cause cholinergic overactivation, leading to bronchospasm and excessive bronchial secretions — symptoms that overlap superficially with bronchitis. However, this is a toxicological *symptom* of poisoning, not evidence that Pralidoxime has a therapeutic pharmacological effect on bronchitis as a primary disease. The causal direction is reversed: Pralidoxime treats the underlying poisoning, it does not treat airway inflammation.

Given this, the mechanistic connection between the original use (antidote for AChE-inhibitor poisoning) and the predicted indication (bronchitis) is considered weak. This is consistent with the evidence pack's own assessment, which explicitly notes the mechanistic link is thin and the causal direction is misapplied. No clinical or literature evidence currently exists to independently support this prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Pralidoxime currently has no marketing authorizations on record (market status: 未上市 / Not Marketed; total registrations: 0). No product license data is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: A Blocking-severity data gap exists — TFDA/HSA package insert warnings and contraindications have not yet been retrieved. This must be resolved before any safety-related decision can be made.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications for Pralidoxime — including the top-ranked candidate, bronchitis — sit at Evidence Level L5 (model prediction only) with no supporting clinical trials or literature (decision stage S0). The mechanistic rationale for bronchitis is weak and directionally inconsistent (poisoning symptom vs. therapeutic indication), and a Blocking-severity safety data gap (missing package insert warnings/contraindications) currently prevents even an initial safety screen (S1).

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (resolves Blocking gap DG001)
- Verified mechanism of action data from DrugBank API (resolves High-priority gap DG002)
- Confirmation of the drug's formally approved indication text, since no local registration/license data currently exists
- At minimum, preclinical or mechanistic literature supporting a plausible pharmacological pathway between AChE reactivation and bronchitis before advancing past S0
- Continued monitoring for clinical trial or publication signals, as none currently exist for any of the ten predicted indications in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

