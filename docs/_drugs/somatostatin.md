---
layout: default
title: Somatostatin
parent: 僅模型預測 (L5)
nav_order: 918
evidence_level: L5
indication_count: 10
---

# Somatostatin
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

# Somatostatin: From an Undocumented Original Indication to Amenorrhea (Disease)

## One-Sentence Summary

> Somatostatin (DB09099) is a naturally occurring regulatory hormone; the evidence pack for this drug is missing its original approved indication and mechanism-of-action data.
> The TxGNN model predicts a possible link to **Amenorrhea (disease)** with a **98.64%** prediction score,
> but this is currently supported only by **0 clinical trials** and **15 publications**, none of which directly test somatostatin for this indication — evidence level is **L4** and the associated recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified — no approved indication data available in evidence pack |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 98.64% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for somatostatin in this evidence pack (Data Gap DG002, High severity). Somatostatin is known generally as an endogenous regulatory peptide that inhibits pituitary hormone secretion (including growth hormone, TSH, and prolactin) and various gastrointestinal/pancreatic secretions via somatostatin receptors (SSTR1–5), but the specific original indication this candidate was evaluated against is not recorded in the source data.

The literature retrieved for the amenorrhea prediction is almost entirely composed of case reports and reviews describing **GH- or ACTH-secreting pituitary adenomas** (acromegaly, Cushing's disease, prolactinomas, McCune-Albright syndrome) in which secondary amenorrhea is a *downstream clinical consequence* of the tumor — typically via hyperprolactinemia or disruption of the hypothalamic-pituitary-gonadal (HPO) axis by mass effect or hormone excess. Somatostatin (and its analogues) are used in that clinical context to suppress the *causal* hormone-secreting tumor, not to act directly on the reproductive axis.

Because none of the retrieved evidence tests somatostatin as a treatment for amenorrhea itself, this prediction most likely reflects a **strong co-occurrence signal** in the knowledge graph (both concepts frequently appear together in pituitary-adenoma literature) rather than a genuine, direct pharmacological mechanism. This is consistent with the evidence-pack's own rationale, which explicitly states there is no direct action on the HPO axis and no trial has tested this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28170483](https://pubmed.ncbi.nlm.nih.gov/28170483/) | 2017 | Review | JAMA | General review of pituitary adenoma diagnosis and treatment; hormone hypersecretion and mass effects discussed. |
| [17644863](https://pubmed.ncbi.nlm.nih.gov/17644863/) | 2002 | Review | Eating and Weight Disorders | GH/IGF-I axis abnormalities, including amenorrhea, in anorexia nervosa and malnutrition states. |
| [15578985](https://pubmed.ncbi.nlm.nih.gov/15578985/) | 2004 | Review | Curr Drug Targets Immune Endocr Metab Disord | Review of Cushing's syndrome treatment approaches; amenorrhea listed as a clinical feature of cortisol excess. |
| [34158336](https://pubmed.ncbi.nlm.nih.gov/34158336/) | 2021 | Case Report | BMJ Case Reports | Adolescent with secondary amenorrhea from pituitary macroadenoma, later diagnosed with ACTH-dependent Cushing's disease. |
| [24683483](https://pubmed.ncbi.nlm.nih.gov/24683483/) | 2014 | Case Report | Endocrinol Diabetes Metab Case Rep | GH-secreting macroadenoma with secondary amenorrhea and acromegalic features; surgical management described. |
| [41687635](https://pubmed.ncbi.nlm.nih.gov/41687635/) | 2025 | Case Report | Georgian Medical News | Delayed diagnosis of acromegaly (somatoprolactinoma) presenting initially with amenorrhea. |
| [21814887](https://pubmed.ncbi.nlm.nih.gov/21814887/) | 2012 | Case Report | Pituitary | MEN1A patient presenting with amenorrhea and galactorrhea due to prolactin-secreting tumor. |
| [2922994](https://pubmed.ncbi.nlm.nih.gov/2922994/) | 1989 | Case Series | Acta Neuropathologica | Immunocytochemistry of 4 mixed pituitary adenomas, one associated with amenorrhea-galactorrhea syndrome. |
| [15765032](https://pubmed.ncbi.nlm.nih.gov/15765032/) | 2004 | Review | Minerva Endocrinologica | Overview of pituitary tumor hormone hypersecretion syndromes, including prolactin-driven amenorrhea-galactorrhea. |
| [6277529](https://pubmed.ncbi.nlm.nih.gov/6277529/) | 1981 | Review | Clinical Biochemistry | Historical review of anterior pituitary hormone control mechanisms. |

---

## Singapore Market Information

No market authorization records are available. Somatostatin currently has **0 registered licenses** and is **not marketed** in Singapore.

---

## Safety Considerations

Please refer to the package insert for safety information. (All safety fields — key warnings, contraindications, and drug-drug interactions — are unavailable in the current data source; TFDA/HSA labeling data has not yet been retrieved, flagged as a Blocking data gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between somatostatin and amenorrhea is indirect — all retrieved literature describes amenorrhea as a *symptom* of pituitary tumors that somatostatin analogues treat, not evidence that somatostatin corrects amenorrhea directly. With no clinical trials, evidence level capped at L4, and a Blocking-severity gap in basic safety/labeling data, this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- Original approved indication and combination/class context for somatostatin (currently undocumented in evidence pack)
- Mechanism-of-action data from DrugBank (DG002)
- TFDA/HSA package insert warnings and contraindications (DG001, Blocking)
- A study or trial directly evaluating somatostatin/analogues on the HPO axis or menstrual function, rather than on the underlying pituitary tumor

**Note:** Among the other candidates in this evidence pack, **multiple endocrine neoplasia** (rank 5, evidence level L2, "Proceed with Guardrails") is substantially better supported — multiple completed Phase 2/3 trials show somatostatin analogues (octreotide, lanreotide) are standard-of-care for MEN-associated functional neuroendocrine tumors. That candidate may warrant its own dedicated evaluation report rather than being assessed under the amenorrhea signal analyzed above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

