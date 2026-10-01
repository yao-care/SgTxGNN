---
layout: default
title: Lamotrigine
parent: Low Evidence (L5)
nav_order: 570
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Lamotrigine: From Antiseizure Therapy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Lamotrigine is an antiseizure medicine. The Singapore registration data in the Evidence Pack do not state its approved indication text.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm** with a very high score, but there are **0 clinical trials** and only **2 publications**, and both publications are about trigeminal neuralgia rather than tumour treatment.
The score most likely reflects the knowledge graph linking lamotrigine to trigeminal neuralgia, not any antitumour effect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (all HSA approved-indication fields are empty) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Lamotrigine blocks voltage-gated sodium channels in a use-dependent manner and reduces glutamate release. The Evidence Pack's structured mechanism-of-action field is empty. This description comes from the pack's repurposing rationale.

No antitumour mechanism has been established for lamotrigine. Its known actions calm overactive nerve firing and do not target tumour growth.

The likely explanation for the high score is proximity in the knowledge graph. Lamotrigine is used in trigeminal neuralgia, a nerve pain condition, and the graph appears to place it close to disease terms involving the trigeminal nerve. The two papers retrieved for this prediction both concern trigeminal neuralgia, not neoplasm therapy. The prediction should therefore be read as a likely naming or graph artifact, not as a credible signal of tumour activity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Overview of medical and surgical treatments for trigeminal neuralgia. It does not address tumour therapy. |
| [30650431](https://pubmed.ncbi.nlm.nih.gov/30650431/) | 2018 | Case report | Stereotact Funct Neurosurg | Gamma Knife radiosurgery for trigeminal neuralgia caused by a cavernous malformation. It does not involve lamotrigine treating a neoplasm. |

## Singapore Market Information

Ten registrations were found; the five main ones are listed below. The approved-indication text is blank for all of them in the source data.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN09094P | LAMICTAL DISPERSIBLE TABLET 5 mg | Tablet |
| SIN13365P | Lamitor - 50 | Tablet |
| SIN14028P | Lamotrix Tablet 100mg | Tablet |
| SIN07498P | LAMICTAL TABLET 100 mg | Tablet |
| SIN13555P | Apo-Lamotrigine 100mg Tablet | Tablet |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no supporting tumour literature, and no antitumour mechanism is known. The evidence is model prediction only (L5).

**To proceed, the following is needed:**
- Any preclinical or clinical evidence that lamotrigine has activity against trigeminal nerve tumours. Nothing currently supports this.
- HSA package insert data (warnings, contraindications, approved indications), which are currently missing and block safety screening.
- Mechanism-of-action data from DrugBank.
- Consider redirecting attention to **trigeminal neuralgia** (rank 2 in the same pack), the more clinically meaningful signal. It has a completed Phase 2/3 trial (NCT00913107, n=21, lamotrigine vs carbamazepine), a placebo-controlled add-on study (NCT00203229, n=20), and an evidence level of L2. The EAN 2019 guideline lists lamotrigine only as an add-on or second-line option based on low-quality evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

