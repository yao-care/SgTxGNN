---
layout: default
title: Doravirine
parent: 僅模型預測 (L5)
nav_order: 343
evidence_level: L5
indication_count: 10
---

# Doravirine
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

# Doravirine: From HIV-1 Infection (Adults) to Congenital Human Immunodeficiency Virus

## One-Sentence Summary

Doravirine (MK-1439) is a Non-Nucleoside Reverse Transcriptase Inhibitor (NNRTI) approved for adult HIV-1 treatment in multiple countries, though it has not yet been registered in Singapore.
TxGNN predicts potential applicability across several HIV-related indications; among the 10 top-ranked predictions, **congenital human immunodeficiency virus** (vertically transmitted HIV-1 infection) carries the strongest mechanistic rationale and is supported by **5 clinical trials**, including two completed Phase 3 adult RCTs and one pregnancy pharmacokinetic study.
The majority of other top-ranked predictions — feline AIDS, neurodevelopmental disorders, and prostatic tumors — lack biological plausibility and are most likely knowledge graph artifacts rather than genuine repurposing candidates.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection in adults (inferred from clinical trial context; no Singapore regulatory data available) |
| Predicted New Indication | Congenital Human Immunodeficiency Virus (Rank 5, best-evidenced human indication) |
| TxGNN Prediction Score | 98.75% |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Doravirine is an NNRTI that selectively inhibits HIV-1 reverse transcriptase by binding to a non-substrate allosteric pocket, thereby blocking both RNA-dependent and DNA-dependent DNA polymerase activity. Two completed Phase 3 trials (NCT02397096 DRIVE-SHIFT; NCT02275780 DRIVE-AHEAD) have established its safety and virological efficacy in both treatment-naïve and virologically suppressed adult HIV-1 patients.

Congenital HIV arises from vertical mother-to-child transmission of HIV-1 — the identical pathogen and the identical viral target (HIV-1 reverse transcriptase) are involved. The NNRTI mechanism of action is therefore directly applicable regardless of transmission route. Prevention of mother-to-child transmission (PMTCT) is a WHO global health priority, and existing antiretrovirals proven in adults are routinely evaluated for this purpose.

A key gap — whether Doravirine achieves adequate plasma concentrations during pregnancy — is directly addressed by NCT04518228, a completed study (N=205) characterising pharmacokinetics of antiretroviral drugs in pregnant and postpartum women. The remaining critical gap is the absence of any dedicated pediatric or neonatal PK/PD and safety data for Doravirine, which would be required before formal extension of the indication to congenital/neonatal HIV management.

---

## All Predicted Indications — Summary

| Rank | Indication | TxGNN Score | Evidence Level | Decision |
|------|-----------|-------------|---------------|---------|
| 1 | Feline acquired immunodeficiency syndrome | 99.93% | L5 | **Hold** — veterinary indication; FIV RT is structurally divergent from HIV-1 RT and largely resistant to NNRTI |
| 2 | Simian immunodeficiency virus infection | 99.93% | L5 | **Hold** — SIV RT shows high resistance to most NNRTI; supporting literature (PMID 31658118) concerns islatravir, not Doravirine |
| 3 | Neurodevelopmental disorder with ataxic gait, absent speech, decreased cortical white matter | 99.91% | L5 | **Hold** — rare genetic disorder (e.g. ADAR1 mutation); no known link to HIV-1 RT mechanism |
| 4 | Fibroma of prostate | 98.76% | L5 | **Hold** — benign stromal tumour; no viral or RT-related aetiology; likely KG path artefact |
| **5** | **Congenital human immunodeficiency virus** | **98.75%** | **L2** | **Research Question** ✓ |
| 6 | AIDS related complex | 98.75% | L3 | **Research Question** ✓ |
| 7 | Brenner tumor | 98.75% | L5 | **Hold** — ovarian transitional cell tumour; no NNRTI mechanism link; likely KG cluster artefact |
| 8 | Benign reproductive system neoplasm | 98.70% | L5 | **Hold** — broad category; no viral or RT aetiology |
| 9 | Benign prostate phyllodes tumor | 98.63% | L5 | **Hold** — rare mesenchymal-epithelial tumour; no known NNRTI antifibrotic or antitumour activity |
| 10 | Male reproductive organ cancer | 98.46% | L5 | **Hold** — hormone/genetic aetiology; Doravirine has no antitumour evidence |

