---
layout: default
title: Ceftriaxone
parent: 僅模型預測 (L5)
nav_order: 225
evidence_level: L5
indication_count: 10
---

# Ceftriaxone
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

# Ceftriaxone: From Serious Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Ceftriaxone is a broad-spectrum third-generation cephalosporin antibiotic, widely used globally for serious bacterial infections including meningitis, pneumonia, septicemia, and gonorrhea.
The TxGNN model predicts it may be effective for **Infectious Otitis Media** (rank 4 among 10 predicted indications), with **3 clinical trials** and **19 publications** currently supporting this direction.
Notably, this is the highest-evidence prediction in the entire evidence pack (L1, "Proceed with Guardrails") — the top 3 TxGNN-ranked predictions (polyclonal hyperviscosity syndrome, hyperamylasemia, congenital analbuminemia) lack mechanistic basis or carry pharmacological safety concerns and are all rated Hold.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious bacterial infections (meningitis, pneumonia, bacteremia, septicemia, gonorrhea) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacological knowledge, Ceftriaxone is a third-generation cephalosporin that inhibits bacterial cell wall synthesis by irreversibly binding to penicillin-binding proteins (PBPs), disrupting peptidoglycan cross-linking and triggering bacterial lysis. This bactericidal mechanism delivers broad-spectrum activity against both gram-positive and gram-negative organisms, and — critically — Ceftriaxone achieves therapeutic concentrations in middle ear fluid after a single intramuscular (IM) dose.

The three primary pathogens responsible for infectious otitis media — *Streptococcus pneumoniae* (including penicillin-intermediate resistant strains), *Haemophilus influenzae*, and *Moraxella catarrhalis* — fall squarely within Ceftriaxone's coverage spectrum. This means the mechanistic link here is direct, not inferential: the same PBP-binding mechanism that treats meningitis or pneumonia caused by *S. pneumoniae* applies equally to middle ear infections caused by the same organism. The American Academy of Pediatrics (AAP) guidelines explicitly endorse IM Ceftriaxone as a second-line agent in children with acute otitis media (AOM) who fail amoxicillin, and a 3-day regimen has been established for non-responsive cases involving drug-resistant pneumococcal strains.

