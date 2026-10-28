---
layout: default
title: Rufinamide
parent: Low Evidence (L5)
nav_order: 887
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "Rufinamide"
predicted_indications: ["perioral myoclonia with absences"]
description: "Rufinamide: predicted new indication Perioral myoclonia with absences (evidence level L5). Approved use: Not recorded in the local data"
---

# Rufinamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Rufinamide: Perioral myoclonia with absences
{: .text-alpha }

## One-Sentence Summary

Rufinamide is an antiseizure medication originally used for seizures associated with Lennox-Gastaut syndrome.
but currently there are **0 clinical trials** and **0 publications** directly supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Perioral myoclonia with absences |
| TxGNN Prediction Score | 0.9951 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, rufinamide is a triazole-derivative antiseizure drug. Its efficacy in Lennox-Gastaut syndrome has been established, and it is generally thought to act by modulating sodium channels. Mechanistically, it may be applicable to FIRES, but this link is unproven.

FIRES is a severe, refractory epileptic encephalopathy that develops after a febrile illness. Its course is thought to be driven largely by neuroinflammation. Lennox-Gastaut syndrome is also a drug-resistant epileptic encephalopathy, which may explain why the model places the two close together. However, rufinamide's sodium-channel activity targets seizure generation, not the inflammatory process behind FIRES. It should not be read as evidence of benefit.

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
| SIN15146P | INOVELON FILM-COATED TABLET 200 MG | Tablet, film coated (oral) | Indication text not listed in the registration record |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these are model-derived associations, not package-insert text): liver failure, liver disease, gallbladder disease, leukopenia, anxiety disorder, neurotic disorder, and dysthymic disorder.
- **Drug Interactions**: The interaction query returned 100 records. The 20 retrieved are all rated Moderate. Main examples:
  - Corticosteroids: hydrocortisone, prednisone, triamcinolone, betamethasone
  - Vitamin D analogues: cholecalciferol, calcifediol, calcitriol
  - Opioids and related agents: morphine, difenoxin, diphenoxylate
  - Cannabinoids: dronabinol, nabilone
  - Other: pioglitazone, bupropion, ondansetron, metoclopramide, eliglustat, naloxegol, nitisinone, rolapitant

Please refer to the package insert for the full warnings and contraindications. These were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The FIRES prediction has no supporting trials or publications (Evidence Level L5). The mechanistic link is plausible but unsupported, and rufinamide does not target neuroinflammation, the main driver of FIRES. Package-insert safety data have also not yet been reviewed.

Among the other predictions, "childhood onset epileptic encephalopathy" has far more literature, including a Phase III dosing publication. However, that support mostly reflects rufinamide's already-approved Lennox-Gastaut indication, not true repurposing.

**To proceed, the following is needed:**
- Case series, registry data, or trials of rufinamide specifically in FIRES
- Detailed mechanism of action data, and an assessment of whether sodium-channel modulation is relevant to neuroinflammation-driven epilepsy
- The Singapore package insert (HSA) warnings, contraindications, and approved indication text
- A review of the interaction profile (100 records) against the medicines typically used in FIRES, such as corticosteroids and other antiseizure drugs
- A safety assessment for hepatic impairment and leukopenia, given the knowledge-graph contraindication signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

