---
layout: default
title: Obinutuzumab
parent: 僅模型預測 (L5)
nav_order: 721
evidence_level: L5
indication_count: 10
---

# Obinutuzumab
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

# Obinutuzumab: From Chronic Lymphocytic Leukemia to Follicular Lymphoma

*Note: This evidence pack (`TW-DB08935-multi`) contains 10 TxGNN-predicted indications for obinutuzumab. The single highest-scoring candidate (a CLL/SLL molecular subtype) currently has zero matched trials/literature due to an ontology-labeling gap, so this report leads with **Follicular Lymphoma (rank 3)** — the candidate with the strongest and most decision-relevant evidence (L1, Proceed with Guardrails). All other candidates, including the top-ranked CLL/SLL subtypes, are summarized in the appendix at the end.*

## One-Sentence Summary

Obinutuzumab is a type II glycoengineered anti-CD20 monoclonal antibody already established internationally as a treatment for chronic lymphocytic leukemia (CLL). The TxGNN model predicts it may also be effective for **Follicular Lymphoma**, a prediction already validated by **50 matched clinical trials** (including two completed Phase 3 RCTs) and **19 matched publications**, though the drug itself is not currently registered in Singapore.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Lymphocytic Leukemia (CLL) — anti-CD20 monoclonal antibody class |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for obinutuzumab is not available in this evidence pack. Based on the information that is available, obinutuzumab is a type II, fully humanized, glycoengineered anti-CD20 monoclonal antibody that acts through enhanced antibody-dependent cellular cytotoxicity (ADCC), complement-dependent cytotoxicity (CDC), and direct B-cell apoptosis. Its efficacy in chronic lymphocytic leukemia (CLL) has already been demonstrated in a Phase 3 RCT (the CLL11 trial), which is the drug's established original indication.

