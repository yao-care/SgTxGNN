---
layout: default
title: Desogestrel
parent: 僅模型預測 (L5)
nav_order: 230
evidence_level: L5
indication_count: 10
---

# Desogestrel
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

# Desogestrel: From Oral Contraception to Amenorrhea

## One-Sentence Summary

Desogestrel is a third-generation synthetic progestogen widely used as a component in combined oral contraceptives (COCs) and as a progestogen-only pill (POP), primarily for contraception.
The TxGNN model predicts it may have clinical relevance for **Amenorrhea**, with **2 clinical trials** and **16 publications** currently providing contextual evidence — though the biological relationship is notably bidirectional and requires careful sub-type characterisation before any repurposing claim can be made.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Oral contraception (progestogen component in COC and POP) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacology, Desogestrel is a third-generation gonane progestogen that is metabolised upon oral absorption to its biologically active form, etonogestrel. It exerts its primary effect by suppressing the hypothalamic–pituitary–ovarian (HPO) axis — attenuating the LH surge and reliably inhibiting ovulation at the 75 µg progestogen-only dose. This deep HPO axis engagement is the mechanistic basis for TxGNN's strong association between Desogestrel and amenorrhea.

However, the relationship is explicitly bidirectional, which makes the prediction pharmacologically plausible but therapeutically nuanced. At the POP dose (75 µg), Desogestrel itself is a recognised *cause* of functional amenorrhea — a substantial proportion of users experience absent or highly infrequent withdrawal bleeding as a direct consequence of HPO suppression. Conversely, in hyperandrogenic states such as polycystic ovary syndrome (PCOS), combined formulations of desogestrel with ethinyl estradiol reduce free androgen levels, raise sex hormone-binding globulin (SHBG), and can restore regular cyclical bleeding in women with androgen-excess amenorrhea. Pharmacodynamic studies from the 1980s–1990s specifically evaluated desogestrel's lower androgenicity relative to earlier progestogens in the context of acne and amenorrhea in PCOS-like presentations.

