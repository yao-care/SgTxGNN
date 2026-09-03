---
layout: default
title: Pimecrolimus
parent: 僅模型預測 (L5)
nav_order: 784
evidence_level: L5
indication_count: 10
---

# Pimecrolimus
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

# Pimecrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

> Pimecrolimus (Elidel®) is a topical calcineurin inhibitor originally developed and registered for mild-to-moderate atopic dermatitis (eczema).
> The TxGNN model predicts it may also be effective for **Seborrheic Dermatitis**,
> with **1 completed randomized controlled trial** currently supporting this direction (no dedicated literature yet indexed).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic dermatitis, mild-to-moderate (per global registered indication referenced in clinical trial records; no Singapore-specific label text available) |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available in the current record (`original_moa: [Data Gap]`). However, based on the supporting literature captured in this evidence pack, Pimecrolimus is known as an ascomycin-derivative topical calcineurin inhibitor. It selectively inhibits T-cell activation and blocks release of pro-inflammatory cytokines (IL-2, IL-4, IFN-γ, TNF-α), and also inhibits mast cell degranulation — while, unlike tacrolimus, having minimal effect on Langerhans cell differentiation and maturation.

Atopic dermatitis and seborrheic dermatitis are both chronic inflammatory dermatoses with a significant T-cell-mediated inflammatory component, even though seborrheic dermatitis also involves a *Malassezia* yeast colonization factor. Because Pimecrolimus's core pharmacology targets the T-cell/cytokine-driven inflammatory axis rather than a disease-specific antigen, its anti-inflammatory action is mechanistically plausible for seborrheic dermatitis as an extension of its established anti-inflammatory use in eczema.

This is not purely theoretical: a completed Phase 2, randomized, double-blind, active-comparator-controlled trial (NCT00403559, n=113) directly tested Pimecrolimus against an active comparator for seborrheic dermatitis, which is why this candidate reaches Evidence Level L2 rather than a prediction-only L5.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00403559](https://clinicaltrials.gov/study/NCT00403559) | Phase 2 | Completed | 113 | 4-week randomized, double-blind, parallel-group, active-comparator-controlled exploratory study evaluating Elidel (Pimecrolimus) for treatment of seborrheic dermatitis |

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Pimecrolimus is currently **not marketed** in Singapore, and no HSA license records were found in this evidence pack (total registrations: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

**Additional note:** Topical calcineurin inhibitors as a class (including Pimecrolimus) carry a well-known long-term malignancy safety signal that has been the subject of systematic review (PMID: 36370744, *Lancet Child & Adolescent Health*, 2023, cancer risk meta-analysis in atopic dermatitis patients exposed to pimecrolimus/tacrolimus). This was not captured in the structured `safety` fields of this evidence pack (marked as Data Gap) and should be explicitly retrieved and reviewed before any regulatory or clinical decision.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed, randomized, active-comparator-controlled Phase 2 trial directly supports Pimecrolimus's efficacy in seborrheic dermatitis (Evidence Level L2), and the drug's known anti-inflammatory mechanism is biologically consistent with this indication. However, the drug is not currently marketed in Singapore, and critical safety documentation is missing.

**To proceed, the following is needed:**
- **[Blocking]** Official label warnings/contraindications (equivalent to TFDA/HSA package insert) — required before any S1 safety pre-assessment can proceed
- **[High priority]** Formal DrugBank/regulatory mechanism-of-action documentation to confirm the mechanistic linkage described above
- Confirmation of Singapore/regional market entry pathway, since there are currently zero local registrations
- Retrieval of the topical calcineurin inhibitor class malignancy safety signal (see PMID 36370744) into formal safety review before advancing past S3
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

