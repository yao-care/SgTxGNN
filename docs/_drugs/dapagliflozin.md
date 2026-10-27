---
layout: default
title: Dapagliflozin
parent: Low Evidence (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dapagliflozin: predicted new indication Focal stiff limb syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Dapagliflozin"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis", "autoimmune oophoritis"]
---

# Dapagliflozin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Dapagliflozin: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome
{: .text-alpha }

## One-Sentence Summary

Dapagliflozin is an SGLT2 inhibitor originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**,
but there are currently **no clinical trials** and **no publications** supporting this prediction, which rests on the model's computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 98.20% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, dapagliflozin is an SGLT2 inhibitor that lowers blood glucose by reducing renal glucose reabsorption, independent of insulin. Its efficacy in type 2 diabetes is established.

For focal stiff limb syndrome, no plausible mechanistic link has been identified. This condition belongs to the stiff-person spectrum, which involves impaired GABAergic inhibition and is often associated with anti-GAD65 autoimmunity. Dapagliflozin acts on renal glucose handling and has no known effect on this pathway. The high score most likely reflects network proximity: GAD65 autoimmunity is shared with diabetes-related nodes in the knowledge graph, rather than a pharmacological rationale.

The same pattern appears in the other top predictions, such as classic stiff person syndrome (98.20%), opsismodysplasia (98.06%), thiamine-responsive dysfunction syndrome (98.03%), and several localized lipodystrophies (about 97%). Most of these are linked to diabetes or metabolic-disease nodes in the graph. None has clinical or literature support.

Among the ten predictions in this set, pancreatic agenesis (96.59%) is the only one with any retrieved literature. This consists of a preclinical rat study on pancreatic injury and AMPK/mTOR signalling (PMID 33559163) and a case report series on HNF1B-MODY (PMID 42369057). Both are indirect and do not show dapagliflozin efficacy in pancreatic agenesis. Because that condition involves severe insulin deficiency, an SGLT2 inhibitor would carry a substantial risk of diabetic ketoacidosis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for focal stiff limb syndrome.

## Singapore Market Information

Eight valid licences cover products containing dapagliflozin. The data compiled for this report does not include approved indication text for any of them. The five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14542P | FORXIGA TABLET 10mg | Film-coated tablet | Not available in the compiled data |
| SIN14541P | FORXIGA TABLET 5MG | Film-coated tablet | Not available in the compiled data |
| SIN17199P | DAPAGLIFLOZIN SANDOZ FILM COATED TABLET 10MG | Film-coated tablet | Not available in the compiled data |
| SIN15079P | XIGDUO XR TABLETS 10MG/1000MG | Film-coated extended-release tablet | Not available in the compiled data |
| SIN16958P | SIDAPVIA FIXED DOSE COMBINATION TABLET 10 MG/100 MG | Film-coated tablet | Not available in the compiled data |

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records. The 20 retrieved are mostly Moderate, with a few Minor. Examples of Moderate interactions include:
  - Furosemide and hydrochlorothiazide (diuretics)
  - Fosinopril and aliskiren (renin-angiotensin agents)
  - Nifedipine and acebutolol (cardiovascular agents)
  - Salbutamol, formoterol, epinephrine, phenylephrine and pseudoephedrine (sympathomimetics)
  - Hydrocortisone and ethanol
  - Topical hydrocortisone and topical alclometasone are Minor interactions.
- **Disease-specific consideration**: In conditions with insulin deficiency (such as pancreatic agenesis or thiamine-responsive dysfunction syndrome), SGLT2 inhibitors carry a ketoacidosis risk that would need careful evaluation.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for focal stiff limb syndrome is supported only by the model score. There are no trials or publications, and no plausible mechanistic link to SGLT2 inhibition. The score likely reflects diabetes-related network proximity. The other nine predictions in this set are likewise unsupported.

**To proceed, the following is needed:**
- Detailed mechanism of action data for dapagliflozin
- Package insert warnings and contraindications from the Health Sciences Authority (HSA), which are required before any safety screening
- Approved indication text for the Singapore licences
- Any preclinical or clinical evidence linking SGLT2 inhibition to GABAergic or stiff-person-spectrum pathology; without it, this candidate should not advance
- A review of the remaining nine predictions for a candidate with stronger evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

