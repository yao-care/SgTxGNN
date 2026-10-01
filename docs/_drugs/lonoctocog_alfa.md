---
layout: default
title: Lonoctocog Alfa
parent: Low Evidence (L5)
nav_order: 605
evidence_level: L5
indication_count: 10
---

# Lonoctocog Alfa
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

# Lonoctocog alfa: From Hemophilia A to Pseudo-von Willebrand Disease

## One-Sentence Summary

Lonoctocog alfa (marketed as AFSTYLA) is a single-chain recombinant factor VIII (FVIII) used to treat hemophilia A.
The TxGNN model predicts it may be effective for **pseudo-von Willebrand disease** with a very high score, but **0 clinical trials** and **0 publications** support this direction, and the expert mechanistic review found no plausible therapeutic link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia A (from the drug's known use; the HSA licence text in the data provided is blank) |
| Predicted New Indication | Pseudo-von Willebrand disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, lonoctocog alfa is a single-chain recombinant FVIII. It replaces missing FVIII activity in hemophilia A, where FVIII acts as the cofactor of activated factor IX in the intrinsic tenase complex.

Pseudo-von Willebrand disease (platelet-type VWD) is a different problem. It is caused by a gain-of-function defect in the platelet receptor GPIbα, which increases platelet binding to von Willebrand factor (VWF). Replacing FVIII does not correct this platelet receptor defect. The only link is indirect, through the VWF-FVIII interaction.

The high TxGNN score most likely reflects the drug's proximity in the knowledge graph to other FVIII and VWF-related bleeding disorders, not a therapeutic mechanism. The same pattern appears in the other nine predictions, which are all bleeding or platelet-related conditions. Nine of the ten are judged to have no plausible mechanism for FVIII replacement, and two carry a possible safety concern:

- **Platelet function and count disorders** (primary release disorder of platelets, Glanzmann thrombasthenia, Scott syndrome, collagen receptor defect, constitutional thrombocytopenia): the defect lies in the platelets, not in FVIII.
- **Esophageal varices, with or without bleeding**: the cause is portal hypertension, and exogenous FVIII adds thrombotic risk without expected benefit.
- **Thrombotic thrombocytopenic purpura (TTP)**: a pro-hemostatic drug could worsen thrombosis. This prediction should not be pursued without a clear rationale.
- **Acquired coagulation factor deficiency** (rank 5, the only research question): this is the most biologically coherent prediction, since FVIII replacement directly addresses FVIII deficiency. The term is too broad, though. Acquired hemophilia A is usually managed with bypassing agents or immunosuppression because inhibitors can neutralize FVIII, and deficiencies of factors II, VII, IX or X would not respond to FVIII.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15820P | AFSTYLA Powder and Solvent for Solution for Injection 3000IU/vial | Lyophilized powder for injection solution | Not stated in the data provided |
| SIN15821P | AFSTYLA Powder and Solvent for Solution for Injection 250IU/vial | Lyophilized powder for injection solution | Not stated in the data provided |
| SIN15822P | AFSTYLA Powder and Solvent for Solution for Injection 500IU/vial | Lyophilized powder for injection solution | Not stated in the data provided |
| SIN15823P | AFSTYLA Powder and Solvent for Solution for Injection 1000IU/vial | Lyophilized powder for injection solution | Not stated in the data provided |
| SIN15824P | AFSTYLA Powder and Solvent for Solution for Injection 2000IU/vial | Lyophilized powder for injection solution | Not stated in the data provided |

All five registrations are held by CSL Behring GmbH and cover different vial strengths. The only available route is injection.

## Safety Considerations

Please refer to the package insert for safety information.

Note from the mechanistic review: FVIII replacement is pro-hemostatic, and elevated FVIII and VWF levels are associated with thrombotic risk. This matters most for TTP and for cirrhosis-related conditions such as esophageal varices.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5), with no clinical trials or literature. For pseudo-von Willebrand disease, the defect is in the platelet receptor GPIbα, which FVIII replacement does not address. The high score most likely reflects graph proximity, not a therapeutic mechanism.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications, which is a blocking gap for safety screening
- Mechanism of action data (for example from DrugBank)
- A narrower disease definition for "acquired coagulation factor deficiency" (for example acquired hemophilia A or acquired FVIII deficiency), followed by a targeted literature and trial search
- Explicit exclusion of TTP and esophageal varices from further assessment unless a clear rationale and thrombotic-risk analysis are provided
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

