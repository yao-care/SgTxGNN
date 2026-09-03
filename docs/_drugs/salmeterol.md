---
layout: default
title: Salmeterol
parent: 僅模型預測 (L5)
nav_order: 887
evidence_level: L5
indication_count: 10
---

# Salmeterol
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

# Salmeterol: From Asthma/COPD to Chronic Bronchitis

## One-Sentence Summary

Salmeterol is a long-acting β2-agonist (LABA) bronchodilator with a well-established role in asthma and chronic obstructive pulmonary disease (COPD). The TxGNN model's top prediction is **Bronchitis**, and the extensive clinical evidence behind this signal actually reflects salmeterol's *already-established* use in chronic bronchitis/COPD rather than a genuinely novel indication — supported by **16 clinical trials** and **19 publications**, including several large Phase 3 RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma / Chronic Obstructive Pulmonary Disease (long-acting bronchodilator, LABA) — established global use; not currently registered in Singapore |
| Predicted New Indication | Bronchitis (chronic bronchitis / COPD-associated) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation was not available in the source data. Based on the evidence collected, Salmeterol is a selective, long-acting β2-adrenoceptor agonist (LABA) that relaxes bronchial smooth muscle and improves mucociliary clearance — the standard bronchodilator mechanism underlying treatment of obstructive airway conditions.

The TxGNN model's top-ranked prediction, "Bronchitis," is mechanistically well-founded because salmeterol's core pharmacology directly addresses the bronchospastic and mucus-clearance components of chronic bronchitis and COPD. Notably, the underlying evidence indicates this is **not a novel repurposing hypothesis but confirmation of an already-established indication** — salmeterol (alone and combined with fluticasone as Seretide/Advair) has long been approved internationally for "COPD associated with chronic bronchitis." The high TxGNN score therefore reflects strong, pre-existing pharmacological and clinical alignment rather than a new discovery.

