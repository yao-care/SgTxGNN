---
layout: default
title: Varenicline
parent: Low Evidence (L5)
nav_order: 1056
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Varenicline: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the Singapore licence records compiled for this report"
monitor_inn: "Varenicline"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "alopecia", "open-angle glaucoma", "primary hereditary glaucoma", "headache disorder", "pulmonary hypertension"]
---

# Varenicline
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

# Varenicline: From Smoking Cessation to Migraine Disorder

## One-Sentence Summary

Varenicline is a nicotinic receptor partial agonist, marketed in Singapore as Champix. The TxGNN model predicts it may be effective for **migraine disorder**, but no clinical trials and no efficacy publications support this direction. The prediction is based on computational modelling only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records compiled for this report |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From the pharmacology of the drug class, varenicline is a partial agonist of α4β2 nicotinic acetylcholine receptors and a full agonist of α7 receptors. It is widely known as a smoking cessation aid, although the Singapore licence records do not state the indication text.

Nicotinic cholinergic signalling has been loosely linked to trigeminovascular and cortical spreading depression pathways, both of which are involved in migraine. However, no direct evidence supports a therapeutic role in migraine. The high TxGNN score is a computational prediction only and should not be read as evidence of efficacy.

Other predictions were also generated, including migraine with brainstem aura, hair disorders (alopecia, hypotrichosis), glaucoma, headache disorder and pulmonary hypertension. All are at evidence level L5 with a "Hold" recommendation. For headache disorder, the retrieved literature reflects keyword overlap with adverse-event reports (headache is a known side effect of varenicline), not treatment evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19585710](https://pubmed.ncbi.nlm.nih.gov/19585710/) | 2009 | Case report | Therapie | Cardiac arrest reported with varenicline; a safety report, not evidence of benefit in migraine |

This is the only publication retrieved for migraine disorder. It describes an adverse event and provides no support for efficacy.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13323P | Champix Tablet 1mg | Film-coated tablet | Not stated in the compiled data |
| SIN13322P | Champix Tablet Starter Pack | Film-coated tablet | Not stated in the compiled data |

Both licences are valid single-ingredient products from Pfizer Italia S.r.l. and are oral formulations. No licences have been cancelled.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (derived from drug-disease edges in the TxGNN knowledge graph, not from label text): anxiety disorder, neurotic disorder, dysthymic disorder, bipolar disorder, major affective disorder, substance abuse/dependence, schizophrenia, acute coronary syndrome, peripheral vascular disease, intermittent vascular claudication and peripheral arterial disease.
- **Drug interactions**: 100 interactions were identified in total. The only one with a graded severity among those listed is cimetidine (Minor). Others, such as phentermine, metformin, glimepiride, omeprazole, pantoprazole, morphine and simvastatin, have no severity grade assigned.
- **Related safety literature**: the EAGLES randomised trial (PMID 27116918) examined neuropsychiatric safety in smokers with and without psychiatric disorders, and case reports describe cardiac arrest and bath-related headache with varenicline.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (evidence level L5). There are no clinical trials, no efficacy literature in migraine, and only a speculative mechanistic link. Headache is a known adverse effect of varenicline, which argues against a treatment role. The knowledge graph also flags several psychiatric and cardiovascular contraindication signals, and the package insert warnings have not been reviewed.

**To proceed, the following is needed:**
- The Singapore package insert warnings and contraindications (HSA), and the approved indication text
- Detailed mechanism of action data (for example from DrugBank)
- Preclinical or mechanistic studies supporting nicotinic receptor modulation in migraine
- A literature review specifically on migraine treatment, with adverse-event reports excluded
- A safety assessment for populations with psychiatric or cardiovascular conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

