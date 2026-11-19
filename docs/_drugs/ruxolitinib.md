---
layout: default
title: Ruxolitinib
parent: Low Evidence (L5)
nav_order: 889
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
monitor_inn: "Ruxolitinib"
predicted_indications: ["uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lymphangiomyoma", "lymphangioleiomyomatosis", "liposarcoma", "familial rhabdoid tumor", "lung PEComa", "ovarian myxoid liposarcoma", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease", "hemophagocytic syndrome associated with an infection"]
description: "Ruxolitinib: predicted new indication Uterine corpus perivascular epithelioid cell tumor (evidence level L5). In Singapore: 4 HSA registrations (4 valid)"
---

# Ruxolitinib
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

## Ruxolitinib: Uterine corpus perivascular epithelioid cell tumor
{: .text-alpha }

## One-Sentence Summary

Ruxolitinib is an oral JAK inhibitor, originally used for myeloproliferative neoplasms such as myelofibrosis and polycythemia vera.
The TxGNN model predicts it may be effective for **uterine corpus perivascular epithelioid cell tumor**, but this is a prediction only, with **0 clinical trials** and **0 publications** supporting it.
Other predicted indications have more support, notably hemophagocytic lymphohistiocytosis (HLH), and are summarised under "Conclusion and Next Steps".

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Uterine corpus perivascular epithelioid cell tumor |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 4 of 4) |
| Number of Registrations | 4 (valid: 4) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for ruxolitinib: "Ruxolitinib, a kinase inhibitor, inhibits Janus Associated Kinases (JAKs), JAK1 and JAK2, which mediate the signaling of a number of cytokines and growth factors that are important for hematopoiesis and immune function. JAK signaling involves recruitment of STATs (signal transducers and activators of transcription) to cytokine receptors, activation, and subsequent localization of STATs to the nucleus leading to modulation of gene expression." ([DailyMed: Jakafi (ruxolitinib) prescribing information, Incyte Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f1c82580-87ae-11e0-bc84-0002a5d5c51b), label version 2026-07-20; accessed 2026-11-19.) Based on known information, ruxolitinib is a JAK1/2 inhibitor. Its efficacy in myeloproliferative neoplasms is established, and these diseases are driven by overactive JAK-STAT signalling.

The link to the predicted indication is weak. PEComas are typically driven by activation of the mTOR pathway (loss of TSC1 or TSC2), and the data compiled for this report do not establish any connection between this pathway and JAK1/2 inhibition. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The same pattern holds for the other PEComa-family predictions (benign PEComa, lung PEComa, lymphangiomyoma, lymphangioleiomyomatosis). All are prediction-only with no trials or publications. Lymphangioleiomyomatosis is mTOR-driven and already has an established therapy, sirolimus.

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
| SIN14396P | JAKAVI TABLET 5MG | TABLET | Valid |
| SIN14397P | JAKAVI TABLET 15MG | TABLET | Valid |
| SIN14398P | JAKAVI TABLET 20MG | TABLET | Valid |
| SIN14927P | JAKAVI TABLET 10MG | TABLET | Valid |

<!-- licenses:end -->

All four registrations are valid single-ingredient oral products from Novartis Pharma Stein AG. No indication text is recorded for them in the registry data.

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the DDInter database. The 20 reviewed include the following.
  - **Major**: clarithromycin, cobicistat, deferasirox, deferiprone, ibritumomab tiuxetan, tositumomab, tositumomab (I-131), samarium (153Sm) lexidronam
  - **Moderate**: dexamethasone, rosuvastatin, fenfluramine, dexfenfluramine, sibutramine, troglitazone, palifermin, strontium chloride Sr-89
  - **Minor**: aprepitant, cimetidine, miconazole, clotrimazole

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5). There are no trials or publications, and the known biology of PEComa (mTOR-driven) does not point to a role for JAK inhibition.

**Other predicted indications with more support:**
- **Hemophagocytic lymphohistiocytosis (HLH), including infection-associated forms (L3):** This has the strongest evidence of the predictions reviewed. It includes a prospective pediatric response-stratified study, case series, compassionate-use reports and murine mechanistic work. Most evidence is retrospective or case-based, and no registered trials were identified, so a prospective controlled trial is still needed.
- **Liposarcoma (L4):** Two preclinical papers describe JAK-STAT signalling in myxoid liposarcoma. There is no clinical evidence with ruxolitinib.
- **HLH associated with malignancy (L4):** The two supporting papers are indirect, so this would have to be extrapolated from the broader secondary HLH literature.

**To proceed, the following is needed:**
- A mechanistic rationale linking JAK/STAT inhibition to PEComa biology, plus any preclinical or clinical data in PEComa
- The mechanism of action and the package insert warnings and contraindications, which are missing from the compiled data and are needed for safety screening
- Singapore-approved indication text for the four registrations
- For HLH, a prospective controlled trial design and a route and dosing assessment

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Jakafi (ruxolitinib) prescribing information, Incyte Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f1c82580-87ae-11e0-bc84-0002a5d5c51b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

