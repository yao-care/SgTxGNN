---
layout: default
title: Dexchlorpheniramine Maleate
parent: 僅模型預測 (L5)
nav_order: 234
evidence_level: L5
indication_count: 10
---

# Dexchlorpheniramine Maleate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Dexchlorpheniramine Maleate: From Allergic Rhinitis to Acute Intermittent Porphyria

## One-Sentence Summary

Dexchlorpheniramine maleate is a first-generation H1 antihistamine, classically used for symptomatic relief of allergic rhinitis, urticaria, and related hypersensitivity reactions. The TxGNN model predicts it may be effective for **Acute Intermittent Porphyria (AIP)** as its highest-ranked candidate (score 99.12%), yet this is currently supported by **no clinical trials** and **no published literature**. The mechanistic link is not established and carries an active porphyria-specific safety concern; of the 10 predicted indications evaluated, **Allergic Urticaria (rank #6, L3 evidence)** represents the only candidate with actionable clinical support.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis, urticaria (first-generation H1 antihistamine; no Singapore HSA registration on record) |
| Predicted New Indication | Acute Intermittent Porphyria |
| TxGNN Prediction Score | 99.12% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Dexchlorpheniramine maleate is the pharmacologically active dextro-enantiomer of chlorpheniramine — a first-generation, sedating H1 receptor competitive antagonist. It blocks peripheral and central histamine H1 receptors, suppressing vascular dilation, increased capillary permeability, and pruritic signalling that characterise allergic reactions. It also carries notable anticholinergic activity and readily crosses the blood-brain barrier, accounting for its CNS sedative effects.

Acute Intermittent Porphyria is a metabolic disorder driven by loss-of-function mutations in the *HMBS* gene, resulting in impaired haem biosynthesis and toxic accumulation of δ-aminolevulinic acid (ALA) and porphobilinogen (PBG) — neurotoxic precursors responsible for the autonomic, motor, and psychiatric symptoms of acute attacks. The core pathophysiology is fundamentally unrelated to histamine receptor signalling; H1 receptor antagonism has no known direct regulatory interaction with the haem biosynthesis pathway.

The high TxGNN score (0.9912) most likely reflects indirect connections through comorbidity networks or shared symptom nodes in the knowledge graph — for example, psychiatric or autonomic symptoms appearing as shared graph neighbours — rather than a true therapeutic mechanistic link. Critically, British and South African Porphyria guidelines classify certain drugs (including members of the first-generation antihistamine class) under "use with caution" or safety-uncertain categories due to the theoretical risk of precipitating acute attacks. This prediction is mechanistically unsupported and carries an active safety signal that must be resolved before any further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Dexchlorpheniramine maleate has **no Health Sciences Authority (HSA) product registrations** in Singapore. This drug is not currently marketed in Singapore under any dosage form or brand name.

---

## Safety Considerations

**Important porphyria-specific safety signal:** British and South African Porphyria guidelines list certain first-generation antihistamines under categories requiring caution or with undefined safety status in acute porphyrias. Use in AIP patients carries a potential risk of precipitating an acute attack. Any further evaluation must first verify this drug's porphyria safety classification against current databases (e.g., [www.drugs-porphyria.org](https://www.drugs-porphyria.org)).

For general safety information including CNS sedation, anticholinergic effects, and age-related contraindications, please refer to the drug's package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial evidence, no supporting literature, and no established mechanistic rationale connecting dexchlorpheniramine maleate to the treatment of Acute Intermittent Porphyria. The additional porphyria-specific safety signal makes this a low-priority repurposing direction without substantially more data to resolve both efficacy and safety unknowns.

**To proceed, the following is needed:**
- Verify this drug's porphyria safety classification via a recognised porphyria drug safety database (e.g., www.drugs-porphyria.org) — this is a **blocking prerequisite** before any further work
- Obtain complete TFDA/HSA-equivalent package insert to assess full warning and contraindication profile (currently a blocking data gap)
- Obtain detailed MOA data from DrugBank (DB09555) to determine whether any pleiotropic mechanism could interact with haem biosynthesis
- Generate a preclinical mechanistic hypothesis supported by basic science evidence before advancing to clinical consideration
- **If pivoting to Allergic Urticaria (rank #6, L3 evidence, "Proceed with Guardrails"):** this indication carries a direct mechanistic rationale and has 6 supporting publications including a comparative RCT-level study (PMID 39265704); it represents the only actionable repurposing candidate in this Evidence Pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

