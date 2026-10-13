---
layout: default
title: Tyrosine
parent: Low Evidence (L5)
nav_order: 1037
evidence_level: L5
indication_count: 10
---

# Tyrosine
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

# Tyrosine: From Parenteral Nutrition Amino Acid Component to Cauda Equina Syndrome

## One-Sentence Summary

Tyrosine is an amino acid used as a component of parenteral nutrition (amino acid infusion) products marketed in Singapore.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** supporting this specific indication.
Among the other top-ranked predictions, only hyperthyroidism has a registered trial, and that trial is not of tyrosine alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (the products are amino acid infusion and nutrition products) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 15 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Tyrosine is a known amino acid and a precursor of catecholamines (dopamine and norepinephrine) and of thyroid hormones. It is supplied in Singapore as a component of parenteral nutrition products.

For cauda equina syndrome, no mechanistic link was identified in the data compiled for this report. The condition is a compressive injury of the nerve roots of the cauda equina, and nothing in the data connects catecholamine precursor supply to that injury. The high score (0.998) is a graph-based prediction only and should be read as a hypothesis, not as evidence.

Other top-ranked predictions show the same pattern:
- **Hyperthyroidism, hyperthyroxinemia, and thyroid hormone resistance**: Tyrosine is a substrate for thyroid hormone synthesis, but supplying more substrate would be expected to be neutral or unfavorable when the goal is to lower hormone activity. This is a safety concern as well as a lack of evidence.
- **Postural orthostatic tachycardia syndrome**: A link to autonomic function is plausible, since tyrosine is a catecholamine precursor. However, the only paper retrieved is a case report of chronic fatigue syndrome treated with alpha-methyl-p-tyrosine, a tyrosine hydroxylase inhibitor that acts opposite to tyrosine.
- **Glaucoma-related conditions (angle-closure, traumatic, neovascular, aqueous misdirection)**: None of the retrieved papers tests tyrosine as a treatment. Two predictions share an identical score, which suggests they are driven by shared graph neighbours rather than tyrosine-specific biology.
- **Obsolete neurogenic bladder (disease)**: The term is flagged as obsolete in the ontology and needs to be mapped to a current term before any assessment.

---

## Clinical Trial Evidence

For the top prediction (cauda equina syndrome), currently no related clinical trials are registered.

The only trial found among the top 10 predictions is for hyperthyroidism:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06264544](https://clinicaltrials.gov/study/NCT06264544) | Not applicable | Not yet recruiting | 150 | Placebo-controlled trial of a zinc, selenium, and L-tyrosine supplement for preventing thyrotoxicosis in people with the SEPP1 r25191G/A polymorphism and raised TPOAb. Tyrosine is part of a combination, so it gives no direct evidence for tyrosine alone. No results are available. |

---

## Literature Evidence

For the top prediction (cauda equina syndrome), currently no related literature is available.

The most relevant publications among the other predictions are listed below. None tests tyrosine as a treatment.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39063020](https://pubmed.ncbi.nlm.nih.gov/39063020/) | 2024 | Case report | Int J Mol Sci | Chronic fatigue syndrome responded to alpha-methyl-p-tyrosine, a tyrosine hydroxylase inhibitor. This is the opposite of tyrosine supplementation, and the condition is not POTS. |
| [42812246](https://pubmed.ncbi.nlm.nih.gov/42812246/) | 2026 | Cohort | Front Med | Plasma amino acid alterations are associated with ocular parameters in early primary angle-closure glaucoma. This is a biomarker association, not evidence of benefit. |
| [36848916](https://pubmed.ncbi.nlm.nih.gov/36848916/) | 2023 | Review | Lancet Diabetes Endocrinol | General review of hyperthyroidism causes, diagnosis, and management. Does not address tyrosine therapy. |
| [35087972](https://pubmed.ncbi.nlm.nih.gov/35087972/) | 2021 | Review | Rom J Ophthalmol | Review of neovascular glaucoma. Treatment centres on VEGF inhibition, with no link to tyrosine. |
| [10579356](https://pubmed.ncbi.nlm.nih.gov/10579356/) | 1999 | Mechanistic study | Endocrinology | Thyroid hormone receptor beta mutations that impair ligand binding in thyroid hormone resistance. Does not test tyrosine. |
| [15135777](https://pubmed.ncbi.nlm.nih.gov/15135777/) | 2004 | Review | Growth Horm IGF Res | Molecular mechanisms of end-organ hormone resistance. Does not test tyrosine. |

---

## Singapore Market Information

All 15 registrations are valid single-ingredient products. The registration data contain no approved indication text. The five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11682P | AMINOVEN SOLUTION FOR INFUSION 5% | Injection | Not stated |
| SIN11829P | AMINOVEN SOLUTION FOR INFUSION 10% | Injection | Not stated |
| SIN16337P | AMINOVEN SOLUTION FOR INFUSION 15% | Infusion, solution | Not stated |
| SIN08352P | AMINOPLASMAL-15% INFUSION | Injection | Not stated |
| SIN07846P | TROPHAMINE INJECTION 10% | Injection | Not stated |

The remaining 10 registrations include amino acid, peritoneal dialysis, and multi-chamber parenteral nutrition products (for example Nutrineal PD4, Vaminolact, Aminoplasmal B.Braun 10% E, Oliclinomel, and SmofKabiven variants).

---

## Safety Considerations

Please refer to the package insert for safety information.

One point can be noted from the predictions themselves: for the thyroid-related predictions (hyperthyroidism, hyperthyroxinemia), tyrosine is a substrate for thyroid hormone synthesis, so supplementation could be unfavorable in those patients. This needs to be assessed before any further work in these indications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for cauda equina syndrome rests only on a graph-based score, with no clinical trials, no literature, and no identified mechanism. The same is true of the other top predictions. For the thyroid-related predictions, the biology suggests possible harm rather than benefit.

**To proceed, the following is needed:**
- Detailed mechanism of action data, and a plausible mechanistic link between tyrosine and the target condition
- Package insert warnings and contraindications from the HSA, which are currently missing and block safety screening
- Approved indication text for the Singapore registrations, to define the original indication
- A targeted literature and trial search on tyrosine itself for the predicted indications, excluding tyrosine kinase inhibitor papers
- Mapping of the obsolete neurogenic bladder term to a current ontology term
- Route and formulation compatibility assessment, since current products are all parenteral nutrition formulations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

