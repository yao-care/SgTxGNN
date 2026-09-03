---
layout: default
title: Sulbactam
parent: 僅模型預測 (L5)
nav_order: 929
evidence_level: L5
indication_count: 10
---

# Sulbactam
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

# Sulbactam: From Bacterial Infections to Bacterial Arthritis

## One-Sentence Summary

> Sulbactam is a β-lactamase inhibitor with minimal antibacterial activity on its own, used clinically in combination with ampicillin (and other β-lactams) to restore efficacy against β-lactamase-producing bacteria.
> The TxGNN model predicts it may be effective for **Bacterial Arthritis**,
> with **no registered clinical trials** but **20 supporting publications** (including one RCT and several comparative cohort studies) currently identified for this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections, used in combination with ampicillin as a β-lactamase inhibitor (specific TFDA/HSA-approved indication text not available — drug is not registered in Singapore) |
| Predicted New Indication | Bacterial Arthritis |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for sulbactam alone is not available in DrugBank. Based on known pharmacology, sulbactam is an irreversible β-lactamase inhibitor that is almost always co-administered with ampicillin (as ampicillin/sulbactam, or the oral prodrug sultamicillin). It has minimal intrinsic antibacterial activity but restores the effectiveness of ampicillin against β-lactamase-producing organisms such as *Staphylococcus aureus*, *Haemophilus influenzae*, and various Enterobacteriaceae.

Bacterial (septic) arthritis is an infection requiring prompt, broad-spectrum empirical antibiotic coverage, frequently caused by β-lactamase-producing organisms — exactly the pathogen population that ampicillin/sulbactam was designed to cover. This is therefore best understood as an extension of an already well-established antibacterial indication (skeletal/soft-tissue infections) rather than a novel mechanistic hypothesis.

An important caveat: the evidence pack notes that sulbactam's `original_indications` field is empty (data gap), and essentially all clinical evidence identified is for the **ampicillin/sulbactam combination**, not sulbactam monotherapy. This attribution ambiguity should be kept in mind when interpreting the strength of this prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2677956](https://pubmed.ncbi.nlm.nih.gov/2677956/) | 1989 | RCT | Pediatric Infectious Disease Journal | Randomized 2:1 comparison of ampicillin/sulbactam vs. ceftriaxone in 105 children with soft-tissue infection, suppurative arthritis, or osteomyelitis; ampicillin/sulbactam group covered common pathogens including *S. aureus* and *S. pyogenes* |
| [3026018](https://pubmed.ncbi.nlm.nih.gov/3026018/) | 1986 | Cohort (sequential therapy trial) | Reviews of Infectious Diseases | 9 children with osteomyelitis/septic arthritis treated with sequential IV sulbactam/ampicillin then oral sultamicillin; all isolated pathogens susceptible, adequate serum bactericidal titers achieved |
| [3026009](https://pubmed.ncbi.nlm.nih.gov/3026009/) | 1986 | Cohort (open comparative trial) | Reviews of Infectious Diseases | Open randomized comparison of sulbactam/ampicillin vs. cefotaxime for serious bone, joint, and soft-tissue infections; clinical cure/improvement in all 13 sulbactam/ampicillin patients at 2 weeks post-therapy |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Cohort (pathogen surveillance) | Clinical Laboratory | Analysis of pathogen distribution and antimicrobial resistance in bone and joint infections among young children, informing empirical antibiotic selection |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Review | International Journal of Antimicrobial Agents | Review of off-label and formal antibiotic use (including β-lactam/β-lactamase inhibitor combinations) for MDR/XDR bacterial infections |
| [16269877](https://pubmed.ncbi.nlm.nih.gov/16269877/) | 2005 | Review | Acta Orthopaedica et Traumatologica Turcica | Review of septic arthritis diagnosis and initial antibiotic treatment protocols in children and adults |
| [6094857](https://pubmed.ncbi.nlm.nih.gov/6094857/) | 1984 | Clinical study | The Japanese Journal of Antibiotics | Pediatric clinical study of sulbactam/cefoperazone including a case of acute purulent knee arthritis; 100% overall efficacy rate reported |
| [3252119](https://pubmed.ncbi.nlm.nih.gov/3252119/) | 1988 | Clinical trial | Mikrobiyoloji Bulteni | 84 patients with various infections including 5 cases of septic arthritis/osteomyelitis treated with parenteral ampicillin/sulbactam, with favorable clinical and microbiological outcomes |
| [9263167](https://pubmed.ncbi.nlm.nih.gov/9263167/) | 1997 | Case Report | The Journal of Rheumatology | *Pasteurella multocida* infectious arthritis after cat bite successfully treated with ampicillin/sulbactam plus joint aspiration and intra-articular steroids |
| [36550469](https://pubmed.ncbi.nlm.nih.gov/36550469/) | 2022 | Case Report | BMC Infectious Diseases | Septic arthritis case caused by rare pathogen *Ureaplasma parvum*, complicated by hyperammonemia, illustrating diagnostic and treatment challenges in atypical septic arthritis |

---

## Singapore Market Information

Sulbactam has no registered pharmaceutical licenses in Singapore (0 registrations, market status: Not Marketed). No product-level licensing data is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Mechanistic plausibility is strong (β-lactamase inhibition covering typical septic arthritis pathogens) and is supported by one RCT and several comparative cohort studies, but nearly all evidence is decades old, pediatric-focused, and attributable to the ampicillin/sulbactam combination rather than sulbactam alone — consistent with an L3 evidence level rather than confirmatory Phase 3 data.

**To proceed, the following is needed:**
- TFDA/HSA package insert data (warnings, contraindications) — currently a **Blocking** data gap preventing S1 safety screening
- DrugBank-sourced mechanism of action (MOA) data for sulbactam specifically — currently a **High**-severity gap affecting mechanistic attribution
- Clarification of whether this indication should be evaluated for the ampicillin/sulbactam combination product rather than sulbactam as a standalone entity
- Contemporary clinical trial or susceptibility data to update the largely 1980s–1990s evidence base
- A Singapore market entry pathway assessment, given the drug currently holds zero local registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

