---
layout: default
title: Crotamiton
parent: Low Evidence (L5)
nav_order: 282
evidence_level: L5
indication_count: 10
---

# Crotamiton
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

# Crotamiton: From Scabies to Trombiculiasis

## One-Sentence Summary

Crotamiton is a topical scabicide and antipruritic (anti-itch) agent, originally used to treat scabies and relieve itching.
The TxGNN model predicts it may be effective for **trombiculiasis** (chigger mite dermatitis), but **no clinical trials or publications** currently support this direction, so the prediction rests on model output and indication similarity alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Scabies (including Norwegian scabies) and mite infestation; itch relief (the Singapore licence records contain no indication text) |
| Predicted New Indication | Trombiculiasis |
| TxGNN Prediction Score | 96.24% |
| Evidence Level | L5 (model prediction only, no actual studies) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

*Note: The data compiled for this report labels this candidate L4 with a "Research Question" recommendation, based on indirect pharmacological reasoning. Under the standard evidence rules (no clinical trials, no literature), it falls at L5. The Hold decision reflects that gap, while the biological plausibility justifies keeping it as a research question.*

---

## Why is This Prediction Reasonable?

Crotamiton is a scabicidal agent whose exact mechanism of action against mites is unknown. Its general antipruritic effect has been linked to inhibition of the TRPV4 (transient receptor potential vanilloid 4) channel, which is expressed in the skin and in primary sensory neurons. Detailed mechanism of action data are otherwise not available.

Trombiculiasis is a mite-induced itchy skin condition caused by chigger larvae. It shares two features with crotamiton's established uses: a mite-related cause (as in scabies, caused by *Sarcoptes scabiei*) and intense itching. Crotamiton is also already used for itching from insect bites and stings, which are clinically similar to chigger bites. This makes the extension biologically plausible, and it likely explains the high TxGNN score.

However, this reasoning is indirect. It is based on similarity of indication and pharmacological class, not on clinical data in trombiculiasis. Antipruritic benefit may be achievable even where mite-killing activity is not relevant, since chigger larvae do not burrow and live in the skin as scabies mites do.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN04958P | Crotamiton Lotion 10% v/v | Lotion | Not stated in the licence record |
| SIN04689P | Crotamiton Cream 10% v/w | Cream | Not stated in the licence record |
| SIN08812P | Guardian Anti-Itch Cream | Cream | Not stated in the licence record |

All three licences are valid, single-ingredient products from Sunward Pharmaceutical Private Limited. Both products are topical (lotion and cream).

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: Dermatitis is recorded as a contraindication-linked disease in the TxGNN knowledge graph. This should be verified against the official label, because crotamiton is also used for itchy dermatitis according to pharmacology sources.
- **Drug Interactions**: No conventional drug-drug interactions were identified. The only entry is a pharmacological target relationship: crotamiton inhibits the TRPV4 channel, which is the proposed basis of its anti-itch effect.

For other safety information, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Trombiculiasis is the only one of the ten predictions with a plausible mechanistic link, but there are no trials or publications to support it. The other nine predictions (for example, sacrum chordoma, abdominal ectopic pregnancy, and hordeolum) have no mechanistic rationale and look like graph-based artifacts. They should not be pursued.

**To proceed, the following is needed:**
- A literature and trial search specific to crotamiton in trombiculiasis (chigger bites)
- Package insert warnings and contraindications from the HSA website, to enable safety screening
- Detailed mechanism of action data, especially whether crotamiton has any activity against chigger larvae or acts only as an antipruritic
- Clarification of the approved indication wording for the three Singapore licences
- Confirmation that the existing topical cream and lotion are suitable for the intended use (route compatibility is still pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

