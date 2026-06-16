---
layout: default
title: Cefaclor
parent: 僅模型預測 (L5)
nav_order: 217
evidence_level: L5
indication_count: 10
---

# Cefaclor
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

# Cefaclor: From Bacterial Infections to Gonococcal Urethritis

## One-Sentence Summary

Cefaclor is a second-generation oral cephalosporin antibiotic, widely used to treat bacterial infections of the respiratory tract, urinary tract, and skin.
The TxGNN model's highest-evidence prediction is **Gonococcal Urethritis** (model rank #3), supported by **0 registered clinical trials** and **6 published studies** spanning 1979–1997.
The majority of the top-10 TxGNN predictions (ranks 1, 2, 4–10) lack biological plausibility and are assessed as likely knowledge-graph noise; only the gonococcal urethritis prediction carries actionable clinical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum bacterial infections (respiratory, urinary tract, skin) |
| Predicted New Indication (Best Evidence) | Gonococcal Urethritis |
| TxGNN Prediction Score | 97.48% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cefaclor belongs to the second-generation cephalosporin class of β-lactam antibiotics. Its core mechanism is inhibition of bacterial cell wall synthesis through covalent binding to penicillin-binding proteins (PBPs). Because *Neisseria gonorrhoeae* possesses a cell wall and expresses susceptible PBP variants, Cefaclor's antibacterial mechanism applies directly — making this a biologically plausible repurposing candidate, not a graph-generated artefact.

The connection between Cefaclor's established role in treating bacterial infections and its potential use in gonococcal urethritis is straightforward: both involve susceptible gram-negative bacteria requiring cell wall disruption. Between 1979 and 1997, multiple controlled and comparative clinical trials demonstrated clinical cure rates above 89% when Cefaclor was used in single or multi-dose regimens, including head-to-head comparisons against spectinomycin. The evidence base is older but methodologically direct.

The critical caveat is that the antibiotic landscape has shifted significantly. Current WHO and CDC guidelines deprioritise second-generation cephalosporins for gonococcal infections due to the global emergence of cephalosporin-resistant *N. gonorrhoeae* strains (including ESBL and high-level cephalosporin resistance). Any consideration of Cefaclor for this indication would require local antibiogram data to confirm strain susceptibility before clinical use.

> **Note on MOA data gap:** Formal DrugBank mechanism-of-action data was not retrieved for this report. The pharmacological rationale above is derived from the class-level knowledge of second-generation cephalosporins and from the mechanistic link documented in the Evidence Pack's `repurposing_rationale` field.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [121455](https://pubmed.ncbi.nlm.nih.gov/121455/) | 1979 | Clinical Trial (open-label) | Postgraduate Medical Journal | Controlled trial in 40 men with uncomplicated gonococcal urethritis; 1 g loading dose of Cefaclor showed activity against *N. gonorrhoeae* in vitro and clinically |
| [116373](https://pubmed.ncbi.nlm.nih.gov/116373/) | 1979 | Clinical Trial (open-label) | Sexually Transmitted Diseases | Randomised trial in men; regimens of 2–4 g Cefaclor ± probenecid evaluated; therapeutic outcomes confirmed by Day 7 follow-up cultures of 66 participants |
| [6225482](https://pubmed.ncbi.nlm.nih.gov/6225482/) | 1983 | Comparative Clinical Trial | British Journal of Venereal Diseases | 400 men randomised to spectinomycin, cefamandole, or Cefaclor ± probenecid; Cefaclor 3 g + probenecid achieved 95.8% cure rate vs. 98.9% for spectinomycin |
| [6400040](https://pubmed.ncbi.nlm.nih.gov/6400040/) | 1984 | Clinical Trial (interventional) | Medical Journal of Malaysia | Single-dose oral Cefaclor evaluated in men with uncomplicated gonococcal urethritis |
| [9582471](https://pubmed.ncbi.nlm.nih.gov/9582471/) | 1997 | Comparative Study | Genitourinary Medicine | Reassessment of in vivo and in vitro efficacy of Cefaclor for uncomplicated gonococcal infection; evaluated as potential alternative to third-generation cephalosporins in resource-limited settings |
| [2673664](https://pubmed.ncbi.nlm.nih.gov/2673664/) | 1989 | Large Case Series | Current Medical Research and Opinion | 1,505-patient multi-national study comparing cefetamet pivoxil against standard antibiotics including Cefaclor; single doses of comparator cephalosporins shown effective for gonorrhoea |

---

## Singapore Market Information

Cefaclor has **no registered products in Singapore** at this time (HSA market status: Not Marketed; total licences: 0). This means any clinical development pathway would need to proceed via new product registration with the Health Sciences Authority (HSA) under the relevant therapeutic indication.

---

## Safety Considerations

Please refer to the package insert for safety information. Full prescribing data — including warnings, contraindications, and drug interactions — was not available in this Evidence Pack.

> **Pharmacokinetic alert (from repurposing rationale):** Patients with hypoalbuminaemia may exhibit significantly altered Cefaclor pharmacokinetics due to reduced protein binding, leading to elevated free-drug concentrations. This should be considered when dosing in patients with hepatic disease, malnutrition, or albumin-related disorders.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple controlled clinical trials from 1979–1997 confirmed Cefaclor's direct antibacterial activity against *N. gonorrhoeae* with cure rates exceeding 89–95%, and the β-lactam cell-wall inhibition mechanism is directly applicable. However, the evidence predates the emergence of cephalosporin-resistant gonorrhoea strains, which substantially limits direct clinical translation without contemporary susceptibility data.

**To proceed, the following is needed:**

- **Local antibiogram data**: Current *N. gonorrhoeae* susceptibility profiles in Singapore (or target market) must confirm Cefaclor MIC values are within therapeutic range — this is the single most critical gate
- **Formal MOA documentation**: Retrieve DrugBank API entry (DB00833) to complete the mechanistic dossier
- **Regulatory safety package**: Obtain and parse the Singapore HSA package insert (or equivalent market authorisation in an approved jurisdiction) to fill the blocking data gap (DG001) on warnings and contraindications
- **Resistance review**: Systematic literature review of post-2000 cephalosporin resistance rates in gonorrhoea to quantify the gap between 1979–1997 trial populations and current epidemiology
- **HSA registration pathway**: Initiate pre-submission consultation with HSA given zero current Singapore registrations

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

