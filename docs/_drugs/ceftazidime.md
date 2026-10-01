---
layout: default
title: Ceftazidime
parent: Medium Evidence (L3-L4)
nav_order: 223
evidence_level: L4
indication_count: 10
---

# Ceftazidime
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Ceftazidime: From an Unrecorded Original Indication to Hyperamylasemia

## One-Sentence Summary

Ceftazidime is an injectable cephalosporin antibiotic, and its original approved indication is not recorded in the Evidence Pack.
The TxGNN model predicts it may be effective for **hyperamylasemia** (score 99.51%), but **no clinical trials** and only **1 publication** support this direction.
That publication is about routine antibiotics in general and its abstract does not name ceftazidime, so this is a weak, model-driven signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the approved indication text is blank in all Singapore licences) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Ceftazidime is a beta-lactam antibiotic, but its recorded original indication is blank, so the link to the new indication cannot be assessed directly.

Hyperamylasemia (raised blood amylase) is a laboratory finding rather than an infection. It is often linked to pancreatic inflammation. The only supporting signal is a 2001 paper suggesting that routine antibiotic prophylaxis reduced pancreatitis after ERCP (endoscopic retrograde cholangiopancreatography). If an antibiotic lowered amylase in that setting, it would be by preventing infection or inflammation, not through a ceftazidime-specific action. The paper's title does not mention ceftazidime, so its relevance must be confirmed from the full text.

There is no plausible direct mechanism, and the high score may partly reflect a knowledge-graph association rather than pharmacology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11985972](https://pubmed.ncbi.nlm.nih.gov/11985972/) | 2001 | Unclassified (possibly a prophylaxis RCT) | J Gastrointest Surg | Prospective study of routine antibiotics to reduce post-ERCP pancreatitis. Ceftazidime is not named in the title, and the abstract available here is truncated. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15074P | Ceftazidime Kabi Powder for Solution for Injection 1g/vial | Injection, powder, for solution | Not stated in the record |
| SIN14738P | Ceftazidime Mevon Powder for Solution for Injection or Infusion 1g/vial | Injection, powder, for solution | Not stated in the record |
| SIN15075P | Ceftazidime Kabi Powder for Solution for Injection 2g/vial | Injection, powder, for solution | Not stated in the record |
| SIN11470P | Cefazime for Injection 1g/vial | Injection | Not stated in the record |

All four products are injectables.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on one indirect 2001 paper about antibiotics in general and has no registered trials. Any amylase effect would be secondary to infection control rather than a drug-specific action, so the evidence is insufficient to advance.

**To proceed, the following is needed:**
- Full text of PMID 11985972 to confirm whether ceftazidime was used and what happened to amylase levels
- Ceftazidime's original approved indications and mechanism of action (e.g. from DrugBank), which are currently missing
- HSA package insert warnings and contraindications, currently a blocking gap for safety screening
- A clear clinical rationale for treating a laboratory finding (hyperamylasemia) rather than an underlying condition

**Note:** Other predictions for this drug have stronger evidence than the top-ranked one. Urinary tract infection (rank 4) has Phase 2 trials, mostly of ceftazidime-avibactam. Infectious otitis media (rank 9) has several small clinical studies of ceftazidime in Pseudomonas-related chronic suppurative otitis media. These may deserve their own evaluations.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

