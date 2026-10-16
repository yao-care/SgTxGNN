---
layout: default
title: Tigecycline
parent: Medium Evidence (L3-L4)
nav_order: 990
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Tigecycline: predicted new indication Disorder of tyrosine metabolism (evidence level L4). Approved use: Streptococcal pneumonia"
monitor_inn: "Tigecycline"
predicted_indications: ["disorder of tyrosine metabolism", "teratogenic Pierre Robin syndrome", "tetrahydrobiopterin-responsive hyperphenylalaninemia/phenylketonuria", "disorder of phenylalanine metabolism", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy"]
---

# Tigecycline
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Tigecycline: From Streptococcal Pneumonia to Disorder of Tyrosine Metabolism

## One-Sentence Summary

Tigecycline is an injectable glycylcycline antibiotic, originally used to treat infections such as streptococcal pneumonia.
The TxGNN model predicts it may be effective for **disorder of tyrosine metabolism**,
but there are currently **no registered clinical trials** and only **4 publications** (all preclinical or commentary, none showing a therapeutic effect in this condition), so the prediction rests almost entirely on computation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Streptococcal pneumonia (from the knowledge graph; the Singapore licence records contain no approved indication text) |
| Predicted New Indication | Disorder of tyrosine metabolism |
| TxGNN Prediction Score | 95.76% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, tigecycline is a glycylcycline (a tetracycline-class antibiotic) that inhibits the bacterial 30S ribosome. Its efficacy in bacterial infections such as streptococcal pneumonia is established.

The link to tyrosine metabolism is weak. The retrieved literature mostly describes tigecycline inhibiting mitochondrial translation and oxidative phosphorylation (OXPHOS) in cancer stem cells and leukaemia cells. One 2025 in vitro study examined its effects on human epidermal melanocytes and fibroblasts. Because melanin synthesis depends on tyrosine metabolism, this is tangentially relevant, but it describes pigment-related side effects, not a treatment benefit in a tyrosine metabolism disorder.

The high TxGNN score is a computational prediction from knowledge-graph relationships. It is not supported by clinical data, and no direct mechanistic connection has been established.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41009505](https://pubmed.ncbi.nlm.nih.gov/41009505/) | 2025 | In vitro study | Int J Mol Sci | Examined tigecycline's effects on human epidermal melanocytes and fibroblasts, in the context of known pigmentary and phototoxic side effects of tetracyclines |
| [31765940](https://pubmed.ncbi.nlm.nih.gov/31765940/) | 2020 | Preclinical | Neoplasia | Targeting SIRT1 and mitochondrial OXPHOS eradicated EGFR TKI-resistant cancer stem cells in lung adenocarcinoma (not about tyrosine metabolism) |
| [28920959](https://pubmed.ncbi.nlm.nih.gov/28920959/) | 2017 | Preclinical | Nature Medicine | Targeting mitochondrial OXPHOS (tigecycline with imatinib) eradicated therapy-resistant chronic myeloid leukaemia stem cells |
| [29404396](https://pubmed.ncbi.nlm.nih.gov/29404396/) | 2018 | Commentary | Mol Cell Oncol | Author commentary on the CML stem cell study; tigecycline plus imatinib prevented relapse in preclinical models |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16104P | Tigeccord (Tigecycline for Injection USP 50 mg/vial) | Injection, powder, for solution | Not available in licence record |
| SIN13282P | Tygacil (Tigecycline) Injection 50 mg | Injection, powder, lyophilised, for solution | Not available in licence record |

---

## Safety Considerations

- **Contraindication-related conditions (from knowledge graph, not label text)**: liver failure, hyperbilirubinaemia (including hereditary forms and Gilbert syndrome), *Clostridium difficile* colitis, perinatal necrotising enterocolitis, pancreatitis.
- **Drug Interactions**: 30 interactions were recorded. Those graded Moderate are picosulfuric acid, dicoumarol, warfarin, methoxsalen and tacrolimus. Others (for example vancomycin, clopidogrel, heparin, metronidazole, clarithromycin, simvastatin, prednisone, omeprazole and morphine) have no severity grade assigned.
- **Class-level considerations**: tetracycline-class effects on tooth and bone development raise fetal-risk concerns, and pigmentary and phototoxic effects have been described for the class.

For full warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score. There are no clinical trials, and the available literature is preclinical and does not address tyrosine metabolism disorders. No plausible mechanism connects tigecycline to this condition, and the drug's safety profile (hepatic, pancreatic and fetal concerns) adds caution.

**To proceed, the following is needed:**
- Mechanism of action data and a testable hypothesis linking tigecycline to tyrosine metabolism
- Preclinical evidence in relevant disease models of tyrosine metabolism disorders
- The package insert warnings and contraindications from the Singapore Health Sciences Authority (HSA), required for safety screening
- A review of the risk-benefit balance for a chronic metabolic condition, given that tigecycline is an injectable antibiotic with hepatic and pancreatic safety concerns

**Other predicted indications (for reference):** Of the other nine predictions, none has clinical trial support. Monoclonal gammopathy has indirect and mixed preclinical myeloma evidence (including one study showing tigecycline opposing the effect of bortezomib), so it is flagged only as a research question. The others, including hyperamylasaemia (which may reflect a known adverse-effect signal rather than a therapeutic opportunity), have no supporting evidence and remain on Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

