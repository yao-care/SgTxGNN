---
layout: default
title: Cefadroxil
parent: Low Evidence (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
---

# Cefadroxil
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

# Cefadroxil: From Urinary Tract Infection to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Cefadroxil is a first-generation oral cephalosporin antibiotic, originally used for bacterial infections such as urinary tract infection, tonsillitis and staphylococcal or streptococcal infections.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** support this prediction, and no credible mechanistic link exists, so it should be treated as a model artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, tonsillitis, streptococcal infection, staphylococcal infections (approved indication text is not listed in the Singapore licence record) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 98.60% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cefadroxil is a first-generation cephalosporin that inhibits bacterial cell wall synthesis, and its efficacy in bacterial infections of the urinary tract, throat and skin is established.

The predicted indication, however, is not an infection. Polyclonal hyperviscosity syndrome is driven by elevated immunoglobulins or serum proteins, and an antibacterial does not act on that process. The high score (98.60%) is most likely a knowledge-graph artifact rather than a pharmacological signal. The same pattern appears in the other top-ranked predictions: hyperamylasemia, congenital analbuminemia, blood group incompatibility, monoclonal gammopathy and related haematological conditions all lack a plausible mechanism.

Among the lower-ranked predictions, the infectious ones are closer to the drug's class but are also weak:
- **Gonococcal urethritis** is mechanistically plausible for cephalosporins in general, but cefadroxil has poor gonococcal activity, and later-generation agents such as ceftriaxone are standard.
- **Ureaplasma urethritis** is unlikely to respond because Ureaplasma has no cell wall, so beta-lactams are intrinsically ineffective.
- **Septicemic plague** is not treated with oral first-generation cephalosporins; aminoglycosides, fluoroquinolones and doxycycline are first-line.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for the top-ranked prediction, polyclonal hyperviscosity syndrome.

For reference, one paper was linked to a lower-ranked prediction (gonococcal urethritis):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2673664](https://pubmed.ncbi.nlm.nih.gov/2673664/) | 1989 | Cohort | Current Medical Research and Opinion | Reports on 1,000 patients treated with cefetamet pivoxil, a different oral cephalosporin; cefadroxil was only one of the comparator antibiotics. Single doses of cefetamet pivoxil were effective in gonorrhoea. This is indirect, class-level evidence only. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11665P | SOFIDROX CAPSULE 500 mg | Capsule | Not stated in the licence record |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: Clostridium difficile colitis, perinatal necrotizing enterocolitis, impaired renal function disease.
- **Drug Interactions**: 51 interactions were identified. Those rated Moderate are:
  - Balsalazide
  - Picosulfuric acid

  Other listed interactions have an unrated severity (e.g. acetylsalicylic acid, doxycycline, metformin, omeprazole, pantoprazole, prednisone, simvastatin, metronidazole), and they should be reviewed before any use.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature, and it has no credible mechanistic basis, because a cell-wall-active antibacterial does not address protein- or immunoglobulin-driven hyperviscosity. The high TxGNN score alone is not sufficient to justify further investment.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis linking cefadroxil to the predicted indication
- Detailed mechanism of action data (MOA) from DrugBank
- Package insert warnings and contraindications from the HSA website
- Any preclinical or clinical evidence for the predicted indication
- If an infectious repurposing direction is of interest, a review of the lower-ranked infectious predictions (such as gonococcal urethritis) against current treatment guidelines and local resistance data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

