---
layout: default
title: Erdosteine
parent: 僅模型預測 (L5)
nav_order: 387
evidence_level: L5
indication_count: 10
---

# Erdosteine
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

# Erdosteine: From Respiratory Disease (COPD / Chronic Bronchitis) to Marcothrombocytopenia with Mitral Valve Insufficiency

## One-Sentence Summary

Erdosteine is a thiol-containing mucolytic and antioxidant agent used for respiratory conditions including COPD and chronic bronchitis, with demonstrated efficacy in reducing acute exacerbation frequency (RESTORE RCT, PMID: 26560176).
The TxGNN model predicts it may be effective for **Marcothrombocytopenia with Mitral Valve Insufficiency**,
however, **no clinical trials or published literature** currently support this direction — this prediction appears to be a knowledge graph structural extrapolation artifact rather than a mechanistically driven finding.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Respiratory diseases (mucolytic agent; COPD, chronic bronchitis) |
| Predicted New Indication | Marcothrombocytopenia with Mitral Valve Insufficiency |
| TxGNN Prediction Score | 84.75% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Erdosteine is a thiol-containing mucolytic prodrug that undergoes hepatic metabolism to produce active metabolites (Met-1, Met-2) bearing free sulfhydryl (-SH) groups. These metabolites reduce mucus viscosity by cleaving disulfide bonds in mucus glycoproteins, and additionally exert antioxidant and anti-adhesion effects on respiratory epithelium. Its efficacy and safety in COPD are well-documented in the large-scale RESTORE RCT (PMID: 26560176), providing a solid respiratory safety profile.

The mechanistic leap to marcothrombocytopenia with mitral valve insufficiency is, however, extremely tenuous. Thiol-class compounds such as N-acetylcysteine (NAC) have shown mild antiplatelet aggregation effects in some studies, which may account for Erdosteine's proximity in the TxGNN knowledge graph to platelet-related disease nodes. However, Erdosteine itself has no published platelet-related mechanism data, and the combined syndrome — simultaneously involving thrombocytopenia and cardiac valvular pathology — introduces a heart valve component for which there is no conceivable thiol-drug pathway.

This prediction most likely reflects graph topology rather than pharmacological signal: Erdosteine's thiol-class annotations place it near NAC nodes that carry platelet-related edges in the knowledge graph. Notably, among all 10 predicted indications in this pack, **RSV infectious disease (rank 9, score 74.95%)** is the most mechanistically aligned with Erdosteine's established respiratory and antioxidant properties, and represents the only candidate worth advancing to S1 safety evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Erdosteine is currently not registered with the Health Sciences Authority (HSA) of Singapore. No Singapore marketing authorizations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Erdosteine are at evidence level L5 (model prediction only, with zero supporting clinical trials or publications), and the top-ranked prediction carries essentially no mechanistic connection to Erdosteine's established pharmacology. Singapore regulatory standing is unestablished, with 0 HSA registrations on record.

**To proceed, the following is needed:**
- Obtain Erdosteine's full prescribing information (SmPC / package insert) to resolve the blocking safety data gap — without this, S1 safety evaluation cannot commence
- Prioritise RSV infectious disease (rank 9, TxGNN score 74.95%) as the most mechanistically coherent repurposing candidate, and commission a targeted literature review covering Erdosteine + RSV (mucolysis in bronchiolitis, antioxidant attenuation of RSV-induced epithelial oxidative stress)
- Consider a secondary mechanistic hypothesis screen for the fibromatosis cluster (Ledderhose disease rank 7, penile fibromatosis rank 8) via thiol-NF-κB / TGF-β antifibrotic pathway analogies drawn from NAC literature before investing in wet-lab work
- Re-run TxGNN evidence collection with expanded PubMed queries (e.g., "erdosteine AND respiratory syncytial virus", "erdosteine AND fibrosis") to verify that zero-hit status is not a query-specificity artefact
- Assess HSA registration pathway requirements if a viable indication is confirmed downstream
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

