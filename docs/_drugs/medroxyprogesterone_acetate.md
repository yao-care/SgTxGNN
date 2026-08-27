---
layout: default
title: Medroxyprogesterone Acetate
parent: 僅模型預測 (L5)
nav_order: 634
evidence_level: L5
indication_count: 10
---

# Medroxyprogesterone Acetate
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

# Medroxyprogesterone Acetate: From Contraceptive/Hormonal Therapy to Amenorrhea

## One-Sentence Summary

> Medroxyprogesterone acetate (MPA) is a synthetic progestin most widely known as an injectable/oral contraceptive and hormone therapy agent (e.g. Depo-Provera).
> The TxGNN model predicts it may be effective for **Amenorrhea**,
> with **10 clinical trials** and **20 publications** currently retrieved in this evidence pack, though only a small subset directly and strongly support the mechanism.

> **Note on data completeness:** The formal `original_indications` and `original_moa` fields in this evidence pack are empty/data-gap (see DG002). The "contraceptive/hormonal therapy" framing above is drawn from the drug's own literature evidence within this pack (e.g. "Depo-Provera," "injectable contraception," "long-acting contraceptive options") rather than a structured indication record.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (data gap — `original_indications` empty, no Taiwan license record) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.9994% |
| Evidence Level | L2 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the evidence pack (`original_moa`: data gap, DG002). Based on known pharmacology, medroxyprogesterone acetate is a synthetic progestin. Progestins are well established to induce endometrial decidualization and, upon withdrawal, endometrial shedding ("withdrawal bleeding"); at higher/depot doses (as in DMPA — depot medroxyprogesterone acetate), the drug suppresses gonadotropin secretion and ovulation, which induces amenorrhea. This is in fact a well-documented feature of MPA when used as a long-acting injectable contraceptive.

The relationship between MPA's established contraceptive/hormonal use and the predicted new indication (amenorrhea) is therefore mechanistically close rather than distant: amenorrhea is already a recognized pharmacological consequence — and in some clinical contexts a deliberate therapeutic goal — of MPA/DMPA administration (e.g. induction of therapeutic amenorrhea in bleeding disorders, or endometrial-ablation-adjunct amenorrhea). Several items in the evidence base directly reflect this dual nature: PMID 9554247 examines "DMPA-induced amenorrhea" treatment/reversal, and PMID 842303 characterizes endometrial histology and hormone levels specifically in women with "MPA-induced amenorrhoea."

