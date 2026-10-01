---
layout: default
title: Tazobactam
parent: High Evidence (L1-L2)
nav_order: 947
evidence_level: L1
indication_count: 10
---

# Tazobactam
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Tazobactam: From Beta-Lactamase Inhibitor Component to Pneumonia

## One-Sentence Summary

Tazobactam is a beta-lactamase inhibitor that is marketed only in fixed combinations with partner beta-lactams such as piperacillin and ceftolozane. The TxGNN model predicts it may be effective for **Pneumonia**, with **50 clinical trials** and **20 publications** retrieved for this direction. Several of these are Phase 3 RCTs, though in most of them tazobactam is part of a combination product or the active comparator.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the source record (all registrations have blank approved-indication text) |
| Predicted New Indication | Pneumonia |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Tazobactam is a beta-lactamase inhibitor. It restores the activity of partner beta-lactams (piperacillin, ceftolozane) against beta-lactamase-producing Gram-negative respiratory pathogens.

Tazobactam is marketed only as part of fixed combinations, so use in pneumonia is effectively an **on-label combination use**, not repurposing in the strict sense. The registry records list no original indications, which is why the prediction looks like a new indication in this dataset.

Phase 3 RCT evidence exists for hospital-acquired and ventilator-associated bacterial pneumonia (HABP/VABP). The main example is ASPECT-NP, which tested ceftolozane-tazobactam against meropenem. Piperacillin-tazobactam also serves as the active comparator in several HABP/VABP trials.

---

## Clinical Trial Evidence

