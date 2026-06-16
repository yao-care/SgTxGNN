---
layout: default
title: Codeine
parent: 僅模型預測 (L5)
nav_order: 273
evidence_level: L5
indication_count: 10
---

# Codeine
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

# Codeine: From Cough & Pain Management to Bronchial Disease

## One-Sentence Summary

Codeine is a naturally occurring opioid alkaloid widely used as an antitussive (cough suppressant) and mild-to-moderate analgesic. This multi-indication TxGNN report (10 predicted indications, TW-DB00318-multi) identifies **Bronchial Disease** as the strongest actionable candidate, supported by **5 clinical trials** and **20 publications** — notably including a Phase 4 RCT (n=668) and a 2024 nationwide Korean cohort. The majority of other predicted indications (8 of 10) carry counter-indicative evidence or no mechanistic basis, and should not be pursued.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cough suppression and mild-to-moderate pain management (well-established clinical use; original_indications field empty in regulatory source) |
| Predicted New Indication | Bronchial Disease (Rank 10; strongest actionable evidence in this 10-indication report) |
| TxGNN Prediction Score | 93.66% |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed (0 registered products) |
| Number of Registrations | 0 |
| Recommended Decision | **Proceed with Guardrails** (Bronchial Disease only) |

---

## Multi-Indication Overview

This is a multi-indication report. All 10 TxGNN predictions are ranked below for context before detailed analysis of the best candidate:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Key Issue |
|------|---------|-------------|----------------|----------------|-----------|
| 1 | Nasal Cavity Disease | 99.93% | L5 | Hold | ⚠️ Counter-indicative: literature documents intranasal opioid abuse causing nasal necrosis |
| 2 | Acute Laryngopharyngitis | 99.92% | L5 | Hold | No direct clinical evidence; mechanism is generic opioid inference |
| 3 | Trigeminal Autonomic Cephalalgia | 99.43% | L5 | Hold | ⚠️ Counter-indicative: opioids generally ineffective in cluster headache; risk of medication-overuse headache (MOH) |
| 4 | Allergic Urticaria | 99.37% | L5 | Hold | ⚠️ Counter-indicative: Codeine is a known mast cell trigger causing urticaria, not a treatment |
| 5 | Faucial Diphtheria | 97.63% | L5 | Hold | No biological plausibility; bacterial infection requiring antitoxin + antibiotics |
| 6 | Cervical Disc Degenerative Disorder | 97.40% | L4 | Hold | Class-effect inference only; no Codeine-specific evidence |
| 7 | Papillary Conjunctivitis | 97.17% | L5 | Hold | No mechanistic basis for systemic opioid in local ocular inflammation |
| 8 | Tracheal Disease | 95.70% | L3 | Research Question | Antitussive mechanism applicable; limited indirect evidence |
| 9 | Cold Urticaria | 94.63% | L5 | Hold | ⚠️ Counter-indicative: Codeine used as mast cell degranulation probe, may worsen symptoms |
| **10** | **Bronchial Disease** | **93.66%** | **L2** | **✅ Proceed with Guardrails** | Phase 4 RCT + nationwide cohort directly supporting antitussive use |

> **Important note on Ranks 1, 3, 4, and 9**: These are not simply lacking evidence — the available literature actively documents Codeine as a causative or worsening agent for these conditions. These predictions from TxGNN likely reflect shared biological pathways (e.g., mast cell/opioid receptor interactions) without accounting for the direction of effect.

---

## Why Is This Prediction Reasonable? (Bronchial Disease)

Currently, detailed mechanism of action data is not available from the regulatory data source. Based on well-established pharmacological knowledge, Codeine is an opioid prodrug metabolised to morphine primarily by CYP2D6. It acts on μ-opioid receptors in the medullary cough centre and nucleus tractus solitarius (NTS), suppressing the afferent limb of the cough reflex. This central mechanism reduces cough frequency and severity, and mildly decreases bronchial secretion viscosity.

