---
layout: default
title: Palonosetron
parent: Low Evidence (L5)
nav_order: 750
evidence_level: L5
indication_count: 10
---

# Palonosetron
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

# Palonosetron: From Chemotherapy-Induced Nausea and Vomiting to Migraine Disorder

## One-Sentence Summary

Palonosetron is a 5-HT3 receptor antagonist antiemetic, used to prevent chemotherapy-induced and postoperative nausea and vomiting.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 clinical trials** and only **1 publication** on this indication.
That publication is a case report of palonosetron *causing* migraine-type headache, so the available evidence points in the opposite direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of chemotherapy-induced nausea and vomiting (inferred from the trial and literature record, because the Singapore licence records contain no indication text) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 (weak: a single case report suggesting harm) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. From general pharmacology, palonosetron is a second-generation 5-HT3 receptor antagonist with a long half-life. 5-HT3 signalling is plausibly involved in trigeminovascular pain pathways, which could explain why a knowledge-graph model links the drug to migraine.

This link is weak. The score likely reflects graph proximity rather than clinical evidence. Headache and migraine-type headache are commonly reported adverse effects of 5-HT3 antagonists, and the only migraine-related publication describes a drug-induced event. The other top-10 predictions (for example atrophoderma vermiculata, ulerythema ophryogenesis, glaucoma, sciatic neuropathy) have no supporting trials or literature. Several are rare or genetic conditions with no plausible 5-HT3 mechanism, and they are likely graph-topology artefacts.

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine disorder.

Three palonosetron trials appear under the neighbouring prediction "headache disorder" (NCT05315999, NCT05956899, NCT04060771). They are all antiemetic prophylaxis studies (opioid-induced or postoperative nausea and vomiting) that do not test headache treatment, so they are not counted as evidence here.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Case report | Can J Anaesth | Reports migraine-type headache induced by palonosetron, i.e. a possible adverse effect and the opposite of the proposed benefit (no abstract available; summarised from the title) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN16959P | Palonosetron-AFT Solution for Injection 0.25mg/5ml | Injection, solution |
| SIN14038P | ALOXI® Solution for Injection 50mcg/ml | Injection, solution |
| SIN16899P | Akynzeo® IV Concentrate for Solution for Infusion 235 mg/0.25 mg/vial | Infusion, solution concentrate |
| SIN15031P | Akynzeo Capsules 300mg/0.5mg | Capsule, gelatin coated |

The two Akynzeo products are fixed-dose combinations that contain palonosetron together with netupitant (or fosnetupitant in the IV form).

## Safety Considerations

- **Adverse effects (from the case report and general class experience)**: Headache, including migraine-type headache, has been reported with palonosetron and other 5-HT3 antagonists.
- **Drug Interactions**: No interaction records were found in the queried source.

Please refer to the package insert for other safety information. The HSA package insert warnings and contraindications have not yet been retrieved.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high model score is not supported by any clinical trial or drug-specific literature. The only related publication suggests palonosetron can cause migraine-type headache rather than treat it. The evidence does not support repurposing for migraine.

**To proceed, the following is needed:**
- Retrieve the HSA package insert (warnings, contraindications, approved indications), which is currently a blocking gap
- Obtain mechanism of action data from DrugBank
- Systematic review of headache and migraine as adverse events in palonosetron trials, to clarify the direction of effect
- Preclinical or early-phase clinical evidence that 5-HT3 antagonism has a therapeutic effect in migraine before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

