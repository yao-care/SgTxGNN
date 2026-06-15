---
layout: default
title: Betaxolol
parent: 僅模型預測 (L5)
nav_order: 153
evidence_level: L5
indication_count: 10
---

# Betaxolol
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

# Betaxolol: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Betaxolol is a cardioselective beta-1 adrenergic antagonist established globally as a topical ophthalmic treatment for open-angle glaucoma and ocular hypertension, but currently not registered with Singapore's HSA.
The TxGNN model ranks **Primary Hereditary Glaucoma** as its top predicted new indication (score 99.74%), reflecting mechanistic overlap across the glaucoma disease spectrum.
The closely related **Open-Angle Glaucoma** indication cluster (ranks #2–3) is supported by **2 Phase 3 clinical trials** and **19+ publications**, providing L1-level evidence that underpins the rationale for Singapore market entry.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; established globally for open-angle glaucoma / ocular hypertension |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L1 (Open-Angle Glaucoma cluster: ≥2 completed Phase 3 RCTs; direct evidence for primary hereditary glaucoma: L4) |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Betaxolol is a lipophilic beta-1 adrenoceptor antagonist with only weak beta-2 blocking activity. When applied topically to the eye, it lowers intraocular pressure (IOP) by inhibiting β1-adrenergic receptors on the ciliary epithelium, thereby reducing aqueous humor production. This IOP-lowering mechanism is the foundation of its established global use in open-angle glaucoma and ocular hypertension — conditions in which elevated IOP is the primary modifiable risk factor for progressive optic nerve damage. Notably, betaxolol also exhibits calcium channel blocking properties that may confer additional neuroprotection to the optic nerve, an effect not shared by non-selective beta-blockers such as timolol.

Primary hereditary glaucoma (encompassing congenital and juvenile-onset forms driven by MYOC or CYP1B1 mutations) results in structural failure of the trabecular meshwork, leading to impaired aqueous drainage and elevated IOP — a downstream pathophysiology mechanistically analogous to POAG. While surgical goniotomy or trabeculotomy remains the definitive intervention, residual post-operative IOP elevation is common, and adjunctive pharmacological IOP lowering using topical beta-blockers is recognised clinical practice. Betaxolol's β1 selectivity makes it a mechanistically rational candidate for this adjunctive role, particularly in paediatric patients where systemic beta-blocker exposure is a concern.

The TxGNN knowledge graph captures the structural proximity between betaxolol's pharmacological target (β1 adrenergic receptor) and all glaucoma disease nodes, producing high prediction scores across the entire glaucoma spectrum (ranks #1–3 and #6 all fall within the glaucoma family). This is biologically coherent: regardless of glaucoma subtype, the final common pathway of IOP-mediated optic nerve injury and the central role of aqueous humor dynamics remain consistent. The landmark EMGT Phase 3 trial — which directly used betaxolol as its active treatment arm — further demonstrated that IOP reduction causally slows disease progression, providing robust translational support.

---

## Clinical Trial Evidence

No clinical trials specifically targeting primary hereditary glaucoma with betaxolol are currently registered. The following Phase 3 trials from the closely related Open-Angle Glaucoma indication cluster (ranks #2–3) provide the primary evidence base, with directly applicable mechanistic relevance.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02617459](https://clinicaltrials.gov/study/NCT02617459) | Phase 3 | Completed | 366 | Multicenter RCT evaluating levobetaxolol (β-enantiomer of betaxolol) vs. positive control in Chinese patients with POAG or ocular hypertension; demonstrated IOP-lowering safety and efficacy in an Asian population |
| [NCT00000132](https://clinicaltrials.gov/study/NCT00000132) | Phase 3 | Completed (per published results) | N/A | Early Manifest Glaucoma Trial (EMGT) — landmark trial with betaxolol as the active treatment arm; immediate IOP-lowering significantly reduced glaucoma progression risk compared with deferred treatment, establishing the causal IOP–optic nerve relationship |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12365904](https://pubmed.ncbi.nlm.nih.gov/12365904/) | 2002 | RCT | Archives of Ophthalmology | EMGT primary results: IOP reduction via betaxolol reduced OAG progression risk by ~45% vs. no treatment; confirmed IOP lowering as causally protective against optic nerve damage |
| [26526633](https://pubmed.ncbi.nlm.nih.gov/26526633/) | 2016 | Systematic Review & Network Meta-analysis | Ophthalmology | Comparative effectiveness of first-line POAG/OHT medications; ranked betaxolol against prostaglandin analogues, alpha-agonists, and carbonic anhydrase inhibitors across multiple outcomes |
| [40261315](https://pubmed.ncbi.nlm.nih.gov/40261315/) | 2025 | Clinical Review | The Medical Letter on Drugs and Therapeutics | Current drug treatment landscape for open-angle glaucoma; beta-blockers including betaxolol contextualised against contemporary agents |
| [11755834](https://pubmed.ncbi.nlm.nih.gov/11755834/) | 2002 | RCT | American Journal of Ophthalmology | 6-month double-masked RCT: unoprostone vs. timolol vs. betaxolol 0.5% BID in POAG / pseudoexfoliation glaucoma / OHT; established betaxolol as a standard active comparator |
| [7639651](https://pubmed.ncbi.nlm.nih.gov/7639651/) | 1995 | RCT | Archives of Ophthalmology | 1-year double-masked RCT: dorzolamide vs. timolol vs. betaxolol in OAG/OHT; betaxolol arm showed consistent IOP control with well-characterised tolerability profile |
| [3518464](https://pubmed.ncbi.nlm.nih.gov/3518464/) | 1986 | RCT | American Journal of Ophthalmology | 6-month double-masked RCT: betaxolol vs. timolol at 0.25% and 0.5% concentrations in POAG; both significantly reduced IOP from baseline |
| [2898859](https://pubmed.ncbi.nlm.nih.gov/2898859/) | 1988 | RCT | Acta Ophthalmologica | 26-week double-masked RCT: betaxolol vs. timolol in POAG/OHT; mean IOP reduction −6.3 mmHg (betaxolol) vs. −7.2 mmHg (timolol), no statistically significant difference |
| [11039742](https://pubmed.ncbi.nlm.nih.gov/11039742/) | 2000 | RCT | Journal of Glaucoma | Brimonidine 0.2% vs. betaxolol 0.25% BID in OAG/OHT; comparable clinical success rates with quality-of-life assessment favoring brimonidine for certain patient-reported outcomes |
| [2202584](https://pubmed.ncbi.nlm.nih.gov/2202584/) | 1990 | Review | Drugs | Comprehensive pharmacological review: ocular betaxolol reduces IOP by 13–30%, comparable to timolol; β1 selectivity yields better systemic tolerability, particularly in patients with respiratory disease |
| [33126804](https://pubmed.ncbi.nlm.nih.gov/33126804/) | 2020 | Prospective Cohort | Ceska a slovenska oftalmologie | Betaxolol, brimonidine, and carteolol in normal-tension glaucoma; evaluated influence on visual field defect progression over time — particularly relevant given betaxolol's postulated neuroprotective mechanism |

---

## Singapore Market Information

Betaxolol currently has no product authorisations registered with Singapore's Health Sciences Authority (HSA). There are no licensed products to list.

---

## Safety Considerations

> Please refer to the package insert for safety information.

All safety-specific fields (key warnings, contraindications, and drug–drug interactions) are not available in the current Evidence Pack and must be sourced from the official prescribing information (FDA/EMA labelling) prior to any clinical or regulatory application.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Betaxolol holds L1-level evidence for open-angle glaucoma, supported by multiple Phase 3 RCTs (including the landmark EMGT) and systematic reviews spanning over three decades of global clinical use. Its β1-selective pharmacology provides a mechanistically coherent basis for application across the glaucoma spectrum, including primary hereditary glaucoma where adjunctive IOP control is standard post-surgical practice. The current absence of Singapore HSA registration represents a market gap rather than an unresolved safety or efficacy concern.

**To proceed, the following is needed:**
- Retrieve the full FDA/EMA prescribing information for betaxolol ophthalmic formulations to populate the safety, contraindication, and drug interaction sections required for HSA submission
- Obtain detailed MOA documentation from DrugBank (DB00195) to complete the mechanistic rationale for the regulatory dossier
- Conduct a Singapore-specific glaucoma epidemiology and treatment gap assessment to establish unmet clinical need — particularly for patient subgroups (mild-to-moderate asthma, COPD) where betaxolol's β1 selectivity offers a clinical advantage over non-selective beta-blockers such as timolol
- For the primary hereditary glaucoma indication (rank #1): conduct a targeted literature review on betaxolol as adjunctive post-surgical IOP management in paediatric and juvenile glaucoma to determine whether direct evidence can be assembled for an indication-extension application
- Develop a pharmacovigilance plan addressing high-risk populations (cardiac conduction disorders, reactive airway disease, diabetic patients on masking medications)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

