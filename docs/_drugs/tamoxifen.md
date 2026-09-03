---
layout: default
title: Tamoxifen
parent: 僅模型預測 (L5)
nav_order: 944
evidence_level: L5
indication_count: 10
---

# Tamoxifen
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

# Tamoxifen: From Breast Cancer to Mammary Paget Disease

## One-Sentence Summary

Tamoxifen is a selective estrogen receptor modulator (SERM) with a long-established role in treating estrogen receptor (ER)-positive breast cancer.
The TxGNN model predicts it may also be effective for **Mammary Paget Disease**,
with **1 clinical trial** and **13 relevant publications** currently identified, though no trial has directly tested tamoxifen's efficacy against Paget disease as a primary endpoint.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Breast Cancer (ER-positive) — inferred from surrounding trial evidence; not present in the structured regulatory dataset for this drug |
| Predicted New Indication | Mammary Paget Disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data for tamoxifen is not available in the current evidence pack. Based on the surrounding trial and literature context, however, tamoxifen is consistently characterized as a **Selective Estrogen Receptor Modulator (SERM)** that competitively blocks estrogen-driven proliferation signaling in ER-positive breast tissue — the mechanism underlying its established role in breast cancer treatment.

Mammary (nipple) Paget disease is frequently associated with an underlying ER-positive ductal carcinoma in situ (DCIS) or invasive ductal carcinoma beneath the epidermal lesion. Because the two conditions share overlapping ER-positive pathology within the same breast tissue compartment, tamoxifen's anti-estrogenic mechanism provides a plausible, indirect therapeutic rationale for Paget disease when hormone-receptor-positive disease is present.

That said, the mechanistic link remains theoretical: the evidence identified centers on case reports and a single Phase 3 trial (NCT00002920) that addresses a **safety monitoring** question (endometrial protection during tamoxifen therapy) in a population that happens to include Paget disease patients, rather than a trial testing tamoxifen's efficacy against Paget disease itself. No prospective study has been designed with Paget disease as the primary treatment target.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002920](https://clinicaltrials.gov/study/NCT00002920) | Phase 3 | Completed | 313 | Randomized comparison of medroxyprogesterone acetate vs. observation to prevent endometrial pathology in postmenopausal breast cancer patients (including Paget's disease of the nipple) on tamoxifen. This is a safety-monitoring trial, not a Paget disease efficacy trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34463889](https://pubmed.ncbi.nlm.nih.gov/34463889/) | 2022 | Case Report | Investigational New Drugs | Successful treatment of hormone receptor-positive metastatic extramammary Paget disease with tamoxifen |
| [14965622](https://pubmed.ncbi.nlm.nih.gov/14965622/) | 2001 | Case Report | Breast (Edinburgh) | Extensive, long-concealed case of nipple Paget disease; response achieved with tamoxifen after radiotherapy |
| [25759627](https://pubmed.ncbi.nlm.nih.gov/25759627/) | 2014 | Meta-Analysis/Cohort | Breast Care (Basel) | Meta-analysis of local recurrence after mastectomy vs. breast-conserving surgery for Paget's disease |
| [1648987](https://pubmed.ncbi.nlm.nih.gov/1648987/) | 1991 | Review/Case Series | British Journal of Surgery | 48-patient series of nipple Paget disease; treatments included mastectomy, cone excision, and tamoxifen |
| [8955252](https://pubmed.ncbi.nlm.nih.gov/8955252/) | 1996 | Case Series | The American Surgeon | Review of 32 world-literature cases of male breast Paget disease |
| [29694313](https://pubmed.ncbi.nlm.nih.gov/29694313/) | 2018 | Case Report | Il Giornale di Chirurgia | Male nipple Paget disease; notes absence of standard treatment procedures/guidelines |
| [12924421](https://pubmed.ncbi.nlm.nih.gov/12924421/) | 2003 | Case Report | Surgery Today | Synchronous bilateral breast cancer with Paget's disease and invasive ductal carcinoma |
| [19112575](https://pubmed.ncbi.nlm.nih.gov/19112575/) | 2009 | Case Report | Archives of Gynecology and Obstetrics | Sequential vulvar and breast Paget's disease with underlying adenocarcinoma |
| [17319355](https://pubmed.ncbi.nlm.nih.gov/17319355/) | 2006 | Case Series | Nigerian Journal of Clinical Practice | 8-patient case series of nipple-areola Paget disease from a Nigerian teaching hospital |
| [16277886](https://pubmed.ncbi.nlm.nih.gov/16277886/) | 2005 | Cohort | Clinical Breast Cancer | Paget's disease of the nipple as local recurrence after breast-conserving therapy |

---

## Singapore Market Information

No product registrations were found for tamoxifen in the current dataset (0 licenses, market status: Not Marketed). Registration status should be confirmed directly with the Singapore Health Sciences Authority (HSA) before proceeding.

---

## Safety Considerations

Please refer to the package insert for safety information. Structured safety data (key warnings, contraindications, drug–drug interactions) was not available in the current evidence pack for this candidate, and retrieval of the official product label is a **blocking** data gap identified in this evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between tamoxifen's SERM activity and ER-positive Paget disease is biologically plausible, but current evidence is limited to case reports/case series and one Phase 3 trial that addresses endometrial safety monitoring rather than Paget disease efficacy — no prospective trial has tested tamoxifen against Paget disease as a primary endpoint (Evidence Level L4). In addition, the absence of official safety labeling data is a blocking gap that prevents completion of the initial safety screening (S1) stage.

**To proceed, the following is needed:**
- Official product label / package insert (warnings, contraindications, DDI) from the relevant regulatory authority
- Confirmed drug mechanism-of-action documentation (e.g., DrugBank API)
- A prospective or retrospective study specifically evaluating tamoxifen efficacy in ER-positive mammary Paget disease
- Confirmation of Singapore/regional market and registration status for tamoxifen products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

