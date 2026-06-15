---
layout: default
title: Canagliflozin
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 10
---

# Canagliflozin
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

# Canagliflozin: From Type 2 Diabetes to Focal Stiff Limb Syndrome

## One-Sentence Summary

Canagliflozin is a selective SGLT2 inhibitor originally approved for the treatment of Type 2 Diabetes Mellitus, with well-established cardiovascular and renal protective effects.
The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome**, a rare autoimmune neurological subtype of Stiff Person Syndrome.
Currently, **no clinical trials** and **no publications** specifically support this repurposing direction — this remains a model-only prediction with no external validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 97.92% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data was not available in the data inputs received. Based on established pharmacological knowledge, Canagliflozin is a selective sodium-glucose co-transporter 2 (SGLT2) inhibitor that blocks renal glucose reabsorption, achieving glycaemic control through an insulin-independent mechanism. Beyond glucose lowering, large cardiovascular outcome trials (CANVAS, CREDENCE) have demonstrated organ-protective effects, and preclinical studies have identified indirect anti-inflammatory properties — including NF-κB pathway suppression and reduction of oxidative stress — as plausible secondary mechanisms.

Focal Stiff Limb Syndrome is an autoimmune neurological subtype of Stiff Person Syndrome (SPS), primarily mediated by antibodies against GAD65 or amphiphysin, which disrupt GABAergic neurotransmission in the spinal cord. While SGLT2 inhibitors possess some indirect immunomodulatory activity, there is no known pathway by which SGLT2 blockade influences the GABAergic system, GAD65 autoantibody titres, or the specific neuro-autoimmune cascade driving SPS. The mechanistic bridge is not established.

The high TxGNN score (97.92%) most likely reflects topological proximity in the knowledge graph between metabolic disease nodes and autoimmune disease nodes — a known pattern in graph-based models where co-morbidity structure (e.g., Type 1 DM co-occurs in approximately 30–40% of SPS patients) inflates similarity scores without implying therapeutic equivalence. This prediction should be interpreted as a hypothesis-generating signal only, not a mechanistically grounded finding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Canagliflozin is currently not registered in Singapore. No marketing authorisations were identified in the regulatory database.

> **Note for reviewers:** Canagliflozin (brand name Invokana®) is approved in multiple major markets including the US (FDA, 2013), EU (EMA, 2013), and Australia (TGA). Absence from the Singapore market should be confirmed against the HSA product register directly, as data gaps exist in the current regulatory dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Known class-level concerns for SGLT2 inhibitors** (from general clinical knowledge, pending formal data extraction):
> - Diabetic ketoacidosis (DKA), including euglycaemic DKA — particularly relevant in off-label or Type 1 DM settings
> - Genitourinary infections (urinary tract infections, genital mycotic infections)
> - Fournier's gangrene (necrotising fasciitis of the perineum) — rare but serious
> - Lower limb amputation risk (observed in CANVAS trial, specific to canagliflozin)
> - Volume depletion and hypotension — relevant in elderly or renally impaired patients
>
> Formal safety data extraction from TFDA package inserts and DrugBank API is required before any clinical evaluation proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-predicted indications for Canagliflozin in this report are at Evidence Level L5 — model prediction only — with zero supporting clinical trials, zero literature, and no credible mechanistic rationale connecting SGLT2 inhibition to any of the identified rare neurological or structural diseases. The drug is also not currently registered in Singapore, adding a regulatory pathway consideration before any clinical development could begin.

**To proceed, the following is needed:**

- **Mechanistic data:** Extract full MOA profile from DrugBank API (DB08907) to enable formal mechanism-indication plausibility scoring
- **Regulatory data:** Download and parse HSA/TFDA package insert PDFs to obtain approved indications, key warnings, and contraindications
- **Indication re-prioritisation:** Consider whether the TxGNN model should be re-queried for Canagliflozin's established indications (T2DM, heart failure, CKD) to identify repurposing candidates with stronger biological plausibility — the current top-10 list is dominated by ultra-rare diseases with no mechanistic connection
- **Safety dossier:** Conduct a full drug interaction and contraindication review before any hypothesis advances beyond S0
- **Subtype specificity check:** The identical TxGNN scores for focal vs. classic SPS (both 0.97925) suggest the model is not distinguishing between disease subtypes — this reduces confidence in the rank ordering and warrants model-level review

---

*⚠️ Disclaimer: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any clinical application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

