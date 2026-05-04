---
layout: default
title: Goserelin
parent: 僅模型預測 (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
---

# Goserelin
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

# Goserelin: From Hormone-Sensitive Cancers to Amenorrhea

## One-Sentence Summary

Goserelin (Zoladex) is a synthetic GnRH agonist primarily used in hormone-sensitive cancers (breast cancer, prostate cancer) and gynaecological conditions such as endometriosis, achieving therapeutic effects through reversible suppression of the hypothalamic-pituitary-gonadal axis.
The TxGNN model predicts it may be effective for **Amenorrhea**, with **7 clinical trials** and **19 publications** currently supporting this direction.
Given the well-established pharmacological mechanism and multiple completed Phase 3 RCTs, evidence strength is rated **L1**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hormone-sensitive cancers and endometriosis (no Singapore registration data available) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal DrugBank MOA data is unavailable for this report. However, based on established pharmacology, Goserelin is a synthetic analogue of gonadotropin-releasing hormone (GnRH/LHRH). When administered continuously, it paradoxically down-regulates pituitary GnRH receptors, triggering a sharp decline in LH and FSH secretion. This cascade suppresses ovarian production of oestrogen and progesterone, resulting in endometrial atrophy and the induction of medical amenorrhoea. This is a direct, well-characterised pharmacological mechanism — not an incidental side effect.

Amenorrhoea is therefore an *intended and expected endpoint* of GnRH agonist therapy in multiple clinical scenarios. Goserelin is routinely deployed to induce reversible amenorrhoea for ovarian protection during chemotherapy (reducing premature ovarian insufficiency), for ovarian suppression as adjuvant therapy in premenopausal hormone receptor-positive breast cancer, and for managing oestrogen-dependent conditions including endometriosis and uterine fibroids. In each context, achieving amenorrhoea is the primary therapeutic goal, not a secondary finding. This makes the TxGNN prediction not only plausible but essentially a formal validation of current clinical practice.

The prediction is further reinforced by the volume and quality of supporting evidence: three completed Phase 3 RCTs with a combined enrolment exceeding 750 patients directly tested Goserelin's ability to induce and maintain amenorrhoea as an ovarian protection strategy. No other indication in the predicted list approaches this level of clinical support.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|------|--------|------------|--------------|
| [NCT00427245](https://clinicaltrials.gov/study/NCT00427245) | Phase 3 | Completed | 400 | OPTION trial: Goserelin vs no Goserelin to prevent premature menopause in premenopausal Stage I–III breast cancer patients undergoing chemotherapy; largest RCT directly assessing goserelin-induced amenorrhoea for ovarian protection |
| [NCT00068601](https://clinicaltrials.gov/study/NCT00068601) | Phase 3 | Completed | 257 | LHRH analogue (goserelin) co-administered with chemotherapy to prevent ovarian failure (early menopause) in Stage I–IIIA hormone receptor-negative breast cancer; randomised vs chemotherapy alone |
| [NCT02483767](https://clinicaltrials.gov/study/NCT02483767) | Phase 3 | Completed | 98 | Prospective RCT evaluating GnRH agonist goserelin for preserving ovarian function during chemotherapy in premenopausal breast cancer; ovarian function restoration after chemotherapy-induced amenorrhoea as primary endpoint |
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Phase 3 | Unknown | 300 | Adjuvant toremifene ± goserelin in premenopausal Stage I–IIIA HR+ breast cancer; chemotherapy-induced amenorrhoea used as ovarian suppression confirmation marker |
| [NCT03475758](https://clinicaltrials.gov/study/NCT03475758) | Phase 2 | Unknown | 100 | Goserelin for ovarian protection in premenopausal patients receiving cyclophosphamide-containing chemotherapy; menstruation outcome as primary endpoint |
| [NCT01218581](https://clinicaltrials.gov/study/NCT01218581) | Phase 2/3 | Completed | 32 | RCT comparing GnRH agonist (goserelin) vs aromatase inhibitor for uterine adenomyosis; amenorrhoea as secondary outcome; confirms amenorrhoea induction across gynaecological indications |
| [NCT00488722](https://clinicaltrials.gov/study/NCT00488722) | N/A | Unknown | N/A | Single-arm study of Zoladex 3.6 mg + CEF chemotherapy as neoadjuvant therapy in premenopausal operable breast cancer; documents reversible amenorrhoea as a key goserelin pharmacological effect |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | Meta-analysis / RCT | Annals of Oncology | OPTION trial publication: GnRH agonist (goserelin) during chemotherapy for early breast cancer significantly reduced premature ovarian insufficiency; confirms amenorrhoea induction as protective mechanism |
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | RCT | J Clin Oncology | IBCSG Trial VIII QOL analysis: amenorrhoea, hot flashes, and QOL compared between chemotherapy, goserelin, and sequential combination in premenopausal lymph node-negative breast cancer |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | RCT | J Natl Cancer Inst | IBCSG Trial VIII primary results: sequential CMF + goserelin vs either modality alone; goserelin-induced amenorrhoea confirmed as effective adjuvant endocrine strategy |
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | RCT | J Clin Oncology | ZEBRA study: goserelin vs CMF chemotherapy as adjuvant therapy in premenopausal node-positive breast cancer; ovarian suppression and amenorrhoea as key efficacy endpoints |
| [8513962](https://pubmed.ncbi.nlm.nih.gov/8513962/) | 1993 | RCT | Fertility & Sterility | GnRH agonist (goserelin) vs low-dose oral contraceptive for endometriosis-related pelvic pain; amenorrhoea induction compared between treatment arms |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | Cohort | Cancer Res & Treatment | Ovarian ablation using goserelin improves survival in premenopausal Stage II/III HR+ breast cancer without chemotherapy-induced amenorrhoea; highlights amenorrhoea status as prognostic marker |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Review / Meta-analysis | Breast Cancer Res & Treatment | Comprehensive overview of LHRH agonists in early breast cancer; goserelin as most extensively studied agent; reversible ovarian ablation (medical amenorrhoea) central to therapeutic rationale |
| [12734855](https://pubmed.ncbi.nlm.nih.gov/12734855/) | 2003 | Review | British J Surgery | Review of ovarian ablation methods including goserelin as adjuvant treatment for premenopausal breast cancer; medical amenorrhoea induction assessed across surgical, radiological, and pharmacological approaches |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Review | J Royal Army Medical Corps | Early review of therapeutic amenorrhoea induction; goserelin described as highly effective GnRH analogue for medical amenorrhoea with fewer systemic side effects than continuous oral contraceptives |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Observational | J Clin Oncology | Clinical discussion on oestradiol monitoring in women receiving goserelin-based ovarian suppression for breast cancer; amenorrhoea as practical clinical indicator of adequate suppression |

---

## Singapore Market Information

Goserelin is currently **not registered in Singapore**. No product authorisations are on record in the HSA database. Clinicians seeking to use this agent would need to explore import under the Therapeutic Products (Unregistered Medicinal Products) framework or named patient supply channels.

---

## Safety Considerations

Please refer to the package insert for safety information. No safety data (key warnings, contraindications, or drug interactions) was retrievable from the current data sources for this report. Formal safety documentation should be obtained directly from the manufacturer (AstraZeneca, Zoladex) or sourced from the Summary of Product Characteristics (SmPC) filed with EMA or PMDA prior to clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed Phase 3 RCTs with a combined enrolment of over 750 patients (OPTION trial, LHRH Analogue Study NCT00068601, and IBCSG-related NCT02483767) directly demonstrate Goserelin's ability to induce and maintain amenorrhoea as ovarian protection in premenopausal women; the mechanistic link is direct, pharmacologically established, and consistent with Goserelin's mode of action as a GnRH agonist — making this the strongest possible evidence base for a repurposing candidate.

**To proceed, the following is needed:**

- **Regulatory pathway**: Goserelin is not currently registered in Singapore; a formal HSA submission or Therapeutic Products (Unregistered) import licence would be required before clinical use
- **Safety documentation**: Obtain package insert warnings and contraindications (DG001 — Blocking severity); this is a prerequisite for any formal safety review
- **Formal MOA data**: Retrieve DrugBank MOA entry (DG002) to complete mechanistic documentation for regulatory dossier
- **Clinical context definition**: Clarify the specific indication scope — ovarian protection during chemotherapy, adjuvant ovarian suppression in HR+ breast cancer, standalone amenorrhoea induction, or gynaecological indication — as each may require a distinct regulatory and clinical pathway
- **Long-term safety monitoring plan**: Address known class effects of GnRH agonists including bone mineral density loss, vasomotor symptoms, and cardiovascular risk with prolonged oestrogen suppression; consider add-back hormone therapy protocols for use beyond 6 months
- **Local clinical feasibility assessment**: Determine whether Singapore oncology/gynaecology centres have existing experience with goserelin and identify appropriate patient selection criteria
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

