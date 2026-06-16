---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 362
evidence_level: L5
indication_count: 10
---

# Efavirenz
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

# Efavirenz: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Efavirenz (EFV) is a non-nucleoside reverse transcriptase inhibitor (NNRTI) established globally for the treatment of HIV-1 infection, though it carries no registration in Singapore.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**, with **1 clinical trial** (withdrawn, 0 enrolled) and **16 publications** identified in support of this direction.
Critically, all existing evidence is based on animal model studies using a chimeric RT-SHIV virus — this represents a research tool scenario rather than a human clinical repurposing target.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 Infection (established global use; no Singapore registration on record) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank query. Based on established pharmacological knowledge, Efavirenz is a non-nucleoside reverse transcriptase inhibitor that binds directly and non-competitively to HIV-1 reverse transcriptase (RT), blocking viral RNA-to-DNA transcription and halting HIV-1 replication. This mechanism is highly specific to HIV-1 RT and does not apply to native SIV reverse transcriptase, which has meaningful structural differences in its NNRTI binding pocket that render it insensitive to EFV.

The reason TxGNN assigns a high prediction score for SIV infection is that the research literature extensively uses **RT-SHIV** — an artificially constructed chimeric virus with an SIV backbone but HIV-1 reverse transcriptase substituted in. Because this chimera incorporates HIV-1 RT, it retains sensitivity to NNRTIs including EFV. Multiple animal studies (2004–2022) demonstrate that EFV-containing HAART regimens effectively suppress RT-SHIV viral loads in rhesus and pigtail macaques by 3+ log orders, making this a validated nonhuman primate model for studying HIV treatment strategies, drug resistance evolution, and viral reservoir dynamics.