The 10 most relevant of the 50 retrieved trials are listed. Only study designs are summarized here; the Evidence Pack contains no outcome data for these trials.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Phase 3 | Completed | 726 | Ceftolozane/tazobactam vs meropenem in ventilated nosocomial pneumonia; primary endpoint is Day 28 all-cause mortality (non-inferiority) |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Phase 3 | Completed | 537 | Imipenem/relebactam vs piperacillin/tazobactam in HABP/VABP; primary endpoint is all-cause mortality (non-inferiority) |
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Phase 3 | Completed | 274 | Multinational imipenem/relebactam vs piperacillin/tazobactam in HABP/VABP; Day 28 all-cause mortality |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Phase 3 | Completed | 460 | Levofloxacin 750 mg vs piperacillin/tazobactam 4 g/500 mg in mild to moderate hospital-acquired pneumonia; clinical efficacy at test of cure |
| [NCT01796717](https://clinicaltrials.gov/study/NCT01796717) | Phase 2/3 | Unknown | 50 | Prolonged vs regular infusion of piperacillin/tazobactam (4.5 g q6h) in ICU nosocomial pneumonia; clinical and bacteriologic response, PK and safety |
| [NCT03581370](https://clinicaltrials.gov/study/NCT03581370) | Phase 3 | Recruiting | 80 | Short vs prolonged infusion of ceftolozane-tazobactam in *Pseudomonas aeruginosa* VAP; PK exposure comparison |
| [NCT06977347](https://clinicaltrials.gov/study/NCT06977347) | N/A | Not yet recruiting | 100 | Piperacillin/tazobactam alone vs plus a fluoroquinolone in severe community-acquired pneumonia (Korea) |
| [NCT06972537](https://clinicaltrials.gov/study/NCT06972537) | N/A | Recruiting | 42 | Model-guided vs empirical piperacillin-tazobactam dosing in elderly patients with pneumonia |
| [NCT04986254](https://clinicaltrials.gov/study/NCT04986254) | N/A | Completed | 179 | Individualized beta-lactam dosing in ICU pneumonia; supportive PK/PD evidence, no pneumonia efficacy endpoint |
| [NCT01853982](https://clinicaltrials.gov/study/NCT01853982) | Phase 3 | Terminated | 4 | Ceftolozane/tazobactam vs piperacillin/tazobactam in VAP; terminated early with minimal enrollment |

---

## Literature Evidence

The 10 most relevant of the 20 retrieved publications are listed, with RCTs first.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | RCT | Lancet Infect Dis | ASPECT-NP: phase 3, double-blind, non-inferiority trial of ceftolozane-tazobactam vs meropenem in Gram-negative nosocomial pneumonia |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | RCT | Clin Infect Dis | RESTORE-IMI 2: imipenem/cilastatin/relebactam vs piperacillin/tazobactam in HABP/VABP, evaluating efficacy and safety |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | RCT | Int J Infect Dis | Phase 3 non-inferiority trial of IMI/REL vs PIP/TAZ in HABP/VABP in critically ill adults |
| [30208454](https://pubmed.ncbi.nlm.nih.gov/30208454/) | 2018 | RCT | JAMA | Piperacillin-tazobactam vs meropenem for ceftriaxone-resistant *E. coli*/*K. pneumoniae* bloodstream infection (MERINO). This is not a pneumonia trial, but it informs the guardrail on ESBL bacteremia |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Systematic review / network meta-analysis | Clin Microbiol Infect | Network meta-analysis of RCTs comparing empiric antibiotic regimens in non-ventilator HAP |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Systematic review | Int J Antimicrob Agents | PK/PD of novel beta-lactam/beta-lactamase inhibitor combinations for carbapenem-resistant Gram-negative pneumonia |
| [39701120](https://pubmed.ncbi.nlm.nih.gov/39701120/) | 2025 | Cohort | Lancet Infect Dis | CACTUS: retrospective comparison of ceftazidime-avibactam vs ceftolozane-tazobactam in multidrug-resistant *P. aeruginosa* infections |
| [32662691](https://pubmed.ncbi.nlm.nih.gov/32662691/) | 2020 | Review | Expert Rev Anti Infect Ther | Review of ceftolozane-tazobactam for hospital-acquired pneumonia |
| [34598422](https://pubmed.ncbi.nlm.nih.gov/34598422/) | 2021 | Review | Rev Esp Quimioter | Ceftolozane-tazobactam is formally approved for cUTI, cIAI and HABP/VABP |
| [10353303](https://pubmed.ncbi.nlm.nih.gov/10353303/) | 1999 | Review | Drugs | Piperacillin/tazobactam is effective in lower respiratory tract and other bacterial infections |

---

## Singapore Market Information

Six registrations are on file; five are shown below. The source record contains no approved-indication text for any of them.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN15317P | ZERBAXA Powder for Solution for Injection 1G/0.5G (ceftolozane/tazobactam) | Injection, powder, for solution |
| SIN13985P | Piperacillin/Tazobactam Sandoz Powder for Solution for Injection/Infusion 4.5g vials | Powder, for solution |
| SIN13758P | TAZPEN for Injection 4.5g/vial | Injection, powder, for solution |
| SIN15299P | SALATAZ Powder for Solution for Injection/Infusion 4.5G/vial | Injection, powder, for solution |
| SIN15482P | PIPTAZ-AFT Powder for Solution for Injection 4.5G/vial | Injection, powder, lyophilized, for solution |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction records were retrieved for this drug.

One rare literature signal is a 2025 case report of piperacillin-tazobactam-induced hemophagocytic lymphohistiocytosis in a patient with community-acquired pneumonia ([PMID 41305690](https://pubmed.ncbi.nlm.nih.gov/41305690/)). Elevated procalcitonin masked the diagnosis in that case.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
At least two completed Phase 3 RCTs in HABP/VABP involve tazobactam, either as ceftolozane-tazobactam (ASPECT-NP) or as the piperacillin-tazobactam comparator, which supports evidence level L1. Tazobactam is only used in fixed combinations, so this is an on-label combination use, and the model score is high (99.46%). Most trials do not isolate tazobactam's own contribution, and safety screening is incomplete.

**Guardrails:**
- Use only as a combination product.
- Follow antimicrobial stewardship and local resistance data.
- Adjust the dose for renal function.

**To proceed, the following is needed:**
- The Singapore package insert (warnings, contraindications and approved indications) from the HSA website; this is a blocking gap for safety screening.
- Detailed mechanism of action data from DrugBank.
- Outcome results from the Phase 3 trials above (ASPECT-NP and the piperacillin-tazobactam comparator arms), to confirm efficacy in the pneumonia subtypes of interest.

**Other predicted indications:**
- **Urinary tract infection and pyelonephritis:** evidence level L1, also Proceed with Guardrails.
- **Streptococcal pneumonia and bacterial arthritis:** evidence level L4, treated as research questions.
- **Gonococcal urethritis, Ureaplasma urethritis, uterine inflammatory disease, xanthogranulomatous pyelonephritis and urogenital tuberculosis:** Hold.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

