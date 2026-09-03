---
layout: default
title: Oxymetazoline
parent: 僅模型預測 (L5)
nav_order: 743
evidence_level: L5
indication_count: 10
---

# Oxymetazoline
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

# Oxymetazoline: From Nasal Congestion (OTC Decongestant) to Nasal Cavity Disease

## One-Sentence Summary

Oxymetazoline is a topical α1/α2-adrenergic agonist long used as an OTC nasal decongestant for symptomatic nasal congestion. The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, with **17 clinical trials** and **5 publications** currently associated with this indication — though, as the evidence itself notes, this prediction largely reconfirms the drug's already-established mechanism rather than identifying a truly novel use. The drug is not currently registered or marketed in Singapore.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Nasal congestion (topical OTC decongestant use) — no formal Singapore registration record available |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data for oxymetazoline is not available in this evidence pack (original_moa is a data gap). However, the evidence pack's own repurposing rationale confirms that oxymetazoline is a topical α1/α2-adrenergic receptor agonist that produces direct vasoconstriction of the nasal mucosa, reducing mucosal swelling and congestion — this is the well-established pharmacological basis of its use as an OTC nasal decongestant.

Because "Nasal Cavity Disease" is a broad diagnostic category that includes congestion, rhinitis, and related mucosal conditions, this predicted indication sits very close to the drug's already-known clinical use rather than representing a genuinely new therapeutic area. The evidence pack explicitly flags this: the mechanistic link is described as "an extension of an existing use rather than a true repurposing candidate — low novelty, but the mechanism is the best-supported of all predictions in this set."

This is reinforced by the related rank-9 prediction (nasopharyngitis), which shares the identical vasoconstriction/decongestant mechanism and is described as the "typical extension application" of oxymetazoline as an OTC cold/nasopharyngitis decongestant, even though no direct trials or literature were retrieved for that specific term in this dataset.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Phase 4 | Completed | 20 | Topical 0.05% oxymetazoline vs. 1:1000 epinephrine before endoscopic sinus surgery — direct comparison of effect on blood loss and surgical visualization |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | Randomized, double-blind, placebo-controlled, 4-way crossover study of nasal congestion following allergen challenge in seasonal allergic rhinitis |
| [NCT04104789](https://clinicaltrials.gov/study/NCT04104789) | Phase 2 | Withdrawn | 0 | Kovanaze (tetracaine + oxymetazoline) nasal mist vs. articaine injection for dental pulpal anesthesia |
| [NCT03962634](https://clinicaltrials.gov/study/NCT03962634) | Phase 2 | Terminated | 3 | Same Kovanaze (tetracaine + oxymetazoline) vs. articaine comparison, terminated early |
| [NCT01411969](https://clinicaltrials.gov/study/NCT01411969) | N/A | Completed | 16 | Acoustic rhinometry of nasal cavities after decongestion with 0.05% oxymetazoline aerosol spray |
| [NCT03620513](https://clinicaltrials.gov/study/NCT03620513) | Phase 4 | Completed | 160 | Double-blind study of topical anesthesia and/or decongestant pretreatment for comfort during fiberoptic nasal pharyngoscopy/laryngoscopy |
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | N/A | Completed | 106 | Comparison of co-phenylcaine nasal spray vs. nasal nebulization for decongestion/anesthesia before rigid nasoendoscopy |
| [NCT01974726](https://clinicaltrials.gov/study/NCT01974726) | N/A | Terminated | 95 | Evaluation of Eustachian tube function tests in children/adults with middle-ear disease |
| [NCT07021040](https://clinicaltrials.gov/study/NCT07021040) | N/A | Recruiting | 125 | Collection and analysis of human olfactory lining biopsies from the nasal cavity in health and disease |
| [NCT06457100](https://clinicaltrials.gov/study/NCT06457100) | Phase 1/2 | Active, not recruiting | 60 | Perioperative esmolol vs. lidocaine infusion for recovery quality after functional endoscopic sinus surgery |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9929658](https://pubmed.ncbi.nlm.nih.gov/9929658/) | 1998 | Cohort | Ann NY Acad Sci | Olfactory function assessment (CSERP, psychophysical testing, acoustic rhinometry) in acute rhinitis |
| [8615587](https://pubmed.ncbi.nlm.nih.gov/8615587/) | 1996 | Animal/Preclinical | Ann Otol Rhinol Laryngol | Topical oxymetazoline nose drops evaluated for effect on early local tissue defense in experimental bacterial sinusitis (rabbit model) |
| [25496205](https://pubmed.ncbi.nlm.nih.gov/25496205/) | 2015 | Cohort | J Plast Surg Hand Surg | Acoustic rhinometry evaluation of nasal patency after repair of unilateral cleft lip and palate |
| [28490409](https://pubmed.ncbi.nlm.nih.gov/28490409/) | 2017 | Case Series | Am J Rhinol Allergy | Endoscopic-guided coblation treatment of nasal telangiectasias in hereditary hemorrhagic telangiectasia |
| [38024464](https://pubmed.ncbi.nlm.nih.gov/38024464/) | 2023 | Case Report | Global Pediatr Health | Case report of rhinoscleroma (nasal cavity granulomatous disease) in a 9-year-old boy |

---

## Singapore Market Information

Oxymetazoline is currently **not marketed** in Singapore — no HSA registration records were found in this evidence pack (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism (topical α1/α2-adrenergic vasoconstriction) is well-supported and one Phase 2 double-blind, placebo-controlled RCT plus one completed Phase 4 comparative trial directly evaluate oxymetazoline's decongestant effect in nasal/sinus contexts, justifying an L2 evidence level. However, the predicted indication overlaps substantially with the drug's existing known use rather than representing a novel therapeutic direction, and the drug has no current Singapore registration.

**To proceed, the following is needed:**
- Detailed mechanism of action (MOA) documentation from DrugBank
- TFDA/HSA package insert warnings and contraindications (currently a blocking data gap)
- Formal drug interaction (DDI) data (current query returned no results)
- A regulatory pathway assessment for Singapore market entry, since the drug is currently unregistered
- Clarification on whether this candidate should be reclassified as "existing indication confirmation" rather than "new indication repurposing" given the low novelty noted in the evidence rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

