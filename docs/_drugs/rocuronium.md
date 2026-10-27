---
layout: default
title: Rocuronium
parent: Low Evidence (L5)
nav_order: 880
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Rocuronium: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the Singapore licence records (the approved indication…"
monitor_inn: "Rocuronium"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "cauda equina syndrome", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "ulerythema ophryogenesis", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "sciatic neuropathy", "headache disorder"]
---

# Rocuronium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Rocuronium: From Neuromuscular Blockade in Anaesthesia to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Rocuronium is a non-depolarising neuromuscular blocker used as an anaesthetic adjunct (for example, to facilitate intubation and skeletal muscle relaxation during surgery).
The TxGNN model predicts it may be effective for **migraine disorder**, but only **1 clinical trial** (an incidental, non-efficacy pharmacokinetics study) and **no directly relevant publications** are linked to this prediction.
The evidence is essentially model prediction only, and the prediction is not supported mechanistically.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records (the approved indication text is empty) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, rocuronium is a non-depolarising neuromuscular blocker. It competitively antagonises nicotinic acetylcholine receptors at the neuromuscular junction, producing temporary skeletal muscle paralysis.

The review of this prediction found **no credible mechanistic link** to migraine. Migraine involves CGRP signalling, trigeminovascular activation and cortical spreading depression, which are central and neurovascular processes. Peripheral muscle relaxation does not address them. The very high TxGNN score most likely reflects proximity in the knowledge graph rather than a pharmacological rationale.

The other top predictions point the same way: related migraine subtypes, cauda equina syndrome, rare follicular skin disorders, irritable bowel syndrome and sciatic neuropathy. These are either inherited from the parent migraine node or have no plausible mechanism. This prediction should be treated as a probable knowledge-graph artefact.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3520 | Pharmacokinetics of understudied drugs given to children as standard of care. It has no migraine-specific efficacy endpoint, and rocuronium appears only because of its use as an anaesthetic adjunct. Relevance grade: C. |

---

## Literature Evidence

No publications were found for the migraine prediction itself. The only literature comes from the related prediction "headache disorder", and it is contextual rather than supportive:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23812022](https://pubmed.ncbi.nlm.nih.gov/23812022/) | 2014 | Clinical study | The Journal of ECT | Compared succinylcholine with rocuronium-sugammadex for myalgia and headache after electroconvulsive therapy. Headache is an adverse perioperative outcome here, not a treatment target. |
| [24196089](https://pubmed.ncbi.nlm.nih.gov/24196089/) | 2013 | Case report | Pediatric Emergency Care | Rapid sequence intubation with propofol and remifentanil in a child with raised intracranial pressure. It is not related to headache treatment. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN17025P | NOVERON SOLUTION FOR INJECTION 10MG/ML | Injection, solution | Not stated |
| SIN15106P | ROCURONIUM KABI SOLUTION FOR INJECTION/INFUSION 10MG/ML | Injection, solution | Not stated |
| SIN09479P | ESMERON INJECTION 50 mg/5ml | Injection | Not stated |
| SIN15237P | ROCURONIUM-HAMELN INJECTION 10MG/ML | Injection, solution | Not stated |

All four registrations are valid, single-ingredient injectable products.

---

## Safety Considerations

- **Drug Interactions**: 73 interactions were recorded. Examples from the data compiled for this report:
  - **Major**: paromomycin, kanamycin, neomycin (aminoglycosides, which may potentiate neuromuscular blockade)
  - **Moderate**: magnesium sulfate, magnesium chloride, vancomycin, amphotericin B, tetracyclines (doxycycline, minocycline, tetracycline), corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, prednisone), mannitol, metoclopramide
  - **Minor**: ranitidine

Please refer to the package insert for warnings and contraindications.

Rocuronium causes skeletal muscle paralysis, including the respiratory muscles. It is restricted to controlled settings with airway and ventilation support. Chronic or outpatient use for a condition such as migraine is not practical or safe.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score. There is no mechanistic link, no efficacy trial and no supporting literature for migraine. The only linked trial is a general pediatric pharmacokinetics study. The risk profile of a paralysing agent also makes migraine use unrealistic.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis connecting nicotinic receptor blockade to migraine pathophysiology
- Preclinical or clinical efficacy data specific to migraine
- Full mechanism of action data and package insert warnings and contraindications
- Evaluation of safe routes and settings of administration, since the current use is limited to supervised anaesthesia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

