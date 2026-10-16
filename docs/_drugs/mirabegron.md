---
layout: default
title: Mirabegron
parent: Low Evidence (L5)
nav_order: 679
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Mirabegron: predicted new indication Thoracic malformation (evidence level L5). Approved use: Overactive bladder"
---

# Mirabegron
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

# Mirabegron: From Overactive Bladder to Thoracic Malformation

## One-Sentence Summary

Mirabegron is a drug originally used to treat overactive bladder.
The TxGNN model predicts it may be effective for **thoracic malformation**, but **no clinical trials and no publications** currently support this direction. The prediction rests on the graph-based model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Overactive bladder (the Singapore licence records contain no indication text, so this comes from the knowledge-graph indication data) |
| Predicted New Indication | Thoracic malformation |
| TxGNN Prediction Score | 83.06% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacological knowledge, mirabegron is a beta-3 adrenergic agonist that relaxes the detrusor (bladder) smooth muscle, which is how it helps in overactive bladder.

Thoracic malformation is a developmental (structural) condition. No pathway connecting beta-3 adrenergic agonism to thoracic development is supported by the data compiled for this report. The score of 0.831 is a graph-based statistical association only, and the model ranked this prediction at 40,334, so it should be treated as a hypothesis, not a finding.

The other top-ranked predictions are also unsupported. All ten have no trials or literature, and several are rare genetic conditions, such as ciliopathies and monogenic hair disorders, with no plausible link to beta-3 agonism. Two carry theoretical concerns:
- **Polycystic kidney disease:** cyst growth is driven by cAMP signalling, which beta-3 agonism could theoretically worsen.
- **Esophageal varices:** the standard of care is beta-1/2 blockade, which is the opposite direction to beta-3 agonism. Bleeding settings also raise safety concerns.

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
| SIN14622P | BETMIGA Prolonged-Release Tablets 25 mg | Film-coated extended-release tablet | Not recorded in the licence data |
| SIN14623P | BETMIGA Prolonged-Release Tablets 50 mg | Film-coated extended-release tablet | Not recorded in the licence data |

Both licences are valid single-ingredient products, with no cancelled registrations. Both are oral formulations.

---

## Safety Considerations

- **Contraindications (knowledge-graph data, not label text):** the knowledge graph links mirabegron with hypertensive disorder and hypertension as contraindicated conditions. This needs checking against the package insert.
- **Drug Interactions:** 70 interactions were identified in total. A sample of 20 is available, including:
  - **Major:** eliglustat
  - **Moderate:** lorcaserin, trospium, metoclopramide, dexfenfluramine, fenfluramine, glycerol phenylbutyrate, promethazine, lusutrombopag, fostamatinib
  - **Minor:** aprepitant, dexamethasone, cimetidine, clarithromycin, miconazole, clotrimazole, troglitazone, cobicistat, deferasirox, warfarin

For other safety information, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (evidence level L5), and there is no plausible mechanistic link between beta-3 agonism and thoracic malformation. The knowledge graph also flags hypertension as a contraindication. Repurposing is not justified on the current data.

**To proceed, the following is needed:**
- Mechanism of action data for mirabegron, to allow a proper mechanistic analysis
- Package insert warnings and contraindications from the HSA, since safety screening cannot proceed without them
- Preclinical or mechanistic evidence linking beta-3 signalling to thoracic development
- Review of the hypertension contraindication and the major interaction with eliglustat
- Route compatibility and similarity-to-original-indication assessments, which are still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