Because this mechanistic link is already embedded in MPA's known secondary pharmacology (rather than a novel, unrelated target), the TxGNN prediction is biologically plausible. However, the distinction between amenorrhea as a *side effect to manage* versus a *therapeutic endpoint to intentionally induce* matters clinically, and this evidence pack does not yet resolve which framing is intended — this should be clarified before any further development decision.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02449161](https://clinicaltrials.gov/study/NCT02449161) | Phase 3 | Terminated | 60 | Only trial directly evaluating post-ablation MPA on endometrial amenorrhea rate; highest mechanistic relevance (Grade A) but terminated early, limiting statistical power |
| [NCT00808132](https://clinicaltrials.gov/study/NCT00808132) | Phase 3 | Completed | 1,886 | Large double-blind RCT of bazedoxifene/conjugated estrogens on endometrial hyperplasia and osteoporosis prevention; intervention-drug correspondence to MPA/amenorrhea endpoint unconfirmed from title alone (Grade B) |
| [NCT06671548](https://clinicaltrials.gov/study/NCT06671548) | Phase 3 | Recruiting | 120 | Placebo-controlled RCT of relugolix for heavy menstrual bleeding with uterine fibroids; relevance to MPA-induced amenorrhea unconfirmed (Grade B) |
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Phase 4 | Completed | 42 | Examines progesterone-induced endometrial withdrawal bleeding before ovulation induction in oligo-/amenorrhea; mechanistically related but MPA not confirmed as the study drug (Grade B) |
| [NCT01463202](https://clinicaltrials.gov/study/NCT01463202) | Phase 4 | Completed | 184 | Directly uses postpartum DMPA, but primary endpoint is breastfeeding continuation, not amenorrhea (Grade B) |
| [NCT03018366](https://clinicaltrials.gov/study/NCT03018366) | Phase 2 | Completed | 29 | Observational study of functional hypothalamic amenorrhea and cardiovascular risk; not a treatment trial (Grade C) |
| [NCT00392093](https://clinicaltrials.gov/study/NCT00392093) | Phase 4 | Completed | 108 | HRT effect on disease activity/menopausal symptoms/bone density in SLE; not focused on amenorrhea induction (Grade C) |
| [NCT01300676](https://clinicaltrials.gov/study/NCT01300676) | Phase 2/3 | Completed | 79 | HRT safety profile with Tualang honey adjunct in postmenopausal women; not related to amenorrhea induction (Grade C) |
| [NCT07020429](https://clinicaltrials.gov/study/NCT07020429) | N/A | Not Yet Recruiting | 276 | Traditional Chinese herbal formula for premature ovarian insufficiency; intervention is not MPA (Grade C) |
| [NCT02792153](https://clinicaltrials.gov/study/NCT02792153) | Phase 1 | Withdrawn | 0 | Estradiol (not MPA) for fear-extinction in anorexia nervosa; withdrawn with zero enrollment (Grade C) |

**Overall trial quality note:** Only one trial (NCT02449161) directly tests MPA against the amenorrhea endpoint, and it was terminated with a small sample (n=60). The remainder are either indirectly related or use different interventions — this is a thin and mixed-quality trial base.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9554247](https://pubmed.ncbi.nlm.nih.gov/9554247/) | 1998 | Randomized comparative study | Contraception | 100 women with DMPA-induced amenorrhea randomized to Cyclofem switch vs. continued DMPA; 82% of Cyclofem users resumed bleeding vs. 10% of DMPA continuers — directly characterizes DMPA-induced amenorrhea |
| [842303](https://pubmed.ncbi.nlm.nih.gov/842303/) | 1977 | Mechanistic/endocrine study | Acta Obstet Gynecol Scand | Endometrial histology and circulating MPA/estradiol/FSH/LH levels in women with MPA-induced amenorrhoea vs. secondary amenorrhoea — direct mechanistic evidence |
| [38530848](https://pubmed.ncbi.nlm.nih.gov/38530848/) | 2024 | RCT | PLoS One | WHICH randomized trial comparing DMPA-IM vs. NET-EN on estradiol levels and menstrual/psychological/behavioral measures relevant to HIV risk |
| [8725701](https://pubmed.ncbi.nlm.nih.gov/8725701/) | 1996 | Review | J Reprod Med | Counseling framework and side-effect management for DMPA users, including menstrual disturbance/amenorrhea |
| [5107182](https://pubmed.ncbi.nlm.nih.gov/5107182/) | 1971 | Review | Obstetrics and Gynecology | Discusses therapeutic amenorrhea induction in hematologic disorders, relevant to intentional amenorrhea use case |
| [8492647](https://pubmed.ncbi.nlm.nih.gov/8492647/) | 1993 | Review | MCN Am J Matern Child Nurs | General clinical review of Depo-Provera, including menstrual effects |
| [6141923](https://pubmed.ncbi.nlm.nih.gov/6141923/) | 1984 | Review | Drug Intell Clin Pharm | Review of drug-induced infertility mechanisms, including hormonal agents affecting the hypothalamic-pituitary-gonadal axis |
| [12179873](https://pubmed.ncbi.nlm.nih.gov/12179873/) | 1988 | Review | International Health News | Discussion of Depo-Provera controversy, including menstrual/amenorrhea side effects |
| [6119259](https://pubmed.ncbi.nlm.nih.gov/6119259/) | 1981 | Review | Int J Gynaecol Obstet | Postpartum contraception review noting postpartum amenorrhea and timing of contraceptive initiation |
| [120837](https://pubmed.ncbi.nlm.nih.gov/120837/) | 1979 | Review | IARC Monographs | General pharmacological/toxicological monograph on medroxyprogesterone acetate |

---

## Taiwan Market Information

No Taiwan drug license records were found for medroxyprogesterone acetate in this evidence pack (`market_status`: 未上市 / Not Marketed; `total_licenses`: 0). No dosage-form or brand data is currently available.

---

## Safety Considerations

Please refer to the package insert for safety information. (All safety fields in this evidence pack — key warnings, contraindications, and drug interactions — are currently data gaps; DDI query returned no results.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base includes one directly relevant but underpowered/terminated Phase 3 trial (NCT02449161) and a small set of supportive historical literature (notably PMID 9554247 and PMID 842303) that specifically characterize MPA-induced amenorrhea, giving reasonable mechanistic plausibility (L2). However, the drug is not currently marketed in Taiwan (0 registrations), and both the mechanism-of-action and safety/contraindication data are formally missing from this pack — one of which (TFDA label data, DG001) is flagged as **Blocking** for any safety pre-assessment.

**To proceed, the following is needed:**
- TFDA package insert / label data (warnings, contraindications) — currently Blocking (DG001)
- Confirmed mechanism of action from DrugBank API — currently High-impact gap (DG002)
- Clarification of clinical intent (side-effect management vs. deliberate therapeutic amenorrhea induction), since these represent different regulatory and clinical pathways
- Additional completed, adequately powered RCTs directly testing MPA against an amenorrhea endpoint (the current strongest trial was terminated at n=60)
- DDI data, since the current query returned no results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

