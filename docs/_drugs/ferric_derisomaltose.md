---
layout: default
title: Ferric Derisomaltose
parent: 僅模型預測 (L5)
nav_order: 422
evidence_level: L5
indication_count: 10
---

# Ferric Derisomaltose
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

# Ferric Derisomaltose: From Iron Deficiency Anemia to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Ferric derisomaltose (Monofer®/Monoferric®) is an intravenous iron formulation studied in large Phase 3 trials for iron deficiency anemia (IDA), with its efficacy demonstrated across both general IDA and chronic kidney disease populations.
The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy (NPDR)**, with **no clinical trials and no publications** currently directly supporting this new direction.
The closely related indication of diabetic retinopathy (rank 2, score 96.73%) has 2 Phase 3 trials on file, though both provide indirect safety data only and do not evaluate DR as an endpoint.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Iron deficiency anemia (IDA) — inferred from FERWON trial series |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, ferric derisomaltose is an intravenous iron–carbohydrate complex (isomaltoside carrier), its efficacy in correcting iron deficiency anemia has been demonstrated in large Phase 3 trials (FERWON-IDA, FERWON-NEPHRO), and mechanistically the drug may be relevant to diabetic complications where iron deficiency plays a co-pathological role.

Iron deficiency anemia is an independent aggravating factor for diabetic retinopathy. The pathophysiological axis of **IDA → reduced retinal oxygen-carrying capacity → retinal hypoxia → accelerated neovascularization** provides a rationale: correcting IDA in diabetic patients with concurrent iron deficiency could potentially slow the progression of DR. The TxGNN knowledge graph likely captures the strong node co-occurrence of "diabetes → iron metabolism dysregulation," generating a high prediction score (0.985) for this mechanistic pathway.

However, the prediction specifically targets **severe NPDR**, which sits at the threshold of proliferative disease. In patients without concurrent IDA, IV iron supplementation may increase oxidative stress through the Fenton reaction (Fe²⁺ + H₂O₂ → Fe³⁺ + ·OH + OH⁻), potentially worsening retinal oxidative damage. The mechanistic relationship is inherently bidirectional — beneficial in IDA-complicated DR, potentially harmful in iron-replete patients — making this a hypothesis that requires prospective clinical validation before any repurposing conclusion can be drawn.

---

## Clinical Trial Evidence

No clinical trials directly targeting severe nonproliferative diabetic retinopathy have been registered for ferric derisomaltose.

**Related trials providing indirect safety data (from Rank 2 — diabetic retinopathy prediction):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02940886](https://clinicaltrials.gov/study/NCT02940886) | Phase 3 | Completed | 1,512 | FERWON-IDA: Head-to-head comparison of ferric derisomaltose vs. iron sucrose in IDA; primary endpoint is haemoglobin response; provides the core drug safety database but diabetic retinopathy is not evaluated as a primary or secondary endpoint |
| [NCT02940860](https://clinicaltrials.gov/study/NCT02940860) | Phase 3 | Completed | 1,538 | FERWON-NEPHRO: Paired trial in non-dialysis-dependent CKD with IDA; combined with NCT02940886 yields a 3,050-patient safety dataset; diabetic subgroup retinal event data may exist in raw trial records as exploratory analysis material |

> ⚠️ Both trials carry evidence Grade C (same study drug, different indication). They do not establish efficacy of ferric derisomaltose in diabetic retinopathy but can inform safety profiling for the drug class.

---

## Literature Evidence

Currently no related literature available for ferric derisomaltose in severe nonproliferative diabetic retinopathy or diabetic retinopathy.

---

## Singapore Market Information

Ferric derisomaltose is not currently registered in Singapore. No authorization records are available.

> For reference: The drug is approved as **Monoferric®** by the US FDA (2020) for IDA in adults, and as **Monofer®** by the EMA, for use in patients intolerant to oral iron or with clinical need for rapid iron delivery. Singapore market entry would require HSA registration.

---

## Safety Considerations

Please refer to the package insert for safety information (Singapore TFDA label data was not available for this analysis).

**Known mechanistic safety concern relevant to this indication:**
Intravenous iron supplementation in patients **without** concurrent iron deficiency may increase systemic oxidative stress via Fenton chemistry, posing a theoretical risk of worsening retinal oxidative damage in diabetic patients. Iron status (serum ferritin, transferrin saturation) must be confirmed before any clinical investigation in this direction.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests entirely on TxGNN model output (L5 evidence) with no direct clinical trials or literature supporting ferric derisomaltose as a treatment for severe nonproliferative diabetic retinopathy. The mechanistic hypothesis is plausible only in the specific subpopulation of diabetic patients with concurrent IDA; outside this subgroup, the risk-benefit profile is unclear or potentially unfavourable.

**To proceed, the following is needed:**

- **Confirm patient subpopulation**: Establish that the intended target population has documented concurrent IDA — this is the necessary prerequisite for mechanistic plausibility
- **Label review**: Obtain and parse the FDA/EMA Monoferric® package insert for full warnings, contraindications, and drug interactions (DG001, DG002 remediation)
- **MOA clarification**: Query DrugBank API for ferric derisomaltose mechanism of action, iron release kinetics, and oxidative stress profile
- **Subgroup data mining**: Request or review diabetic subgroup data from the FERWON-IDA and FERWON-NEPHRO trials for any retinal-related adverse events or incidental secondary findings
- **Hypothesis-generating study design**: Design a prospective observational cohort study — IDA correction outcomes in Type 2 DM patients with NPDR as a pre-specified secondary endpoint
- **Expert consultation**: Engage ophthalmology and haematology specialists to evaluate clinical feasibility before committing trial resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

