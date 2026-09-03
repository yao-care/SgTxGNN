---
layout: default
title: Pemigatinib
parent: 僅模型預測 (L5)
nav_order: 765
evidence_level: L5
indication_count: 10
---

# Pemigatinib
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

# Pemigatinib: From Cholangiocarcinoma to Multiple Endocrine Neoplasia

## One-Sentence Summary

Pemigatinib is a selective FGFR1-3 tyrosine kinase inhibitor, originally developed for FGFR2 fusion/rearrangement-positive cholangiocarcinoma. The TxGNN model predicts a possible link to **Multiple Endocrine Neoplasia (MEN)** with a **99.71%** prediction score, but there are currently **no clinical trials and no literature** supporting this direction, and the biological rationale is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cholangiocarcinoma, FGFR2 fusion/rearrangement-positive (not verifiable via Singapore license records — drug is not marketed locally) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Pemigatinib is a small-molecule, orally administered inhibitor that selectively targets FGFR1, FGFR2, and FGFR3 tyrosine kinases. Its established clinical value comes from blocking aberrant FGFR2 signaling in fusion/rearrangement-positive cholangiocarcinoma.

Multiple Endocrine Neoplasia, however, is not an FGFR-driven disease — MEN1 and MEN2 syndromes are caused by germline mutations in the *MEN1* and *RET* genes respectively, pathways unrelated to FGFR signaling. The evidence pack's own mechanistic assessment explicitly flags this gap, noting no literature supports a role for FGFR inhibitors in MEN.

Given the absence of a plausible biological mechanism and the complete lack of supporting trials or publications, this specific prediction (rank 1) is best interpreted as a high TxGNN similarity score that does not reflect a validated pharmacological relationship — likely a knowledge-graph artifact rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Pemigatinib is not marketed in Singapore; no license records are available in the evidence pack.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective FGFR1-3 small-molecule tyrosine kinase inhibitor) |
| Myelosuppression Risk | Not available in evidence pack — please refer to the package insert |
| Emetogenicity Classification | Not available in evidence pack — please refer to the package insert |
| Monitoring Items | Not available in evidence pack — please refer to the package insert |
| Handling Protection | Not available in evidence pack — please refer to the package insert |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 — a model prediction with no clinical trials, no literature, and no supported mechanism of action. The rationale in the evidence pack itself indicates MEN is driven by *RET*/*MEN1* mutations rather than FGFR signaling, making this a low-confidence candidate not warranted for further investment at this time.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data (MOA) for Pemigatinib beyond the FGFR1-3 target class
- Preclinical or mechanistic evidence directly linking FGFR inhibition to MEN pathophysiology
- Full safety profile (contraindications, key warnings, DDI) from TFDA/manufacturer labeling
- Singapore regulatory/registration status confirmation
- Consider reprioritizing evaluation toward rank 3 (HER2-positive breast carcinoma, evidence level L4, decision stage S1), which has a documented mechanistic crosstalk rationale (FGFR upregulation as a HER2-targeted therapy resistance mechanism) and at least one supporting literature reference — a comparatively stronger candidate than the top-ranked MEN prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

