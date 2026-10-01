---
layout: default
title: Fentanyl
parent: Low Evidence (L5)
nav_order: 421
evidence_level: L5
indication_count: 10
---

# Fentanyl
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

# Fentanyl: From Severe Pain to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a potent opioid analgesic, marketed in Singapore as a transdermal patch and a sublingual tablet for severe pain. The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**. However, **no clinical trials and no publications** currently support this direction, and the mechanism argues against it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe pain (analgesia). The registration records provided contain no indication text. |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.46% (rank 6,786) |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 18 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source data. Fentanyl is a mu-opioid receptor agonist, and its efficacy in pain relief is well established.

The predicted disease is caused by gain-of-function variants in the AVPR2 gene. These variants make the kidney concentrate urine inappropriately, leading to low blood sodium. Mu-opioid agonism has no plausible way to correct this defect, and opioids can even promote antidiuresis. The very high graph score appears to be an artifact of the knowledge graph rather than a real pharmacological signal, so the prediction should not be considered credible on mechanistic grounds.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

18 registrations are listed. The five main ones are shown below. The provided records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN08332P | DUROGESIC TRANSDERMAL SYSTEM 75 mcg/hr | Patch |
| SIN08335P | DUROGESIC TRANSDERMAL SYSTEM 50 mcg/hr | Patch |
| SIN08334P | DUROGESIC TRANSDERMAL SYSTEM 25 mcg/hr | Patch |
| SIN15148P | ABSTRAL SUBLINGUAL TABLET 200 mcg | Tablet |
| SIN15147P | ABSTRAL SUBLINGUAL TABLET 100 mcg | Tablet |

Other dosage forms recorded for fentanyl are injection and injection solution.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials or literature behind it (L5), and the disease mechanism (AVPR2 gain-of-function) is not something a mu-opioid agonist could correct. The high score most likely reflects a knowledge-graph artifact. Fentanyl also carries dependence and respiratory-depression risks that cannot be justified without supporting evidence.

**Other predicted candidates:**
- Among the other predictions, only **myofascial pain syndrome** reached the next screening stage (Research Question). It would be a symptomatic extension of fentanyl's analgesic use, not true repurposing.
- Its one Phase 3 trial (NCT00343733) needs its study population checked against the registry record.
- Long-term opioid use for chronic musculoskeletal pain carries significant safety concerns.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications
- Mechanism of action data (for example, from DrugBank)
- Any direct clinical or preclinical evidence linking fentanyl to NSIAD, which is unlikely to exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

