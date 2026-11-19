---
layout: default
title: Cladribine
parent: Low Evidence (L5)
nav_order: 258
evidence_level: L5
indication_count: 7
monitor_inn: "Cladribine"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "liver sarcoma"]
last_modified_at: 2026-11-20
description: "Cladribine: predicted new indication parameningeal embryonal rhabdomyosarcoma (evidence level L5). In Singapore: 1 HSA registration (1 valid)"
---

# Cladribine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Cladribine: purine nucleoside analogue → parameningeal embryonal rhabdomyosarcoma
{: .text-alpha }

## One-Sentence Summary

Cladribine is a purine nucleoside analogue that is marketed in Singapore as an oral tablet.
The TxGNN model predicts it may be effective for **parameningeal embryonal rhabdomyosarcoma**, but **no clinical trials and no publications** directly support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | parameningeal embryonal rhabdomyosarcoma |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for cladribine: "The mechanism by which cladribine exerts its therapeutic effects in patients with multiple sclerosis has not been fully elucidated but is thought to involve cytotoxic effects on B and T lymphocytes through impairment of DNA synthesis, resulting in depletion of lymphocytes." ([DailyMed: Mavenclad (cladribine) prescribing information, EMD Serono, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9c75e30a-a410-40f1-b653-04d532bd9144), label version 2026-05-27; accessed 2026-11-19.) Cladribine is generally described as a purine nucleoside analogue that resists breakdown by adenosine deaminase. It causes DNA strand breaks and apoptosis, mainly in lymphocytes and monocytes that have high deoxycytidine kinase activity.

Parameningeal embryonal rhabdomyosarcoma is a solid mesenchymal tumour. No specific mechanistic rationale or supporting data link cladribine's activity in lymphoid cells to this tumour type. The high score (0.9977) most likely reflects the way related rhabdomyosarcoma subtypes cluster together in the model, not drug-specific evidence. The same pattern applies to the other rhabdomyosarcoma-family predictions, which also have no trials or literature behind them.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the main prediction.

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN15691P | MAVENCLAD TABLET 10MG | TABLET | Valid |

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analogue) |
| Myelosuppression Risk | High. Lymphopenia, neutropenia and other cytopenias are expected with this drug class |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (especially lymphocyte count), liver and renal function |
| Handling Protection | Follow local cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for product-specific requirements.

## Safety Considerations

- **Drug Interactions**: Interaction screening returned 100 records. Those listed include many **Major**-level interactions:
  - Corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone
  - Other drugs: deferiprone
  - Radiopharmaceuticals and radioimmunotherapies: ibritumomab tiuxetan, iobenguane (I-131), tositumomab (I-131), tositumomab, samarium (153Sm) lexidronam, strontium chloride Sr-89
  - Moderate-level interactions include palifermin, dipyridamole, cilostazol and eltrombopag.
- **Conditions of concern**: Kidney disease, thrombocytopenia, neutropenia, agranulocytosis, anaemia (including macrocytic anaemia), peripheral neuropathy and peripheral nervous system disease are flagged as conditions of concern. These come from drug–disease relationship data, not from label text.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. No trials or publications address parameningeal embryonal rhabdomyosarcoma, and no mechanistic rationale is available for extending cladribine from lymphoid cells to a solid paediatric sarcoma. Cladribine's marked myelosuppression and immunosuppression add to the case for caution.

**To proceed, the following is needed:**
- Preclinical data (for example, cell line or xenograft activity in embryonal rhabdomyosarcoma)
- Detailed mechanism of action data and a rationale specific to this tumour type
- Package insert warnings and contraindications from the Singapore regulator
- A safety and monitoring plan covering myelosuppression, infection risk and the listed interactions

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Mavenclad (cladribine) prescribing information, EMD Serono, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9c75e30a-a410-40f1-b653-04d532bd9144) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

