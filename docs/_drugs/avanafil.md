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

Avanafil is an oral PDE5 inhibitor originally used to treat erectile dysfunction.
The TxGNN model predicts it may be effective for **amenorrhea**,
but **no clinical trials and no publications** currently support this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Erectile dysfunction (also psychologic dyspareunia and premature ejaculation, per the knowledge graph; the Singapore licence records contain no indication text) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 94.59% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, avanafil is a PDE5 inhibitor. It raises cGMP levels and promotes smooth muscle relaxation and vasodilation, which underlies its effect in erectile dysfunction.

A hypothetical link to uterine or pelvic blood flow exists. However, amenorrhea is mainly driven by dysfunction of the hypothalamic-pituitary-ovarian axis, so the connection to PDE5 inhibition is weak. The high TxGNN score is a computational output without clinical or literature support, and it should be treated as a hypothesis rather than a finding.

**Other predictions reviewed (all L5, no trials or publications):**

| Rank | Predicted Disease | Score | Assessment |
|------|------|------|------|
| 2 | Hypoalphalipoproteinemia | 91.54% | No clear link between PDE5 inhibition and HDL metabolism |
| 3 | Malignant catarrh | 90.62% | Veterinary viral disease in ruminants; likely a knowledge-graph artifact |
| 4 | Infectious bovine rhinotracheitis | 90.62% | Cattle herpesvirus infection; likely a knowledge-graph artifact |
| 5 | Raynaud disease | 88.54% | Biologically the most plausible; sildenafil and tadalafil have been studied, but there is no avanafil-specific evidence |
| 6 | Ambras type hypertrichosis universalis congenita | 87.79% | Rare hair-follicle development disorder; no link to the PDE5/cGMP pathway |
| 7 | Obsolete susceptibility to ischemic stroke | 87.28% | Obsolete ontology term; not a suitable clinical target |
| 8 | Malformation syndrome with odontal and/or periodontal component | 80.46% | Heterogeneous congenital syndromes; not mechanistically interpretable |
| 9 | Stroke disorder | 79.21% | Plausible but indirect preclinical rationale for the class |
| 10 | Adrenal gland hyperfunction | 79.06% | No established link |

Raynaud disease is the only alternative flagged as a research question. Any further work would first require a separate review of class-level PDE5 inhibitor evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15880P | SPEDRA TABLET 50MG | Tablet | Not listed in the data |
| SIN15879P | SPEDRA TABLET 100MG | Tablet | Not listed in the data |
| SIN15881P | SPEDRA TABLET 200MG | Tablet | Not listed in the data |

All three are single-ingredient products from MENARINI VON HEYDEN GmbH, and all are currently valid. Only the oral route is available.

## Safety Considerations

- **Drug Interactions**: 53 known interactions were identified. Examples by severity:
  - **Major**: Aprepitant, Clarithromycin, Amyl Nitrite, Cobicistat
  - **Moderate**: Canagliflozin, Dapagliflozin, Empagliflozin, Ertugliflozin, Dexamethasone, Lorcaserin, Papaverine, Troglitazone, Ethanol, Deferasirox, Diazoxide, Phentolamine, Nitrous acid, Fostamatinib, Epoprostenol, Iloprost
- Cardiovascular safety (hypotension, interactions with nitrates and antihypertensives) would need review in any new patient population, particularly stroke.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The amenorrhea prediction has a high model score but no clinical trials or publications behind it, and the mechanistic link is weak. Evidence is L5 (model prediction only), so there is not enough support to move forward.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (needed before any safety screening)
- Detailed mechanism of action data from DrugBank
- Clinical or mechanistic evidence specific to avanafil in amenorrhea
- If a more plausible direction is wanted, a separate review of PDE5 inhibitor class evidence for Raynaud disease
- A safety plan for the cardiovascular and drug-interaction risks in any new target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

