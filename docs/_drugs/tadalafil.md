---
layout: default
title: Tadalafil
parent: Low Evidence (L5)
nav_order: 938
evidence_level: L5
indication_count: 10
---

# Tadalafil
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

# Tadalafil: From Its Registered Uses to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tadalafil is a PDE5 inhibitor marketed in Singapore, but the registration records provided do not state its approved indication.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita** with a very high score, but **no clinical trials and no publications** support this prediction.
It is most likely a knowledge-graph artifact, and the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records provided |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Tadalafil is generally known as a PDE5 inhibitor that raises intracellular cGMP, but this evidence pack does not document its original indications.

On this basis, the prediction is **not mechanistically supported**:

- Ambras syndrome is a genetic disorder caused by a chromosome 8q22 position effect that alters regulation of the *TRPS1* gene. No known pathway connects PDE5/cGMP signaling to this mechanism.
- The condition involves excess hair growth. A drug that reduces hair growth would be needed, and nothing suggests tadalafil does this.
- The high score probably reflects graph propagation through shared hair-phenotype nodes, not a real pharmacological link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Tadalafil has 20 registrations in Singapore. Five main ones are shown below. The approved indication text is not available in the records provided.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|------|
| SIN16935P | A-Tadalafil Film-Coated Tablets 10 mg | Film-coated tablet | Micro Labs Limited |
| SIN16885P | Tadalafil-Teva FC Tablet 5 mg | Film-coated tablet | Teva Pharma, S.L.U. |
| SIN15899P | Caliberi Orodispersible Film 5 mg | Soluble film | CTCBIO Inc. |
| SIN16134P | Tadafil 2.5 Tadalafil Tablets USP 2.5 mg | Film-coated tablet | Hetero Labs Limited |
| SIN16132P | Tadafil 10 Tadalafil Tablets USP 10 mg | Film-coated tablet | Hetero Labs Limited |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records (not found). This does not mean no interactions exist.
- **Migraine signal**: A 2006 case report ([PMID 17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/), *Cephalalgia*) describes tadalafil associated with typical migraine aura without headache. This matters for the lower-ranked migraine predictions, which are not supported as treatment targets.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no trials, no literature, and no plausible mechanism, and it is likely a graph-propagation artifact. The other nine predictions reviewed (Evidence Level L4–L5, all Hold) are also unsupported:

- **Hair and skin conditions** (hypertrichosis, isolated genetic hair shaft abnormality, familial isolated trichomegaly, hypotrichosis simplex of the scalp): no established link.
- **Malformation syndromes** (Dandy-Walker feature, odontal/periodontal component): no plausible mechanism. The periodontal literature is general periodontitis literature that never mentions tadalafil.
- **Migraine** (with brainstem aura, and migraine disorder): the only evidence is the adverse-event case report above, which argues against this direction.
- **Kyphoscoliotic heart disease**: the only indirectly plausible candidate. Kyphoscoliosis can cause secondary pulmonary hypertension, which PDE5 inhibition could theoretically help. There are no trials or literature, and evidence in similar pulmonary hypertension groups has been mixed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (this blocks any safety screening)
- The drug's original indications and mechanism of action (e.g., from the DrugBank API)
- For kyphoscoliotic heart disease, a targeted literature search on PDE5 inhibitors in secondary pulmonary hypertension
- Any preclinical or clinical data specific to tadalafil in the predicted conditions before reconsidering the hair-related predictions

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

