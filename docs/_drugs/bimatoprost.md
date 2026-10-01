---
layout: default
title: Bimatoprost
parent: Low Evidence (L5)
nav_order: 160
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

# Bimatoprost: From Glaucoma / Ocular Hypertension to Malformation Syndrome with Odontal and/or Periodontal Component

## One-Sentence Summary

Bimatoprost is a prostamide (FP-receptor agonist) eye-drop ingredient, marketed in Singapore as ophthalmic solutions for glaucoma and ocular hypertension.
The TxGNN model ranks **malformation syndrome with odontal and/or periodontal component** as its top prediction, but there are **0 clinical trials** and **20 publications**, none of which mention bimatoprost.
This prediction looks like a graph-propagation artifact, not a biological signal. The better-supported candidate is **alopecia** (see the end of this report).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / ocular hypertension (inferred from the ophthalmic product forms and the drug's known use; the registration indication text is not provided) |
| Predicted New Indication | Malformation syndrome with odontal and/or periodontal component |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the DrugBank record. Bimatoprost is described as a prostamide/FP-receptor agonist. It lowers intraocular pressure in glaucoma and also prolongs the hair-growth (anagen) phase, which is why it is used for eyelash growth.

**No credible mechanistic link was found** between FP-receptor agonism and a dental or periodontal malformation syndrome. The very high score (0.99997, rank 118) appears to come from the structure of the knowledge graph rather than from biology. The 20 retrieved publications are general periodontitis literature. They cover diabetes and periodontitis, treatment guidelines, plaque microbiology, and surgical techniques, and none of them discuss bimatoprost.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The 10 publications below are the highest-priority items retrieved. All are general periodontitis literature, and **none mention bimatoprost**, so they do not support this prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35420698](https://pubmed.ncbi.nlm.nih.gov/35420698/) | 2022 | Systematic Review | Cochrane Database Syst Rev | Periodontitis treatment and glycaemic control in people with diabetes |
| [35688447](https://pubmed.ncbi.nlm.nih.gov/35688447/) | 2022 | Guideline | J Clin Periodontol | EFP clinical practice guideline for stage IV periodontitis |
| [22057194](https://pubmed.ncbi.nlm.nih.gov/22057194/) | 2012 | Review | Diabetologia | Two-way relationship between periodontitis and diabetes |
| [37435999](https://pubmed.ncbi.nlm.nih.gov/37435999/) | 2023 | Review | Periodontol 2000 | Complications and errors in regenerative periodontal surgery |
| [36883660](https://pubmed.ncbi.nlm.nih.gov/36883660/) | 2023 | Review | J Dent Res | Role of gingival fibroblasts in periodontitis pathogenesis |
| [38907216](https://pubmed.ncbi.nlm.nih.gov/38907216/) | 2024 | Review | J Nanobiotechnology | Biomaterial-mediated macrophage immunotherapy for periodontitis |
| [29193334](https://pubmed.ncbi.nlm.nih.gov/29193334/) | 2018 | Review | Periodontol 2000 | Peri-implant vs periodontal soft tissues in health and disease |
| [9495612](https://pubmed.ncbi.nlm.nih.gov/9495612/) | 1998 | Observational | J Clin Periodontol | Microbial complexes in subgingival plaque (185 subjects) |
| [38362600](https://pubmed.ncbi.nlm.nih.gov/38362600/) | 2024 | Clinical study | J Dent Res | Effect of periodontitis and its treatment on oral and gut microbiota |
| [37452425](https://pubmed.ncbi.nlm.nih.gov/37452425/) | 2023 | Preclinical | Adv Sci (Weinh) | Melatonin-engineered M2 macrophage exosomes for periodontitis therapy |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN16938P | LUMIGAN PF (Bimatoprost Ophthalmic Solution) 0.03% | Sterile solution | Allergan Pharmaceuticals Ireland |
| SIN14365P | LUMIGAN (Bimatoprost Ophthalmic Solution) 0.01% | Sterile solution | Allergan Pharmaceuticals Ireland |
| SIN13589P | Ganfort Eye Drops | Sterile solution | Allergan Pharmaceuticals Ireland |
| SIN14966P | GANFORT PF Eye Drops (Bimatoprost 0.3 mg/ml, Timolol 5.0 mg/ml) | Sterile solution | Allergan Pharmaceuticals Ireland |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no bimatoprost-specific literature, and no plausible mechanism. It is L5 (model prediction only), and the high TxGNN score is not supported by biology.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any biological rationale linking FP-receptor agonism to periodontal or dental malformation. Without one, this prediction should not be pursued.

**Better-supported candidate: alopecia (predicted rank 8, score 99.993%, L2, "Research Question").**
- **Trials:** Completed Phase 2 scalp trials exist in men with androgenetic alopecia (NCT01904721, n=244; NCT01325337, n=307) and in women with female pattern hair loss (NCT01325350, n=306). A Phase 4 pediatric eyelash hypotrichosis trial (NCT01023841, n=71) also exists.
- **Gaps:** There is no Phase 3 scalp trial, and efficacy outcomes are not included in the data.
- **Suggested action:** Evaluate this indication separately.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

