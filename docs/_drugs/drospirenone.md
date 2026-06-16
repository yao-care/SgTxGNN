---
layout: default
title: Drospirenone
parent: 僅模型預測 (L5)
nav_order: 352
evidence_level: L5
indication_count: 10
---

# Drospirenone
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

# Drospirenone: From Hormonal Contraception/PMDD to Zinc, Elevated Plasma

## One-Sentence Summary

Drospirenone is a synthetic progestin with antimineralocorticoid and antiandrogenic properties, used internationally in combined oral contraceptives and approved for treating Premenstrual Dysphoric Disorder (PMDD); it is not currently registered in Singapore.
The TxGNN model ranks **Zinc, Elevated Plasma** as the top predicted new indication (score: 98.74%), but this is a laboratory value rather than a disease entity, and the prediction carries **no supporting clinical trials or literature** for this specific target.
All 10 predicted indications in this pack are rated **L5 (model prediction only)**, and the overall recommendation is **Hold** pending mechanistic and regulatory clarification.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; internationally used for oral contraception and PMDD (drospirenone + ethinyl estradiol combinations) |
| Predicted New Indication | Zinc, Elevated Plasma |
| TxGNN Prediction Score | 98.74% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on published literature retrieved during evidence collection, drospirenone is a fourth-generation synthetic progestin closely related to spironolactone. Its key pharmacological features are its **antimineralocorticoid activity** (antagonism of aldosterone receptors, leading to sodium and water excretion) and **antiandrogenic activity** (blocking androgen receptors), distinguishing it from older progestins.

The mechanistic link between drospirenone and elevated plasma zinc is highly speculative. Aldosterone is known to influence renal electrolyte handling broadly, and zinc homeostasis involves renal tubular reabsorption; in theory, antimineralocorticoid agents could indirectly affect trace-mineral excretion profiles. However, **no direct pharmacological evidence** supports drospirenone as a modulator of zinc metabolism, and "zinc, elevated plasma" is a laboratory finding rather than a clinical disease entity, making it an inappropriate target for drug repurposing development.

Among the 10 predicted indications, the one with the most plausible mechanistic rationale is **Mayer-Rokitansky-Küster-Hauser syndrome (MRKHS, rank 10)**: MRKHS patients (46,XX, absent uterus with normal ovarian function) often require hormone replacement therapy, and drospirenone combined with estradiol is used in HRT formulations internationally. This connection is not reflected in the current evidence pack but could support an upgraded evidence level upon external literature review.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top predicted indication (Zinc, Elevated Plasma).

---

## Literature Evidence

Currently no related literature available for the top predicted indication (Zinc, Elevated Plasma).

---

## Singapore Market Information

Drospirenone has **no registered products** in Singapore. No authorization numbers, product names, or approved indications are on record.

> **Note for investigators:** Drospirenone-containing products (e.g., Yasmin®, Yaz®, Angeliq®) are marketed in multiple jurisdictions (EU, US, Japan, Taiwan) for contraception, PMDD, and menopausal hormone therapy. Singapore registration would need to be pursued de novo.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data gap notice:** Key warnings, contraindications, and drug-drug interaction data were not retrieved during this evidence collection cycle. Before any clinical or formulary evaluation, the following should be obtained:
> - Full prescribing information / Summary of Product Characteristics (SmPC) from an approved jurisdiction (e.g., EU or US FDA label)
> - Drug interaction profile, particularly with potassium-sparing agents, ACE inhibitors, and ARBs (relevant given drospirenone's aldosterone-antagonist activity and known hyperkalemia risk)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for drospirenone are rated L5 (model prediction only, no supporting studies), and the top-ranked target — "zinc, elevated plasma" — is a laboratory value rather than a treatable disease entity, making it unsuitable as a repurposing candidate without substantial mechanistic reconceptualisation.

**To proceed, the following is needed:**

- **Re-evaluate the prediction target:** "Zinc, elevated plasma" should be deprioritised as a repurposing goal; consider redirecting analysis toward more clinically actionable predictions within this pack (e.g., MRKHS, rank 10, which has an established rationale for drospirenone-based HRT)
- **Retrieve full MOA data:** Query DrugBank API (DB01395) for pharmacodynamics, targets, and pathways to enable proper mechanistic-link scoring
- **Retrieve safety data:** Download and parse the prescribing information from an approved jurisdiction (US FDA label or EMA SmPC) to fill the Blocking data gap (DG001) and complete the safety profile
- **Pursue Singapore registration data:** Confirm whether any drospirenone-containing combination products have been submitted or are pending registration with HSA Singapore
- **Upgrade evidence for MRKHS:** Conduct a targeted PubMed search for "drospirenone" AND "MRKHS" or "Mayer-Rokitansky" to assess whether external literature supports an L3 upgrade for rank-10 indication before the next evaluation cycle
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

