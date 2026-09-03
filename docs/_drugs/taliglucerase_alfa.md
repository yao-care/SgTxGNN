---
layout: default
title: Taliglucerase Alfa
parent: 僅模型預測 (L5)
nav_order: 943
evidence_level: L5
indication_count: 10
---

# Taliglucerase Alfa
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

# Taliglucerase Alfa: From Gaucher Disease to Lysosomal Storage Disease with Skeletal Involvement

## One-Sentence Summary

Taliglucerase alfa is a recombinant glucocerebrosidase enzyme replacement therapy; registry data on its original indication is missing, but literature confirms established use in **Type 1 Gaucher disease**. Of the 10 TxGNN-predicted indications reviewed, 9 — including the top-ranked "Hurler syndrome" (score 99.52%) — have **zero clinical trial or literature support** and are flagged by the model's own rationale as knowledge-graph clustering noise (unrelated enzyme targets). The only indication with real evidence, "Lysosomal Storage Disease with Skeletal Involvement," is supported by **2 publications** but mechanistically corresponds to Gaucher disease itself rather than a genuinely novel indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in registry data (Data Gap); literature indicates Type 1 Gaucher disease |
| Predicted New Indication | Lysosomal Storage Disease with Skeletal Involvement (mechanistically = Gaucher disease phenotype) |
| TxGNN Prediction Score | 98.94% (rank 10,953) — Note: the highest-scoring candidate overall, Hurler syndrome (99.52%), has no supporting evidence and is assessed separately below |
| Evidence Level | L1 (per scoring; underlying literature is real-world cohort + review, not RCT) |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails (this indication only); **Hold** on all other 9 predicted indications |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on known information, taliglucerase alfa is a recombinant human glucocerebrosidase, used as enzyme replacement therapy to reduce glucocerebroside accumulation in macrophages caused by GBA1 gene mutations — the defect underlying Gaucher disease.

"Lysosomal Storage Disease with Skeletal Involvement" is not a distinct new indication in the pharmacological sense — skeletal involvement (bone infarcts, avascular necrosis, growth retardation) is a well-documented manifestation of Type 1 Gaucher disease, the drug's own approved indication. The TxGNN model has effectively rediscovered the drug's known indication under an alternate disease-ontology label, which explains why this is the only candidate among the top 10 with genuine clinical and literature backing.

By contrast, the remaining 9 predictions (Hurler syndrome, Scheie syndrome, adrenal adenoma, ichthyosis syndrome, cholesteryl ester storage disease, Wolman disease ×2, proximal myopathy, growth hormone insensitivity syndrome) target **different enzyme deficiencies** (alpha-L-iduronidase, lysosomal acid lipase, etc.) that do not overlap with glucocerebrosidase substrate metabolism. Their high TxGNN scores likely reflect the model's tendency to cluster diseases within the broad "lysosomal storage disease" category rather than true mechanistic relevance — a limitation explicitly noted in each candidate's own rationale text, and consistent with zero clinical trials or publications found for any of them.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41096096](https://pubmed.ncbi.nlm.nih.gov/41096096/) | 2025 | Cohort (real-world) | Journal of Clinical Medicine | 10-year prospective follow-up of taliglucerase alfa in Type 1 Gaucher disease (Albania); confirms long-term efficacy/safety in treatment-naïve and previously-treated patients |
| [22916340](https://pubmed.ncbi.nlm.nih.gov/22916340/) | 2012 | Review | Drugs of Today | Overview of taliglucerase alfa mechanism (glucocerebrosidase replacement) and its role in treating Gaucher's disease, including hematologic and skeletal manifestations |

## Singapore Market Information

Taliglucerase alfa is **not currently marketed** in Singapore — no authorization records (0 licenses) are on file.

## Safety Considerations

Please refer to the package insert for safety information. TFDA/HSA label warnings, contraindications, and drug-drug interaction data could not be retrieved for this evidence pack (see Data Gap DG001 below).

## Conclusion and Next Steps

**Decision: Hold** (for genuinely novel indications) / **Proceed with Guardrails** (for skeletal-involvement/Gaucher re-indication only)

**Rationale:**
Nine of the ten TxGNN-predicted indications have no clinical or literature evidence and target biologically unrelated enzyme deficiencies — these should not proceed. The one indication with real evidence support is not a novel repurposing opportunity but a restatement of the drug's known Gaucher disease indication, so any "guardrailed" progress should be framed as expanding documentation of existing use (e.g., skeletal outcome data), not as new-indication development.

**To proceed, the following is needed:**
- **[Blocking]** TFDA/HSA label warnings and contraindications (DG001) — required before any safety pre-assessment (S1) can begin
- **[High]** Confirmed mechanism of action from DrugBank (DG002) — needed to formally validate/reject mechanistic links for all 10 candidates
- Confirmation of the drug's actual original approved indication(s), since registry data (`original_indications`) is currently empty
- If pursuing the skeletal-involvement angle: additional RCT-level evidence beyond the single cohort study to support upgrading past L1/S3
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

