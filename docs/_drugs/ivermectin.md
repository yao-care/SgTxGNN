---
layout: default
title: Ivermectin
parent: Low Evidence (L5)
nav_order: 561
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ivermectin: predicted new indication Vulvovaginal candidiasis (evidence level L5). Approved use: Strongyloidiasis, onchocerciasis"
monitor_inn: "Ivermectin"
predicted_indications: ["vulvovaginal candidiasis", "esophageal candidiasis", "anogenital human papillomavirus infection", "vulvovaginitis", "candida glabrata", "neonatal candidiasis", "congenital candidiasis", "postmenopausal atrophic vaginitis", "candidiasis, invasive", "vulvitis"]
---

# Ivermectin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Ivermectin: From Strongyloidiasis and Onchocerciasis to Vulvovaginal Candidiasis
{: .text-alpha }

## One-Sentence Summary

Ivermectin is an antiparasitic drug, originally used to treat strongyloidiasis and onchocerciasis.
The TxGNN model predicts it may be effective for **vulvovaginal candidiasis**, with a very high score, but **0 clinical trials** and **0 publications** currently support this direction.
This is a model prediction only and is not backed by actual studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Strongyloidiasis, onchocerciasis |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, ivermectin acts on glutamate-gated chloride channels in invertebrates, which causes paralysis and death of parasites. Its efficacy in strongyloidiasis and onchocerciasis is well established.

Vulvovaginal candidiasis is a fungal infection. Fungal cells have no clear equivalent of the glutamate-gated chloride channel target, so no mechanistic link between ivermectin's known action and this condition can be confirmed. The high TxGNN score (0.9995) most likely reflects proximity within the knowledge graph (for example, to other candidiasis-related nodes) rather than demonstrated antifungal activity.

The other top predictions are mostly related conditions (other forms of candidiasis, vulvovaginitis, vulvitis, anogenital HPV infection). None has clinical trials or supporting literature. Two of them have retrieved papers (esophageal candidiasis and congenital candidiasis), but these describe approved antiparasitic uses (strongyloidiasis and scabies) and are not evidence for antifungal use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for vulvovaginal candidiasis.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15197P | SOOLANTRA CREAM 10MG/G | Cream | Not stated in the data compiled |

Ivermectin is registered in Singapore as a single-ingredient topical cream. The oral formulations used for strongyloidiasis and onchocerciasis are not among the registrations in the data compiled for this report.

---

## Safety Considerations

- **Contraindications (from knowledge graph, not label text)**: loiasis and filariasis are listed as disease contraindications for ivermectin.
- **Drug Interactions**: 100 interactions were identified. Examples of moderate-level interactions include:
  - Warfarin and dicoumarol (anticoagulants)
  - Clarithromycin and cobicistat (CYP3A4 inhibitors)
  - Aprepitant
  - Deferasirox
  - Fostamatinib
  - Ethanol
  - Radioactive iodide (I-123, I-131)
  - Abametapir (topical)

  Other interactions, such as with omeprazole, prednisone and heparin, have an unclassified severity level.
- **Special population note**: Use in neonates would need careful safety evaluation, because data in young infants are limited and blood-brain barrier function is immature.

Please refer to the package insert for warnings and other safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no clinical trials, no relevant publications, and no plausible mechanism, since fungal cells lack a clear target for ivermectin. The two papers that were retrieved concern antiparasitic uses and do not support the antifungal prediction.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (a blocking gap for safety screening)
- Mechanism of action data for ivermectin (for example, from DrugBank)
- In vitro antifungal activity data against *Candida* species, including *C. albicans* and *C. glabrata*
- Preclinical or early clinical studies in vulvovaginal candidiasis
- Assessment of route compatibility between the registered topical cream and the intended use
- Comparison against current antifungal standards of care (azoles and echinocandins)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

