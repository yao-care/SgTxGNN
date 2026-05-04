---
layout: default
title: Anastrozole
parent: 僅模型預測 (L5)
nav_order: 100
evidence_level: L5
indication_count: 10
---

# Anastrozole
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

# Anastrozole: From Postmenopausal ER-Positive Breast Cancer to Female Breast Carcinoma

## One-Sentence Summary

Anastrozole is a third-generation non-steroidal aromatase inhibitor, globally established as a standard of care for hormone receptor-positive breast cancer in postmenopausal women, but currently not registered with Singapore's HSA.
The TxGNN model predicts it would be effective for **Female Breast Carcinoma**, supported by over **40 clinical trials** (including multiple completed Phase 3 RCTs) and **20 publications**.
Landmark studies such as the ATAC trial (n=9,358) and IBIS-II trial (n=3,864) firmly establish Level 1 evidence, making the primary gap regulatory rather than scientific.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Adjuvant treatment for ER-positive / HR-positive breast cancer in postmenopausal women (globally established; no Singapore HSA registration on record) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal MOA data is not captured in the current evidence pack. However, based on extensive published literature and the mechanistic rationale available, Anastrozole is a highly selective competitive inhibitor of CYP19A1 (aromatase), the enzyme that converts androgens (androstenedione, testosterone) into estrogens (estrone, estradiol). By eliminating the primary source of systemic estrogen in postmenopausal women, Anastrozole directly suppresses estrogen-driven proliferation in ER-positive / PR-positive breast tumors. This is mechanistically distinct from tamoxifen, which competes at the receptor level — Anastrozole acts upstream by removing the ligand entirely. Ki-67 reductions consistently observed in preoperative window-of-opportunity studies confirm on-target pharmacodynamic activity.

The link between this mechanism and female breast carcinoma is direct and well-characterized. In postmenopausal women, peripheral adipose tissue aromatase becomes the dominant estrogen source after ovarian shutdown. Tumors that express estrogen receptors are thereby dependent on this substrate supply. Blocking aromatase reduces both tumor estrogen signaling and the proliferative stimulus that drives ER+ breast cancer growth and recurrence. The ATAC trial demonstrated significantly prolonged disease-free survival versus tamoxifen after five years of adjuvant use, and IBIS-II showed a 49% reduction in breast cancer incidence in high-risk women over a 10-year follow-up.

