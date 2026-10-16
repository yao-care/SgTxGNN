---
layout: default
title: Alectinib
parent: Low Evidence (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Alectinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Non-small cell lung carcinoma / lung cancer"
---

# Alectinib
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

# Alectinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Alectinib is an oral ALK inhibitor originally used to treat non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **hereditary gingival fibromatosis**,
but **no clinical trials and no publications** currently support this prediction, so it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung carcinoma / lung cancer (the Singapore licence text does not state an approved indication) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on known information, alectinib is a selective inhibitor of anaplastic lymphoma kinase (ALK), and its efficacy in ALK-positive NSCLC is well established. The published literature also describes activity against RET.

For gingival fibromatosis, the plausibility is weak. No known ALK-driven mechanism links alectinib to hereditary gingival fibromatosis, and no ALK alteration has been described in this condition. The very high score (99.97%) is therefore best read as a pattern from the knowledge-graph network, not as evidence of a biological link. Many other diseases received almost identical scores (>99.95%), including conditions with no plausible ALK link, which suggests that these scores do not discriminate well between candidates.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15220P | ALECENSA HARD CAPSULE 150MG | Capsule (oral) | Not stated in the available licence record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (published case reports describe haemolytic anaemia, and anaemia is generally mild) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; typically blood counts, liver function and creatine phosphokinase, plus lipid levels, weight and heart rate, based on published adverse-event reports |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Package-insert warnings and contraindications were not available in the data compiled for this report, so please refer to the package insert for safety information.

- **Drug Interactions**: 92 interactions are recorded (DDInter). Examples at **Major** level: aminolevulinic acid. Examples at **Moderate** level: dolasetron, naltrexone, mefloquine, quinine, atazanavir, bedaquiline, and the beta-blockers atenolol, bisoprolol, acebutolol and betaxolol. Several of these relate to QT prolongation or bradycardia, which is consistent with published alectinib electrophysiology data. Cholinesterase-related agents (edrophonium, physostigmine, ambenonium) are also listed.
- **Adverse events reported in the literature**: hypertriglyceridaemia-induced pancreatitis, haemolytic anaemia, DRESS syndrome, erythema multiforme, weight gain, and QT/cardiac effects (case reports and pharmacovigilance analyses).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the TxGNN model score. There are no clinical trials or publications for gingival fibromatosis, and no plausible ALK-related mechanism. The strong evidence for alectinib (ALEX, J-ALEX, ALINA) applies to its existing NSCLC indication, not to this one.

**To proceed, the following is needed:**
- Evidence of any ALK or ALK-pathway involvement in gingival fibromatosis (genetic or expression data)
- Preclinical data supporting efficacy in this condition
- Mechanism-of-action data for alectinib
- Package-insert warnings and contraindications from HSA, which are required before any safety screening
- A risk-benefit assessment, since a systemic kinase inhibitor with a notable adverse-event profile would be used for a benign condition

**Note on other predictions:** The other top-ranked predictions do not change the overall picture. Most (fibroma of lung, hamartoma of lung, pulmonary sulcus neoplasm, and several rare genetic disorders) have no trials or literature. The lung benign neoplasm match reflects evidence for the already-approved NSCLC indication, not benign tumours. The most biologically interesting candidate is **lung germ cell tumor** (indirect support from case reports of alectinib in ALK-rearranged neuroendocrine and other rare tumours), but its single trial (NCT04644315, Phase 2, terminated, 1 participant) is uninformative. All were assigned Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

