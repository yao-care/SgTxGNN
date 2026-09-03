---
layout: default
title: Proparacaine
parent: 僅模型預測 (L5)
nav_order: 825
evidence_level: L5
indication_count: 10
---

# Proparacaine
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

# Proparacaine: From Topical Ocular Anesthesia to Cauda Equina Syndrome

## One-Sentence Summary

Proparacaine is an ester-type local anaesthetic conventionally used for topical corneal/conjunctival anesthesia in ophthalmic procedures. The TxGNN model assigns its highest score to **Cauda Equina Syndrome**, but this prediction is currently supported by **zero clinical trials and zero publications**, and the evidence pack's own mechanistic review explicitly flags the biological plausibility as weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Topical ocular (corneal/conjunctival) anesthesia — based on known drug class information; no Singapore-registered indication text is available |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 96.90% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Proparacaine (flagged as a High-severity data gap). Based on known pharmacological class information, Proparacaine is an ester-type local anaesthetic that acts by blocking voltage-gated sodium channels on peripheral sensory nerve terminals, producing short-acting surface anesthesia of the cornea and conjunctiva for ophthalmic examinations and minor procedures.

Cauda equina syndrome is a neurosurgical emergency caused by compression of the lumbosacral nerve roots, presenting with motor weakness, sensory loss, and bowel/bladder sphincter dysfunction. The evidence pack's own mechanistic rationale for this candidate states there is **no plausible pharmacological connection** between a topically applied peripheral sensory-nerve blocker restricted to the ocular surface and the central nerve-root compression pathology underlying cauda equina syndrome. No clinical trials, literature, or preclinical data were found to support this association — the score appears to be a model artifact rather than a biologically grounded signal.

Given the absence of any corroborating mechanistic, preclinical, or clinical evidence, this candidate should be treated as a low-confidence model output rather than a credible repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Proparacaine is currently **not marketed** in Singapore (0 registrations on file), so no product authorization records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: The TFDA package insert (warnings/contraindications) is flagged as a **Blocking** data gap (DG001) — this must be resolved before any formal safety (S1) evaluation can proceed. Mechanism of action data is also missing (DG002, High severity), limiting the mechanistic plausibility assessment above.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Cauda Equina Syndrome) has an L5 evidence level — no clinical trials, no literature, and the mechanistic review itself concludes there is no plausible pharmacological link. Combined with the drug's absence from the Singapore market and missing safety/MOA data, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/official package insert data (warnings, contraindications) — currently blocking safety evaluation (DG001)
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- Any preclinical or case-level evidence specifically linking local anaesthetic sodium-channel blockade to cauda equina pathology, if such a hypothesis is to be pursued further
- Given the weak signal, consider re-screening lower-ranked candidates in this evidence pack (e.g., allergic asthma, rank 2) which at least have preclinical literature support (L4) for a more tractable next step
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

