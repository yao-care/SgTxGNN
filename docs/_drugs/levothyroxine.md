---
layout: default
title: Levothyroxine
parent: 僅模型預測 (L5)
nav_order: 593
evidence_level: L5
indication_count: 10
---

# Levothyroxine
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

Using the evidence pack, I'll follow the v5 report template exactly — pulling all figures directly from the JSON (no invented data), and explicitly flagging where fields are genuinely empty (original indication, Singapore licensing, MOA) rather than fabricating them.

# Levothyroxine: From Thyroid Hormone Replacement to Endemic Goiter

## One-Sentence Summary

Levothyroxine (DrugBank DB00451) is a synthetic thyroid hormone (T4); this Evidence Pack does not contain a specific approved original-indication text (no Singapore/Taiwan licenses on file), so it is characterized here only at the drug-class level.
The TxGNN model's top-ranked prediction is that levothyroxine may be effective for **Endemic Goiter**, with the pipeline currently surfacing **1 clinical trial** and **20 publications** related to this pairing (10 of the most relevant are summarized below).
Because the single retrieved trial tests an unrelated herbal extract rather than levothyroxine itself, the clinical-trial support for this specific indication is weak; the literature — including one tier-1 levothyroxine intervention cohort — carries most of the evidentiary weight.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — `taiwan_regulatory.licenses` is empty and `drug.original_indications` is empty in this Evidence Pack |
| Predicted New Indication | Endemic Goiter |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for levothyroxine is not available in this Evidence Pack (flagged as data gap DG002, High severity). Based on what is known, levothyroxine is a synthetic form of thyroxine (T4), and its pharmacological action is described consistently across the individual repurposing rationales attached to this candidate set: iodine deficiency drives compensatory pituitary TSH secretion, which in turn drives thyroid follicular hyperplasia and goiter formation. Exogenous levothyroxine raises circulating T4/T3, suppresses TSH via negative feedback on the pituitary, and thereby removes the growth stimulus behind goiter enlargement.

Endemic goiter is, by definition, the iodine-deficiency-driven form of this same TSH-mediated enlargement process, so the mechanistic link is direct rather than speculative. That said, the Evidence Pack's own rationale for this candidate notes an important caveat: modern first-line management of endemic goiter is iodine repletion (dietary/iodized salt/iodized oil), with levothyroxine reserved mainly for patients who have progressed to confirmed hypothyroidism rather than as a universal first-line agent.

