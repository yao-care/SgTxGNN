---
layout: default
title: Fluorouracil
parent: 僅模型預測 (L5)
nav_order: 438
evidence_level: L5
indication_count: 10
---

# Fluorouracil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Fluorouracil: From Antineoplastic Chemotherapy to Botryoid-Type Embryonal Rhabdomyosarcoma of the Vagina

## One-Sentence Summary

Fluorouracil (5-FU) is a classic fluoropyrimidine antimetabolite widely used as a backbone of cancer chemotherapy regimens for colorectal, gastric, and other solid tumours worldwide.
The TxGNN model predicts it may be effective for **Botryoid-Type Embryonal Rhabdomyosarcoma of the Vagina**,
however there are currently **0 clinical trials** and **0 publications** directly supporting this extremely rare indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Singapore registration data available |
| Predicted New Indication | Botryoid-type embryonal rhabdomyosarcoma of the vagina |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Fluorouracil (5-FU) is a fluoropyrimidine antimetabolite that inhibits thymidylate synthase (TS), thereby blocking DNA synthesis and disrupting the cell cycle of rapidly proliferating tumour cells. Its broad-spectrum cytotoxic activity theoretically extends to any rapidly dividing malignancy.

Botryoid-type embryonal rhabdomyosarcoma of the vagina is an exceptionally rare paediatric soft tissue sarcoma arising from embryonal rhabdomyoblasts in the vaginal wall. Because rhabdomyosarcoma cells are rapidly dividing, the TS-inhibition mechanism of 5-FU theoretically could confer antiproliferative effects. The TxGNN high prediction score likely arises from an indirect knowledge graph path linking "rhabdomyosarcoma → chemotherapy → 5-FU" rather than any disease-specific evidence.

It is critical to note that the established standard-of-care chemotherapy for rhabdomyosarcoma is the VAC regimen (vincristine + actinomycin-D + cyclophosphamide), not 5-FU. No clinical trials or publications exist for this specific anatomic subtype and this drug combination. The high TxGNN score reflects a computational inference, not clinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Fluorouracil is not registered with the Health Sciences Authority (HSA) of Singapore. No product authorisations are on record for this drug.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Fluoropyrimidine antimetabolite class) |
| Myelosuppression Risk | Moderate — neutropenia and thrombocytopenia reported, particularly with continuous infusion or high-dose bolus schedules; less pronounced than platinum or alkylating agents |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (before each cycle), liver function tests, renal function, electrolytes; cardiac monitoring for patients with pre-existing cardiac disease (5-FU-associated vasospasm/cardiotoxicity) |
| Handling Protection | Must be handled according to cytotoxic drug handling regulations — closed-system drug transfer devices (CSTDs) recommended; avoid skin contact and inhalation |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is zero direct clinical or preclinical evidence linking Fluorouracil to botryoid-type embryonal rhabdomyosarcoma of the vagina; the TxGNN prediction (L5) reflects a purely computational inference from knowledge graph topology, and the established standard of care for this disease is the VAC regimen, not fluoropyrimidines.

**To proceed, the following is needed:**
- Preclinical in vitro data demonstrating 5-FU cytotoxicity against rhabdomyosarcoma cell lines (e.g., RD, Rh30) to establish any mechanistic basis
- Review of existing VAC-refractory rhabdomyosarcoma literature to determine whether any salvage regimens incorporating 5-FU have been explored
- Mechanism of action data from DrugBank API (DG002) to support or refute TS-inhibition rationale in the rhabdomyosarcoma context
- Singapore HSA package insert or international prescribing information (DG001) to complete the safety profile
- Evaluation of higher-ranked indications with actual evidence (e.g., **Liver Sarcoma** at rank 7, which has 5 clinical trials and 20 publications) as a more actionable repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

