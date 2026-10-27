---
layout: default
title: Lonoctocog Alfa
parent: Low Evidence (L5)
nav_order: 611
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lonoctocog Alfa: predicted new indication Pseudo-von Willebrand disease (evidence level L5). Approved use: Hemophilia"
monitor_inn: "Lonoctocog alfa"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "esophageal varices without bleeding", "esophageal varices with bleeding", "thrombotic thrombocytopenic purpura"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Lonoctocog alfa: From Hemophilia to Pseudo-von Willebrand Disease
{: .text-alpha }

## One-Sentence Summary

Lonoctocog alfa is a recombinant single-chain factor VIII, originally used to treat hemophilia (factor VIII deficiency).
The TxGNN model predicts it may be effective for **pseudo-von Willebrand disease**,
but **no clinical trials and no publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia; symptomatic form of hemophilia in female carriers (the Singapore licences do not list indication text) |
| Predicted New Indication | Pseudo-von Willebrand disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, lonoctocog alfa is a recombinant single-chain factor VIII (rVIII-SingleChain) that replaces the missing clotting factor in hemophilia. Its efficacy there is the basis for its use, and it may mechanistically touch other bleeding disorders only indirectly.

Pseudo-von Willebrand disease (platelet-type von Willebrand disease) is caused by a gain-of-function defect in platelet GPIbα, which leads to loss of high-molecular-weight VWF multimers. Factor VIII is not the primary deficit, although secondary reductions can occur. The link is therefore weak and indirect. The very high TxGNN score (99.85%) is most likely driven by the disease's proximity to other bleeding disorders in the knowledge graph, not by a demonstrated mechanism.

Other top-ranked predictions show the same pattern. Most are platelet function disorders (primary release disorder of platelets, Glanzmann thrombasthenia, Scott syndrome, collagen receptor defect, constitutional thrombocytopenia). In these the defect lies in the platelet, and factor VIII replacement does not address it. Acquired coagulation factor deficiency is the closest to the original indication, but inhibitors in acquired hemophilia neutralise infused factor VIII, so bypassing agents are the standard.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

All five licences are valid single-ingredient products from CSL Behring GmbH (brand AFSTYLA), supplied as lyophilised powder and solvent for injection. No approved indication text is recorded for them in the data compiled for this report.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15821P | AFSTYLA Powder and Solvent for Solution for Injection 250IU/vial | Injection, powder, lyophilised, for solution | Not stated |
| SIN15822P | AFSTYLA Powder and Solvent for Solution for Injection 500IU/vial | Injection, powder, lyophilised, for solution | Not stated |
| SIN15823P | AFSTYLA Powder and Solvent for Solution for Injection 1000IU/vial | Injection, powder, lyophilised, for solution | Not stated |
| SIN15824P | AFSTYLA Powder and Solvent for Solution for Injection 2000IU/vial | Injection, powder, lyophilised, for solution | Not stated |
| SIN15820P | AFSTYLA Powder and Solvent for Solution for Injection 3000IU/vial | Injection, powder, lyophilised, for solution | Not stated |

## Safety Considerations

Please refer to the package insert for safety information.

One theoretical concern comes from the mechanistic review. In thrombotic thrombocytopenic purpura, and in liver disease with varices, factor VIII is prothrombotic and could plausibly worsen thrombosis. This is a reason for caution in those conditions, not an established finding. No drug-interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone. No clinical trials or publications were found, and the mechanistic review judges the link to pseudo-von Willebrand disease weak and indirect. The package insert safety data are also missing, so the safety screening stage cannot be completed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website
- Mechanism of action data (for example, from DrugBank)
- Any clinical or preclinical evidence of factor VIII replacement benefit in platelet-type VWD
- Review of acquired factor VIII deficiency as a possible alternative candidate, taking inhibitor status into account
- Route compatibility and similarity-to-original-indication assessments, which are still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