Follicular lymphoma (FL) and CLL are both CD20-positive, mature B-cell lymphoproliferative malignancies, so the same molecular target and cytotoxic mechanism apply directly to FL tumor cells. This mechanistic overlap is not merely theoretical: obinutuzumab has already received regulatory approval in multiple markets for previously untreated advanced FL, based on the pivotal Phase 3 GALLIUM trial (NCT01332968), which showed superior progression-free survival compared with rituximab-based immunochemotherapy. The volume and maturity of trial and literature evidence for this indication — spanning frontline, relapsed/refractory, and maintenance settings — further support the biological plausibility and clinical actionability of this TxGNN prediction.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01332968](https://clinicaltrials.gov/study/NCT01332968) | Phase 3 | Completed | 1401 | GALLIUM trial — obinutuzumab + chemotherapy vs rituximab + chemotherapy followed by maintenance in untreated advanced indolent NHL; pivotal trial underlying FL approval |
| [NCT03817853](https://clinicaltrials.gov/study/NCT03817853) | Phase 4 | Completed | 114 | Post-marketing confirmatory study of obinutuzumab short-duration (90-min) infusion combined with chemotherapy in previously untreated advanced FL |
| [NCT05848765](https://clinicaltrials.gov/study/NCT05848765) | Phase 2 | Recruiting | 284 | REFRACT — randomized trial of obinutuzumab-based novel therapy vs standard chemotherapy in relapsed/refractory FL |
| [NCT06191744](https://clinicaltrials.gov/study/NCT06191744) | Phase 3 | Recruiting | 1095 | EPCORE™FL-2 — epcoritamab + lenalidomide/rituximab vs chemoimmunotherapy in previously untreated FL |
| [NCT05058404](https://clinicaltrials.gov/study/NCT05058404) | Phase 3 | Active, not recruiting | 605 | FIL_FOLL19 — shortened vs standard chemotherapy combined with immunotherapy in high-tumor-burden FL |
| [NCT01059630](https://clinicaltrials.gov/study/NCT01059630) | Phase 3 | Completed | 413 | Bendamustine vs bendamustine + obinutuzumab in rituximab-refractory indolent NHL |
| [NCT01582776](https://clinicaltrials.gov/study/NCT01582776) | Phase 1/2 | Completed | 317 | Obinutuzumab + lenalidomide in relapsed/refractory and previously untreated FL, plus aggressive B-cell lymphoma cohorts |
| [NCT00825149](https://clinicaltrials.gov/study/NCT00825149) | Phase 1 | Completed | 137 | Obinutuzumab combined with CHOP, FC, or bendamustine chemotherapy in CD20+ FL |
| [NCT04034056](https://clinicaltrials.gov/study/NCT04034056) | N/A | Completed | 299 | Real-world retrospective/prospective study of obinutuzumab effectiveness and safety in untreated advanced FL |
| [NCT04450173](https://clinicaltrials.gov/study/NCT04450173) | Phase 2 | Recruiting | 40 | Obinutuzumab + ibrutinib + venetoclax in previously untreated FL |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | RCT | New England Journal of Medicine | GALLIUM primary results: obinutuzumab-based chemoimmunotherapy for first-line FL |
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | RCT | Journal of Clinical Oncology | GALLIUM subgroup analysis of chemotherapy backbone impact on efficacy/safety |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | RCT (final analysis) | HemaSphere | GALLIUM final results — obinutuzumab vs rituximab immunochemotherapy in untreated iNHL |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | RCT | Journal of Clinical Oncology | ROSEWOOD — zanubrutinib + obinutuzumab vs obinutuzumab monotherapy in relapsed/refractory FL |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | Cohort (Phase 2) | The Lancet Haematology | GALEN — obinutuzumab + lenalidomide in relapsed/refractory FL |
| [37767550](https://pubmed.ncbi.nlm.nih.gov/37767550/) | 2024 | Phase 1b/2 | Haematologica | Polatuzumab vedotin + bendamustine/rituximab or obinutuzumab in relapsed/refractory FL |
| [34797453](https://pubmed.ncbi.nlm.nih.gov/34797453/) | 2021 | Cohort | Current Oncology Reports | Early progressing FL (POD24) — risk factors and outcomes |
| [39830356](https://pubmed.ncbi.nlm.nih.gov/39830356/) | 2024 | Review | Frontiers in Pharmacology | Rapid review of efficacy, safety, and cost-effectiveness of obinutuzumab in FL |
| [35180337](https://pubmed.ncbi.nlm.nih.gov/35180337/) | 2022 | Review | Oncology (Williston Park) | Current and emerging therapies for follicular lymphoma |
| [38660754](https://pubmed.ncbi.nlm.nih.gov/38660754/) | 2024 | Review | Turkish Journal of Haematology | Comprehensive review of FL management, including obinutuzumab-based regimens |

## Singapore Market Information

Obinutuzumab currently has **no registered product license in Singapore** (0 registrations; market status: 未上市 / Not Marketed). No authorization records are available to summarize.

## Cytotoxicity

Obinutuzumab is an antineoplastic agent (targeted immunotherapy used to treat B-cell hematologic malignancies), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy (Type II, glycoengineered anti-CD20 monoclonal antibody) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Follicular lymphoma is supported by L1-level evidence — including two completed Phase 3 RCTs (GALLIUM, and the bendamustine ± obinutuzumab trial) plus an additional Phase 3 and Phase 4 study ongoing — and obinutuzumab is already an internationally approved standard-of-care option for FL. However, the drug has zero registrations in Singapore and lacks local safety labeling data, so registration and safety review must precede any clinical use.

**To proceed, the following is needed:**
- TFDA/HSA package insert (warnings/contraindications) — currently a blocking data gap (DG001)
- Detailed mechanism-of-action documentation via DrugBank (DG002)
- Confirmation of local drug registration pathway, since obinutuzumab has zero existing Singapore licenses
- Drug interaction (DDI) data — current query returned no results

---

## Appendix: Other Predicted Indications in This Evidence Pack

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|------|------|------|------|
| 1 | Pregerminal center CLL/SLL | 99.21% | L5 | Hold | Molecular CLL subtype; mechanism plausible (CLL is an approved indication) but no trials/literature are mapped to this specific ontology term — likely a labeling/ontology gap requiring manual review rather than a true negative |
| 2 | CLL/SLL with IGHV somatic hypermutation | 99.21% | L5 | Hold | Same CLL/SLL ontology-gap issue as rank 1 |
| 4 | Mantle Cell Lymphoma | 98.75% | L2 | Proceed with Guardrails | Second-strongest candidate; CD20+ B-cell lymphoma with head-to-head obinutuzumab vs rituximab data and multiple Phase 2 combination trials |
| 5 | Metastatic neoplasm | 98.51% | L4 | Hold | Term too broad/non-specific; matched trials mostly involve other drugs (atezolizumab, acalabrutinib) with obinutuzumab as background pretreatment only |
| 6 | Malignant spiradenoma | 98.47% | L5 | Hold | Sweat-gland-derived skin tumor, not a B-cell malignancy — no CD20 mechanistic basis; likely embedding-based false positive |
| 7 | Neoplasm of mature B-cells | 98.08% | L3 | Research Question | Valid upper-level category encompassing CLL/FL/MCL; mechanistically sound but too broad for standalone clinical decision-making |
| 8 | Small intestinal Burkitt lymphoma | 97.84% | L4 | Hold | CD20+ mature B-cell lymphoma (class-level plausibility via rituximab precedent) but no direct trial/literature evidence |
| 9 | Langerhans cell histiocytosis | 97.81% | L5 | Hold | Dendritic/histiocytic lineage, does not express CD20 — no mechanistic basis; likely false positive |
| 10 | Thyroid MALT lymphoma | 97.76% | L4 | Hold | CD20+ marginal zone lymphoma (class-level plausibility via rituximab precedent) but no direct trial/literature evidence |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

