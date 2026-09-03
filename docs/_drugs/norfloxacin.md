---
layout: default
title: Norfloxacin
parent: 僅模型預測 (L5)
nav_order: 715
evidence_level: L5
indication_count: 10
---

# Norfloxacin
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

# Norfloxacin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Norfloxacin is a fluoroquinolone antibacterial; this evidence pack does not contain specific original-indication or mechanism-of-action data for the drug. The TxGNN model's top-ranked prediction is **Hyperamylasemia**, but the pipeline's own mechanistic review found **no biological connection** to norfloxacin's antibacterial activity and flagged the signal as likely embedding noise — **zero clinical trials and zero publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (no Singapore licensing record); norfloxacin is a fluoroquinolone antibacterial by drug class |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Singapore Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, norfloxacin is a fluoroquinolone antibacterial that inhibits bacterial DNA gyrase and topoisomerase IV; it is conventionally used against gram-negative bacterial infections (e.g., urinary tract infections).

The top-ranked predicted indication, hyperamylasemia, is a laboratory finding reflecting pancreatic or salivary gland enzyme dysregulation — a metabolic/endocrine process with no established link to fluoroquinolone antibacterial pharmacology. The evidence pack's own repurposing rationale explicitly states there is "no mechanistic connection" and judges this to be TxGNN embedding noise rather than a genuine signal.

For context, two lower-ranked candidates in this pack did reach a "Research Question" stage with supporting literature: **septicemic plague** (rank 10) has a class-effect rationale — other fluoroquinolones are approved for *Yersinia pestis* — though norfloxacin itself lacks clinical-use evidence for this indication; and **punctate epithelial keratoconjunctivitis** (rank 5) returned literature that concerns a parasitic (microsporidial) pathogen outside norfloxacin's antibacterial spectrum, indicating only a keyword-level match. Neither of these, nor the top-ranked hyperamylasemia signal, currently rises to actionable evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

Norfloxacin is currently not marketed in Singapore (0 registrations on file; no license records available in this evidence pack).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction (hyperamylasemia) has no clinical trials, no literature, and is explicitly flagged by the mechanistic review as an unsupported/noise signal (L5, decision stage S0). The drug is also unregistered in Singapore, so there is no local regulatory or safety baseline to build on.

**To proceed, the following is needed:**
- HSA/TFDA-equivalent package insert (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism-of-action data for norfloxacin (currently a data gap)
- If pursuing repurposing further, prioritize re-examining ranks 5 and 10 (both reached "Research Question" stage with literature) rather than the top-ranked hyperamylasemia signal, and independently verify norfloxacin-specific (not class-effect) evidence for septicemic plague
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

