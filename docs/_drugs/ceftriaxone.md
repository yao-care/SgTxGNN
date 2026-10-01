---
layout: default
title: Ceftriaxone
parent: Low Evidence (L5)
nav_order: 225
evidence_level: L5
indication_count: 10
---

# Ceftriaxone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Ceftriaxone: From Antibacterial Therapy to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Ceftriaxone is a third-generation cephalosporin antibiotic. The registration data supplied do not state its approved indications.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** support this, and the pack's own mechanistic review calls the high score a graph-proximity artifact.
Of the other predicted indications, only the otitis media group has meaningful evidence, and that is likely an established use rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the local registration data (the approved indication text is empty for all listed licenses) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.39% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

It is not, based on the available information. Ceftriaxone is a bactericidal beta-lactam that inhibits penicillin-binding proteins and blocks bacterial cell wall synthesis. It has no known effect on serum viscosity or on excess immunoglobulin, which is the underlying problem in polyclonal hyperviscosity syndrome.

The 99.39% score most likely reflects proximity in the knowledge graph rather than a real biological link. The condition is neither an infection nor a target of an antibacterial. Detailed mechanism-of-action data from DrugBank are not currently available, but the known pharmacology gives no reason to expect a benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other Predicted Indications Worth Noting

The top-ranked prediction has no support, but several lower-ranked predictions have more substantial evidence. All of them concern otitis media.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 4 | Infectious otitis media | 99.26% | L2 | Two randomized trials support efficacy in acute otitis media. This is probably an established use, and the empty original-indication field is likely a data gap. |
| 6 | Suppurative otitis media | 99.02% | L3 | Only a small 1989 comparative study supports acute use. The rest is microbiology surveillance. |
| 7 | Chronic otitis media | 99.01% | L4 | Indirect evidence only. Ceftriaxone is a weak choice for Pseudomonas and biofilm organisms, and topical therapy is standard. |
| 9 | Middle ear disease | 98.99% | L3 | A broad parent category. The registered trials cannot be tied to ceftriaxone. |

Key publications for the rank 4 and rank 6 candidates:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | RCT | Pediatrics | Single intramuscular ceftriaxone dose compared with 10 days of oral TMP-SMX in acute otitis media |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | RCT | Pediatr Infect Dis J | One-day vs three-day intramuscular ceftriaxone in nonresponsive acute otitis media in children |
| [2523493](https://pubmed.ncbi.nlm.nih.gov/2523493/) | 1989 | Clinical study | Jpn J Antibiot | Ceftriaxone 1 g once daily compared with cefotiam in acute suppurative otitis media and acute exacerbation of chronic suppurative otitis media (efficacy 71% vs 86%) |

The remaining candidates are hyperamylasemia (rank 2), congenital analbuminemia (rank 3), blood group incompatibility (rank 5), premalignant hematological system disease (rank 8) and otosalpingitis (rank 10). All have L5 or minimal evidence and no plausible mechanism, so they stay at Hold.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15008P | Ceftriaxone Kabi Powder for Solution for Injection 1g/vial | Injection, powder, for solution | Not listed in the data |
| SIN16822P | Ceftriaxone Advagen Powder for Solution for Injection 2g/vial | Injection, powder, for solution | Not listed in the data |
| SIN15207P | Ceftriaxone-AFT Powder for Injection 0.5g/vial | Injection, powder, for solution | Not listed in the data |
| SIN16113P | Cyrosef Powder for Solution for Injection 2gm | Injection, powder, for solution | Not listed in the data |
| SIN11104P | Cefaxone for Injection 1 g/vial | Injection, powder, for solution | Not listed in the data |

All listed products are injectable powders.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, polyclonal hyperviscosity syndrome, has no trials, no literature and no plausible mechanism, so the score is not credible. The only well-supported direction is acute otitis media, which is likely an existing use rather than a new one.

**To proceed, the following is needed:**
- Approved indications for the Singapore-registered products, taken from the HSA package inserts, to confirm whether otitis media is already labeled
- Safety information from the package insert (warnings, contraindications), which is currently missing
- For the otitis media direction, a check of current guideline positioning (typically second-line, for treatment failure or when oral therapy is not possible), and a review of the trial phase and design of the supporting RCTs
- Mechanism-of-action data from DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

