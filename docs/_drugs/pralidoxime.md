---
layout: default
title: Pralidoxime
parent: Low Evidence (L5)
nav_order: 816
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pralidoxime: predicted new indication Bronchitis (evidence level L5). Approved use: Organophosphate poisoning"
---

# Pralidoxime
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

# Pralidoxime: From Organophosphate Poisoning to Bronchitis

## One-Sentence Summary

Pralidoxime is a cholinesterase reactivator, used clinically to treat organophosphate poisoning (usually together with atropine).
The TxGNN model predicts it may be effective for **bronchitis**, but **no clinical trials and no publications** currently support this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Organophosphate poisoning (per the known clinical use of pralidoxime; the Singapore licence text for the registered product does not state an indication) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 95.70% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, pralidoxime reactivates acetylcholinesterase (ACHE) that has been inhibited by organophosphates, restoring the breakdown of acetylcholine at nerve synapses.

There is a theoretical overlap: organophosphate exposure causes excess cholinergic stimulation, which can lead to bronchorrhea (excess airway secretions) and bronchospasm. However, this applies to poisoning, not to bronchitis, and does not support using pralidoxime to treat bronchitis. The high score most likely reflects associations in the knowledge graph rather than a proven therapeutic link.

Other predictions in the top 10 (female breast carcinoma, seborrheic dermatitis, plasma cell myeloma, indolent plasma cell myeloma, seborrheic keratosis, bronchial neoplasm, genital herpes, vulvar inverted follicular keratosis, headache disorder) also have no identified mechanistic rationale and no supporting trials or literature. Headache is a reported adverse effect of pralidoxime, so that association may reflect adverse-event annotations rather than benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN05412P | PAM-A INJECTION 500 mg/ampoule (Ildong Pharmaceutical Co., Ltd) | Injection, powder, lyophilized, for solution | Not stated in the licence record |

## Safety Considerations

- **Drug Interactions** (4 entries found):
  - **Moderate**: Mivacurium, Succinylcholine. Both are neuromuscular blockers whose breakdown depends on cholinesterase, so this interaction needs attention.
  - **Minor**: Atropine. This is a combination commonly used together with pralidoxime in organophosphate poisoning.
  - **Target**: Acetylcholinesterase (ACHE), the pharmacological target of pralidoxime.
- **Known adverse effect**: Headache is reported as an adverse effect of pralidoxime.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for bronchitis (and for all other top-ranked predictions) is supported only by a computational score. There are no registered trials, no publications, and no plausible mechanistic link. Evidence level is L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (currently a blocking gap for safety screening)
- Mechanism of action data (e.g. from DrugBank)
- Preclinical or mechanistic evidence showing pralidoxime has any effect in bronchitis
- Assessment of route compatibility (the only licensed product is an injection) and of similarity to the original indication
- Literature and trial searches to confirm no relevant studies exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

