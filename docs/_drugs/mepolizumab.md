---
layout: default
title: Mepolizumab
parent: Medium Evidence (L3-L4)
nav_order: 650
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Mepolizumab: predicted new indication Thrombocytopenia due to immune destruction (evidence level L4). Approved use: Eosinophilic pneumonia"
monitor_inn: "Mepolizumab"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets", "pseudo-von Willebrand disease", "autoimmune thrombocytopenic", "Glanzmann thrombasthenia", "Evans syndrome", "neonatal thrombocytopenia", "autosomal thrombocytopenia with normal platelets", "filariasis", "mixed-type autoimmune hemolytic anemia"]
---

# Mepolizumab
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Mepolizumab: From Eosinophilic Pneumonia to Thrombocytopenia Due to Immune Destruction

## One-Sentence Summary

Mepolizumab was originally used for eosinophil-driven lung conditions (eosinophilic pneumonia and pulmonary eosinophilia).
The TxGNN model predicts it may be effective for **thrombocytopenia due to immune destruction**,
but the supporting evidence is thin: **0 clinical trials** and **1 publication** (a single case report).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Eosinophilic pneumonia; pulmonary eosinophilia (from the knowledge graph; no approved-indication text in the Singapore licence records) |
| Predicted New Indication | Thrombocytopenia due to immune destruction |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Mepolizumab is known to be an anti-IL-5 antibody that depletes eosinophils, which is why it fits eosinophil-driven diseases such as eosinophilic pneumonia and pulmonary eosinophilia.

The link to immune thrombocytopenia is indirect. A single case report describes a patient with a steroid-resistant hypereosinophilic immune disorder and a mixed thrombotic microangiopathy who improved on mepolizumab. The benefit is plausibly due to controlling eosinophil-driven immune dysregulation, not to a direct effect on platelet autoimmunity (anti-platelet autoantibodies and Fc-gamma receptor-mediated platelet clearance). The high TxGNN score is a computational prediction and does not replace clinical evidence.

Most other top-ranked predictions (inherited platelet disorders such as Glanzmann thrombasthenia and pseudo-von Willebrand disease) have no plausible IL-5-related mechanism and likely reflect proximity in the knowledge graph. Filariasis has a loose eosinophil link, but depleting eosinophils could impair parasite defence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Case report | Blood Cells, Molecules & Diseases | Steroid-resistant hypereosinophilic immune disorder resolved with mepolizumab, with improvement in a mixed thrombotic microangiopathy |

A review of hypereosinophilic syndrome management including mepolizumab ([PMID 20565230](https://pubmed.ncbi.nlm.nih.gov/20565230/), 2010) was linked to the second-ranked prediction (primary release disorder of platelets), but it does not address platelet disorders directly.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16811P | NUCALA Solution for Injection in Pre-filled Syringe 40mg/0.4mL | Injection, solution | Not stated in the compiled data |
| SIN16172P | NUCALA Solution for Injection in Pre-filled Pen 100mg/mL | Injection, solution | Not stated in the compiled data |
| SIN16171P | NUCALA Solution for Injection in Pre-filled Syringe 100mg/mL | Injection, solution | Not stated in the compiled data |

All three licences are valid single-ingredient products from Glaxo Operations UK Ltd.

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the data compiled for this report, and no knowledge-graph contraindications were recorded.

Specific concerns for the predicted uses:
- **Filariasis:** eosinophil depletion could impair host defence against parasites.
- **Neonatal thrombocytopenia:** no safety or pharmacokinetic data exist for mepolizumab in neonates.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction rests on a single case report in a different condition (hypereosinophilic syndrome with thrombotic microangiopathy), with no trials and no established mechanism for IL-5 blockade in immune platelet destruction. The model score alone is not enough to proceed.

**To proceed, the following is needed:**
- Mechanism of action data and a clearer mechanistic hypothesis, for example whether an eosinophilic or Th2-skewed ITP subset exists
- Package insert warnings and contraindications from the HSA, so safety screening can be done
- Controlled or at least larger observational data in immune thrombocytopenia
- Approved indication text for the Singapore licences, to confirm the original-indication link
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

