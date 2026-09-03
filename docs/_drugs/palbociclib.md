---
layout: default
title: Palbociclib
parent: 僅模型預測 (L5)
nav_order: 747
evidence_level: L5
indication_count: 10
---

# Palbociclib
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

# Palbociclib: From Breast Cancer to Myeloid Leukemia

## One-Sentence Summary

Palbociclib is a CDK4/6 (cyclin-dependent kinase 4/6) inhibitor originally developed for HR-positive, HER2-negative metastatic breast cancer. Among ten indications flagged by the TxGNN model, **myeloid leukemia** is the only candidate backed by substantive clinical and mechanistic evidence — **5 clinical trials** (including one completed Phase 1/2 study) and **20 publications** — and is the focus of this report. The remaining nine predictions carry a TxGNN score but essentially no supporting evidence and are summarized separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Breast cancer (HR+/HER2-negative, advanced/metastatic) — inferred from literature context in this evidence pack; not formally recorded, as the drug is not marketed in Singapore |
| Predicted New Indication | Myeloid leukemia (acute myeloid leukemia, AML) |
| TxGNN Prediction Score | 98.94% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is currently a data gap (flagged as High severity in this evidence pack). Based on information embedded in the accompanying literature, Palbociclib is a selective CDK4/6 inhibitor that blocks the CDK4/6–Rb (retinoblastoma protein) axis, arresting the G1-to-S phase transition of the cell cycle — the mechanism underlying its approval for HR+/HER2- breast cancer.

Breast cancer and myeloid leukemia are both malignancies driven by dysregulated cell-cycle progression, but the mechanistic link here is more specific than tissue-of-origin similarity: multiple preclinical studies show that CDK6 (rather than CDK4) is selectively overexpressed and required for proliferation in specific AML subtypes, including FLT3-ITD-mutated and MLL(KMT2A)-rearranged leukemias. This gives palbociclib a plausible, subtype-specific rationale distinct from its original oncology use.

