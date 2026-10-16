---
layout: default
title: Cefotaxime
parent: Low Evidence (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cefotaxime: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Bacterial infections (bacterial pneumonia, bacterial meningitis…"
monitor_inn: "Cefotaxime"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "pneumococcal meningitis", "septicemic plague", "congenital hematological disorder"]
---

# Cefotaxime
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

# Cefotaxime: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Cefotaxime is a third-generation cephalosporin antibiotic, originally used for bacterial infections such as bacterial pneumonia, bacterial meningitis, peritonitis and bacterial arthritis.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome** (score 98.5%), but **no clinical trials and no publications** currently support this prediction, and no plausible mechanism has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (bacterial pneumonia, bacterial meningitis, peritonitis, bacterial arthritis, among others); no approved indication text is recorded for the Singapore licences |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 98.47% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, cefotaxime is a beta-lactam antibiotic that inhibits bacterial cell wall synthesis. Its efficacy in bacterial infections is well established.

Polyclonal hyperviscosity syndrome is driven by excess serum immunoglobulins and has no antibacterial target. No mechanistic link to cefotaxime was identified. The high TxGNN score appears to be a graph-based prediction without supporting clinical or literature data, and is likely a network-proximity artifact.

The other top-ranked predictions show the same pattern. Hyperamylasemia, congenital analbuminemia, premalignant hematological disease and neuropathy-associated hematological disease have no plausible mechanism and no evidence. The only predictions with a rational basis are those where cefotaxime treats an infection (pneumococcal meningitis, septicemic plague). These are either on-label uses or supported only by animal data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications were found for the top-ranked prediction (polyclonal hyperviscosity syndrome). The table below shows the most relevant literature for the lower-ranked predictions, to provide context. These publications do not support the top prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19047432](https://pubmed.ncbi.nlm.nih.gov/19047432/) | 2008 | Review | Pediatrics in Review | Empiric therapy for suspected bacterial meningitis in non-neonates includes vancomycin plus cefotaxime or ceftriaxone (pneumococcal meningitis) |
| [37741342](https://pubmed.ncbi.nlm.nih.gov/37741342/) | 2023 | Review | Infectious Diseases Now | Antibiotic treatment of neuro-meningeal infections; no pneumococcal meningitis cases resistant to third-generation cephalosporins recorded in France |
| [29290234](https://pubmed.ncbi.nlm.nih.gov/29290234/) | 2017 | Review | Archives de Pédiatrie | Bacterial meningitis antibiotic treatment after pneumococcal conjugate vaccines |
| [12182395](https://pubmed.ncbi.nlm.nih.gov/12182395/) | 2002 | Review | Pediatr Infect Dis J | Standard empiric therapy is cefotaxime or ceftriaxone plus vancomycin; resistance complicates treatment |
| [9024464](https://pubmed.ncbi.nlm.nih.gov/9024464/) | 1997 | Guideline | Pediatrics | AAP guidance on invasive pneumococcal infections; treatment failures of cefotaxime or ceftriaxone reported with resistant strains |
| [34120184](https://pubmed.ncbi.nlm.nih.gov/34120184/) | 2021 | Retrospective cohort | J Antimicrob Chemother | CSF concentrations of cefotaxime after high-dose administration in adults with pneumococcal meningitis |
| [36326246](https://pubmed.ncbi.nlm.nih.gov/36326246/) | 2022 | Review | Antimicrob Agents Chemother | Observational cohort on treating penicillin- and cephalosporin-resistant pneumococcal meningitis |
| [8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/) | 1994 | Animal study | Antimicrob Agents Chemother | Cefotaxime was active against Yersinia pestis in a mouse infection model (septicemic plague) |
| [9054316](https://pubmed.ncbi.nlm.nih.gov/9054316/) | 1996 | Animal study | Antibiot Khimioter | Third-generation cephalosporins, including cefotaxime, were promising in experimental plague in mice |
| [35003054](https://pubmed.ncbi.nlm.nih.gov/35003054/) | 2021 | Case report | Frontiers in Immunology | Cefotaxime-sulbactam-induced acute intravascular hemolysis in a newborn with ABO incompatibility (adverse event, not a benefit) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16368P | CYTAXIN POWDER FOR SOLUTION FOR INJECTION 1G/VIAL | Injection, powder, for solution | Not recorded |
| SIN16367P | CYTAXIN POWDER FOR SOLUTION FOR INJECTION 0.5G/VIAL | Injection, powder, for solution | Not recorded |

## Safety Considerations

- **Knowledge-graph contraindications**: Clostridium difficile colitis and perinatal necrotizing enterocolitis (from the TxGNN knowledge graph, not from label text).
- **Drug Interactions**: 73 interactions were identified. Moderate-level interactions include:
  - Kanamycin
  - Neomycin
  - Streptomycin
  - Picosulfuric acid

  Other listed interactions (for example vancomycin, metformin, omeprazole, prednisone, morphine) have no assigned severity level.
- **Literature safety signal**: A case report describes cefotaxime-sulbactam-induced acute intravascular hemolysis in a newborn. Beta-lactams at high doses are also associated with neurotoxicity.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for polyclonal hyperviscosity syndrome rests only on a graph-model score. There are no clinical trials or literature, and there is no plausible mechanism, since cefotaxime has no effect on excess immunoglobulins. Among the other predictions, pneumococcal meningitis is effectively an existing indication. Septicemic plague is supported only by preclinical animal studies, and plague first-line therapy relies on other agents.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Singapore regulator (HSA), including the approved indication text for the two Cytaxin licences
- Mechanism of action data (MOA)
- A biological rationale linking cefotaxime to hyperviscosity syndrome, or a decision to redirect the evaluation to the better-supported infectious indications (for example, septicemic plague) and to review the drug's resistance patterns
- Any human clinical evidence for the predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

