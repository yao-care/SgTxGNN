---
layout: default
title: Tezepelumab
parent: 僅模型預測 (L5)
nav_order: 968
evidence_level: L5
indication_count: 10
---

# Tezepelumab
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

# Tezepelumab: From Th2-Driven Inflammatory Disease to Diabetic Cataract

## One-Sentence Summary

Tezepelumab is an anti-TSLP monoclonal antibody that targets epithelial cytokine-driven Th2/inflammatory pathways (the class of disease this mechanism is clinically relevant to, e.g. severe asthma); however, no formal original-indication or regulatory data is on file for Taiwan.
The TxGNN model predicts it may be effective for **Diabetic Cataract**, but this prediction is supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags the result as a likely knowledge-graph clustering artifact rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — Tezepelumab is not registered in Taiwan and no license/indication text is on file |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.40% |
| Evidence Level | L5 (model prediction only, no supporting clinical trials or literature) |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Tezepelumab is not formally documented in this evidence pack (DG002, High severity gap). Based on the mechanistic rationale attached to the predictions, Tezepelumab is an anti-TSLP (thymic stromal lymphopoietin) monoclonal antibody that blocks an upstream epithelial alarmin driving Th2/type-2 inflammation — the pathway relevant to conditions such as severe asthma. This is fundamentally an immunology/allergy-axis mechanism.

Diabetic cataract, and the other cataract subtypes ranked #1–9 in this candidate list, are driven by entirely different pathophysiology: the polyol (sorbitol/aldose reductase) pathway, oxidative stress, and lens protein glycation/aggregation. None of these processes have an established link to TSLP or Th2 signaling. The evidence pack's own rationale text explicitly states there is "no known direct association" between the TSLP-Th2 axis and these lens pathologies.

A further red flag is the score distribution: ranks #2–6 all share an almost identical score (0.983126699924469), and ranks #7–9 cluster within 0.001 of each other. This pattern — a tight cluster of unrelated or loosely related cataract subtypes all scoring nearly identically — is a classic signature of embedding-space node clustering in the knowledge graph rather than a drug-specific mechanistic prediction. In short, the high TxGNN score appears to reflect proximity of "cataract" disease nodes to each other in the graph, not a real biological rationale connecting Tezepelumab to lens disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Tezepelumab is not currently registered or marketed in Taiwan. No license records are available (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack — DG001, Blocking severity, pending TFDA label acquisition.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-prediction-only candidate with zero supporting clinical trials or literature. The top 10 ranked indications are nearly all cataract subtypes with near-identical scores, which strongly suggests a knowledge-graph clustering artifact rather than a genuine drug-disease mechanistic signal — a concern the evidence pack itself raises repeatedly. There is no plausible mechanistic bridge between the TSLP-Th2 inflammatory axis and lens pathology (polyol pathway, oxidative stress, protein aggregation). Combined with the drug's unregistered status in Taiwan and blocking safety data gaps, this candidate does not meet the bar to advance.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/international package insert for warnings, contraindications, and DDI data
- Resolve DG002 (High): confirm formal original indication and MOA via DrugBank API or product label
- Independent preclinical or mechanistic evidence linking TSLP signaling to lens/cataract pathophysiology before further evaluation
- Re-run or audit the TxGNN evidence collection for this candidate cluster to rule out embedding-space clustering artifacts across similar disease nodes
- Continued monitoring for any emerging clinical trials or literature before revisiting this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

