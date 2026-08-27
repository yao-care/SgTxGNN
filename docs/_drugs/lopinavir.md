---
layout: default
title: Lopinavir
parent: 僅模型預測 (L5)
nav_order: 607
evidence_level: L5
indication_count: 10
---

# Lopinavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Lopinavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Lopinavir is an HIV-1 protease inhibitor, typically co-formulated with ritonavir (Kaletra/Aluvia), that blocks viral maturation and has been a cornerstone of antiretroviral therapy — though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**,
with **0 clinical trials** and **3 animal study publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; established HIV-1 protease inhibitor |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Lopinavir inhibits the HIV-1 aspartyl protease, preventing cleavage of the Gag-Pol polyprotein during viral assembly. Without this processing step, immature, non-infectious virions are produced. It is invariably co-administered with ritonavir, a CYP3A4 inhibitor that acts as a pharmacokinetic booster to sustain therapeutically effective lopinavir plasma concentrations.

The rationale for an SIV prediction rests on structural analogy: SIV possesses a homologous aspartyl protease, but its amino-acid sequence diverges substantially from HIV-1. This divergence means lopinavir's binding affinity to wild-type SIV protease is considerably weaker than to its intended HIV-1 target — making direct clinical translation uncertain. A key nuance in the evidence is that the animal studies available involve **SHIV** (chimeric SIV constructs that carry the HIV-1 protease gene inserted into an SIV backbone), not authentic wild-type SIV. In SHIV models, lopinavir activity is expected and mechanistically predictable; for wild-type SIV, efficacy remains unestablished.

The very high TxGNN prediction score most likely reflects knowledge-graph co-clustering of HIV and SIV nodes — a network topology signal — rather than a confirmed pharmacological signal against wild-type SIV protease. The mechanistic connection is indirect analogy, not direct biological equivalence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal Study (Macaque) | Journal of Virology | Quadruple ART including lopinavir produced rapid viral decay in cynomolgus macaques infected with SIVmac251, modelling HIV-1 kinetic parameters |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal Study (Macaque) | Journal of Virological Methods | Oral LPV/r + AZT + 3TC (HAART) modulated peripheral CD8 subsets in SHIV(89.6P)-infected rhesus macaques; LPV/r active in chimeric SHIV model |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Animal Model Construction | Microbes and Infection | Construction of SHIV-pr carrying HIV-1 protease gene; viral growth completely blocked by peptide-analog PI in vitro; weak persistent viremia in inoculated macaques |

---

## Singapore Market Information

Lopinavir has no marketing authorizations on record with the Health Sciences Authority (HSA) of Singapore. The drug is classified as **not marketed**.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is confined to preclinical macaque studies using SHIV chimeric models (which incorporate the HIV-1 protease gene), rather than wild-type SIV, providing insufficient basis to advance lopinavir as a repurposing candidate for SIV infection in any clinical or translational context.

**To proceed, the following is needed:**

- **MOA clarification against wild-type SIV protease**: quantitative inhibition data (IC₅₀ comparison: HIV-1 PR vs. SIV PR) to determine whether any biologically meaningful activity exists
- **Clarification of clinical intent**: SIV infection is a non-human primate disease — if the downstream goal is primate research (e.g., vaccine model support) rather than human indication, a fundamentally different evaluation framework applies
- **Singapore (HSA) regulatory filing**: obtain approved indications, full label warnings, and contraindication text to enable S1 safety screening
- **DrugBank MOA data**: retrieve full mechanism-of-action, drug interaction, and toxicity profiles to complete the evidence dossier before any further development decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

