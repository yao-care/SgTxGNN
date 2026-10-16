---
layout: default
title: Vancomycin
parent: Low Evidence (L5)
nav_order: 1055
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Vancomycin: predicted new indication Diffuse scleroderma (evidence level L5). Approved use: Clostridium difficile colitis, staphylococcal infection, endocarditis…"
---

# Vancomycin
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

# Vancomycin: From Clostridium difficile Colitis to Diffuse Scleroderma

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic originally used for Gram-positive bacterial infections, including Clostridium difficile colitis, staphylococcal infections and endocarditis.
The TxGNN model predicts it may be effective for **diffuse scleroderma**, but there are **0 clinical trials** and only **1 unrelated case report** behind this prediction.
The high score is most likely a knowledge-graph artifact rather than a real therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Clostridium difficile colitis, staphylococcal infection, endocarditis, bacterial arthritis, staphylococcal pneumonia (indications from the knowledge graph; the Singapore licence records contain no indication text) |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, vancomycin inhibits bacterial cell wall synthesis by binding D-Ala-D-Ala terminals. This acts on Gram-positive bacteria only.

Diffuse scleroderma is a fibrotic autoimmune disease, not a bacterial infection. There is no plausible mechanistic link between vancomycin and its pathology. The only literature hit is a case report of erythroderma with sepsis and eosinophilia, which is a differential-diagnosis discussion and not evidence of benefit. The high score is therefore likely a graph artifact, and the prediction is not supported.

**Other predictions reviewed.** Nine other candidates were screened, and none is supported:

- **Gram-negative infections (paratyphoid fever, salmonellosis, typhoid fever):** Vancomycin cannot cross the Gram-negative outer membrane and has no intrinsic activity. Standard therapy for these infections is well established.
- **Non-infectious conditions (congenital analbuminemia, hyperamylasemia, polyclonal hyperviscosity syndrome, blood group incompatibility, premalignant haematological disease):** There is no mechanistic rationale, and no trials or relevant literature.
- **Streptococcal pneumonia (the only biologically plausible candidate):** This is an L4 research question. Streptococcus pneumoniae is Gram-positive, and vancomycin is used as an adjunct for penicillin- or cephalosporin-resistant pneumococcal infection. Beta-lactams remain first-line for pneumonia, the literature is indirect, and no trials were found. It overlaps with the existing staphylococcal pneumonia indication, so it would be a label extension rather than true repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case report | The American Journal of Case Reports | A 56-year-old man with diffuse exfoliative rash, sepsis and eosinophilia was evaluated for erythroderma. It is a differential-diagnosis discussion and does not show vancomycin benefit in scleroderma. |

---

## Singapore Market Information

All 10 licences are valid single-ingredient products. No approved-indication text is recorded for them. The five main authorisations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08069P | Vancomycin HCl Injection 500 mg/vial | Powder for solution for injection | Not recorded |
| SIN15417P | Vancosala powder for solution for injection or infusion 500 mg | Lyophilised powder for injection | Not recorded |
| SIN16445P | Vancover Capsules 250 mg | Capsule | Not recorded |
| SIN15070P | Vancomycin Kabi powder for concentrate for solution for infusion 500 mg | Lyophilised powder for infusion | Not recorded |
| SIN16932P | Difforal Capsules 250 mg | Capsule | Not recorded |

Both injectable and oral (capsule) forms are registered.

---

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text):** kidney disease, pyoureter, neutropenia, agranulocytosis, hearing disorder, auditory system disease.
- **Drug Interactions:** 100 interactions were found. Examples from the 20 reviewed:
  - **Major:** intravenous human immunoglobulin G, human botulinum neurotoxin A/B immune globulin, live Vibrio cholerae CVD 103-HgR vaccine.
  - **Moderate:** NSAIDs (ketorolac, ibuprofen, diclofenac, celecoxib), aminoglycosides and related nephrotoxic or ototoxic agents (amikacin, capreomycin, amphotericin B), carboplatin, metformin, bacitracin and cholestyramine.

Please also refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has an L5 evidence level. It has no clinical trials, no mechanistic link between a Gram-positive antibacterial and a fibrotic autoimmune disease, and only an irrelevant case report. The high TxGNN score is likely a graph artifact. Safety also needs attention, since the knowledge graph flags kidney and hearing disorders.

**To proceed, the following is needed:**
- Mechanism of action data (MOA)
- Package insert warnings and contraindications from HSA, which are currently missing
- Any preclinical or clinical evidence linking vancomycin to scleroderma. Without it, the prediction should not advance.
- If a Gram-positive extension is of interest, a separate review of **streptococcal pneumonia**, the one biologically plausible candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

