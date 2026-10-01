---
layout: default
title: Vasopressin
parent: Low Evidence (L5)
nav_order: 1047
evidence_level: L5
indication_count: 10
---

# Vasopressin
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

# Vasopressin: From an Unspecified Original Indication to Congenital Prothrombin Deficiency

## One-Sentence Summary

Vasopressin is a marketed injectable hormone product in Singapore, but the registration record does not state its approved indication.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but there are **0 clinical trials** and only **3 indirect publications** (1 review, 2 case reports), none of which studies vasopressin for this condition.
The score is high, but the clinical support is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration record |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L4 (indirect mechanistic literature only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for vasopressin is not available in this evidence pack. The original indication is also not recorded, so the usual "original-to-new indication" comparison cannot be made.

The only mechanistic link comes from the retrieved literature, which concerns **desmopressin (DDAVP)**, not vasopressin. DDAVP is a V2-selective vasopressin analog. In factor VIII/V deficiency and acquired hemophilia A, V2 agonism releases von Willebrand factor and factor VIII.

This mechanism does not carry over to prothrombin (factor II) deficiency, and the reports do not test vasopressin itself. The very high TxGNN score (0.996) is therefore not supported by clinical evidence, and it should be read as a model output only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | Acquired hemophilia A (autoantibodies against factor VIII): diagnosis, causes, clinical spectrum and treatment options. Not specific to prothrombin deficiency or vasopressin. |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case report | Rinsho Ketsueki (Japanese Journal of Clinical Hematology) | DDAVP given to a 43-year-old man with congenital combined factor V and factor VIII deficiency. Involves desmopressin, not vasopressin. |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case report | Rinsho Ketsueki (Japanese Journal of Clinical Hematology) | Cesarean section managed with factor VIII concentrate replacement in a pregnant woman with combined factor V and factor VIII deficiency. Not about vasopressin or prothrombin. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08350P | VASOPRESSIN INJECTION USP 20 u/ml (Fresenius Kabi USA, LLC) | Injection | Not stated in record |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings or contraindications were available in the evidence pack, and the drug-interaction query returned no results.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials behind it. The few publications concern desmopressin in other clotting-factor deficiencies, and their mechanism does not apply to prothrombin deficiency. Safety data and the approved indication are also missing, so the candidate cannot move to safety screening.

The other predicted indications in the pack are also on Hold. Most are prediction-only. For cystic neoplasm, the retrieved trials study tolvaptan, a V2 antagonist, in a non-neoplastic kidney cyst disease (ADPKD). That signal points to potential harm rather than benefit.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications, approved indication), which is currently a blocking gap
- Mechanism of action data for vasopressin, for example from the DrugBank API
- Direct evidence for vasopressin (not desmopressin) in prothrombin deficiency, or a documented rationale for why it would work
- Route and formulation compatibility assessment for the proposed use

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

