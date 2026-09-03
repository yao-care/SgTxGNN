---
layout: default
title: Phenylephrine
parent: 僅模型預測 (L5)
nav_order: 779
evidence_level: L5
indication_count: 10
---

# Phenylephrine
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

# Phenylephrine: From Nasal Decongestant/Vasopressor Use to Nasal Cavity Disease

## One-Sentence Summary

Phenylephrine is a classic alpha-1 adrenergic agonist long used clinically as a topical nasal decongestant and as a vasopressor to support blood pressure during anesthesia and surgery.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, with **8 clinical trials** and **8 publications** currently identified as supporting evidence — though much of this evidence documents already-known decongestant/anesthetic-adjunct uses rather than a genuinely novel indication.
Overall evidence quality is moderate (L3): most trials test related agents (oxymetazoline, cocaine, co-phenylcaine) rather than phenylephrine alone, so the signal should be read as reinforcing an existing use rather than opening a new therapeutic area.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no Singapore license record); phenylephrine is broadly recognized clinically as a topical nasal decongestant and intraoperative vasopressor |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, a formal DrugBank-sourced mechanism-of-action record is not available for this candidate (data gap). Based on known pharmacology, phenylephrine is a selective alpha-1 adrenergic receptor agonist that acts on vascular smooth muscle in the nasal mucosa to cause vasoconstriction, reducing mucosal blood flow and congestion. This is a well-established, textbook-level pharmacological effect — which is exactly why the evidence pack's own rationale flags this prediction as essentially reconfirming an already-known class-level use rather than a truly novel repurposing candidate.

Because nasal mucosal vasoconstriction is the direct, intended pharmacological action of phenylephrine, its relevance to "nasal cavity disease" (congestion, mucosal swelling, and the need for a clear surgical/endoscopic field) follows naturally from mechanism rather than requiring a new hypothesis. This is reflected in the supporting literature, where phenylephrine-containing formulations (e.g., co-phenylcaine, Polydexa with phenylephrine) are studied for decongestion and improved visualization prior to nasoendoscopy, sinus surgery, and in the management of rhinosinusitis.

The main caveat is that several of the identified clinical trials test related alpha-agonists (oxymetazoline, cocaine, xylometazoline) as active comparators rather than phenylephrine itself, so trial-level evidence for phenylephrine specifically is thinner than the aggregate count suggests. The strongest direct evidence is the co-phenylcaine (phenylephrine + lidocaine) literature, which is an already-marketed combination product for nasal endoscopy premedication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Phase 4 | Completed | 20 | Compared topical oxymetazoline vs. epinephrine (not phenylephrine itself) for blood loss/visualization before sinus surgery — indirect, same-class evidence |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | H3-antagonist effect on nasal congestion after allergen challenge; phenylephrine not the study drug |
| [NCT04104789](https://clinicaltrials.gov/study/NCT04104789) | Phase 2 | Withdrawn | 0 | Kovanaze (phenylephrine + tetracaine nasal mist) vs. articaine injection for maxillary dental pulpal anesthesia |
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | Completed | 16 | Cocaine vs. lidocaine/xylometazoline vs. saline for intranasal analgesia before awake nasotracheal intubation; phenylephrine not directly tested |
| [NCT02993770](https://clinicaltrials.gov/study/NCT02993770) | N/A | Unknown | 120 | Endoscopic vs. external dacryocystorhinostomy comparison; nasal decongestants used peri-procedurally |
| [NCT03962634](https://clinicaltrials.gov/study/NCT03962634) | Phase 2 | Terminated | 3 | Kovanaze (phenylephrine-containing) vs. articaine for dental pulpal anesthesia (same design as NCT04104789, terminated early) |
| [NCT06457100](https://clinicaltrials.gov/study/NCT06457100) | Phase 1/2 | Active, not recruiting | 60 | Esmolol vs. lidocaine infusion for postoperative recovery quality after FESS; epinephrine/vasoconstrictor use noted as confounder, not primary intervention |
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | N/A | Completed | 106 | Co-phenylcaine (contains phenylephrine) nasal spray vs. nasal nebulization before rigid nasoendoscopy — direct, moderate-relevance evidence for decongestion/visualization |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15854186](https://pubmed.ncbi.nlm.nih.gov/15854186/) | 2005 | RCT | Int J Clin Pract | Double-blind RCT: co-phenylcaine spray vs. placebo before flexible nasendoscopy; minimal pain/discomfort in both groups, no significant difference |
| [25133491](https://pubmed.ncbi.nlm.nih.gov/25133491/) | 2014 | RCT | PLoS ONE | Triple-blind RCT on topical tranexamic acid (not phenylephrine) for bleeding/surgical field quality during FESS — comparator context for nasal cavity surgery |
| [40899890](https://pubmed.ncbi.nlm.nih.gov/40899890/) | 2025 | Experimental + Clinical Safety Study | Vestnik Otorinolaringologii | Safety/efficacy evaluation of Polydexa nasal spray with phenylephrine in acute rhinosinusitis |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | Review | Vestnik Otorinolaringologii | Pathogenetic approach to treating inflammatory diseases of the nose and paranasal sinuses; discusses decongestant drug choice |
| [37184554](https://pubmed.ncbi.nlm.nih.gov/37184554/) | 2023 | Case series | Vestnik Otorinolaringologii | Differential diagnosis of chronic nasal disease after surgery and topical antibiotic therapy, including Polydexa with phenylephrine |
| [9780066](https://pubmed.ncbi.nlm.nih.gov/9780066/) | 1998 | Observational study | Int J Pediatr Otorhinolaryngol | Acoustic rhinometric evaluation of nasal cavity/nasopharynx geometry after adenotonsillectomy |
| [1375136](https://pubmed.ncbi.nlm.nih.gov/1375136/) | 1992 | In vitro mechanistic study | Clin Otolaryngol Allied Sci | Preliminary study of drug effects (including sympathomimetics) on nasal ciliary beat frequency in vitro |
| [7378007](https://pubmed.ncbi.nlm.nih.gov/7378007/) | 1980 | Case report | Arch Ophthalmol | Cocaine and intranasal phenylephrine toxicity reaction during dacryocystorhinostomy |

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug interaction data were available in this evidence pack (Singapore label review is an outstanding, blocking data gap).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The pharmacological rationale for phenylephrine in nasal cavity disease is strong (direct alpha-1 mediated mucosal vasoconstriction), and there is some direct supporting evidence (co-phenylcaine RCT and nasoendoscopy studies), but most identified trials test related alpha-agonists rather than phenylephrine itself, and this candidate substantially overlaps with phenylephrine's already-known decongestant use rather than representing a novel indication.

**To proceed, the following is needed:**
- Singapore (HSA) label warnings and contraindications — currently a blocking data gap (DG001)
- Confirmed DrugBank mechanism-of-action record (DG002)
- Clarification of route compatibility (topical/intranasal vs. systemic) for the target nasal cavity disease population
- A scoping review to separate genuinely new therapeutic claims from restatements of phenylephrine's existing decongestant/vasopressor label, before this candidate is positioned as "repurposing" rather than "existing use confirmation"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

