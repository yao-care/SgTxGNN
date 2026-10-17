---
layout: default
title: Etravirine
parent: Medium Evidence (L3-L4)
nav_order: 411
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Etravirine: predicted new indication Simian immunodeficiency virus infection (evidence level L4). Approved use: HIV infectious disease"
monitor_inn: "Etravirine"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "benign prostate phyllodes tumor", "obsolete familial combined hyperlipidemia"]
---

# Etravirine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Etravirine: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Etravirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI), originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**, but there are **0 clinical trials** and only **1 indirect publication** (an in vitro HIV study) supporting this direction.
The prediction is best treated as a research question, not an actionable repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (the Singapore licence text lists no approved indication) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, etravirine is an NNRTI that inhibits HIV-1 reverse transcriptase, and its efficacy in HIV infection is established. Simian immunodeficiency virus (SIV) is a closely related lentivirus, which is why the model places it close to HIV in the knowledge graph.

However, the mechanistic link is weak. SIV and HIV-2 are intrinsically resistant to most NNRTIs, so activity of etravirine against SIV is not expected from its class mechanism. The high TxGNN score most likely reflects network proximity to the HIV indication rather than a demonstrated pharmacological effect.

Also note that SIV infection is an animal (non-human primate) disease. Any value would be as a research model rather than a human therapeutic indication.

Other predictions in the top 10 are not better supported:
- **Feline acquired immunodeficiency syndrome** (score 99.98%): veterinary, no evidence, and NNRTI activity against FIV is generally poor.
- **AIDS related complex** and **congenital HIV**: these largely overlap with the existing HIV indication, so they are effectively on-label use rather than true repurposing. Evidence is observational or virologic only (Evidence Level L3).
- **Rare neurodevelopmental disorder, benign prostate and reproductive neoplasms, Brenner tumor, obsolete familial combined hyperlipidemia**: no plausible mechanism and no evidence. These look like graph artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26529558](https://pubmed.ncbi.nlm.nih.gov/26529558/) | 2015 | Preclinical (in vitro) | Molecular Pharmaceutics | Nanoparticle-based antiretroviral combinations for synergistic inhibition of cell-free and cell-cell HIV transmission. This concerns HIV, not SIV, so it is indirect evidence only. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14535P | INTELENCE TABLET 200 MG | Tablet (oral) | Not stated in the data compiled for this report |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): chronic hepatitis C virus infection, hepatitis C virus infection, chronic hepatitis B virus infection, peripheral nervous system disease, and peripheral neuropathy.
- **Drug Interactions**: 100 interactions were identified in total. The list reviewed contains mostly Moderate-level entries and one Minor entry. Notable examples include:
  - Acid-suppressing drugs: omeprazole, rabeprazole, cimetidine, ranitidine (minor)
  - Corticosteroids: dexamethasone, betamethasone, hydrocortisone, triamcinolone
  - Antidiabetic drugs: pioglitazone, glimepiride, chlorpropamide, saxagliptin, linagliptin
  - Others: clarithromycin, metronidazole, aprepitant, eliglustat, dronabinol, naloxegol, naldemedine

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on network proximity to the HIV indication. There are no clinical trials and only one indirect in vitro HIV paper. SIV is intrinsically resistant to most NNRTIs, and it is a non-human disease outside the human repurposing scope.

**To proceed, the following is needed:**
- Mechanism of action data for etravirine
- Package insert warnings and contraindications from HSA (needed before any safety screening)
- Direct in vitro or animal data on etravirine activity against SIV
- A decision on whether a non-human indication is within the scope of this programme
- For HIV-related labels (AIDS related complex, congenital HIV), treat them as existing on-label use and assess them within the current HIV indication, with dedicated pregnancy safety data where relevant
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

