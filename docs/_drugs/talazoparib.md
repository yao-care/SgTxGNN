---
layout: default
title: Talazoparib
parent: 僅模型預測 (L5)
nav_order: 942
evidence_level: L5
indication_count: 10
---

# Talazoparib
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

# Talazoparib: From BRCA-Mutated HER2-Negative Breast Cancer to HER2-Positive Breast Carcinoma

## One-Sentence Summary

> Talazoparib is a PARP inhibitor globally approved for germline BRCA1/2-mutated, **HER2-negative** locally advanced or metastatic breast cancer (EMBRACA trial).
> The TxGNN model's top-ranked prediction is **HER2-Positive Breast Carcinoma**, but nearly all of the **10 clinical trials** and **13 publications** cited under this label actually describe HER2-negative/BRCA-mutated populations — a strong signal that this is a knowledge-graph disease-label mapping artifact rather than a genuine new-indication finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Singapore-specific label on file (0 licenses). Globally approved for germline BRCA1/2-mutated, HER2-negative locally advanced/metastatic breast cancer |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 98.98% |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed structured MOA data is not available in DrugBank for this record (Data Gap DG002). Based on information present elsewhere in the evidence pack, Talazoparib is an oral PARP (poly-ADP ribose polymerase) inhibitor that exploits **synthetic lethality** in tumors with homologous-recombination deficiency, most notably germline BRCA1/2-mutated tumors. It is globally approved (EMBRACA Phase 3 trial, NCT01945775) specifically for **HER2-negative** advanced/metastatic breast cancer.

The rank-1 predicted indication in this pack, "HER2 positive breast carcinoma," is the opposite of the drug's known approved population. Critically, when we examine the supporting evidence attached to this exact prediction, the trials and literature almost uniformly describe **HER2-negative or triple-negative** breast cancer populations (e.g., NCT03499353 "early HER2-negative breast cancer," NCT04134884 "HER2-negative metastatic breast cancer," NCT03911973 "HER2 negative breast cancers"). No trial in the list specifically enrolls or targets HER2-positive disease. This mismatch strongly suggests a **knowledge-graph/disease-node mapping error** (HER2 status inverted) rather than a pharmacologically plausible new signal.

A more mechanistically consistent candidate exists within the same evidence pack: rank 3, "progesterone-receptor negative breast cancer" (Evidence Level L2, decision stage S2, "Proceed with Guardrails"). PR-negative breast cancer overlaps heavily with the triple-negative/BRCA-mutated population that is Talazoparib's core validated mechanism, and is supported by the Phase 3 EMBRACA trial itself plus 26 related clinical trials. This candidate should be treated as the primary evidence-backed repurposing signal from this pack, while the HER2-positive label should be flagged for data-quality review before any further action.

---

