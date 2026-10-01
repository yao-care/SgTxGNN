---
layout: default
title: Choline Salicylate
parent: Low Evidence (L5)
nav_order: 243
evidence_level: L5
indication_count: 10
---

# Choline Salicylate
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

# Choline Salicylate: From Topical Oral Pain Relief to Prinzmetal Angina

## One-Sentence Summary

Choline salicylate is a salicylate anti-inflammatory and analgesic, marketed in Singapore only as topical oral gels (the registration records do not state the approved indications).
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but **no clinical trials and no publications** support this direction.
This is a model-only prediction with a safety concern, so it is not ready for further development.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records (the products are labelled as oral gels for pain relief) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.84% (rank 2863) |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, choline salicylate is a non-acetylated salicylate with weak COX inhibition. It is not known to have any meaningful irreversible antiplatelet effect.

The link between the original use (topical pain relief) and coronary vasospasm is weak. Nothing in the evidence explains how a salicylate would relieve vasospasm. The TxGNN score of 0.998 is near saturation and does not separate this candidate from the others, so it should be read as a graph-neighbourhood signal, not evidence of efficacy. Aspirin-class drugs have also been reported to worsen vasospastic angina at some doses, which raises a possible safety concern.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN10428P | SORAGEL ANTISEPTIC PAIN RELIEVING ORAL GEL | Gel | ICM Pharma Pte. Ltd. |
| SIN04948P | ORA-SED JEL | Gel | Hamilton Pharmaceutical Pty Ltd |
| SIN04303P | BONJELA GEL | Gel | Reckitt Benckiser Healthcare (UK) Ltd |

All three registered products are topical gels, and the registration records list no approved indication text. Topical oral gels are unlikely to give the systemic exposure a cardiovascular indication would need. Route compatibility has not yet been assessed.

## Safety Considerations

Please refer to the package insert for safety information.

Concerns from the prediction analysis:
- Salicylates and aspirin-class drugs may worsen vasospastic angina at some doses.
- A published case report describes urticarial and bronchospastic reactions to non-acetylated salicylates in a patient with asthma, nasal polyps and rheumatoid arthritis. Caution applies to patients with asthma, nasal polyps or NSAID hypersensitivity.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a saturated model score alone, with no supporting trials or literature and no plausible mechanism. There is also a possible safety concern in vasospastic angina.

**Other candidates from the same run:** Rheumatoid arthritis is the only candidate with any published support. Four papers from 1977 to 1986 were retrieved (Evidence Level L3, Research Question). Their study designs are unverified, no trials were retrieved, and the original indications are empty in the pack, so on-label status should be checked first. The remaining candidates (hypertensive disorder, migraine, pulmonary hypertension, Raynaud disease and the malignant hypertensive renal entries) have no trial or literature evidence that tests choline salicylate. For several of them, salicylate or NSAID effects on blood pressure and renal perfusion argue against use.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data (from DrugBank)
- Confirmed approved indications for the three Singapore products
- Any direct clinical or mechanistic evidence for coronary vasospasm, and an assessment of whether a topical gel could deliver the exposure required
- Consider redirecting review to the rheumatoid arthritis candidate

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

