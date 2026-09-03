---
layout: default
title: Uracil
parent: 僅模型預測 (L5)
nav_order: 1033
evidence_level: L5
indication_count: 10
---

# Uracil
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

# Uracil: From Fluoropyrimidine-Enhancing Component to Colonic Neoplasm

## One-Sentence Summary

Uracil (DrugBank DB03419) has no independently registered indication in Singapore; it is best known as the pyrimidine component of the tegafur-uracil (UFT) oral combination chemotherapy used against gastrointestinal cancers.
The TxGNN model predicts it may be effective for **Colonic Neoplasm**, and this is strongly corroborated by real-world evidence — the UFT combination itself has already been tested and used clinically in colon cancer for over two decades.
Support currently includes **47 clinical trials** and **20 publications**, several of which are Phase 3 RCTs studying the drug (as UFT) directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not independently documented for Uracil; historically used as the DPD-modulating component of tegafur-uracil (UFT), a fluoropyrimidine combination for gastrointestinal cancers |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Uracil is not available in the evidence pack. Based on known pharmacology reflected in the supporting literature (e.g., PMID 26722024), uracil is part of the tegafur-uracil (UFT) combination: it competitively inhibits dihydropyrimidine dehydrogenase (DPD), the enzyme that degrades 5-fluorouracil, thereby prolonging the exposure and cytotoxic activity of the 5-FU generated from tegafur within tumour tissue.

This DPD-modulating role is not a new concept for gastrointestinal malignancy — UFT has an established, decades-long track record as an oral fluoropyrimidine regimen for colorectal and gastric cancer. Multiple randomized controlled trials (e.g., NSABP C-06, ACTS-CC 02, JFMC46-1201) have directly evaluated UFT plus leucovorin against standard IV 5-FU/LV or other fluoropyrimidine backbones specifically in colon cancer.

