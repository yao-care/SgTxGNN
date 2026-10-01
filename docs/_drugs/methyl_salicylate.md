---
layout: default
title: Methyl Salicylate
parent: Low Evidence (L5)
nav_order: 654
evidence_level: L5
indication_count: 10
---

# Methyl Salicylate
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

# Methyl Salicylate: From Topical Analgesic Use to Gout

## One-Sentence Summary

Methyl salicylate is a topical salicylate used in rubs and lotions. The TxGNN model predicts it may be effective for **gout**, but **0 clinical trials** and only **1 publication** (an unrelated grapevine study) support this. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the registration data. The one Singapore product is a lotion named "Robinson Ringworm and Whitespot Lotion" |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 98.86% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Methyl salicylate is a salicylate, and topical products use it as a counter-irritant that delivers salicylate locally for muscle and joint pain. A link to gout could come from the anti-inflammatory and uricosuric effects of salicylates.

That link is weak here. Those effects occur at systemic doses, and topical methyl salicylate does not reach comparable levels. The single retrieved paper is a plant science study and says nothing about human gout. The high score most likely reflects proximity in the knowledge graph rather than a real therapeutic signal.

For context, other predicted indications are better supported. **Osteoarthritis** has the strongest support (evidence level L3), with a 1956 uncontrolled topical evaluation, a plaster RCT whose composition is unverified, reviews of topical therapy, and safety reports. **Rheumatoid arthritis** has preclinical support only (L4), and that work used methyl salicylate glycosides rather than the marketed compound. Both mostly overlap with the drug's existing use as a topical pain reliever, so they are weak repurposing signals.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26042139](https://pubmed.ncbi.nlm.nih.gov/26042139/) | 2015 | Basic plant science | Front Plant Sci | Volatile compounds as markers of elicitor response in grapevine. Not relevant to gout or human use |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08677P | Robinson Ringworm and Whitespot Lotion | Lotion | Not stated in the registration data |

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records. Published literature does report that topical methyl salicylate can potentiate warfarin (PMID 2778785, case-level), and that topical salicylate products can cause toxicity (PMID 18091121).
- **Heart failure**: Salicylates and NSAIDs can cause fluid retention, which matters if the drug were used in patients with heart failure.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The gout prediction has no clinical trials and no relevant literature, and the systemic mechanism that might link salicylates to gout does not apply to a topical lotion. The drug stays at evidence level L5 and at the first screening stage.

**To proceed, the following is needed:**
- The HSA package insert, for warnings and contraindications. This gap currently blocks safety screening.
- Mechanism of action data from DrugBank.
- A stated approved indication for the Singapore product.
- If a topical joint-pain indication is pursued, review osteoarthritis rather than gout. That would need a controlled trial with guardrails for anticoagulant (warfarin) interaction and salicylate toxicity.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

