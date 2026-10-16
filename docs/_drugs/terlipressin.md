---
layout: default
title: Terlipressin
parent: Low Evidence (L5)
nav_order: 970
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Terlipressin: predicted new indication Open-angle glaucoma (evidence level L5). Approved use: Not stated in the Singapore registration records compiled"
monitor_inn: "Terlipressin"
predicted_indications: ["open-angle glaucoma", "primary hereditary glaucoma", "pulmonary hypertension", "kyphoscoliotic heart disease", "esotropia", "glaucoma 1, open angle", "headache disorder", "hyperthyroidism", "glaucoma", "trigeminal autonomic cephalalgia"]
---

# Terlipressin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Terlipressin: From Its Registered Use to Open-Angle Glaucoma

## One-Sentence Summary

Terlipressin is a vasopressin analogue (a prodrug of lysine-vasopressin) that is marketed in Singapore as an injectable. The registration records compiled for this report do not state its approved indication.
The TxGNN model predicts it may be effective for **open-angle glaucoma**, but this rests on the model score alone, with **0 clinical trials** and **0 relevant publications**.
Among the other top-10 predictions, only **pulmonary hypertension** has any supporting literature (small hemodynamic studies and case reports).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records compiled |
| Predicted New Indication | Open-angle glaucoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Terlipressin is a vasopressin V1 receptor agonist and a prodrug of lysine-vasopressin. Its main pharmacological effect is vasoconstriction, notably in the splanchnic circulation, which lowers portal pressure.

The data compiled for this report do not support a plausible route from this mechanism to lower intraocular pressure. The high TxGNN score (0.998) is a statistical prediction from the knowledge graph. No trials, mechanistic studies, or relevant papers back it. Systemic vasoconstriction could, in principle, be a concern for ocular perfusion, so the prediction needs careful scrutiny.

Several other top predictions are also unsupported: primary hereditary glaucoma, "glaucoma 1, open angle" (a near-duplicate of the first prediction), and the generic "glaucoma". The same applies to esotropia, hyperthyroidism, kyphoscoliotic heart disease, headache disorder, and trigeminal autonomic cephalalgia. Headache is a recognised adverse effect of terlipressin, which argues for caution in headache-related indications.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for open-angle glaucoma.

The only paper retrieved for the generic "glaucoma" prediction (PMID [31841026](https://pubmed.ncbi.nlm.nih.gov/31841026/), 2020) is a randomized trial on dobutamine reversing terlipressin's cardio-suppressive effects in cirrhosis. It is not about glaucoma and was treated as a false-positive match.

---

## Other Prediction with Supporting Literature: Pulmonary Hypertension

Pulmonary hypertension (TxGNN score 99.56%) is the only prediction in the top 10 with relevant literature. It reaches **L3** evidence, with a "Research Question" recommendation. No registered clinical trials were found.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22893473](https://pubmed.ncbi.nlm.nih.gov/22893473/) | 2012 | Small cohort | Hepatobiliary Pancreat Dis Int | In 7 cirrhotic patients with pulmonary hypertension, the first terlipressin dose (2 mg) decreased pulmonary vascular resistance |
| [21733953](https://pubmed.ncbi.nlm.nih.gov/21733953/) | 2012 | Small cohort | Angiology | Echo study comparing terlipressin's effects on pulmonary and systemic hemodynamics in cirrhosis with and without pulmonary hypertension |
| [18280605](https://pubmed.ncbi.nlm.nih.gov/18280605/) | 2008 | Case report | J Hepatol | Significant reduction in pulmonary arterial pressure after 1 week of terlipressin in portopulmonary hypertension |
| [15259082](https://pubmed.ncbi.nlm.nih.gov/15259082/) | 2004 | Echo study | World J Gastroenterol | Assessed terlipressin's effect on systolic pulmonary artery pressure in cirrhosis |
| [32999121](https://pubmed.ncbi.nlm.nih.gov/32999121/) | 2020 | Case report | Indian Pediatr | Rescue treatment of persistent pulmonary hypertension and refractory shock in a preterm infant |

**Caveats:**
- V1 agonism can also raise pulmonary vascular resistance in other settings, so effects are context-dependent.
- Much of the retrieved literature concerns portal hypertension, a different condition, and should not be counted as direct evidence.
- Some study designs could not be confirmed because titles and abstracts were truncated.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN17190P | TERLIPRESSIN-AFT Solution for Injection 0.85 mg/8.5 mL | Injection, solution | Not listed in the record |
| SIN14244P | GLYPRESSIN Solution for Injection 1 mg/8.5 mL | Injection, solution | Not listed in the record |

Both are valid single-ingredient licences, and neither is cancelled. They are injectable products only; no ophthalmic (eye-drop) formulation is registered, which is a further barrier for a glaucoma indication.

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the data compiled.
- **Theoretical concern**: Systemic vasoconstriction could, in principle, compromise ocular perfusion.
- **Adverse effect**: Headache is a recognised adverse effect of terlipressin.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The glaucoma predictions rest solely on a model score. There are no trials or relevant publications, no plausible mechanism, and no ophthalmic formulation, and there is a theoretical ocular perfusion concern. Pulmonary hypertension is the only prediction with any supporting data, and even that is small, mostly observational, and context-dependent.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, and the approved indications for the two Singapore licences
- Detailed mechanism-of-action data (for example, from DrugBank)
- A mechanistic or preclinical rationale linking V1 agonism to intraocular pressure, if glaucoma is to be pursued
- For pulmonary hypertension: a systematic review and well-designed prospective studies that separate pulmonary from portal hypertension populations, plus a safety assessment of pulmonary vascular resistance effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

