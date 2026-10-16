---
layout: default
title: Netupitant
parent: Low Evidence (L5)
nav_order: 709
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Netupitant: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not stated in the Singapore licence data"
---

# Netupitant
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

# Netupitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Netupitant is a selective NK1 receptor antagonist, marketed in Singapore as a fixed-dose combination with palonosetron. The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence data |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 98.35% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Netupitant is a selective NK1 (substance P) receptor antagonist. Detailed mechanism of action data are not available in the data compiled for this report. The Singapore product (Akynzeo) combines netupitant with palonosetron, and the licence data do not state an approved indication.

NSIAD is caused by gain-of-function variants in the vasopressin V2 receptor, and no direct link between NK1 antagonism and V2 receptor activity has been established. The high TxGNN score is a graph-based prediction, and the supporting rationale is weak.

Other top-ranked predictions are also unsupported by trials or literature. Migraine and its subtypes (ranks 3, 4 and 6) have a plausible trigeminovascular substance P rationale, but earlier NK1 antagonists failed in clinical migraine trials. Several predictions look like graph-embedding artifacts: hyperargininemia, hypertrichosis, kyphoscoliotic heart disease and leprosy. Pulmonary hypertension and coronary artery disease have weak rationales and added drug-interaction concerns.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15031P | AKYNZEO CAPSULES 300MG/0.5MG | Capsule, gelatin coated (oral) | Not stated in the licence data |

## Cytotoxicity

Netupitant is a supportive-care (antiemetic) agent, not an antineoplastic, so it carries no cytotoxic handling requirements itself.

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified. Netupitant is a moderate CYP3A4 inhibitor, so co-administered CYP3A4 substrates are the main concern.
  - **Major**: eliglustat, naloxegol
  - **Moderate**, including:
    - Corticosteroids: dexamethasone, betamethasone, budesonide, hydrocortisone, prednisolone, prednisone, triamcinolone
    - Antiemetics: aprepitant, granisetron
    - Other drugs: naldemedine, nitisinone, repaglinide, saxagliptin, simvastatin, tinidazole, troglitazone
  - **Minor**: cobicistat

  Only 20 of the 100 interactions are shown here.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score. There are no trials or publications, and no plausible mechanistic link between NK1 antagonism and the V2 receptor gain-of-function that causes NSIAD. The large interaction burden adds further caution.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indication from the HSA, which are currently missing
- Mechanism of action data
- Preclinical or mechanistic evidence linking NK1 antagonism to V2 receptor signalling or renal water handling
- A literature and trial search specific to netupitant and NSIAD
- A decision on which predicted indication to pursue. Migraine has the most plausible biology but a history of NK1 antagonist failures.
- A drug-interaction assessment for any target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

