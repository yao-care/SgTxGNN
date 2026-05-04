---
layout: default
title: Atazanavir
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 10
---

# Atazanavir
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

# Atazanavir: From HIV-1 Infection to AIDS Related Complex

## One-Sentence Summary

Atazanavir (Reyataz, BMS-232632) is a well-established HIV-1 protease inhibitor approved in multiple major jurisdictions (US FDA, EMA) for the treatment of HIV-1 infection in adults and children, though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **AIDS Related Complex (ARC)** — an intermediate pre-AIDS stage of HIV disease — with **2 completed Phase 3 clinical trials** and **3 publications** directly supporting this direction.
A closely related prediction, **congenital (pediatric) HIV infection**, is further supported by over **10 clinical trials**, including multiple completed Phase 3 studies in infants and children.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (known global approved use; not registered in Singapore) |
| Predicted New Indication | AIDS Related Complex (ARC) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacological knowledge, Atazanavir belongs to the azapeptide class of HIV-1 protease inhibitors. It works by selectively and competitively binding to the catalytic site of HIV-1 protease — the enzyme responsible for cleaving the Gag-Pol polyprotein precursor into its structural and functional components. When protease is inhibited, newly budded viral particles remain immature and non-infectious, halting the progression of HIV replication at the post-translational level.

AIDS Related Complex (ARC) is a distinct clinical staging entity in HIV disease. It describes patients with confirmed HIV-1 infection who have declining CD4⁺ T-cell counts (typically 200–500 cells/mm³), constitutional symptoms (prolonged fever, night sweats, unexplained weight loss, lymphadenopathy), and early opportunistic infections, but who have not yet met the full CDC surveillance criteria for an AIDS diagnosis. The underlying pathological driver is identical to other stages of HIV infection: continuous HIV-1 replication causing progressive immune exhaustion and CD4⁺ cell depletion.

Because Atazanavir directly suppresses HIV-1 replication at the protease step, it mechanistically addresses the root cause of ARC progression. Atazanavir boosted with low-dose ritonavir (ATV/r) has been extensively studied in head-to-head Phase 3 trials against Lopinavir/Ritonavir (LPV/r), demonstrating non-inferior to superior virological suppression (HIV-1 RNA < 50 copies/mL), CD4⁺ T-cell recovery, and a more favourable lipid profile. The TxGNN prediction therefore reflects a mechanistically sound and clinically established relationship between this drug class and the full HIV disease spectrum, including ARC. The additional prediction for congenital HIV further validates the drug's utility in paediatric HIV, where specific powder and capsule formulations of ATV/r have been purpose-developed and Phase 3-tested for infants as young as three months.

---

## Clinical Trial Evidence

