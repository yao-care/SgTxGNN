---
layout: default
title: Tazobactam
parent: 僅模型預測 (L5)
nav_order: 947
evidence_level: L5
indication_count: 10
---

# Tazobactam
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

# Tazobactam: From Beta-Lactamase Inhibitor (Combination Antibacterial Therapy) to Pneumonia

## One-Sentence Summary

> Tazobactam has no independent antibacterial indication — it is a beta-lactamase inhibitor always administered in combination with agents such as piperacillin or ceftolozane to restore activity against beta-lactamase–producing bacteria.
> The TxGNN model predicts these tazobactam-containing combinations may be effective for **Pneumonia** (including hospital-acquired and ventilator-associated bacterial pneumonia),
> with **80+ clinical trials** and **20 publications** currently supporting this direction, several of which are completed Phase 3 head-to-head RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not independently indicated — Tazobactam functions solely as a beta-lactamase inhibitor within fixed-dose combination antibacterials (e.g., piperacillin/tazobactam, ceftolozane/tazobactam) |
| Predicted New Indication | Pneumonia |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L1 |
| Singapore Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Tazobactam itself is not available (registered as a data gap). Based on known pharmacological information, Tazobactam is a beta-lactamase inhibitor with no clinically meaningful antibacterial activity on its own. It is co-formulated with a beta-lactam partner drug — most commonly piperacillin (piperacillin/tazobactam) or ceftolozane (ceftolozane/tazobactam) — to inhibit bacterial beta-lactamase enzymes (including many ESBL and some AmpC enzymes) and thereby restore or extend the antibacterial spectrum of the partner drug against Gram-negative pathogens.

Pneumonia — particularly hospital-acquired bacterial pneumonia (HABP) and ventilator-associated bacterial pneumonia (VABP) — is not truly a "new" indication in the repurposing sense; it is a core, already-approved indication for piperacillin/tazobactam and ceftolozane/tazobactam internationally. The TxGNN prediction is therefore best interpreted as the model correctly recovering an established mechanistic and clinical relationship rather than identifying a novel therapeutic hypothesis. This is reflected in the very high prediction score (99.46%) and the depth of existing Phase 3 RCT evidence.

