---
layout: default
title: Bromhexine
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 10
---

# Bromhexine
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

# Bromhexine: From Respiratory Mucolysis to Vulvitis

## One-Sentence Summary

Bromhexine is a mucolytic agent widely used to reduce the viscosity of respiratory secretions, facilitating expectoration in patients with bronchitis and other airway conditions.
The TxGNN model predicts it may be effective for **Vulvitis**, with a prediction score of **83.75%**.
However, **no clinical trials and no relevant literature** currently support this direction — all top-10 predicted indications carry an **L5 evidence level** (model prediction only), and there is strong indication that the high scores reflect knowledge graph topological artefacts rather than genuine biological signals.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mucolytic agent for respiratory secretion management (not registered in Singapore) |
| Predicted New Indication | Vulvitis |
| TxGNN Prediction Score | 83.75% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacology, Bromhexine is a synthetic derivative of vasicine and acts as a mucolytic agent by depolymerising mucopolysaccharide fibres in bronchial secretions, thereby reducing sputum viscosity and facilitating mucociliary clearance. It is also known to act as a TMPRSS2 serine protease inhibitor, which attracted interest during the COVID-19 pandemic as a potential viral entry blocker.

Vulvitis is a localised inflammatory condition of the vulva, typically caused by infection, contact irritants, or autoimmune processes. There is no established pharmacological bridge between mucolytic activity or TMPRSS2 inhibition and vulvar inflammation.

The Evidence Pack's own mechanistic analysis strongly suggests these high TxGNN scores are driven by **knowledge graph (KG) topological clustering** rather than biological signal. Ranks 1, 4, 7, 8, 9, and 10 all belong to the same vulvar/vaginal disease cluster (vulvitis, vulvovaginitis, ulceration of vulva, vulvar neoplasm, bacterial vaginosis, vaginal discharge), which is a hallmark pattern of KG neighbourhood artefact — the model is measuring graph distance to a disease node cluster, not drug-disease biological affinity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top predicted indication (Vulvitis).

> **Note on retrieved literature:** Two papers were retrieved from PubMed during evidence collection for other predicted indications, but neither is relevant:
> - [PMID 2080031](https://pubmed.ncbi.nlm.nih.gov/2080031/) (retrieved for vaginitis) is a 1990 clinical report on **neonatal respiratory distress syndrome** — entirely unrelated to vaginal inflammation; this is a database name-matching artefact.
> - [PMID 28860846](https://pubmed.ncbi.nlm.nih.gov/28860846/) (retrieved for IBS) is a narrative review on **Ambroxol for fibromyalgia** — a different drug (Bromhexine's active metabolite) targeting a different condition; results cannot be extrapolated to Bromhexine or to irritable bowel syndrome.

---

## Singapore Market Information

Bromhexine currently holds **no product registrations** in Singapore. It is not an approved or marketed product under the Health Sciences Authority (HSA).

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (key warnings, contraindications, and drug-drug interactions) were not available in this Evidence Pack. Completing TFDA/HSA prescribing information retrieval is a **Blocking** prerequisite before any safety-dependent evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications carry L5 evidence (model prediction only), with zero supporting clinical trials and no relevant literature for any target indication. The clustering of six gynaecological/vulvovaginal disease nodes in the top-10 list strongly suggests a KG topological artefact — the predictions reflect structural graph proximity rather than actionable biological repurposing signal. There is no mechanistic basis linking Bromhexine's mucolytic or TMPRSS2-inhibitory activity to vulvar, vaginal, or vulvovaginal pathology.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Retrieve Singapore HSA / original market prescribing information to enable safety evaluation.
- **Resolve DG002 (High):** Obtain confirmed MOA data from DrugBank API to allow mechanistic bridging analysis.
- **KG artefact triage:** Investigate whether Bromhexine's known respiratory and TMPRSS2 pharmacology produces higher-confidence predictions outside the gynaecological node cluster (e.g., SARS-CoV-2, Sjögren's syndrome, or COPD indications, which have existing published evidence for Bromhexine).
- **Rerun TxGNN with debiased KG:** If feasible, remove or down-weight the vulvar/vaginal disease cluster's edges to test whether Bromhexine's top predictions shift to biologically coherent indications.
- **Do not invest clinical or regulatory resources** in any of the 10 predicted indications listed here until the artefact hypothesis is ruled out and at least one indication reaches L3 evidence level.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