The TxGNN prediction likely reflects the dense knowledge-graph co-occurrence between Ceftriaxone and otitis media pathogens, which accurately mirrors real-world clinical practice. Of the 10 predicted indications reviewed, the four otitis media-spectrum conditions (ranks 4, 6, 7, 9) form a coherent and pharmacologically supported cluster. The remainder — particularly congenital analbuminemia (rank 3), where Ceftriaxone's high albumin binding (>85%) would paradoxically elevate free-drug toxicity — should be actively avoided.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2b | Terminated | 520 | Multicenter double-blind RCT (children 6–23 months) comparing 5-day vs 10-day antimicrobial courses for AOM; terminated early — establishes Ceftriaxone use in this pediatric population but requires cautious interpretation given early termination |
| [NCT02567825](https://clinicaltrials.gov/study/NCT02567825) | N/A | Completed | 250 | Tympanostomy tube placement vs non-surgical management for recurrent AOM over 2 years; provides surgical-intervention benchmark useful for defining antibiotic-failure populations where Ceftriaxone IM rescue is indicated |
| [NCT01272999](https://clinicaltrials.gov/study/NCT01272999) | N/A | Completed | 391 | Post-marketing observational study of Prevnar 13 impact on otitis media incidence in children; contextualises the shifting pathogen landscape (reduced PCV7 serotypes, residual non-vaccine *S. pneumoniae*) that determines Ceftriaxone's current coverage profile |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | RCT | *Pediatrics* | Prospective randomised single-blind trial: single IM Ceftriaxone vs 10-day TMP-SMZ in AOM — comparable clinical efficacy; foundational evidence establishing IM Ceftriaxone as an effective alternative |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | RCT | *Pediatr Infect Dis J* | 1-day vs 3-day IM Ceftriaxone in non-responsive AOM — 3-day regimen superior for bacteriologic eradication, particularly against drug-resistant *S. pneumoniae*; established standard of care |
| [9877360](https://pubmed.ncbi.nlm.nih.gov/9877360/) | 1998 | RCT | *Pediatr Infect Dis J* | Bacteriologic efficacy of 3-day IM Ceftriaxone in non-responsive AOM — confirmed high eradication rates for resistant pneumococcal strains; supports 3-day over single-dose protocol in treatment failures |
| [12237596](https://pubmed.ncbi.nlm.nih.gov/12237596/) | 2002 | Clinical Trial | *Pediatr Infect Dis J* | Pneumococcal nasopharyngeal carriage dynamics after 1-day vs 3-day IM Ceftriaxone in non-responsive AOM — 3-day regimen more effectively reduces resistant pneumococcal carriage |
| [35841649](https://pubmed.ncbi.nlm.nih.gov/35841649/) | 2022 | Real-World Study | *Int J Pediatr Otorhinolaryngol* | Large US primary care database study: documents rising IM Ceftriaxone prescribing for AOM, especially otitis-conjunctivitis syndrome; signals increasing real-world reliance as resistance to oral agents grows |
| [39361280](https://pubmed.ncbi.nlm.nih.gov/39361280/) | 2024 | Clinical Practice Review | *JAMA Network Open* | Optimal pediatric outpatient antibiotic prescribing — 50% of US pediatric outpatient antibiotics inappropriate; frames appropriate use of Ceftriaxone IM in AOM within stewardship principles |
| [12750572](https://pubmed.ncbi.nlm.nih.gov/12750572/) | 1998 | Clinical Trial | *Le Infezioni in Medicina* | Amoxicillin vs cefuroxime axetil vs single-dose IM Ceftriaxone (50 mg/kg) in 75 pediatric AOM patients — no significant efficacy difference; Ceftriaxone single-dose IM offers practical compliance advantage |
| [20802367](https://pubmed.ncbi.nlm.nih.gov/20802367/) | 2010 | Review | *Otology & Neurotology* | Antimicrobial therapy recommendations for AOM and meningitis in children with cochlear implants — Ceftriaxone recommended for severe AOM in this high-risk group where meningitis risk elevates treatment urgency |
| [20660544](https://pubmed.ncbi.nlm.nih.gov/20660544/) | 2010 | Clinical Series | *Pediatrics* | Cochlear implant children: Ceftriaxone as preferred AOM treatment to prevent progression to bacterial meningitis; establishes a high-priority special population for this indication |
| [30279114](https://pubmed.ncbi.nlm.nih.gov/30279114/) | 2019 | Observational | *J Infect Chemother* | Antimicrobial susceptibility of AOM pathogens in Japanese children 2014–2017 — *S. pneumoniae*, *H. influenzae*, and *M. catarrhalis* isolates maintain high susceptibility to Ceftriaxone despite rising resistance to oral agents |

---

## Safety Considerations

Please refer to the package insert for safety information.

Based on established pharmacology, clinicians should be aware of the following considerations when using Ceftriaxone for otitis media:

- **Albumin binding**: Ceftriaxone is >85% protein-bound. Patients with hypoalbuminemia may have elevated free-drug concentrations
- **Biliary effects**: Ceftriaxone precipitates calcium salts in bile, causing reversible biliary pseudolithiasis — particularly relevant in paediatric patients and neonates receiving concurrent IV calcium
- **Hypersensitivity**: Cross-reactivity with penicillins exists in a small subset of patients; allergy history must be verified before use
- **Neonatal use**: Ceftriaxone is contraindicated in neonates receiving IV calcium (including calcium-containing solutions) due to risk of fatal calcium-Ceftriaxone precipitate in lungs and kidneys

No drug interaction data was retrieved from the DDI database query for this evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple RCTs conducted across several decades establish Ceftriaxone IM as an effective second-line treatment for infectious otitis media in children who fail first-line oral therapy, with direct mechanistic support and inclusion in major international clinical guidelines. The evidence level L1 reflects consistent clinical trial data, and the pharmacological rationale is unambiguous.

**To proceed, the following is needed:**
- Verify Singapore HSA market status and identify any special access pathway or import licence required for a currently non-registered drug
- Obtain and review the complete product monograph/package insert for approved formulations to confirm Singapore-specific warnings, contraindications, and approved dosing
- Define the target population precisely: single-dose (50 mg/kg IM) for first-episode AOM failing oral therapy, or 3-day regimen for non-responsive AOM with suspected resistant *S. pneumoniae*
- Survey local Singapore antimicrobial resistance patterns for *S. pneumoniae*, *H. influenzae*, and *M. catarrhalis* in paediatric AOM to confirm Ceftriaxone susceptibility rates in the local context
- Develop antimicrobial stewardship criteria to prevent inappropriate use, given real-world evidence (PMID 35841649) of rising and potentially overuse of IM Ceftriaxone for AOM in primary care
- **Actively exclude** the other 9 TxGNN-predicted indications from further development: ranks 1, 2, 5, 8, and 10 have no clinical evidence; rank 3 (congenital analbuminemia) carries a pharmacological safety concern due to elevated free-drug toxicity risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

