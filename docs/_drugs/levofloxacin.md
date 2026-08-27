---
layout: default
title: Levofloxacin
parent: 僅模型預測 (L5)
nav_order: 591
evidence_level: L5
indication_count: 10
---

# Levofloxacin
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

# Levofloxacin: From Bacterial Infections to Monoclonal Gammopathy (Myeloma Infection Prophylaxis)

> **Note on scope**: This evidence pack (`TW-DB01137-multi`) contains **10 TxGNN-predicted indications** for Levofloxacin, not one. Eight of the ten (punctate epithelial keratoconjunctivitis, hyperamylasemia, polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, premalignant hematological system disease, hematological disease associated with an acquired peripheral neuropathy, congenital hematological disorder) have no supporting clinical trials or literature, or literature that is mechanistically mismatched, and are scored **Hold**. This report focuses on the candidate with the strongest supporting evidence — **monoclonal gammopathy** — rather than the single highest raw TxGNN score (rank 1, "punctate epithelial keratoconjunctivitis"), because the rank-1 prediction's only supporting literature describes a microsporidial (non-bacterial) pathogen, which does not match Levofloxacin's antibacterial mechanism. A second notable candidate, **septicemic plague**, is discussed briefly below since it also carries meaningful (L2) evidence.

## One-Sentence Summary

Levofloxacin is a broad-spectrum fluoroquinolone antibiotic; its original approved indication(s) are not recorded in this dataset (see Data Gap DG002), but its class-level use is for bacterial infections. The TxGNN model predicts a repurposing signal toward **Monoclonal Gammopathy**, and the surrounding literature — 20 PubMed records, including one completed Phase 3 RCT — actually supports a narrower, well-established use: **antibacterial prophylaxis to prevent infection during induction chemotherapy in newly diagnosed, symptomatic multiple myeloma**, not treatment of the gammopathy itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (fluoroquinolone antibiotic class) — specific regulatory indication text is not available in this dataset |
| Predicted New Indication | Monoclonal Gammopathy (evidence specifically supports newly diagnosed multiple myeloma) |
| TxGNN Prediction Score | 99.81% (rank 7 of 10 candidates in this pack) |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

**On the Evidence Level determination**: the underlying evidence pack tags this indication internally as "L1." Applying the rubric independently against the actual literature: only **one** completed Phase 3 RCT is verifiable — the TEAMM trial (PMID 31668592). A second record tagged "RCT" in the metadata (PMID 29080369) is, per its own abstract, a **retrospective cohort study**, not a randomized trial. Since the ≥2-completed-Phase-3-RCT bar for L1 is not met by the visible evidence, this report assigns **L2** ("1 completed Phase 2/3 RCT").

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for Levofloxacin is not available in this evidence pack (flagged as Data Gap DG002, High severity). Based on general pharmacological knowledge, Levofloxacin is a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV, giving it broad-spectrum bactericidal activity against Gram-negative and some Gram-positive organisms.

The TxGNN signal toward "monoclonal gammopathy" is not a direct pharmacological action against the plasma-cell disorder itself — there is no mechanistic pathway by which a DNA-gyrase inhibitor would affect abnormal immunoglobulin production. Instead, the supporting evidence describes an indirect, well-recognized clinical use: newly diagnosed multiple myeloma causes profound immunosuppression, and roughly a quarter of patients develop a serious infection within three months of diagnosis. Levofloxacin prophylaxis during the high-risk induction/neutropenic period reduces bloodstream infections and febrile episodes — this is disease-adjacent infection prevention, not disease-modifying therapy.

Importantly, the TxGNN-predicted term "monoclonal gammopathy" is broader than the evidence base. Essentially all supporting studies concern **newly diagnosed, symptomatic multiple myeloma** patients undergoing chemotherapy or autologous stem-cell transplantation. Patients with MGUS (monoclonal gammopathy of undetermined significance), who are not undergoing myelosuppressive treatment, have no established infection-prophylaxis need, and this evidence should not be extrapolated to them.

*Secondary candidate worth noting*: **Septicemic plague** (rank 9, score 99.80%, L2, "Proceed with Guardrails") is supported by 16 literature records, including FDA approval of Levofloxacin for plague under the Animal Efficacy Rule (non-human primate models), since human RCTs are not ethically feasible for this indication. This represents an established regulatory precedent rather than a novel prediction, but animal-model results are not fully consistent (e.g., PMID 21574421 reports lack of efficacy against a nalidixic-acid-resistant strain), so it is flagged for awareness rather than pursued as the primary candidate here.

## Clinical Trial Evidence

Currently no related clinical trials registered in ClinicalTrials.gov/ICTRP for this indication in this dataset.

