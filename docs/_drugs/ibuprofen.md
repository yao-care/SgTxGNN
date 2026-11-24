---
layout: default
title: Ibuprofen
parent: Low Evidence (L5)
nav_order: 514
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-20
monitor_inn: "Ibuprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
description: "Ibuprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). In Singapore: 26 HSA registrations (26 valid)"
---

# Ibuprofen
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

## Ibuprofen: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Ibuprofen is a widely used non-steroidal anti-inflammatory drug (NSAID), originally used for rheumatoid arthritis, osteoarthritis, headache, juvenile idiopathic arthritis and patent ductus arteriosus.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder.
This prediction has **no clinical trials and no publications** behind it, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 26 of 26) |
| Number of Registrations | 26 (valid: 26) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for ibuprofen: "Ibuprofen has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of CALDOLOR, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Caldolor (ibuprofen) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1eaa7790-f1a1-4f51-b10a-cbbaf033f684), label version 2026-01-29; accessed 2026-11-19.) Ibuprofen is generally known as a non-selective COX inhibitor that reduces prostaglandin production, which explains its anti-inflammatory, analgesic and antipyretic effects in arthritis and headache.

Acromesomelic dysplasia, Hunter-Thompson type, is a genetic skeletal dysplasia linked to the CDMP1/GDF5 pathway. It is a developmental bone disorder, not an inflammatory one. No plausible link between COX inhibition and this pathology is evident. The high score (0.9974) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

At most, ibuprofen might relieve joint pain as symptomatic management. That is not a repurposing rationale, because it does not modify the disease.

The other top-ranked predictions show the same pattern. They include brachyolmia, pseudoachondroplasia and myosclerosis. All have scores between 0.9960 and 0.9971, all are Level L5, and none has trial or literature support or an established mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

The approved indication text is not recorded for any of them. The main authorizations are listed below.

<!-- review:begin sg-lic-20261106-ibuprofen-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Ibuprofen has 20 valid single-ingredient registrations in Singapore and none cancelled. The approved indication text is not recorded for any of them." Removed: the number or status of product registrations stated here did not match the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The Quick Overview and the table under Singapore Market Information show the current number of HSA registrations. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-ibuprofen-1 -->

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN05443P | BRUFEN Suspension 100 mg/5 ml | SYRUP | Valid |
| SIN05464P | IBUFEN TABLETS 200 mg | TABLET, FILM COATED | Valid |
| SIN05722P | BRUFEN TABLET 200 mg | TABLET, SUGAR COATED | Valid |
| SIN06016P | APO-IBUPROFEN-FC TABLET 200 mg | TABLET, FILM COATED | Valid |
| SIN06017P | APO-IBUPROFEN-FC TABLET 400 mg | TABLET, FILM COATED | Valid |

Showing 5 of 26 HSA registrations.

<!-- licenses:end -->

Other registered forms include suspensions and syrups (for example Nurofen for Children and Brufen) as well as further tablets.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for label-based safety information.

- **Conditions flagged in the knowledge graph (not label text):** The drug-disease contraindication links in the TxGNN knowledge graph cover many conditions. The main groups are:
  - Cardiovascular and cerebrovascular: hypertension, hypotension, myocardial infarction, stroke, cerebral infarction.
  - Gastrointestinal: peptic ulcer disease, inflammatory bowel disease.
  - Kidney and liver: kidney disease, liver disease, liver failure.
  - Bleeding and blood: blood coagulation disease, thrombocytopenia.
  - Others: epilepsy, COPD, systemic lupus erythematosus, diabetes mellitus, diabetic ketoacidosis, hypothyroidism, potassium deficiency, benign prostatic hyperplasia, substance abuse/dependence.
- **Drug interactions:** The interaction screen found 100 interacting drugs, and the first 20 returned are summarised here.
  - **Major:** acetylsalicylic acid (aspirin).
  - **Moderate:**
    - Corticosteroids: betamethasone, budesonide, dexamethasone, hydrocortisone.
    - Sulfonylurea antidiabetics: acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide.
    - Others: aprepitant, balsalazide, dexfenfluramine, fenfluramine, exenatide, kanamycin, levofloxacin.
  - **Minor:** famotidine, ranitidine, cimetidine.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. It has no clinical trials, no literature, no known mechanistic link between COX inhibition and the disease, and the evidence level is L5. Ibuprofen is well established and widely marketed in Singapore, but that does not support this new indication.

**To proceed, the following is needed:**
- Mechanism of action data for ibuprofen, and a biological rationale linking it to the GDF5/CDMP1 pathway or to skeletal development
- Preclinical studies, such as cell or animal models of the disease, to test any disease-modifying effect
- A literature and trial search to confirm that no relevant studies exist
- The Singapore package insert, to establish approved indications, warnings and contraindications
- A clear definition of the intended goal. If it is symptomatic pain relief, this should be treated as standard NSAID use, not as repurposing.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Sciences Authority data (the register of therapeutic products). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "Ibuprofen has 20 valid single-ingredient registrations in Singapore and none cancelled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Caldolor (ibuprofen) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1eaa7790-f1a1-4f51-b10a-cbbaf033f684) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

