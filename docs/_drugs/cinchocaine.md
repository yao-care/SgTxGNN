---
layout: default
title: Cinchocaine
parent: Low Evidence (L5)
nav_order: 252
evidence_level: L5
indication_count: 10
---

# Cinchocaine
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

# Cinchocaine: From Dermatitis to Bronchitis

## One-Sentence Summary

Cinchocaine (dibucaine) is an amide-type local anaesthetic, originally used for dermatitis and marketed in Singapore as a topical ointment.
The TxGNN model predicts it may be effective for **bronchitis**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on computation alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis (from the knowledge graph; the Singapore registration lists no approved indication text) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on general class pharmacology, cinchocaine is an amide-type local anaesthetic that blocks voltage-gated sodium channels. Its established use is topical symptom relief of pain and itch.

The link to bronchitis is weak. A surface anaesthetic effect might in theory dampen airway irritation or the cough reflex, but this would only relieve symptoms and would not treat the underlying disease. Systemic or inhaled use also raises concerns about cardiac and central nervous system toxicity. The high score most likely reflects proximity in the knowledge graph rather than a proven biological connection.

The other nine predictions share this weakness. They include acrodermatitis chronica atrophicans, neonatal dermatomyositis, childhood connective-tissue-disease-associated interstitial lung disease, acne keloid, familial hydroa vacciniforme, amyopathic dermatomyositis, and several myasthenia-related or autoimmune neurological conditions. Most are infectious or immune-mediated diseases that a sodium channel blocker is not expected to modify. At best, topical symptom relief might apply to skin conditions such as acne keloid. For the myasthenia gravis predictions (neonatal myasthenia gravis and myasthenia gravis with thymus hyperplasia), the expected direction of effect is potentially harmful, since sodium channel-blocking anaesthetics can worsen neuromuscular transmission. These should be treated as likely false positives with a safety concern.

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
| SIN01718P | PROCTOSEDYL OINTMENT (Bausch Health Companies Inc.) | Ointment | Not listed in the registration data |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph** (these are not label text): epilepsy, kidney disease, pyoureter, liver disease, gallbladder disease, sudden cardiac arrest, heart conduction disease, respiratory failure, myasthenia gravis (including adult-onset), neuromuscular junction disease, butyrylcholinesterase deficiency, cardiovascular disease and heart disease.
- The myasthenia gravis and neuromuscular junction flags matter most for the predicted neuromuscular indications. The cardiac and respiratory flags matter for any systemic or inhaled use in bronchitis.

Please refer to the package insert for the official warnings, contraindications and drug interactions. No such label data were available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials or literature. The mechanism offers at most symptomatic relief, and the only registered product is a topical ointment, which does not fit the predicted indication. For the myasthenia-related predictions, there is a possible safety hazard.

**To proceed, the following is needed:**
- The package insert warnings and contraindications from HSA, which are a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- A route-of-administration compatibility assessment for the predicted indications (topical ointment versus airway delivery)
- A literature and trial search to find any real-world evidence for bronchitis or acne keloid
- A safety assessment for any systemic, inhaled or paediatric use
- If any prediction is pursued, acne keloid is the most plausible candidate, as a topical symptomatic use. The myasthenia gravis predictions should be deprioritised.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