Bronchial disease — particularly chronic bronchitis and related conditions characterised by persistent pathological cough — is mechanistically aligned with Codeine's established pharmacology. Chronic bronchitis produces cough through persistent airway inflammation and mucus hypersecretion, and the cough reflex itself becomes hypersensitised. Codeine's central antitussive action provides symptomatic relief by raising the threshold for cough initiation. Critically, Codeine has been used for decades as the **gold-standard reference comparator** in antitussive clinical trials, meaning its efficacy in cough suppression relative to bronchial pathology is well characterised in the clinical literature.

However, bronchial disease encompasses a heterogeneous spectrum that includes asthma, where Codeine carries a specific risk: it can provoke bronchospasm via non-immunological histamine release from pulmonary mast cells, and may worsen mucus plugging by impairing ciliary clearance. This distinction between non-asthmatic bronchial disease (where Codeine may be appropriate) and asthma (where it is relatively contraindicated) defines the "guardrails" for any clinical application.

---

## Clinical Trial Evidence (Bronchial Disease)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03738917](https://clinicaltrials.gov/study/NCT03738917) | Phase 4 | Completed | 668 | **Most relevant**: Multicenter pragmatic RCT directly comparing antitussives (including Codeine-class), anticholinergics, and honey vs usual care in adults with uncomplicated acute bronchitis; primary endpoint is cough severity on 7-point Likert scale |
| [NCT02321397](https://clinicaltrials.gov/study/NCT02321397) | Phase 2/3 | Completed | 155 | Double-blind crossover study of oxycodone/naloxone PR at higher doses; evaluates opioid antitussive equivalence — indirect relevance to Codeine class |
| [NCT01438567](https://clinicaltrials.gov/study/NCT01438567) | Phase 3 | Completed | 270 | Parallel-group RCT of oxycodone/naloxone PR vs oxycodone PR for pain patients; demonstrates opioid bowel and analgesic effects — indirect class-level relevance |
| [NCT00513656](https://clinicaltrials.gov/study/NCT00513656) | Phase 2 | Completed | 230 | Safety and efficacy of oxycodone/naloxone combination in chronic cancer pain — indirect relevance for opioid class safety characterisation |
| [NCT02982876](https://clinicaltrials.gov/study/NCT02982876) | N/A | Completed | 50 | Airway stents for excessive dynamic airway collapse RCT — structural airway intervention unrelated to Codeine pharmacology |

> **Quality note**: Only NCT03738917 directly investigates antitussive agents (Codeine class) in bronchial disease. Trials NCT02321397, NCT01438567, and NCT00513656 involve oxycodone, not Codeine, and were retrieved based on respiratory context; their relevance to Codeine-specific repurposing is indirect.

---

## Literature Evidence (Bronchial Disease)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39632868](https://pubmed.ncbi.nlm.nih.gov/39632868/) | 2024 | Nationwide Cohort | Scientific Reports | Korean national health insurance cohort study specifically evaluating chronic Codeine use and its impact on cough-related diseases including COPD, asthma, and allergic rhinitis; defines chronic user threshold as >60 continuous days |
| [6539224](https://pubmed.ncbi.nlm.nih.gov/6539224/) | 1984 | RCT | European Journal of Respiratory Diseases | Plasma kinetics and dose-response antitussive effect of Codeine vs dextromethorphan in 8 patients with pathological cough; establishes comparative pharmacokinetic-pharmacodynamic profile |
| [7626920](https://pubmed.ncbi.nlm.nih.gov/7626920/) | 1994 | Clinical Study | Pulmonary Pharmacology | **Critical safety signal**: Codeine causes dose-dependent bronchoconstriction in asthmatic (but not normal) subjects via putative bronchial opiate receptors; naloxone partially reversible |
| [16428699](https://pubmed.ncbi.nlm.nih.gov/16428699/) | 2006 | Review | Chest | ACCP evidence-based clinical practice guidelines for chronic cough due to chronic bronchitis; discusses role and limitations of antitussive agents including Codeine |
| [20385478](https://pubmed.ncbi.nlm.nih.gov/20385478/) | 2010 | Systematic Review | Respiratory Medicine | Systematic review of 75 trials on pharmacological and non-pharmacological cough interventions in adults with respiratory diseases; majority of evidence in asthma and chronic obstructive conditions |
| [15827540](https://pubmed.ncbi.nlm.nih.gov/15827540/) | 2005 | Review | Minerva Medica | Pathophysiology and therapy of chronic cough; discusses cough plasticity, central sensitisation, and the role of opioid-based antitussives |
| [15553659](https://pubmed.ncbi.nlm.nih.gov/15553659/) | 2004 | Controlled Study | Drugs Under Experimental and Clinical Research | Levocloperastine vs standard antitussives including Codeine; notes emerging evidence that Codeine may not reduce cough frequency during upper respiratory infections |
| [952583](https://pubmed.ncbi.nlm.nih.gov/952583/) | 1976 | Controlled Experimental | Arch Int Pharmacodyn Ther | Antitussive potency comparison: butorphanol shown to be 100× more active than **Codeine** (used as benchmark) in guinea pig and dog models; confirms Codeine's established reference role |
| [19692698](https://pubmed.ncbi.nlm.nih.gov/19692698/) | 2009 | Case Series | New England Journal of Medicine | **Critical safety signal**: Codeine-associated postoperative death in CYP2D6 ultra-rapid metabolizer child; pharmacogenomic risk for excess morphine accumulation |
| [29182956](https://pubmed.ncbi.nlm.nih.gov/29182956/) | 2018 | Cohort | Forensic Science International | Australian cohort study on unintentional mortality from paracetamol/Codeine/doxylamine combination products; characterises misuse demographics and risk factors |

---

## Singapore Market Information

Codeine is currently **not registered or marketed in Singapore**. No HSA license records are available (total_licenses: 0). Any repurposing application would require new product registration with the Health Sciences Authority (HSA) under the Health Products Act.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Extracted from literature evidence** — two clinically significant signals identified in the bronchial disease evidence set:
>
> - **Bronchoconstriction in Asthma (PMID: 7626920)**: Codeine can induce dose-dependent bronchoconstriction in asthmatic subjects via bronchial opiate receptors and mast-cell histamine release. Use in patients with asthma or reactive airway disease requires careful risk-benefit assessment.
>
> - **CYP2D6 Ultra-Rapid Metabolizer Toxicity (PMID: 19692698)**: Patients with CYP2D6 ultra-rapid metabolizer genotype convert Codeine to morphine at supranormal rates, risking fatal opioid toxicity. Pre-treatment pharmacogenomic screening is advisable in applicable populations.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(Bronchial Disease — Rank 10 only)*

**Rationale:**
Codeine's central antitussive mechanism (μ-opioid receptor–mediated cough reflex suppression) provides solid biological plausibility for bronchial disease. Its role as the long-standing gold-standard comparator in antitussive trials, combined with a Phase 4 RCT directly assessing antitussive agents in acute bronchitis and a 2024 nationwide real-world cohort, justifies L2 evidence classification and guarded clinical consideration — particularly for non-asthmatic patients with refractory bronchial cough. All other 9 predicted indications should not be pursued, with Ranks 1, 3, 4, and 9 carrying active counter-indicative evidence.

**To proceed, the following is needed:**

- **Regulatory pathway**: Initiate HSA (Singapore) product registration — Codeine is currently not marketed locally (0 licenses)
- **Data gap resolution — MOA**: Retrieve complete mechanism of action data from DrugBank API (DG002, High severity)
- **Data gap resolution — Safety**: Download and parse TFDA package insert PDF for full warnings and contraindications (DG001, Blocking severity)
- **Patient stratification**: Define exclusion criteria for asthmatic patients and those with reactive airway disease prior to any clinical application
- **Pharmacogenomic risk protocol**: Establish CYP2D6 genotyping or phenotyping protocol to identify ultra-rapid metabolizers before prescribing
- **Addiction and dependence management plan**: Codeine is a Schedule drug in most jurisdictions; a controlled-substance risk mitigation strategy is required
- **Indication specificity**: Narrow "bronchial disease" to a well-defined clinical subpopulation (e.g., chronic bronchitis with refractory dry cough, non-asthmatic) for any formal trial design
- **Ranks 1–9 disposition**: Document formal Hold rationale for all other TxGNN predictions, especially counter-indicative findings for nasal cavity disease, trigeminal autonomic cephalalgia, allergic urticaria, and cold urticaria

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

