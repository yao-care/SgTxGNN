---
layout: default
title: Nepafenac
parent: High Evidence (L1-L2)
nav_order: 706
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Nepafenac: predicted new indication Eye disease (evidence level L1). Approved use: Not stated in the Singapore licence data. Ocular inflammation and pai…"
monitor_inn: "Nepafenac"
predicted_indications: ["eye disease", "optic papillitis", "hypotrichosis simplex of the scalp", "seborrheic keratosis", "von Hippel anomaly", "congenital hypotrichosis milia", "mcpherson robertson cammarano syndrome", "lagophthalmos", "vulvar inverted follicular keratosis", "vitreous detachment"]
---

# Nepafenac
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

# Nepafenac: From Postoperative Ocular Inflammation to Eye Disease

## One-Sentence Summary

Nepafenac is a topical NSAID prodrug eye drop, marketed in Singapore as Nevanac® 1 mg/ml eye drops suspension. The TxGNN model predicts it may be effective for **eye disease**, a broad category that largely overlaps with its existing use in postoperative ocular inflammation. The data compiled for this report include **40 clinical trials** and **20 publications** for this prediction, so the evidence is strong, although the prediction is closer to an approved use than to true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence data. Ocular inflammation and pain after cataract surgery is the drug's known use. |
| Predicted New Indication | Eye disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in DrugBank. Based on the published literature, nepafenac is a prodrug. Corneal and ocular tissue enzymes convert it to amfenac, which inhibits COX-1 and COX-2. This lowers prostaglandin synthesis, and so reduces ocular inflammation, pain and breakdown of the blood-retinal barrier.

Its use after cataract surgery is well established, and pharmacokinetic work shows that topical dosing delivers amfenac to the back of the eye. The same mechanism supports its use for cystoid and diabetic macular edema. Animal studies also suggest it may inhibit retinal neovascularisation and diabetes-induced retinal microvascular disease.

"Eye disease" is very broad, so this entry mostly reflects an approved use rather than a new one. The label should be narrowed to specific conditions: postoperative inflammation, cystoid macular edema and diabetic macular edema.

Other predictions were also generated, but their support is weak.
- **Optic papillitis:** Evidence is limited to one rabbit study and one indirect trial (L4). Its causes are usually demyelinating or infectious, for which NSAIDs are not standard care.
- **Vitreous detachment:** One Phase 4 biomarker trial in retinal detachment is the only related evidence (L3).
- **Other predictions (ranks 3 to 9):** These have no trials or literature and rest on model output alone (L5).

## Clinical Trial Evidence

