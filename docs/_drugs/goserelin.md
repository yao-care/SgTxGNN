---
layout: default
title: Goserelin
parent: High Evidence (L1-L2)
nav_order: 490
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Goserelin: predicted new indication Amenorrhea (evidence level L1). Approved use: Endometriosis"
monitor_inn: "Goserelin"
predicted_indications: ["amenorrhea (disease)", "renal hypoplasia (disease)", "renal hypoplasia, bilateral", "gelatinous drop-like corneal dystrophy", "duodenogastric reflux", "duodenal obstruction", "duodenal ulcer (disease)"]
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

# Goserelin: From Endometriosis to Amenorrhea

## One-Sentence Summary

Goserelin is a GnRH (gonadotropin-releasing hormone) agonist, originally used to treat endometriosis.
The TxGNN model predicts it may be effective for **amenorrhea**, with **1 clinical trial** and **16 publications** currently supporting this direction.
Amenorrhea is largely an expected pharmacological effect of ovarian suppression rather than a separate disease target, so the evidence is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis (the Singapore licence records contain no approved indication text) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, goserelin is a GnRH agonist. Continuous exposure desensitises pituitary GnRH receptors, which suppresses LH and FSH and lowers ovarian estradiol production. The result is a reversible, hypoestrogenic state with amenorrhea.

Endometriosis lesions depend on estrogen, so this suppression is how goserelin relieves the disease. Amenorrhea is therefore a built-in effect of the same mechanism. It is also used as a marker of ovarian suppression in premenopausal breast cancer. Chemotherapy-induced amenorrhea and ovarian failure have been studied as outcomes of goserelin ovarian protection.

An important caveat: amenorrhea here is a therapeutic effect or side effect, not a distinct disease for which goserelin is the treatment. The high model score reflects this strong mechanistic link, but the evidence does not show goserelin as a treatment for pathological amenorrhea.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Phase 3 | Unknown | 300 | Adjuvant toremifene with or without goserelin in premenopausal women with hormone receptor-positive stage I-IIIA breast cancer, with or without chemotherapy-induced amenorrhoea. Amenorrhea is a pharmacodynamic outcome here, so the trial is only indirectly relevant. No results confirmed. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | RCT | J Clin Oncol | Goserelin versus CMF chemotherapy as adjuvant therapy in premenopausal node-positive breast cancer (ZEBRA study), looking at short-term toxicity and premature menopause |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | RCT | J Natl Cancer Inst | IBCSG Trial VIII: chemotherapy followed by goserelin versus either alone in node-negative premenopausal breast cancer |
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | RCT (secondary analysis) | J Clin Oncol | Impact of chemotherapy, goserelin, or both on amenorrhea, hot flashes and quality of life |
| [8513962](https://pubmed.ncbi.nlm.nih.gov/8513962/) | 1993 | RCT | Fertil Steril | Goserelin versus low-dose oral contraceptive for endometriosis-associated pelvic pain |
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | Meta-analysis/Review | Ann Oncol | OPTION trial: GnRH agonist during chemotherapy for early breast cancer to reduce the risk of premature ovarian insufficiency |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Review | Breast Cancer Res Treat | Overview of LHRH agonists, including goserelin, in early breast cancer and the benefits of reversible ovarian ablation |
| [12734855](https://pubmed.ncbi.nlm.nih.gov/12734855/) | 2003 | Review | Br J Surg | Methods of ovarian ablation and the relevance of ovarian suppression in adjuvant breast cancer treatment |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Review | J R Army Med Corps | Therapeutic induction of amenorrhoea; goserelin discussed as an effective option alongside continuous oral contraceptives |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | Cohort | Cancer Res Treat | Goserelin ovarian ablation improved survival in stage II/III hormone receptor-positive breast cancer without chemotherapy-induced amenorrhea |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Cohort/Grand Rounds | J Clin Oncol | Whether estradiol monitoring is necessary during ovarian suppression for breast cancer |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN01506P | ZOLADEX DEPOT INJECTION 3.6 mg/syringe | Injection | Not stated in the licence record |
| SIN09793P | ZOLADEX LA DEPOT INJECTION 10.8 mg/syringe | Injection | Not stated in the licence record |

Both licences are valid, single-ingredient products from AstraZeneca UK Ltd.

## Safety Considerations

- **Contraindication-related conditions (from knowledge-graph associations, not package insert text)**: hypertension and hypertensive disorder, hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, obesity (including monogenic obesity), and urinary tract obstruction.
- **Drug Interactions**: 100 interactions were identified. Most are of moderate severity; the one Major interaction in the listed results is **dolasetron**. Moderate interactions in the list include:
  - Antidiabetic agents: acarbose, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide, empagliflozin, glimepiride, linagliptin, metformin, saxagliptin, albiglutide
  - Others: famotidine, loperamide, bisacodyl, clarithromycin, picosulfuric acid, polyethylene glycol (3350 with electrolytes), palonosetron

The package insert warnings and contraindications could not be obtained. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Goserelin reliably induces reversible amenorrhea through ovarian suppression, and several RCTs in breast cancer and endometriosis document this effect. However, amenorrhea is an expected pharmacological effect rather than an independent treatment target. The only registered trial addresses breast cancer, with amenorrhea as an indirect outcome and no confirmed results. The evidence level of L1 therefore overstates direct support for amenorrhea as an indication.

**To proceed, the following is needed:**
- Clarify whether the intended use is therapeutic induction of amenorrhea (for example, menstrual suppression or protection of ovarian function during chemotherapy) or treatment of pathological amenorrhea. The latter is not supported by the data.
- Obtain the Singapore package insert (warnings, contraindications, approved indications), which was unavailable for this review.
- Obtain detailed mechanism of action data from DrugBank.
- Review the DDI list, especially the Major interaction with dolasetron and the antidiabetic agents, together with the metabolic conditions flagged in the contraindication associations.
- Monitor bone density and menopausal symptoms in any long-term or non-oncology use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

