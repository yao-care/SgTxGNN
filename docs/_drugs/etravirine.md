---
layout: default
title: Etravirine
parent: 僅模型預測 (L5)
nav_order: 407
evidence_level: L5
indication_count: 10
---

# Etravirine
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

# Etravirine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Etravirine (Intelence) is a second-generation non-nucleoside reverse transcriptase inhibitor (NNRTI) approved for the treatment of HIV-1 infection in treatment-experienced adults and pediatric patients aged 2 years and older.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**,
with **0 clinical trials** and **1 preclinical publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (treatment-experienced patients) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Etravirine is a second-generation NNRTI belonging to the diarylpyrimidine (DAPY) class. It works by binding non-competitively to HIV-1 reverse transcriptase (RT) in a highly flexible manner, allowing its scaffold to reposition and maintain contact with the RT binding pocket even when common resistance mutations (e.g., K103N, Y181C) are present. This flexibility distinguishes it from first-generation NNRTIs such as efavirenz and nevirapine.

SIV (Simian Immunodeficiency Virus) and HIV-1 belong to the same genus of lentiviruses, and their reverse transcriptase enzymes share a conserved overall three-dimensional structure. The TxGNN model's high prediction score almost certainly reflects this shared RT target — the knowledge graph links Etravirine to lentiviral RT inhibition, and SIV infection occupies a closely connected node.

However, there is a critical limitation: the NNRTI binding pocket in SIV reverse transcriptase contains important amino acid differences from HIV-1, including the absence of key contact residues such as K101. Inhibitory activity of NNRTIs — including Etravirine — against SIV RT has not been established in published preclinical studies. Furthermore, SIV is a non-human primate pathogen with no direct human clinical application. The scientific value of this prediction is therefore confined to basic research into cross-species lentiviral RT biology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26529558](https://pubmed.ncbi.nlm.nih.gov/26529558/) | 2015 | In vitro / Preclinical | Molecular Pharmaceutics | Nanoparticle-based delivery systems for ARV drug combinations (including NNRTIs) demonstrate synergistic inhibition of cell-free and cell-cell HIV transmission; mechanistic relevance to SIV is indirect and not discussed in the study |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the structural homology between SIV and HIV-1 reverse transcriptase provides a superficially plausible mechanistic basis, SIV is a non-human primate pathogen with no direct clinical relevance for human medicine. The single supporting publication is a preclinical HIV nanoparticle study with only indirect applicability to SIV, and known differences in the NNRTI binding pocket between SIV and HIV-1 RT mean that inhibitory activity against SIV cannot be assumed from the HIV-1 data.

**To proceed, the following is needed:**
- In vitro enzyme inhibition data confirming Etravirine activity against SIV reverse transcriptase (IC₅₀ determination)
- Structural analysis comparing the NNRTI binding pocket of SIV RT versus HIV-1 RT (particularly residues Y181, Y188, and K101 equivalents)
- A clearly defined scientific rationale for the research question (e.g., using SIV as an animal model surrogate for HIV treatment studies)
- Mechanism of action (MOA) data from DrugBank to complete drug-level characterisation
- TFDA/HSA package insert review to identify safety warnings and contraindications before any downstream research planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

