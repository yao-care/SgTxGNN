---
layout: default
title: Umeclidinium
parent: Low Evidence (L5)
nav_order: 1040
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Umeclidinium: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the Singapore licence records (the products are inhaled…"
monitor_inn: "Umeclidinium"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "open-angle glaucoma", "primary hereditary glaucoma", "nephrogenic syndrome of inappropriate antidiuresis", "gastroduodenitis", "common cold", "atrophoderma vermiculata", "peptic ulcer disease", "allergic urticaria"]
---

# Umeclidinium
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

# Umeclidinium: From Respiratory Disease (COPD) to Migraine Disorder

## One-Sentence Summary

Umeclidinium is an inhaled long-acting muscarinic antagonist (LAMA) marketed in Singapore as a single-ingredient product and as a component of two combination inhalers. The TxGNN model predicts it may be effective for **migraine disorder**, but **no clinical trials and no supporting publications** were found for this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records (the products are inhaled LAMA-containing inhalers) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 96.36% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, umeclidinium is an inhaled long-acting muscarinic antagonist, used alone or in combination with other inhaled agents. It blocks muscarinic receptors in the airways.

Muscarinic signalling has been loosely discussed in central pain and neurovascular pathways, which may explain why the model links the drug to migraine. However, the mechanistic route is weak. Inhaled umeclidinium has low systemic exposure and limited central nervous system penetration, so it is unlikely to reach the sites relevant to migraine. The high score is a graph-based prediction only.

The other top predictions point the same way. Migraine with brainstem aura is a subtype of the same condition. Glaucoma predictions are more likely to reflect a safety concern than a therapeutic opportunity, because anticholinergics can precipitate angle-closure glaucoma. Gastric conditions (gastroduodenitis, peptic ulcer disease) have a class-level rationale, but low systemic exposure after inhalation makes an effect unlikely. The remaining predictions (nephrogenic syndrome of inappropriate antidiuresis, atrophoderma vermiculata, allergic urticaria, common cold) have no plausible mechanistic support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for migraine disorder.

For reference, the only publication linked to any of the top 10 predictions is a general COPD review, linked to the common cold prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29583021](https://pubmed.ncbi.nlm.nih.gov/29583021/) | 2018 | Review | COPD | Annual review of COPD studies, including fluticasone furoate/vilanterol/umeclidinium in severe COPD. It does not study umeclidinium in the common cold. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14853P | INCRUSE ELLIPTA Inhalation Powder 62.5 mcg/dose | Powder, metered | Not stated in the records |
| SIN15806P | TRELEGY ELLIPTA Inhalation Powder 100 mcg/62.5 mcg/25 mcg | Powder, metered | Not stated in the records |
| SIN14838P | ANORO ELLIPTA Inhalation Powder 62.5 mcg/25 mcg | Powder, metered | Not stated in the records |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs. The 20 shown in the data compiled for this report were all rated **Moderate**. Most are other anticholinergic or antimuscarinic agents, where additive anticholinergic effects are the concern:
  - Hyoscyamine, atropine, glycopyrronium (including topical), clidinium, dicyclomine, trospium, mepenzolate, methscopolamine, propantheline, scopolamine, aclidinium
  - Antihistamines with anticholinergic activity: promethazine, chlorpheniramine, acrivastine
  - Others: eluxadoline, prucalopride, inhaled human insulin, ophthalmic physostigmine, acetylcholine
- **Class-level caution (from the prediction rationale)**: Anticholinergics can precipitate or worsen angle-closure glaucoma, and the umeclidinium label carries a narrow-angle glaucoma warning. They can also cause urinary retention. This matters particularly for the glaucoma predictions, which are a potential safety concern rather than a therapeutic opportunity.

Please refer to the package insert for warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction has a high model score but no clinical trials or literature behind it, and the mechanism is weak because inhaled umeclidinium has low systemic and central nervous system exposure. The other top predictions are also unsupported, and the glaucoma predictions point to a safety risk.

**To proceed, the following is needed:**
- Official package insert warnings and contraindications from the HSA website, and the approved indication text for the three licences
- Mechanism of action data from DrugBank
- Preclinical or mechanistic evidence for muscarinic antagonism in migraine
- Evidence that a route and dose could achieve relevant exposure, since route compatibility has not been assessed
- Review of the safety profile, particularly narrow-angle glaucoma and urinary retention, before any repurposing study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

