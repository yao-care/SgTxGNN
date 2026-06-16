---
layout: default
title: Ephedrine
parent: 僅模型預測 (L5)
nav_order: 379
evidence_level: L5
indication_count: 10
---

# Ephedrine
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

# Ephedrine: From Anesthesia Vasopressor to Nasal Cavity Disease

## One-Sentence Summary

Ephedrine is a classic sympathomimetic amine with a century-long history of use as a vasopressor in anesthesia settings and as a bronchodilator — though it currently holds no registered indication in Singapore.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, with **3 directly relevant clinical trials** and **8 publications** retrieved in support, notably including a 1964 clinical study (PMID 14211229) that directly tested Ephedrine hydrochloride in the nasal cavity.
Evidence is rated at **Level L3** (procedural clinical studies and pharmacological animal models), supporting a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Singapore registration; internationally established as vasopressor (anesthesia), bronchodilator, and nasal decongestant |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the regulatory database for Singapore. Based on established pharmacology, Ephedrine is a mixed α- and β-adrenergic agonist naturally derived from the *Ephedra* plant. Its α1-adrenergic receptor activation causes vasoconstriction of nasal mucosal blood vessels, reducing mucosal edema and restoring nasal patency — the classical mechanism underlying nasal decongestants. This is, in fact, one of Ephedrine's most historically documented clinical applications, predating modern selective agents by decades.

The mechanistic pathway is supported at multiple levels. A 1964 clinical study (PMID 14211229) directly documented the combined use of Ephedrine hydrochloride in the nasal cavity. A comparative clinical study (PMID 11345158) demonstrated that structurally related non-selective α-adrenergic agonists measurably alter nasal cavity dimensions as quantified by acoustic rhinometry. Additionally, three pharmacological animal model studies (PMID 12387934, 11895194, 12962193) established validated dog models of nasal congestion specifically designed to characterize nasal decongestant drug action — models in which Ephedrine's drug class served as pharmacological reference.

In current clinical practice, Ephedrine has been largely superseded by more selective topical agents such as oxymetazoline and xylometazoline due to their superior nasal selectivity and reduced systemic effects. The TxGNN prediction is therefore best interpreted not as a novel discovery, but as a re-identification of a pharmacologically sound historical indication in a context where Singapore-registered formulations do not exist — making it a legitimate regulatory and clinical gap worth addressing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01886768](https://clinicaltrials.gov/study/NCT01886768) | N/A | Unknown | 212 | Randomized prospective study comparing single vs. double nasal pledget methods for transnasal endoscopy; Ephedrine is a standard vasoconstricting component in nasal pledgets (cotton packs) used to reduce mucosal bleeding and congestion during nasal procedures |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | Double-blind, four-way crossover study of H3 receptor antagonist (PF-03654746) vs. decongestant comparator for allergen-challenge-induced nasal congestion in seasonal allergic rhinitis; provides benchmark evidence for the nasal decongestant treatment paradigm |
| [NCT03620513](https://clinicaltrials.gov/study/NCT03620513) | Phase 4 | Completed | 160 | Double-blind RCT comparing topical anesthesia vs. decongestant vs. combination pre-treatment for reducing pain during fiberoptic nasal pharyngoscopy; directly evaluates the role of nasal decongestants (Ephedrine class) in ENT procedures |
| [NCT00517946](https://clinicaltrials.gov/study/NCT00517946) | N/A | Completed | 21 | Established MRI as a sensitive quantitative tool for measuring nasal mucosal dimensions in response to anti-allergy drug treatment after intranasal allergen challenge; methodology directly applicable to evaluating Ephedrine nasal decongestant effects |

> **Note:** None of the retrieved trials uses Ephedrine as the primary investigational drug for nasal cavity disease. Most trials address the nasal disease therapeutic area (rhinitis, sinusitis, nasal endoscopic procedures) where adrenergic decongestants — including Ephedrine — appear as procedural adjuncts or reference comparators. This pattern reflects Ephedrine's established role as a class prototype rather than an agent under active clinical development.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [14211229](https://pubmed.ncbi.nlm.nih.gov/14211229/) | 1964 | Clinical Study | Svenska läkartidningen | Earliest direct evidence: experimental clinical testing of Ephedrine hydrochloride combined with N-hydroxyethylpromethazine chloride directly in the nasal cavity; establishes 60+ years of nasal clinical use history |
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | Comparative Clinical Study | Am J Rhinology | Compared nasal decongestant effects of phenylpropanolamine vs. d-pseudoephedrine (same pharmacological class as Ephedrine) using acoustic rhinometry; demonstrated that non-selective α-adrenergic agonists measurably increase nasal cavity cross-sectional area and volume |
| [1541887](https://pubmed.ncbi.nlm.nih.gov/1541887/) | 1992 | Clinical Procedure Study | J Laryngol Otol | Compared nasal packing vs. spraying for pre-operative nasal preparation; Ephedrine is the standard vasoconstricting agent in pre-operative nasal preparation protocols |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Animal Model | J Pharmacol Toxicol Methods | Pharmacological characterization of a noninvasive chronic dog model of nasal congestion; validated as a reproducible tool for studying nasal decongestant drug mechanisms of action |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | Animal Model | Am J Rhinology | Developed acoustic rhinometry-based dog model of nasal congestion using compound 48/80 mast cell degranulation; adrenergic agents used as pharmacological references to validate congestion reversal endpoints |
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | Animal Model | Am J Rhinology | Ragweed-sensitized allergic nasal congestion dog model; acoustic rhinometry validated for quantifying decongestant drug effects in an allergy-driven nasal disease context |
| [11789239](https://pubmed.ncbi.nlm.nih.gov/11789239/) | 2000 | Clinical Observation | Chin J Integr Med | Preliminary clinical observation on Rhinitis Spray (containing adrenergic decongestant components) for chronic rhinitis; reports symptomatic improvement in nasal congestion |
| [8283338](https://pubmed.ncbi.nlm.nih.gov/8283338/) | 1993 | Case Series | Nihon Jibiinkoka Gakkai | Ten cases of congenital nasal stenosis with respiratory distress in neonates; treatment protocols highlight nasal patency as a clinically critical endpoint and the role of vasoactive agents |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ephedrine's α1-adrenergic nasal decongestant mechanism is one of its oldest and best-established pharmacological applications, supported by direct historical clinical evidence from 1964 and a robust body of pharmacological animal model data. However, it is not currently registered in Singapore for any indication, and complete safety data — including warnings, contraindications, and drug interactions — are unavailable from the current evidence pack. The lack of modern RCT evidence specifically positioning Ephedrine against current standard-of-care nasal decongestants (oxymetazoline, xylometazoline) represents the principal evidentiary gap.

**To proceed, the following is needed:**
- Download and parse the Singapore HSA or international package inserts to extract warnings, contraindications, and drug interaction data
- Retrieve Ephedrine's full mechanism of action from DrugBank API (DB01364)
- Conduct a modern head-to-head clinical comparison of Ephedrine vs. current nasal decongestants in a Singapore or regional patient population
- Define the target dosage form and route for the nasal cavity indication (topical nasal drops/spray vs. oral)
- Establish a cardiovascular safety monitoring protocol, given Ephedrine's systemic α/β adrenergic activity (risks: hypertension, tachycardia, CNS stimulation)
- Evaluate rebound congestion risk (rhinitis medicamentosa) with repeated use, which is a known class-effect limitation for nasal decongestants
- Assess regulatory pathway for Singapore HSA registration of a nasal indication, including whether a new registration or label extension would be required
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

