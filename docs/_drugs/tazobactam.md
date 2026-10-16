---
layout: default
title: Tazobactam
parent: High Evidence (L1-L2)
nav_order: 957
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Tazobactam: predicted new indication Pneumonia (evidence level L1). Approved use: Bacterial pneumonia, peritonitis, appendicitis…"
monitor_inn: "Tazobactam"
predicted_indications: ["pneumonia", "urinary tract infection (disease)", "gonococcal urethritis", "Ureaplasma urethritis", "bacterial arthritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "urogenital tuberculosis", "streptococcal pneumonia", "pyelonephritis"]
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

# Tazobactam: From Bacterial Pneumonia to Pneumonia (Nosocomial and Ventilator-Associated)

## One-Sentence Summary

Tazobactam is a beta-lactamase inhibitor that is used only in combination with partner beta-lactams (such as piperacillin or ceftolozane), originally for bacterial pneumonia, peritonitis, appendicitis and staphylococcal infections.
The TxGNN model predicts it may be effective for **pneumonia** (top-ranked prediction), with **20 clinical trials** and **20 publications** compiled for this indication.
This is largely an on-label use rather than true repurposing, and all evidence applies to combination products, not tazobactam alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia, peritonitis, appendicitis, Staphylococcus aureus infection (from the knowledge graph; the licence records compiled for this report contain no approved indication text) |
| Predicted New Indication | Pneumonia |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, tazobactam is a beta-lactamase inhibitor. It has no antibacterial activity on its own. It restores the activity of partner beta-lactams (piperacillin, ceftolozane) against ESBL- and AmpC-producing Gram-negative bacteria.

Pneumonia overlaps with the listed original indication of bacterial pneumonia, so this prediction is closer to confirming an existing use than to a genuine repurposing. In the Phase 3 trials, tazobactam is either part of the investigational combination (ceftolozane/tazobactam in ASPECT-NP) or part of the active comparator (piperacillin/tazobactam).

Other predicted indications are listed below for context. Their evidence differs widely.

| Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|
| Urinary tract infection | 99.12% | L1 | Proceed with Guardrails |
| Pyelonephritis | 93.77% | L1 | Proceed with Guardrails |
| Bacterial arthritis | 98.79% | L4 | Research Question |
| Gonococcal urethritis | 98.99% | L4 | Hold |
| Uterine inflammatory disease | 98.66% | L4 | Hold |
| Xanthogranulomatous pyelonephritis | 98.62% | L4 | Hold |
| Streptococcal pneumonia | 94.75% | L4 | Hold |
| Ureaplasma urethritis | 98.99% | L5 | Hold (Ureaplasma lacks a cell wall and is intrinsically resistant to beta-lactams) |
| Urogenital tuberculosis | 94.94% | L5 | Hold (weak mechanistic rationale) |

For urinary tract infection and pyelonephritis, the same caveat applies: the benefit is not tazobactam-specific, and outcomes in ESBL-producing infections compared with carbapenems are inconsistent.

## Clinical Trial Evidence

The most relevant trials for pneumonia are shown below (selected from 20 compiled).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Phase 3 | Completed | 726 | Ceftolozane/tazobactam vs meropenem in ventilated nosocomial pneumonia; primary endpoint Day 28 all-cause mortality (non-inferiority) |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Phase 3 | Completed | 537 | Imipenem/relebactam vs piperacillin/tazobactam in HABP/VABP; piperacillin/tazobactam is the active comparator |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Phase 3 | Completed | 460 | Levofloxacin vs piperacillin/tazobactam in mild to moderate hospital-acquired pneumonia (non-inferiority) |
| [NCT02735707](https://clinicaltrials.gov/study/NCT02735707) | Phase 3 | Recruiting | 20000 | REMAP-CAP adaptive platform trial in community-acquired pneumonia |
| [NCT01853982](https://clinicaltrials.gov/study/NCT01853982) | Phase 3 | Terminated | 4 | Ceftolozane/tazobactam vs piperacillin/tazobactam in VAP; terminated early, no usable efficacy data |
| [NCT03006679](https://clinicaltrials.gov/study/NCT03006679) | Phase 3 | Withdrawn | 0 | Meropenem-vaborbactam vs piperacillin/tazobactam in HABP/VABP; withdrawn, no evidence value |
| [NCT00438269](https://clinicaltrials.gov/study/NCT00438269) | Phase 2 | Completed | 80 | Pilot RCT of appropriate antimicrobial therapy in critical care; tazobactam involvement is indirect |
| [NCT04673175](https://clinicaltrials.gov/study/NCT04673175) | Phase 4 | Terminated | 17 | Ceftolozane-tazobactam for Pseudomonas aeruginosa bacteraemia and pneumonia in haematological malignancy and stem cell transplant patients |
| [NCT04223752](https://clinicaltrials.gov/study/NCT04223752) | Phase 1 | Completed | 41 | Safety, tolerability and pharmacokinetics of ceftolozane/tazobactam in paediatric nosocomial pneumonia |
| [NCT06972537](https://clinicaltrials.gov/study/NCT06972537) | N/A | Recruiting | 42 | Model-guided vs empirical piperacillin/tazobactam dosing in elderly pneumonia patients |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | RCT | Lancet Infect Dis | ASPECT-NP: ceftolozane-tazobactam vs meropenem in Gram-negative nosocomial pneumonia (Phase 3, double-blind, non-inferiority) |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | RCT | Clin Infect Dis | RESTORE-IMI 2: imipenem/cilastatin/relebactam vs piperacillin/tazobactam in HABP/VABP |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | RCT | Int J Infect Dis | Phase 3 non-inferiority trial of imipenem/cilastatin/relebactam vs piperacillin/tazobactam in HABP/VABP |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Systematic review | Clin Microbiol Infect | Network meta-analysis of empiric antibiotic regimens in non-ventilator HAP |
| [36543346](https://pubmed.ncbi.nlm.nih.gov/36543346/) | 2022 | Review | Eur Respir Rev | Overview of newly approved antibiotics for Gram-negative pneumonia |
| [35088403](https://pubmed.ncbi.nlm.nih.gov/35088403/) | 2022 | Review | Semin Respir Crit Care Med | New antibiotics for HAP and VAP |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Systematic review | Int J Antimicrob Agents | Pharmacokinetics and pharmacodynamics of novel beta-lactam/beta-lactamase inhibitor combinations in carbapenem-resistant Gram-negative pneumonia |
| [34871744](https://pubmed.ncbi.nlm.nih.gov/34871744/) | 2022 | Observational | Int J Antimicrob Agents | Cefoperazone-sulbactam vs piperacillin-tazobactam for pneumonia in elderly patients |
| [38902935](https://pubmed.ncbi.nlm.nih.gov/38902935/) | 2024 | Clinical study | In Vivo | Mini-tracheostomy plus tazobactam/piperacillin for preventing pneumonia after oesophageal cancer surgery |
| [35488823](https://pubmed.ncbi.nlm.nih.gov/35488823/) | 2022 | Review | Rev Esp Quimioter | Ceftolozane-tazobactam in nosocomial pneumonia |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15317P | ZERBAXA Powder for Solution for Injection 1g/0.5g | Injection, powder, for solution | Not available in the compiled data |
| SIN13985P | Piperacillin/Tazobactam Sandoz Powder for Solution for Injection/Infusion 4.5g | Powder, for solution | Not available in the compiled data |
| SIN13758P | TAZPEN for Injection 4.5g/vial | Injection, powder, for solution | Not available in the compiled data |
| SIN15299P | SALATAZ Powder for Solution for Injection/Infusion 4.5g/vial | Injection, powder, for solution | Not available in the compiled data |
| SIN15482P | PIPTAZ-AFT Powder for Solution for Injection 4.5g/vial | Injection, powder, lyophilized, for solution | Not available in the compiled data |

A sixth registration, TAZOCIN for Injection 4.5 g/vial (SIN08362P), is also valid. All 6 registrations are active and none has been cancelled.

## Safety Considerations

The knowledge graph links tazobactam-containing products with contraindication relationships to the following conditions. This comes from graph data, not label text, and should be verified against the package insert:

- Kidney disease
- Pyoureter
- Neutropenia and agranulocytosis
- Blood coagulation disease
- Clostridium difficile colitis
- Perinatal necrotizing enterocolitis
- Infectious mononucleosis and chronic Epstein-Barr virus infection syndrome

One review in the compiled literature (PMID 30219824) notes that ceftolozane/tazobactam carries a precautionary statement about reduced clinical response in patients with baseline creatinine clearance of 30–50 mL/min, which may reflect unnecessary dose reduction in acute kidney injury.

No drug interaction data were found. For warnings and contraindications from the approved labelling, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several large Phase 3 RCTs (ASPECT-NP, n=726; RESTORE-IMI 2, n=537) involve tazobactam-containing regimens in nosocomial pneumonia, and the drug is already marketed in Singapore. However, this is largely an existing use, the evidence applies to fixed combinations rather than tazobactam alone, and in several trials piperacillin/tazobactam is the comparator rather than the investigational arm.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (a blocking data gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the Singapore registrations
- Evaluation of the product-specific evidence (piperacillin/tazobactam vs ceftolozane/tazobactam) against local resistance patterns
- Renal function and dosing considerations for critically ill and elderly patients
- For the lower-evidence predictions (gonococcal urethritis, Ureaplasma urethritis, urogenital tuberculosis, streptococcal pneumonia, and others), no further work is advised until supporting data emerge
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

