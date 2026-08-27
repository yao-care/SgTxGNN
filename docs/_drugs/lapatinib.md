---
layout: default
title: Lapatinib
parent: 僅模型預測 (L5)
nav_order: 572
evidence_level: L5
indication_count: 10
---

# Lapatinib
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

# Lapatinib: From HER2/EGFR-Targeted Therapy to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Lapatinib is characterized in this evidence pack as an EGFR/HER2 dual tyrosine kinase inhibitor (drug's official original indication and detailed mechanism-of-action fields are not available — flagged as data gaps).
The TxGNN model's top-ranked prediction is **Dermatofibrosarcoma Protuberans**, but this specific prediction currently has **zero supporting clinical trials and zero supporting literature**.
Across all 10 predicted indications in this evidence pack, only one — **Plasmodium falciparum malaria** (rank 8) — has any real supporting evidence (3 publications, including direct in vitro pharmacology data), while the remaining 9 candidates (mostly soft-tissue sarcomas and two parasitic diseases) have little to no independent support. **A blocking safety data gap (missing TFDA/HSA label warnings and contraindications) currently prevents any of these candidates from advancing past initial safety screening.**

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (drug not marketed in Singapore; `original_indications` empty — see Data Gaps) |
| Predicted New Indication (top-ranked) | Dermatofibrosarcoma Protuberans |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

**Note on this evidence pack:** This is a multi-indication candidate pack (`TW-DB01259-multi`) — TxGNN returned 10 ranked disease predictions for lapatinib. The table above reflects the rank-1 prediction as required by the report format, but it is *not* the best-supported candidate in the pack. See "Additional Predicted Indications" below for the full ranked set, including the one candidate (malaria, rank 8) with actual literature support.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for lapatinib is not available as a structured field in this evidence pack (flagged as data gap DG002, High severity). Based on the information that *is* present — repeated references within the model's own repurposing rationale — lapatinib is an **EGFR/HER2 dual tyrosine kinase inhibitor**. The drug's original approved indication could not be extracted from this evidence pack, as `original_indications` is empty and there are no Singapore/Taiwan regulatory licenses on file (market status: not marketed).

For the top-ranked prediction, **dermatofibrosarcoma protuberans (DFSP)**, the model's own rationale text explicitly flags this as a weak mechanistic match: DFSP is driven by a COL1A1-PDGFB fusion gene, and its standard targeted therapy is a PDGFR inhibitor (imatinib) — a pathway with no known overlap with lapatinib's EGFR/HER2 mechanism. No clinical or preclinical literature supports this specific link.

Notably, five of the ten predicted indications (dermatofibrosarcoma protuberans, conventional fibrosarcoma, kidney fibrosarcoma, heart fibrosarcoma, low-grade fibromyxoid sarcoma) form a tight score cluster (98.2%–99.3%) all within the soft-tissue sarcoma family, none of which is mechanistically linked to EGFR/HER2 signaling. The rationale for each of these explicitly attributes this clustering to **TxGNN's knowledge-graph embedding proximity** (diseases sitting near each other in the graph) rather than an independent pharmacological signal — this should be treated as a caution flag, not confirmatory evidence, when interpreting the sarcoma cluster as a group.

The one candidate with genuine supporting evidence is **Plasmodium falciparum malaria** (rank 8, L4/S1): a direct in vitro pharmacology study (PMID 32235391) found that lapatinib inhibits haemozoin formation in malaria parasites — an off-target antimalarial mechanism unrelated to its EGFR/HER2 activity, but experimentally confirmed rather than purely graph-predicted.

---

## Clinical Trial Evidence

Across all 10 predicted indications in this evidence pack, no clinical trials were found in ClinicalTrials.gov or ICTRP for lapatinib against any of these diseases (confirmed by 20 separate zero-result queries in the query log).

Currently no related clinical trials registered.

---

## Literature Evidence

Aggregated across all 10 predicted indications (5 publications found total; grouped by indication):