Of the 40 trials linked to this prediction, the 10 most relevant are listed here. Many are Phase 3 or Phase 4 trials of nepafenac after cataract surgery.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | Completed | 2120 | Nepafenac 0.3% for prevention and treatment of ocular inflammation and pain after cataract surgery |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | Completed | 1342 | Nepafenac 0.3% vs 0.1% vs vehicle for inflammation and pain after cataract surgery |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | Completed | 881 | Nepafenac 0.3% once daily vs vehicle for clinical outcomes in diabetic patients after cataract surgery |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Phase 3 | Completed | 819 | Companion trial of the same design, in diabetic patients after cataract surgery |
| [NCT03025945](https://clinicaltrials.gov/study/NCT03025945) | N/A | Completed | 662 | Once-daily nepafenac 0.3% vs placebo for preventing pseudophakic cystoid macular edema |
| [NCT03499873](https://clinicaltrials.gov/study/NCT03499873) | Phase 3 | Completed | 448 | Clinical equivalence of generic nepafenac 0.3% vs Ilevro for pain and inflammation after cataract surgery |
| [NCT00782717](https://clinicaltrials.gov/study/NCT00782717) | Phase 2 | Completed | 263 | Nevanac 0.1% vs vehicle for macular edema after cataract surgery in diabetic retinopathy |
| [NCT01426854](https://clinicaltrials.gov/study/NCT01426854) | Phase 3 | Completed | 260 | Nepafenac 0.1% vs placebo for inflammation and pain after cataract surgery in Chinese adults |
| [NCT00333255](https://clinicaltrials.gov/study/NCT00333255) | Phase 3 | Completed | 267 | Nevanac 0.1% vs Acular LS before and after cataract surgery |
| [NCT01021761](https://clinicaltrials.gov/study/NCT01021761) | Phase 4 | Completed | 126 | PGE2 inhibition by Acuvail, Xibrom and Nevanac during phacoemulsification, a direct pharmacodynamic COX readout |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39095467](https://pubmed.ncbi.nlm.nih.gov/39095467/) | 2024 | Systematic review (network meta-analysis of RCTs) | Eye | Compared topical NSAIDs, with or without steroids, for macular thickening and visual outcome after phacoemulsification |
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | RCT | Korean J Ophthalmol | Nepafenac 0.1% vs prednisolone 1% for inflammation control after micro-incisional cataract surgery |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | RCT | Ophthalmology Glaucoma | Nepafenac 0.1% vs prednisolone acetate 1% for inflammation after laser peripheral iridotomy |
| [25686158](https://pubmed.ncbi.nlm.nih.gov/25686158/) | 2015 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Topical NSAIDs for diabetic cystoid macular edema |
| [34210237](https://pubmed.ncbi.nlm.nih.gov/34210237/) | 2022 | Review | Clin Exp Optom | Nepafenac reduces postoperative inflammation and pain and the risk of macular edema, with high ocular penetration |
| [26502088](https://pubmed.ncbi.nlm.nih.gov/26502088/) | 2016 | Review | Dev Ophthalmol | NSAIDs in retinal disease through COX inhibition |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | Preclinical/PK | Exp Eye Res | Topical nepafenac and amfenac reach the posterior segment of the eye |
| [17259381](https://pubmed.ncbi.nlm.nih.gov/17259381/) | 2007 | Preclinical (animal) | Diabetes | Topical nepafenac inhibited diabetes-induced retinal microvascular disease in rats |
| [12506103](https://pubmed.ncbi.nlm.nih.gov/12506103/) | 2003 | Preclinical (animal) | Invest Ophthalmol Vis Sci | Topical nepafenac inhibited ocular neovascularisation in three mouse models |
| [17964407](https://pubmed.ncbi.nlm.nih.gov/17964407/) | 2007 | Case report | J Cataract Refract Surg | Corneal melt associated with nepafenac in a patient with graft-versus-host disease (a safety signal) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13759P | Nevanac® Eye Drops Suspension 1 mg/ml (Novartis Manufacturing NV) | Suspension, sterile | Not stated in the licence data |

## Safety Considerations

- **Corneal toxicity:** A published case report describes corneal melt with nepafenac, and the review literature notes that topical NSAIDs may promote corneal melting or delayed healing in at-risk patients. Corneal condition should be monitored.
- **Knowledge-graph contraindication signals:** The TxGNN knowledge graph links nepafenac to the following conditions. These come from the graph and not from label text, so they must be checked against the package insert.
  - Ocular surface: keratitis, keratoconjunctivitis, dry eye syndrome, xerophthalmia, corneal ulcer.
  - Systemic: rheumatoid arthritis, diabetes mellitus, diabetic ketoacidosis, blood coagulation disease.
- **Drug interactions:** No interaction records were found.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials, including large randomised trials after cataract surgery and in diabetic patients, together with systematic reviews, support nepafenac for postoperative ocular inflammation, pain and macular edema (L1). "Eye disease" is too broad to be a valid indication. The recommendation applies only to specific, well-supported conditions, with corneal safety monitoring.

**To proceed, the following is needed:**
- The approved indication text from the Singapore package insert, to confirm which uses are already authorised.
- The package insert warnings and contraindications, checked against the knowledge-graph signals (especially corneal and ocular surface disease, diabetes and bleeding disorders).
- Narrowing of the target to specific conditions (postoperative inflammation, cystoid macular edema, diabetic macular edema).
- A corneal safety monitoring plan for high-risk patients.
- Mechanism of action data from DrugBank.
- Hold on the other predicted indications. Optic papillitis has indirect evidence only, vitreous detachment awaits results of the biomarker trial, and the remainder have no supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

