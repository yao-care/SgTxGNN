---
layout: default
title: Ranibizumab
parent: Medium Evidence (L3-L4)
nav_order: 852
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Ranibizumab: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L4). Approved use: Diabetic retinopathy, diabetic macular edema, macular degeneration…"
monitor_inn: "Ranibizumab"
predicted_indications: ["immature cataract", "tetanic cataract", "diabetes mellitus type 2 associated cataract", "craniostenosis cataract", "mature cataract", "cortical cataract", "nuclear senile cataract", "senile cataract", "hemorrhagic disease of newborn"]
---

# Ranibizumab
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Ranibizumab: From Diabetic Retinopathy and Macular Degeneration to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Ranibizumab is an anti-VEGF antibody fragment, originally used for retinal diseases such as macular degeneration, diabetic macular edema and diabetic retinopathy.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, supported by **18 publications** (including post hoc analyses of Phase 3 RCTs and a recent randomized trial of a ranibizumab port delivery system), but **no registered clinical trials** for this indication in the data compiled for this report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetic retinopathy, diabetic macular edema, macular degeneration, retinal artery occlusion, retinopathy of prematurity (from the knowledge graph; Singapore label text is not available) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (based on literature only; should be confirmed against the primary trial publications) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Ranibizumab is an antibody fragment that blocks VEGF. Detailed mechanism-of-action data from DrugBank are not available in the data compiled for this report. In diabetic retinopathy, VEGF drives retinal vascular permeability and new vessel growth, so blocking it plausibly slows disease progression and improves retinopathy severity.

Diabetic retinopathy and diabetic macular edema are already among the drug's known indications. Severe nonproliferative diabetic retinopathy is an earlier stage of the same disease, so this prediction is a close extension rather than a leap to an unrelated condition.

The literature supports this link. Post hoc analyses of the Phase 3 RIDE/RISE trials (PMID 32606578, 36774994) report diabetic retinopathy regression with ranibizumab. A randomized trial of a ranibizumab port delivery system versus monitoring in nonproliferative diabetic retinopathy (PMID 40048178) directly addresses this patient group.

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication. The RIDE/RISE trials (NCT00473382 / NCT00473330) appear only through post hoc literature, not as registered records for this prediction.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmol | Pavilion trial: ranibizumab port delivery system vs monitoring in NPDR without macular edema |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | Post hoc analysis of RCT (RIDE/RISE) | Ophthalmol Retina | Meta-analysis of how baseline DR severity affects time to DME resolution with ranibizumab |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | Post hoc analysis of RCT (RIDE/RISE) | Clin Ophthalmol | Predictors of early diabetic retinopathy regression with ranibizumab |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | Open-label extension analysis | BMJ Open Ophthalmol | Effect of less frequent ranibizumab on DR severity scale scores after induction therapy |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | Secondary analysis of RCT | JAMA Ophthalmol | Two-year change in DR with aflibercept, bevacizumab and ranibizumab |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | RCT follow-up (DRCR.net Protocol I) | Retina | Five-year changes in DR severity in eyes treated with ranibizumab for DME |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2025 | Systematic review / meta-analysis | Health Technol Assess | Anti-VEGF drugs compared with laser photocoagulation for diabetic retinopathy |
| [42219053](https://pubmed.ncbi.nlm.nih.gov/42219053/) | 2026 | Systematic review / meta-analysis | Eur J Pharmacol | Sustained ranibizumab port delivery in DR and DME |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opin Biol Ther | Review of ranibizumab for diabetic retinopathy |
| [40969370](https://pubmed.ncbi.nlm.nih.gov/40969370/) | 2025 | Cohort | Front Endocrinol | Nomogram of predictors of response to anti-VEGF plus laser in severe NPDR |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14772P | LUCENTIS Solution for Injection in Pre-filled Syringe 1.65mg/0.165ml | Injection, solution | Not available |
| SIN13411P | Lucentis 10mg/ml Solution for Injection | Injection, solution | Not available |

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: eye infectious disease, conjunctivitis.
- **Drug Interactions**: no interactions were found in the queried data.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is plausible, and the literature includes post hoc analyses of Phase 3 RCTs and a recent randomized trial in nonproliferative diabetic retinopathy. The L1 grade rests on literature alone, with no registered trials for this indication, so it needs confirmation. The drug is already marketed in Singapore under two registrations.

**To proceed, the following is needed:**
- Review of the primary RIDE/RISE and Pavilion publications to confirm the L1 grade
- Package insert warnings and contraindications from the HSA website (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Confirmation of the approved indication text for the two Singapore registrations, and whether severe NPDR is covered
- An infection-screening plan (active ocular or periocular infection) before intravitreal use

## Other Predicted Indications (Not Recommended)

The other nine predictions all have a **Hold** recommendation.

| Predicted Indication | Evidence Level | Assessment |
|------|------|------|
| Immature, tetanic, craniostenosis, nuclear senile cataract | L5 | No mechanistic rationale, trials or literature; likely graph-proximity artifacts |
| Type 2 diabetes-associated cataract | L4 | Literature concerns diabetic macular edema, not cataract |
| Mature cataract | L4 | Literature concerns combined surgery with ranibizumab for coexisting retinal disease, not treatment of the cataract |
| Cortical cataract | L4 | Literature concerns macular edema; one case report of capsular block syndrome after injection (an adverse event) |
| Senile cataract | L4 | Studies of aqueous cytokines and anti-VEGF response; indirect |
| Hemorrhagic disease of newborn | L4 | Two trials found, neither relevant (one withdrawn with 0 enrolled in hereditary hemorrhagic telangiectasia, one Phase 1/2 in chorioretinal disease); likely a name-similarity artifact |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

