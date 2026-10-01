---
layout: default
title: Sotalol
parent: Low Evidence (L5)
nav_order: 922
evidence_level: L5
indication_count: 10
---

# Sotalol
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

# Sotalol: From Cardiac Arrhythmia to Sick Sinus Syndrome 2 (Autosomal Dominant)

## One-Sentence Summary

Sotalol is an oral beta-blocker with class III antiarrhythmic activity, used for ventricular arrhythmias and atrial fibrillation.
The TxGNN model predicts it may be effective for **sick sinus syndrome 2, autosomal dominant**, but this is a model prediction only, with **0 clinical trials** and **0 publications** directly supporting it.
The mechanism points the other way: sotalol slows the sinus rate, so the prediction looks like a graph artifact with a bradycardia safety concern.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records (antiarrhythmic use) |
| Predicted New Indication | Sick sinus syndrome 2, autosomal dominant |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, sotalol combines beta-adrenergic blockade with potassium-channel (IKr) blockade. Together these slow the sinus rate and atrioventricular conduction.

The prediction is probably not reasonable. Sick sinus syndrome is a disorder of sinus-node function, often with a slow heart rate. A drug that further slows the sinus rate and AV conduction is generally avoided in this condition unless a pacemaker is in place. The high score most likely reflects the shared "arrhythmia" neighbourhood in the knowledge graph rather than a therapeutic link. Treating the prediction as real could expose patients to bradycardia.

One related lead sits under another predicted indication, stroke disorder. Trial NCT02145546 (Phase 4, status unknown, 600 patients) compares amiodarone, sotalol and propafenone for atrial fibrillation in patients with sick sinus syndrome after pacing. It addresses AF burden in these patients, not treatment of sick sinus syndrome itself.

## Clinical Trial Evidence

Currently no related clinical trials registered for sick sinus syndrome 2, autosomal dominant.

## Literature Evidence

Currently no related literature available for this predicted indication.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13311P | SotaHexal 80mg Tablet | Film-coated tablet | Not stated in the registration record |
| SIN09139P | APO-SOTALOL TABLET 160 mg | Tablet | Not stated in the registration record |

## Safety Considerations

- **Predicted-indication concern**: Sotalol's rate- and conduction-slowing effects make bradycardia a potential problem in sick sinus syndrome.
- **Proarrhythmic risk**: Sotalol prolongs the QT interval, which carries a risk of torsades de pointes.
- **Drug interactions**: No interaction records were found in the Evidence Pack.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or literature. Sotalol's pharmacology argues against use in sick sinus syndrome. The other nine predicted indications also lack supportive efficacy evidence. Stroke disorder is the only one with meaningful data, and that evidence is indirect (AF rhythm control, not stroke outcomes).

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A specific safety assessment of sotalol in sinus-node dysfunction, including pacemaker status
- A stroke-outcome study to test the indirect AF-to-stroke link, if the stroke direction is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

