---
layout: default
title: Megestrol Acetate
parent: 僅模型預測 (L5)
nav_order: 636
evidence_level: L5
indication_count: 10
---

# Megestrol Acetate
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

# Megestrol Acetate: From Cancer-Related Anorexia-Cachexia to Uterine Corpus Endometrial Carcinoma

*Note: Singapore-specific approved-indication text is not available in this evidence pack (drug is not currently registered in Singapore). The original-indication description above reflects Megestrol acetate's globally established, well-documented uses (progestin hormonal therapy for advanced/recurrent breast and endometrial cancer, and cancer/AIDS-related anorexia-cachexia) rather than a locally sourced label.*

## One-Sentence Summary

> Megestrol acetate is a synthetic progestin historically used for cancer-related anorexia-cachexia and as palliative hormonal therapy in advanced breast/endometrial cancer.
> The TxGNN model predicts it may be effective for **Uterine Corpus Endometrial Carcinoma** — specifically in early-stage/fertility-sparing settings —
> with **3 clinical trials** currently identified, one of which is a completed Phase 2 RCT that returned a **negative efficacy result with an increased blood-clot safety signal**, so the evidence should be read as directional, not confirmatory.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this evidence pack (drug not registered in Singapore); generally known as palliative hormonal therapy for breast/endometrial cancer and cancer-related anorexia-cachexia |
| Predicted New Indication | Uterine Corpus Endometrial Carcinoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Megestrol acetate is not available in this evidence pack (marked as a data gap). Based on the mechanistic rationale supplied alongside the TxGNN prediction, Megestrol acetate acts as a progesterone receptor (PR) agonist. Endometrial adenocarcinoma — particularly the endometrioid histological subtype — is frequently PR-positive, and progestins are known to induce tumour cell differentiation and counteract oestrogen-driven proliferation. This is the classical basis for progestin therapy in gynaecologic oncology, most notably in fertility-sparing treatment of early-stage endometrial cancer.

Because Megestrol acetate is already used in hormone-responsive gynaecologic malignancies, extending its use to fertility-sparing management of uterine corpus endometrial carcinoma is mechanistically plausible and consistent with existing clinical practice patterns in this disease area.

However, the strength of this rationale should be weighed against the actual trial evidence below: the one completed, directly relevant Phase 2 RCT (NCT00729586) did **not** show a benefit from adding Megestrol acetate to therapy and instead flagged a significant increase in venous thromboembolism (VTE) risk. The mechanistic plausibility therefore supports **continued investigation**, not an assumption of proven efficacy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Phase 2 | Completed | 73 | Temsirolimus ± Megestrol acetate + Tamoxifen in advanced/recurrent endometrial carcinoma. Verified result: combination arm was **not superior** to control and showed a **significantly increased VTE risk**, leading to early closure of that arm — this is a safety warning signal, not supportive efficacy evidence. |
| [NCT00503581](https://clinicaltrials.gov/study/NCT00503581) | Phase 2 | Terminated | 9 | Continuous vs. sequential progestin (megestrol) therapy for endometrial intraepithelial neoplasia/atypical endometrial hyperplasia. Directly drug-relevant, but terminated early with only 9 participants — underpowered; directional signal only. |
| [NCT04046185](https://clinicaltrials.gov/study/NCT04046185) | Early Phase 1 | Unknown | 60 | PD-1 inhibitor combined with progesterone (not confirmed to be Megestrol specifically) vs. progesterone alone, in fertility-sparing treatment of early-stage endometrial cancer. Exploratory combination study; status unknown. |

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

Megestrol acetate currently has no marketing authorization recorded in Singapore (market status: Not Marketed; 0 registrations on file).

## Safety Considerations

Please refer to the package insert for safety information.

*Additional note from clinical trial evidence: the completed Phase 2 trial (NCT00729586) identified a significantly increased risk of venous thromboembolism when Megestrol acetate was combined with temsirolimus/tamoxifen. This should be treated as an active safety signal for any further clinical development in this indication, even though it falls outside the formal `safety.key_warnings` field (which has no data on file).*

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The mechanistic basis (PR agonism in a frequently PR-positive tumour type) is sound and consistent with established gynaecologic-oncology practice, and one completed Phase 2 RCT directly tested the drug in this population — meeting the L2 evidence bar. However, that same trial returned a negative efficacy result and a significant VTE safety signal, so further development must proceed cautiously with explicit safety monitoring rather than on an assumption of efficacy.

**To proceed, the following is needed:**
- Formal mechanism of action (MOA) documentation from DrugBank (currently a blocking data gap, DG001/DG002)
- Singapore/local label warnings and contraindications (currently a blocking data gap, DG001)
- A dedicated thromboembolism risk-monitoring protocol before any further combination-therapy investigation
- Clarification of whether NCT04046185's "progesterone" arm specifically uses Megestrol acetate
- A properly powered follow-up study, given NCT00503581 was terminated with only 9 participants
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

