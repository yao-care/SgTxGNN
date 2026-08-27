---
layout: default
title: Fentanyl
parent: 僅模型預測 (L5)
nav_order: 421
evidence_level: L5
indication_count: 10
---

# Fentanyl
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

Using the provided Evidence Pack, here is the evaluation report for Fentanyl.

---

# Fentanyl: From Opioid Analgesia to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a potent synthetic opioid, generally used for the management of severe and breakthrough pain and as an anesthetic adjunct. The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic assessment flags the pathway link as biologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded — no `original_indications` or local regulatory filings are available for this drug in the current dataset. (General pharmacological class: opioid analgesic for severe/chronic pain and anesthesia) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for fentanyl in this evidence pack (data gap DG002). Based on general pharmacological knowledge, fentanyl is a synthetic full agonist at the μ-opioid receptor, and its efficacy in severe/chronic pain management and anesthesia is well established.

The predicted new indication, nephrogenic syndrome of inappropriate antidiuresis (NSIAD), is a rare congenital disorder caused by constitutive, ligand-independent activation of the vasopressin V2 receptor (AVPR2) — it is not driven by excess ADH secretion. Opioids, including fentanyl, are known to promote non-osmotic ADH release, which is sometimes cited as a contributing *risk factor* for SIAD-like hyponatremia in perioperative settings. This is mechanistically distinct from NSIAD, whose pathology is receptor-intrinsic and independent of circulating ADH/opioid signaling.

The evidence pack's own mechanistic rationale explicitly notes there is no known overlap between the μ-opioid receptor pathway and the AVPR2 mutation pathway underlying NSIAD, and characterizes this prediction as a likely statistical artifact of the TxGNN knowledge-graph embedding rather than a pharmacologically grounded hypothesis. Combined with the complete absence of clinical trials or literature for this pairing, the mechanistic case does not currently support prioritizing this candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Detailed safety data (key warnings, contraindications, drug-drug interactions) has not yet been retrieved for fentanyl in this evidence pack — this is flagged as a **blocking** data gap (DG001: TFDA/HSA label warnings and contraindications), which prevents entry into the S1 safety pre-assessment stage. Please refer to the official package insert for complete safety information before any clinical use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (NSIAD) has zero supporting clinical trials or literature, and its own mechanistic rationale assesses the opioid-receptor-to-AVPR2-mutation pathway link as biologically implausible rather than merely under-studied. Fentanyl is also not currently marketed in this jurisdiction (0 registrations), and a blocking data gap (missing TFDA/HSA label) prevents even a baseline safety review.

**To proceed, the following is needed:**
- TFDA/HSA package insert (warnings, contraindications) to resolve blocking data gap DG001
- DrugBank mechanism-of-action data to resolve data gap DG002
- Independent pharmacological review of the proposed opioid–AVPR2 mechanistic link before any further investment in this specific candidate
- Note: within this same evidence pack, two other predicted indications for fentanyl show materially stronger support and may warrant separate evaluation — **myofascial pain syndrome** (rank 4, evidence level L2, "Proceed with Guardrails," backed by a completed Phase 3 RCT and supportive review literature) and **tendinitis** (rank 10, evidence level L3, "Research Question," backed by multiple RCTs on perioperative opioid analgesia in tendon/rotator-cuff surgery)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