## Clinical Trial Evidence
*(Trials attached to the rank-1 prediction, "HER2 positive breast carcinoma" — note none actually enroll HER2-positive patients)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03499353](https://clinicaltrials.gov/study/NCT03499353) | Phase 2 | Terminated | 61 | Neoadjuvant talazoparib in gBRCA1/2-mutant, early **HER2-negative** breast cancer; trial terminated |
| [NCT05826964](https://clinicaltrials.gov/study/NCT05826964) | Phase 2 | Active, not recruiting | 24 | ctDNA-guided early treatment switch in HR-positive metastatic breast cancer; not specific to talazoparib label |
| [NCT06735742](https://clinicaltrials.gov/study/NCT06735742) | N/A | Active, not recruiting | 3 | Japan post-marketing safety surveillance of TALZENNA in BRCA-mutated, **HER2-negative** unresectable/recurrent breast cancer |
| [NCT04134884](https://clinicaltrials.gov/study/NCT04134884) | Phase 1 | Completed | 34 | ASTX727 + talazoparib in triple-negative or hormone-resistant **HER2-negative** metastatic breast cancer |
| [NCT04550494](https://clinicaltrials.gov/study/NCT04550494) | Phase 2 | Recruiting | 36 | Talazoparib in advanced solid tumors with DNA-damage-response gene alterations (tumor-agnostic, not HER2-defined) |
| [NCT03911973](https://clinicaltrials.gov/study/NCT03911973) | Phase 1/2 | Active, not recruiting | 37 | Gedatolisib + talazoparib in TNBC or BRCA1/2-positive, **HER2-negative** breast cancer |
| [NCT02401347](https://clinicaltrials.gov/study/NCT02401347) | Phase 2 | Completed | 21 | Talazoparib in BRCA-wild-type TNBC/HRD or advanced **HER2-negative** breast cancer |
| [NCT01042379](https://clinicaltrials.gov/study/NCT01042379) | Phase 2 | Recruiting | 5000 | I-SPY2 adaptive platform trial matching novel agents to breast cancer subtypes; not talazoparib/HER2+ specific |
| [NCT05097599](https://clinicaltrials.gov/study/NCT05097599) | Phase 2 | Terminated | 11 | StrataPATH basket trial of approved drugs in biomarker-guided solid tumor populations |
| [NCT04508803](https://clinicaltrials.gov/study/NCT04508803) | Phase 2 | Completed | 37 | HX008 (anti-PD-1) + niraparib (not talazoparib) in germline-mutated metastatic breast cancer |

---

## Literature Evidence
*(Publications attached to the rank-1 prediction; the great majority describe HER2-negative disease, reinforcing the mapping-error concern)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36379199](https://pubmed.ncbi.nlm.nih.gov/36379199/) | 2022 | Meta-analysis/GRADE | Breast (Edinburgh, Scotland) | Olaparib/talazoparib for BRCA1/2-related advanced **HER2-negative** breast cancer; formal GRADE recommendations |
| [36045677](https://pubmed.ncbi.nlm.nih.gov/36045677/) | 2022 | Comparative study | Frontiers in Immunology | Retrospective comparison of talazoparib vs. conventional chemotherapy; abstract describes **HER2-negative** ABC population despite title |
| [36952230](https://pubmed.ncbi.nlm.nih.gov/36952230/) | 2023 | Real-world cohort | The Oncologist | Real-world US outcomes of talazoparib in germline BRCA-mutated, **HER2-negative** advanced breast cancer |
| [34324367](https://pubmed.ncbi.nlm.nih.gov/34324367/) | 2021 | Guideline | J Clin Oncol | ASCO guideline update on endocrine/targeted therapy for HR-positive, **HER2-negative** metastatic breast cancer |
| [40471518](https://pubmed.ncbi.nlm.nih.gov/40471518/) | 2025 | Phase I/II trial | Breast Cancer Res Treat | Gedatolisib + talazoparib in triple-negative or BRCA1/2-positive, **HER2-negative** breast cancer |
| [36202026](https://pubmed.ncbi.nlm.nih.gov/36202026/) | 2022 | Network meta-analysis | Cancer Treat Rev | Therapeutic sequencing algorithms for metastatic triple-negative breast cancer |
| [33983696](https://pubmed.ncbi.nlm.nih.gov/33983696/) | 2021 | Review | Oncology (Williston Park) | Novel therapies (immunotherapy, ADCs) for metastatic triple-negative breast cancer |
| [40192953](https://pubmed.ncbi.nlm.nih.gov/40192953/) | 2025 | Retrospective | Mol Diagn Ther | Notes FDA approval of olaparib/talazoparib specifically for germline/somatic BRCA1/2-mutated breast cancer |
| [35343197](https://pubmed.ncbi.nlm.nih.gov/35343197/) | 2022 | Review | Indian J Cancer | Role of PARP inhibitors in management of **HER2-negative** metastatic breast cancer |
| [39516069](https://pubmed.ncbi.nlm.nih.gov/39516069/) | 2025 | Real-world cohort | Clin Breast Cancer | Mayo Clinic real-world prescribing patterns and outcomes of PARP inhibitors in metastatic breast cancer |

---

## Singapore Market Information

Talazoparib currently has **no registered product license in Singapore** (0 total licenses, market status: Not Marketed). No authorization number, product name, or approved local indication text is available in this evidence pack.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor; synthetic-lethality mechanism, not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | High — this evidence pack independently flags a separate KG signal ("primary release disorder of platelets," rank 8) noting that thrombocytopenia is a well-known class adverse effect of PARP inhibitors including talazoparib; anemia and neutropenia are also class-typical concerns |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential (particularly platelet count), renal and hepatic function |
| Handling Protection | Recommend handling under institutional hazardous/cytotoxic drug precautions, consistent with oral targeted oncology agents |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data are all listed as data gaps in this evidence pack (safety.key_warnings, safety.contraindications, and DDI query all returned no data).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rank-1 predicted indication ("HER2 positive breast carcinoma") directly contradicts Talazoparib's core validated mechanism and approved population (gBRCA-mutated, **HER2-negative** breast cancer), and essentially all of its attached trial and literature evidence describes HER2-negative populations — indicating a likely disease-label mapping error rather than a genuine repurposing signal. Independently, safety pre-assessment (S1) is blocked because product-label warnings/contraindications (DG001, Blocking) and confirmed MOA (DG002, High) are both data gaps, and Singapore has zero registered licenses for this drug.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/HSA product label warnings and contraindications
- Resolve DG002: confirm MOA via DrugBank API query
- Manually verify/correct the "HER2 positive breast carcinoma" disease-node mapping against the EMBRACA trial population before treating it as a repurposing candidate
- If the mapping error is confirmed, re-run this evaluation using rank-3 "progesterone-receptor negative breast cancer" (L2 evidence, Phase 3 RCT NCT01945775, decision stage S2, "Proceed with Guardrails"), which is mechanistically and clinically the stronger signal in this pack
- Confirm Singapore HSA registration pathway status given the drug is currently not marketed locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

