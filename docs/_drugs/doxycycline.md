---
layout: default
title: Doxycycline
parent: Medium Evidence (L3-L4)
nav_order: 353
evidence_level: L4
indication_count: 10
---

# Doxycycline
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Doxycycline: From Bronchitis and Acne to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Doxycycline is a tetracycline-class antibiotic, originally used for respiratory, skin and sexually transmitted bacterial infections such as bronchitis, acne, bacterial pneumonia, anthrax, gonorrhoea and leptospirosis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but so far only **1 publication** (a 1992 case report) and **no clinical trials** support this specific direction, so the evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bronchitis, acne, bacterial pneumonia, anthrax, gonorrhoea and others (from the knowledge graph; the Singapore licence records contain no indication text) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, doxycycline is a broad-spectrum tetracycline antibiotic that is active against *Chlamydia trachomatis*, and its efficacy in bacterial infections is well established.

The predicted condition, punctate epithelial keratoconjunctivitis, is a form of ocular surface inflammation that can follow chlamydial conjunctivitis. Doxycycline may be mechanistically applicable through its antichlamydial activity, and its anti-inflammatory and matrix metalloproteinase (MMP)-inhibiting effects could plausibly help ocular surface inflammation.

However, this link is indirect. The only supporting paper describes two patients who developed persistent punctate keratitis *after* chlamydial conjunctivitis had been treated with tetracycline or doxycycline. It is not a controlled study of doxycycline for this condition, and it does not show that doxycycline treats the keratitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case report/series | Cornea | Two patients with chlamydial follicular conjunctivitis treated with oral tetracycline or doxycycline had resolution of the follicles. Both later developed recurrent bilateral punctate epithelial keratitis. |

Currently no related clinical trials are registered for this indication.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN02205P | DOXYMYCIN-100 CAPSULES 100 mg | Capsule | Not stated in the available records |
| SIN08536P | MICRODOX CAPSULE 100 mg | Capsule | Not stated in the available records |
| SIN08101P | DOXYCAP CAPSULE U.S.P. 100 mg | Capsule | Not stated in the available records |
| SIN08445P | APO-DOXY-TABS 100 mg | Film-coated tablet | Not stated in the available records |
| SIN00968P | MEDOMYCIN CAPSULE 100 mg | Capsule | Not stated in the available records |

Seven valid single-ingredient licences are registered in total (none cancelled). The two not shown above are SIN08388P (Doxyline enteric-coated capsule 100 mg) and SIN10340P (Doxyline capsule 100 mg). All are oral products.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (these are graph-derived associations, not package insert text): *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, and oesophageal dyskinesia.
- **Drug Interactions**: 100 interactions were identified, and the first 20 retrieved include:
  - **Major**: isotretinoin, acitretin, aminolevulinic acid
  - **Moderate**: aluminium hydroxide, aminophylline, amoxicillin, ampicillin, bedaquiline, atracurium, and others
  - **Minor**: acetazolamide, amiloride, bendroflumethiazide
- For this indication, one in vitro study suggests tetracyclines are less cytotoxic to tympanic membrane fibroblasts than quinolones, but it concerns the ear and not the eye.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is supported only by a single 1992 case report, which is indirect evidence, and no clinical trials exist for this condition. Doxycycline is marketed in Singapore, but there is no evidence that it treats punctate epithelial keratoconjunctivitis.

**To proceed, the following is needed:**
- Controlled clinical studies of doxycycline (oral or ocular) in punctate epithelial keratoconjunctivitis
- Mechanism of action data and a review of its anti-inflammatory/MMP-inhibiting effect on the ocular surface
- Package insert warnings and contraindications from the Singapore HSA
- Clarification of the route and formulation needed for ocular use, since all registered products are oral

---

### Other Predicted Indications (Brief Notes)

The model's other top-ranked predictions have similarly limited support, apart from two with more developed trial or literature bases:

| Predicted Indication | Evidence Level | Decision | Note |
|------|------|------|------|
| Otitis externa | L4 | Hold | Mostly veterinary resistance surveillance; standard therapy is topical |
| Postinfectious vasculitis | L4 | Hold | Case reports only |
| Post-bacterial disorder | L1 | Research Question | 11 trials, mostly doxycycline post-exposure prophylaxis for STIs, including completed Phase 2/3 (NCT00237016) and Phase 3 (NCT00351273) trials. This extends its antibacterial use rather than being a new mechanism, and resistance is a concern |
| Post-infectious syndrome | L1 | Research Question | Doxycycline post-exposure prophylaxis for STIs (NCT04050540, NCT07658976 and NCT07500415) rather than immune-mediated syndromes; the Phase 3 trial is not yet recruiting, so the signal is weak |
| Infective urethral stricture | L4 | Hold | One retrospective brucellosis series; no stricture benefit shown |
| Chagas cardiomyopathy | L4 | Hold | Preclinical study showed no added benefit over benznidazole |
| Infection-related haemolytic uraemic syndrome | L5 | Hold | No evidence; antibiotics may increase toxin release in Shiga toxin-producing *E. coli* infection, a safety concern |
| Exposure keratitis | L4 | Hold | Literature is off-target |
| Chronic gingivitis | L3 | Research Question | Supportive periodontitis studies, but the exact condition is not established, and doxycycline is already approved for periodontitis |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

