---
layout: default
title: Goserelin
parent: High Evidence (L1-L2)
nav_order: 486
evidence_level: L1
indication_count: 10
---

# Goserelin
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Goserelin: From GnRH-Agonist Hormonal Therapy to Amenorrhea (Ovarian Function Preservation)

## One-Sentence Summary

Goserelin (Zoladex) is a GnRH agonist that suppresses ovarian hormone production. The TxGNN model predicts it may be effective for **amenorrhea**, which is really the drug's expected pharmacological effect. The clinically meaningful question is **protecting ovarian function during chemotherapy** in premenopausal cancer patients. This direction is supported by **7 clinical trials** (3 completed Phase 3 RCTs) and **20 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data (the approved indication text for both Singapore licences is blank) |
| Predicted New Indication | Amenorrhea (best interpreted as preventing chemotherapy-induced premature ovarian failure) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from DrugBank. Goserelin is a GnRH agonist. Sustained use desensitises the pituitary, lowers LH/FSH and estradiol, and induces reversible amenorrhea.

Amenorrhea is therefore an effect of goserelin, not a disease it treats. The label should be reframed as **ovarian function preservation** (preventing premature ovarian failure) in premenopausal patients receiving chemotherapy. The idea is that temporarily suppressing the ovaries during chemotherapy may reduce the damage the treatment does to them. Several Phase 3 RCTs test this in breast cancer.

Other ranked predictions do not hold up as well:
- **Endometriosis subtypes** (cervical, rectovaginal septum, cutaneous scar) are mechanistically plausible because goserelin-induced hypoestrogenism is a recognised endometriosis treatment. The evidence is limited to case reports.
- **The remaining predictions** (renal hypoplasia, gelatinous drop-like corneal dystrophy, duodenogastric reflux, duodenal obstruction, duodenal ulcer) have no plausible mechanism and no trials or literature. They are likely knowledge-graph artifacts.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00427245](https://clinicaltrials.gov/study/NCT00427245) | Phase 3 | Completed | 400 | OPTION: goserelin vs no goserelin to prevent early menopause in premenopausal breast cancer patients undergoing chemotherapy |
| [NCT00068601](https://clinicaltrials.gov/study/NCT00068601) | Phase 3 | Completed | 257 | LHRH analog during chemotherapy vs chemotherapy alone to reduce ovarian failure in hormone-receptor-negative early breast cancer |
| [NCT02483767](https://clinicaltrials.gov/study/NCT02483767) | Phase 3 | Completed | 98 | Randomised (1:1) chemotherapy with vs without goserelin to preserve ovarian function in premenopausal breast cancer |
| [NCT03475758](https://clinicaltrials.gov/study/NCT03475758) | Phase 2 | Unknown | 100 | Goserelin for ovarian protection in premenopausal patients receiving cyclophosphamide-containing chemotherapy (menstruation outcome); results may not be available |
| [NCT00488722](https://clinicaltrials.gov/study/NCT00488722) | N/A | Unknown | N/A | Single-arm study of Zoladex 3.6 mg with CEF neoadjuvant chemotherapy in premenopausal breast cancer; no control arm |
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Phase 3 | Unknown | 300 | Toremifene with or without goserelin in premenopausal breast cancer. Goserelin acts as ovarian suppression for cancer treatment, so it is only indirectly relevant |
| [NCT01218581](https://clinicaltrials.gov/study/NCT01218581) | Phase 2/3 | Completed | 32 | Aromatase inhibitors vs GnRH agonists for uterine adenomyosis. This is a different condition, and amenorrhea is only a therapeutic effect |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | RCT | J Clin Oncol | IBCSG Trial VIII: compares quality of life, amenorrhea and hot flashes after chemotherapy, goserelin, or both in premenopausal node-negative breast cancer |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | RCT | J Natl Cancer Inst | IBCSG Trial VIII: sequential chemotherapy then goserelin vs each modality alone |
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | RCT | J Clin Oncol | ZEBRA study: goserelin vs CMF chemotherapy in node-positive premenopausal breast cancer, with attention to premature menopause |
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | Review (as classified; reports the OPTION trial) | Ann Oncol | Anglo Celtic Group OPTION trial: tests whether a GnRH agonist during chemotherapy reduces the risk of premature ovarian insufficiency |
| [21325445](https://pubmed.ncbi.nlm.nih.gov/21325445/) | 2011 | Long-term follow-up | Ann Oncol | Long-term results of IBCSG Trial VIII (goserelin, chemotherapy, or both) |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | Cohort | Cancer Res Treat | Goserelin ovarian ablation in stage II/III hormone-receptor-positive breast cancer without chemotherapy-induced amenorrhea |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Review | Breast Cancer Res Treat | Overview of LHRH agonists in early breast cancer and the benefits of reversible ovarian ablation |
| [12734855](https://pubmed.ncbi.nlm.nih.gov/12734855/) | 2003 | Review | Br J Surg | Methods of ovarian ablation in adjuvant treatment of premenopausal and perimenopausal breast cancer |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Review | J R Army Med Corps | Goserelin as an effective way to induce amenorrhea, discussed for female military personnel |
| [2522795](https://pubmed.ncbi.nlm.nih.gov/2522795/) | 1989 | Clinical study | Br J Obstet Gynaecol | Gonadotrophin suppression with goserelin in 12 women with premature ovarian failure; the title reports that it does not reverse the failure |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN01506P | ZOLADEX DEPOT INJECTION 3.6 mg/syringe | Injection | Not stated in the data |
| SIN09793P | ZOLADEX LA DEPOT INJECTION 10.8 mg/syringe | Injection | Not stated in the data |

## Safety Considerations

Please refer to the package insert for safety information. Interaction queries returned no results.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed Phase 3 RCTs (OPTION, NCT00068601, NCT02483767) directly test goserelin for ovarian protection during chemotherapy, and the drug is already marketed in Singapore. The TxGNN label "amenorrhea" is misleading, so any further work must be framed as ovarian function or fertility preservation.

**To proceed, the following is needed:**
- Define the outcome as ovarian function or fertility, not amenorrhea itself.
- Analyse hormone-receptor-negative and hormone-receptor-positive breast cancer separately.
- Exclude trials where goserelin serves as cancer-treatment ovarian suppression rather than protection (for example NCT02132390).
- Review long-term fertility and survival data.
- Obtain and review the HSA package insert (warnings, contraindications and approved indications); safety screening cannot proceed without it.
- Retrieve mechanism-of-action data from DrugBank.
- Treat the endometriosis subtypes as research questions only, focusing on site-specific efficacy and recurrence after discontinuation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

