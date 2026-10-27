---
layout: default
title: Glycopyrronium
parent: Low Evidence (L5)
nav_order: 488
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Glycopyrronium: predicted new indication Irritable bowel syndrome (evidence level L5). Approved use: Not stated in the licence records compiled for this report (the regis…"
monitor_inn: "Glycopyrronium"
predicted_indications: ["irritable bowel syndrome", "cauda equina syndrome", "obsolete neurogenic bladder (disease)", "neurocirculatory asthenia", "migraine disorder", "migraine with brainstem aura", "open-angle glaucoma", "autonomic nervous system disease", "primary hereditary glaucoma", "dysthymic disorder"]
---

# Glycopyrronium
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

## Glycopyrronium: From Respiratory Disease (Inhaled Formulations) to Irritable Bowel Syndrome
{: .text-alpha }

## One-Sentence Summary

Glycopyrronium is an antimuscarinic (anticholinergic) drug, marketed in Singapore mainly as an inhaled product, either alone or as part of combination inhalers.
The TxGNN model predicts it may be effective for **irritable bowel syndrome** (top-ranked prediction), but **no clinical trials and no publications** currently support this specific direction, so the prediction rests on model output and pharmacology alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records compiled for this report (the registered products are inhaled formulations) |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 98.84% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Glycopyrronium is a quaternary ammonium antimuscarinic. It blocks muscarinic receptors, which reduces smooth muscle spasm and glandular secretions. Detailed mechanism-of-action data is not available in the data compiled for this report, so this description relies on general pharmacology.

Irritable bowel syndrome, especially the pain and cramping subtype, is commonly treated with antispasmodic anticholinergic drugs. Reduced gastrointestinal smooth muscle spasm is therefore a plausible mechanism, which is consistent with the model's high score.

However, no trial or literature evidence was found for this indication. The link remains theoretical. Other predicted indications were also reviewed (see below), and most are weak or even conflict with known pharmacology.

### Other Predicted Indications (All Currently Low Evidence)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Cauda equina syndrome | 98.51% | L5 | Indirect; may relieve bladder symptoms only, not the underlying cause |
| 3 | Neurogenic bladder (term flagged obsolete) | 97.73% | L5 | Antimuscarinics are an established class here, but the disease term should be mapped to a current one |
| 4 | Neurocirculatory asthenia | 96.91% | L5 | Weak, speculative rationale |
| 5 | Migraine disorder | 96.08% | L5 | Poor central nervous system penetration; mechanism unclear |
| 6 | Migraine with brainstem aura | 95.68% | L5 | Likely reflects the generic migraine association |
| 7 | Open-angle glaucoma | 95.61% | L5 | Conflicts with known pharmacology (raised intraocular pressure risk); safety signal |
| 8 | Autonomic nervous system disease | 95.55% | L4 | Only indirect evidence (see below) |
| 9 | Primary hereditary glaucoma | 95.30% | L5 | Same safety concern as open-angle glaucoma |
| 10 | Dysthymic disorder | 93.68% | L5 | No clear rationale |

---

## Clinical Trial Evidence

Currently no clinical trials are registered for irritable bowel syndrome.

The only trial found among the lower-ranked predictions (autonomic nervous system disease) is shown below for reference. It is indirect and does not test glycopyrronium as a treatment for an autonomic disorder.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02872090](https://clinicaltrials.gov/study/NCT02872090) | Phase 4 | Completed | 42 | Randomised, double-blind, cross-over study of the effect of long-acting bronchodilators (tiotropium, glycopyrronium, indacaterol) on cardiac autonomic nervous system control in mild COPD; a physiology and safety endpoint, not efficacy for an autonomic disease |

---

## Literature Evidence

Currently no related literature is available for irritable bowel syndrome.

The only publication found, for the autonomic nervous system disease prediction, is shown for reference:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37714301](https://pubmed.ncbi.nlm.nih.gov/37714301/) | 2024 | Review | Actas Dermo-Sifiliográficas | Narrative review of topical anticholinergics for focal hyperhidrosis in adults and children; indirect support only |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14431P | Seebri Breezhaler Inhalation Powder, Hard Capsule 50 mcg | Capsule | Not listed in the data |
| SIN14539P | Ultibro Breezhaler Inhalation Powder Hard Capsule 110/50 mcg | Capsule | Not listed in the data |
| SIN16153P | Enerzair Breezhaler Inhalation Powder, Hard Capsule 150/50/160 mcg | Powder, metered | Not listed in the data |
| SIN15924P | Trimbow Pressurised Inhalation Solution 100/6/12.5 µg per actuation | Aerosol, metered | Not listed in the data |
| SIN17226P | Trimbow Pressurised Inhalation Solution 200/6/12.5 µg per actuation | Aerosol, metered | Not listed in the data |

A sixth licence, SIN16723P (Breztri Aerosphere Pressurised Inhalation Suspension 160/7.2/5 mcg per actuation, aerosol, metered), is also valid. All six registrations are inhaled products, so no oral or other route suitable for gastrointestinal use is registered locally.

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

**Drug Interactions**: The interaction screen returned 100 interacting drugs, mostly of Moderate severity. Examples from the listed results:
- **Other anticholinergics** (additive effects): aclidinium, hyoscyamine, homatropine, amitriptyline, chlorpheniramine, acrivastine, phenyltoloxamine
- **Opioids and central nervous system depressants**: fentanyl, alfentanil, codeine, dihydrocodeine, tramadol, ethanol
- **Others**: botulinum toxin type A, acebutolol, amantadine, loperamide, acetylcholine
- **Minor**: acetaminophen, hydrochlorothiazide

**Pharmacology-based concern**: For the predicted glaucoma indications, antimuscarinics can cause mydriasis and raise intraocular pressure, and are generally cautioned or contraindicated in angle-closure glaucoma. This should be treated as a safety signal, not a therapeutic opportunity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The irritable bowel syndrome prediction is mechanistically plausible, as antispasmodic anticholinergics are used in this condition. However, there are no trials or publications for it (Evidence Level L5), and the locally registered products are all inhaled formulations.

**To proceed, the following is needed:**
- A systematic literature and trial search for glycopyrronium (or oral or other systemic anticholinergics) in irritable bowel syndrome
- Package insert warnings and contraindications from the Health Sciences Authority (HSA) website, which are currently missing and block safety screening
- Detailed mechanism-of-action data from DrugBank
- Route and formulation compatibility assessment (the registered inhaled products may not deliver gastrointestinal effects)
- Clarification of the original approved indications, which are blank in the licence records
- Mapping of the obsolete neurogenic bladder term to a current disease term, if that indication is to be reviewed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

