---
layout: default
title: Lithium Carbonate
parent: 僅模型預測 (L5)
nav_order: 557
evidence_level: L5
indication_count: 10
---

# Lithium Carbonate
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

# Lithium Carbonate: From Bipolar Disorder to Pseudoachondroplasia

## One-Sentence Summary

Lithium carbonate is a classic mood stabilizer with over 60 years of clinical use, primarily indicated for bipolar disorder and mania — though no Singapore registration currently exists for this compound.
The TxGNN model predicts it may be effective for **Pseudoachondroplasia**, a rare skeletal dysplasia caused by COMP gene mutations, via its GSK-3β inhibitory and autophagy-inducing properties.
Currently, **no clinical trials and no publications** directly support this specific indication, placing this prediction at evidence level **L5** with a recommendation to **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bipolar disorder / mood disorders (established use; no Singapore regulatory record) |
| Predicted New Indication | Pseudoachondroplasia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the current Evidence Pack (Data Gap DG002). Based on established pharmacological literature, lithium carbonate exerts its effects primarily through two well-characterised mechanisms: (1) **inhibition of glycogen synthase kinase-3β (GSK-3β)**, which stabilises β-catenin and activates the WNT/β-catenin signalling pathway; and (2) **depletion of free inositol** (the inositol depletion hypothesis), which suppresses downstream second-messenger cascades. Beyond these, lithium is known to induce autophagy through an mTOR-independent pathway, upregulate BDNF (neuroprotection), increase Bcl-2 expression (anti-apoptosis), and — critically for several indications in this prediction set — stimulate neutrophil release and cause clinically observable leukocytosis.

Pseudoachondroplasia is a rare autosomal dominant skeletal dysplasia caused by heterozygous missense mutations in the **COMP gene** (cartilage oligomeric matrix protein). The mutant COMP protein misfolds and accumulates within the endoplasmic reticulum (ER) of chondrocytes, triggering chronic ER stress, impaired growth plate function, and disproportionate short stature. Lithium's GSK-3β inhibition could theoretically promote chondrogenesis by activating WNT/β-catenin — a pathway integral to growth plate maintenance. Separately, lithium's mTOR-independent autophagy induction could theoretically facilitate clearance of the misfolded COMP protein aggregates from chondrocyte ER.

These mechanistic connections are, however, **indirect and speculative**. Neither lithium's chondrogenic effect nor its autophagy-mediated COMP clearance has been validated in disease-relevant models — whether in COMP-mutant cell lines, organoids, or animal models. The TxGNN prediction reflects knowledge graph topology (shared molecular pathway nodes) rather than functional experimental evidence. This level of biological plausibility is sufficient to justify monitoring but not to justify preclinical investment without further target validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for lithium carbonate in pseudoachondroplasia.

---

## Literature Evidence

Currently no related literature available for lithium carbonate in pseudoachondroplasia.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety data for this compound is not available in the current Evidence Pack (TFDA package insert warnings and contraindications: Data Gap DG001; drug interaction database: not found). This is classified as a Blocking data gap and must be resolved before any formal indication evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications in this batch are currently at L5 evidence level — pure model predictions with no clinical trials and no supporting publications in any of the specific disease contexts queried. The mechanistic connection for the top-ranked indication (pseudoachondroplasia) is theoretically plausible but entirely unvalidated, and the drug has no Singapore market presence.

---

**⚑ Priority Signal — WHIM Syndrome (Rank 9) deserves separate evaluation:**

Among all 10 predicted indications, **WHIM syndrome** carries the strongest pharmacological rationale and is scored separately as "Research Question" rather than "Hold." WHIM syndrome (Warts, Hypogammaglobulinaemia, Infections, Myelokathexis) is caused by gain-of-function mutations in **CXCR4** (e.g., R334X), causing pathological neutrophil retention in the bone marrow. Lithium carbonate's most robustly documented haematological effect is **neutrophil mobilisation and leukocytosis**, with proposed mechanisms including G-CSF stimulation and possible modulation of the CXCR4/CXCL12 retention axis. The disease-drug logic is directly opposed and potentially complementary: CXCR4 GOF traps neutrophils in marrow → lithium promotes neutrophil release from marrow. This is the only pairing in this batch where a known clinical drug effect maps directly onto the core disease mechanism. It merits dedicated literature review and feasibility assessment.

---

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Obtain Singapore/Taiwan package insert to extract key warnings, contraindications, and approved indications before any safety evaluation
- **[DG002 — High]** Query DrugBank API for full MOA data to support mechanistic analysis
- **[Pseudoachondroplasia]** Conduct targeted literature search: lithium + COMP mutation / ER stress / chondrocyte autophagy
- **[WHIM Syndrome — Priority]** Conduct dedicated feasibility assessment: lithium + CXCR4 + neutrophil mobilisation; search for case reports or off-label use in chronic neutropenia
- **[All indications]** All 10 targets are rare genetic disorders with structural/developmental aetiology — confirm that post-natal pharmacological intervention is conceptually feasible before committing resources to any preclinical model
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

