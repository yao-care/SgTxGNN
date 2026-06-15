---
layout: default
title: Carbimazole
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Carbimazole
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

# Carbimazole: From Hyperthyroidism to Resistance to Thyroid Hormone (THR-β Mutation)

## One-Sentence Summary

Carbimazole is a thionamide antithyroid drug, converted in vivo to its active metabolite methimazole, and widely used as a first-line treatment for hyperthyroidism including Graves' disease.
The TxGNN model predicts it may be effective for **resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (RTH-β)**,
with **0 clinical trials** and **1 case report** currently supporting this direction — and critically, the mechanistic rationale is **contradictory** rather than supportive.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperthyroidism (Graves' disease) — well-established pharmacological use; no Singapore HSA registration found |
| Predicted New Indication | Resistance to thyroid hormone due to THR-β mutation (RTH-β) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Carbimazole is a thionamide prodrug that is rapidly hydrolysed to methimazole after oral ingestion. Methimazole inhibits thyroid peroxidase (TPO), thereby blocking the oxidation of iodide and the subsequent coupling of iodotyrosines required to synthesise thyroxine (T4) and triiodothyronine (T3). In addition, there is evidence from controlled studies (PMID 6247656) that carbimazole exerts a direct immunomodulatory effect, reducing TSH receptor antibody (TRAb) and microsomal antibody titres independent of its hormone-lowering action — making it particularly useful in autoimmune-driven hyperthyroidism.

Resistance to thyroid hormone due to THR-β mutation (RTH-β) is a rare genetic disorder caused by loss-of-function mutations in the *THRB* gene. Impaired intracellular thyroid hormone signalling means TSH is not appropriately suppressed despite elevated serum fT4 and fT3 — resulting in a paradoxical picture of high free thyroxine with normal or elevated TSH. Patients may appear clinically euthyroid or show selective features of hypothyroidism (e.g., goitre) and hyperthyroidism simultaneously depending on tissue receptor distribution.

The mechanistic case for carbimazole in RTH-β is, in fact, **contradictory rather than supportive**. Reducing thyroid hormone synthesis would further lower the already-impaired thyroid hormone signal reaching target tissues. Tissues expressing wild-type THR-α (e.g., heart, bone) that are not protected by the THR-β mutation would receive even less T3, potentially worsening tachycardia or osteoporosis in a different direction than intended. The high TxGNN prediction score (99.71%) most likely reflects knowledge-graph co-occurrence bias — RTH-β and Graves' disease share multiple thyroid-axis nodes — rather than genuine mechanistic applicability. The one available case report (PMID 24165508) illustrates precisely this failure: a patient incorrectly treated with carbimazole for a decade with no normalisation of thyroid indices.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | Case report | BMJ Case Reports | Young man treated intermittently with carbimazole for 10 years after elevated fT4 (25–35.7 pmol/L) with persistently non-suppressed TSH (6.78–22.1 mIU/L); later identified as RTH-β. Carbimazole failed to normalise thyroid function, illustrating mechanistic mismatch. |

---

## Singapore Market Information

Carbimazole has no registered products in the Singapore HSA database. It is not currently marketed in Singapore.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
RTH-β is a receptor-level disorder; reducing thyroid hormone synthesis with carbimazole does not address the underlying signalling defect and is likely to worsen the clinical picture in thyroid-hormone-sensitive tissues that retain intact receptor function. The sole supporting literature is a case report documenting treatment failure, not success.

**To proceed, the following is needed:**

- Mechanistic pre-clinical work clarifying whether selective peripheral T4/T3 reduction could benefit any RTH-β subgroup (e.g., protecting cardiac tissue from excess T3 via THR-α without impairing THR-β-dependent pathways)
- Genetic stratification studies to identify RTH-β patients who might have a differential tissue response to reduced circulating thyroid hormone
- Singapore HSA regulatory pathway assessment, as Carbimazole has no current local registration and market entry would require a full submission
- Full MOA data retrieval from DrugBank API (DG002) and TFDA package insert parsing (DG001) before any safety evaluation can proceed

---

> **Important notice:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require prospective clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

