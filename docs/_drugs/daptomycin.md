---
layout: default
title: Daptomycin
parent: 僅模型預測 (L5)
nav_order: 274
evidence_level: L5
indication_count: 10
---

# Daptomycin
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

# Daptomycin: From Gram-Positive Bacterial Infections to Osteoarthritis

## One-Sentence Summary

Daptomycin is a cyclic lipopeptide antibiotic approved for treating serious Gram-positive bacterial infections, including complicated skin and soft tissue infections, *Staphylococcus aureus* bacteremia, and right-sided infective endocarditis.
The TxGNN model predicts it may be effective for **Osteoarthritis** with a score of 99.86%, supported by **0 clinical trials** and **9 associated publications** — however, evidence review indicates this is a false positive driven by literature co-occurrence in patients undergoing joint replacement surgery rather than a genuine repurposing signal.
Of the top 10 predictions, **Rheumatoid Arthritis (Rank 2, score 99.84%, Evidence Level L4)** carries the most scientifically credible mechanistic basis, supported by two 2025 preclinical studies demonstrating NF-κB pathway suppression in collagen-induced arthritis models.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gram-positive bacterial infections (complicated skin/soft tissue infections, *S. aureus* bacteremia, right-sided endocarditis) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Daptomycin is a cyclic lipopeptide antibiotic that disrupts bacterial cell membrane integrity in a calcium-dependent manner — it binds to phosphatidylglycerol in the membrane, causing depolarization and rapid bactericidal cell death. This mechanism is unique among antibiotics and specifically targets Gram-positive organisms including MRSA and VRE. It has no known action on eukaryotic cell signaling pathways relevant to inflammatory joint disease.

Osteoarthritis is driven by progressive cartilage degradation, synovial inflammation, and subchondral bone remodeling — pathways mediated by TGF-β, Wnt/β-catenin, MMP-13, and ADAMTS signaling. Daptomycin has no established activity in any of these pathways. There is no pharmacological rationale connecting an antibiotic membrane depolarizer to OA disease modification.

The high TxGNN score is best explained as a **literature co-occurrence false positive**: all 9 retrieved publications describe Daptomycin being used to treat periprosthetic joint infections (PJIs) and osteoarticular infections in patients who had previously undergone joint replacement surgery — a common outcome in advanced OA. These studies address bacterial infection management, not OA treatment. The knowledge graph has learned an association between Daptomycin and "osteoarthritis" from this incidental clinical overlap, not from any true therapeutic connection.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Daptomycin in osteoarthritis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Retrospective comparative | J Antimicrob Chemother | Daptomycin vs. standard therapy for osteoarticular infections associated with *S. aureus* bacteremia — evaluates antibiotic treatment outcomes, not OA disease modification |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Registry analysis | Medicina Clinica | EU-CORE registry real-world daptomycin use in Spain, including osteoarticular infection patients — routine antibiotic usage data |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Retrospective cohort | J Antimicrob Chemother | Daptomycin for hip and knee periprosthetic joint infections — clinical efficacy and safety as an antibiotic in post-arthroplasty patients |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In vitro susceptibility | J Antibiotics | Susceptibility of *S. aureus* and *S. epidermidis* isolated from prosthetic joint infections to daptomycin — microbiological susceptibility mapping |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Cross-sectional survey | Int J Antimicrob Agents | Physician survey on PJI antibiotic practices; daptomycin cited as preferred option for MRSA PJI — clinical practice guidance, not OA therapy |
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Retrospective cohort | Int Orthop | High-dose daptomycin + rifampicin combination for Gram-positive osteoarticular infections — antibiotic regimen safety and efficacy |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Retrospective epidemiology | Surgical Infections | Microbiologic profile of staphylococci from osteoarticular infections over 10 years — antibiotic susceptibility trends to inform empiric therapy |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Retrospective cohort | Int J Antimicrob Agents | High-dose daptomycin (>6 mg/kg) for complicated bone and joint implant-associated infections — dosing safety data |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Case report | Case Reports in Orthopedics | *C. striatum* septic arthritis misdiagnosed as OA; daptomycin used to treat the infection — highlights diagnostic overlap, not OA treatment |

> ⚠️ **Critical Interpretation Note:** All 9 publications address Daptomycin as an **antibiotic for joint infections** occurring in patients with osteoarthritis or post-arthroplasty. None study Daptomycin as a therapy for OA pathology itself. This literature pattern is the mechanistic source of the TxGNN false positive.

---

## Singapore Market Information

Daptomycin is currently **not registered or marketed in Singapore**. No product authorizations are on file.

For reference, Daptomycin (brand name Cubicin®) is approved in the United States, European Union, and other markets for Gram-positive bacterial infections including MRSA. Any future registration in Singapore would require a new HSA application.

---

## Safety Considerations

Please refer to the package insert for comprehensive safety information, as formal warning and contraindication data were not available in this Evidence Pack.

Based on published literature, the following safety signals are particularly relevant to any repurposing consideration:

- **Myotoxicity (High concern for chronic use):** Daptomycin is associated with elevated creatine kinase (CK), myopathy, and rhabdomyolysis — risk increases with higher doses and prolonged administration. A documented case (PMID 36693494) reports daptomycin-induced rhabdomyolysis complicated by acute secondary gouty arthritis. This toxicity profile is incompatible with the long-term treatment required for OA or RA.
- **Pulmonary toxicity:** Eosinophilic pneumonia has been reported with daptomycin use, requiring treatment discontinuation.
- **Route of administration barrier:** Daptomycin is administered intravenously only. This is a fundamental barrier for any chronic musculoskeletal indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN high-score prediction for osteoarthritis is assessed as a **false positive** resulting from knowledge graph co-occurrence, not a true repurposing signal. Daptomycin has no mechanistic basis for OA disease modification, zero clinical trials, and zero preclinical OA models. All associated literature describes antibiotic use in OA patients with secondary joint infections — a clinically incidental association.

---

**Secondary Finding Warranting Monitoring — Rheumatoid Arthritis (Rank 2, L4):**

Two 2025 publications (PMID [39571268](https://pubmed.ncbi.nlm.nih.gov/39571268/), [40923559](https://pubmed.ncbi.nlm.nih.gov/40923559/)) directly demonstrate Daptomycin's anti-inflammatory activity in the collagen-induced arthritis (CIA) mouse model — the gold-standard preclinical model for RA drug development. The proposed mechanism is inhibition of the NF-κB signaling pathway with downstream suppression of TNF-α, IL-1β, IL-6, and IL-17. One group has already synthesized novel Daptomycin-derived cyclic lipopeptide analogs with improved anti-RA activity (CLP-d2), suggesting active structural optimization efforts. This constitutes genuine early-stage mechanistic evidence and merits tracking as a research question.

**To advance the RA research question, the following is needed:**

- Evaluation of anti-inflammatory dosing vs. antibacterial dosing to determine therapeutic window
- Long-term safety data in chronic administration animal models (myotoxicity is the primary barrier)
- Investigation of Daptomycin-derived structural analogs (e.g., CLP-d2) that dissociate anti-inflammatory from myotoxic effects
- In vitro human synoviocyte and PBMC validation studies
- A clear regulatory pathway assessment, given no Singapore registration and IV-only formulation

> **Research Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

