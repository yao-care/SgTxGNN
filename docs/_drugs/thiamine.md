---
layout: default
title: Thiamine
parent: 僅模型預測 (L5)
nav_order: 971
evidence_level: L5
indication_count: 10
---

# Thiamine
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

# Thiamine: From Vitamin B1 Deficiency to Hyperthyroidism-Associated Cardiovascular Dysfunction

## One-Sentence Summary

> Thiamine (Vitamin B1) is a water-soluble nutrient essential as a metabolic cofactor, traditionally used for thiamine deficiency states (beriberi, Wernicke's encephalopathy); no formal Singapore-registered indication is on file for this drug.
> The TxGNN model predicts it may be effective for **Hyperthyroidism**-associated cardiovascular dysfunction,
> with **1 clinical trial** and **20 publications** currently supporting this direction, though the evidence is preliminary and largely historical/case-based.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — Thiamine has no registered Singapore license record; historically used for Vitamin B1 deficiency/nutritional supplementation |
| Predicted New Indication | Hyperthyroidism (associated cardiovascular dysfunction) |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

> Currently, detailed mechanism of action data is not available. Based on known information, Thiamine is a water-soluble B-vitamin that functions as an essential cofactor (thiamine pyrophosphate) for enzymes in carbohydrate and energy metabolism (e.g., pyruvate dehydrogenase, transketolase, α-ketoglutarate dehydrogenase). Its efficacy in correcting thiamine-deficiency states has been well established, and mechanistically it may be applicable to hyperthyroidism-associated cardiovascular dysfunction.

Hyperthyroidism/thyrotoxicosis is a hypermetabolic state that increases tissue thiamine turnover, which can produce a relative thiamine deficiency. This has been linked in the literature to high-output heart failure and Wernicke's encephalopathy-like presentations in thyrotoxic patients. Thiamine supplementation is therefore proposed to correct this metabolic gap and improve cardiovascular parameters (e.g., left ventricular function) in affected patients.

The rationale is biologically plausible and supported by historical basic-science and case-report literature, but current clinical evidence is limited to one small pilot trial (n=12) — insufficient to confirm efficacy at a confirmatory level.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02767245](https://clinicaltrials.gov/study/NCT02767245) | Phase NA | Completed | 12 | Pilot study in severe hyperthyroidism patients evaluating prevalence of thiamine deficiency and cardiovascular function improvement after thiamine supplementation; small sample size, hypothesis-generating only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32983708](https://pubmed.ncbi.nlm.nih.gov/32983708/) | 2020 | Case Report | Cureus | Wernicke's encephalopathy from thiamine deficiency associated with transient gestational hyperthyroidism and hyperemesis gravidarum. |
| [26567494](https://pubmed.ncbi.nlm.nih.gov/26567494/) | 2015 | Case Report | Crit Care Nurs Clin North Am | High-output heart failure caused by thyrotoxicosis and beriberi (thiamine deficiency), highlighting shared hemodynamic mechanism. |
| [18026802](https://pubmed.ncbi.nlm.nih.gov/18026802/) | 2008 | Case Report | J Gen Intern Med | Thyrotoxicosis-associated Wernicke's encephalopathy from thiamine deficiency. |
| [36176825](https://pubmed.ncbi.nlm.nih.gov/36176825/) | 2022 | Case Report | Cureus | Uncommon presentation of hyperthyroidism (post-methimazole) culminating in neurological consequences consistent with thiamine deficiency. |
| [25148818](https://pubmed.ncbi.nlm.nih.gov/25148818/) | 2014 | Case Report | Endocr Pract | Gestational thyrotoxicosis and hyperemesis gravidarum associated with Wernicke's encephalopathy. |
| [34017792](https://pubmed.ncbi.nlm.nih.gov/34017792/) | 2021 | Case Report | J Family Med Prim Care | Seizure as the presenting manifestation of Wernicke's encephalopathy induced by hyperemesis gravidarum with thyrotoxicosis. |
| [22436368](https://pubmed.ncbi.nlm.nih.gov/22436368/) | 2013 | Case Report | Neurologia (Barcelona) | Wernicke's encephalopathy secondary to hyperthyroidism and ingestion of thiaminase-rich products. |
| [13934469](https://pubmed.ncbi.nlm.nih.gov/13934469/) | 1963 | Animal Study | Ann Biochem Exp Med | Storage of tissue thiamine and its intestinal synthesis in hypo- and hyperthyroid rats. |
| [21064291](https://pubmed.ncbi.nlm.nih.gov/21064291/) | 1946 | Basic Science | Federation Proceedings | Effect of thiamine deficiency, quinidine, hyperthyroidism and hypothyroidism on ATP content/activity of rat heart muscle. |
| [32934066](https://pubmed.ncbi.nlm.nih.gov/32934066/) | 2020 | Case Report | Clin Med (Lond) | Wernicke's encephalopathy in a pregnant patient with hyperemesis gravidarum and thyrotoxicosis. |

---

## Singapore Market Information

Thiamine currently has no registered license record in Singapore (`market_status`: Not Marketed, `total_licenses`: 0). No product-level authorization data is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug-interaction data were flagged as blocking data gaps in this evidence pack and could not be summarized here.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Thiamine is not currently registered or marketed in Singapore, and critical safety data (warnings/contraindications) is a **blocking** data gap that prevents entry into S1 safety review. While the mechanistic link between hyperthyroidism-induced relative thiamine deficiency and cardiovascular dysfunction is biologically plausible and has decades of case-report support, clinical evidence for this specific repurposing is limited to a single small pilot trial (n=12) — Evidence Level L3, insufficient for a Go decision.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent product label data (key warnings, contraindications) — currently the blocking gap
- Detailed mechanism of action documentation (DrugBank query)
- A larger controlled trial confirming cardiovascular benefit of thiamine supplementation in hyperthyroid patients (current n=12 pilot is underpowered)
- Confirmation of Singapore regulatory/registration pathway before any repurposing pursuit

**For consideration:** among the 10 TxGNN-predicted indications reviewed, *pulmonary hypertension* (rank 5) has a more mature and mechanistically direct evidence base — thiamine-responsive pulmonary hypertension is a well-documented, causally established pediatric syndrome with a "Proceed with Guardrails" recommendation — and may warrant prioritization over hyperthyroidism if this candidate is advanced further.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