Mechanistically, the rationale is strong: Gram-negative pathogens implicated in HABP/VABP (e.g., *Pseudomonas aeruginosa*, ESBL-producing Enterobacterales) frequently express beta-lactamases, making beta-lactamase inhibition directly relevant to restoring antibacterial efficacy in the lung. This is corroborated by multiple large, completed, active-comparator Phase 3 trials directly evaluating tazobactam-containing regimens in this population.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Phase 3 | Completed | 537 | Imipenem/cilastatin/relebactam vs piperacillin/tazobactam in HABP/VABP; non-inferiority on all-cause mortality (active comparator design directly evaluating tazobactam combination) |
| [NCT07004049](https://clinicaltrials.gov/study/NCT07004049) | Phase 4 | Recruiting | 600 | TREAT-GNB platform trial evaluating antibiotic strategies (including tazobactam-based regimens) for MDR Gram-negative bloodstream and lower respiratory tract infections |
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Phase 3 | Completed | 726 | Ceftolozane/tazobactam vs meropenem in ventilated nosocomial pneumonia (VABP/HABP); non-inferiority on Day 28 mortality |
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Phase 3 | Completed | 274 | Imipenem/cilastatin/relebactam vs piperacillin/tazobactam in HABP/VABP; multinational confirmatory trial |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Phase 3 | Completed | 460 | Levofloxacin vs piperacillin/tazobactam in mild-to-moderate hospital-acquired pneumonia; non-inferiority in clinical efficacy |
| [NCT04986254](https://clinicaltrials.gov/study/NCT04986254) | N/A | Completed | 179 | Individualized PK-guided dosing regimens (including piperacillin/tazobactam) to optimize antibiotic effectiveness in ICU pneumonia |
| [NCT03897582](https://clinicaltrials.gov/study/NCT03897582) | N/A | Recruiting | 65 | Beta-lactam (including piperacillin/tazobactam) dosing optimization in pneumonia patients on continuous renal replacement therapy |
| [NCT01796717](https://clinicaltrials.gov/study/NCT01796717) | Phase 2/3 | Unknown | 50 | Piperacillin/tazobactam prolonged vs intermittent infusion for nosocomial pneumonia with higher-MIC pathogens |
| [NCT07167524](https://clinicaltrials.gov/study/NCT07167524) | N/A | Not Yet Recruiting | 24 | Dialytic clearance of piperacillin/tazobactam in ICU patients on continuous renal replacement therapy |
| [NCT04352855](https://clinicaltrials.gov/study/NCT04352855) | N/A | Unknown | 55 | Ceftolozane/tazobactam for respiratory infections due to XDR *Pseudomonas aeruginosa* in critically ill patients (retrospective) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30208454](https://pubmed.ncbi.nlm.nih.gov/30208454/) | 2018 | RCT | JAMA | Piperacillin-tazobactam vs meropenem: 30-day mortality in ceftriaxone-resistant *E. coli*/*K. pneumoniae* bloodstream infection |
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | RCT | Lancet Infect Dis | ASPECT-NP: ceftolozane-tazobactam non-inferior to meropenem for nosocomial pneumonia |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | RCT | Clin Infect Dis | RESTORE-IMI 2: imipenem/cilastatin/relebactam vs piperacillin/tazobactam in HABP/VABP |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | RCT | Int J Infect Dis | Phase III noninferiority trial of IMI/REL vs piperacillin/tazobactam in HABP/VABP |
| [32662691](https://pubmed.ncbi.nlm.nih.gov/32662691/) | 2020 | Review | Expert Rev Anti Infect Ther | Ceftolozane/tazobactam for treatment of hospital-acquired pneumonia |
| [35488823](https://pubmed.ncbi.nlm.nih.gov/35488823/) | 2022 | Review | Rev Esp Quimioter | Ceftolozane-tazobactam in nosocomial pneumonia: spectrum and clinical use |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Systematic Review | Int J Antimicrob Agents | PK/PD of novel beta-lactam/beta-lactamase inhibitor combinations for pneumonia caused by carbapenem-resistant Gram-negative bacteria |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Network Meta-Analysis | Clin Microbiol Infect | Empiric antibiotic regimens in non-ventilator HAP: systematic review and network meta-analysis of RCTs |
| [10353303](https://pubmed.ncbi.nlm.nih.gov/10353303/) | 1999 | Review | Drugs | Piperacillin/tazobactam: updated review of use in bacterial infections including lower respiratory tract |
| [34598422](https://pubmed.ncbi.nlm.nih.gov/34598422/) | 2021 | Review | Rev Esp Quimioter | Ceftolozane-tazobactam: when, how, and why to use it |

---

## Singapore Market Information

Tazobactam currently holds **no marketing authorization records in Singapore** (market status: 未上市 / Not Marketed; 0 registrations). No product license table is available for this drug at this time.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data for Tazobactam are currently not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication (pneumonia, including HABP/VABP) is supported by an L1 evidence level, including multiple completed, adequately powered Phase 3 active-comparator RCTs of tazobactam-containing combinations. However, this largely reflects an already-established, approved use of the combination products rather than a genuinely novel repurposing signal, and Tazobactam has no current marketing presence or registration in Singapore.

**To proceed, the following is needed:**
- Resolve blocking data gap: TFDA-equivalent (HSA) package insert warnings/contraindications (currently unavailable, blocks S1 safety screening)
- Obtain formal mechanism-of-action (MOA) documentation via DrugBank API (currently a high-severity data gap)
- Clarify regulatory strategy given zero existing Singapore registrations — determine whether repurposing applies to the combination product (e.g., piperacillin/tazobactam, ceftolozane/tazobactam) rather than tazobactam as a standalone entity
- Confirm route of administration compatibility (IV) and dosing guardrails for the target pneumonia population (route_compatibility data currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

