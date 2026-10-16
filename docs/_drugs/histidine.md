---
layout: default
title: Histidine
parent: Low Evidence (L5)
nav_order: 498
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Histidine: predicted new indication Gastroparesis (evidence level L5). Approved use: Not stated in the registration records"
---

# Histidine
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

# Histidine: From Parenteral Nutrition Amino Acid Component to Gastroparesis

## One-Sentence Summary

Histidine is an essential amino acid used as a component of parenteral nutrition and amino acid infusion products in Singapore, although the data compiled for this report do not list a specific approved indication text.
The TxGNN model predicts it may be effective for **gastroparesis**, but there are **0 clinical trials** and only **1 linked publication**, which does not test histidine.
The prediction currently rests almost entirely on the model score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records (all 17 licences list products without indication text; they are amino acid infusion and parenteral nutrition products) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 17 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, histidine is a component of amino acid and parenteral nutrition formulations, where it supplies an essential amino acid. A mechanism by which it might act on delayed gastric emptying is not established.

The only publication linked to this prediction studies gastric amyloid pathology and mucosal denervation in hereditary ATTR amyloidosis. It does not test histidine and does not show that histidine affects gastric motility. The high TxGNN score (99.55%) reflects a graph-based association, not a demonstrated pharmacological link.

Other predictions show the same pattern. The related predictions for intestinal pseudo-obstruction and familial visceral myopathy are also supported only by model scores. For dyspepsia, one physiological study (PMID 29031770) examined a mixture of three amino acids, including histidine, and its effect on gastric emptying, which is an indirect hint at most. For sclerosing cholangitis, the preclinical evidence points to the histidine-to-histamine pathway as a driver of disease, so the direction of effect appears unfavourable or at best unclear.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42668409](https://pubmed.ncbi.nlm.nih.gov/42668409/) | 2026 | Preclinical/clinical pathology | Amyloid | Describes gastric amyloid pathology and mucosal denervation in hereditary ATTR amyloidosis patients and mice. Histidine was not tested, and no link to gastric motility is shown. |

---

## Singapore Market Information

All 17 valid registrations are single-ingredient licences. Five of them are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11682P | AMINOVEN Solution for Infusion 5% | Injection | Not stated |
| SIN11829P | AMINOVEN Solution for Infusion 10% | Injection | Not stated |
| SIN16337P | AMINOVEN Solution for Infusion 15% | Infusion, solution | Not stated |
| SIN06299P | NEPHROSTERIL for Intravenous Infusion | Injection | Not stated |
| SIN08352P | AMINOPLASMAL-15% Infusion | Injection | Not stated |

---

## Safety Considerations

- **Disease associations from the knowledge graph (not label text)**: The TxGNN knowledge graph links histidine with contraindication edges for several conditions. They include kidney disease (chronic kidney disease, chronic renal failure, end-stage renal failure, nephrolithiasis, nephrocalcinosis, acute urate nephropathy), heart disease and cardiovascular disease (including digitalis poisoning and ventricular fibrillation), calcium and phosphorus disorders (hypercalcaemia, humoral hypercalcaemia of malignancy, sarcoidosis, phosphorus metabolism disease), and phenylalanine metabolism disorders (phenylketonuria). These come from graph data, not from the package insert, and need verification against the label.

Please refer to the package insert for warnings, contraindications and drug interaction information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score only. There are no clinical trials, the single linked paper does not involve histidine, and no mechanism connects histidine to gastric emptying. The evidence level is L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA, which is a blocking gap for safety screening
- Mechanism of action data for histidine (for example from DrugBank)
- Mechanistic or preclinical studies testing histidine directly in gastric motility models
- Review of the knowledge-graph contraindication signals (renal, cardiac, calcium disorders, phenylketonuria) against the label
- Route and formulation compatibility assessment, since current products are intravenous nutrition formulations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

