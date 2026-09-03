---
layout: default
title: Rifampicin
parent: 僅模型預測 (L5)
nav_order: 857
evidence_level: L5
indication_count: 10
---

# Rifampicin
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

# Rifampicin: From Antibacterial Therapy to Conjunctivitis

## One-Sentence Summary

Rifampicin is a rifamycin-class antibacterial classically used against mycobacterial infections such as tuberculosis and leprosy.
The TxGNN model predicts it may also be effective for **Conjunctivitis**,
but currently **0 clinical trials** and only **20 (mostly historical or susceptibility) publications** support this direction, with no dedicated modern efficacy studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the evidence pack (regulatory data gap). Rifampicin is generally recognized as a rifamycin-class antibacterial used for tuberculosis and leprosy multidrug therapy. |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (DG002, High severity data gap). Based on known pharmacology, Rifampicin is a rifamycin antibacterial that inhibits bacterial DNA-dependent RNA polymerase, and it has documented in vitro and historical clinical activity against *Chlamydia trachomatis* — the causative organism of trachoma, a chronic form of follicular conjunctivitis endemic in parts of Africa and Asia.

The mechanistic link between the original antibacterial use and the predicted indication is therefore biologically plausible but narrow: the supporting literature is concentrated on **trachoma** (chlamydial conjunctivitis) rather than the far more common causes of acute bacterial conjunctivitis (e.g., *Staphylococcus*, *Streptococcus*, *Haemophilus*, *Moraxella*). Most of the remaining evidence consists of pathogen susceptibility surveys and case reports describing incidental conjunctivitis in patients treated with rifampicin for unrelated conditions (leprosy, TB, cat-scratch disease), rather than trials designed to test rifampicin as a conjunctivitis treatment.

Overall, the prediction is mechanistically defensible for a chlamydial/trachoma subtype of conjunctivitis, but the evidence base is old (largely 1970s–1990s), indirect, and does not reflect current standard-of-care ophthalmic antibiotic therapy. This supports a cautious "Hold" rather than progression to development planning.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1096630](https://pubmed.ncbi.nlm.nih.gov/1096630/) | 1975 | Clinical Trial (historical) | American Journal of Ophthalmology | Controlled trial in Tunisian schoolchildren comparing 1% rifampicin ointment vs. tetracycline vs. boric acid for endemic trachoma; rifampicin showed antichlamydial activity comparable to tetracycline. |
| [6635446](https://pubmed.ncbi.nlm.nih.gov/6635446/) | 1983 | Review | Reviews of Infectious Diseases | Rifampicin is the most potent antibiotic by weight against *Chlamydia trachomatis*; as effective as tetracyclines for topical trachoma treatment, though resistance can emerge rapidly. |
| [5411121](https://pubmed.ncbi.nlm.nih.gov/5411121/) | 1970 | Preclinical | Nature | Early report of anti-trachoma activity of rifampicin and rifamycin SV derivatives, establishing the pharmacological rationale later tested clinically. |
| [15228931](https://pubmed.ncbi.nlm.nih.gov/15228931/) | 2004 | Review | Anales de Pediatría | Review of the most prevalent bacterial pathogens causing conjunctivitis and their antibiotic sensitivity patterns; contextualizes where rifampicin-susceptible organisms fit. |
| [10537781](https://pubmed.ncbi.nlm.nih.gov/10537781/) | 1999 | Review | Current Opinion in Ophthalmology | Review of ocular manifestations of cat-scratch disease (Bartonella henselae), a rare cause of conjunctivitis sometimes co-managed with rifampicin-containing regimens. |
| [33457332](https://pubmed.ncbi.nlm.nih.gov/33457332/) | 2020 | Cohort/Susceptibility | Advanced Biomedical Research | Bacterial etiology and antibiotic susceptibility survey of conjunctivitis isolates in Iran; informs which pathogens remain rifampicin-susceptible. |
| [30347565](https://pubmed.ncbi.nlm.nih.gov/30347565/) | 2018 | Susceptibility Study | Chinese Journal of Ophthalmology | Genetic typing and antibiotic susceptibility of *Staphylococcus aureus* strains from keratitis/conjunctivitis patients. |
| [21484175](https://pubmed.ncbi.nlm.nih.gov/21484175/) | 2011 | Susceptibility Study | Journal of Ophthalmic Inflammation and Infection | Bacteriologic and plasmid analysis of conjunctivitis etiologic agents in Lagos, Nigeria, including antibiotic resistance profiling. |
| [8363150](https://pubmed.ncbi.nlm.nih.gov/8363150/) | 1993 | Cohort/Susceptibility | Anales Españoles de Pediatría | Microbiologic study of neonatal conjunctivitis showing high antibiotic sensitivity among isolated organisms, except to penicillin. |
| [14686993](https://pubmed.ncbi.nlm.nih.gov/14686993/) | 2003 | Case Report | Clinical Microbiology and Infection | Case of primary meningococcal conjunctivitis successfully treated with topical antibiotics followed by systemic rifampin (used for meningococcal eradication, not primary ocular therapy). |

---

## Singapore Market Information

Rifampicin currently has **no product registration in Singapore** (market status: Not Marketed, 0 licenses on file). No authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data were not available in the evidence pack — this is flagged as a Blocking data gap, DG001, requiring TFDA/HSA label retrieval before any safety-sensitive decision can be made.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported only by L4-level evidence — no clinical trials, and literature consisting mainly of decades-old trachoma studies, pathogen susceptibility surveys, and incidental case reports rather than trials designed to test rifampicin for conjunctivitis. Combined with a Blocking safety data gap (no TFDA/HSA label data) and the drug's non-marketed status in Singapore, the evidence does not support progression past initial screening.

**To proceed, the following is needed:**
- Package insert / regulatory label data (warnings, contraindications, DDI) to clear the Blocking data gap (DG001)
- Confirmed mechanism of action documentation from DrugBank (DG002)
- Modern controlled trial data specifically testing rifampicin (systemic or topical) against common bacterial or chlamydial conjunctivitis pathogens
- Clarification of target sub-indication (trachoma/chlamydial conjunctivitis vs. general bacterial conjunctivitis), since current evidence supports only the former
- Route/formulation feasibility assessment (historical evidence used topical ointment; current available routes are undetermined — `route_compatibility.status: pending`)

**Note on other TxGNN candidates in this evidence pack:** Several other predicted indications for rifampicin (multiple endocrine neoplasia, the rare neurodevelopmental disorder, feline AIDS, SIV infection) are flagged in the source data as knowledge-graph artifacts with no plausible mechanistic link and should not be pursued. HIV infectious disease (rank 5) is also a mismatch — its supporting trials are drug-drug interaction/TB-co-treatment studies, not evidence of anti-HIV activity. Of the ten candidates screened, **rheumatoid arthritis** (rank 7) has the most substantive human trial history (multiple small RCTs from 1988–1993, L2 evidence) and may warrant a separate, dedicated evaluation if this program is expanded beyond the top-ranked candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

