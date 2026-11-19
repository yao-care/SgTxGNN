---
layout: default
title: Remdesivir
parent: Low Evidence (L5)
nav_order: 859
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-12
description: "Remdesivir: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not available"
monitor_inn: "Remdesivir"
predicted_indications: ["multiple endocrine neoplasia", "HIV infectious disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "homozygous familial hypercholesterolemia"]
---

# Remdesivir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Remdesivir: From an Antiviral Injection to Multiple Endocrine Neoplasia
{: .text-alpha }

## One-Sentence Summary

Remdesivir is a nucleotide analogue antiviral that inhibits viral RNA polymerase. It is marketed in Singapore as an intravenous infusion, and the approved indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia** (score 0.9950), but there are **0 clinical trials** and **0 publications** supporting this prediction.
This is a model prediction only, with no identifiable mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the Singapore licence does not list indication text) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 0.9950 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for remdesivir: "Remdesivir is an antiviral drug with activity against severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). […] Remdesivir is an inhibitor of the SARS-CoV-2 RNA-dependent RNA polymerase (RdRp), which is essential for viral replication. Remdesivir is an adenosine nucleotide prodrug that distributes into cells where it is metabolized to a nucleoside monophosphate intermediate by carboxyesterase 1 and/or cathepsin A, depending upon the cell type." ([DailyMed: Veklury (remdesivir) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c0978fa8-53ff-4ca2-82a7-567fd3e958ca), label version 2026-07-29; accessed 2026-11-19.) From general knowledge, remdesivir is a nucleotide analogue prodrug that inhibits viral RNA-dependent RNA polymerase, which is the basis of its antiviral activity.

Multiple endocrine neoplasia is a hereditary tumour syndrome (for example, MEN1 or RET mutations). Its biology has no connection to viral RNA polymerase inhibition. The high TxGNN score (0.9950) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

For context, the other top predictions are also weakly supported:
- **HIV infection** (score 0.9932, evidence L4): the only prediction with a clinical trial, but that trial (NCT04385719) is a pharmacokinetic drug-interaction study in healthy volunteers, not an efficacy study. The literature is almost entirely about COVID-19.
- **Simian and feline immunodeficiency**, and several genetic or cardiovascular conditions: no plausible mechanistic link, with prediction-only or reverse-direction evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for multiple endocrine neoplasia.

---

## Literature Evidence

Currently no related literature available for multiple endocrine neoplasia.

---

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN15950P | VEKLURY® LYOPHILIZED POWDER FOR IV INFUSION 100MG/VIAL | INJECTION, POWDER, LYOPHILIZED, FOR SOLUTION | Valid |

<!-- licenses:end -->

---

## Cytotoxicity

Remdesivir is an antiviral, not an antineoplastic agent, so this assessment does not apply.

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interacting drugs. The 20 shown to the report are all rated Moderate. Examples include:
  - Antibiotics: doxycycline, minocycline, tetracycline, clarithromycin, levofloxacin, vancomycin, kanamycin, neomycin
  - Antifungals: amphotericin B, including the lipid complex formulation
  - Diabetes drugs: acarbose, pioglitazone
  - Others: bupropion, naltrexone, mesalazine, balsalazide, olsalazine, chenodeoxycholic acid, oxandrolone, oxymetholone

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (evidence level L5). There are no trials or publications, and remdesivir's antiviral mechanism has no plausible link to a hereditary endocrine tumour syndrome. Prediction scores this high do not substitute for biological rationale.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis connecting remdesivir to multiple endocrine neoplasia, plus preclinical data
- The mechanism-of-action data for remdesivir from DrugBank
- The HSA package insert (warnings, contraindications, approved indication), which is needed before any safety screening
- If antiviral repurposing is of interest, reviewing better-supported directions first (for example, the HIV-related pharmacokinetic work), noting that these also lack efficacy evidence

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Veklury (remdesivir) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c0978fa8-53ff-4ca2-82a7-567fd3e958ca) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