This distinction matters for decision-making: the value of this evidence pack lies less in identifying a new use for salmeterol and more in validating that the knowledge graph correctly recovers known drug-disease relationships — useful context if this candidate is being evaluated for local registration/formulary purposes rather than novel indication expansion.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00064415](https://clinicaltrials.gov/study/NCT00064415) | Phase 3 | Completed | 799 | Long-term (12-month) safety of a LABA in COPD patients |
| [NCT02173691](https://clinicaltrials.gov/study/NCT02173691) | Phase 3 | Completed | 584 | 6-month comparison of tiotropium, salmeterol inhalation aerosol, and placebo in COPD |
| [NCT00268177](https://clinicaltrials.gov/study/NCT00268177) | Phase 3 | Completed | 130 | Salmeterol/fluticasone vs placebo — bronchial anti-inflammatory activity in COPD |
| [NCT00269126](https://clinicaltrials.gov/study/NCT00269126) | Phase 3 | Completed | 150 | 18-week COPD comparison trial with breathing tests and symptom diaries |
| [NCT01110200](https://clinicaltrials.gov/study/NCT01110200) | Phase 4 | Completed | 639 | FSC 250/50 vs salmeterol 50mcg alone on COPD exacerbation rate post-hospitalization |
| [NCT01332409](https://clinicaltrials.gov/study/NCT01332409) | N/A | Completed | 2000 | Post-marketing surveillance of salmeterol/fluticasone (ADOAIR) safety/effectiveness in COPD/chronic bronchitis, with pneumonia as priority endpoint |
| [NCT00633217](https://clinicaltrials.gov/study/NCT00633217) | Phase 4 | Completed | 247 | FSC HFA MDI vs FSC Diskus, indicated for COPD associated with chronic bronchitis |
| [NCT00857766](https://clinicaltrials.gov/study/NCT00857766) | Phase 4 | Completed | 249 | FSC Diskus vs placebo — effect on arterial stiffness in COPD |
| [NCT00269087](https://clinicaltrials.gov/study/NCT00269087) | Phase 3 | Completed | 122 | Long-term (56-week) safety study of salmeterol/fluticasone in COPD (chronic bronchitis, emphysema) |
| [NCT01361984](https://clinicaltrials.gov/study/NCT01361984) | Phase 4 | Unknown | 20 | Nebulized arformoterol vs DPI salmeterol — small-airway opening in COPD |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15970448](https://pubmed.ncbi.nlm.nih.gov/15970448/) | 2006 | RCT | Pulm Pharmacol Ther | Salmeterol improves mucociliary and cough clearance in chronic bronchitis |
| [19124357](https://pubmed.ncbi.nlm.nih.gov/19124357/) | 2008 | RCT | Ther Adv Respir Dis | 12-month safety and tolerance of arformoterol and salmeterol in COPD |
| [9916607](https://pubmed.ncbi.nlm.nih.gov/9916607/) | 1998 | RCT | Clin Ther | Salmeterol vs oral theophylline: efficacy, tolerability, QoL in mild-moderate COPD |
| [12970006](https://pubmed.ncbi.nlm.nih.gov/12970006/) | 2003 | RCT | Chest | Fluticasone/salmeterol Diskus efficacy and safety in COPD |
| [31852314](https://pubmed.ncbi.nlm.nih.gov/31852314/) | 2020 | RCT (Meta-analysis) | J Int Med Res | FP/formoterol vs FP/salmeterol in pediatric asthma |
| [19210134](https://pubmed.ncbi.nlm.nih.gov/19210134/) | 2009 | Cohort | Curr Med Res Opin | Healthcare utilization/costs in chronic bronchitis patients starting FSC vs other maintenance therapy |
| [21225021](https://pubmed.ncbi.nlm.nih.gov/21225021/) | 2010 | Review | Drugs Today | Overview of chronic bronchitis/COPD inflammation and treatment context |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Review/Guideline | Basic Clin Pharmacol Toxicol | Finnish national COPD diagnosis and pharmacotherapy guideline |
| [15329047](https://pubmed.ncbi.nlm.nih.gov/15329047/) | 2004 | Review | Drugs | Salmeterol/fluticasone propionate use in COPD |
| [16915216](https://pubmed.ncbi.nlm.nih.gov/16915216/) | 2006 | Patient experience trial | MedGenMed | Management of COPD associated with chronic bronchitis using FSC 250/50 |

---

## Singapore Market Information

Salmeterol currently has **no registered product authorizations in Singapore** (0 licenses on file; market status: Not Marketed). No dosage form, brand, or approved-indication data is available from the local registry at this time.

---

## Safety Considerations

- **Key Warning (from clinical evidence, class-level):** LABA monotherapy (salmeterol used without an inhaled corticosteroid) in asthma carries a known risk of increased exacerbations and asthma-related death; guideline-supported use requires combination with an inhaled corticosteroid (ICS) as a guardrail.
- Formal package-insert-level warnings, contraindications, and drug-drug interaction data were not available in this evidence pack — please refer to the manufacturer's package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted "Bronchitis" indication is supported by multiple completed Phase 3 RCTs and a large evidence base (L1), but this evidence largely reconfirms salmeterol's already-established role in COPD/chronic bronchitis rather than revealing a novel therapeutic opportunity. The primary guardrail is the LABA monotherapy black-box-level risk in obstructive airway disease, which requires ICS co-administration.

**To proceed, the following is needed:**
- Formal MOA, package insert warnings/contraindications, and DDI data (currently unavailable)
- Local (Singapore) regulatory pathway assessment, since the drug is not currently registered
- Clarification of study intent: if the goal is genuine indication discovery, note that other predicted candidates in this pack (e.g., atopic eczema, perioperative bronchial neoplasm support) are lower-evidence (L4, "Research Question" stage) and would need dedicated mechanistic/clinical validation rather than guardrail-based proceeding
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

