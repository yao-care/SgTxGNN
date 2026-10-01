---
layout: default
title: Lopinavir
parent: Low Evidence (L5)
nav_order: 607
evidence_level: L5
indication_count: 10
---

# Lopinavir
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

# Lopinavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Lopinavir is an HIV-1 protease inhibitor, sold in Singapore as the lopinavir/ritonavir product Kaletra. The registration data supplied do not record its approved indication, so this is based on the drug's known use.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**, but **no clinical trials** exist and only **3 preclinical macaque publications** support this. SIV is an animal-model infection, not a human indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Singapore registration data (lopinavir/ritonavir is known as an HIV-1 antiretroviral) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (preclinical studies only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Lopinavir is a retroviral aspartic protease inhibitor, and the SIV protease is homologous to the HIV-1 protease. This shared target is the most likely reason the model links the two infections.

The three macaque papers show lopinavir being used in non-human primate models, either as part of combination antiretroviral therapy or as a tool for testing protease inhibitors. This is animal-model use, not a new treatment opportunity. SIV is not a human disease, and the human HIV indication is covered separately in the model's other predictions. There is little repurposing value here beyond research use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Preclinical (macaque) | Journal of Virology | Four SIVmac251-infected cynomolgus macaques received a 7-day course of quadruple antiretroviral therapy. The study modelled viral decay and reported rapid viral decline. |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Preclinical (macaque, SHIV construct) | Microbes and Infection | A new SHIV carrying the HIV-1 protease gene was built as a tool for testing protease inhibitors in vivo. A peptide-analog protease inhibitor completely blocked its growth in cell culture. Two rhesus macaques inoculated with it developed a weak but long-lasting infection. |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Preclinical (monkey, HAART immunology) | Journal of Virological Methods | Two rhesus macaques chronically infected with SHIV 89.6P received oral AZT, 3TC and lopinavir/ritonavir for 28 days. The study assessed effects on the CD8 subset. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN13250P | Kaletra Tablet 200mg/50mg | Film-coated tablet | AbbVie Deutschland GmbH & Co. KG |
| SIN11492P | Kaletra Oral Solution | Syrup | AbbVie Inc. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only evidence is three animal-model papers and no registered clinical trials. SIV is not a human indication, so there is no clinical development path for this prediction. The stronger HIV-related predictions for lopinavir (congenital HIV, AIDS-related complex) largely reflect its existing HIV use rather than true repurposing.

**To proceed, the following is needed:**
- Original approved indication text from the Singapore registrations
- Package insert warnings and contraindications
- Mechanism of action data from DrugBank
- A decision on whether an animal-model-only prediction has any research value for this programme
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

