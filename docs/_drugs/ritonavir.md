---
layout: default
title: Ritonavir
parent: Medium Evidence (L3-L4)
nav_order: 867
evidence_level: L4
indication_count: 10
---

# Ritonavir
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

# Ritonavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Ritonavir is an HIV protease inhibitor and pharmacokinetic booster, marketed in Singapore in products such as Norvir and Kaletra.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, a non-human disease.
Currently **0 clinical trials** are registered, and the **11 publications** retrieved are mostly in vitro or macaque studies, so this is a model prediction with only preclinical support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred from the marketed products; the registry indication text was not provided) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Ritonavir is known to inhibit the HIV-1 aspartyl protease, and it is widely used at low doses as a CYP3A4 booster in combination regimens. Its efficacy in HIV-1 is established, and mechanistically it may be applicable to SIV.

SIV is a primate lentivirus closely related to HIV, and its protease is structurally similar to that of HIV-1. An in vitro assay supports this. Ritonavir inhibited SIVmac239 with an EC50 of 13 nM, compared with 25 nM for HIV-1.

The very high score most likely reflects the HIV-1 association inherited through the knowledge graph, not independent SIV evidence. SIV is mainly a research model for HIV, so there is no clinical development path for this indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No randomized trials or human studies were found. The most relevant publications are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro susceptibility | Antimicrob Agents Chemother | Ritonavir inhibited SIVmac239 (EC50 13 ± 5 nM), with potency similar to that against HIV-1 (25 ± 14 nM) |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility | Antivir Ther | Sixteen approved anti-HIV drugs were tested against HIV-2, SIV and SHIV strains to inform treatment and post-exposure prophylaxis |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Preclinical (macaque) | J Virol | In SIVmac251-infected cynomolgus macaques, a 7-day quadruple antiretroviral course was used to model viral decay |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Preclinical (macaque) | Microbes Infect | A chimeric SHIV carrying the HIV-1 protease gene was built as a tool for testing protease inhibitors in vivo |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Preclinical (macaque) | J Virol Methods | In two SHIV-infected macaques, oral AZT, 3TC and lopinavir/ritonavir for 28 days was used to assess the effect on the CD8 subset |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Preclinical (macaque) | PLoS Pathog | A highly intensified multidrug ART regimen suppressed viremia and restricted the viral reservoir in SIVmac251-infected macaques |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Preclinical (macaque) | PLoS One | Intensive cART plus the HDAC inhibitor SAHA was studied in SIV-infected Chinese rhesus macaques as a reservoir model |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Preclinical/Review | mBio | Lentiviral infection persists in the brain despite effective ART in several models |

Most of these studies test combination ART regimens, so ritonavir's own contribution cannot be separated out.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN14288P | Norvir Tablets 100 mg | Tablet, film coated | AbbVie Deutschland GmbH & Co. KG |
| SIN16877P | Paxlovid Film-Coated Tablets | Tablet, film coated | Pfizer Manufacturing Deutschland GmbH / Pfizer Ireland Pharmaceuticals / AbbVie Deutschland GmbH & Co. KG |
| SIN13250P | Kaletra Tablet 200mg/50mg | Tablet, film coated | AbbVie Deutschland GmbH & Co. KG |
| SIN11492P | Kaletra Oral Solution | Syrup | AbbVie Inc. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for SIV infection is in vitro susceptibility data and macaque studies used as models for HIV. No clinical trials exist, and SIV is not a human disease, so there is no clinical path. The high TxGNN score reflects the known HIV-1 association rather than new evidence.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism of action data from DrugBank
- Confirmation that SIV is a relevant target. If it is not, other predicted indications for ritonavir, such as hepatitis B, hepatitis E and congenital HIV, are better candidates for follow-up. In the hepatitis B and delta trials ritonavir acts mainly as a booster for partner drugs.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

