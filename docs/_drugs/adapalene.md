---
layout: default
title: Adapalene
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Adapalene
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

# Adapalene: From Acne Vulgaris to Sebaceous Gland Anomaly

## One-Sentence Summary

Adapalene is a third-generation topical retinoid with established use in acne vulgaris, working by selectively modulating retinoic acid receptors (RAR-β/γ) to normalize pilosebaceous unit function and suppress local inflammation.
The TxGNN model evaluated 10 predicted indications across the full pilosebaceous disease spectrum; **Sebaceous Gland Anomaly** carries the strongest clinical evidence, supported by **2 completed clinical trials** (including 1 Phase 3, n=452) and **1 preclinical study**.
Among all predictions in this multi-indication report, sebaceous gland anomaly is the only candidate reaching L2 evidence level and the only one recommended to **Proceed with Guardrails**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acne vulgaris |
| Predicted New Indication | Sebaceous Gland Anomaly |
| TxGNN Prediction Score | 85.16% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Adapalene is a third-generation synthetic retinoid that selectively binds retinoic acid receptors RAR-β and RAR-γ. This receptor selectivity differentiates it from earlier pan-retinoid agents, enabling targeted modulation of keratinocyte differentiation within the follicular canal without the broad systemic effects associated with non-selective retinoids. At the cellular level, adapalene normalizes aberrant cornification of the pilosebaceous duct epithelium, preventing microcomedone formation — the earliest pathological event in acne and related pilosebaceous disorders. Its additional anti-inflammatory effects, mediated through inhibition of TLR-2 signalling and suppression of IL-6/IL-8 cytokines, further address the inflammatory component that is a hallmark of pilosebaceous disease.

"Sebaceous gland anomaly" as a diagnostic category encompasses disorders of the pilosebaceous unit characterized by abnormal sebaceous secretion, ductal architecture, or inflammatory changes — the same anatomical target as adapalene's core mechanism of action. The mechanistic link is therefore direct rather than analogical: adapalene already acts on sebaceous ductal keratinocytes, the precise cell type dysregulated in sebaceous gland anomalies. From a clinical coding perspective, the overlap between "sebaceous gland anomaly" and acne-spectrum disease is substantial, meaning that existing clinical trial data for acne vulgaris is directly applicable to this indication.

A completed Phase 3 trial (NCT00446043, n=452, 12 months) provides robust long-term safety and efficacy data for adapalene in acne — a condition defined pathologically by sebaceous gland dysfunction. This prediction is well-grounded in both mechanism and clinical precedent, and represents the most actionable finding in this multi-indication analysis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00446043](https://clinicaltrials.gov/study/NCT00446043) | Phase 3 | Completed | 452 | Long-term (12-month), multicentre, open-label study of adapalene 0.1%/BPO 2.5% gel in acne vulgaris; evaluates local tolerability (erythema, scaling, dryness, stinging/burning), haematological parameters, and blood chemistry at 10 time points over 52 weeks — strongest direct evidence for adapalene on pilosebaceous pathology |
| [NCT02557399](https://clinicaltrials.gov/study/NCT02557399) | Phase 4 | Completed | 350 | Multicentre, single-blind, active-controlled RCT in Japanese subjects comparing BPO/clindamycin (Duac®) vs. adapalene 0.1% + clindamycin 1%; provides head-to-head comparative efficacy data and Asian-population safety profile relevant to a Singapore regulatory submission |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25217865](https://pubmed.ncbi.nlm.nih.gov/25217865/) | 2014 | Animal Study | Journal of Dermatological Science | Adapalene 0.1% reduces comedone formation in the Kyoto Rhino Rat model (ENU-induced Hr gene nonsense mutation); demonstrates comedolytic activity in non-inflammatory pilosebaceous lesions and provides mechanistic evidence that adapalene directly modifies sebaceous gland pathology at the structural level |

---

## Singapore Market Information

Adapalene is **not currently registered or marketed in Singapore**. No HSA-licensed products are on record (0 authorizations). This absence means any indication claim — including the currently approved acne indication — would require a full new drug application or registration via the HSA Drug Regulatory Route before clinical use in Singapore can proceed.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** Package insert warnings, contraindications, and drug–drug interaction data were not available in this Evidence Pack (classified as Data Gaps DG001 and DG002). Prior to any regulatory submission or clinical use assessment, the following must be retrieved: (1) full SmPC/labelling from an approved jurisdiction (e.g., EMA, US FDA, or TGA), and (2) DrugBank MOA and pharmacokinetic profile. Key class-level considerations for topical retinoids include local skin reactions (erythema, dryness, photosensitivity) and pregnancy contraindication.

---

## Prediction Landscape Overview

For context, the full set of 10 TxGNN predictions for adapalene is summarised below. Only rank 9 has actionable clinical evidence.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|----------------|----------------|
| 1 | Zinc, elevated plasma | 99.51% | L5 | Hold |
| 2 | Isolated congenital adermatoglyphia | 98.80% | L5 | Hold |
| 3 | Beare-Stevenson cutis gyrata syndrome | 98.78% | L5 | Hold |
| 4 | Demodicidosis of sebaceous gland | 95.45% | L5 | Research Question |
| 5 | PAPA syndrome | 95.30% | L5 | Research Question |
| 6 | Prolidase deficiency | 89.33% | L5 | Hold |
| 7 | Drug-induced osteoporosis | 87.21% | L5 | Hold |
| 8 | Seborrheic dermatitis | 86.28% | L4 | Research Question |
| **9** | **Sebaceous gland anomaly** | **85.16%** | **L2** | **Proceed with Guardrails** |
| 10 | Inherited skin tumor | 82.92% | L5 | Research Question |

High TxGNN scores at ranks 1–7 reflect knowledge graph topology bias rather than clinical plausibility — these predictions lack biological rationale support in the literature and are rated Hold. Seborrheic dermatitis (rank 8) has indirect mechanistic plausibility (normalisation of keratinocyte differentiation, sebum regulation) and warrants monitoring as a **Research Question** if further mechanistic studies emerge.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Adapalene's core mechanism of action directly targets the pilosebaceous unit — the anatomical structure underlying sebaceous gland anomalies — and a completed Phase 3 trial (n=452, 12 months) provides robust long-term safety data meeting L2 evidence criteria. The prediction represents a mechanistically justified extension of adapalene's existing indication scope rather than a speculative leap.

**To proceed, the following is needed:**
- **Regulatory pathway:** Initiate HSA registration assessment for adapalene (currently 0 Singapore-licensed products); determine whether a full NDA or abridged application referencing approved US/EU labelling is feasible
- **Safety data retrieval:** Obtain full SmPC/package insert to address Data Gaps DG001 (warnings/contraindications) and DG002 (MOA) before any Stage 1 safety evaluation can be completed
- **ICD coding clarification:** Confirm whether the target patient population coded as "sebaceous gland anomaly" is clinically distinguishable from standard acne vulgaris in Singapore clinical practice — if not, existing acne approval in a reference jurisdiction may directly support label use
- **Formulation confirmation:** Verify which topical dosage forms (gel, cream, lotion) and concentrations (0.1%, 0.3%) are commercially available for import or local manufacturing
- **Seborrheic dermatitis watch:** Flag rank 8 (seborrheic dermatitis) for re-evaluation if a dedicated Phase 2 trial emerges — mechanistic rationale exists but current evidence is insufficient for a regulatory submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

