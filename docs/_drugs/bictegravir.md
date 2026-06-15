---
layout: default
title: Bictegravir
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 10
---

# Bictegravir
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

# Bictegravir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Bictegravir is a second-generation integrase strand transfer inhibitor (INSTI), widely approved in international markets as part of the fixed-dose combination Biktarvy (bictegravir/emtricitabine/tenofovir alafenamide, B/F/TAF) for the treatment of HIV-1 infection in adults.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**, with **0 clinical trials** and **3 preclinical publications** currently supporting this direction.
This prediction reflects cross-species mechanistic validity rather than a conventional clinical repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (approved in other markets; not registered in Singapore) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacological knowledge, Bictegravir is a potent second-generation INSTI. It binds to the HIV integrase–DNA complex and blocks the strand transfer step, preventing insertion of viral cDNA into the host cell chromosome. This makes it the active antiretroviral core of the Biktarvy fixed-dose combination.

SIV is a retrovirus that naturally infects non-human primates and is phylogenetically closely related to HIV-1. Crucially, SIV integrase shares high structural homology with HIV-1 integrase — providing a direct mechanistic basis for Bictegravir's predicted cross-species activity. In vitro experiments (PMID 28923862) have directly confirmed that Bictegravir inhibits integrase inhibitor-resistant SIVmac239 variants with potency comparable to its activity against HIV-1, and structural biology studies (PMID 32506843) explain this through shared intasome architecture.

However, SIV infection is not a human clinical disease. Its primary relevance is as a non-human primate (NHP) preclinical model for studying HIV pathogenesis, latency, and cure strategies. A 2024 humanized mouse study (PMID 39559349) further demonstrates deployment of Bictegravir-containing regimens to test efficacy against both SIV and HIV in small-animal models. This TxGNN prediction is therefore best understood as mechanistic validation for research tool use, not a clinical repurposing pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | In vitro / Preclinical | Antimicrobial Agents and Chemotherapy | Bictegravir inhibits integrase inhibitor-resistant SIVmac239 and HIV-1 in vitro; demonstrates a higher genetic barrier to resistance than first-generation INSTIs raltegravir and elvitegravir |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | Structural Biology / Mechanistic Review | The FEBS Journal | Cryo-EM and X-ray intasome structures reveal how second-generation INSTIs including Bictegravir achieve high resistance barriers; covers HIV/SIV integrase structural homology and drug binding mechanisms |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Animal Model Study | Frontiers in Immunology | Dual-purpose humanized mouse model validates Bictegravir-containing ARV regimens against both SIV and HIV; proposes a small-animal alternative to NHP models for cost-effective preclinical testing |

---

## Singapore Market Information

Bictegravir (as Biktarvy B/F/TAF) is currently **not registered** with the Health Sciences Authority (HSA) of Singapore. There are no product authorizations on record. Any clinical use in Singapore would require a full HSA new drug application or access via the Special Access Route (SAR).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
SIV infection is an animal model condition rather than a human clinical disease, and there are no human clinical trials in this indication. Although Bictegravir has confirmed in vitro activity against SIV integrase, the drug is not registered in Singapore and the biological relevance of this prediction is confined to preclinical NHP/humanized mouse research. This does not meet the threshold for clinical repurposing evaluation.

**Notable context across all 10 predicted indications:** Among the full TxGNN output for this Evidence Pack, **AIDS Related Complex (Rank 5)** carries the highest evidence level (L1 — Phase 3 RCT ARTISTRY-1, *Lancet* 2026, PMID 41763229), and **Congenital HIV / Vertical Transmission Prevention (Rank 6)** is supported by L2 evidence including an active neonatal B/F/TAF PK study (NCT07055451). These two indications are substantially more actionable and are recommended for dedicated evaluation reports.

**To proceed with research or clinical development, the following is needed:**

- Retrieve MOA data from DrugBank API (active Data Gap — DG002)
- Retrieve Singapore package insert warnings and contraindications from HSA (active Data Gap — DG001)
- Assess HSA regulatory pathway for Biktarvy market authorization in Singapore
- If pursuing SIV research use: design NHP study protocol and obtain species-specific pharmacokinetic data
- Initiate separate evaluation reports for **AIDS Related Complex** and **Congenital HIV**, which carry actionable clinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

