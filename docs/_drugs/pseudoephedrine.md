---
layout: default
title: Pseudoephedrine
parent: 僅模型預測 (L5)
nav_order: 832
evidence_level: L5
indication_count: 10
---

# Pseudoephedrine
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

# Pseudoephedrine: From OTC Nasal Decongestant to Nasal Cavity Disease

## One-Sentence Summary

Pseudoephedrine is a well-known indirect sympathomimetic amine, globally recognized as an over-the-counter oral decongestant for nasal congestion. The TxGNN model's top prediction — **Nasal Cavity Disease** — largely confirms this already-established pharmacological action rather than identifying a genuinely novel use, and is supported by **2 relevant completed Phase 2 clinical trials** (including one directly testing pseudoephedrine) and **7 literature references**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formal registry text available (drug not currently marketed in Singapore); pseudoephedrine is a globally established OTC oral nasal decongestant (α1-adrenergic agonist) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured MOA data was not available in the registry record, but the evidence pack's mechanistic analysis provides sufficient pharmacological detail: pseudoephedrine is an **indirect sympathomimetic amine** that triggers release of endogenous norepinephrine, which stimulates **α1-adrenergic receptors** on nasal mucosal vascular smooth muscle. This causes vasoconstriction, reducing mucosal swelling and nasal congestion.

Because this is precisely the mechanism underlying pseudoephedrine's long-established use as an OTC decongestant, the TxGNN prediction of "Nasal Cavity Disease" is best understood not as a novel repurposing candidate, but as a **re-confirmation of an already-known indication** via graph-based inference. This is corroborated by two clinical trials with A-grade relevance: NCT00562120 (an H3-antagonist congestion study using acoustic rhinometry as the efficacy endpoint) and NCT00804687 (a head-to-head trial of pseudoephedrine itself against a novel H3-antagonist and placebo in allergic rhinitis), both of which use nasal decongestion/congestion endpoints consistent with pseudoephedrine's established pharmacology.

Nine additional lower-ranked predictions in this evidence pack (e.g., acute laryngopharyngitis, allergic urticaria, trigeminal autonomic cephalalgia, rosacea conjunctivitis, cold urticaria, faucial diphtheria, cervical disc degenerative disorder, massive neonatal aspiration syndrome, bronchial disease) carry substantially weaker evidence (L4–L5, mostly "Hold") and are not developed further in this report; several show clear mechanistic mismatch (e.g., allergic urticaria requires H1-antihistamine activity, not α1-agonism) and are not recommended for advancement.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00804687](https://clinicaltrials.gov/study/NCT00804687) | Phase 2 | Completed | 53 | Randomized, single-dose, double-blind, double-dummy, placebo-controlled 3-way crossover comparing JNJ-39220675, pseudoephedrine, and placebo for allergic rhinitis in an environmental exposure chamber model — direct pseudoephedrine efficacy data. |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | Randomized, double-blind, double-dummy, placebo-controlled 4-way crossover study of an H3-receptor antagonist on nasal congestion after allergen challenge, using acoustic rhinometry — design template typical of decongestant efficacy trials. |
| [NCT00517946](https://clinicaltrials.gov/study/NCT00517946) | N/A | Completed | 21 | MRI-based assessment of anti-allergy drug effects on nasal/sinus mucosal anatomy after intranasal allergen challenge in seasonal allergic rhinitis; drug identity not confirmed as pseudoephedrine specifically. |

*Note: 16 additional trials in the source evidence were graded C (low relevance) or "pending" and are omitted here as they do not directly support the pseudoephedrine–nasal cavity disease link (e.g., surgical, device, probiotic, or unrelated pharmacologic interventions).*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | RCT/Comparative | American Journal of Rhinology | Direct comparison of oral and topical decongestant effects of phenylpropanolamine and d-pseudoephedrine on nasal cavity dimensions using acoustic rhinometry — direct pharmacological evidence for the predicted indication. |
| [22794679](https://pubmed.ncbi.nlm.nih.gov/22794679/) | 2012 | Review | Allergy and Asthma Proceedings | Review of nonallergic rhinitis pathophysiology and treatment context relevant to nasal congestion management. |
| [24492651](https://pubmed.ncbi.nlm.nih.gov/24492651/) | 2014 | Preclinical (animal model) | J Pharmacol Exp Ther | Pharmacological evaluation of selective α2c-adrenergic agonists in animal models of nasal congestion; supports the adrenergic vasoconstriction mechanism class. |
| [19769798](https://pubmed.ncbi.nlm.nih.gov/19769798/) | 2009 | Preclinical (animal model) | American Journal of Rhinology & Allergy | Feline model evaluating decongestant effects of loratadine/montelukast combination with and without D-pseudoephedrine. |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Preclinical (animal model) | J Pharmacol Toxicol Methods | Pharmacological characterization of a dog model of nasal congestion developed for studying decongestant mechanism of action. |

---

## Singapore Market Information

Pseudoephedrine currently has **no marketing authorization registered in Singapore** (`market_status: 未上市`, 0 licenses on file), so no product-level table can be produced from the registry data.

---

## Safety Considerations

Structured safety data (key warnings, contraindications, drug interaction database query) were not available for this record. However, a safety signal was identified during literature review that should be factored into any safety evaluation:

- **Literature Safety Signal**: [PMID 20398975](https://pubmed.ncbi.nlm.nih.gov/20398975/) — a case report describing posterior reversible encephalopathy syndrome (PRES) associated with a cough/cold medication containing pseudoephedrine.

Please refer to the package insert for full safety information once available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top-ranked prediction (Nasal Cavity Disease) is supported by L2-level evidence, including a completed Phase 2 RCT directly testing pseudoephedrine against an active comparator and placebo for nasal congestion — but this largely reconfirms an already well-established pharmacological use rather than revealing a novel indication, and a blocking data gap exists on formal local safety labeling.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: obtain TFDA/HSA package insert warnings and contraindications before any S1 safety assessment
- Resolve high-priority data gap DG002: confirm structured mechanism of action data from DrugBank
- Clarify formal original indication text, since the drug currently has no active Singapore registration
- Evaluate the PRES case report (PMID 20398975) as part of formal safety review
- Confirm whether "Nasal Cavity Disease" should be treated as a novel repurposing target or reclassified as label-confirmatory evidence, given overlap with pseudoephedrine's known OTC use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

