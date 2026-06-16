---
layout: default
title: Ethinylestradiol
parent: 僅模型預測 (L5)
nav_order: 403
evidence_level: L5
indication_count: 10
---

# Ethinylestradiol
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

# Ethinylestradiol: From Oral Contraception to Amenorrhea

## One-Sentence Summary

Ethinylestradiol (EE) is a synthetic estrogen that has served as the estrogenic component of combined oral contraceptive pills worldwide for over 60 years, acting on estrogen receptors throughout the body to regulate the hypothalamic-pituitary-ovarian (HPO) axis.
The TxGNN model predicts it may be effective for **Amenorrhea**, with **8 clinical trials** and **20 publications** currently supporting this direction.
Among all 10 predicted indications, amenorrhea carries the strongest clinical evidence (L2) and is the only indication reaching the actionable threshold.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Oral contraception (estrogenic component of combined oral contraceptives) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 94.68% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ethinylestradiol is a synthetic derivative of 17β-estradiol, modified at the C17α position with an ethinyl group to achieve oral bioavailability by resisting first-pass hepatic metabolism. As an estrogen receptor (ERα/ERβ) agonist, EE exerts its principal effects through stimulating endometrial proliferation, modulating pituitary gonadotropin release (FSH/LH) via negative feedback, and — when combined with a progestogen — inducing predictable cyclic withdrawal bleeding.

Amenorrhea (absent or suppressed menstruation) and EE's pharmacological actions are mechanistically tightly coupled. In functional hypothalamic amenorrhea — as seen in athletes with energy deficiency or patients with anorexia nervosa — the HPO axis becomes hypoactive, resulting in insufficient endogenous estrogen. EE directly corrects this deficiency, restoring endometrial responsiveness and enabling cycle-like bleeding when paired with a progestogen. This is precisely the mechanism underlying its use in the estrogen-progestogen challenge test as a diagnostic tool for amenorrhea evaluation.

