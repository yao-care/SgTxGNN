---
layout: default
title: Cefotaxime
parent: Low Evidence (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
---

# Cefotaxime
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

# Cefotaxime: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Cefotaxime is a third-generation cephalosporin antibiotic, originally used to treat bacterial infections.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting it.
Other predicted indications for this drug have more support, especially pneumococcal meningitis (see Conclusion).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (the Singapore registry extract has no approved-indication text) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 98.47% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured record. Based on known information, cefotaxime is a beta-lactam antibacterial that inhibits bacterial cell wall synthesis. Its efficacy in bacterial infections is established.

Mechanistically, there is no plausible link to polyclonal hyperviscosity syndrome. This condition involves raised serum viscosity from excess immunoglobulins. Cefotaxime has no known effect on serum viscosity or immunoglobulin levels. The high score (0.985) reflects patterns in the knowledge graph and should not be read as evidence of benefit. No trials or publications support this specific prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN16368P | CYTAXIN Powder for Solution for Injection 1G/vial | Injection, powder, for solution | Tenamyd Pharmaceutical Corporation |
| SIN16367P | CYTAXIN Powder for Solution for Injection 0.5G/vial | Injection, powder, for solution | Tenamyd Pharmaceutical Corporation |

Both products are injectable only.

---

## Safety Considerations

Please refer to the package insert for safety information.

Literature retrieved for other predicted indications includes a case report of acute intravascular hemolysis in a newborn after cefotaxime-sulbactam (PMID [35003054](https://pubmed.ncbi.nlm.nih.gov/35003054/), 2021). This is a reminder that cephalosporins can cause immune-mediated hemolysis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication rests on a model score alone (L5). There is no mechanistic rationale, trial, or publication. The antibacterial mechanism does not address serum hyperviscosity.

**Stronger candidates among the other predictions:**
- **Pneumococcal meningitis** (rank 8, L3, Proceed with Guardrails). It is mechanistically direct. It has a completed Phase 4 trial ([NCT01540838](https://clinicaltrials.gov/study/NCT01540838), n=375, in which cefotaxime was background therapy, not the randomized intervention). It also has CSF-penetration data and clinical reports. This is probably already standard care, so its status as a "repurposing" candidate and its label coverage should be verified.
- **Septicemic plague** (rank 9, L4, Research Question). Support comes from older animal studies only, and first-line plague agents are better supported.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the approved indications on the Singapore labels
- For pneumococcal meningitis: a check of current label coverage and local resistance data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

