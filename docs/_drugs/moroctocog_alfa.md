---
layout: default
title: Moroctocog Alfa
parent: Low Evidence (L5)
nav_order: 688
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Moroctocog Alfa: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Hemophilia"
---

# Moroctocog Alfa
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

# Moroctocog alfa: From Hemophilia to Primary Release Disorder of Platelets

## One-Sentence Summary

Moroctocog alfa is a recombinant B-domain-deleted factor VIII, originally used to treat hemophilia (including the symptomatic form in female carriers).
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **no clinical trials and no publications** currently support this direction.
The prediction is best read as a graph-based signal rather than a mechanistically grounded finding.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia; symptomatic form of hemophilia in female carriers |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, moroctocog alfa is a recombinant factor VIII (B-domain-deleted) that replaces deficient FVIII in the intrinsic coagulation pathway. Its efficacy in hemophilia comes from correcting that FVIII deficit.

For the top prediction, the mechanistic fit is weak. Primary platelet release disorders are platelet function defects (impaired granule secretion) with normal FVIII activity, so FVIII replacement does not address the underlying problem. The very high TxGNN score (0.9997) most likely reflects the drug's proximity to other bleeding disorders in the knowledge graph rather than a true therapeutic link.

The same pattern holds for the other predicted indications:

- **Platelet-intrinsic or platelet-number disorders** (pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, collagen receptor defects, constitutional thrombocytopenia): FVIII is normal or not the limiting factor, and standard care relies on other measures such as platelet transfusion, antifibrinolytics, recombinant FVIIa, or thrombopoietin receptor agonists.
- **Acquired coagulation factor deficiency** (rank 4, score 99.88%): the most mechanistically plausible, since FVIII replacement could in principle correct an acquired FVIII deficit. However, the category is heterogeneous (liver disease, vitamin K deficiency, DIC, acquired hemophilia A with inhibitors), and single-factor replacement would often be ineffective or insufficient. It would need to be narrowed to a specific subtype.
- **Thrombotic-tendency or unclear conditions** (hereditary thrombocytosis with transverse limb defect, familial thrombomodulin anomalies, "flood factor deficiency"): a procoagulant could raise safety concerns, or the disease concept itself needs verification.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13791P | Xyntha Powder and Solvent for Solution for Injection 250iu | Injection, powder, for solution | Not stated in the available data |
| SIN13792P | Xyntha Powder and Solvent for Solution for Injection 500iu | Injection, powder, for solution | Not stated in the available data |
| SIN13794P | Xyntha Powder and Solvent for Solution for Injection 1000iu | Injection, powder, for solution | Not stated in the available data |
| SIN13793P | Xyntha Powder and Solvent for Solution for Injection 2000iu | Injection, powder, for solution | Not stated in the available data |

All four registrations are valid single-ingredient products (Wyeth Farma S.A, with pre-filled syringe diluent supplied by Vetter Pharma-Fertigung GmbH & Co. KG).

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications rest on model prediction alone (L5), with no registered trials or publications. The top prediction, primary release disorder of platelets, involves a platelet defect with normal FVIII, so FVIII replacement has no clear mechanistic basis. High TxGNN scores appear to reflect shared bleeding phenotypes in the knowledge graph.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Singapore-registered products, since safety screening cannot proceed without them
- Approved indication text for the Singapore registrations
- Mechanism of action data to support mechanistic-link analysis
- For acquired coagulation factor deficiency, narrowing to a specific subtype (e.g., a documented acquired FVIII deficit without inhibitors), followed by a targeted literature and trial search
- Verification of the disease concept "flood factor deficiency"
- Route compatibility and similarity-to-original-indication assessments, which are still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

