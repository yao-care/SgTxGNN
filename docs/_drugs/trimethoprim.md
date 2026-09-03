---
layout: default
title: Trimethoprim
parent: 僅模型預測 (L5)
nav_order: 1019
evidence_level: L5
indication_count: 10
---

# Trimethoprim
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

# Trimethoprim: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Trimethoprim is a classic DHFR-inhibiting antibacterial agent, traditionally used to treat bacterial infections (e.g. urinary tract infections, often combined with sulfamethoxazole or, in ophthalmic form, polymyxin B). The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**, but this specific prediction is currently supported only by the model's score — **no clinical trials and no published literature** have been identified for this exact indication.

> Note: the drug's original indication and mechanism of action are marked as data gaps in this evidence pack (no Singapore label on file), so the "original indication" above is based on trimethoprim's well-established pharmacological class rather than a documented local approval.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Data gap — not documented in Singapore regulatory filings (trimethoprim is classically used as an antibacterial agent) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (High-severity data gap — DrugBank MOA lookup pending). Based on known information, trimethoprim is a dihydrofolate reductase (DHFR) inhibitor commonly formulated as a topical ophthalmic antibacterial (e.g. combined with polymyxin B in products such as Polytrim), and mechanistically it may be applicable to ocular surface conditions.

Punctate epithelial keratoconjunctivitis and bacterial conjunctivitis (a related, better-evidenced candidate in this evidence pack, see below) are both ocular surface disorders where secondary or co-existing bacterial infection can play a role. The repurposing rationale for this candidate describes the link as an **indirect, class-based extrapolation** — trimethoprim's known antibacterial spectrum overlaps with organisms implicated in conjunctivitis-type disease, but no direct trial or literature evidence exists for punctate epithelial keratoconjunctivitis specifically. This should therefore be treated as a research hypothesis rather than a validated repurposing signal.

It is worth noting that a related candidate in the same evidence pack — **conjunctivitis (disease)**, ranked #2 by TxGNN score — has substantially stronger support: an L1 evidence level, a completed Phase 4 head-to-head RCT (NCT00581542), and roughly 20 associated publications including RCTs. This suggests that trimethoprim's realistic near-term repurposing value in ophthalmology is currently concentrated in conjunctivitis, not punctate epithelial keratoconjunctivitis (see "Conclusion and Next Steps").

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Trimethoprim is currently **not marketed** in Singapore under this evidence pack (0 registrations found, no license records available).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are currently marked as data gaps in this evidence pack — see "Conclusion and Next Steps" for remediation.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (punctate epithelial keratoconjunctivitis) has only mechanistic/analogic support (L4), with zero clinical trials or literature directly addressing this indication, and the drug is not currently marketed in Singapore. A Blocking-severity data gap (missing label warnings/contraindications) also prevents a preliminary S1 safety assessment.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications — download and parse the official label PDF (Blocking gap, required before any S1 safety screening)
- Detailed mechanism of action data via DrugBank API (High-priority gap)
- If this specific indication is to be pursued, dedicated clinical studies (even small case series) directly evaluating trimethoprim in punctate epithelial keratoconjunctivitis, since current support is purely class-based extrapolation
- Consider prioritizing **conjunctivitis (disease)** instead as the lead repurposing candidate for this drug — it already has L1 evidence, a completed Phase 4 RCT, and a "Proceed with Guardrails" recommendation within the same evidence pack, representing a materially stronger and more actionable opportunity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

