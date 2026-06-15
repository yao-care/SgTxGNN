---
layout: default
title: Carbocisteine
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 10
---

# Carbocisteine
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

# Carbocisteine: From Mucolytic Agent to Bronchitis

## One-Sentence Summary

Carbocisteine is a well-established mucoregulatory drug used for respiratory conditions in many countries, though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Bronchitis** — the strongest evidence-backed prediction among all candidates — supported by **1 clinical trial** and **20 publications**, including multiple Cochrane systematic reviews and double-blind RCTs.
Among the 10 TxGNN-predicted indications, bronchitis carries L1 evidence and is the only actionable candidate; the remaining predictions are rated L4–L5 or flagged as knowledge graph artefacts.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not currently registered in Singapore (established use for viscous mucus-associated respiratory disorders in UK, EU, and Japan) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 98.77% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Carbocisteine (S-carboxymethyl-L-cysteine) is a mucoregulatory agent that works through three well-characterised pathways. First, it restructures mucus glycoproteins by downregulating MUC5AC — the gel-forming mucin responsible for the abnormally thick secretions seen in bronchitis — while relatively preserving MUC5B, which has more favourable viscoelastic properties for expectoration. Second, it acts as a direct reactive oxygen species (ROS) scavenger, reducing oxidative stress in inflamed airways. Third, it enhances mucociliary clearance by restoring normal ciliary function, which is impaired in chronic airway disease. Although detailed MOA data are not yet available from DrugBank in this Evidence Pack, the mechanisms above are well-documented in the peer-reviewed literature (e.g., PMID 8500784, PMID 19144049, PMID 15205558).

Bronchitis — both acute and chronic — is characterised precisely by mucus hypersecretion, impaired mucociliary transport, and airway inflammation: the three pathological targets that carbocisteine directly addresses. In chronic bronchitis and COPD, excess MUC5AC production and reduced ciliary beat frequency are central to the cycle of exacerbation and hospitalisation. Carbocisteine's ability to normalise mucus rheology, reduce bacterial airway load (PMID 20807377), and suppress NF-κB-mediated inflammation creates a mechanistic rationale that is among the most coherent of any mucolytic agent.

