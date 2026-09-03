---
layout: default
title: Sulfamethoxazole
parent: 僅模型預測 (L5)
nav_order: 930
evidence_level: L5
indication_count: 10
---

# Sulfamethoxazole
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

# Sulfamethoxazole: From Broad-Spectrum Antibacterial Use to Acute Contagious Conjunctivitis

## One-Sentence Summary

> Sulfamethoxazole is a sulfonamide antibacterial that inhibits bacterial dihydropteroate synthase (DHPS) to block folate synthesis; detailed registry data on its original approved indication is not on file for this Evidence Pack.
> The TxGNN model predicts it may be relevant to **Acute Contagious Conjunctivitis**,
> with **0 clinical trials** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (drug not marketed in Singapore; no approved indication text in registry data). Pharmacologically classified as a broad-spectrum sulfonamide antibacterial per repurposing rationale evidence. |
| Predicted New Indication | Acute Contagious Conjunctivitis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L3 |
| Singapore Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The formal DrugBank MOA field for this drug is currently a data gap (DG002). However, the repurposing rationale attached to the top prediction describes the underlying mechanism: Sulfamethoxazole inhibits bacterial dihydropteroate synthase (DHPS), blocking folate synthesis and producing broad-spectrum antibacterial activity — consistent with the well-established pharmacology of the sulfonamide class.

Bacterial conjunctivitis is a classic indication for sulfonamide antibiotics; topical sulfacetamide, a related sulfonamide, has historically been used to treat bacterial conjunctivitis. This lends mechanistic plausibility to TxGNN's prediction linking sulfamethoxazole to acute contagious (bacterial) conjunctivitis.

That said, the product on file is a systemic (oral) formulation, not an ophthalmic preparation, and route compatibility between systemic dosing and this ocular indication has not been confirmed (marked "pending" in the Evidence Pack). The single supporting reference is a susceptibility survey describing local antibiotic resistance patterns in children with bacterial conjunctivitis, not a treatment-efficacy study of sulfamethoxazole itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31788487](https://pubmed.ncbi.nlm.nih.gov/31788487/) | 2019 | Cross-sectional/Susceptibility | Medical hypothesis, discovery & innovation ophthalmology journal | Retrospective analysis of bacteriology and antimicrobial susceptibility patterns in childhood acute bacterial conjunctivitis (Western Greece); informs empiric antibiotic selection but does not directly test sulfamethoxazole efficacy |

---

## Singapore Market Information

Sulfamethoxazole is not currently marketed in Singapore (market status: 未上市). No product registrations or licenses are on file in this Evidence Pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is supported only by a single low-tier, indirect literature reference and no clinical trials (Evidence Level L3), and the drug currently has no market presence or registration in Singapore. Combined with a blocking data gap on safety warnings/contraindications (DG001), the evidence base is insufficient to move beyond the research-question stage.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (DG001 — blocking; required before any S1 safety review)
- Confirmed mechanism of action from DrugBank (DG002)
- Route compatibility assessment — confirm whether a topical/ophthalmic formulation exists or is feasible, versus the currently available systemic-only product
- Prospective clinical evidence specific to acute contagious conjunctivitis (zero trials currently registered)
- Assessment of registration pathway given current "not marketed" status in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

