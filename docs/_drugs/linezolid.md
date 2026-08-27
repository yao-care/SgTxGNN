---
layout: default
title: Linezolid
parent: 僅模型預測 (L5)
nav_order: 597
evidence_level: L5
indication_count: 10
---

# Linezolid
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

# Linezolid: From Gram-Positive Bacterial Infections to Pyelonephritis

## One-Sentence Summary

Linezolid is an oxazolidinone antibiotic established for treating serious Gram-positive bacterial infections, including MRSA and vancomycin-resistant *Enterococcus* (VRE). Among the 10 indications TxGNN predicted for Linezolid, 9 (ranks 1–9) have **zero supporting clinical trials or literature** and are flagged by the pipeline's own rationale as likely knowledge-graph noise; the only candidate that clears a credible evidence bar is **Pyelonephritis**, supported by **1 RCT and 9 other relevant publications** on Gram-positive/multidrug-resistant urinary pathogens — though no pyelonephritis-specific clinical trial currently exists.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gram-positive bacterial infections (e.g., MRSA, VRE) — based on established pharmacological knowledge; no Singapore license text is available in the evidence pack |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 82.67% |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the evidence pack (flagged as a **High-severity data gap, DG002**). Based on established pharmacological knowledge, Linezolid is an oxazolidinone-class antibiotic that inhibits bacterial protein synthesis by binding the 23S ribosomal RNA of the 50S subunit, blocking formation of the initiation complex. It is active against Gram-positive organisms — including MRSA, vancomycin-resistant *Enterococcus faecium/faecalis* (VRE), and *Streptococcus* species — and is an established option for complicated skin/soft-tissue infections, community-acquired pneumonia, and VRE bacteremia.

**Note on candidate selection:** TxGNN generated 10 ranked candidate indications for Linezolid. Ranks 1–5, 7 and 8 (polyclonal hyperviscosity syndrome, hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant hematological disease, hematological disease with acquired peripheral neuropathy, congenital hematological disorder) have **no clinical trials, no literature, and no plausible mechanistic link** to Linezolid's antibacterial action — the pipeline's own rationale explicitly labels several of these as graph noise, and notably flags rank 7 as a probable **direction-reversal error**, since peripheral neuropathy is a known *adverse effect* of long-term Linezolid use, not a treatable indication. Rank 6 (monoclonal gammopathy) and rank 9 (septicemic plague) only appear in the literature because Linezolid was used to treat *concurrent infections* in patients with those conditions — not because it treats the conditions themselves. Given this, this report focuses on the one candidate with genuine supporting evidence: **Pyelonephritis** (rank 10).

Pyelonephritis is predominantly caused by Gram-negative organisms (e.g., *E. coli*), but Gram-positive uropathogens — including MRSA, VRE, *Enterococcus* species, and Group B *Streptococcus* — are well-recognized causative agents, particularly in complicated, catheter-/stent-associated, post-surgical, or drug-resistant cases. Because Linezolid's antibacterial spectrum directly covers these organisms, this candidate represents a **coherent spectrum-extension repurposing** (same mechanism, same drug class, adjacent infectious-disease indication) rather than a novel or speculative mechanistic application — distinguishing it clearly from the mechanistically unsupported candidates above.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14520141](https://pubmed.ncbi.nlm.nih.gov/14520141/) | 2003 | RCT | Pediatr Infect Dis J | Linezolid vs. vancomycin in neonates with known/suspected resistant Gram-positive infections (*S. aureus*, CoNS, enterococci); linezolid was FDA-approved for Gram-positive infections in pediatric patients |
| [21308555](https://pubmed.ncbi.nlm.nih.gov/21308555/) | 2010 | Review | Curr Infect Dis Rep | *Enterococcus* is an increasingly important UTI pathogen; multidrug resistance (including vancomycin resistance) complicates management and drives need for alternative agents such as linezolid |
| [33034781](https://pubmed.ncbi.nlm.nih.gov/33034781/) | 2021 | Cohort | Eur J Clin Microbiol Infect Dis | Retrospective study of 415 post-PCNL, ureteral-stent patients analyzing risk factors, causative species, and drug resistance in stent-associated acute pyelonephritis |
| [19918525](https://pubmed.ncbi.nlm.nih.gov/19918525/) | 2009 | Case Report | Cases Journal | First reported case of xanthogranulomatous pyelonephritis caused by community-associated MRSA — an organism for which linezolid is a first-line oral option |
| [18349306](https://pubmed.ncbi.nlm.nih.gov/18349306/) | 2008 | Case Report | Ann Pharmacother | Successful treatment of VRE-associated pyelonephritis (with daptomycin) in a pregnant patient, illustrating VRE as a recognized Gram-positive uropathogen requiring non-vancomycin coverage |
| [34556047](https://pubmed.ncbi.nlm.nih.gov/34556047/) | 2021 | Case Report | BMC Infect Dis | Pyelonephritis with *Enterococcus hirae* bacteremia — a rare Gram-positive uropathogen — with literature review |
| [38161637](https://pubmed.ncbi.nlm.nih.gov/38161637/) | 2024 | Case Report | Clin Case Rep | VRE bacteremia/UTI following continent urinary diversion; highlights need for multidrug-resistant Gram-positive screening and management |
| [38050281](https://pubmed.ncbi.nlm.nih.gov/38050281/) | 2023 | Case Report | Medicine | Two pediatric cases of renal abscess complicating acute pyelonephritis, reviewing diagnostic and treatment approaches |
| [27645240](https://pubmed.ncbi.nlm.nih.gov/27645240/) | 2016 | Preclinical | Antimicrob Agents Chemother | In vitro/in vivo activity of a bi-aryl oxazolidinone (RBx 11760) benchmarked directly against linezolid in *S. aureus*, *S. epidermidis*, *Enterococcus*, and *S. pneumoniae* |
| [26510270](https://pubmed.ncbi.nlm.nih.gov/26510270/) | 2015 | Cohort | Br J Biomed Sci | Screening study of asymptomatic Group B *Streptococcus* (a Gram-positive uropathogen) bacteriuria among pregnant women |

---

## Safety Considerations

Please refer to the package insert for safety information.

Local (Singapore) prescribing safety information — key warnings, contraindications, and drug-drug interaction data — is currently unavailable in the evidence pack. This is flagged as a **Blocking-severity data gap (DG001)**: without it, this candidate cannot advance past the S1 safety pre-screening stage, regardless of the supporting efficacy literature above.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One RCT and nine additional publications support Linezolid's activity against the Gram-positive/multidrug-resistant pathogens (VRE, MRSA, GBS, *Enterococcus* spp.) known to cause pyelonephritis, and the mechanism represents a coherent extension of Linezolid's existing antibacterial spectrum rather than a novel target. However, no pyelonephritis-specific clinical trial exists, the drug is not currently marketed in Singapore, and local safety/label data is a blocking gap — so this should proceed only as a guarded research direction, not a market-ready repurposing candidate.

**To proceed, the following is needed:**
- Local (Singapore-equivalent) package insert / regulatory safety data to resolve the Blocking data gap (DG001) and complete S1 safety screening
- Confirmed mechanism-of-action documentation from DrugBank to resolve DG002
- A targeted retrospective or prospective study evaluating Linezolid specifically in complicated/MDR Gram-positive pyelonephritis (current evidence is extrapolated from general Gram-positive infection and UTI literature, not pyelonephritis-specific trials)
- No further investment in ranks 1–9 candidates unless new mechanistic or clinical evidence emerges — current data supports treating them as TxGNN graph-noise artifacts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

