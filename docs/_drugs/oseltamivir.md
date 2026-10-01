---
layout: default
title: Oseltamivir
parent: Low Evidence (L5)
nav_order: 737
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Oseltamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

Oseltamivir is an oral antiviral neuraminidase inhibitor used to treat influenza. The HSA records supplied do not state its approved indication.
The TxGNN model predicts it may be effective for **pyelonephritis** (a kidney infection), but **0 clinical trials** and only **1 publication** (an unrelated review of influenza in pregnancy) support this. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied HSA data (oseltamivir is generally known as an influenza antiviral) |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 97.85% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 11 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the DrugBank record. Oseltamivir is a viral neuraminidase inhibitor. Its efficacy in influenza is established, but it has no known antibacterial activity against the organisms that usually cause pyelonephritis, such as *E. coli* and other urinary tract pathogens.

No biological rationale for this prediction has been identified. Pyelonephritis is a bacterial kidney infection, while oseltamivir acts on an enzyme of the influenza virus. The only retrieved paper is a review of influenza in pregnancy. It discusses seasonal and pandemic flu and vaccination, and it does not address pyelonephritis. The high score therefore appears to be a knowledge-graph association rather than a clinically supported link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26033556](https://pubmed.ncbi.nlm.nih.gov/26033556/) | 2015 | Review | Presse Medicale | Overview of influenza in pregnancy: higher risk of pneumonia and hospitalization, and vaccination recommendations. It does not address pyelonephritis, so it is not direct evidence for this indication. |

## Singapore Market Information

Eleven registrations exist; five are listed below. The supplied records give no approved indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN16242P | NATFLU Oseltamivir Phosphate USP Capsules 75 mg | Capsule | Natco Pharma Limited |
| SIN16667P | SELTAVIR Capsule 75 mg | Capsule | MSN Laboratories Private Limited |
| SIN11403P | TAMIFLU Capsule 75 mg | Capsule | Delpharm Milano S.r.l. / CENEXI SAS |
| SIN16669P | SELTAVIR 30 Capsule 30 mg | Capsule | MSN Laboratories Private Limited |
| SIN16307P | FLUVIR Oseltamivir Phosphate Capsules 75 mg | Capsule | Hetero Labs Limited |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no supporting literature and no plausible mechanism. A viral neuraminidase inhibitor is not expected to treat a bacterial kidney infection, so the high TxGNN score alone does not justify further work on this indication.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications and approved indication), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence of oseltamivir activity in urinary tract or kidney infection; without it, this candidate should not advance

**Note on other candidates:** Among the other predictions in the Evidence Pack, **pneumonia** (rank 8) has the most evidence, with many registered trials and literature at L3. That support applies to influenza-associated pneumonia, which is close to the existing influenza indication and is not a truly new one. The staphylococcal, streptococcal pneumonia and aspergillosis candidates are L4 research questions only.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

