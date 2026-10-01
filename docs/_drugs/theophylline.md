---
layout: default
title: Theophylline
parent: Low Evidence (L5)
nav_order: 970
evidence_level: L5
indication_count: 10
---

# Theophylline
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

# Theophylline: From Asthma and COPD (Bronchodilator Use) to Thrombotic Disease

## One-Sentence Summary

Theophylline is a long-established bronchodilator used for airway diseases such as asthma and COPD.
The TxGNN model predicts it may be effective for **thrombotic disease**, but this rests on the model score alone: there are **no registered clinical trials** and no publications showing theophylline treats thrombosis.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

The Singapore licence records provided carry no approved-indication text, so the original indication is not listed here. The bronchodilator use above comes from the retrieved literature.

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in this Evidence Pack. Theophylline is known to be a phosphodiesterase (PDE) inhibitor and an adenosine receptor antagonist. Its efficacy in airway disease is well established.

The two actions point in opposite directions for thrombosis. PDE inhibition can raise cAMP in platelets, which in theory reduces aggregation. Adenosine antagonism could blunt the antiplatelet effect of adenosine. No supporting data were provided, so the net direction is unclear. The very high TxGNN score (0.996) is a graph-based association and not evidence of clinical benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No RCTs were found. The retrieved papers are mostly platelet biology, assay methods, or unrelated conditions. None shows theophylline treating thrombosis. The most relevant items are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Crit Rev Biochem | Thromboxane A2 and prostacyclin act oppositely on platelets; prostacyclin stimulates adenylate cyclase to inhibit aggregation (the cAMP rationale) |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Not classified | Gen Pharmacol | Milrinone, a PDE inhibitor, reduces platelet aggregation and raises cAMP, and interacts with adenosine effects (a related drug, not theophylline) |
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clin Pharmacokinet | Pharmacokinetics of ticlopidine, an antiplatelet agent (not theophylline) |
| [6241135](https://pubmed.ncbi.nlm.nih.gov/6241135/) | 1984 | Not classified | Cor Vasa | T-lymphocyte subsets in patients with myocardial infarction and thrombophlebitis; theophylline was used only as a cell-subset marker |
| [26764324](https://pubmed.ncbi.nlm.nih.gov/26764324/) | 2016 | Not classified | J Nutr | Aged garlic extract inhibits platelet aggregation via cAMP and cGMP signalling (not theophylline) |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Not classified | Platelets | Soluble CLEC-2 as a platelet-activation marker for thrombotic risk (not theophylline) |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Not classified | Br J Haematol | Platelet factor 4 assay; theophylline appears only as a sample additive to prevent platelet activation |
| [14231672](https://pubmed.ncbi.nlm.nih.gov/14231672/) | 1964 | Not classified | Z Gesamte Inn Med | Chronic cor pulmonale after thromboembolic disease (no abstract available) |

## Singapore Market Information

Eight registrations are on record; the five main ones are shown. Approved-indication text is not recorded in the data.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN11399P | NUELIN-SR 125 TABLET | Tablet | Adcock Ingram Limited |
| SIN10679P | NUELIN-SR 250 TABLET | Tablet | Adcock Ingram Limited |
| SIN03139P | THEOPHYLLINE TABLETS 100 mg | Tablet | Beacons Pharmaceuticals Pte. Ltd. |
| SIN09668P | APO-THEO LA TABLET 200 mg | Tablet | Apotex Inc |
| SIN10158P | APO-THEO LA TABLET 100 mg | Tablet | Apotex Inc |

Forms across all registrations are oral tablets (including film-coated) and syrup.

## Safety Considerations

- **Narrow therapeutic index**: serum level monitoring is needed. CYP1A2-related and other drug interactions require review.
- **Drug Interactions**: the interaction query returned no records, which is likely a data gap and not evidence of no interactions.
- **Carcinogenicity**: an NTP carcinogenesis study in rodents is in the literature and should be reviewed.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score. No trials exist, and the retrieved literature contains no data on theophylline in thrombosis. The two main mechanisms may oppose each other for platelet function.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications, which block safety screening
- Mechanism-of-action data from DrugBank
- A targeted literature search on theophylline, platelet aggregation and thrombosis
- Consideration of better-supported candidates in the same pack, namely nasal cavity disease (L2, a completed Phase 2 trial of nasal theophylline irrigation for post-viral olfactory dysfunction, n=27) and obstructive lung disease (L1, but this is the existing approved use and not true repurposing)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

