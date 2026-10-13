---
layout: default
title: Adapalene
parent: Low Evidence (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Adapalene
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

# Adapalene: From Acne to Zinc, Elevated Plasma

## One-Sentence Summary

Adapalene is a topical retinoid originally used to treat acne.
The TxGNN model predicts it may be effective for **elevated plasma zinc** (the top-ranked prediction), but **no clinical trials and no publications** support this direction, so the prediction rests on model output alone.
The best-supported candidates in the list are seborrheic dermatitis and sebaceous gland anomaly, and even these have only indirect evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne (acne vulgaris) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Adapalene is known as a topical retinoid that acts on retinoic acid receptors (RAR-beta/gamma). It normalizes follicular keratinization and has anti-inflammatory effects. Its efficacy in acne is established.

For the top prediction, **elevated plasma zinc**, no mechanistic link to a topical retinoid could be identified. The high score (99.51%) is a graph-based prediction only, and there are no supporting trials or publications. The prediction should therefore be treated as a model artefact until shown otherwise.

Other predicted indications fall into three groups:

- **Dermatological conditions with some plausibility (indirect only):** Seborrheic dermatitis (86.28%), sebaceous gland anomaly (85.16%) and demodicidosis of the sebaceous gland (95.45%) involve follicular and sebaceous pathology that overlaps with acne. Retinoids normalize follicular keratinization, so a link is conceivable, but no direct evidence was found.
- **Genetic or metabolic conditions with no plausible mechanism:** Isolated congenital adermatoglyphia (SMARCAD1 variants), Beare-Stevenson cutis gyrata syndrome (FGFR2 gain-of-function) and prolidase deficiency (PEPD enzyme defect) have causes that a topical retinoid is not expected to correct.
- **Other:** PAPA syndrome is an IL-1-driven autoinflammatory disease, and adapalene might at most affect the acne component. Drug-induced osteoporosis raises a directional concern, because systemic retinoids are associated with adverse bone effects, though topical adapalene has minimal systemic absorption. Inherited skin tumour is a heterogeneous category with no adapalene-specific evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked indication, or for any other predicted indication in the list.

## Literature Evidence

No literature is available for the top-ranked indication (elevated plasma zinc). The publications below were retrieved for lower-ranked candidates, and all are indirect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39069843](https://pubmed.ncbi.nlm.nih.gov/39069843/) | 2024 | RCT (acne) | Italian Journal of Dermatology and Venereology | Randomized, double-blind trial of adapalene 0.3%/benzoyl peroxide 2.5% gel in Korean patients with acne, with histopathological and immunohistochemical analysis. Retrieved under seborrheic dermatitis, but it concerns acne. |
| [25217865](https://pubmed.ncbi.nlm.nih.gov/25217865/) | 2014 | Preclinical animal study | Journal of Dermatological Science | 0.1% adapalene was tested in a non-inflammatory Kyoto Rhino Rat acne model with comedones. Retrieved under sebaceous gland anomaly. |
| [36102580](https://pubmed.ncbi.nlm.nih.gov/36102580/) | 2022 | Clinical study | Journal of Cosmetic Dermatology | Moisturizer with licochalcone A, 1,2-decanediol, L-carnitine and salicylic acid, studied for effects on facial skin lipids in people with seborrhea. It does not involve adapalene. |
| [27504089](https://pubmed.ncbi.nlm.nih.gov/27504089/) | 2016 | Case report | Case Reports in Dermatology | Localized late-onset Darier's disease presenting as inframammary dermatitis. It does not involve adapalene. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11116P | DIFFERIN CREAM 0.1% | Cream | Not listed in the compiled data |
| SIN08957P | DIFFERIN GEL 0.1% | Gel | Not listed in the compiled data |
| SIN15460P | EPIDUO FORTE GEL 0.3%/2.5% | Gel | Not listed in the compiled data |
| SIN13789P | EPIDUO GEL 0.1%/2.5% | Gel | Not listed in the compiled data |

All four authorizations are valid and topical (cream or gel). The Epiduo products are adapalene/benzoyl peroxide combinations.

## Safety Considerations

- **Knowledge-graph contraindication signals:** The knowledge graph links adapalene to photoparoxysmal response, photosensitivity disease, exfoliative dermatitis and dermatitis. These come from graph edges, not from package insert text, and need confirmation against the label.
- **Drug Interactions:** The interaction screen returned 58 interacting drugs, but severity levels are all unclassified. Examples include doxycycline, tetracycline, minocycline, metronidazole, prednisone, triamcinolone, budesonide, omeprazole, pantoprazole, ibuprofen, fluconazole and clopidogrel.
- **Systemic retinoid concern:** For drug-induced osteoporosis, systemic retinoids are associated with adverse bone effects. Topical adapalene has minimal systemic absorption, but the directional concern is theoretical and unconfirmed.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (elevated plasma zinc) has a high model score but no trials, no publications and no plausible mechanism, so the evidence level is L5. Only seborrheic dermatitis and sebaceous gland anomaly reach L4, and that evidence is indirect (acne studies and an animal model).

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, which are currently missing and block safety screening
- Detailed mechanism of action data (for example from DrugBank)
- Direct clinical or preclinical studies of adapalene in seborrheic dermatitis, demodicidosis or sebaceous gland disorders, if these are prioritized as research questions
- Confirmation of the knowledge-graph contraindication signals (photosensitivity, dermatitis) against the label
- Severity classification of the 58 drug interactions
- A decision on whether to deprioritize the elevated plasma zinc prediction, because no mechanistic rationale exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

