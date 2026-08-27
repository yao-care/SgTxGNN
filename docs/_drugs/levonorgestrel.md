---
layout: default
title: Levonorgestrel
parent: 僅模型預測 (L5)
nav_order: 592
evidence_level: L5
indication_count: 10
---

# Levonorgestrel
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

# Levonorgestrel: From Contraception to Acne

## One-Sentence Summary

Levonorgestrel is a progestin widely used in oral contraceptives, emergency contraception, and intrauterine systems (IUS) for contraception. The TxGNN model predicts it may also be effective for **Acne**, with **5 clinical trials** and **20 publications** identified in the evidence pack, though only a small subset directly examine Levonorgestrel-containing regimens in acne, and the mechanistic direction is not fully consistent.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Contraception (progestin; no Singapore-approved label text available — see Market Status below) |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA query returned a data gap). Based on the evidence available, Levonorgestrel is a synthetic progestin derived from 19-nortestosterone and is best known as the progestin component of combined oral contraceptives, progestin-only pills, emergency contraception, and levonorgestrel-releasing intrauterine systems (LNG-IUS).

The proposed link to acne relies on the general pharmacology of combined hormonal contraceptives: the estrogen component raises sex hormone-binding globulin (SHBG), which lowers free (bioavailable) testosterone and can improve androgen-driven acne. However, the evidence pack's own mechanistic analysis flags an important caveat — Levonorgestrel itself has comparatively **high androgenic activity** among progestins (PMID 7825629), and this androgenicity can work *against* the estrogen-driven benefit, or even aggravate acne, unlike lower-androgenicity progestins (e.g., chlormadinone acetate, drospirenone) that are more consistently associated with acne improvement (PMID 15025547, PMID 16796485).

In other words, the predicted association is mechanistically plausible only through the estrogen-partner effect in combination pills, not through a direct antiacne action of Levonorgestrel itself — and the direction of Levonorgestrel's own androgenic activity runs counter to the therapeutic hypothesis. This warrants cautious interpretation rather than treating it as a confirmed mechanistic pathway.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00480532](https://clinicaltrials.gov/study/NCT00480532) | N/A | Completed | 131 | Studied continuous combined oral contraceptives plus doxycycline; doxycycline (an antibiotic also used for acne) was the primary study drug, so the OC/Levonorgestrel contribution to any acne-related outcome is not directly isolated. |
| [NCT05570786](https://clinicaltrials.gov/study/NCT05570786) | Phase 2 | Completed | 100 | Randomized, placebo-controlled trial of a subdermal gestrinone (not confirmed as Levonorgestrel) implant for endometriosis-related pelvic pain; not an acne trial, drug identity needs verification. |
| [NCT00161226](https://clinicaltrials.gov/study/NCT00161226) | N/A | Terminated | 44 | Levonorgestrel-IUS trial for endometrial cancer prevention in obese women; acne appears only as a known side effect of oral progestins mentioned in background text, not a study endpoint. |
| [NCT05492487](https://clinicaltrials.gov/study/NCT05492487) | Phase 2 | Unknown | 60 | Pilot study comparing Mirena (LNG-IUS) vs. megestrol for fertility-sparing treatment of atypical endometrial hyperplasia; unrelated to acne. |
| [NCT01650168](https://clinicaltrials.gov/study/NCT01650168) | N/A | Completed | 101,498 | Large safety cohort comparing nomegestrol acetate/estradiol vs. Levonorgestrel-containing combined oral contraceptives; general safety comparison, not acne-focused. |

**Note:** None of the identified trials directly and primarily test Levonorgestrel for acne as a defined endpoint; relevance is indirect (background mentions or drug-class comparisons).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12196750](https://pubmed.ncbi.nlm.nih.gov/12196750/) | 2002 | RCT | Journal of the American Academy of Dermatology | Placebo-controlled RCT of a low-dose oral contraceptive (20 mcg ethinyl estradiol / 100 mcg Levonorgestrel) reported improvement in moderate acne, attributed to reduced bioavailable androgens. |
| [15025547](https://pubmed.ncbi.nlm.nih.gov/15025547/) | 2004 | Review | Drugs | Ethinylestradiol/chlormadinone acetate was significantly *more* effective than ethinylestradiol/Levonorgestrel (0.03/0.15 mg) for mild-to-moderate papulopustular acne, suggesting Levonorgestrel is a weaker comparator, not a strong standalone option. |
| [6084924](https://pubmed.ncbi.nlm.nih.gov/6084924/) | 1984 | Clinical study | Acta Dermato-Venereologica | Compared serum testosterone/SHBG in acne patients treated with desogestrel- vs. Levonorgestrel-containing oral contraceptives; baseline androgen abnormalities were common, with differing hormonal responses between progestins. |
| [21895044](https://pubmed.ncbi.nlm.nih.gov/21895044/) | 2011 | Review | American Journal of Clinical Dermatology | Reviews hyperandrogenism-driven acne, hirsutism, and hair loss, contextualizing why lower-androgenicity progestins (vs. Levonorgestrel) tend to offer greater dermatological benefit. |
| [7825629](https://pubmed.ncbi.nlm.nih.gov/7825629/) | 1995 | Review | The American Journal of Medicine | Explains that progestins derived from testosterone (including Levonorgestrel) retain relatively higher androgenic activity compared to pregnane-derived progestins — the core mechanistic caveat for this prediction. |
| [16796485](https://pubmed.ncbi.nlm.nih.gov/16796485/) | 2006 | Review | Journal of Women's Health | Compares drospirenone with medroxyprogesterone acetate, Levonorgestrel, and micronized progesterone; drospirenone's antiandrogenic profile was associated with reduced acne occurrence relative to Levonorgestrel. |

---

## Singapore Market Information

Levonorgestrel currently has **no marketed product registration** in Singapore according to the evidence pack (0 registrations; market status: Not Marketed). No authorization records, product names, or approved indication text are available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. *(No key warnings, contraindications, or drug interaction data were retrievable in this evidence pack; the local regulatory label/DDI query returned no results.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case is internally conflicted — Levonorgestrel's relatively high androgenic activity runs counter to the antiacne hypothesis, and the strongest supporting evidence (PMID 12196750, PMID 15025547) shows Levonorgestrel combinations are either modestly effective or *less* effective than lower-androgenicity alternatives. Combined with the blocking data gap on local safety labeling (no HSA/TFDA warnings or contraindications available) and the drug's current non-marketed status in Singapore, there is insufficient basis to advance beyond a research question at this time.

**To proceed, the following is needed:**
- Official package insert / regulatory label data (warnings and contraindications) to clear the blocking safety data gap
- Confirmed mechanism of action data from DrugBank
- A trial or study that isolates Levonorgestrel's own contribution to acne outcomes (separate from its estrogen partner or from comparator progestins)
- Drug-drug interaction (DDI) data, currently not found in the queried source
- Clarification of local regulatory pathway, given the drug is not currently marketed in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

