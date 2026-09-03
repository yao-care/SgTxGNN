---
layout: default
title: Tetracaine
parent: 僅模型預測 (L5)
nav_order: 966
evidence_level: L5
indication_count: 10
---

# Tetracaine
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

# Tetracaine: From Local Anesthesia to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Tetracaine is an ester-type local anesthetic that works by blocking sodium channels to produce topical/regional numbness; no formal indication text or approved product record is present in this evidence pack. The TxGNN model's top prediction is **Acrodermatitis Chronica Atrophicans** (a late-stage skin manifestation of Lyme disease), but this is currently supported by **0 clinical trials** and **0 publications**, and the model itself flags the association as likely noise.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (tetracaine is pharmacologically an ester-type, sodium-channel-blocking local anesthetic, per repurposing rationale text) |
| Predicted New Indication | Acrodermatitis Chronica Atrophicans |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a High-severity data gap). Based on the repurposing rationale supplied with this evidence pack, tetracaine is understood to be a sodium-channel-blocking local anesthetic, with no known antimicrobial, anti-spirochetal, or immunomodulatory activity.

Acrodermatitis chronica atrophicans is a late cutaneous manifestation of *Borrelia* infection (Lyme disease), driven by chronic spirochetal infection and associated tissue atrophy — a disease process with no plausible mechanistic overlap with sodium-channel blockade. There is no evidence in this pack (0 trials, 0 publications) connecting tetracaine to this disease.

The evidence pack itself explicitly assesses this as an implausible association, suggesting the very high TxGNN score is likely an artifact of knowledge-graph embedding noise (e.g., operative/procedural co-occurrence in dermatology contexts) rather than a genuine mechanistic or clinical signal. This prediction should not be treated as a credible repurposing lead without independent mechanistic justification.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Singapore Market Information

Tetracaine has **no registered product license** in Singapore (market status: Not Marketed; total registrations: 0). No authorization records, dosage forms, or approved indication text are available to summarize.

## Safety Considerations

Formal safety data (key warnings, contraindications, drug interactions) could not be retrieved for tetracaine in this evidence pack — please refer to the package insert for authoritative safety information.

**Important safety signal identified during evidence review (not part of the top prediction, but relevant to any tetracaine repurposing pathway):** Among the 10 model-predicted indications reviewed, "cauda equina syndrome" (rank 8, TxGNN score 99.55%) is supported by 9 case reports/mechanistic studies (e.g., PMID [11685003](https://pubmed.ncbi.nlm.nih.gov/11685003/), [8017646](https://pubmed.ncbi.nlm.nih.gov/8017646/), [1994754](https://pubmed.ncbi.nlm.nih.gov/1994754/)) — but these all describe tetracaine **causing** neurotoxic injury after intrathecal/spinal administration, not treating the condition. This is a documented **adverse effect**, and the high association score most likely reflects the knowledge graph encoding a cause→effect edge rather than a treatment edge. This should be flagged as a safety/pharmacovigilance concern rather than pursued as a repurposing candidate.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (acrodermatitis chronica atrophicans) has zero supporting clinical or literature evidence and is explicitly assessed as mechanistically implausible / likely model noise. Across all 10 predicted indications reviewed, none reached above L4, and the two with literature support are either indirectly related (bronchitis, via an unrelated 1988 saline-instillation study) or represent a known adverse effect rather than a therapeutic signal (cauda equina syndrome).

**To proceed, the following is needed:**
- TFDA-equivalent package insert (warnings/contraindications) — currently a **Blocking** data gap (DG001)
- Verified mechanism of action data from DrugBank — currently a **High**-severity data gap (DG002)
- Independent mechanistic or preclinical rationale linking tetracaine to acrodermatitis chronica atrophicans before allocating further evidence-collection resources
- If pursued further, the cauda equina syndrome signal should be routed to pharmacovigilance/safety review rather than repurposing evaluation
- Confirmation of regulatory pathway feasibility, given tetracaine currently has no marketed product or registration in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