Beyond deficiency states, clinicians have long used EE-containing preparations therapeutically to induce or suppress menstruation (e.g., in blood dyscrasias where menstrual blood loss poses risk), and in hyperandrogenic conditions such as polycystic ovary syndrome (PCOS) where irregular or absent cycles are common. The mechanistic link is not hypothetical — it is the foundation of how combined oral contraceptives regulate the menstrual cycle. The TxGNN prediction therefore reflects a well-understood pharmacology, not a speculative extrapolation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01103518](https://clinicaltrials.gov/study/NCT01103518) | Phase 4 | Unknown | 100 | Randomised double-blind comparison of two EE + cyproterone acetate preparations for menstrual irregularities of hyperandrogenic origin — the most directly relevant trial with EE as primary study drug |
| [NCT04831151](https://clinicaltrials.gov/study/NCT04831151) | N/A | Unknown | 42 | Compares two EE-containing OC formulations (cyproterone vs drospirenone) on blood metabolomics in PCOS women — directly evaluates EE-based treatment in a population with frequent amenorrhea |
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | Completed | 121 | Transdermal vs oral estrogen in adolescent athletes with functional hypothalamic amenorrhea and estrogen deficiency — evaluates estrogen replacement for bone and hormonal outcomes in amenorrheic athletes |
| [NCT00088153](https://clinicaltrials.gov/study/NCT00088153) | Phase 2/3 | Completed | 110 | Estrogen administration (including EE-containing OC) to adolescent girls with anorexia nervosa-related amenorrhea — assesses hormone replacement for bone density preservation |
| [NCT01588873](https://clinicaltrials.gov/study/NCT01588873) | Phase 4 | Unknown | 42 | 59-week comparison of oral EE-containing OC vs hormonal vaginal ring in PCOS women — evaluates androgen suppression, metabolic effects and cycle regulation |
| [NCT01165307](https://clinicaltrials.gov/study/NCT01165307) | Phase 4 | Completed | 77 | Medical therapy (OC as a primary option) vs radiofrequency endometrial ablation for menorrhagia — supports EE-based hormonal management of menstrual disorders in a comparative surgical trial |
| [NCT02729545](https://clinicaltrials.gov/study/NCT02729545) | Phase 2 | Completed | 60 | Acupuncture vs Diane-35 (EE/cyproterone) as active control for PCOS ovarian function — EE arm serves as active comparator, providing safety data in the PCOS/amenorrhea context |
| [NCT00117260](https://clinicaltrials.gov/study/NCT00117260) | Phase 3 | Withdrawn | 0 | Seasonale (EE-containing extended-cycle OC) for secondary amenorrhea with osteopenia in adolescents — trial was withdrawn before enrolment; no efficacy data available |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [5107182](https://pubmed.ncbi.nlm.nih.gov/5107182/) | 1971 | Case Series | Obstet Gynecol | Therapeutic amenorrhea induction using hormonal contraception (including EE-containing preparations) in patients with haematologic disorders to reduce menstrual blood loss — earliest direct clinical use of EE for amenorrhea management |
| [9130733](https://pubmed.ncbi.nlm.nih.gov/9130733/) | 1997 | Clinical Trial | Hum Reprod | GnRH agonist plus EE/CPA vs EE/CPA alone in PCOS hyperandrogenism — demonstrates EE's central role in cycle regulation and androgen suppression in a population with amenorrhoea |
| [15025547](https://pubmed.ncbi.nlm.nih.gov/15025547/) | 2004 | Drug Review | Drugs | Comprehensive profile of EE/chlormadinone acetate — documents efficacy in menstrual regulation, acne, and contraception, including comparison with EE/levonorgestrel |
| [8447356](https://pubmed.ncbi.nlm.nih.gov/8447356/) | 1993 | Review | Am J Obstet Gynecol | Desogestrel/EE tolerability profile — highlights non-contraceptive benefits of EE-containing OC including dysmenorrhoea reduction and menstrual cycle regulation |
| [8324604](https://pubmed.ncbi.nlm.nih.gov/8324604/) | 1993 | Cohort | Br Med Bull | Review of safety and efficacy of combined OC in over 60 million users — documents that health risks are dose-dependent, and discusses menstrual cycle management benefits |
| [3161265](https://pubmed.ncbi.nlm.nih.gov/3161265/) | 1985 | Pharmacodynamic Study | Acta Obstet Gynecol Scand Suppl | Androgenicity of progestogens when combined with EE — specifically addresses PCO-related amenorrhea, obesity and hirsutism as context for EE-progestogen combination selection |
| [65298](https://pubmed.ncbi.nlm.nih.gov/65298/) | 1977 | Clinical Guidance | Fertil Steril | Systematic diagnostic scheme for primary and secondary amenorrhea — proposes the cyclic estrogen-progestogen (EE-based) test as a key diagnostic step, underpinning EE's mechanistic role |
| [3118717](https://pubmed.ncbi.nlm.nih.gov/3118717/) | 1987 | Review | Am J Obstet Gynecol | Progestogen potency in OC — explains how unopposed EE causes endometrial hyperplasia and amenorrhea; combined cycling produces predictable withdrawal bleeding and acceptable menstrual patterns |
| [12279701](https://pubmed.ncbi.nlm.nih.gov/12279701/) | 1983 | Clinical Review | Lyon Méd | Direct discussion of amenorrhea and the contraceptive pill — addresses post-pill amenorrhea and the use of EE-containing preparations in cycle management |
| [803166](https://pubmed.ncbi.nlm.nih.gov/803166/) | 1975 | Clinical Review | Fertil Steril | Management of endometriosis in infertile patients — discusses therapeutic amenorrhea induction with EE-based pseudopregnancy and pseudomenopause regimens, extending EE's use beyond contraception |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug interaction data were not available in this Evidence Pack. Given that EE is a well-established pharmaceutical agent with a long clinical history, clinicians should consult the full prescribing information — particularly regarding thromboembolic risk, cardiovascular contraindications, hormone-sensitive conditions, and interactions with enzyme-inducing medications — before any therapeutic application.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
EE's mechanism of action directly addresses the hormonal deficiency underlying functional hypothalamic amenorrhea, and its use in menstrual cycle regulation is supported by decades of clinical experience, multiple completed Phase 3/4 trials, and an extensive literature base — meeting the L2 evidence threshold (at least one completed Phase 2/3 intervention study). However, EE is not currently registered in Singapore, and comprehensive safety data (TFDA package insert warnings, contraindications, DDI profile) is absent from this pack, preventing full safety gatekeeping.

**To proceed, the following is needed:**
- Obtain full prescribing information (package insert / SmPC) for EE-containing products to complete S1 safety screening — particularly thromboembolic risk, cardiovascular contraindications, and hepatic impairment warnings
- Clarify the specific amenorrhea subtype being targeted (functional hypothalamic, hyperandrogenic/PCOS-related, post-pill, or therapeutic), as evidence strength and risk-benefit profiles differ significantly by aetiology
- Confirm whether a standalone EE formulation or an EE-containing combination product (with progestogen) is intended, as monotherapy EE carries unopposed oestrogen risk
- Assess Singapore regulatory pathway: as EE is not currently marketed, a new marketing authorisation application or compassionate use framework would be required
- Conduct mechanistic similarity analysis to the original indication to formalize the rationale for the TxGNN prediction (currently marked as "pending")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

