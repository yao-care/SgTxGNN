---
layout: default
title: Ipilimumab
parent: Low Evidence (L5)
nav_order: 545
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
description: "Ipilimumab: predicted new indication Choroideremia (evidence level L5). Approved use: Metastatic melanoma"
monitor_inn: "Ipilimumab"
predicted_indications: ["choroideremia"]
---

# Ipilimumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Ipilimumab: From Metastatic Melanoma to Choroideremia
{: .text-alpha }

## One-Sentence Summary

Ipilimumab was originally used to treat metastatic melanoma.
The TxGNN model predicts it may be effective for **choroideremia** (an inherited retinal degeneration), but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The high score appears to be a model artifact rather than a reflection of real evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic melanoma |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 0.9906 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for ipilimumab: "CTLA-4 is a negative regulator of T-cell activity. Ipilimumab is a monoclonal antibody that binds to CTLA-4 and blocks the interaction of CTLA-4 with its ligands, CD80/CD86. Blockade of CTLA-4 has been shown to augment T-cell activation and proliferation, including the activation and proliferation of tumor infiltrating T-effector cells." ([DailyMed: Yervoy (ipilimumab) prescribing information, E.R. Squibb & Sons, L.L.C.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2265ef30-253e-11df-8a39-0800200c9a66), label version 2026-08-20; accessed 2026-11-19.) Ipilimumab is known to block CTLA-4, which enhances T-cell priming and anti-tumour immunity. This mechanism underlies its efficacy in metastatic melanoma.

Choroideremia is a single-gene, X-linked retinal degeneration caused by loss of the CHM (REP1) gene. It is not driven by tumour growth or by a failure of immune surveillance. No plausible biological link between CTLA-4 blockade and this disease was identified.

The very high TxGNN score (0.9906) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No trials or literature back it up, so the prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN14598P | YERVOY INJECTION CONCENTRATE 5MG/ML | INJECTION, SOLUTION, CONCENTRATE | Valid |

<!-- licenses:end -->

This is a single-ingredient product with a valid registration, and it is an injectable formulation. The approved indication text was not available in the data compiled for this report.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CTLA-4 monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; immune-related adverse events (e.g. liver, thyroid, skin, bowel) are typically monitored for checkpoint inhibitors |
| Handling Protection | Please refer to the package insert and local institutional policy for handling of antineoplastic biologics |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records. The first 20 reviewed include:
  - **Major**: anticoagulants, including apixaban, betrixaban, bivalirudin, dalteparin, desirudin, edoxaban, argatroban and danaparoid.
  - **Moderate**: corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone), metronidazole, tinidazole, naltrexone, rosuvastatin and simvastatin.

Corticosteroids matter in practice because they are commonly used to manage immune-related adverse events, and this interaction should be considered when planning care.

For warnings and contraindications, please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no trials or publications, and no plausible mechanistic link between CTLA-4 blockade and a monogenic retinal degeneration such as choroideremia. Safety label data are also incomplete.

**To proceed, the following is needed:**
- Mechanistic evidence for any biological role of CTLA-4 or immune pathways in choroideremia
- Preclinical data in relevant retinal disease models
- Package insert warnings and contraindications for Singapore (HSA), and the approved indication text
- Detailed mechanism of action data (MOA)
- A safety assessment for ocular use, since immune-related adverse events could further harm an already degenerating retina

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available from the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Yervoy (ipilimumab) prescribing information, E.R. Squibb & Sons, L.L.C.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2265ef30-253e-11df-8a39-0800200c9a66) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

