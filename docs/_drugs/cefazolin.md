---
layout: default
title: Cefazolin
parent: Medium Evidence (L3-L4)
nav_order: 219
evidence_level: L4
indication_count: 10
---

# Cefazolin
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

# Cefazolin: From Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic given by injection, and it is marketed in Singapore. The TxGNN model predicts it may be effective for **infectious otitis media**. The support is thin: **1 clinical trial** and **3 publications** were retrieved, and none directly shows cefazolin treating this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records provided (cefazolin is a first-generation cephalosporin antibacterial) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Cefazolin inhibits bacterial cell-wall synthesis, so activity against gram-positive bacteria is plausible. Detailed mechanism-of-action data is not available in the current record. The link to otitis media rests on this general antibacterial activity, since otitis media is often a bacterial infection.

The mechanistic fit is weak. Cefazolin has poor activity against *Haemophilus influenzae* and *Moraxella catarrhalis*, the main otitis media pathogens. It is also available only as an injection, which is impractical for a condition usually treated as an outpatient.

The very high TxGNN score (0.994) reflects how close cefazolin sits to other cephalosporins in the knowledge graph. It is not clinical evidence of benefit.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2 | Terminated | 520 | Randomized, double-blind, placebo-controlled trial comparing 5-day and 10-day antibiotic courses in children aged 6–23 months with acute otitis media. Cefazolin is not confirmed as the intervention, so this is not direct evidence. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Review | Clinical Pharmacy | Case and literature review of Stevens-Johnson syndrome. It mentions otitis media only as background, so it is of limited relevance. |
| [877649](https://pubmed.ncbi.nlm.nih.gov/877649/) | 1977 | Review | Southern Medical Journal | Overview of cephalosporins in pediatric practice. Notes their activity against gram-positive cocci and some gram-negative bacilli, and their usefulness in penicillin hypersensitivity. |
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case series | Annals of Otology, Rhinology, and Laryngology | Ceftazidime-cefazolin empiric therapy for pediatric Gradenigo syndrome, a rare complication of acute otitis media. This is a complication setting, not routine otitis media. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN14846P | Cefazolin Mevon Powder for Solution for Injection or Infusion 1g/vial | Injection, powder, for solution |
| SIN12471P | Cezolin Injection 1 gm/vial | Injection, powder, for solution |
| SIN07879P | Cefazolin Sandoz 1 g/vial | Injection, powder, for solution |
| SIN14304P | Zepilen Powder for Injection 1g/vial | Injection, powder, for solution |
| SIN15018P | Cefazolin-AFT Powder for Injection 500mg/VIAL | Injection, powder, lyophilized, for solution |

All registered products are injectable.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by graph proximity to other cephalosporins. The single retrieved trial is terminated and does not confirm cefazolin as the intervention. Cefazolin has weak coverage of key otitis media pathogens and is injectable only. HSA package insert data is also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- The HSA package insert (indications, warnings, contraindications)
- Mechanism-of-action data from DrugBank
- Confirmation of whether cefazolin was the intervention in NCT01511107
- A review of cefazolin's coverage of the main otitis media pathogens and whether an injection-only route is workable
- Of the other predicted indications, suppurative otitis media and urinary tract infection are flagged "Research Question", but both overlap cefazolin's established antibacterial use and may not be true repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

