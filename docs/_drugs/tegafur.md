---
layout: default
title: Tegafur
parent: 僅模型預測 (L5)
nav_order: 949
evidence_level: L5
indication_count: 10
---

# Tegafur
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

# Tegafur: From Gastrointestinal Cancer to Colonic Neoplasm

## One-Sentence Summary

Tegafur is an oral prodrug of 5-fluorouracil (5-FU), historically used as a component of combination fluoropyrimidine chemotherapy (UFT, S-1) for gastrointestinal cancers. The TxGNN model predicts it may be effective for **Colonic Neoplasm**, and this is strongly supported by **30 clinical trials** (including multiple completed Phase 3 RCTs) and **22 publications** — though the underlying evidence indicates this is largely a **re-confirmation of an already-established standard indication** rather than a novel repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore; internationally, Tegafur (as UFT/S-1 combinations) is an established chemotherapy for gastric and colorectal cancer |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Tegafur is an orally administered prodrug of 5-fluorouracil (5-FU). It is metabolized by hepatic CYP2A6 into active 5-FU, which inhibits thymidylate synthase and thereby blocks DNA synthesis in rapidly dividing cells. This antimetabolite mechanism is the pharmacological backbone of fluoropyrimidine-based chemotherapy regimens (UFT, S-1/TS-1) that are already standard-of-care for colorectal cancer, particularly in Japan and across Asia.

Because of this, the relationship between Tegafur and colonic neoplasm is not a speculative new hypothesis — it reflects an existing, well-validated clinical use. Multiple completed Phase 3 randomized controlled trials (e.g., NSABP C-06, ACTS-CC 02, JFMC33-0502, NSAS-CC) have already established Tegafur-based regimens (UFT ± leucovorin, S-1 ± oxaliplatin) as effective adjuvant and metastatic-setting treatments for colon and colorectal cancer. The TxGNN prediction therefore should be interpreted as validating known pharmacology rather than surfacing a genuinely novel indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | SALTO study: S-1 vs capecitabine as first-line therapy in metastatic colorectal cancer |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1,535 | UFT+leucovorin vs TS-1 as adjuvant therapy for Stage III colon cancer, with gene-expression predictive factor analysis |
| [NCT00392899](https://clinicaltrials.gov/study/NCT00392899) | Phase 3 | Completed | 2,025 | Adjuvant UFT vs observation alone in curatively resected Stage II colon cancer |
| [NCT00152230](https://clinicaltrials.gov/study/NCT00152230) | Phase 3 | Completed | 900 | NSAS-CC: postoperative adjuvant UFT vs surgery alone in Dukes C colorectal cancer |
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Phase 3 | Completed | 1,608 | Oral UFT+LV vs IV 5-FU+LV in Stage II/III colon carcinoma |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown (ongoing/registered) | 1,191 | SOX (S-1+oxaliplatin) vs XELOX as adjuvant chemotherapy for Stage III colorectal cancer |
| [NCT00209742](https://clinicaltrials.gov/study/NCT00209742) | Phase 3 | Unknown | 340 | Postoperative UFT+LV vs UFT+LV+PSK regimens for Stage III colorectal cancer |
| [NCT00497107](https://clinicaltrials.gov/study/NCT00497107) | Phase 3 | Unknown | 300 | UFT/LV vs UFT/LV+PSK as postoperative adjuvant therapy for Stage IIIa/IIIb colorectal cancer |
| [NCT00905047](https://clinicaltrials.gov/study/NCT00905047) | Phase 3 | Completed | 89 | Crossover comparison of capecitabine vs UFT+folinic acid in advanced/metastatic colorectal cancer |
| [NCT05266300](https://clinicaltrials.gov/study/NCT05266300) | N/A | Completed | 722 | Clinical implementation of DPYD-genotyping to guide safe fluoropyrimidine (incl. tegafur) dosing |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clinical Colorectal Cancer | ACTS-CC 02: S-1+oxaliplatin vs UFT/LV as postoperative adjuvant therapy in high-risk Stage III colon cancer |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT | ESMO Open | Updated 5-year overall survival and subgroup analysis of ACTS-CC 02 trial |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | RCT / Meta-analysis | Medicine | Nationwide cohort study + meta-analysis: uracil-tegafur vs fluorouracil as adjuvant therapy in Stage II/III colon cancer |
| [16648506](https://pubmed.ncbi.nlm.nih.gov/16648506/) | 2006 | RCT | Journal of Clinical Oncology | NSABP C-06: oral UFT+LV non-inferior to IV 5-FU+LV in Stage II/III colon carcinoma |
| [6402917](https://pubmed.ncbi.nlm.nih.gov/6402917/) | 1983 | RCT | American Journal of Clinical Oncology | Oral tegafur vs IV 5-FU comparative efficacy/toxicity in metastatic colorectal cancer |
| [26347106](https://pubmed.ncbi.nlm.nih.gov/26347106/) | 2015 | RCT | Annals of Oncology | JFMC33-0502: optimal treatment duration for UFT/LV adjuvant therapy in Stage IIB/III colon cancer |
| [35168560](https://pubmed.ncbi.nlm.nih.gov/35168560/) | 2022 | Prospective Observational | BMC Cancer | JFMC46-1201: UFT/LV efficacy in high-risk Stage II colon cancer using propensity score matching |
| [38833114](https://pubmed.ncbi.nlm.nih.gov/38833114/) | 2024 | Prospective Observational (final analysis) | International Journal of Clinical Oncology | JFMC46-1201 final analysis: updated 5-year OS for UFT/LV in high-risk Stage II colon cancer |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surgery Today | UFT postoperative adjuvant chemotherapy for solid tumors: clinical evidence, mechanism, future direction |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Review/Guideline | Clinical Colorectal Cancer | Asian consensus adaptation of international guidelines for metastatic colorectal cancer |

---

## Singapore Market Information

Tegafur currently holds **no marketing authorization in Singapore** (0 registrations, market status: Not Marketed). No local product, dosage form, or approved indication text is available in the evidence pack.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Fluoropyrimidine class, 5-FU prodrug) |
| Myelosuppression Risk | Moderate — hematological toxicity (including a documented case of UFT-induced haemolytic anaemia) is reported; myelosuppression is a known class effect of fluoropyrimidines |
| Emetogenicity Classification | Low to moderate (typical of oral fluoropyrimidines) |
| Monitoring Items | CBC with differential, liver and renal function; DPD (dihydropyrimidine dehydrogenase) status/genotype screening is specifically relevant given documented toxicity risk in DPD-deficient patients |
| Handling Protection | Must follow institutional cytotoxic drug handling regulations, despite oral route of administration |

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were available in the evidence pack (all flagged as data gaps). Notably, clinical evidence (NCT05266300) highlights DPYD genotyping as a relevant pre-treatment safety consideration for fluoropyrimidines including tegafur.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs and consistent literature confirm Tegafur-based regimens are effective in colorectal/colon cancer, satisfying L1 evidence criteria. However, this predicted indication substantially overlaps with an already-established standard use rather than representing a novel repurposing opportunity, and the drug is currently unregistered in Singapore with no local safety labeling.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent package insert warnings and contraindications (currently a Blocking data gap)
- Formal mechanism-of-action documentation for the regulatory dossier (currently a High-severity data gap)
- Confirmation of intended Singapore registration pathway, since the drug has zero current local licenses
- A DPD-deficiency screening protocol prior to treatment initiation, given documented toxicity risk in fluoropyrimidine therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