*(Note: the TEAMM Phase 3 RCT supporting this indication is present in the literature/PubMed corpus below but was not captured by the registry-based clinical-trials search in this evidence pack.)*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31668592](https://pubmed.ncbi.nlm.nih.gov/31668592/) | 2019 | RCT (Phase 3) | The Lancet. Oncology | TEAMM trial: levofloxacin prophylaxis in newly diagnosed myeloma reduced febrile episodes and possible/definite infections vs. placebo during the first 12 weeks. |
| [31690402](https://pubmed.ncbi.nlm.nih.gov/31690402/) | 2019 | HTA Report (TEAMM full report) | Health Technology Assessment | Full health-technology-assessment report of the TEAMM RCT; evaluates cost-effectiveness and infection outcomes of prophylactic levofloxacin in newly diagnosed symptomatic myeloma. |
| [29080369](https://pubmed.ncbi.nlm.nih.gov/29080369/) | 2018 | Retrospective Cohort (mislabeled "RCT" in source metadata) | Clinical Transplantation | Retrospective comparison of ciprofloxacin vs. levofloxacin prophylaxis in autologous HSCT for myeloma; comparable breakthrough-infection rates between agents. |
| [32172361](https://pubmed.ncbi.nlm.nih.gov/32172361/) | 2020 | Review | Current Hematologic Malignancy Reports | Reviews supportive care in multiple myeloma, including infection-prophylaxis strategies alongside bone disease and renal management. |
| [31668593](https://pubmed.ncbi.nlm.nih.gov/31668593/) | 2019 | Review/Commentary | The Lancet. Oncology | Commentary discussing the TEAMM findings in the context of reducing infection-related morbidity and mortality in myeloma. |
| [26150022](https://pubmed.ncbi.nlm.nih.gov/26150022/) | 2015 | Cohort | Biology of Blood and Marrow Transplantation | Levofloxacin prophylaxis associated with reduced bloodstream infection and fever/neutropenia rates in myeloma patients undergoing autologous HSCT. |
| [37573150](https://pubmed.ncbi.nlm.nih.gov/37573150/) | 2023 | Cohort | Transplant Infectious Disease | Characterizes infectious complications after autologous HSCT in myeloma patients, comparing outcomes with/without levofloxacin prophylaxis. |
| [32304873](https://pubmed.ncbi.nlm.nih.gov/32304873/) | 2020 | Retrospective Review | Biology of Blood and Marrow Transplantation | Re-examines the value of fluoroquinolone prophylaxis in autologous stem-cell transplantation for myeloma. |
| [25212681](https://pubmed.ncbi.nlm.nih.gov/25212681/) | 2014 | Cohort | International Journal of Hematology | Levofloxacin prophylaxis reduced severe infection rates in myeloma patients receiving bortezomib-based regimens. |
| [32019731](https://pubmed.ncbi.nlm.nih.gov/32019731/) | 2020 | Cohort | Clinical Lymphoma, Myeloma & Leukemia | Real-world Asian cancer-center data on bacterial infection rates during bortezomib-based induction therapy for myeloma, without routine fluoroquinolone prophylaxis. |

## Singapore Market Information

Levofloxacin currently has **0 registrations** and is **not marketed** in Singapore under this dataset (`market_status: 未上市`). No license records are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-interaction data are available in this evidence pack — this is itself flagged internally as a **Blocking-severity data gap (DG001: TFDA/HSA label warnings and contraindications)**, meaning this candidate cannot yet complete a formal safety pre-assessment (S1).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- One completed Phase 3 RCT (TEAMM) plus multiple supportive cohort studies consistently show that levofloxacin prophylaxis reduces infection/febrile episodes in newly diagnosed multiple myeloma patients during induction chemotherapy — the strongest evidence base among the 10 TxGNN predictions in this pack.
- The evidence supports a narrow, infection-prophylaxis use in a specific at-risk population (newly diagnosed myeloma undergoing myelosuppressive therapy), not the broader "monoclonal gammopathy" category, and the drug is not currently marketed in Singapore — both warrant guardrails rather than an unqualified "Go."

**To proceed, the following is needed:**
- TFDA/HSA package-insert warnings and contraindications (Blocking data gap, DG001) — required before any formal S1 safety pre-assessment
- Confirmed mechanism-of-action documentation (Data gap DG002)
- Clarification/restriction of clinical scope to newly diagnosed, symptomatic multiple myeloma patients undergoing induction chemotherapy or autologous HSCT, explicitly excluding MGUS
- Singapore market-entry/registration pathway assessment, given 0 current registrations
- Local antimicrobial-resistance data to evaluate suitability of a fluoroquinolone-prophylaxis strategy in this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

