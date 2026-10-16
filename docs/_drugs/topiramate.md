---
layout: default
title: Topiramate
parent: Low Evidence (L5)
nav_order: 1006
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Topiramate: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy (generalized tonic-clonic seizures, partial epilepsy…"
---

# Topiramate
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

# Topiramate: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Topiramate is an antiseizure medication, originally used for epilepsy, including generalized tonic-clonic seizures, partial epilepsy and Lennox-Gastaut syndrome.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but there are currently **0 clinical trials** and **0 publications** supporting this specific direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (generalized tonic-clonic seizures, partial epilepsy, Lennox-Gastaut syndrome), per the knowledge-graph indication data. The Singapore licence records contain no indication text. |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Topiramate is a broad-spectrum antiseizure drug. It is generally understood to act on voltage-gated sodium channels, enhance GABA-A activity, antagonize AMPA/kainate glutamate receptors and inhibit carbonic anhydrase. Its efficacy in epilepsy is well established.

The link to a tumour of the trigeminal nerve is weak. These mechanisms control neuronal hyperexcitability and do not act against tumour growth. The high score is therefore probably a graph-based artefact. The model may be picking up network proximity between topiramate and trigeminal-related nodes, such as trigeminal neuralgia, rather than any anti-neoplastic activity.

No plausible mechanistic link between topiramate and tumour control has been established in the data compiled for this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Topiramate has 10 valid single-ingredient registrations and none cancelled. The five main authorizations are below.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN09689P | TOPAMAX 50 Tablet 50 mg | Film-coated tablet |
| SIN09687P | TOPAMAX 100 Tablet 100 mg | Film-coated tablet |
| SIN09688P | TOPAMAX 25 Tablet 25 mg | Film-coated tablet |
| SIN16662P | TROKENDI XR Extended-Release Capsule 25 mg | Extended-release capsule |
| SIN14131P | Topiron film-coated tablets 50 mg | Film-coated tablet |

The other five registrations are further strengths of Trokendi XR (50, 100 and 200 mg) and Topiron (25 and 100 mg). All forms are oral.

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these are graph-derived associations, not label text): kidney disease, nephrolithiasis (including SLC26A1-related susceptibility), acute urate nephropathy, pyoureter, liver disease, gallbladder disease, diarrheal disease, ocular hypertension, metabolic acidosis and acidosis disorders, anxiety disorder, neurotic disorder, dysthymic disorder, amnestic disorder and retrograde amnesia.
- **Drug Interactions** (100 interactions recorded; the first 20 retrieved are summarised here):
  - **Major**: metformin, and anticholinergic agents including hyoscyamine, atropine, scopolamine, glycopyrronium, clidinium, dicyclomine, mepenzolate, methscopolamine, propantheline and trospium.
  - **Moderate**: pioglitazone, glyburide, morphine, dronabinol, nabilone, phentermine, metoclopramide, phenylbutyric acid and glycerol phenylbutyrate.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for trigeminal nerve neoplasm is supported only by a graph-based score. There are no trials or literature, and no mechanistic basis for anti-tumour activity. Topiramate is well established and widely registered in Singapore, but that does not support this indication.

Other predictions for topiramate have more support. Trigeminal neuralgia (score 98.92%) is rated L2 with a recommendation of Proceed with Guardrails. Its evidence is a small randomized, placebo-controlled crossover pilot study and a meta-analysis against carbamazepine. The predicted seizure-related indications, such as audiogenic seizures and thinking seizures, are rated L3-L4. These may be better candidates for further evaluation.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data
- Evidence of anti-neoplastic activity of topiramate, for example preclinical studies in trigeminal nerve tumour models
- Confirmation of whether the prediction reflects trigeminal neuralgia rather than a true neoplasm
- Package insert warnings and contraindications from the HSA website, to complete safety screening
- Route and formulation compatibility assessment for the proposed use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

