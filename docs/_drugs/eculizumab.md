---
layout: default
title: Eculizumab
parent: Low Evidence (L5)
nav_order: 365
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Eculizumab: predicted new indication Cyclic hematopoiesis (evidence level L5). Approved use: Paroxysmal nocturnal hemoglobinuria"
monitor_inn: "Eculizumab"
predicted_indications: ["cyclic hematopoiesis", "autosomal recessive severe congenital neutropenia due to JAGN1 deficiency", "X-linked severe congenital neutropenia", "congenital neutropenia-myelofibrosis-nephromegaly syndrome", "adult idiopathic neutropenia", "autosomal recessive severe congenital neutropenia due to CXCR2 deficiency", "primary immunodeficiency syndrome due to p14 deficiency", "autosomal recessive severe congenital neutropenia due to CSF3R deficiency", "severe congenital neutropenia", "primary release disorder of platelets"]
---

# Eculizumab
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

## Eculizumab: From Paroxysmal Nocturnal Hemoglobinuria to Cyclic Hematopoiesis
{: .text-alpha }

## One-Sentence Summary

Eculizumab is a complement C5 inhibitor, originally used to treat paroxysmal nocturnal hemoglobinuria and neuromyelitis optica.
The TxGNN model predicts it may be effective for **cyclic hematopoiesis** (cyclic neutropenia), but **no clinical trials and no directly relevant publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Paroxysmal nocturnal hemoglobinuria; neuromyelitis optica (the Singapore license text has no approved indication wording) |
| Predicted New Indication | Cyclic hematopoiesis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for eculizumab: "Eculizumab, the active ingredient in SOLIRIS, is a monoclonal antibody that specifically binds to the complement protein C5 with high affinity, thereby inhibiting its cleavage to C5a and C5b and preventing the generation of the terminal complement complex C5b-9. SOLIRIS inhibits terminal complement-mediated intravascular hemolysis in PNH patients and complement-mediated thrombotic microangiopathy (TMA) in patients with aHUS." ([DailyMed: Soliris (eculizumab) prescribing information, Alexion Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ebcd67fa-b4d1-4a22-b33d-ee8bf6b9c722), label version 2026-07-08; accessed 2026-11-19.) Based on known information, eculizumab is a monoclonal antibody that inhibits complement protein C5 and blocks terminal complement activation. Its efficacy in complement-driven diseases such as paroxysmal nocturnal hemoglobinuria is established.

The link to cyclic hematopoiesis is weak. Cyclic neutropenia is typically driven by ELANE mutations that disrupt the regulation of neutrophil precursors, not by uncontrolled complement activity. The high score of 0.9997 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No mechanistic or clinical evidence supports it.

The other top-ranked predictions (various congenital neutropenias, adult idiopathic neutropenia, primary immunodeficiency due to p14 deficiency, and primary release disorder of platelets) share this problem. All have TxGNN scores between 0.9994 and 0.9996 and no supporting trials. Their mechanisms (neutrophil maturation, chemokine or G-CSF signaling, endosomal function, platelet secretion) are unrelated to terminal complement inhibition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature directly addresses eculizumab in cyclic hematopoiesis. Literature was retrieved only for lower-ranked predictions, and it does not support them:

- **Congenital neutropenia-myelofibrosis-nephromegaly syndrome (rank 4):** 20 publications were retrieved, mostly reviews on complement-mediated diseases (PNH, thrombotic microangiopathy, atypical hemolytic uremic syndrome, myasthenia gravis, CD59 deficiency). They appear to have been matched by drug or complement keywords, not disease relevance, and none address this syndrome.
- **Primary release disorder of platelets (rank 10):** The only publication is a PNH case-based roundtable review (PMID 23271156, 2012), which does not address platelet release disorders.

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN14226P | Soliris Concentrate for Solution for Infusion 300mg/vial | INFUSION, SOLUTION CONCENTRATE | Valid |

<!-- licenses:end -->

## Cytotoxicity

Not applicable. Eculizumab is not an antineoplastic drug.

## Safety Considerations

- **Drug Interactions:** 4 interactions were identified, all graded **Minor**. All involve human immunoglobulin G preparations (intravenous, subcutaneous, intramuscular, and intravenous plus subcutaneous).

Please refer to the package insert for warnings and contraindications. These were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials, no relevant literature, and no plausible link between complement C5 inhibition and the biology of cyclic neutropenia. The retrieved publications concern other complement-mediated diseases and do not support this indication.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- A disease-specific literature search and trial search for eculizumab in cyclic neutropenia
- Preclinical or mechanistic evidence that complement activity contributes to cyclic hematopoiesis
- Route and formulation compatibility assessment for the new indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Soliris (eculizumab) prescribing information, Alexion Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ebcd67fa-b4d1-4a22-b33d-ee8bf6b9c722) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

