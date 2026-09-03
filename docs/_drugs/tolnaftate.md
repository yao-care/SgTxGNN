---
layout: default
title: Tolnaftate
parent: 僅模型預測 (L5)
nav_order: 993
evidence_level: L5
indication_count: 10
---

# Tolnaftate
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

# Tolnaftate: From Superficial Fungal Infections to Ectothrix Infectious Disease

## One-Sentence Summary

Tolnaftate is a topical thiocarbamate antifungal, traditionally used to treat superficial dermatophyte (tinea/ringworm) infections. The TxGNN model's top-ranked prediction is **Ectothrix Infectious Disease** (a dermatophyte pattern affecting the outer hair shaft), but this is currently supported by **0 clinical trials** and **0 publications** — the prediction score is high, but there is no direct evidence base behind it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Superficial fungal infections (dermatophytosis/tinea) — based on known clinical use; no formal Singapore registration record available |
| Predicted New Indication | Ectothrix Infectious Disease |
| TxGNN Prediction Score | 98.59% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field is a data gap). Based on known information, Tolnaftate belongs to the thiocarbamate class of antifungals, and its efficacy against superficial dermatophyte infections has been well established for decades; mechanistically, this same action could plausibly extend to ectothrix infection patterns.

Ectothrix infection describes a dermatophyte infection pattern where fungal elements (typically *Microsporum* species) colonize the *outside* of the hair shaft. This is mechanistically consistent with Tolnaftate's known action of inhibiting squalene epoxidase and blocking ergosterol biosynthesis in dermatophytes — the same fungal class Tolnaftate is already approved to treat. In other words, this is not a mechanistically distant "new" indication; it is a close variant of the drug's existing, well-established antifungal spectrum.

Importantly, the evidence pack's own rationale for this candidate explicitly notes that ectothrix infection represents "an extension of the existing indication rather than a genuinely new indication," and no direct trial or literature evidence currently exists for this specific presentation. By comparison, other lower-ranked candidates in this pack have materially more support — **superficial mycosis** (rank 5) is explicitly identified as the drug's core original indication with L1-level evidence (RCTs, systematic review), while **cutaneous candidiasis** (rank 3, L4) has some early/mixed evidence for a genuinely different fungal target (yeast vs. dermatophyte). These may be more productive angles for further evaluation than the top-ranked prediction itself.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

No Singapore market authorization records are currently available for Tolnaftate (Market Status: Not Marketed; 0 registrations on file).

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: A blocking data gap has been identified — TFDA/HSA label warnings and contraindications have not yet been retrieved, which currently prevents this candidate from advancing to a formal safety pre-assessment stage.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (ectothrix infectious disease) has a high TxGNN score but zero supporting clinical trials or literature, and the pack's own mechanistic rationale characterizes it as a label extension rather than a genuinely novel indication — insufficient basis to proceed at this time.

**To proceed, the following is needed:**
- TFDA/HSA product label data (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism of action via DrugBank API query
- Targeted literature/trial search specifically on tolnaftate efficacy in ectothrix-pattern tinea capitis (e.g., *Microsporum* species)
- Clarification of whether this candidate should be reclassified as a label-extension review rather than a repurposing candidate
- Consider prioritizing **superficial mycosis** (existing indication, L1 evidence) and **cutaneous candidiasis** (L4, distinct fungal target) for more actionable next steps
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