It is also worth noting that within this same prediction set, two closely related indications — **nodular goiter** (rank 3) and **nontoxic goiter** (rank 6) — carry substantially stronger evidence (Evidence Level L1, Decision Stage S3, including a 1,024-patient Phase 4 placebo-controlled RCT, NCT00277589). These findings reinforce the biological plausibility of TSH-suppression therapy across the goiter disease family and provide indirect support for the endemic goiter hypothesis even though the direct trial evidence for endemic goiter itself is thin.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04482907](https://clinicaltrials.gov/study/NCT04482907) | N/A | Completed | 68 | Randomized placebo-controlled trial of *Anethum graveolens* (dill) extract in thyroiditis/nodular goiter patients, evaluating hormone levels, inflammatory markers, and ultrasound-measured nodule size over 90 days. **Note:** the intervention tested is dill extract, not levothyroxine — this trial only overlaps on disease population (relevance grade C in the pack) and does not directly support a levothyroxine–endemic goiter link. |

No clinical trial in the pack directly tests levothyroxine in an endemic-goiter population; the strongest direct levothyroxine trial evidence in this data set instead sits under the related nodular/nontoxic goiter indications (e.g., NCT00277589, Phase 4, n=1024).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24393641](https://pubmed.ncbi.nlm.nih.gov/24393641/) | 1998 | Cohort/Intervention | Asia Pacific J Clin Nutr | Longitudinal study giving 100 µg/day levothyroxine to Indigenous residents (Aborigines) of an iodine-deficient endemic-goitre area in Malaysia, followed for 1.5 years (311 subjects at baseline, 184 by final follow-up). |
| [3278876](https://pubmed.ncbi.nlm.nih.gov/3278876/) | 1988 | Multicenter clinical study | Dtsch Med Wochenschr | 74 patients with diffuse endemic goiter randomized to 150 µg levothyroxine alone vs. 100 µg levothyroxine + 130.8 µg potassium iodide for 6 months, followed by iodide prophylaxis; compared goiter reduction between regimens. |
| [25629792](https://pubmed.ncbi.nlm.nih.gov/25629792/) | 2015 | RCT/Cohort | Curr Med Res Opin | 460 pregnant women across non-goiter, iodine-deficient endemic, and iodine-supplemented endemic-area groups; examined maternal/neonatal thyroid function and birth outcomes. |
| [8121602](https://pubmed.ncbi.nlm.nih.gov/8121602/) | 1993 | Case series | Minerva Ginecol | 38 pregnant women with endemic nodular goiter; 10.5% received L-thyroxine (50–100 µg/day) during pregnancy — goiter remained asymptomatic in 97.4% of cases. |
| [4312017](https://pubmed.ncbi.nlm.nih.gov/4312017/) | 1969 | Field trial (iodized oil) | Am J Clin Nutr | Prophylaxis and treatment of endemic goiter with iodized oil in rural Ecuador and Peru. |
| [2997259](https://pubmed.ncbi.nlm.nih.gov/2997259/) | 1985 | Field trial | J Clin Endocrinol Metab | Oral/IM iodized oil given to Sudanese schoolchildren reduced goiter prevalence from 67% to 36% (oral) and 42% (IM) over one year. |
| [3090091](https://pubmed.ncbi.nlm.nih.gov/3090091/) | 1986 | Cohort | J Clin Endocrinol Metab | Thyroid function survey (n=1218) in an Italian endemic-goiter area with moderate iodine deficiency (65% goiter prevalence); characterized TSH/TRH response. |
| [263304](https://pubmed.ncbi.nlm.nih.gov/263304/) | 1978 | Cohort | J Clin Endocrinol Metab | Maternal/neonatal thyroid function study in severe endemic goiter (Zaïre); iodized-oil-treated mothers showed better neonatal thyroid status than untreated mothers. |
| [2031356](https://pubmed.ncbi.nlm.nih.gov/2031356/) | 1991 | Review | World J Surg | Overview establishing iodine deficiency as the primary cause of endemic goiter and the central role of iodine prophylaxis. |
| [6304776](https://pubmed.ncbi.nlm.nih.gov/6304776/) | 1983 | Review/Basic research | Prog Clin Biol Res | TSH secretion correlates inversely with iodine intake and serum T4 in endemic-goiter/cretinism populations — mechanistic support for TSH-suppression therapy. |

(10 of 20 pack literature entries shown, prioritized by direct levothyroxine relevance and study tier; the remaining 10 are lower-tier epidemiological/case reports on endemic goiter generally.)

---

## Singapore Market Information

Levothyroxine currently has **no marketing authorization on record** in this Evidence Pack — `taiwan_regulatory.market_status` is "未上市" (Not Marketed) with `total_licenses = 0` and an empty license list. No product/dosage-form/indication table can be generated from this data.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and DDI fields in this Evidence Pack are all unpopulated; the DDI query itself returned `not_found`. TFDA/HSA label warnings and contraindications are flagged as a Blocking data gap (DG001) and must be sourced before this candidate can pass an S1 safety pre-screen.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The mechanistic story is sound and well-supported at the goiter-disease-family level (nodular/nontoxic goiter carry L1/S3 evidence including a large Phase 4 RCT), but the endemic-goiter-specific evidence is currently Level L2 (Decision Stage S2): no trial directly tests levothyroxine in endemic goiter, and the strongest direct literature support is a single tier-1 supplementation cohort (PMID 24393641) plus a multicenter levothyroxine+iodide study (PMID 3278876) — supportive but not definitive, and dated relative to current iodine-repletion-first practice.

**To proceed, the following is needed:**
- TFDA/HSA product label (warnings, contraindications) — currently a Blocking data gap (DG001)
- Formal DrugBank/pharmacology MOA text — currently a High-severity data gap (DG002)
- Confirmation of Singapore/regional registration status, since the drug is currently marked as not marketed with zero licenses
- A drug-interaction (DDI) query re-run, since the current query returned no results
- Consideration of whether "nodular goiter" and "nontoxic goiter" (both L1/S3 in this same prediction set) should be prioritized ahead of endemic goiter given their stronger direct trial evidence

---
*This analysis is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

