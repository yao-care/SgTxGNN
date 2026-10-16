---
layout: default
title: Mupirocin
parent: Low Evidence (L5)
nav_order: 691
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Mupirocin: predicted new indication Pleural empyema (evidence level L5). Approved use: Impetigo, bullous impetigo"
monitor_inn: "Mupirocin"
predicted_indications: ["pleural empyema (disease)", "punctate epithelial keratoconjunctivitis", "neurotrophic keratopathy", "cutaneous candidiasis", "vaginal discharge", "exposure keratitis", "leukoplakia of vagina", "non-human animal disease", "staphylococcal scalded skin syndrome", "bacterial vaginosis"]
---

# Mupirocin
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

# Mupirocin: From Impetigo to Pleural Empyema

## One-Sentence Summary

Mupirocin is a topical antibiotic originally used for skin infections such as impetigo and bullous impetigo.
The TxGNN model predicts it may be effective for **pleural empyema**, but **no clinical trials and no publications** currently support this direction.
Mupirocin is an ointment that cannot reach a deep body-cavity infection at therapeutic concentrations, so this prediction is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Impetigo, bullous impetigo |
| Predicted New Indication | Pleural empyema |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

The approved-indication text was blank on all Singapore licence records. The original indications above come from the drug-disease relationships used by the TxGNN model.

## Why is This Prediction Reasonable?

Mupirocin inhibits bacterial isoleucyl-tRNA synthetase, which blocks protein synthesis. It is mainly active against *Staphylococcus aureus* and some streptococci, the organisms behind impetigo. Pleural empyema is also often caused by these Gram-positive bacteria, which is probably why the model linked the two.

The mechanistic link is weak in practice, for two reasons:

- Empyema is a deep-seated infection of the pleural space. A topical ointment cannot reach it at therapeutic concentrations.
- Mupirocin is not suitable for systemic or intrapleural use.

The high score therefore reflects a statistical association in the model rather than a plausible treatment route.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

All six licences are valid single-ingredient 2% w/w ointments. The five main ones are listed below. No approved-indication text is recorded for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14421P | Muprin Ointment 2% w/w | Ointment | Not listed |
| SIN05075P | Bactroban Nasal Ointment 2% w/w | Ointment | Not listed |
| SIN13712P | Mupider Ointment 2% w/w | Ointment | Not listed |
| SIN16306P | Epirozin Ointment 2% w/w | Ointment | Not listed |
| SIN11895P | Supirocin Ointment 2% w/w | Ointment | Not listed |

All registered products are ointments only. No injectable or other systemic form is registered in Singapore.

## Safety Considerations

- **Disease-level contraindication signal**: dermatitis appears as a contraindicated condition in the drug-disease relationships used by the model. This is not label text and should be checked against the package insert.
- **Drug Interactions**: The interaction screen returned 100 entries, all with an unspecified severity level. Examples include calcitriol, clotrimazole, morphine, metformin, pantoprazole, omeprazole, vancomycin, triamcinolone, prednisone and simvastatin. These cannot be ranked by clinical importance without further review.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone, with no trials or literature. A topical ointment cannot plausibly treat a deep pleural infection, and no systemic or intrapleural formulation exists.

**To proceed, the following is needed:**
- A rationale for a systemic or intrapleural formulation, with pharmacokinetic and safety data, if this indication is to be pursued at all.
- Package insert warnings and contraindications from the Singapore Health Sciences Authority (HSA).
- Detailed mechanism of action data from DrugBank.

**Other candidates:** Among the other predicted indications, **staphylococcal scalded skin syndrome** has the strongest support (evidence level L3, "Proceed with Guardrails"). It involves the same pathogen and toxin mechanism as bullous impetigo. A 2023 comparative study (PMID 37404367) evaluated intravenous antibiotics combined with 2% mupirocin ointment in children. Mupirocin would be an adjunct to systemic antibiotics only, with attention to resistance and to absorption through denuded skin in neonates. This candidate is a more promising focus for further evaluation than pleural empyema.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

