---
layout: default
title: Carfilzomib
parent: 僅模型預測 (L5)
nav_order: 212
evidence_level: L5
indication_count: 10
---

# Carfilzomib
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

# Carfilzomib: From Multiple Myeloma to CMM7 (Cutaneous Malignant Melanoma 7)

## One-Sentence Summary

Carfilzomib (Kyprolis®) is a second-generation, irreversible proteasome inhibitor globally approved for the treatment of relapsed/refractory multiple myeloma.
The TxGNN model assigns its highest prediction score to **CMM7 (Cutaneous Malignant Melanoma 7, OMIM #612263)** — a genetic susceptibility locus rather than an independent disease target — with a score of **99.37%** but **no supporting clinical trials or published literature**.
The more actionable repurposing direction within this evidence pack is **myeloid leukemia (rank 8)**, which is supported by a completed Phase 1 clinical trial and multiple preclinical studies, and warrants further evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple Myeloma (relapsed/refractory) — globally approved; not registered in Singapore |
| Predicted New Indication | CMM7 (Cutaneous Malignant Melanoma 7, OMIM #612263) |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Carfilzomib is a selective, irreversible inhibitor of the 20S proteasome — specifically its β5 chymotrypsin-like active site. As the brand Kyprolis®, it is an established treatment for relapsed/refractory multiple myeloma, a malignancy in which plasma cells are heavily dependent on the ubiquitin-proteasome system (UPS) for maintaining protein homeostasis. By permanently blocking proteasomal degradation, carfilzomib triggers proteotoxic stress and activates the mitochondrial apoptotic pathway. This mechanism is well-supported by Phase 3 trials (ASPIRE, ENDEAVOR) in myeloma, and its clinical efficacy is not in dispute in that indication.

CMM7, however, is not a treatble disease entity in the conventional sense. It designates a **hereditary melanoma susceptibility locus** driven by CDK4 gain-of-function mutations that increase the lifetime risk of cutaneous melanoma. There is no direct mechanistic link between irreversible proteasome inhibition and CDK4-mediated genomic predisposition. The high TxGNN score (99.37%) most likely reflects **topological proximity in the knowledge graph** between myeloma-associated protein nodes and melanoma-related genetic loci — not a biologically actionable relationship. This is a known limitation of graph-based predictions when genetic risk loci are represented alongside disease phenotype nodes.

Among the 10 predicted indications in this evidence pack, **myeloid leukemia (rank 8, L3)** presents the most credible repurposing opportunity: AML cells rely on the UPS to degrade pro-survival proteins (MCL-1, p53 negative regulators), and the completed Phase 1 trial NCT01137747 (PMID 26674111, n=18) has already established an initial safety profile and maximum tolerated dose. Preclinical evidence further demonstrates synergy with tyrosine kinase inhibitors in CML models and enhancement of CAR-NK cell efficacy in AML. Myeloid leukemia — not CMM7 — should be the primary focus for any subsequent research investment.

---

## Clinical Trial Evidence

Currently no clinical trials registered for CMM7 in relation to Carfilzomib.

---

## Literature Evidence

Currently no related literature available for CMM7 in relation to Carfilzomib.

---

## Singapore Market Information

Carfilzomib is not registered with Singapore's Health Sciences Authority (HSA). No product authorizations, approved indications, or registered dosage forms are on record.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Second-generation proteasome inhibitor (irreversible, epoxyketone class) |
| Myelosuppression Risk | High — thrombocytopenia and neutropenia are common dose-limiting toxicities; anaemia also reported |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential and platelet count, serum creatinine and eGFR, left ventricular ejection fraction (LVEF), blood pressure (hypertension risk), pulmonary function |
| Handling Protection | Must comply with cytotoxic drug handling regulations; IV preparation to be performed in a certified pharmacy under appropriate containment |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Detailed warnings and contraindications (data gap DG001) were not available from the Singapore HSA package insert at the time of this report. Carfilzomib carries established cardiovascular risks (cardiac failure, hypertension, pulmonary arterial hypertension) based on global regulatory labelling — formal local documentation should be retrieved before any clinical evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
CMM7 is a genetic susceptibility locus, not an independent therapeutic target; there is no mechanistic basis for applying proteasome inhibition to CDK4-mediated hereditary melanoma predisposition, and the evidence level is L5 (model prediction only). The high TxGNN score reflects knowledge graph topology rather than biological plausibility, and this prediction should be deprioritised or excluded from further evaluation.

**To proceed effectively with this drug, the following is needed:**

- **Redirect focus to myeloid leukemia (rank 8):** This is the most actionable indication in this evidence pack, with Phase 1 data (NCT01137747 / PMID 26674111), mechanistic rationale, and an emerging combination strategy (proteasome inhibition + CAR-T/NK)
- **Obtain Phase 2 efficacy data** for Carfilzomib in AML/CML combination regimens (e.g., with TKIs or immunotherapy) to advance evidence from L3 toward L2
- **Resolve data gap DG001:** Download and parse the Singapore HSA (or FDA/EMA) package insert to retrieve complete warnings, contraindications, and approved indication text
- **Resolve data gap DG002:** Query the DrugBank API to retrieve full MOA, pharmacokinetics, and DrugBank category data to enable proper mechanism-relevance scoring
- **Establish a cardiovascular risk protocol** before any clinical evaluation — carfilzomib's cardiac toxicity (heart failure, hypertension) requires prospective LVEF monitoring and patient selection criteria
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

