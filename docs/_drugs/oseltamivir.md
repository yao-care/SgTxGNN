---
layout: default
title: Oseltamivir
parent: Low Evidence (L5)
nav_order: 745
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Oseltamivir: predicted new indication Pyelonephritis (evidence level L5). Approved use: Influenza"
monitor_inn: "Oseltamivir"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism", "teratogenic Pierre Robin syndrome", "disorder of phenylalanine metabolism", "tetrahydrobiopterin-responsive hyperphenylalaninemia/phenylketonuria", "staphylococcus aureus infection", "cardioencephalomyopathy, fatal infantile, due to cytochrome c oxidase deficiency", "pneumonia", "streptococcal pneumonia", "aspergillosis, susceptibility to"]
---

# Oseltamivir
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

# Oseltamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

Oseltamivir is an oral antiviral originally used to treat influenza.
The TxGNN model predicts it may be effective for **pyelonephritis**, but there are **0 clinical trials** and only **1 publication** (a general review on influenza in pregnancy that does not address pyelonephritis), so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 97.85% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Oseltamivir is known to be an inhibitor of viral neuraminidase. Its efficacy in influenza is well established, but that mechanism is specific to influenza viruses.

Pyelonephritis is typically a bacterial infection of the kidney and urinary tract. Oseltamivir has no known antibacterial activity, and no plausible mechanistic link to this condition could be identified. The single retrieved paper concerns influenza in pregnancy and does not mention pyelonephritis. The high prediction score is most likely an artifact of the knowledge graph, not a reflection of biology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26033556](https://pubmed.ncbi.nlm.nih.gov/26033556/) | 2015 | Review | Presse Medicale | Overview of influenza in pregnancy, which is more frequent and severe with a higher risk of pneumonia and hospitalisation. It does not address pyelonephritis. |

---

## Singapore Market Information

Eleven valid single-ingredient registrations exist, all oral capsules. The first five are listed below, and the approved indication text is not recorded for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN16242P | Natflu Oseltamivir Phosphate USP Capsules 75 mg | Capsule | Natco Pharma Limited |
| SIN16667P | Seltavir Capsule 75 mg | Capsule | MSN Laboratories Private Limited |
| SIN11403P | Tamiflu Capsule 75 mg | Capsule | Delpharm Milano S.r.l. / Cenexi SAS |
| SIN16669P | Seltavir 30 Capsule 30 mg | Capsule | MSN Laboratories Private Limited |
| SIN16307P | Fluvir Oseltamivir Phosphate Capsules 75 mg | Capsule | Hetero Labs Limited |

---

## Safety Considerations

- **Disease-level contraindication signal**: The knowledge graph lists delirium as a contraindicated condition. This comes from graph data, not label text.
- **Drug Interactions**: 66 potential interactions were identified, all with unclassified severity. Examples include pantoprazole, vancomycin, prednisone, simvastatin, clarithromycin, metformin, morphine and omeprazole.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no relevant literature and no plausible mechanism, since oseltamivir inhibits viral neuraminidase and pyelonephritis is usually bacterial. The high TxGNN score alone does not justify further investment.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking neuraminidase inhibition to pyelonephritis, with preclinical support
- Detailed mechanism of action data and the Singapore package insert warnings and contraindications
- Consideration of better-supported lower-ranked predictions instead, such as pneumonia (influenza-related viral pneumonia) and streptococcal pneumonia (post-influenza secondary infection). These are indirect and largely overlap with the existing influenza indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