Because uracil's mechanistic contribution (5-FU potentiation via DPD inhibition) is disease-agnostic across the GI tract, and because colon cancer already shares the same fluoropyrimidine-based standard-of-care backbone used in UFT trials, the TxGNN prediction for "colonic neoplasm" is highly consistent with existing pharmacological and clinical practice — this is less a *novel* repurposing signal and more a *confirmation* of an indication the combination product already occupies in several markets.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Phase 3 | Completed | 1,608 | Direct trial of oral uracil/tegafur (UFT) plus leucovorin vs. IV 5-FU plus leucovorin in resected Stage II/III colon cancer |
| [NCT01228734](https://clinicaltrials.gov/study/NCT01228734) | Phase 3 | Completed | 553 | Cetuximab + FOLFOX-4 vs. FOLFOX-4 alone in first-line RAS wild-type metastatic colorectal cancer (Chinese subjects) |
| [NCT00227747](https://clinicaltrials.gov/study/NCT00227747) | Phase 3 | Completed | 598 | Preoperative chemoradiation regimens (capecitabine ± oxaliplatin) in resectable rectal carcinoma |
| [NCT00952029](https://clinicaltrials.gov/study/NCT00952029) | Phase 2/3 | Completed | 492 | FOLFIRI + bevacizumab with/without bevacizumab maintenance in non-pretreated metastatic colorectal cancer |
| [NCT02251977](https://clinicaltrials.gov/study/NCT02251977) | Phase 3 | Completed | 196 | GM1 for prevention of oxaliplatin-induced neurotoxicity during adjuvant chemotherapy in colorectal cancer |
| [NCT00484939](https://clinicaltrials.gov/study/NCT00484939) | Phase 3 | Completed | 280 | Bevacizumab + capecitabine vs. capecitabine alone in elderly first-line metastatic colorectal cancer |
| [NCT04607421](https://clinicaltrials.gov/study/NCT04607421) | Phase 3 | Active, not recruiting | 831 | Encorafenib + cetuximab ± chemotherapy vs. standard of care in BRAF V600E-mutant metastatic colorectal cancer |
| [NCT05253651](https://clinicaltrials.gov/study/NCT05253651) | Phase 3 | Recruiting | 400 | Tucatinib + trastuzumab + mFOLFOX6 vs. mFOLFOX6-based regimens in HER2+ metastatic colorectal cancer |
| [NCT05239741](https://clinicaltrials.gov/study/NCT05239741) | Phase 3 | Recruiting | 100 | Pembrolizumab vs. standard chemotherapy in MSI-H/dMMR Stage IV colorectal cancer (Chinese participants) |
| [NCT05863195](https://clinicaltrials.gov/study/NCT05863195) | Phase 3 | Recruiting | 408 | Hepatic arterial infusion + systemic therapy vs. systemic therapy alone for unresectable colorectal liver metastases |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16648506](https://pubmed.ncbi.nlm.nih.gov/16648506/) | 2006 | RCT | J Clin Oncol | NSABP C-06: oral UFT + leucovorin non-inferior to IV 5-FU + leucovorin in Stage II/III colon cancer |
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Colorectal Cancer | ACTS-CC 02 Phase III: S-1+oxaliplatin (SOX) vs. tegafur-uracil+leucovorin (UFT/LV) as adjuvant therapy in high-risk Stage III colon cancer |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT (updated survival) | ESMO Open | ACTS-CC 02 5-year survival update: SOX not superior to UFT/LV as adjuvant chemotherapy |
| [38833114](https://pubmed.ncbi.nlm.nih.gov/38833114/) | 2024 | Prospective controlled trial (final analysis) | Int J Clin Oncol | JFMC46-1201: UFT/LV improves disease-free survival vs. surgery alone in high-risk Stage II colon cancer |
| [35168560](https://pubmed.ncbi.nlm.nih.gov/35168560/) | 2022 | Prospective observational study | BMC Cancer | JFMC46-1201 interim analysis supporting UFT/LV benefit in high-risk Stage II colon cancer |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | Cohort study / meta-analysis | Medicine | Nationwide Taiwan cohort: UFT vs. 5-FU as postoperative adjuvant chemotherapy in Stage II/III colon cancer, comparable DFS/OS |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | RCT | Int J Clin Oncol | Adjuvant immunochemotherapy combining OK-432 with oral pyrimidines (including UFT) in colorectal cancer |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surgery Today | Clinical evidence and mechanism of action of UFT (tegafur+uracil) as adjuvant therapy in colorectal, gastric, lung and breast cancer |
| [26722024](https://pubmed.ncbi.nlm.nih.gov/26722024/) | 2016 | Review | Anticancer Research | Review of oral fluoropyrimidines (S-1, UFT, capecitabine) and DPD-inhibition strategy to enhance 5-FU efficacy in colon cancer |
| [11320674](https://pubmed.ncbi.nlm.nih.gov/11320674/) | 2001 | Case report | Cancer Chemother Pharmacol | UFT-induced haemolytic anaemia in a patient treated for metastatic colon cancer |

---

## Singapore Market Information

Uracil is not currently registered in Singapore (0 licenses on file; market status: **Not Marketed**). No HSA product authorization data is available for either uracil monotherapy or a UFT-type combination product under this DrugBank entry.

---

## Cytotoxicity

Uracil is assessed as antineoplastic-adjacent because it is a core component of the fluoropyrimidine-class combination chemotherapy tegafur-uracil (UFT), used across the retrieved evidence exclusively in cancer treatment regimens.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Fluoropyrimidine class — DPD-inhibiting enhancer within the UFT combination) |
| Myelosuppression Risk | Medium — literature describes UFT as having a comparatively mild toxicity profile relative to IV 5-FU (PMID 17952521), but case reports document haematological adverse events including haemolytic anaemia (PMID 11320674) |
| Emetogenicity Classification | Low to Moderate — consistent with oral fluoropyrimidine regimens |
| Monitoring Items | CBC with differential, liver and renal function, signs of haemolysis; DPD deficiency screening is advisable given fluoropyrimidine-class toxicity risk |
| Handling Protection | Standard cytotoxic drug handling precautions apply as part of a fluoropyrimidine combination regimen, despite oral route of administration |

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were retrievable for this candidate in the current evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence quality is high (L1) — the tegafur-uracil combination that uracil is part of has multiple completed Phase 3 RCTs directly demonstrating efficacy in colon cancer, and this indication is already established clinical practice in several markets. However, uracil has zero Singapore registrations and a Blocking-severity data gap on safety labeling, so this cannot proceed to clinical use without closing that gap.

**To proceed, the following is needed:**
- Obtain and parse the HSA (or equivalent regulatory) package insert / product label for tegafur-uracil (UFT) to resolve the Blocking safety data gap (DG001)
- Confirm mechanism of action (DG002) directly from DrugBank API rather than inferred literature to finalize the mechanistic rationale
- Establish a formal drug-drug interaction profile, particularly with other DPD-pathway-affecting agents (e.g., other fluoropyrimidines, DPD inhibitors)
- If clinical development is pursued in Singapore, initiate a registration pathway assessment with HSA given the current "Not Marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