> **Note on high scores for non-HIV indications:** TxGNN scores for Ranks 1–4 and 7–10 are likely inflated by strong HIV ↔ immune-deficiency and reproductive-system node clustering within the knowledge graph, not by genuine biological relationships.

---

## Clinical Trial Evidence

*(Primary focus: Congenital Human Immunodeficiency Virus, Rank 5)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT04518228](https://clinicaltrials.gov/study/NCT04518228) | N/A | Completed | 205 | Evaluates PK of Doravirine and other ARVs during pregnancy and postpartum — directly addresses PMTCT feasibility and foetal/neonatal exposure profile |
| [NCT02397096](https://clinicaltrials.gov/study/NCT02397096) | Phase 3 | Completed | 673 | DRIVE-SHIFT: Switch to Doravirine/Lamivudine/TDF in virologically suppressed adults — establishes non-inferiority and safety as the mechanistic foundation for HIV-1 RT inhibition |
| [NCT02275780](https://clinicaltrials.gov/study/NCT02275780) | Phase 3 | Completed | 769 | DRIVE-AHEAD: Doravirine vs Darunavir/ritonavir in treatment-naïve HIV-1 adults — foundational Phase 3 efficacy and tolerability data |
| [NCT02652260](https://clinicaltrials.gov/study/NCT02652260) | Phase 2 | Completed | 86 | CNS toxicity switch study (ATRIPLA → Doravirine/Lamivudine/TDF) — characterises CNS safety profile, relevant to congenital HIV with neurological involvement |
| [NCT07412977](https://clinicaltrials.gov/study/NCT07412977) | N/A | Not Yet Recruiting | 5,160 | VIROPREG French prospective cohort on viral infections during pregnancy (HIV, HBV, HCV, arboviruses) — will provide long-term real-world maternal and child safety data |

---

## Literature Evidence

*(For AIDS Related Complex, Rank 6 — only indication with available literature)*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34459470](https://pubmed.ncbi.nlm.nih.gov/34459470/) | 2021 | Review | *Current Opinion in HIV and AIDS* | Reviews DDI landscape in the contemporary ART era; highlights that newer agents such as Doravirine carry a lower DDI burden due to favourable PK profiles — directly relevant to managing ARC patients who often require polypharmacy |

Currently no direct literature on Doravirine for congenital HIV is available.

---

## Singapore Market Information

Doravirine is currently not registered in Singapore. There are no active product licences on record. Any future introduction would require a full HSA new drug application.

---

## Safety Considerations

Please refer to the package insert for safety information. Package insert warnings and contraindications are not available in this Evidence Pack (flagged as a Blocking data gap requiring TFDA/HSA monograph retrieval). No drug-drug interaction records were identified in the current database query.

---

## Conclusion and Next Steps

**Decision: Research Question (Congenital HIV, AIDS Related Complex) / Hold (all other indications)**

**Rationale:**
Doravirine's HIV-1 RT inhibition mechanism is directly applicable to congenital HIV, which is caused by the same pathogen via vertical transmission. Two completed Phase 3 adult RCTs establish the clinical efficacy foundation, and a completed pregnancy PK study (NCT04518228) provides critical PMTCT-relevant pharmacokinetic data. AIDS related complex, as a defined pre-AIDS stage of HIV-1 disease progression, is similarly supported by the same mechanistic and clinical evidence base. Neither indication yet has dedicated paediatric or ARC-specific endpoint data.

**To proceed, the following is needed:**

- **Blocking:** Retrieve and review Doravirine package insert (HSA/FDA) for full warning, contraindication, and DDI profile before any clinical decision
- **High priority:** Obtain mechanism of action data from DrugBank (DB12301) to complete mechanistic rationale analysis
- **Congenital HIV:** Commission or identify paediatric/neonatal PK/PD studies; analyse NCT04518228 results for specific PMTCT endpoint data
- **AIDS Related Complex:** Define ARC-specific clinical endpoints and confirm coverage by existing adult HIV Phase 3 data
- **Singapore pathway:** Assess HSA registration strategy for Doravirine as a new NNRTI entry, given current zero-licence status
- **Hold decisions:** Do not invest further resources in Ranks 1–4 and 7–10 without new mechanistic evidence contradicting the current assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

