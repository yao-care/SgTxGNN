---
layout: default
title: Baloxavir Marboxil
parent: Low Evidence (L5)
nav_order: 135
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Baloxavir Marboxil: predicted new indication Hemophagocytic syndrome associated with an infection (evidence level L5). Approved use: Influenza"
monitor_inn: "Baloxavir marboxil"
predicted_indications: ["hemophagocytic syndrome associated with an infection", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease", "cardioencephalomyopathy, fatal infantile, due to cytochrome c oxidase deficiency", "Singleton-Merten syndrome", "hemophagocytic syndrome", "chronic hepatitis C virus infection", "hepatitis C virus infection", "hepatitis E virus infection", "hepatitis A virus infection", "Omsk hemorrhagic fever"]
---

# Baloxavir Marboxil
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

## Baloxavir marboxil: From Influenza to Infection-Associated Hemophagocytic Syndrome
{: .text-alpha }

## One-Sentence Summary

Baloxavir marboxil is an oral antiviral originally used to treat influenza.
The TxGNN model predicts it may be effective for **hemophagocytic syndrome associated with an infection**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza (from the knowledge graph; the Singapore licence records contain no indication text) |
| Predicted New Indication | Hemophagocytic syndrome associated with an infection |
| TxGNN Prediction Score | 98.85% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, baloxavir is a cap-dependent endonuclease inhibitor that targets the polymerase acidic (PA) protein of the influenza virus. Its efficacy in influenza is established.

Influenza can trigger infection-associated hemophagocytic lymphohistiocytosis (HLH), so treating the viral trigger is conceptually plausible. However, baloxavir has no known direct effect on the hyperinflammatory cytokine cascade that drives HLH. At best it would be relevant only to influenza-triggered cases, and standard care focuses on immune suppression plus treating the trigger.

The score is a graph-based prediction. It does not reflect any supporting trial or published study, and should be treated as a hypothesis only.

Other top predictions (for context) have even weaker rationale:
- **Other hemophagocytic conditions** (malignancy-associated HLH, unspecified hemophagocytic syndrome): no plausible mechanistic link; the scores likely reflect shared graph neighbours with other HLH nodes.
- **Hepatitis A, C and E viruses, and Omsk hemorrhagic fever**: these viruses do not use cap-snatching, so the baloxavir target is absent. Effective treatments or vaccines already exist for several of them.
- **Cardioencephalomyopathy due to cytochrome c oxidase deficiency, and Singleton-Merten syndrome**: no connection between a viral endonuclease inhibitor and these mitochondrial or interferon-signalling disorders.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15679P | XOFLUZA Film Coated Tablets 20mg | Tablet, film coated | Not recorded in the licence data |
| SIN15680P | XOFLUZA Film Coated Tablets 40mg | Tablet, film coated | Not recorded in the licence data |

Both licences are valid single-ingredient products for oral use, with none cancelled.

## Safety Considerations

**Drug Interactions**: 26 interactions were identified, and every one of the 20 detailed entries is rated Moderate. They fall into a clear pattern of polyvalent cation and adsorbent products, which commonly reduce oral absorption of the drug when taken together:
- **Aluminium- and magnesium-containing products**: aluminium hydroxide, magaldrate, magnesium carbonate, chloride, citrate, gluconate, hydroxide, oxide and sulfate
- **Calcium-containing products**: calcium acetate, carbonate, citrate, glubionate, gluconate, lactate and phosphate
- **Others**: iron, kaolin, attapulgite, sucralfate

Dosing should be separated from these products. The remaining six interactions are not itemised in the data.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature and no direct mechanistic link to the hyperinflammation that defines HLH. Baloxavir could be relevant at most to influenza-triggered cases, which is an extension of its existing use rather than a new therapeutic effect.

**To proceed, the following is needed:**
- Detailed mechanism-of-action data from DrugBank
- Package insert warnings and contraindications from the HSA website, to allow safety screening
- Approved indication text for the Singapore licences
- Case-level or preclinical evidence on antiviral treatment in influenza-triggered HLH
- Complete listing of the remaining drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