The TxGNN prediction at 99.68% is therefore not a novel finding but an independent computational confirmation of a well-established clinical relationship. From a Singapore-market perspective, the absence of HSA registration for a drug with this evidence base represents an access gap. The prediction supports prioritizing this drug for registration review.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00849030](https://clinicaltrials.gov/study/NCT00849030) | Phase 3 | Completed | 9,358 | ATAC trial: Anastrozole vs tamoxifen vs combination as 5-year adjuvant therapy; anastrozole significantly prolonged disease-free survival with a better tolerability profile |
| [NCT00784862](https://clinicaltrials.gov/study/NCT00784862) | Phase 3 | Completed | 9,358 | ATAC pharmacokinetics sub-study: assessed interaction between anastrozole and tamoxifen; tamoxifen reduced anastrozole plasma levels, supporting use as monotherapy |
| [NCT00078832](https://clinicaltrials.gov/study/NCT00078832) | Phase 3 | Completed | 3,864 | IBIS-II: Anastrozole vs placebo for chemoprevention in high-risk postmenopausal women; anastrozole reduced breast cancer incidence over a decade of follow-up |
| [NCT00301457](https://clinicaltrials.gov/study/NCT00301457) | Phase 3 | Completed | 1,914 | Compared 6 vs 3 years of adjuvant anastrozole following 2–3 years of tamoxifen; evaluated optimal duration for extended endocrine therapy |
| [NCT00688194](https://clinicaltrials.gov/study/NCT00688194) | Phase 3 | Unknown | 396 | Overcoming endocrine resistance in metastatic breast cancer: factorial design comparing fulvestrant ± lapatinib ± aromatase inhibitor in AI-refractory disease |
| [NCT04568616](https://clinicaltrials.gov/study/NCT04568616) | Phase 2 | Active, not recruiting | 178 | NAOMI: neoadjuvant aromatase inhibitor in Stage I–III ER+/HER2– breast cancer; molecular biomarker analysis comparing baseline biopsy vs surgical specimen |
| [NCT00629616](https://clinicaltrials.gov/study/NCT00629616) | Phase 2 | Completed | 116 | Multicenter RCT: anastrozole vs fulvestrant in neoadjuvant setting; evaluated hormone sensitivity profiling and clinical response in postmenopausal women |
| [NCT04023292](https://clinicaltrials.gov/study/NCT04023292) | Phase 2 | Unknown | 185 | Compared 2-week vs 4-week preoperative endocrine therapy in luminal breast cancer using Ki-67 as primary biomarker; supports short-term neoadjuvant strategy |
| [NCT01016665](https://clinicaltrials.gov/study/NCT01016665) | N/A | Completed | 71 | Prospective placebo-controlled study: anastrozole reduced Ki-67 proliferation index and progesterone receptor expression in short-term preoperative treatment |
| [NCT00186121](https://clinicaltrials.gov/study/NCT00186121) | Phase 2 | Completed | 35 | Anastrozole + goserelin (Zoladex) in ER-positive metastatic breast cancer in premenopausal women; evaluated AI combined with ovarian suppression |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [31839281](https://pubmed.ncbi.nlm.nih.gov/31839281/) | 2020 | Phase 3 RCT (IBIS-II long-term) | Lancet | Anastrozole reduced breast cancer incidence (invasive + DCIS) by 49% vs placebo at median 131-month follow-up in high-risk postmenopausal women |
| [15639680](https://pubmed.ncbi.nlm.nih.gov/15639680/) | 2005 | Phase 3 RCT (ATAC) | Lancet | After 5-year adjuvant treatment, anastrozole significantly prolonged disease-free survival vs tamoxifen (HR favoring anastrozole) with fewer thromboembolic and gynaecological events |
| [24716940](https://pubmed.ncbi.nlm.nih.gov/24716940/) | 2014 | Meta-analysis | Asian Pac J Cancer Prev | Pooled analysis of fulvestrant 250 mg vs anastrozole 1 mg in advanced breast cancer; anastrozole favored for time to progression in first-line postmenopausal settings |
| [20923259](https://pubmed.ncbi.nlm.nih.gov/20923259/) | 2010 | Drug Monograph | Expert Opin Drug Safety | Confirmed anastrozole superiority over tamoxifen across multiple adjuvant RCTs; reviewed safety profile including bone and cardiovascular considerations |
| [28614542](https://pubmed.ncbi.nlm.nih.gov/28614542/) | 2017 | Systematic Review | Rev Assoc Med Bras | Systematic review of anastrozole in chemoprevention and treatment; identified interindividual pharmacokinetic variability as a clinically relevant factor |
| [16034487](https://pubmed.ncbi.nlm.nih.gov/16034487/) | 2005 | Drug Review | Drugs Today | Reviewed CYP19A1 inhibition mechanism and major clinical trials; at time of publication, anastrozole was the only AI licensed for adjuvant use in ER+ early breast cancer |
| [16439860](https://pubmed.ncbi.nlm.nih.gov/16439860/) | 2006 | Narrative Review | Oncology | Evidence for anastrozole across the breast cancer continuum: second-line advanced, first-line advanced, early adjuvant, and at-risk prevention populations |
| [16761927](https://pubmed.ncbi.nlm.nih.gov/16761927/) | 2006 | Review | Expert Rev Anticancer Ther | Updated ATAC analysis; established anastrozole as a widely accepted alternative to tamoxifen for initial adjuvant therapy in postmenopausal HR+ breast cancer |
| [19445563](https://pubmed.ncbi.nlm.nih.gov/19445563/) | 2009 | Comparative Review | Expert Opin Pharmacother | Head-to-head comparison of anastrozole, letrozole, and exemestane in early breast cancer trials; all three AIs demonstrated superiority over tamoxifen |
| [14687437](https://pubmed.ncbi.nlm.nih.gov/14687437/) | 2003 | Review | Curr Med Res Opin | Overview of anastrozole clinical evidence through 2003: superior to megestrol acetate as second-line and to tamoxifen as first-line therapy in advanced disease |

---

## Singapore Market Information

Anastrozole currently has **no registered products** with the Health Sciences Authority (HSA) in Singapore. There are no authorization records, approved indications, or dosage form listings on file. This stands in contrast to its widely approved status in the US (FDA), Europe (EMA), Japan (PMDA), and Taiwan (TFDA).

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted endocrine therapy — non-steroidal aromatase inhibitor (not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Low — anastrozole does not cause clinically significant bone marrow suppression |
| Emetogenicity Classification | Minimal — nausea reported as mild and infrequent; not classified as emetogenic |
| Monitoring Items | Bone mineral density (DEXA scan at baseline and annually), lipid profile, liver function tests (periodic), musculoskeletal symptom assessment |
| Handling Protection | Standard oral oncology handling practices apply; dedicated cytotoxic chemotherapy handling protocols (closed-system transfer devices, dedicated PPE) are not required |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Anastrozole has Level 1 evidence for female breast carcinoma, anchored by at least three completed Phase 3 RCTs (ATAC, IBIS-II, and extended-duration studies) enrolling a combined total exceeding 14,000 participants, complemented by a meta-analysis and multiple systematic reviews. The drug is approved by every major regulatory authority globally. The absence of Singapore HSA registration is a market access gap, not a scientific one.

**To proceed, the following is needed:**
- Submit an HSA registration application via the well-established use (WEU) or abridged evaluation pathway, referencing existing FDA and EMA approvals
- Download and review the TFDA or FDA package insert PDF to populate the safety section (key warnings, contraindications, drug interactions) currently absent from this evidence pack
- Establish a local bone health monitoring protocol: baseline DEXA scan and annual review, with bisphosphonate co-prescription criteria defined
- Confirm drug interaction profile with tamoxifen (known PK antagonism) and CYP3A4-related comedications before clinical deployment
- Define patient eligibility criteria specific to the Singapore context: postmenopausal status verification method, mandatory ER/PR receptor testing, and HER2 status documentation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

