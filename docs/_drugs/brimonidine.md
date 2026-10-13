---
layout: default
title: Brimonidine
parent: Medium Evidence (L3-L4)
nav_order: 174
evidence_level: L4
indication_count: 10
---

# Brimonidine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Brimonidine: From Open-Angle Glaucoma to Papillary Conjunctivitis

## One-Sentence Summary

Brimonidine is an alpha-2 adrenergic agonist originally used to treat open-angle glaucoma and ocular hypertension, and in topical form for facial redness in rosacea.
The TxGNN model predicts it may be associated with **papillary conjunctivitis**, but the **3 publications** found describe brimonidine as a *cause* of conjunctivitis, not a treatment, and there are **no registered clinical trials**.
This prediction most likely reflects an adverse-effect signal in the knowledge graph rather than therapeutic potential.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma, ocular hypertension, rosacea (from the knowledge graph; approved indication text is not available in the Singapore licence records) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 9 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, brimonidine is an alpha-2 adrenergic agonist. In the eye it lowers intraocular pressure by reducing aqueous humour production and increasing uveoscleral outflow. On the skin, it constricts small blood vessels, which reduces rosacea-related redness.

The link between the original indications and papillary conjunctivitis is weak. The literature describes brimonidine as a known cause of allergic, follicular or papillary conjunctivitis, as well as anterior uveitis and conjunctival lesions with long-term use. The high TxGNN score therefore most likely reflects a drug-disease association in the knowledge graph, such as an adverse-effect or shared-pathway signal. It does not indicate therapeutic benefit. Nothing in the data supports therapeutic use for this condition, and there is a clear signal of potential harm.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18303383](https://pubmed.ncbi.nlm.nih.gov/18303383/) | 2008 | Case series (adverse event) | Journal of Glaucoma | Bilateral anterior uveitis and granulomatous papillary conjunctivitis in a 78-year-old man after 2 years of brimonidine therapy |
| [38992579](https://pubmed.ncbi.nlm.nih.gov/38992579/) | 2024 | Retrospective cohort | BMC Ophthalmology | Compared ocular allergy prevalence in glaucoma patients using brinzolamide/brimonidine fixed combination with and without a β-blocker |
| [37352771](https://pubmed.ncbi.nlm.nih.gov/37352771/) | 2023 | Case report (adverse event) | International Journal of Surgery Case Reports | Atypical salmon patch-like conjunctival lesion after long-term topical brimonidine; allergic follicular or papillary conjunctivitis is noted as a well-known side effect |

---

## Singapore Market Information

The approved indication text is not available in the Singapore licence records for any of these products.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN17198P | ALPHAGAN P Ophthalmic Solution 0.1% w/v | Sterile solution | Not available |
| SIN12336P | ALPHAGAN P Ophthalmic Solution 0.15% w/v | Solution | Not available |
| SIN09788P | ALPHAGAN Ophthalmic Solution 0.2% | Solution | Not available |
| SIN14828P | MIRVASO Gel 3 mg/g | Gel (topical) | Not available |
| SIN15085P | SIMBRINZA Eye Drops, Suspension 10 mg/ml + 2 mg/ml | Sterile suspension | Not available |

Four further licences are valid but not listed here: SIN17034P (Rimonal), SIN15099P (Brimochek), SIN13406P (Combigan) and SIN15191P (Brimochek-T).

---

## Safety Considerations

- **Conditions flagged in the knowledge graph as contraindications** (these come from knowledge-graph drug-disease edges, not from package insert text):
  - Cardiovascular and circulatory: orthostatic hypotension, multiple system atrophy, postural orthostatic tachycardia syndrome, atrioventricular block, cerebrovascular disorder, Raynaud disease, thromboangiitis obliterans
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hypoglycemia, hyperthyroidism, Graves disease, thyrotoxicosis
  - Neuromuscular: myasthenia gravis (including adult-onset), neuromuscular junction disease
  - Respiratory: pulmonary emphysema, bronchial disease
  - Psychiatric: anxiety disorder, neurotic disorder, dysthymic disorder
  - Other: anaphylaxis
- **Drug interactions**: 100 potential interactions were identified, but none has a severity grade. Examples include calcitriol, phentermine, pantoprazole, glimepiride, metformin, omeprazole, atropine, simvastatin, prednisone and hydrocortisone. These need pharmacist review.
- **Adverse reactions in the literature**: allergic and follicular conjunctivitis, anterior uveitis, conjunctival lesions, ocular lichen planus, and periorbital contact dermatitis.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only evidence for papillary conjunctivitis shows brimonidine causing the condition, not treating it, and there are no clinical trials. The high TxGNN score appears to reflect an adverse-effect association, so there is no basis for therapeutic development.

**Other predictions in the top 10:**
- **Rosacea conjunctivitis** (98.49% is for rank 1; this one scores 94.65%) is the only one flagged as a research question. Topical brimonidine is already used for facial redness in rosacea, so there is some biological plausibility for the ocular form. However, no trials or literature were supplied, and brimonidine's conjunctival side effects could worsen ocular surface inflammation.
- **Primary hereditary glaucoma** is mechanistically plausible but essentially an extension of the existing glaucoma indication. Alpha-2 agonists carry paediatric safety concerns (CNS depression, apnoea, bradycardia in infants), which matter because hereditary glaucoma often presents in childhood.
- **Lichen-related conditions** (lichen disease, hypertrophic lichen planus, lichen planus pigmentosus, annular atrophic lichen planus): case reports show brimonidine inducing lichenoid reactions, which argues against therapeutic use.
- **Hair disorders** (congenital hypotrichosis milia, hypotrichosis simplex of the scalp, diffuse alopecia areata): computational predictions only, with no plausible mechanism.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, since safety screening cannot proceed without them
- Mechanism of action data from DrugBank
- Approved indication text for the Singapore licences
- Controlled clinical evidence for any ocular surface indication, such as ocular rosacea, before further consideration
- A paediatric safety assessment if hereditary glaucoma is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

