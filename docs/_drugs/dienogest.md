---
layout: default
title: Dienogest
parent: 僅模型預測 (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
---

# Dienogest
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

# Dienogest: From Endometriosis to Amenorrhea

## One-Sentence Summary

Dienogest (Visanne®) is a fourth-generation progestin established for the treatment of endometriosis, where it suppresses the hypothalamic-pituitary-ovarian (HPO) axis to reduce estrogen and control ectopic endometrial tissue.
The TxGNN model predicts it may be applicable to **Amenorrhea**, with **4 clinical trials** and **6 publications** currently available — however, all existing evidence documents amenorrhea as a *pharmacological consequence* of dienogest therapy (incidence 40–70%), not as a primary therapeutic target.
This mechanistic inversion is the central issue: the drug *induces* amenorrhea rather than *treats* it, and the research question must be carefully re-framed before any repurposing pathway can be defined.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Endometriosis |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dienogest is a fourth-generation synthetic progestin with highly selective progesterone receptor (PR-A and PR-B) affinity and minimal androgenic or estrogenic activity. Its primary mechanism in endometriosis is suppression of the HPO axis, which reduces circulating estradiol to early follicular-phase levels, depriving ectopic endometrial implants of hormonal stimulation. A direct pharmacological consequence of this HPO suppression is the reliable induction of amenorrhea, reported in 40–70% of patients across clinical studies.

The TxGNN model almost certainly detected the strong statistical co-occurrence between dienogest and amenorrhea in the biomedical knowledge graph — a correlation that is pharmacologically valid, but reflects a causal rather than therapeutic relationship. Pathological amenorrhea (e.g., hypothalamic amenorrhea, PCOS-related anovulation, or structural causes) requires restoration of normal hormonal cycling, not further suppression. Administering a potent HPO-suppressing progestin to treat amenorrhea would, in most disease contexts, worsen rather than resolve the condition.

That said, a legitimate re-framing exists: where *therapeutic* amenorrhea is the intended clinical goal — such as managing refractory heavy menstrual bleeding, relieving endometriosis-related dysmenorrhea, or providing hormonal quiescence prior to uterine procedures — dienogest's amenorrhea-inducing property could reasonably be considered its primary therapeutic mechanism. Pursuing this angle, however, requires a distinctly defined research question separate from "treating amenorrhea disease."

---

## Clinical Trial Evidence

> **Important context:** All four identified trials target endometriosis as the primary indication. Amenorrhea appears in these trials as a secondary endpoint or a documented adverse event — not as the condition being treated.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Phase 3 | Recruiting | 290 | Multicenter non-inferiority RCT comparing Indinol Forto® 200 mg vs Visanne® 2 mg in endometriosis; amenorrhea rate likely captured as a secondary efficacy or safety endpoint |
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | Observational | Completed | 895 | ENVISION prospective cohort in Asian women with endometriosis treated with dienogest in routine practice; amenorrhea recorded as an adverse event rather than a treatment outcome |
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | Observational | Completed | 968 | VISANNE real-world study in endometriosis; provides real-world incidence data on amenorrhea during dienogest therapy |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | Observational | Active, Not Recruiting | 138 | Compares dienogest+transdermal estradiol versus drospirenone+transdermal estradiol regimens in endometriosis; focuses on patient satisfaction and tolerability |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Systematic Review + Bayesian Analysis | BMC Pharmacology & Toxicology | Comprehensive adverse effect profile of dienogest across endometriosis and adenomyosis studies; amenorrhea is among the most frequently reported pharmacological effects |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Mechanistic/Pharmacological Study | Eur J Contracept Reprod Health Care | Characterises the high inhibition ratio and transformation index of 2 mg dienogest; explicitly frames amenorrhea induction and hypoestrogenic environment as the intended therapeutic mechanism in endometriosis |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Narrative Review | Reviews in Endocrine & Metabolic Disorders | Endocrine basis of hormonal endometriosis therapy; covers progesterone resistance, estrogen dependency, and long-term hormonal management strategies |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Retrospective Cohort | Reproductive Sciences | Long-term efficacy and safety of dienogest in 514 women with ovarian endometrioma over >12 months; documents sustained amenorrhea rates and recurrence patterns |

---

## Singapore Market Information

Dienogest is not currently registered or marketed in Singapore. No product authorizations are on record with HSA. Brands available in neighbouring markets (e.g., Visanne® by Bayer) would require a separate registration application before any clinical use in Singapore.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction captures a real pharmacological relationship — dienogest reliably induces amenorrhea — but the mechanistic direction is inverted relative to a repurposing claim. All available clinical trial and literature evidence positions amenorrhea as a *downstream effect* of HPO suppression in endometriosis management, not as a disease being treated. Without first resolving whether the target indication is "therapeutic amenorrhea induction" (plausible) or "treatment of pathological amenorrhea" (contradicted by mechanism), this candidate cannot advance to safety or feasibility review.

**To proceed, the following is needed:**

- **Re-define the research question**: Clarify whether the proposed repurposing is (a) using dienogest's amenorrhea-inducing property as a primary endpoint in a new indication such as heavy menstrual bleeding or pre-procedural hormonal quiescence, or (b) treating pathological amenorrhea — the latter lacks mechanistic support and should be deprioritised
- **Retrieve complete MOA data** from DrugBank (currently unavailable) to confirm receptor binding profile, HPO suppression kinetics, and tissue selectivity
- **Obtain full safety profile** from the package insert or an HSA-equivalent monograph (all key warnings and contraindications are currently missing — a blocking data gap)
- **Assess Singapore registration pathway**: With zero existing authorizations and no HSA-approved product, a fresh regulatory strategy is required before any clinical development can be planned locally
- **If pursuing therapeutic amenorrhea induction**: Design a prospective study with amenorrhea rate as the primary endpoint and clinically meaningful secondary endpoints (e.g., pain scores, quality of life) to distinguish this from existing endometriosis indications

---

*This report is generated for research reference purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

