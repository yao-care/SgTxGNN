---
layout: default
title: Mesterolone
parent: 僅模型預測 (L5)
nav_order: 648
evidence_level: L5
indication_count: 10
---

# Mesterolone
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

# Mesterolone: From Original Indication (Not on File) to Gout

## One-Sentence Summary

> Mesterolone (DrugBank ID DB13587) is an androgen-class compound; this evidence pack contains **no verified original approved indication or mechanism-of-action data** (both flagged as data gaps). TxGNN's top-ranked prediction is **Gout**, but the underlying rationale describes a known **risk association** (androgens raising serum uric acid), not a therapeutic one — and the search found **0 clinical trials and 0 publications** directly supporting Mesterolone for gout. Across all 10 TxGNN-predicted indications reviewed for this drug, evidence is uniformly weak (L5, one L4), and none currently supports repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no original indication or Singapore license/label on file (data gap) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 98.20% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Mesterolone is not available in this evidence pack (data gap **DG002**, High severity — impacts mechanistic-relevance analysis). Likewise, no original approved indication is recorded here: `original_indications` is empty and Singapore market data shows zero registrations, so there is no baseline indication to compare the new prediction against.

More importantly, the rationale attached to this specific prediction argues **against**, rather than for, a therapeutic link. Androgen-class drugs like Mesterolone are known to reduce renal urate excretion and raise serum uric acid — a mechanism associated with **increased gout risk**, not gout treatment. TxGNN's high similarity score most likely reflects this known drug–risk (comorbidity) relationship embedded in the knowledge graph, rather than a genuine repurposing opportunity. This is reinforced by the fact that targeted searches across ClinicalTrials.gov, ICTRP, and PubMed for "Mesterolone + gout" all returned zero results (see query log IDs 3–5), meaning there is no independent literature to counter or support the mechanistic concern.

Given this, the Gout prediction should be read as a **caution signal about the graph embedding, not a treatment lead**. It does not currently meet even a preliminary bar for repurposing consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

No Singapore registration currently on file. `taiwan_regulatory.total_licenses = 0` and `market_status = 未上市 (Not Marketed)` — Mesterolone has no active license or approved-indication text to draw from in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information — this evidence pack does not contain verified warnings, contraindications, or drug-interaction records for Mesterolone (`key_warnings`, `contraindications`, and DDI search all returned no data; DDI query status: *not_found*).

**Note on data completeness:** the missing product label/warning data is logged as data gap **DG001** (severity: **Blocking**), meaning this candidate cannot proceed to a Stage 1 (S1) safety evaluation until TFDA/HSA labeling is obtained and parsed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rank-1 candidate (Gout) is supported only by a model score, with its own stated mechanism pointing to a risk relationship rather than a treatment effect, and zero clinical or literature evidence. Reviewing all 10 TxGNN-predicted indications for Mesterolone in this pack: eight are Hold with no mechanistic support or corroborating evidence (several explicitly flagged in the evidence pack as likely false-positive graph associations, e.g. the 18-literature cluster for "brain small vessel disease... with ocular anomalies," which is topically unrelated to androgen pharmacology); one ("autoimmune oophoritis") is marked "Research Question" but carries major safety concerns for the implied patient population; and one (heart disease, L4) is supported only by preclinical evidence of *adverse* cardiac remodeling and worsened lipid profile (PMID 18808528) — a safety warning, not a repurposing signal. No candidate in this pack currently justifies advancement.

**To proceed, the following is needed:**
- TFDA/HSA product label (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Verified mechanism-of-action data from DrugBank (currently data gap DG002)
- Confirmation of Mesterolone's original approved indication(s), none of which are on file in this pack
- If the gout signal is to be pursued at all, dedicated studies directly testing therapeutic (not risk) effects of Mesterolone in gout/urate metabolism
- A cardiovascular risk assessment in light of preclinical cardiac toxicity evidence (PMID 18808528) before any further human-use consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

