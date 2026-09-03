---
layout: default
title: Oteracil
parent: 僅模型預測 (L5)
nav_order: 739
evidence_level: L5
indication_count: 10
---

# Oteracil
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

# Oteracil: From Gastric Cancer to Colonic Neoplasm

## One-Sentence Summary

Oteracil is a component of the S-1 combination (tegafur + gimeracil + oteracil), a fluoropyrimidine-based regimen historically established for gastric cancer treatment. The TxGNN model predicts it may be effective for **Colonic Neoplasm**, with **8 clinical trials** and substantial published literature currently supporting this direction. However, Singapore-specific regulatory and safety data (package insert, HSA licensing) remain unavailable, so this candidate requires safety data completion before further action.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric cancer (as component of S-1 combination; no Singapore license data available) |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data for oteracil is not available in DrugBank (data gap). Based on known pharmacology, oteracil (potassium oxonate) is an OPRT (orotate phosphoribosyltransferase) inhibitor that distributes selectively to gastrointestinal mucosa, where it suppresses local activation of 5-FU to reduce gut toxicity such as diarrhea and mucositis. It functions as the biochemical modulator in the fixed-dose combination S-1 (tegafur + gimeracil + oteracil); oteracil itself has no independent antitumor activity — its clinical role is to widen the systemic therapeutic window of tegafur, a 5-FU prodrug.

Gastric cancer and colonic neoplasm are both gastrointestinal malignancies that respond to fluoropyrimidine-based chemotherapy through the same 5-FU/thymidylate synthase inhibition pathway. In fact, the S-1 combination is already an approved standard/adjuvant chemotherapy for colorectal cancer in Japan and several other markets, which directly supports the mechanistic plausibility of the TxGNN model's prediction — the evidence for colonic neoplasm effectively derives from the S-1 combination as a whole rather than from oteracil as an isolated agent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown | 1,191 | SOX (S-1 + Oxaliplatin) vs. XELOX as adjuvant chemotherapy for Stage III colorectal cancer |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | SALTO trial: S-1 vs. Capecitabine as first-line treatment for metastatic colorectal cancer |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1,535 | UFT+Leucovorin vs. TS-1 (contains oteracil) as adjuvant treatment for Stage III colon cancer |
| [NCT00524706](https://clinicaltrials.gov/study/NCT00524706) | Phase 1/2 | Unknown | 42 | S-1 + Leucovorin + Oxaliplatin (SOL) in untreated metastatic colorectal cancer |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | Terminated | 20 | S-1 vs. Capecitabine+Oxaliplatin, coronary artery blood flow (cardiac safety) in metastatic GI adenocarcinoma |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | Unknown | 40 | S-1 + Bevacizumab in unresectable/recurrent colorectal cancer after prior chemotherapy failure |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | Unknown | 82 | Raltitrexed + S-1 in metastatic colorectal cancer after standard chemotherapy failure |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | Not yet recruiting | 52 | Fuquintinib + tegafur/gimeracil/oteracil, third-line treatment for advanced metastatic CRC |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Colorectal Cancer | ACTS-CC 02: SOX superior to UFT/LV as postoperative adjuvant therapy in high-risk Stage III colon cancer |
| [27056996](https://pubmed.ncbi.nlm.nih.gov/27056996/) | 2016 | RCT | Ann Oncol | ACTS-RC: Phase 3 trial comparing S-1 vs. UFT as adjuvant chemotherapy for Stage II/III rectal cancer |
| [24942277](https://pubmed.ncbi.nlm.nih.gov/24942277/) | 2014 | RCT | Ann Oncol | ACTS-CC trial: S-1 non-inferior to UFT/LV as adjuvant chemotherapy for Stage III colon cancer |
| [32189156](https://pubmed.ncbi.nlm.nih.gov/32189156/) | 2020 | RCT | Int J Clin Oncol | KSCC1303: S-1 + Oxaliplatin (C-SOX) feasibility and 3-year disease-free survival in Stage III colon cancer |
| [26036466](https://pubmed.ncbi.nlm.nih.gov/26036466/) | 2015 | RCT | BMC Cancer | Randomized Phase 2 study of S-1 dosing schedule for resected colorectal cancer |
| [22415232](https://pubmed.ncbi.nlm.nih.gov/22415232/) | 2012 | RCT | Br J Cancer | ACTS-CC trial safety analysis of UFT/LV vs. S-1 as adjuvant therapy for Stage III colon cancer |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Review | Clin Colorectal Cancer | Asian consensus adapting international guidelines for metastatic colorectal cancer |
| [10897209](https://pubmed.ncbi.nlm.nih.gov/10897209/) | 2000 | Review | Gan To Kagaku Ryoho | Conceptual review of biochemical modulation of 5-FU underlying S-1 design |
| [26976971](https://pubmed.ncbi.nlm.nih.gov/26976971/) | 2016 | Cohort | Anticancer Res | Genome-wide DNA copy-number biomarker analysis within the ACTS-CC adjuvant trial for Stage III colon cancer |
| [23320901](https://pubmed.ncbi.nlm.nih.gov/23320901/) | 2013 | RCT (protocol) | Trials | Study protocol for RCT evaluating optimal S-1 adjuvant chemotherapy schedule in Stage III colon cancer |

---

## Singapore Market Information

Oteracil/S-1 currently has no marketing authorization on record in Singapore (0 registrations). No license or approved-indication data is available for this evaluation.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine class), delivered via the S-1 combination; oteracil itself is a biochemical modulator (OPRT inhibitor) with no independent cytotoxic activity |
| Myelosuppression Risk | Low–Moderate — oteracil's mucosal-protective action mitigates GI toxicity from tegafur/5-FU; case reports document hand-foot syndrome and hypertriglyceridemia rather than a strong myelosuppression signal |
| Emetogenicity Classification | Low to Moderate (typical of oral fluoropyrimidines such as S-1) |
| Monitoring Items | CBC with differential, liver and renal function, triglycerides, skin/mucosal toxicity assessment |
| Handling Protection | Yes — must follow cytotoxic drug handling protocols as a component of the S-1 chemotherapy regimen |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs (e.g., ACTS-CC, ACTS-CC 02, ACTS-RC, SALTO) support the efficacy of S-1-based regimens containing oteracil in colorectal/colon cancer, giving an L1 evidence level. However, oteracil has no Singapore marketing authorization and no available safety/package-insert data, so guardrails are required before proceeding.

**To proceed, the following is needed:**
- HSA-equivalent package insert warnings, contraindications, and drug interaction data (currently a blocking data gap)
- Confirmed drug-specific mechanism of action (DrugBank MOA data, currently unavailable)
- Confirmation of Singapore market/registration pathway for S-1 or oteracil-containing products
- A dedicated safety monitoring plan given absence of local labeling data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