However, this is fundamentally a **research tool application, not a clinical repurposing opportunity**. There is no human patient population with "SIV infection," and the mechanistic link depends entirely on the artificial RT-SHIV construct rather than native SIV biology. Direct extrapolation to a human clinical translation pathway is not appropriate. For genuine clinical repurposing candidates in this Evidence Pack, see **AIDS Related Complex** (Rank 5, L1 evidence) and **Congenital HIV** (Rank 6, L1 evidence), both of which carry substantial Phase 3 RCT data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | N/A | Withdrawn | 0 | Planned study of HIV RNA decay kinetics with the integrase inhibitor raltegravir; referenced SIV primate decay comparisons as background context. Study was withdrawn before enrollment began. Research drug was raltegravir, not EFV; indication was HIV-1, not SIV — no evidence contribution to this indication. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15328115](https://pubmed.ncbi.nlm.nih.gov/15328115/) | 2004 | Animal Study | Antimicrobial Agents and Chemotherapy | Foundational study: EFV therapy evaluated directly in rhesus macaques infected with RT-SHIV (SIV backbone + HIV-1 RT). Demonstrated that EFV suppresses the chimeric virus through its NNRTI activity against the HIV-1 RT component — the mechanistic basis for all subsequent RT-SHIV/EFV literature. |
| [15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/) | 2005 | Animal Study | Journal of Virology | HAART (EFV 200 mg + lamivudine + tenofovir) in 7 RT-SHIV-infected rhesus macaques reduced plasma viral RNA by >3 log₁₀ copies/mL. Established the RT-SHIV HAART model as a proof-of-concept platform mirroring HIV treatment in humans. |
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | In Vitro | Journal of Virology | In vitro characterisation of the SIV-HIV-1 chimeric RT-SHIV construct; confirmed NNRTI susceptibility profile and assessed potential for antiviral resistance studies in pigtail macaques — foundational for the animal model. |
| [19195672](https://pubmed.ncbi.nlm.nih.gov/19195672/) | 2009 | Animal Study | Virology | RT-SHIV characterised for vaginal transmission in Chinese rhesus macaques; viral RNA accumulated in lymph nodes and spleen correlating with plasma viremia — relevant to understanding tissue reservoir formation in the EFV model. |
| [19889213](https://pubmed.ncbi.nlm.nih.gov/19889213/) | 2009 | Animal Study | Retrovirology | RT-SHIV subpopulation dynamics in pigtail macaques: short-course EFV monotherapy followed by combination ART; single-genome sequencing tracked wild-type and drug-resistant HIV-1 RT variants over time. |
| [20668516](https://pubmed.ncbi.nlm.nih.gov/20668516/) | 2010 | Animal Study | PLoS ONE | Characterised viral decay kinetics in HAART-treated rhesus macaques (EFV + 3TC + TDF); demonstrated biphasic viral decay and persistent residual viremia consistent with human HIV HAART responses. |
| [21084490](https://pubmed.ncbi.nlm.nih.gov/21084490/) | 2011 | Animal Study | Journal of Virology | SIV/HIV chimera (RT-SHIV) genetic diversity analysed before, during, and after ART including short-course EFV monotherapy in pigtail macaques; diversity persisted despite treatment. |
| [22933296](https://pubmed.ncbi.nlm.nih.gov/22933296/) | 2012 | Virology/Sequencing | Journal of Virology | Ultrasensitive allele-specific PCR detected rare pre-existing EFV-resistant variants in RT-SHIV-infected macaques before ART; characterised how resistance mutations emerge under drug selection pressure. |
| [24777106](https://pubmed.ncbi.nlm.nih.gov/24777106/) | 2014 | Animal Study | Antimicrobial Agents and Chemotherapy | Four- and five-drug HAART (including integrase inhibitor L-870-812 added to EFV-containing backbone) in RT-SHIV rhesus macaques; enhanced regimens improved early viral decay and reduced rebound upon cessation. |
| [35856680](https://pubmed.ncbi.nlm.nih.gov/35856680/) | 2022 | Translational Imaging | Antimicrobial Agents and Chemotherapy | Mass spectrometry imaging of 6 ARVs (including EFV) in spleens of RT-SHIV-infected nonhuman primates; mapped spatial relationship between drug tissue distribution, viral RNA expression, and fibrosis markers — most recent study in this series. |

---

## Singapore Market Information

Efavirenz is currently **not registered** with Singapore's Health Sciences Authority (HSA). No product authorisations exist in the local regulatory database, and market status is confirmed as "not marketed."

Any clinical use in Singapore would require accessing EFV through special order, compassionate use channels, or institutional import, subject to HSA approval on a case-by-case basis.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: TFDA package insert warnings and contraindications were identified as a blocking data gap (DG001). DDI data was not returned from the query. A full safety profile including CYP3A4 induction interactions, CNS neuropsychiatric effects, and teratogenicity concerns (Category D in pregnancy) should be reviewed from the originator label and WHO prescribing information before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction of EFV for "simian immunodeficiency virus infection" reflects the drug's established role in RT-SHIV primate research models, not a translatable human clinical indication. Native SIV is not sensitive to EFV; all 16 publications involve the artificially chimeric RT-SHIV virus engineered to carry HIV-1 reverse transcriptase. There is no identifiable human patient population with SIV infection, and the single registered clinical trial was withdrawn before enrolling a single participant. This prediction is best characterised as a **knowledge graph topology artefact** — the model correctly identified a biological connection, but the connection is a research model construct rather than a clinical treatment target.

**To proceed, the following is needed:**

- **Redirect attention to higher-value candidates**: If the goal is HIV-spectrum drug repurposing, **AIDS Related Complex** (Rank 5, L1, 5 clinical trials including Phase 3b, 17 publications) and **Congenital HIV / PMTCT** (Rank 6, L1, multiple Phase 3 RCTs, 20 publications) offer far more actionable evidence with established human clinical relevance
- **Resolve blocking data gaps**: Obtain EFV package insert (TFDA or FDA label) for safety warnings, contraindications, and CYP3A4 DDI profile (DG001 — Blocking severity)
- **MOA documentation**: Retrieve EFV DrugBank MOA data (DG002 — High severity) to enable mechanistic link analysis for any repurposing candidate
- **Singapore import pathway**: If EFV is to be considered for any Singapore patient use, map HSA compassionate use or special access procedures given zero local registrations
- **KG quality flag**: Recommend flagging the SIV infection node connection for knowledge graph review — the edge likely reflects RT-SHIV model co-citation rather than a genuine treatment relationship, and may be contributing to similar false-positive clusters seen in reproductive system neoplasm predictions (Ranks 7–10)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

