---
layout: default
title: Oxybutynin
parent: 僅模型預測 (L5)
nav_order: 741
evidence_level: L5
indication_count: 10
---

# Oxybutynin
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

# Oxybutynin: From Overactive Bladder to Restless Legs Syndrome

## One-Sentence Summary

> Oxybutynin is a well-established antimuscarinic agent used to treat overactive bladder and urinary incontinence caused by detrusor overactivity.
> The TxGNN model predicts it may be effective for **Restless Legs Syndrome**, with a very high prediction score (**99.74%**),
> but currently **no clinical trials or published literature** support this specific link — the signal is model-based only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Overactive bladder / urinary incontinence (detrusor overactivity) — based on general pharmacological knowledge; no Singapore-specific approved indication text is available |
| Predicted New Indication | Restless Legs Syndrome |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack. Based on established pharmacological knowledge, oxybutynin is a synthetic antimuscarinic (anticholinergic) agent that antagonizes M3 (and to a lesser extent M1) muscarinic receptors, relaxing bladder detrusor smooth muscle. It is widely used for overactive bladder, urge incontinence, and neurogenic bladder.

Restless Legs Syndrome (RLS), however, is primarily driven by central dopaminergic dysfunction and abnormal iron metabolism — a pathophysiology that does not have a known mechanistic link to peripheral/central anticholinergic activity. According to the model's own repurposing rationale, there is **no established pharmacological connection** between oxybutynin's anticholinergic action and RLS pathology; the prediction reflects the TxGNN score alone, without any supporting clinical or mechanistic evidence.

Given this gap, the high prediction score should be interpreted as a hypothesis-generating signal rather than a validated therapeutic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Oxybutynin currently has no marketing authorization on record in Singapore (0 registrations; market status: 未上市/Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for oxybutynin–RLS is high, but there is zero clinical trial or literature support, and the underlying mechanistic rationale is explicitly weak (anticholinergic action vs. dopaminergic/iron-metabolism pathology). This is a pure model prediction (L5) and does not meet the evidence bar to advance.

**To proceed, the following is needed:**
- Preclinical or mechanistic studies exploring any plausible anticholinergic pathway in RLS
- At minimum an observational/case-level signal before considering trial design
- Confirmed original indication and approved labeling text (Singapore or reference market) for this drug, since no local registration data exists
- Formal MOA documentation (currently "[Data Gap]")

**Note:** Other TxGNN candidates for oxybutynin in this evidence pack carry substantially stronger evidence and may warrant separate evaluation — notably *low compliance bladder* (2 clinical trials incl. a Phase 3, 20 literature items, L4) and *insomnia* (5 clinical trials incl. two Phase 3, L4), both mechanistically closer to oxybutynin's known urological/anticholinergic effects than RLS.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

