---
layout: default
title: Tryptophan
parent: Medium Evidence (L3-L4)
nav_order: 1034
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Tryptophan: predicted new indication Restless legs syndrome (evidence level L3). Approved use: Not stated in the registration records"
---

# Tryptophan
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Tryptophan: From Parenteral Amino Acid Nutrition to Restless Legs Syndrome

## One-Sentence Summary

Tryptophan is an essential amino acid supplied in Singapore as a component of parenteral nutrition and amino acid infusion products.
The TxGNN model ranks **restless legs syndrome** as its top predicted new indication, with a score of 99.7%. However, there are **no registered clinical trials** and only **2 small, dated clinical reports (1986-1987)** supporting this direction.
The most evidence-supported candidate is actually **insomnia**, which has a 1983 controlled study and a small 1987 study of L-tryptophan, though current guidelines do not endorse it.

> This report evaluates the top-ranked prediction (restless legs syndrome) in detail and summarises the other nine predictions briefly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records (the 19 licences are for amino acid infusion and parenteral nutrition products) |
| Predicted New Indication | Restless legs syndrome |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 19 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known information, tryptophan is the metabolic precursor of serotonin (via 5-hydroxytryptophan) and of melatonin. It is an essential nutrient, supplied in Singapore only as one ingredient of multi-amino-acid infusions.

Restless legs syndrome (RLS) is thought to involve dopaminergic pathways and iron metabolism, with some serotonergic influence. Two small clinical reports from the 1980s examined L-tryptophan in RLS and periodic leg movements (PMIDs 3953904 and 3659737). However, pharmacovigilance data show that serotonergic antidepressants can cause or worsen movement disorders, including RLS. This suggests that boosting serotonin signalling is not clearly beneficial and may even be harmful in this condition.

The prediction is therefore biologically plausible but not convincingly supported. No modern controlled data exist.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3953904](https://pubmed.ncbi.nlm.nih.gov/3953904/) | 1986 | Clinical study | Am J Psychiatry | L-tryptophan in the treatment of restless legs syndrome (no abstract available) |
| [3659737](https://pubmed.ncbi.nlm.nih.gov/3659737/) | 1987 | Clinical study | Sleep | Periodic leg movement with L-dopa, 5-hydroxytryptophan and L-tryptophan (no abstract available) |
| [33836477](https://pubmed.ncbi.nlm.nih.gov/33836477/) | 2021 | Systematic review / meta-analysis | Sleep Med Rev | RLS in chronic liver disease; elevated tryptophan and altered dopamine turnover are discussed as possible contributors |
| [1305630](https://pubmed.ncbi.nlm.nih.gov/1305630/) | 1992 | Review | Int J Neurosci | L-tryptophan in neuropsychiatric disorders; serotonin abnormalities linked to several movement disorders |
| [36897462](https://pubmed.ncbi.nlm.nih.gov/36897462/) | 2023 | Case series | Neurol Sci | RLS in DNAJC12 deficiency, a disorder of impaired dopamine and serotonin neurotransmission |
| [32546134](https://pubmed.ncbi.nlm.nih.gov/32546134/) | 2020 | Pharmacovigilance study | BMC Psychiatry | Antidepressants are associated with movement disorders; serotonergic modulation may not be beneficial in RLS |

---

## Singapore Market Information

All 19 licences are valid single-ingredient registrations. No approved indication text was recorded for any of them. The five main ones are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16337P | Aminoven Solution for Infusion 15% | Infusion, solution | Not recorded |
| SIN11682P | Aminoven Solution for Infusion 5% | Injection | Not recorded |
| SIN11829P | Aminoven Solution for Infusion 10% | Injection | Not recorded |
| SIN06299P | Nephrosteril for Intravenous Infusion | Injection | Not recorded |
| SIN08352P | Aminoplasmal-15% Infusion | Injection | Not recorded |

The remaining registrations include Trophamine, Nutrineal PD4, Vaminolact, Aminoplasmal B. Braun 10% E, Oliclinomel, SmofKabiven (several variants) and Nutriflex Omega products. All are injectable, emulsion or sterile-solution forms; no oral tryptophan product appears among them.

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: autoimmune disease, systemic lupus erythematosus (including paediatric), anxiety disorder, neurotic disorder, dysthymic disorder, schizophrenia, phenylketonuria and other disorders of phenylalanine metabolism, and eosinophilia-myalgia syndrome (including the tryptophan-associated form).
- **Drug Interactions**: 17 interactions were identified.
  - **Major (10)**: lorcaserin, dolasetron, palonosetron, ondansetron, fenfluramine, granisetron, sibutramine, methylene blue, doxepin (oral and topical), and procarbazine. Serotonin syndrome is the main concern with serotonergic agents and MAO-inhibiting drugs.
  - **Moderate (7)**: morphine, codeine, hydrocodone, cyproheptadine, ozanimod, ifosfamide.
- **Product quality**: historic eosinophilia-myalgia syndrome (EMS) associated with contaminated L-tryptophan supplements is a relevant quality concern for any oral product.

Package insert warnings and contraindications were not available; please refer to the package insert for label safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Restless legs syndrome has a high model score but only two small 1980s clinical reports, no registered trials, and pharmacovigilance signals suggesting serotonergic modulation may not help. The evidence is insufficient to justify advancing this indication.

**Other predicted indications (brief):**

| Rank | Indication | Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 2 | Primary hereditary glaucoma | 99.57% | L5 | Hold |
| 3 | Open-angle glaucoma | 99.50% | L4 | Hold (observational metabolomic data only) |
| 4 | Insomnia | 99.47% | L3 | Proceed with Guardrails |
| 5 | Methemoglobinemia | 99.30% | L5 | Hold |
| 6 | Methemoglobinemia, alpha type | 99.18% | L5 | Hold |
| 7 | Methemoglobin reductase deficiency | 99.08% | L5 | Hold |
| 8 | Congenital prothrombin deficiency | 99.01% | L5 | Hold |
| 9 | Acne | 98.60% | L4 | Hold (preclinical, microbial-metabolite data only) |
| 10 | Pregnancy-associated osteoporosis | 98.59% | L5 | Hold |

**Insomnia is the most developed alternative.** A 1983 controlled study (PMID 6410442, 96 patients) compared 1 g L-tryptophan with flurazepam, secobarbital and placebo. A 1987 study (PMID 3432358) reported improved sleep in 19 of 25 patients with severe chronic insomnia on 2 g L-tryptophan. Recent work is mostly preclinical or combination-product based, and the 2017 AASM guideline (PMID 27998379) does not endorse tryptophan. Any pursuit would need guardrails for serotonergic interactions and product quality.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the registered products (currently missing and blocking safety screening)
- Mechanism of action data
- Modern, adequately powered randomised controlled trials in RLS (or, with higher priority, insomnia), with a defined oral formulation and dose
- A serotonin-syndrome risk management plan covering the interacting drugs listed above
- Route compatibility assessment, since all registered Singapore products are parenteral while an RLS or insomnia use would most likely require an oral product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

