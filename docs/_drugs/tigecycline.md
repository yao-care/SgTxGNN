---
layout: default
title: Tigecycline
parent: Low Evidence (L5)
nav_order: 980
evidence_level: L5
indication_count: 10
---

# Tigecycline
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

# Tigecycline: From Bacterial Infections to Disorder of Tyrosine Metabolism

## One-Sentence Summary

Tigecycline is a glycylcycline-class injectable antibiotic, currently marketed in Singapore under 2 registrations.
The TxGNN model predicts it may be effective for **disorder of tyrosine metabolism**, but only **1 clinical trial** and **4 publications** were retrieved, and none addresses this disease. They are keyword matches on "tyrosine kinase" in leukaemia and lung cancer research, so this is effectively a **model-only prediction**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (antibiotic). The Singapore registration records contain no indication text. |
| Predicted New Indication | Disorder of tyrosine metabolism |
| TxGNN Prediction Score | 95.76% |
| Evidence Level | L4 (preclinical or mechanism-level material only, none specific to this disease) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Tigecycline is a tetracycline-derived antibiotic with a bacteriostatic effect. It is known to inhibit mitochondrial translation, which can alter cellular energy metabolism.

The link to tyrosine metabolism is weak. No data connect tigecycline to the enzymes of tyrosine catabolism. The only tangential signal is an in vitro study of tigecycline's effect on melanocytes and fibroblasts, since melanocytes use tyrosine for melanin synthesis. That study concerns pigmentation side effects, not treatment of a metabolic disorder.

The other retrieved papers study tigecycline in leukaemia and lung cancer cells, where "tyrosine" refers to tyrosine kinase inhibitors such as imatinib and gefitinib. That is a different biology from inherited tyrosine metabolism disorders. The high TxGNN score is therefore not supported by disease-specific evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02883036](https://clinicaltrials.gov/study/NCT02883036) | N/A | Unknown | 100 | In vitro study of tigecycline's effect on mitochondrial biogenesis and metabolism in chronic myeloid leukaemia. It is not directed at tyrosine metabolism disorders. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41009505](https://pubmed.ncbi.nlm.nih.gov/41009505/) | 2025 | In vitro | Int J Mol Sci | Effects of tigecycline on homeostasis of human melanocytes and fibroblasts, relating to pigmentary and phototoxic side effects of tetracyclines. |
| [28920959](https://pubmed.ncbi.nlm.nih.gov/28920959/) | 2017 | Preclinical | Nature Medicine | Targeting mitochondrial oxidative phosphorylation (with tigecycline) helps eradicate therapy-resistant chronic myeloid leukaemia stem cells. |
| [29404396](https://pubmed.ncbi.nlm.nih.gov/29404396/) | 2018 | Commentary | Mol Cell Oncol | Commentary on the study above: tigecycline plus imatinib eradicated leukaemia stem cells and prevented relapse in animal models. |
| [31765940](https://pubmed.ncbi.nlm.nih.gov/31765940/) | 2020 | Preclinical | Neoplasia | SIRT1 targeting eliminates EGFR TKI-resistant cancer stem cells in lung adenocarcinoma via mitochondrial oxidative phosphorylation. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16104P | Tigeccord (Tigecycline for Injection USP 50 mg/vial) | Injection, powder, for solution | Not listed in the registration record |
| SIN13282P | Tygacil (Tigecycline) Injection 50 mg | Injection, powder, lyophilized, for solution | Not listed in the registration record |

## Safety Considerations

- **Fetal harm**: Tigecycline carries fetal-harm warnings, which is a concern in any use involving pregnancy or developmental conditions.
- **Pancreatitis**: Tigecycline is associated with pancreatitis.
- **Drug interactions**: A 2024 in vitro study found that tigecycline opposed the effect of bortezomib in myeloma cells by lowering mitochondrial reactive oxygen species. This is a preclinical signal only.

No drug interaction records were found in the database. Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the model score. The single trial and four papers do not address tyrosine metabolism disorders, and no plausible mechanism links an antibiotic to this condition.

**To proceed, the following is needed:**
- The HSA package insert, to complete the safety review (currently a blocking gap).
- Mechanism of action data from DrugBank.
- Disease-specific mechanistic or preclinical evidence for tyrosine metabolism disorders, which does not currently exist.
- A separate review of the lower-ranked prediction **monoclonal gammopathy**. It is the only candidate with relevant preclinical work (myeloma cell studies) and could be handled as a research question, taking the possible antagonism with bortezomib into account.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

