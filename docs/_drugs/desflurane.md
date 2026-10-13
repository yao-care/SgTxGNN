---
layout: default
title: Desflurane
parent: Low Evidence (L5)
nav_order: 313
evidence_level: L5
indication_count: 10
---

# Desflurane
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

# Desflurane: From General Anaesthesia to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Desflurane is an inhaled volatile anaesthetic used to induce and maintain general anaesthesia (the approved indication text is not recorded in the Singapore licence data compiled for this report).
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are **0 clinical trials** and **0 publications** supporting this prediction. The prediction is purely computational.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the licence data (desflurane is a general inhalational anaesthetic) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 98.90% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, desflurane is a volatile anaesthetic that acts mainly by enhancing GABA-A receptor activity and modulating NMDA and K2P channels.

NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2), leading to inappropriate water retention and low blood sodium. Desflurane has no known activity at the V2 receptor, so there is no established mechanistic link between the drug and this disease. The high TxGNN score appears to be a graph-based association without supporting biology. The prediction should be treated as a hypothesis only.

Other top-ranked predictions (Prinzmetal angina, manic bipolar disorder, Tourette syndrome, myositis, trichotillomania, tendinitis, fibromyalgia, myofascial pain syndrome) also have no supporting trials. For several of them, the nature of desflurane raises concerns rather than support: it is a short-acting, inhaled, hospital-only agent unsuited to chronic conditions, and it is a known trigger of malignant hyperthermia in susceptible muscle disease patients.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for the top predicted indication (NSIAD). For the second-ranked prediction, Prinzmetal angina, one publication was retrieved, but it does not support a therapeutic benefit:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20502771](https://pubmed.ncbi.nlm.nih.gov/20502771/) | 2010 | Case report | Rhinology | A patient with variant angina under desflurane anaesthesia developed ventricular tachycardia and cardiac arrest after submucosal epinephrine injection. This is a safety event, not evidence of benefit. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08818P | SUPRANE INHALATION ANAESTHETIC (Baxter Healthcare Corporation) | Solution | Not recorded |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease links in the TxGNN knowledge graph, not from label text):
  - Liver and biliary: liver disease, cirrhosis of liver, gallbladder disease, hepatitis B virus infection, hepatitis C virus infection
  - Cardiovascular: coronary artery disease
  - Neuromuscular and muscle: myasthenia gravis (including adult-onset), neuromuscular junction disease, neuromuscular disease, myopathy, Duchenne muscular dystrophy, Becker muscular dystrophy, muscular dystrophy, familial periodic paralysis, hypokalaemic periodic paralysis, periodic paralysis
  - Anaesthesia-related: malignant hyperthermia of anaesthesia, exercise-induced malignant hyperthermia
  - Neurological: pseudotumor cerebri, intracranial hypertension
- **Drug Interactions** (10 recorded; main ones):
  - **Major**: Epinephrine
  - **Moderate**: Morphine, Opium, Codeine, Hydrocodone
  - Interaction severity not classified: Omeprazole, Atropine, Ondansetron, Heparin, Lidocaine

For warnings and contraindications from the approved label, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or literature, and no biological link between desflurane and the vasopressin V2 receptor. Desflurane is also an inhaled, hospital-administered anaesthetic, which makes it impractical for a chronic condition such as NSIAD. Knowledge-graph contraindications (including malignant hyperthermia and muscle disease) add safety concerns for several other predicted indications.

**To proceed, the following is needed:**
- Mechanism of action data for desflurane, and any experimental evidence of effects on AVPR2 or renal water handling
- Preclinical or mechanistic studies supporting a benefit in NSIAD
- The approved indication and the package insert warnings and contraindications from the Singapore regulator (HSA)
- Assessment of whether a practical route and dosing regimen could exist for any predicted chronic indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

