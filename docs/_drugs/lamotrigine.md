---
layout: default
title: Lamotrigine
parent: Low Evidence (L5)
nav_order: 576
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lamotrigine: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy"
monitor_inn: "Lamotrigine"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "restless legs syndrome"]
---

# Lamotrigine
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

# Lamotrigine: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Lamotrigine is an established antiseizure medicine, originally used for epilepsy, including partial epilepsy and Lennox-Gastaut syndrome.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm** with a very high score. However, there are **0 clinical trials** and only **2 publications**, and both publications concern trigeminal *neuralgia* (a pain condition), not a tumour. This prediction is therefore supported by **model output only**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (partial epilepsy, Lennox-Gastaut syndrome; taken from the knowledge-graph indication list because the Singapore licence records contain no indication text) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Lamotrigine is widely understood to work by blocking voltage-gated sodium channels and reducing glutamate release. This calms over-excited nerve cells, which is why it works in epilepsy.

The prediction likely reflects the model's graph proximity to **trigeminal neuralgia**, a facial pain disorder of the same nerve, where sodium channel blockade is a plausible way to work. It does not appear to reflect any anti-tumour activity. The retrieved literature is about trigeminal neuralgia, including a case where the pain was caused by a cavernous malformation. No evidence shows that lamotrigine shrinks or controls a neoplasm, or that it relieves symptoms in patients with a trigeminal nerve tumour.

The more credible signal is the neighbouring prediction, **trigeminal neuralgia**. It has two completed lamotrigine trials (NCT00913107, a Phase 2/3 comparison with carbamazepine with 21 patients, and NCT00203229, a placebo-controlled add-on study with 20 patients) and positioning in guidelines as an alternative or add-on option. That is a different disease from the headline prediction and should be evaluated separately.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for trigeminal nerve neoplasm.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Overview of medical and surgical treatments for trigeminal neuralgia; concerns the pain syndrome, not a neoplasm |
| [30650431](https://pubmed.ncbi.nlm.nih.gov/30650431/) | 2018 | Case report | Stereotact Funct Neurosurg | Gamma Knife radiosurgery for trigeminal neuralgia caused by a brainstem cavernous malformation; no lamotrigine anti-tumour data |

---

## Singapore Market Information

All 10 licences are valid single-ingredient oral tablets. The licence records contain no approved-indication text. The 5 main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN07497P | LAMICTAL TABLET 50 mg | Tablet | — |
| SIN07498P | LAMICTAL TABLET 100 mg | Tablet | — |
| SIN09094P | LAMICTAL DISPERSIBLE TABLET 5 mg | Tablet | — |
| SIN14088P | Lamictal Tablet 25 mg | Tablet | — |
| SIN13555P | Apo-Lamotrigine 100mg Tablet | Tablet | — |

---

## Safety Considerations

- **Conditions linked to lamotrigine in the knowledge graph (not label text):** liver disease, gallbladder disease, anxiety and neurotic disorders, dysthymic disorder, non-infectious meningitis, and several blood disorders (thrombocytopenia, neutropenia, agranulocytosis, anaemia, pancytopenia, aplastic anaemia). These should be reviewed against the package insert before any use in a new patient group.
- **Drug Interactions:** 100 interactions are recorded. Moderate-level ones include morphine (including liposomal), opium, dronabinol, nabilone, metoclopramide and orlistat. Metformin is rated minor. Several others, such as omeprazole, pantoprazole, lansoprazole and doxycycline, are of unknown severity.

For other safety information, including warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by any trial or by any literature on tumours. The retrieved papers are about trigeminal neuralgia, not a neoplasm. There is no basis to expect an anti-tumour effect or a symptomatic role in a nerve tumour.

**To proceed, the following is needed:**
- Evidence of anti-tumour or symptom-control effect of lamotrigine in trigeminal nerve tumours; otherwise the prediction should be treated as an artefact of graph proximity to trigeminal neuralgia
- Consider evaluating **trigeminal neuralgia** as a separate candidate. Slow dose titration is needed because of rash risk, and lamotrigine would be positioned as a second-line option.
- Mechanism of action data (MOA)
- Package insert warnings and contraindications from the HSA, which are needed before any safety screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

