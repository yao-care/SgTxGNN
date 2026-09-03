---
layout: default
title: Rifaximin
parent: 僅模型預測 (L5)
nav_order: 858
evidence_level: L5
indication_count: 10
---

# Rifaximin
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

# Rifaximin: From Unregistered Indication to Oral Candidiasis

## One-Sentence Summary

Rifaximin is a gut-selective, non-absorbable rifamycin antibiotic; however, no original indication data is available in this evidence pack (the drug is not registered in Singapore or Taiwan) and detailed mechanism of action data is also missing.
The TxGNN model predicts it may be effective for **Oral Candidiasis** with a very high similarity score, but the only supporting literature found actually reports the **opposite direction of effect** — rifaximin use was associated with an *increase* in resistant Candida infections, not treatment benefit.
With **0 clinical trials** and only **1 publication** (which reports harm rather than efficacy), this candidate should be treated as a likely false positive from the model's embedding space rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is not registered in Singapore/Taiwan, and no original indication data was provided in the evidence pack |
| Predicted New Indication | Oral Candidiasis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 (model prediction only; the one available publication is negative/contradictory) |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for rifaximin in this evidence pack (`original_moa: [Data Gap]`). Based on general pharmacological knowledge captured in the rationale field, rifaximin is a rifamycin-class antibiotic with minimal systemic or mucosal absorption, acting locally within the gastrointestinal tract on the gut bacterial microbiota. It has no known antifungal activity.

This creates a mechanistic mismatch with the predicted indication of oral candidiasis, which is a fungal infection of the oral mucosa. There is no plausible pharmacodynamic pathway by which a gut-restricted, non-absorbed antibacterial agent would treat a mucosal *Candida* infection.

More importantly, the single piece of literature evidence associated with this prediction (PMID 34180023) does not support efficacy — it reports that rifaximin use in allogeneic hematopoietic stem cell transplant recipients was associated with a **higher incidence of micafungin-resistant Candida infections**, consistent with a mechanism of bacterial suppression permitting fungal overgrowth (ecological disruption), rather than a therapeutic effect. The same negative-direction pattern repeats for the related prediction "candidiasis" (rank 6), which cites this same paper plus a second study identifying rifaximin/cirrhosis-related risk factors for candidaemia. TxGNN's high similarity score in this case most likely reflects a graph-embedding artifact (co-occurrence of rifaximin and Candida-related terms in adverse-event contexts) rather than a genuine therapeutic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for oral candidiasis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohort/Case series | Annals of Hematology | In allogeneic HSCT recipients, rifaximin prophylaxis was associated with an increased incidence of micafungin-resistant *Candida* spp. infections — an adverse association, not a therapeutic finding |

---

## Singapore Market Information

Rifaximin is not currently registered in the Singapore market (0 licenses on file); no product authorization data is available.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were available in this evidence pack (all flagged as data gaps: DG001 — TFDA label warnings/contraindications, severity Blocking).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (oral candidiasis, TxGNN score 99.75%) is not supported by clinical trial evidence and is directly contradicted by the only available publication, which reports rifaximin use *increasing* resistant Candida infection risk rather than treating it. Combined with missing MOA data and no Singapore market registration, this candidate does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- TFDA/HSA label warnings and contraindications (DG001, Blocking — currently blocks any S1 safety screening)
- Confirmed mechanism of action data from DrugBank (DG002)
- Independent re-evaluation of the TxGNN embedding for false-positive risk, given the negative-direction literature signal
- If further repurposing work is pursued for this drug, note that **HIV infectious disease** (rank 9, TxGNN score 98.2%) reached evidence level L3 with an active "Research Question" stage — it has a directly relevant Phase 4 trial (NCT01654939, withdrawn/0 enrollment) and a pilot RCT (PMID 25214516) showing only a "marginal" effect on microbial translocation. This is a more defensible starting point for further evaluation than oral candidiasis, though still far from Go-level evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