| Predicted Indication | PMID | Year | Type | Journal | Key Findings |
|---|------|-----|------|------|---------|
| Plasmodium falciparum malaria | [32235391](https://pubmed.ncbi.nlm.nih.gov/32235391/) | 2020 | In Vitro Pharmacology (direct) | Molecules | Lapatinib (with nilotinib and lomitapide) inhibits haemozoin (β-haematin) formation in malaria parasites — a validated antimalarial drug-repositioning screen finding, direct evidence of off-target antiparasitic activity. |
| Plasmodium falciparum malaria | [29301082](https://pubmed.ncbi.nlm.nih.gov/29301082/) | 2018 | Medicinal Chemistry/SAR (indirect) | ACS Infect Dis | Optimization of lapatinib-derived 4-anilinoquinoline analogs against *P. falciparum*; tests structural analogs, not lapatinib itself. |
| Plasmodium falciparum malaria | [25685309](https://pubmed.ncbi.nlm.nih.gov/25685309/) | 2015 | Medicinal Chemistry/SAR (indirect) | MedChemComm | Thienopyrimidine scaffolds derived from the lapatinib kinase-inhibitor chemotype evaluated against trypanosomiasis, leishmaniasis, and malaria; primary focus is trypanosomiasis, indirect relevance to malaria. |
| Fibroblastic neoplasm | [34239043](https://pubmed.ncbi.nlm.nih.gov/34239043/) | 2021 | Mechanistic/Preclinical | Oncogene | Describes a SNAI2-PEAK1-INHBA stromal axis that drives **lapatinib resistance** in HER2-positive breast cancer — evidence of a resistance mechanism, not of therapeutic benefit in fibroblastic neoplasms; direction is opposite to the indication hypothesis. |
| Lymphangiomyoma | [20979677](https://pubmed.ncbi.nlm.nih.gov/20979677/) | 2010 | Case Report | Respiratory Care | Case report of recurrent pneumothorax in a lymphangioleiomyomatosis (LAM) patient during **unrelated breast cancer chemotherapy** — not a lapatinib study and not evidence of efficacy in LAM. |

No literature is available for dermatofibrosarcoma protuberans, conventional fibrosarcoma, kidney fibrosarcoma, cysticercosis, heart fibrosarcoma, low-grade fibromyxoid sarcoma, or coenurosis.

---

## Singapore Market Information

Lapatinib is not currently marketed in Singapore — `taiwan_regulatory` reports 0 registered licenses. No market/authorization table is available.

---

## Cytotoxicity

Lapatinib is described within this evidence pack's rationale text as an EGFR/HER2-targeted agent used in the context of HER2-positive breast cancer (per literature reference PMID 34239043), and several of its predicted indications are oncologic. This section is included on that basis, though DrugBank category and toxicity data are not present in this evidence pack.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR/HER2 dual tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-drug interaction data are flagged in this evidence pack as a Blocking-severity data gap — DG001 — meaning safety pre-screening (S1) cannot currently be completed for any candidate indication until TFDA/HSA label data is obtained.)*

---

## Additional Predicted Indications in This Evidence Pack

All 10 candidates returned by TxGNN for lapatinib, ranked by prediction score:

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Supporting Literature |
|------|---------|-------------|-----------------|-----------------|------------------|------------------------|
| 1 | Dermatofibrosarcoma protuberans | 99.30% | L5 | S0 | Hold | None |
| 2 | Fibroblastic neoplasm | 98.43% | L5 | S0 | Hold | 1 (evidence of resistance, not efficacy) |
| 3 | Conventional fibrosarcoma | 98.36% | L5 | S0 | Hold | None |
| 4 | Kidney fibrosarcoma | 98.35% | L5 | S0 | Hold | None |
| 5 | Cysticercosis | 98.34% | L5 | S0 | Hold | None |
| 6 | Heart fibrosarcoma | 98.25% | L5 | S0 | Hold | None |
| 7 | Low grade fibromyxoid sarcoma | 98.23% | L5 | S0 | Hold | None |
| 8 | Plasmodium falciparum malaria | 98.02% | L4 | S1 | Research Question | 3 (1 direct in vitro, 2 indirect SAR) |
| 9 | Coenurosis | 97.46% | L5 | S0 | Hold | None |
| 10 | Lymphangiomyoma | 97.29% | L5 | S0 | Hold | 1 (unrelated case report) |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Nine of the ten predicted indications have no supporting clinical or literature evidence (L5, model-prediction-only), and the sarcoma cluster's high scores are flagged in the model's own rationale as likely reflecting knowledge-graph embedding proximity rather than an independent pharmacological signal. The one candidate with genuine experimental support — Plasmodium falciparum malaria — has only in vitro evidence (L4) and is best framed as a research question, not a repurposing candidate ready for clinical evaluation. Critically, a **blocking** data gap on TFDA/HSA safety labeling (warnings, contraindications) means no candidate in this pack can currently pass initial safety screening (S1) regardless of efficacy evidence strength.

**To proceed, the following is needed:**
- TFDA/HSA package insert data (key warnings, contraindications) — currently blocking (DG001)
- Structured mechanism-of-action data via DrugBank API — currently high-severity gap (DG002)
- If pursuing the malaria signal specifically: in vivo efficacy and pharmacokinetic data at antimalarial dosing, followed by safety assessment against the antimalarial (not oncology) dosing/exposure profile
- Drug-drug interaction data (current DDI query returned no results)
- Confirmation of original approved indication(s) and regulatory status, not present in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

