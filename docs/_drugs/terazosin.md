---
layout: default
title: Terazosin
parent: Low Evidence (L5)
nav_order: 955
evidence_level: L5
indication_count: 10
---

# Terazosin
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

# Terazosin: From Alpha-1 Blocker Uses (BPH and Hypertension) to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Terazosin is an oral alpha-1 adrenergic blocker. The Singapore registration data does not list an approved indication, but the drug class is generally used for benign prostatic hyperplasia and hypertension.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, a genetic hair-loss condition.
**No clinical trials and no publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Singapore registration records |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence package. Based on known information, terazosin is an alpha-1 adrenergic antagonist that relaxes vascular and smooth muscle. It has also been reported to activate the enzyme PGK1. Its efficacy in its usual indications is established, but nothing in this package links these actions to hair growth.

The high score most likely reflects the drug's proximity to hair-disorder nodes in the knowledge graph, not a known pharmacological mechanism. Alpha-1 blockade has no established role in genetic hypotrichosis. Other hair-related predictions for this drug point in opposite directions: several concern hair loss and one concerns hair excess (Ambras hypertrichosis). This pattern suggests a graph-proximity artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12672P | APO-TERAZOSIN TABLET 2 mg | Tablet | Not listed |
| SIN11676P | HYTRIN TABLET 5 mg | Tablet | Not listed |
| SIN11674P | HYTRIN TABLET 1 mg | Tablet | Not listed |
| SIN11675P | HYTRIN TABLET 2 mg | Tablet | Not listed |
| SIN11600P | TERASIN TABLET 2 mg | Tablet | Not listed |

All five products are oral tablets.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the evidence package.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This indication rests on a model score alone, with no trials, no literature, and no plausible mechanism. It is most likely a knowledge-graph artifact.

**Other predicted indications for this drug:**
- **Raynaud disease** has the strongest mechanistic plausibility, since alpha-1 blockade causes peripheral vasodilation. It has one 1997 clinical study (PMID 9273472) whose design and size are unverified, and it is rated L4 (Research Question).
- **Migraine disorder** has two older papers, a 1994 open study (PMID 7911406) and a 1997 review (PMID 9074296), and is also rated L4.
- **Alopecia** has only one narrative review whose content on terazosin is unverified.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA, which are currently missing and block safety screening
- Approved indication text for the Singapore licences
- Detailed mechanism of action data, for example from DrugBank
- Abstract and full-text review of the supporting papers if any hair-related indication is pursued
- A review of the Raynaud disease candidate as a separate protocol, since it is the more credible repurposing lead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

