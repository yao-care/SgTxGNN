---
layout: default
title: Norfloxacin
parent: Low Evidence (L5)
nav_order: 723
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Norfloxacin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Typhoid fever, salmonellosis, paratyphoid fever…"
monitor_inn: "Norfloxacin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "punctate epithelial keratoconjunctivitis", "premalignant hematological system disease", "diffuse scleroderma", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Norfloxacin
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

## Norfloxacin: From Bacterial Infections to Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Norfloxacin is a fluoroquinolone antibiotic originally used for urinary tract infections, gastrointestinal infections (dysentery, diarrhoeal disease, typhoid and paratyphoid fever, salmonellosis) and respiratory and other bacterial infections.
The TxGNN model predicts it may be effective for **hyperamylasemia**, with a very high score but **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on knowledge-graph proximity alone and should be treated as a computational hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Typhoid fever, salmonellosis, paratyphoid fever, urinary tract infection, bronchitis, bacterial pneumonia, dysentery and other bacterial infections (the Singapore licence text lists no approved indication, so these come from the knowledge graph) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, norfloxacin is a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV. This explains its efficacy against bacterial infections of the urinary and gastrointestinal tracts.

No identifiable mechanistic link connects this action to hyperamylasemia. Hyperamylasemia is a laboratory finding with varied causes (pancreatic, salivary, renal), not an infection. The high TxGNN score comes from graph-based prediction only, and no trials or literature support it.

**Other predictions reviewed** (all with no clinical trials):
- **Septicemic plague (rank 10, L4, "Research Question")**: the only biologically plausible candidate. *Yersinia pestis* is within the fluoroquinolone antibacterial spectrum, and other fluoroquinolones are used for plague. The retrieved papers are preclinical and do not show norfloxacin-specific efficacy. Norfloxacin's limited serum and tissue levels also make it unsuitable for septicaemia.
- **Punctate epithelial keratoconjunctivitis (rank 5, L4)**: only microsporidial keratoconjunctivitis case series were found, with no demonstrated norfloxacin benefit.
- **Remaining predictions** (polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, diffuse scleroderma, monoclonal gammopathy and others): no plausible mechanism and no supporting evidence. For diffuse scleroderma and neuropathy-related conditions, fluoroquinolone safety warnings argue for caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for hyperamylasemia.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08998P | LOXONE-400 TABLET 400 mg (Micro Labs Ltd) | Film-coated tablet | Not stated in the licence data |

---

## Safety Considerations

- **Contraindications / risk conditions (from knowledge-graph drug-disease edges, not label text)**: long QT syndrome, torsades de pointes, epilepsy, liver failure and liver disease, kidney disease, tendinitis, peripheral neuropathy, rhabdomyolysis, diabetes mellitus, thrombocytopenia, psychotic and other mental disorders, and potassium deficiency.
- **Drug Interactions**: 100 interactions were recorded. Major-level examples include:
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), which raise tendon-injury risk
  - Bupropion
  - Chlorpropamide
- **Moderate-level interactions** include antidiabetic agents (metformin, pioglitazone, acarbose, alogliptin, canagliflozin, albiglutide), calcium salts, famotidine, loperamide and aspirin. Several antidiabetic agents appear here, so blood-glucose monitoring is relevant.

Please refer to the package insert for authoritative warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The hyperamylasemia prediction has no clinical trials, no literature and no plausible mechanism (Evidence Level L5). The safety profile also includes many risk conditions and major interactions. Of the predictions reviewed, only septicemic plague has a plausible class-level rationale, and it is limited by norfloxacin's poor systemic exposure.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any clinical or mechanistic evidence linking norfloxacin to hyperamylasemia, or norfloxacin-specific data for plague, before reconsidering
- A review of the other predicted indications if a broader repurposing assessment is wanted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

