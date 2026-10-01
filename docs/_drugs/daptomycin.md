---
layout: default
title: Daptomycin
parent: Low Evidence (L5)
nav_order: 299
evidence_level: L5
indication_count: 10
---

# Daptomycin
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

# Daptomycin: From Gram-Positive Bacterial Infections to Osteoarthritis

## One-Sentence Summary

Daptomycin is a cyclic lipopeptide antibiotic, used against Gram-positive infections such as skin infections, bacteraemia and right-sided endocarditis.
The TxGNN model predicts it may be effective for **osteoarthritis** (score 99.86%), but **no clinical trials** and no studies of osteoarthritis itself were found.
The 8 publications retrieved are about bone and joint *infections*, so this prediction is best treated as a knowledge-graph artefact for now.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gram-positive infections (skin infections, bacteraemia, right-sided endocarditis, per published literature; the Singapore registration records contain no indication text) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 (no studies of osteoarthritis itself; the source pack labels it L4, based on infection-related literature) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Daptomycin is a cyclic lipopeptide with strong antibacterial activity against most Gram-positive pathogens, and its efficacy in bacterial infections is established.

The osteoarthritis prediction is **not mechanistically supported**. Osteoarthritis is a degenerative joint disease, whereas every paper retrieved concerns daptomycin as an antibacterial for osteoarticular or prosthetic joint infections. The high score most likely reflects a "joint/bone" association in the knowledge graph rather than a disease-modifying effect.

Two lower-ranked predictions are worth noting:
- **Rheumatoid arthritis** (score 99.84%): two 2025 preclinical studies (PMID 39571268, 40923559) report that daptomycin, or derived cyclic lipopeptides, reduced inflammatory cytokines and NF-κB signalling and alleviated collagen-induced arthritis in mice. This is a plausible anti-inflammatory mechanism, but there is no human data. Translation is limited by IV-only dosing, the risk of CPK elevation and myopathy, and the need for long-term use in a chronic disease.
- **Gout** (score 99.79%): the only report is a case of daptomycin-induced rhabdomyolysis followed by acute gouty arthritis. This is an adverse-event signal, not a therapeutic one.

The remaining seven predictions (osteoarthritis susceptibility and several rare skeletal or congenital syndromes) have no supporting mechanism and no trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of these papers tests daptomycin as a treatment for osteoarthritis. All concern bone and joint infections.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Cohort | International Orthopaedics | Safety and efficacy of high-dose daptomycin plus rifampicin in Gram-positive osteoarticular infections |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Cohort | J Antimicrob Chemother | Clinical efficacy and safety of daptomycin in hip and knee periprosthetic joint infections |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Cohort | Int J Antimicrob Agents | High-dose daptomycin (>6 mg/kg) in complicated bone, joint and implant-associated Gram-positive infections (no abstract available) |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Cohort | J Antimicrob Chemother | Outcomes of daptomycin versus standard therapy for osteoarticular infections with *S. aureus* bacteraemia |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Cohort | Medicina Clínica | Spanish experience with daptomycin from the EU-CORE registry across Gram-positive infections |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Cohort (survey) | Int J Antimicrob Agents | Survey of infectious diseases physicians on current prosthetic joint infection management |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Cohort | Surgical Infections | Ten-year evolution of staphylococcal profiles in osteoarticular infections |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In vitro | J Antibiot | Antibiotic susceptibility of *S. aureus* and *S. epidermidis* from prosthetic joint infections |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Case report | Case Reports in Orthopedics | Chronic *Corynebacterium striatum* septic arthritis in a patient with known osteoarthritis referred for knee replacement |

## Singapore Market Information

Approved indication text is not available in the registration records.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN16443P | Pfizer Daptomycin 500 mg/vial (Hospira Australia) | Lyophilised powder for injection/infusion |
| SIN16813P | Penmix Daptomycin 500 mg/vial (Penmix Ltd) | Lyophilised powder for injection/infusion |
| SIN16828P | Bedapt Daptomycin 500 mg/vial (Biological E.) | Powder for injection/infusion |
| SIN17204P | Daptomycin/Anfarm 500 mg/vial (Anfarm Hellas) | Lyophilised powder for injection/infusion |
| SIN16900P | Daptomycin-AFT 500 mg/vial (Qilu Pharmaceutical, Hainan) | Lyophilised powder for injection/infusion |

All products are injectable only, so any chronic-disease use would require IV administration.

## Safety Considerations

- **Muscle toxicity signal**: the literature describes daptomycin-induced rhabdomyolysis (a 2023 case complicated by acute gouty arthritis, PMID 36693494). CPK elevation and myopathy are recognised risks, and they matter for any long-term use in chronic joint disease.

No structured warnings, contraindications or drug interaction data were available. Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The osteoarthritis prediction has a very high model score but no supporting trials, and the retrieved literature concerns joint infections rather than degenerative osteoarthritis. The drug is IV-only and carries a muscle-toxicity risk, which makes chronic use in osteoarthritis unattractive.

**To proceed, the following is needed:**
- Any direct evidence of daptomycin in osteoarthritis (currently none)
- HSA package insert warnings and contraindications
- Mechanism of action data from DrugBank
- If pursuing an anti-inflammatory direction, rheumatoid arthritis is the more plausible research question, and would need human safety and efficacy data beyond the 2025 mouse studies

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

