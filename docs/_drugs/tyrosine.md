---
layout: default
title: Tyrosine
parent: Low Evidence (L5)
nav_order: 1027
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

Tyrosine is an amino acid that Singapore markets as a component of amino acid infusion solutions. The TxGNN model predicts it may be effective for **cauda equina syndrome** with a very high score. However, there are **0 clinical trials** and only **1 publication** (a tumour case report with no treatment signal), so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the registration records. Marketed in amino acid infusion products |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 15 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Tyrosine is a building block for several important molecules: melanin, the catecholamines (dopamine and norepinephrine) and thyroid hormones. It is supplied in parenteral nutrition as a nutritional amino acid.

No therapeutic rationale for cauda equina syndrome was found. The only retrieved paper is a case report on a spinal nerve root tumour (clear cell sarcoma, previously diagnosed as melanotic schwannoma). It links tyrosine to the tumour's melanin-related histology, not to any treatment benefit. The high TxGNN score (0.998) is a graph-based prediction with no supporting clinical data. The similarity between the original and new indications has not yet been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17341045](https://pubmed.ncbi.nlm.nih.gov/17341045/) | 2006 | Case report | Neurosurgical focus | Clear cell sarcoma arising from the S-1 nerve root, previously diagnosed as psammomatous melanotic schwannoma. The paper is about tumour histology and does not test tyrosine as a treatment. |

## Singapore Market Information

Five of the 15 registrations are shown below. Approved indication text is not recorded for these products.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN11682P | AMINOVEN SOLUTION FOR INFUSION 5% | Injection |
| SIN11829P | AMINOVEN SOLUTION FOR INFUSION 10% | Injection |
| SIN16337P | AMINOVEN SOLUTION FOR INFUSION 15% | Infusion, solution |
| SIN08352P | AMINOPLASMAL-15% INFUSION | Injection |
| SIN07846P | TROPHAMINE INJECTION 10% | Injection |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found. Registered products are injectable or infusion forms, and their package inserts have not yet been reviewed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no clinical trials and no literature showing a therapeutic effect. The score is high, but nothing supports a plausible mechanism in cauda equina syndrome.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Evidence that tyrosine has a therapeutic role in cauda equina syndrome, such as preclinical or clinical studies
- Review of the other predicted indications. Among them, only postural orthostatic tachycardia syndrome has an indirect mechanistic rationale (L4, "Research Question"), and the direction of effect (supplementation vs. inhibition) is unresolved. The thyroid-related predictions (hyperthyroidism, hyperthyroxinemia) raise a possible safety concern. Several trial and literature matches are name-match artifacts from "tyrosine kinase inhibitor". One disease term (obsolete neurogenic bladder) is flagged obsolete in the ontology and needs remapping.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