Consistent with this, palbociclib has been studied in combination regimens (with venetoclax/azacitidine, decitabine, or sorafenib) to resensitize resistant AML cells to apoptosis, and one Phase 1/2 combination trial (CPX-351 + palbociclib) has already completed with a defined efficacy readout. This is meaningfully stronger and more direct evidence than any of the other nine TxGNN-flagged indications in this pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03844997](https://clinicaltrials.gov/study/NCT03844997) | Phase 1/2 | Completed | 35 | Palbociclib + CPX-351 in AML; evaluated safety/tolerability and overall response rate (CR/CRi by 2003 IWG criteria) |
| [NCT03132454](https://clinicaltrials.gov/study/NCT03132454) | Phase 1 | Active, not recruiting | 32 | Palbociclib alone and combined with sorafenib, decitabine, or dexamethasone in relapsed/refractory leukemia |
| [NCT02310243](https://clinicaltrials.gov/study/NCT02310243) | Phase 1b/2a | Unknown | 50 | Palbociclib in MLL-rearranged acute leukemias (AML and ALL); dose based on prior breast cancer regimen (125 mg/day, 21 days on/7 off) |
| [NCT05627232](https://clinicaltrials.gov/study/NCT05627232) | Phase 1 | Recruiting | 24 | Palbociclib pre-treatment followed by tazemetostat + CPX-351 in relapsed/refractory AML |
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | Terminated | 2 | Multi-drug precision-oncology platform trial (SMMART); terminated with minimal enrollment, low evidentiary value |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36076608](https://pubmed.ncbi.nlm.nih.gov/36076608/) | 2022 | Preclinical | Biomedicine & Pharmacotherapy | Palbociclib (CDK6 inhibitor) enhances antitumor activity of venetoclax + azacitidine in AML |
| [33068248](https://pubmed.ncbi.nlm.nih.gov/33068248/) | 2021 | Preclinical | Int J Hematology | CDK4/6 inhibition + autophagy inhibition synergistically induces apoptosis in t(8;21) AML cells |
| [27323399](https://pubmed.ncbi.nlm.nih.gov/27323399/) | 2016 | Preclinical (mechanistic) | Oncotarget | Identifies an FLT3-ITD → HCK → CDK6 signaling pathway; FLT3-ITD AML cells are CDK6-dependent, not CDK4-dependent |
| [38890447](https://pubmed.ncbi.nlm.nih.gov/38890447/) | 2024 | Preclinical | Leukemia | Combined menin and CDK6/FLT3 kinase inhibition is effective in NUP98-rearranged leukemia |
| [41468895](https://pubmed.ncbi.nlm.nih.gov/41468895/) | 2026 | Preclinical (patient samples + PDX) | Cell Reports Medicine | Venetoclax + palbociclib shows synergistic activity across 302 AML patient samples and PDX models, overcoming venetoclax resistance |
| [38430306](https://pubmed.ncbi.nlm.nih.gov/38430306/) | 2024 | Case Report | Cancer Chemotherapy and Pharmacology | Successful use of palbociclib + venetoclax + azacitidine in an adult with refractory/relapsed therapy-related AML |
| [36400926](https://pubmed.ncbi.nlm.nih.gov/36400926/) | 2023 | Review | Leukemia | Reviews cell-cycle and apoptosis-targeting strategies, including CDK inhibitors, to overcome AML chemoresistance |
| [29291023](https://pubmed.ncbi.nlm.nih.gov/29291023/) | 2017 | Preclinical | Oncotarget | Combined venetoclax and a CDK9/CDK4-6-class inhibitor (alvocidib) shows activity in AML |
| [34430715](https://pubmed.ncbi.nlm.nih.gov/34430715/) | 2021 | Preclinical (mouse xenograft) | Biochemistry and Biophysics Reports | In vivo confirmation that CDK4/6 + autophagy co-inhibition is effective in a t(8;21) AML xenograft model |
| [30381403](https://pubmed.ncbi.nlm.nih.gov/30381403/) | 2018 | Preclinical (genomic) | Blood Advances | Identifies recurrent CCND3 (cyclin D3, upstream of CDK4/6) mutations in MLL-rearranged AML |

---

## Singapore Market Information

Palbociclib is **not currently registered or marketed in Singapore** (0 authorizations on file in this evidence pack). No dosage form, brand, or approved-indication data is available locally.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective CDK4/6 inhibitor; not a conventional cytotoxic chemotherapeutic) |
| Myelosuppression Risk | High — the evidence pack literature explicitly reports palbociclib-induced myelosuppression as a class effect (PMID 39940918), and bone-marrow suppression is described as a common adverse event of CDK4/6 inhibitors (PMID 37994878) |
| Monitoring Items | Complete blood count with differential (neutropenia is the expected dose-limiting toxicity); pulmonary symptom monitoring given reported interstitial lung disease signals with this drug class (PMID 37994878) |
| Handling Protection | Oral antineoplastic agent — handle per institutional cytotoxic/hazardous drug handling policy |

---

## Other TxGNN-Predicted Indications (Screened)

The remaining nine TxGNN predictions in this evidence pack are **Hold**, evidence level **L5** (model prediction only):

| Indication | TxGNN Score | Why Screened Out |
|---|---|---|
| Rheumatoid arthritis (rank 2) | 99.36% | Evidence level L4, "Research Question" — one case report + preclinical mouse data suggest CDK6-driven synoviocyte proliferation may respond, but other literature shows CDK4/6i can also trigger autoimmune disease; direction is unresolved and no trials exist |
| Thrombotic disease | 99.32% | Literature is pharmacovigilance/FAERS data showing CDK4/6 inhibitors may **increase** thromboembolic risk — a safety signal, not a treatment signal; trials found are unrelated (oncology combination, withdrawn COVID trial) |
| Multiple endocrine neoplasia | 98.86% | All 25 "matching" trials are actually HR+/HER2- breast cancer studies — a likely entity-mapping artifact, not a genuine signal |
| Hyperthyroidism, resistance to thyroid hormone (THRB mutation), brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome, hyperthyroxinemia, Prinzmetal angina | 98.7–99.4% | Zero clinical trials, zero literature; no plausible mechanistic connection to CDK4/6 inhibition identified |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Myeloid leukemia is the only TxGNN-predicted indication in this pack supported by a coherent, subtype-specific mechanism (CDK6-dependence in FLT3-ITD and MLL-rearranged AML) plus a completed Phase 1/2 combination trial and consistent preclinical replication across multiple independent labs. Evidence is real but still early-phase and combination-based, not a standalone confirmed efficacy signal.

**To proceed, the following is needed:**
- Palbociclib MOA and DrugBank profile data (currently a High-severity data gap, DG002)
- TFDA/regulatory label warnings and contraindications (currently Blocking, DG001) — required before any S1 safety screening
- Outcome/results data from the completed NCT03844997 (CPX-351 + palbociclib) trial, not yet reflected in this evidence pack
- Clarification of the AML molecular subgroup(s) most likely to respond (FLT3-ITD, MLL-rearranged, t(8;21)) to scope a repurposing indication precisely, since "myeloid leukemia" as a whole is broader than the supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

