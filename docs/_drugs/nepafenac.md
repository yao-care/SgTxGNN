---
layout: default
title: Nepafenac
parent: 僅模型預測 (L5)
nav_order: 698
evidence_level: L5
indication_count: 10
---

# Nepafenac
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

# Nepafenac: From Post-Cataract Surgery Ocular Inflammation to Eye Disease

## One-Sentence Summary

Nepafenac is a topical ophthalmic NSAID originally developed to treat pain and inflammation after cataract surgery.
The TxGNN model predicts it may be effective more broadly for **Eye Disease**,
with **41 clinical trials** and **20 publications** currently supporting anti-inflammatory activity across a range of ocular conditions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ocular pain and inflammation associated with cataract surgery (per published literature; no local Singapore license on file) |
| Predicted New Indication | Eye disease (broad ophthalmic indication expansion) |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, a structured DrugBank mechanism-of-action record is not available (data gap). Based on information contained in the supporting literature, Nepafenac is a prodrug that, following topical ocular administration, is converted to its active metabolite amfenac, which inhibits both COX-1 and COX-2, thereby suppressing prostaglandin E2 (PGE2) synthesis in ocular tissue (PMID 26474497, 19897019). Its efficacy in preventing and treating inflammation and pain after cataract surgery is well established and forms the basis of its existing global approvals (as Nevanac/Ilevro).

The predicted new indication, "eye disease," is a broad category rather than a narrowly novel target. In practice, the supporting evidence largely reflects the drug's already-known anti-inflammatory role across the eye — extending from cataract-surgery inflammation into related inflammatory/vascular ocular conditions such as diabetic macular edema, uveitis, and post-laser iridotomy inflammation. This should be read as a confirmation and extension of an established pharmacological effect rather than a genuinely new therapeutic hypothesis.

Mechanistically, COX-mediated PGE2 suppression is relevant wherever ocular inflammation or vascular permeability drives disease — this is supported by preclinical work showing topical nepafenac reduces diabetic-retinopathy-related retinal microvascular abnormalities in a rat model (PMID 17259381) and inhibits retinal angiogenesis in vitro (PMID 19897019), lending biological plausibility to indications beyond post-surgical inflammation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | Completed | 2120 | Pivotal registration trial: nepafenac 0.3% for prevention/treatment of ocular inflammation and pain after cataract surgery |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | Completed | 881 | Nepafenac 0.3% QD superior to vehicle in diabetic patients following cataract surgery |
| [NCT00939276](https://clinicaltrials.gov/study/NCT00939276) | Phase 3 | Terminated | 175 | Nepafenac evaluated for macular edema in diabetic retinopathy patients after cataract surgery |
| [NCT00782717](https://clinicaltrials.gov/study/NCT00782717) | Phase 2 | Completed | 263 | Nepafenac vs vehicle for reducing macular edema incidence after cataract surgery in diabetic retinopathy patients |
| [NCT01331005](https://clinicaltrials.gov/study/NCT01331005) | Phase 2 | Completed | 125 | Topical NSAID effect on macular volume in non-central diabetic macular edema (independent of cataract surgery) |
| [NCT00801905](https://clinicaltrials.gov/study/NCT00801905) | Phase 2 | Terminated | 50 | Nepafenac for macular thickening related to pan-retinal photocoagulation in diabetic retinopathy |
| [NCT01939691](https://clinicaltrials.gov/study/NCT01939691) | Phase 4 | Terminated | 9 | Nepafenac vs difluprednate for macular edema in uveitis |
| [NCT02955641](https://clinicaltrials.gov/study/NCT02955641) | N/A | Unknown | 100 | Efficacy/necessity of anti-inflammatory drops (incl. nepafenac) after laser peripheral iridotomy |
| [NCT05847049](https://clinicaltrials.gov/study/NCT05847049) | N/A | Completed | 16 | Combined eplerenone, aflibercept and topical nepafenac for serous foveal detachment in central serous chorioretinopathy |
| [NCT03025945](https://clinicaltrials.gov/study/NCT03025945) | N/A | Completed | 662 | Adjunctive once-daily topical nepafenac 0.3% vs placebo for pseudophakic cystoid macular edema prevention |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24345529](https://pubmed.ncbi.nlm.nih.gov/24345529/) | 2014 | RCT (Phase 3) | J Cataract Refract Surg | Once-daily nepafenac 0.3% effective for preventing/treating ocular pain and inflammation after cataract surgery |
| [22795976](https://pubmed.ncbi.nlm.nih.gov/22795976/) | 2012 | RCT | J Cataract Refract Surg | Prophylactic nepafenac and ketorolac superior to placebo in preventing postoperative macular edema |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | RCT | Ophthalmology Glaucoma | Nepafenac 0.1% vs prednisolone acetate for inflammation control after laser peripheral iridotomy |
| [35196591](https://pubmed.ncbi.nlm.nih.gov/35196591/) | 2022 | RCT | Ophthalmology Glaucoma | Nepafenac 0.1% vs bromfenac 0.09% for inflammation after laser peripheral iridotomy |
| [24345317](https://pubmed.ncbi.nlm.nih.gov/24345317/) | 2014 | RCT | Am J Ophthalmol | Randomized prospective study of nepafenac's effect on intraocular pressure in cataract eyes |
| [39936354](https://pubmed.ncbi.nlm.nih.gov/39936354/) | 2025 | Systematic Review/Meta-analysis | Eur J Ophthalmol | Nepafenac reduces macular swelling and improves visual outcomes after cataract surgery when added to topical steroids |
| [35025078](https://pubmed.ncbi.nlm.nih.gov/35025078/) | 2022 | Review | Drugs | Review of therapeutic agents, including topical NSAIDs, for non-infectious corneal injury |
| [34210237](https://pubmed.ncbi.nlm.nih.gov/34210237/) | 2022 | Review | Clin Exp Optom | Review of nepafenac's role in reducing postoperative inflammation, pain and cystoid macular edema in cataract surgery |
| [17259381](https://pubmed.ncbi.nlm.nih.gov/17259381/) | 2007 | Preclinical | Diabetes | Topical nepafenac inhibits diabetes-induced retinal microvascular disease in a rat model |
| [36573765](https://pubmed.ncbi.nlm.nih.gov/36573765/) | 2023 | Case Report | J Cataract Refract Surg | Case of extreme IOP elevation and steroid-dependent iritis in a patient on chronic topical nepafenac/steroid therapy |

---

## Singapore Market Information

Nepafenac currently has no registered product license in Singapore (0 licenses on file); it is classified as not marketed locally.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Clinical evidence for nepafenac's anti-inflammatory activity across ocular conditions is strong (L1, multiple completed Phase 3 RCTs), but the predicted indication ("eye disease") is broad and substantially overlaps with the drug's already-established use rather than representing a distinct unmet need. More critically, local safety labeling data is a **Blocking** data gap (DG001) that prevents the candidate from entering the S1 safety initial evaluation, and the drug is not currently registered in Singapore.

**To proceed, the following is needed:**
- Local package insert / warnings and contraindications (resolve DG001, Blocking) to enable S1 safety review
- Confirmed DrugBank mechanism-of-action data (resolve DG002)
- A narrower, clinically distinct target indication within "eye disease" (e.g., diabetic macular edema, uveitis, or CSCR) rather than the broad disease category, to support a focused submission
- A Singapore market entry / registration pathway assessment, given zero current local licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

