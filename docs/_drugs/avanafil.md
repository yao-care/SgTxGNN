---
layout: default
title: Avanafil
parent: Low Evidence (L5)
nav_order: 123
evidence_level: L5
indication_count: 10
---

# Avanafil
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

# Avanafil: From Erectile Dysfunction to Amenorrhea

## One-Sentence Summary

Avanafil is an oral PDE5 inhibitor marketed in Singapore as Spedra. The Singapore registry data supplied here does not record its approved indication; it is generally used for erectile dysfunction.
The TxGNN model predicts it may be effective for **amenorrhea**, but **no clinical trials and no relevant publications** support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied registry data (PDE5 inhibitors are generally used for erectile dysfunction; not verified from this pack) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 94.59% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Avanafil is a PDE5 inhibitor, which raises cGMP and promotes vasodilation.

Amenorrhea is mainly a disorder of the hypothalamic-pituitary-ovarian axis, and no clear link to the cGMP/vasodilation pathway was identified. The high score (0.946) is not supported by any trial or literature. Treat it as an unexplained model output, not a mechanistic lead.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15880P | SPEDRA TABLET 50MG | Tablet | Not stated in registry data |
| SIN15879P | SPEDRA TABLET 100MG | Tablet | Not stated in registry data |
| SIN15881P | SPEDRA TABLET 200MG | Tablet | Not stated in registry data |

All three are held by MENARINI VON HEYDEN GmbH and are oral tablets.

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records. This means nothing was found, not that no interactions exist.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials, no relevant literature and no plausible mechanistic link between PDE5 inhibition and amenorrhea. Safety data (warnings and contraindications) is also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications, approved indication)
- Mechanism of action data from DrugBank
- A targeted trial and literature search for avanafil or PDE5 inhibitors in amenorrhea, and an expert view on whether a rationale exists

**Other candidates in this run:** Raynaud disease (score 88.5%, also L5) is the most biologically plausible, since PDE5-mediated vasodilation is relevant to vasospasm. It is flagged as a "Research Question" and merits a targeted search before this amenorrhea prediction does. The remaining candidates are Hold. Several are veterinary or obsolete ontology terms (malignant catarrh, infectious bovine rhinotracheitis, obsolete susceptibility to ischemic stroke), which look like knowledge-graph artifacts.

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

