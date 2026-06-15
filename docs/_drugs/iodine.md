---
layout: default
title: Iodine
parent: 僅模型預測 (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
---

# Iodine
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

# Iodine: From Antiseptic Use to Sjogren Syndrome

## One-Sentence Summary

Iodine (DrugBank ID: DB05382) is an essential element with established antiseptic and antimicrobial properties, currently not registered as a pharmaceutical product in Singapore and carrying no formally approved therapeutic indications on file.
The TxGNN model predicts it may be effective for **Sjogren Syndrome**, likely on the basis of the Sodium-Iodide Symporter (NIS) co-expressed in salivary glands and thyroid tissue.
However, this prediction is supported by **0 clinical trials** and **20 publications** — all of which describe iodine as a contributing factor to salivary and lacrimal dysfunction rather than as a therapeutic agent for Sjogren Syndrome.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indications on file |
| Predicted New Indication | Sjogren Syndrome |
| TxGNN Prediction Score | 94.09% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iodine (DB05382) is an essential element whose pharmacological roles span antisepsis, thyroid hormone biosynthesis, and — in radioactive form (I-131) — targeted thyroid ablation. The TxGNN prediction most likely derives from the **Sodium-Iodide Symporter (NIS)**, a membrane transporter co-expressed in both thyroid follicular epithelium and the ductal epithelium of salivary glands. A 2025 computational immunology study (PMID 41516079) identified shared NIS epitopes capable of triggering autoreactive T- and B-cell responses in both Hashimoto's thyroiditis and Sjogren's Syndrome, pointing to a convergent molecular pathway between these two autoimmune conditions.

Despite this structurally plausible link, the causal direction in all available evidence runs counter to a therapeutic role for iodine. High-dose radioactive iodine therapy for thyroid cancer causes iatrogenic sicca syndrome — salivary and lacrimal gland dysfunction closely resembling Sjogren's Syndrome — as a well-documented adverse effect (PMID 11337569). Multiple cross-sectional studies confirm a high comorbidity rate between primary Sjogren's Syndrome and autoimmune thyroid disease (PMID 7485204, PMID 12035942), but this reflects shared immune dysregulation, not a therapeutic effect of iodine on Sjogren's pathology.

In summary, the existing literature falls into three non-therapeutic categories: (1) radioactive iodine as a trigger of iatrogenic salivary/lacrimal dysfunction; (2) radiolabeled iodine as a diagnostic imaging tracer for salivary gland scintigraphy; and (3) epidemiological studies on autoimmune thyroid–Sjogren comorbidity. No published study has tested iodine as a treatment intervention in Sjogren's Syndrome, and the mechanistic hypothesis remains entirely speculative. The high TxGNN score most plausibly reflects shared knowledge-graph topology rather than a validated therapeutic relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41516079](https://pubmed.ncbi.nlm.nih.gov/41516079/) | 2025 | Computational/Immunological | Int J Mol Sci | NIS epitopes computationally predicted to trigger autoimmune responses shared between Sjogren's Syndrome and Hashimoto's thyroiditis; provides the primary mechanistic hypothesis behind the TxGNN prediction |
| [35817018](https://pubmed.ncbi.nlm.nih.gov/35817018/) | 2023 | Case Series/Review | ORL J Oto-Rhino-Laryngol | Sialendoscopy for chronic sialadenitis caused by Sjogren's syndrome and RAI therapy; iodine appears as a disease trigger, not a treatment |
| [11337569](https://pubmed.ncbi.nlm.nih.gov/11337569/) | 2001 | Prospective Cohort | J Nucl Med | High-dose radioiodine therapy causes sicca syndrome (salivary and lacrimal dysfunction); up to 3-year follow-up confirms iodine as a causative agent |
| [24899999](https://pubmed.ncbi.nlm.nih.gov/24899999/) | 2011 | Diagnostic Study | Nucl Med Mol Imaging | Salivary gland scintigraphy with radiolabeled iodine used to compare gland dysfunction in SS patients vs post-RAI thyroid cancer patients; iodine as diagnostic tracer |
| [30344785](https://pubmed.ncbi.nlm.nih.gov/30344785/) | 2018 | Diagnostic Study | Nucl Med Mol Imaging | Quantitative SPECT/CT using Tc-99m pertechnetate to evaluate salivary gland dysfunction in Sjogren's Syndrome patients |
| [12035942](https://pubmed.ncbi.nlm.nih.gov/12035942/) | 2002 | Cross-sectional | J Endocrinol Invest | Thyroid hormone autoantibodies more prevalent in primary Sjogren's syndrome than in Hashimoto's thyroiditis or Graves' disease; documents immune overlap |
| [7485204](https://pubmed.ncbi.nlm.nih.gov/7485204/) | 1995 | Cross-sectional | Am J Med | Systematic evaluation of autoimmune thyroid disease prevalence and thyroid dysfunction in a primary Sjogren's syndrome cohort |
| [4951717](https://pubmed.ncbi.nlm.nih.gov/4951717/) | 1967 | Clinical Study | Ann Rheum Dis | Early measurement of salivary flow rates and iodide trapping capacity in SS patients; among the first data linking iodide handling to SS gland pathology |
| [4965427](https://pubmed.ncbi.nlm.nih.gov/4965427/) | 1967 | Clinical Study | Br J Ophthalmol | Early clinical documentation of the co-occurrence of Sjogren's syndrome and thyroid disease |
| [3261973](https://pubmed.ncbi.nlm.nih.gov/3261973/) | 1988 | Case Report | Arch Intern Med | Silent thyroiditis in a Sjogren's syndrome patient with thyrotoxicosis and depressed radioactive iodine uptake; antinuclear antibody changes documented |

---

## Singapore Market Information

Iodine (DB05382) is currently not registered as a pharmaceutical product in Singapore. No marketing authorizations or product licenses are on record. Any clinical use would require a new regulatory pathway from the ground up before the predicted indication could be pursued.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The entire body of available literature positions iodine as a causative agent of Sjogren's-like salivary and lacrimal dysfunction — not as a therapeutic intervention — and the mechanistic hypothesis connecting iodine to Sjogren's Syndrome treatment has not been tested in any clinical or preclinical setting.

**To proceed, the following is needed:**

- **Mechanistic clarification:** Establish whether iodine (at physiological or pharmacological doses, distinct from radioactive I-131) can modulate NIS-mediated autoimmune activity in salivary glands rather than damage gland epithelium
- **Preclinical studies:** In vitro and animal model experiments in Sjogren's-like models are required before any human study is warranted
- **Safety data acquisition:** TFDA package insert warnings and contraindications are currently unavailable and must be obtained (designated as a blocking data gap)
- **MOA data from DrugBank:** Formal mechanism of action documentation to confirm or refute the NIS hypothesis
- **Expert consultation:** Rheumatology and nuclear medicine input to assess whether any therapeutic dose window exists between iodine's known glandular toxicity and a hypothetical anti-autoimmune effect
- **Directionality review:** A formal knowledge-graph audit is recommended to flag this candidate as a potential false positive (iodine as pathogen, not therapeutic agent) before further resources are committed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

