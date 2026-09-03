---
layout: default
title: Propylthiouracil
parent: 僅模型預測 (L5)
nav_order: 828
evidence_level: L5
indication_count: 10
---

# Propylthiouracil
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

# Propylthiouracil: From Hyperthyroidism to Resistance to Thyroid Hormone (RTH-β)

## One-Sentence Summary

Propylthiouracil (PTU) is a thionamide antithyroid drug historically used to treat hyperthyroidism (Graves' disease, thyrotoxicosis) by suppressing thyroid hormone synthesis. The TxGNN model predicts potential relevance to **Resistance to Thyroid Hormone due to a Mutation in Thyroid Hormone Receptor Beta (RTH-β)**, but this is currently supported only by **0 clinical trials** and **6 case-report/mechanistic publications**, several of which actually describe PTU treatment failing in this condition rather than helping it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperthyroidism / Graves' disease (thyrotoxicosis) — inferred from literature context; not confirmed via Singapore regulatory filings, as the drug is not marketed there |
| Predicted New Indication | Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank for this candidate. Based on known pharmacology, propylthiouracil is a thionamide that inhibits thyroid peroxidase, blocking iodide organification and iodotyrosine coupling, thereby reducing thyroid hormone synthesis. Its efficacy in hyperthyroid states (Graves' disease, thyrotoxicosis) is well established in clinical practice.

RTH-β, however, is a different kind of disorder: a germline mutation in the thyroid hormone receptor beta gene reduces target-tissue sensitivity to thyroid hormone. Patients typically present with elevated free T4/T3 but non-suppressed TSH, which can superficially mimic hyperthyroidism and lead clinicians to mistakenly start antithyroid drugs. Because PTU only lowers hormone production without correcting the receptor defect, it does not address the underlying pathology — and one of the papers in this evidence pack (PMID 10724359) explicitly documents this: a patient was given propylthiouracil for presumed thyrotoxicosis, and her goiter *enlarged* rather than resolving, consistent with treatment failure once RTH-β was correctly diagnosed.

This suggests the high TxGNN score likely reflects strong textual co-occurrence — PTU is frequently mentioned in RTH-β case reports as a misdiagnosis pitfall — rather than a genuine mechanistic rationale for therapeutic benefit. This pattern mirrors what the evidence pack already flags for other candidates in this drug's prediction list (e.g., Hashimoto thyroiditis, rank 4, and Prinzmetal angina, rank 9), where high-scoring predictions were also found to rest on incidental or contraindicated associations rather than efficacy signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18561095](https://pubmed.ncbi.nlm.nih.gov/18561095/) | 2009 | Case report | Exp Clin Endocrinol Diabetes | Turkish family with TR-β P453A mutation causing RTH; describes diagnostic features, not PTU treatment outcomes |
| [14684607](https://pubmed.ncbi.nlm.nih.gov/14684607/) | 2004 | Mechanistic (animal) study | Endocrinology | Mouse model shows mutant TR-β acts as dominant-negative in cardiac tissue, explaining tissue-selective TH resistance |
| [22919057](https://pubmed.ncbi.nlm.nih.gov/22919057/) | 2012 | Mechanistic (animal) study | Endocrinology | TR-β mutant mice develop thyroid carcinoma driven by chronic TSH elevation; no PTU treatment data |
| [12201835](https://pubmed.ncbi.nlm.nih.gov/12201835/) | 2002 | Case report | Clinical Endocrinology | Family with TRβ M313T mutation; infant misdiagnosed with neonatal thyrotoxicosis, responded to antithyroid therapy transiently before RTH was recognized |
| [10724359](https://pubmed.ncbi.nlm.nih.gov/10724359/) | 1999 | Case report | Endocrine Journal | Thai woman with de novo TRβ L330S mutation; **PTU was given for presumed thyrotoxicosis, but her goiter enlarged**, indicating treatment did not address the underlying RTH |
| [21909131](https://pubmed.ncbi.nlm.nih.gov/21909131/) | 2012 | Mechanistic (animal) study | Oncogene | TR-β PV mutant mouse model shows thyroid hormone drives tumor proliferation; mechanistic, not PTU-focused |

---

## Singapore Market Information

Propylthiouracil is not currently registered or marketed in Singapore (0 authorizations on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials and only case-report/mechanistic literature supporting this indication, and part of that literature actually documents PTU treatment failing in RTH-β (a case where the goiter enlarged despite therapy). Combined with the absence of confirmed MOA data and Singapore market/label information, the evidence does not support advancing this candidate.

**To proceed, the following is needed:**
- TFDA/manufacturer label data on warnings and contraindications (currently a blocking data gap)
- Confirmed mechanism of action from DrugBank
- A systematic review or case series specifically evaluating outcomes of thyroid-suppressive therapy in genetically confirmed RTH-β patients, to clarify whether any subgroup (e.g., transient hyperthyroxinemic phases) could plausibly benefit
- Re-evaluation of the TxGNN scoring signal to rule out spurious co-occurrence-driven associations, given the pattern seen elsewhere in this drug's prediction set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

