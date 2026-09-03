---
layout: default
title: Theophylline
parent: 僅模型預測 (L5)
nav_order: 970
evidence_level: L5
indication_count: 10
---

# Theophylline
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

# Theophylline: From Asthma/COPD (Bronchodilator) to Nasal Cavity Disease (Post-Viral Olfactory Dysfunction)

## One-Sentence Summary

> Theophylline is a classical methylxanthine bronchodilator long used for asthma and chronic obstructive pulmonary disease (COPD).
> The TxGNN model predicts it may also be effective for **Nasal Cavity Disease**, specifically post-viral olfactory dysfunction (smell loss),
> with **1 completed Phase 2 clinical trial** and **3 supporting publications** currently available.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in structured regulatory data; classically used as a bronchodilator/anti-inflammatory agent for asthma and COPD |
| Predicted New Indication | Nasal Cavity Disease (post-viral olfactory dysfunction) |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured DrugBank record for this evidence pack. Based on the pharmacological literature reviewed here, Theophylline is a methylxanthine that acts as a non-selective phosphodiesterase (PDE) inhibitor and adenosine receptor antagonist. This mechanism raises intracellular cAMP, producing bronchodilation and anti-inflammatory effects, and is the basis for its long-established use in obstructive airway disease.

The respiratory mucosa (bronchial and nasal) shares overlapping inflammatory and ciliary-function pathways. A completed randomised trial (PMID 9648963) showed that slow-release theophylline reduced the nasal eosinophilic inflammatory response following allergen challenge in patients with allergic rhinitis — directly demonstrating that theophylline's anti-inflammatory action extends to nasal mucosal tissue, not just the lower airway.

Building on this mechanistic bridge, a completed Phase 2 trial (SCENT, NCT03990766) directly tested topical nasal theophylline irrigation for post-viral olfactory dysfunction (smell loss following viral respiratory infection), comparing it against saline placebo over 6 weeks. This represents a genuine repurposing signal — moving from theophylline's classical role as a systemic bronchodilator to a novel topical application targeting nasal mucosal/olfactory recovery — though the trial's small sample size (n=27) limits definitive conclusions.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03990766](https://clinicaltrials.gov/study/NCT03990766) | Phase 2 | Completed | 27 | Nasal theophylline irrigation vs. saline placebo for post-viral olfactory dysfunction; smell function tested before and after 6 weeks of treatment, with monitoring for side effects. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9648963](https://pubmed.ncbi.nlm.nih.gov/9648963/) | 1998 | RCT | European Respiratory Journal | Slow-release theophylline reduced the nasal eosinophilic inflammatory response following allergen challenge in patients with allergic rhinitis, supporting a topical/local anti-inflammatory effect on nasal mucosa. |
| [21139231](https://pubmed.ncbi.nlm.nih.gov/21139231/) | 2010 | Animal Study | Biological & Pharmaceutical Bulletin | Guinea pig asthma model in which antigen passes through the nasal cavity before reaching the lung, supporting the nasal mucosa as a relevant site of allergic/inflammatory signaling in xanthine-responsive airway disease. |
| [11331690](https://pubmed.ncbi.nlm.nih.gov/11331690/) | 2001 | Cohort | Pediatrics | Compares high-flow nasal cannula with nasal CPAP for apnea of prematurity; only tangentially related (nasal airway device study, no direct theophylline-nasal disease link). |

---

## Singapore Market Information

Theophylline currently has **no marketing authorization** on record for this jurisdiction (market status: Not Marketed; total registrations: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: safety warnings, contraindications, and drug-drug interaction data for Theophylline are currently unavailable in this evidence pack — flagged as a blocking data gap (DG001) that must be resolved before any S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
A completed Phase 2 RCT (SCENT trial, n=27) shows a plausible efficacy signal for topical nasal theophylline irrigation in post-viral olfactory dysfunction, mechanistically supported by an earlier RCT demonstrating theophylline's anti-inflammatory effect on nasal mucosa. However, the evidence rests on a single small trial (L2), so it is not yet sufficient to move beyond a research question.

**To proceed, the following is needed:**
- A larger, confirmatory Phase 2/3 RCT of nasal theophylline irrigation for post-viral olfactory dysfunction
- Formal mechanism of action (MOA) data from DrugBank/product labeling (currently a data gap, DG002)
- TFDA/HSA-equivalent package insert warnings, contraindications, and drug interaction data (currently a blocking data gap, DG001) before any safety pre-assessment
- Confirmation of local (Singapore) regulatory pathway, since Theophylline is not currently marketed in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