The high TxGNN score almost certainly reflects the strong knowledge-graph signal connecting Desogestrel to the HPO axis and amenorrhea-related nodes, rather than a conventional repurposing signal where a drug treats a new disease. Whether the drug is being considered as a *treatment for* amenorrhea or as a *modulator of* the hormonal milieu that underlies it depends entirely on the amenorrhea sub-type. This distinction must be resolved before any development pathway can be defined.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | Completed | 121 | Investigates fat-mediated modulation of reproductive and endocrine function in young athletes with exercise-induced amenorrhea; evaluates whether transdermal or oral oestrogen improves bone density in oestrogen-deficient amenorrhoeic athletes. Desogestrel is a study variable rather than the primary intervention. |
| [NCT01588873](https://clinicaltrials.gov/study/NCT01588873) | Phase 4 | Unknown | 42 | Compares combined OC (containing desogestrel) versus hormonal vaginal ring on androgen secretion, insulin and lipid metabolism, and SHBG in women with PCOS — a condition commonly associated with oligomenorrhoea and amenorrhoea. Study status is unknown; small sample size limits interpretability. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35261299](https://pubmed.ncbi.nlm.nih.gov/35261299/) | 2022 | RCT/Observational | Gynecological Endocrinology | Compares bleeding profiles of drospirenone-only pill (4 mg) versus desogestrel 75 µg in women with cardiovascular risk factors; directly notes that desogestrel POP is associated with irregular bleeding and amenorrhea, highlighting the challenge of cycle control |
| [21249657](https://pubmed.ncbi.nlm.nih.gov/21249657/) | 2011 | Systematic Review/Meta-analysis | Cochrane Database Syst Rev | Updated Cochrane review comparing 20 µg versus >20 µg oestrogen COCs; evaluates contraceptive effectiveness and dose-dependent changes in bleeding patterns including amenorrhea incidence across formulations |
| [18843653](https://pubmed.ncbi.nlm.nih.gov/18843653/) | 2008 | Systematic Review/Meta-analysis | Cochrane Database Syst Rev | Original Cochrane review on oestrogen dose in COCs; provides meta-analytic data on bleeding irregularity and amenorrhea rates associated with low-dose formulations containing desogestrel |
| [8218004](https://pubmed.ncbi.nlm.nih.gov/8218004/) | 1993 | Comparative RCT | British Journal of Obstetrics and Gynaecology | Randomised comparison of two desogestrel-containing OCs (Mercilon 20 µg EE vs Marvelon 30 µg EE); directly assesses cycle control differences including amenorrhea rates between formulations |
| [3161265](https://pubmed.ncbi.nlm.nih.gov/3161265/) | 1985 | Pharmacodynamic Study | Acta Obstet Gynecol Scand Suppl | Foundational pharmacodynamic study of desogestrel alone and in combination with EE; specifically evaluates androgenicity relative to other progestogens and discusses relevance to amenorrhea in PCOS-like states |
| [11725730](https://pubmed.ncbi.nlm.nih.gov/11725730/) | 2001 | Clinical Study | Journal of Reproductive Medicine | Evaluates OC effect on bone mineral density in young women with hypothalamic (hypogonadotrophic) amenorrhea; examines whether oestrogen dose in desogestrel-containing OCs influences bone loss |
| [23221134](https://pubmed.ncbi.nlm.nih.gov/23221134/) | 2012 | Clinical Study | Georgian Medical News | Examines central-genesis menstrual disorders including amenorrhea and oligomenorrhoea in 159 infertile women; evaluates hormonal management pathways for central forms |
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | RCT | Contraception | Randomised trial comparing Implanon (etonogestrel — the active metabolite of desogestrel) versus Norplant; documents amenorrhea as a key quantitative outcome, providing direct data on etonogestrel-induced amenorrhea rates over 4 years |
| [1436906](https://pubmed.ncbi.nlm.nih.gov/1436906/) | 1992 | Review | Obstetrical & Gynecological Survey | Comprehensive review of third-generation progestogens including desogestrel; discusses lower androgenicity as rationale for improved cycle control and reduced androgen-related amenorrhea |
| [8324604](https://pubmed.ncbi.nlm.nih.gov/8324604/) | 1993 | Review | British Medical Bulletin | Reviews safety and efficacy of combined OCs in over 60 million users; discusses dose–response relationships affecting bleeding patterns, with implications for amenorrhea management |

---

## Singapore Market Information

Desogestrel currently has no registered products in Singapore (HSA). No authorization records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is exceptionally high (99.96%), reflecting a genuine and well-established biological connection between Desogestrel and the HPO axis pathways that govern menstrual cyclicity. However, this connection is bidirectional — Desogestrel can both *induce* amenorrhea (as a POP side effect) and potentially *resolve* certain forms of hyperandrogenic amenorrhea (via combined OC formulations). The existing evidence (L3: predominantly reviews and observational data, with no trial specifically designed to treat amenorrhea with Desogestrel) is insufficient to define a repurposing hypothesis without first stratifying by amenorrhea sub-type. Notably, the **acne** indication (TxGNN rank 4, evidence level L2, "Proceed with Guardrails") carries substantially stronger direct clinical evidence, with a dedicated Phase 4 trial and multiple clinical studies demonstrating anti-androgenic benefit — this may represent a more actionable near-term repurposing pathway.

**To proceed, the following is needed:**

- **Sub-type stratification**: clearly define the target amenorrhea population — hyperandrogenic (PCOS-associated) amenorrhea versus hypogonadotrophic/functional (exercise-induced, stress-related) amenorrhea — as the therapeutic role of Desogestrel differs fundamentally between these
- **MOA data**: retrieve full mechanism of action from DrugBank API (DB00304) to support mechanistic narrative
- **Safety data**: obtain TFDA/HSA package insert PDF and extract key warnings, contraindications, and drug interactions (currently a blocking data gap per DG001)
- **Regulatory landscape review**: assess whether any existing COC or POP label in Singapore, Taiwan, or internationally implicitly covers amenorrhea management as a recognised non-contraceptive benefit
- **Prospective study design**: if advancing, develop a protocol specifically evaluating Desogestrel (COC or POP formulation) as a treatment for a defined amenorrhea sub-type, with prespecified primary endpoints (return of cyclical bleeding, hormone normalisation)
- **Consider acne indication in parallel**: given stronger evidence (L2) for the acne repurposing pathway, evaluate whether a concurrent development plan for that indication is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