The following trials are the most directly relevant to AIDS Related Complex and congenital/paediatric HIV, selected from the top-evidence predictions (ranks 5 and 6):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00272779](https://clinicaltrials.gov/study/NCT00272779) | Phase 3 | Completed | 1,057 | 96-week head-to-head RCT: ATV/RTV vs LPV/RTV, each with TDF/FTC, in treatment-naïve HIV-1 adults; primary efficacy and long-term safety dataset for ATV-based regimens |
| [NCT02269917](https://clinicaltrials.gov/study/NCT02269917) | Phase 3 | Completed | 1,149 | Switch from boosted PI (including ATV/RTV) + FTC/TDF to D/C/F/TAF single-tablet regimen in virologically suppressed HIV-1 adults; comprehensive comparative efficacy, renal, and bone safety data |
| [NCT00035932](https://clinicaltrials.gov/study/NCT00035932) | Phase 3 | Completed | 571 | ATV with RTV or SQV plus TDF and a nucleoside vs LPV/RTV in treatment-experienced HIV subjects; directly supports ARC-context efficacy of Atazanavir |
| [NCT01910402](https://clinicaltrials.gov/study/NCT01910402) | Phase 3 | Completed | 499 | DTG/ABC/3TC vs ATV+RTV+TDF/FTC in ART-naïve HIV-1 infected women; comparative efficacy evidence for ATV-based regimen over 48 weeks |
| [NCT02227238](https://clinicaltrials.gov/study/NCT02227238) | Phase 3 | Completed | 627 | Dolutegravir vs LPV/RTV in first-line treatment failure patients; contextualises PI-class positioning in second-line therapy |
| [NCT01335698](https://clinicaltrials.gov/study/NCT01335698) | Phase 3 | Completed | 160 | PRINCE II: Safety, efficacy, and PK of ATV powder + RTV in HIV-infected children ≥3 months to <11 years; paediatric congenital HIV treatment evidence |
| [NCT01099579](https://clinicaltrials.gov/study/NCT01099579) | Phase 3 | Completed | 82 | PRINCE I: Safety, efficacy, and PK of ATV powder + RTV in HIV-infected infants and toddlers ≥3 months to <6 years; youngest-age paediatric formulation data |
| [NCT01691794](https://clinicaltrials.gov/study/NCT01691794) | Phase 4 | Completed | 108 | Real-world safety of ATV capsule + RTV in HIV-infected children and adolescents aged 6–18 years; paediatric long-term safety data |
| [NCT00207142](https://clinicaltrials.gov/study/NCT00207142) | Phase 4 | Completed | 252 | INDUMA: ATV/RTV induction followed by switch to unboosted ATV vs continued ATV/RTV maintenance; treatment simplification strategy for sustained virological suppression |
| [NCT01232127](https://clinicaltrials.gov/study/NCT01232127) | Phase 4 | Completed | 25 | Effect of famotidine (H2-blocker) on ATV/RTV pharmacokinetics in HIV-infected subjects; critical drug interaction management information for clinical practice |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [27242802](https://pubmed.ncbi.nlm.nih.gov/27242802/) | 2016 | Prospective Cohort | Frontiers in Immunology | PHACS SMARTT study: comprehensive safety assessment of in utero ART (including ATV) exposure in >3,500 HIV-exposed but uninfected infants across 22 US sites; domains include metabolic, cardiac, and neurodevelopmental outcomes |
| [25383770](https://pubmed.ncbi.nlm.nih.gov/25383770/) | 2015 | Cohort | JAMA Pediatrics | Congenital anomalies and in utero ARV (including ATV) exposure in HIV-exposed uninfected infants; overall safety profile reassuring for most ARV agents |
| [40011239](https://pubmed.ncbi.nlm.nih.gov/40011239/) | 2025 | Case/Non-case | European Journal of Clinical Pharmacology | European congenital anomaly registry evaluation of fetal ARV exposure risk; most recent pharmacoepidemiology data using large registry data |
| [28991888](https://pubmed.ncbi.nlm.nih.gov/28991888/) | 2018 | Cohort | Journal of Acquired Immune Deficiency Syndromes | Differential effects of common cART regimens on AIDS-defining neurological conditions; contextualises the role of ART in preventing ARC-to-neuroAIDS progression |
| [24992294](https://pubmed.ncbi.nlm.nih.gov/24992294/) | 2015 | PK Cohort | Antiviral Therapy | Atazanavir pharmacokinetics during pregnancy with and without tenofovir co-administration; confirms adequate drug exposure in PMTCT setting |
| [28459118](https://pubmed.ncbi.nlm.nih.gov/28459118/) | 2016 | Cohort | Journal of AIDS and Immune Research | Newborn hearing screening outcomes in HIV-exposed uninfected infants; safety monitoring data for in utero ATV exposure |
| [29859254](https://pubmed.ncbi.nlm.nih.gov/29859254/) | 2018 | In Vitro / Mechanistic | Reproductive Toxicology | ATV and RTV interactions with placental ABC efflux transporters (ABCB1, ABCG2, ABCC2); mechanistic data on transplacental drug transfer relevant to congenital HIV prevention |
| [34978889](https://pubmed.ncbi.nlm.nih.gov/34978889/) | 2022 | Basic Research | Antimicrobial Agents and Chemotherapy | Novel CNS-targeting HIV-1 protease inhibitors with enhanced blood-brain barrier penetration; builds on ATV-class scaffold for HIV-associated neurocognitive disorders (HAND) |
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | Cohort | AIDS Reviews | Gastrointestinal adverse events in HIV-treated and untreated patients; ATV tolerability context across HIV disease stages |
| [31595301](https://pubmed.ncbi.nlm.nih.gov/31595301/) | 2020 | Pharmacovigilance | Clinical Infectious Diseases | Pharmacovigilance database analysis of ART safety signals in pregnancy; provides the regulatory framework for safety monitoring in special populations |

---

## Singapore Market Information

Atazanavir is currently **not registered in Singapore**. There are no product licences on record with the Health Sciences Authority (HSA).

> **Note:** Atazanavir (Reyataz®) holds regulatory approval from the US FDA (2003), EMA, and Health Canada, among others. Its absence from the Singapore market represents a potential access gap for patients who could benefit from an ATV-based regimen, particularly in paediatric and pregnancy contexts where specific formulations have been purpose-developed.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Clinical note (from evidence context):** The literature included in this evidence pack highlights specific safety areas to review prior to use: in utero exposure and congenital anomaly risk (PHACS SMARTT cohort, European registry data), transplacental transfer via ABC transporters, and gastrointestinal tolerability. Drug interaction data with acid-reducing agents (which reduce ATV absorption) was flagged in one Phase 4 trial (NCT01232127) and should be reviewed carefully.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple large, completed Phase 3 RCTs provide robust L1-level evidence supporting Atazanavir's efficacy and safety across the HIV disease spectrum — including the pre-AIDS ARC stage and congenital/paediatric HIV infection — and the drug holds full regulatory approval in multiple major markets; the primary barrier to use in Singapore is the absence of local HSA registration rather than any evidentiary gap.

**To proceed, the following is needed:**

- **HSA registration pathway assessment:** Determine whether an abridged application (referencing US FDA / EMA approvals) is feasible under Singapore's regulatory framework for a drug with this level of global approval evidence
- **Mechanism of action and full safety data:** Retrieve the official Summary of Product Characteristics (SmPC) or US Prescribing Information (USPI) to complete the DG001/DG002 data gaps — particularly TFDA-equivalent warnings, contraindications, and CYP3A4/UGT1A1 drug interaction profile
- **Drug interaction review:** Atazanavir has known significant interactions with acid-suppressing agents (PPIs, H2-blockers), tenofovir, and numerous CYP3A4/UGT1A1 substrates; a formal DDI assessment is needed before any clinical deployment
- **Paediatric formulation access plan:** If congenital/paediatric HIV is the target population, confirm availability of the ATV powder formulation (for children <6 years) and the capsule (for children ≥6 years) within the Singapore supply chain
- **Pharmacovigilance plan:** Establish monitoring for hyperbilirubinaemia, nephrolithiasis, PR interval changes, and metabolic effects, per the established safety profile of the ATV class
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