Carbocisteine has been licensed for respiratory indications in the United Kingdom, France, Japan, and other jurisdictions for decades. Multiple Cochrane systematic reviews and independent RCTs confirm reductions in exacerbation frequency and symptomatic improvement in patients with chronic bronchitis and COPD. The Singapore market, where the drug is currently absent, represents a regulatory white space for an indication that is not novel globally — making the repurposing pathway more a market-entry exercise than a first-in-class development programme.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT02858193](https://clinicaltrials.gov/study/NCT02858193) | Phase 1 | Completed | 30 | 2-way crossover bioequivalence study comparing carbocisteine-L-lysine salt 1.35 g powder for oral solution vs 90 mg/mL syrup in healthy volunteers under fasting conditions; confirmed bioequivalent Cmax and AUC0-t — supports formulation flexibility for market entry |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3907681](https://pubmed.ncbi.nlm.nih.gov/3907681/) | 1985 | RCT (Double-blind, Placebo-controlled) | Br J Clin Pract | Long-term oral carbocisteine vs placebo in chronic bronchitis; direct efficacy endpoint |
| [789027](https://pubmed.ncbi.nlm.nih.gov/789027/) | 1976 | RCT (Double-blind, 3-month) | Chest | n=82 chronic bronchitis patients; S-carboxymethylcysteine reduced sputum viscosity and improved expectoration capacity vs placebo |
| [2099568](https://pubmed.ncbi.nlm.nih.gov/2099568/) | 1990 | Controlled Study (Double-blind) | Respiration | n=24 chronic bronchitis outpatients; single high-dose carbocisteine-lysine produced significant viscosity reductions (−67%) persisting 8 days post-treatment |
| [31107966](https://pubmed.ncbi.nlm.nih.gov/31107966/) | 2019 | Cochrane SR + Meta-analysis | Cochrane Database Syst Rev | Largest pooled analysis (26 studies) of mucolytics vs placebo in chronic bronchitis/COPD; supports reduction in exacerbation frequency with mucolytics including carbocisteine |
| [39413571](https://pubmed.ncbi.nlm.nih.gov/39413571/) | 2024 | Systematic Review | Respiratory Investigation | Most recent meta-analysis of mucolytics in stable COPD; evaluates efficacy and safety endpoints including exacerbation rate |
| [23728642](https://pubmed.ncbi.nlm.nih.gov/23728642/) | 2013 | Cochrane Review | Cochrane Database Syst Rev | Acetylcysteine and carbocysteine for acute RTIs in paediatric patients; safety and efficacy review in children without chronic bronchopulmonary disease |
| [19160217](https://pubmed.ncbi.nlm.nih.gov/19160217/) | 2009 | Cochrane Review | Cochrane Database Syst Rev | Earlier Cochrane edition on carbocisteine for acute RTIs in children; flags limited evidence for acute paediatric use |
| [20956182](https://pubmed.ncbi.nlm.nih.gov/20956182/) | 2010 | Review | Eur Respir Rev | Mucoactive therapy in COPD; reviews carbocisteine evidence including effects on FEV₁ decline, hospitalisations, and mortality risk |
| [30670922](https://pubmed.ncbi.nlm.nih.gov/30670922/) | 2019 | Review | Clin Med Insights ENT | Confirms carbocysteine's well-established status with regulatory approval in multiple countries; notes OTC/prescription availability |
| [18832259](https://pubmed.ncbi.nlm.nih.gov/18832259/) | 2008 | Review | Drug Ther Bull | Compares mucolytics for COPD exacerbations; notes carbocisteine and mecysteine are licensed for long-term use in viscous-mucus respiratory disorders, distinct from erdosteine's short-course licence |

---

## Singapore Market Information

Carbocisteine is not currently registered in Singapore. No product authorisations were found in the Singapore HSA database.

For reference, the drug holds marketing authorisation in the following jurisdictions under the trade name **Mucodyne** (UK), **Rhinathiol** (France), and **Mucosolvan/Mucodyne** (Japan), covering indications including chronic bronchitis, COPD, and upper respiratory tract disorders with viscous secretions.

---

## Safety Considerations

Formal safety data (package insert warnings, contraindications, and drug-drug interactions) are not available for the Singapore context in this Evidence Pack.

> Please refer to the package insert from an approved jurisdiction (e.g., UK SmPC or EU Summary of Product Characteristics) for complete safety information.

**Safety signal from literature:** A case report (PMID 23291681, 2013) documents confirmed carbocisteine-induced pneumonia in a 32-year-old patient with CATCH22 syndrome (DiGeorge/22q11.2 deletion), an immunocompromised condition. Drug-lymphocyte stimulation test was positive. This suggests that patients with primary immunodeficiency or chromosomal deletion syndromes may require additional risk assessment before initiating therapy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Carbocisteine has L1 evidence for bronchitis and chronic obstructive pulmonary disease, supported by multiple Cochrane systematic reviews and double-blind placebo-controlled RCTs spanning four decades. The drug is already licensed in major markets (UK, EU, Japan), meaning safety and efficacy data are accessible through established regulatory filings — significantly lowering the development burden for a Singapore market application.

**To proceed, the following is needed:**

- **Regulatory pathway confirmation:** Engage Singapore HSA to determine whether an abridged NDA (referencing UK/EU approval) or a full submission is required, given the absence of any current Singapore registration
- **Safety dossier extraction:** Obtain the UK SmPC or EU SmPC to formally document contraindications, special population warnings (paediatric, renal impairment, pregnancy), and known drug interactions
- **Drug-drug interaction profile:** Re-query DrugBank API and the WHO DDI database; current DDI search returned zero results, which likely reflects a data gap rather than absence of interactions
- **Paediatric use assessment:** Cochrane reviews (PMID 23728642, 19160217) indicate limited evidence for acute use in children without chronic lung disease; a paediatric risk-benefit statement will be needed for any label targeting this population
- **Formulation decision:** Determine whether to enter the Singapore market as oral syrup, capsule, or granule for oral solution, informed by the bioequivalence data from NCT02858193
- **Immunocompromised population warning:** Incorporate CATCH22 and other primary immunodeficiency conditions as a precautionary contraindication or monitoring requirement, based on PMID 23291681
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

