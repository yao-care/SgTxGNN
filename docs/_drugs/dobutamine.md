---
layout: default
title: Dobutamine
parent: Low Evidence (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dobutamine: predicted new indication Alopecia (evidence level L5). Approved use: Not stated in the HSA licence data (injectable inotrope…"
monitor_inn: "Dobutamine"
predicted_indications: ["alopecia", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "open-angle glaucoma", "Raynaud disease", "primary hereditary glaucoma", "headache disorder", "hypertrichosis (disease)", "migraine disorder"]
---

# Dobutamine
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

## Dobutamine: From Acute Cardiac Inotropic Support to Alopecia
{: .text-alpha }

## One-Sentence Summary

Dobutamine is an injectable beta-1 adrenergic inotrope. The HSA licence text on file gives no approved indication wording, so the original use is inferred from its known pharmacology rather than taken from the licence.
The TxGNN model predicts it may be effective for **alopecia**, but there are **0 clinical trials** and only **1 publication** (a veterinary case report that does not test dobutamine as a treatment).
The prediction is therefore model-only, with no credible supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the HSA licence data (injectable inotrope, cardiac support) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, dobutamine is a beta-1 adrenergic agonist given intravenously to increase cardiac contractility, for example in acute heart failure or low-output states.

The prediction has no credible mechanistic basis. Dobutamine has no known action on hair follicles. The high score is most likely an artefact of the knowledge graph, which links cardiovascular drugs to hair-growth conditions through shared associations such as minoxidil, a vasodilator used for hair growth. The only retrieved paper describes heart failure caused by minoxidil poisoning in a cat, in which dobutamine was used only to treat low blood pressure. It does not evaluate dobutamine for alopecia.

Other top-ranked predictions (hypotrichosis, diffuse alopecia areata, hypertrichosis, glaucoma, Raynaud disease, headache, migraine) show the same pattern: high scores with no trials and no supporting literature. Headache in particular is more likely an adverse-effect signal than a treatment indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | Case report (veterinary) | J Vet Cardiol | Heart failure from minoxidil poisoning in a cat; dobutamine was used only for hypotension, not for hair loss |

This is the only publication retrieved for alopecia, and it does not support dobutamine as a treatment.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08702P | Dobutamine Injection 12.5 mg/ml (Hospira, Inc.) | Injection | Not stated in the licence data |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (from the TxGNN knowledge graph, not from label text):
  - Hypertension and hypertensive disorders
  - Atrial fibrillation
  - Aortic stenosis (including aortic valve disease and supravalvular aortic stenosis)
  - Myocardial infarction and coronary thrombosis
  - Hypertrophic cardiomyopathy (including the familial form)
  - Potassium deficiency
  - Hemoglobinopathy
- **Drug Interactions**: The database lists 100 interactions. The 20 retrieved are all rated Moderate. They are mainly:
  - Antidiabetic agents: acarbose, metformin, pioglitazone, repaglinide, chlorpropamide, and the DPP-4 inhibitors (alogliptin, linagliptin), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), GLP-1 agonists (albiglutide, dulaglutide, liraglutide, semaglutide), and insulins (aspart, degludec)
  - Sympathomimetic anorectics: phentermine and diethylpropion
  - Others: cimetidine and vancomycin

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials, no supporting literature, and no plausible mechanism linking a beta-1 inotrope to hair-follicle biology. Dobutamine is an intravenous hospital drug with cardiovascular contraindications, so a systemic route for a non-life-threatening cosmetic or dermatological condition would be hard to justify.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA, and the approved indication text for the licence
- Mechanism of action data from DrugBank
- Preclinical evidence of an effect on hair follicles or hair growth
- Assessment of whether a topical route is feasible, since only an injectable form is registered in Singapore
- Re-examination of whether the alopecia prediction is a minoxidil-related knowledge-graph artefact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

