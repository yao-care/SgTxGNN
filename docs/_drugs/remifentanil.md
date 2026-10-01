---
layout: default
title: Remifentanil
parent: Low Evidence (L5)
nav_order: 851
evidence_level: L5
indication_count: 10
---

# Remifentanil
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

# Remifentanil: From Anesthesia Analgesia to Common Cold

## One-Sentence Summary

Remifentanil is a short-acting opioid given by injection for analgesia during anesthesia.
The TxGNN model predicts it may be effective for the **common cold**, but only **2 clinical trials** and **2 publications** were retrieved, and none of them studies the common cold.
The high score is most likely a knowledge-graph artifact rather than a real therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration record (remifentanil is used for analgesia during anesthesia) |
| Predicted New Indication | Common cold |
| TxGNN Prediction Score | 98.68% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Remifentanil is a short-acting mu-opioid receptor agonist used for analgesia and anesthesia. It has no antiviral, anti-inflammatory or symptom-relieving role in upper respiratory infection.

Its original use (pain control and anesthesia) and the common cold share no disease pathway. Mechanistically there is no plausible link, and the model's high score is likely a knowledge-graph artifact.

The retrieved trials support this view. Both are anesthesia or perioperative studies in which remifentanil is only a background drug. Neither tests it as a treatment for a cold.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06950957](https://clinicaltrials.gov/study/NCT06950957) | N/A | Recruiting | 64 | Video laryngeal mask airway vs endotracheal tube in septoplasty. Remifentanil is only background anesthetic. Relevance grade C. |
| [NCT06841822](https://clinicaltrials.gov/study/NCT06841822) | N/A | Recruiting | 168 | Paravertebral nerve block approaches and hemodynamics during thoracoscopic lobectomy induction. Unrelated to the common cold. Relevance grade C. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21179290](https://pubmed.ncbi.nlm.nih.gov/21179290/) | 2010 | RCT | Korean J Anesthesiol | Cold propofol plus remifentanil pretreatment for propofol injection pain. Here "cold" refers to temperature, not the common cold. |
| [25909573](https://pubmed.ncbi.nlm.nih.gov/25909573/) | 2015 | Review | J Neurosurg | Awake craniotomy methods for glioma resection over 27 years. Not related to the common cold. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN09542P | ULTIVA FOR INJECTION 1 mg/vial | Injection, powder, for solution |

The registration record does not list approved indication text.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no plausible mechanism and no relevant clinical study for the common cold, so the prediction is model output only (L5). Remifentanil is an injectable anesthesia opioid, which makes it an unlikely candidate for a self-limiting upper respiratory infection.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications, which block safety screening
- Detailed mechanism of action data from DrugBank
- A mechanistic rationale linking mu-opioid agonism to cold symptoms or pathology, plus any relevant clinical study
- A route-compatibility assessment (the only registered form is injectable)

The other nine predicted indications (rank 2 to 10) are also on Hold. Several periodic paralysis and malignant hyperthermia items rest on case reports of safe anesthetic use, which show feasibility rather than efficacy.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

