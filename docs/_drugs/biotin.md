---
layout: default
title: Biotin
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
---

# Biotin
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

# Biotin: From Biotin Deficiency to Dyspepsia

## One-Sentence Summary

Biotin (vitamin B7) is an essential water-soluble vitamin that functions as a cofactor for five critical carboxylase enzymes, clinically used in the treatment of biotin deficiency states and related metabolic disorders.
The TxGNN model ranks **Dyspepsia (functional indigestion)** as the top new indication by prediction score,
supported by **2 clinical trials** and **7 publications** — though the evidence is largely indirect and mechanistically inferential.

> **Note for reviewers:** By evidence quality, **Biotin Metabolic Disease** (Rank 8, **L1** evidence, 42 clinical trials, 20 publications) and **Vitamin Deficiency Disorder** (Rank 7, **L2** evidence, 10 clinical trials) are substantially better supported. Dyspepsia leads only by TxGNN prediction score (99.43%), not by clinical evidence strength.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Biotin deficiency / nutritional supplementation — no Singapore regulatory registration on file |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory data set. Based on established biochemical knowledge documented across the evidence base, Biotin functions as a prosthetic group covalently bound to five essential carboxylases: acetyl-CoA carboxylase 1 and 2 (fatty acid synthesis), pyruvate carboxylase (gluconeogenesis and TCA cycle anaplerosis), propionyl-CoA carboxylase (odd-chain fatty acid and branched-chain amino acid catabolism), and methylcrotonyl-CoA carboxylase (leucine catabolism). These enzymes are indispensable for the energy metabolism and proliferative capacity of gastrointestinal mucosal epithelium.

The theoretical link between Biotin and dyspepsia operates through two indirect pathways. First, biotin-dependent fatty acid synthesis carboxylases support intestinal epithelial cell renewal; their impairment under deficiency could compromise the gastric mucosal barrier and predispose to dyspeptic symptoms. Second, recent translational research (PMID 35017197) demonstrates that impaired gut microbial biotin metabolism is associated with severe metabolic dysregulation, suggesting Biotin availability may modulate the gut microbiome composition relevant to upper GI function. Supportive but non-specific evidence comes from PMID 25384804, which reported that a multi-component food supplement containing Biotin — alongside sodium alginate, calcium carbonate, pineapple, papaya, ginger, and fennel — improved functional dyspepsia quality of life after H. pylori eradication; however, Biotin's independent contribution cannot be isolated from this multi-ingredient design.

The mechanistic connection remains largely speculative. Dyspepsia is a multifactorial condition more directly driven by gastric acid secretion, motility dysfunction, and visceral hypersensitivity rather than carboxylase insufficiency. The TxGNN prediction at Rank 1 most likely reflects knowledge graph network topology connecting biotin metabolism nodes to gastrointestinal disease nodes rather than an established therapeutic pathway.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Pharmacokinetics of transdermal vitamin absorption (including Biotin) in post-bariatric surgery patients; primary endpoint is serum micronutrient levels, not dyspepsia — population and endpoints are not directly relevant |

> NCT05389813 (oxycodone vs. pregabalin for postoperative pain) was excluded as confirmed data noise — no connection to Biotin or dyspepsia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [25384804](https://pubmed.ncbi.nlm.nih.gov/25384804/) | 2014 | Clinical interventional (open-label multicenter) | Minerva Gastroenterol Dietol | Multi-component supplement including Biotin improved quality of life in functional dyspepsia after H. pylori eradication; Biotin's individual contribution cannot be isolated from the formula |
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Case report | J Dermatol | 5-month-old infant with neonatal dyspepsia fed amino acid formula developed classic Biotin deficiency — suggests formula-fed GI patients are at depletion risk; not a treatment efficacy study |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Review/Clinical | Exp Clin Gastroenterology | Biotin-containing B-vitamin complex (Stimbifid) corrected intestinal microbiota dysbiosis in bronchopulmonary patients on antibiotics; indirect GI microbiome relevance only |

---

## Singapore Market Information

Biotin (DB00121) currently has **no registered pharmaceutical products in Singapore**. No authorization numbers, brand names, dosage forms, or approved indications are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical safety alert — Immunoassay interference:** High-dose Biotin supplementation (>5 mg/day, particularly formulations such as MD1003 at 100–300 mg/day) is known to interfere with electrochemiluminescence immunoassays (ECLIA). This can produce **falsely abnormal results** for thyroid function tests (TSH, FT4, FT3), cardiac biomarkers (Troponin I/T), oncology markers (PSA, AFP, CEA), and pregnancy tests (β-HCG). Clinicians should routinely ask patients about Biotin supplementation before ordering these tests, and patients should be advised to discontinue Biotin 48–72 hours prior to laboratory sampling to avoid diagnostic errors.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial has directly tested Biotin monotherapy for dyspepsia, and the only supportive study (PMID 25384804) used a multi-ingredient supplement that prevents attribution of benefit to Biotin. The mechanistic connection is indirect and L4 evidence is insufficient to justify advancing this indication.

**To proceed, the following is needed:**
- Survey Biotin deficiency prevalence in functional dyspepsia patient populations as a prerequisite feasibility study
- Design a placebo-controlled pilot trial of Biotin supplementation in confirmed-deficient functional dyspepsia patients
- Retrieve full MOA documentation from DrugBank (Data Gap DG002) to characterize the mechanism properly
- Obtain Singapore-approved package insert warnings and contraindications (Data Gap DG001) before safety assessment can proceed
- **Strategic prioritization:** Research resources are more efficiently directed toward **Biotin Metabolic Disease** (Rank 8, L1 evidence, 42 clinical trials — including Phase 2 RCT NCT03114215 and the direct Biotinidase deficiency study NCT03269045) and **Vitamin Deficiency Disorder** (Rank 7, L2 evidence, 10 clinical trials), where Biotin's therapeutic role is mechanistically direct and clinically established
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

