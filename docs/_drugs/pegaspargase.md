---
layout: default
title: Pegaspargase
parent: 僅模型預測 (L5)
nav_order: 760
evidence_level: L5
indication_count: 10
---

# Pegaspargase
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

# Pegaspargase: From Acute Lymphoblastic Leukemia to Precursor Lymphoblastic Lymphoma/Leukemia

## One-Sentence Summary

Pegaspargase is a pegylated asparaginase enzyme with an established role in multi-agent chemotherapy for acute lymphoblastic leukemia (ALL), as documented in the clinical literature reviewed for this candidate.
The TxGNN model predicts it may be effective for **precursor lymphoblastic lymphoma/leukemia**, essentially the same disease biology as its known core indication,
with **50 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Lymphoblastic Leukemia (ALL) — established use as part of multi-agent chemotherapy, per cited literature; no local Singapore license data available |
| Predicted New Indication | Precursor lymphoblastic lymphoma/leukemia |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available from DrugBank for this candidate. Based on known information, Pegaspargase is a pegylated form of *E. coli*-derived L-asparaginase and is part of the asparaginase drug class used in multi-agent chemotherapy regimens for acute lymphoblastic leukemia; its efficacy in ALL has been proven in numerous Phase 3 trials, and mechanistically it is directly applicable to precursor lymphoblastic lymphoma/leukemia.

The core, well-characterized mechanism underlying this prediction is that precursor (B- or T-lineage) lymphoblasts lack sufficient endogenous asparagine synthetase and therefore cannot synthesize adequate asparagine to survive. Pegaspargase depletes circulating asparagine, selectively inducing apoptosis in these asparagine-dependent lymphoblasts. Because "precursor lymphoblastic lymphoma/leukemia" and "acute lymphoblastic leukemia" describe overlapping/closely related disease biology, this is best understood not as a novel repurposing hypothesis but as a direct extension of the drug's existing standard-of-care role — which is precisely why the supporting evidence base is unusually strong (L1) compared with the drug's other TxGNN-predicted indications (most of which are Hold-level, L5, with no supporting trials or literature).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00103285](https://clinicaltrials.gov/study/NCT00103285) | Phase 3 | Completed | 5377 | Randomized comparison of combination chemotherapy regimens in newly diagnosed standard-risk B-precursor ALL |
| [NCT00967057](https://clinicaltrials.gov/study/NCT00967057) | Phase 3 | Completed | 470 | ALLR3 international collaborative trial; combination chemotherapy incl. PEG-asparaginase backbone for relapsed/refractory ALL |
| [NCT01117441](https://clinicaltrials.gov/study/NCT01117441) | Phase 3 | Completed | 6136 | International collaborative treatment protocol comparing combination chemotherapy regimens in children/adolescents with ALL |
| [NCT01190930](https://clinicaltrials.gov/study/NCT01190930) | Phase 3 | Active, not recruiting | 9350 | Risk-adapted chemotherapy regimens in newly diagnosed standard-risk B-ALL or localized B-lineage lymphoblastic lymphoma |
| [NCT03914625](https://clinicaltrials.gov/study/NCT03914625) | Phase 3 | Active, not recruiting | 6720 | Blinatumomab plus chemotherapy (incl. pegaspargase) in newly diagnosed standard-risk B-ALL/B-lymphoblastic lymphoma |
| [NCT00819351](https://clinicaltrials.gov/study/NCT00819351) | Phase 3 | Completed | 650 | NOPHO protocol comparing intermittent vs. continuous PEG-asparaginase dosing for asparagine depletion |
| [NCT00671034](https://clinicaltrials.gov/study/NCT00671034) | Phase 3 | Completed | 166 | Calaspargase pegol vs. pegaspargase combined with chemotherapy in high-risk ALL |
| [NCT05602194](https://clinicaltrials.gov/study/NCT05602194) | Phase 3 | Recruiting | 440 | Levocarnitine prophylaxis to prevent asparaginase-associated hepatotoxicity in AYA ALL/LL/MPAL patients |
| [NCT01769209](https://clinicaltrials.gov/study/NCT01769209) | Phase 2 | Completed | 18 | Bortezomib added to chemotherapy (VXLD) for relapsed/refractory adult ALL |
| [NCT05192889](https://clinicaltrials.gov/study/NCT05192889) | Phase 1/2 | Active, not recruiting | 35 | Venetoclax + navitoclax combination in relapsed/refractory pediatric ALL/lymphoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Cohort/comparative | J Clin Oncol | DFCI 11-001: efficacy/toxicity comparison of calaspargase pegol vs. standard pegaspargase in childhood ALL |
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Cohort (risk-adapted program) | Blood Advances | GIMEMA LAL1913: pegaspargase added to pediatric-inspired regimen in adult Ph− ALL/LL |
| [27114587](https://pubmed.ncbi.nlm.nih.gov/27114587/) | 2016 | RCT (COG) | J Clin Oncol | AALL0232: dexamethasone and high-dose methotrexate improve outcomes in high-risk B-ALL |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Expert consensus | Haematologica | Panel consensus on recognition/prevention/management of asparaginase-associated adverse events in adult ALL |
| [39322712](https://pubmed.ncbi.nlm.nih.gov/39322712/) | 2024 | Phase 2 follow-up | Leukemia | Long-term follow-up of venetoclax + hyper-CVAD/nelarabine/pegylated asparaginase in T-ALL/LBL |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | RCT (COG AALL0434) | J Clin Oncol | Phase III trial testing nelarabine in newly diagnosed T-ALL |
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | Phase III trial (COG AALL1231) | J Clin Oncol | Bortezomib added to chemotherapy in newly diagnosed T-ALL/T-LL |
| [31030380](https://pubmed.ncbi.nlm.nih.gov/31030380/) | 2019 | Review | Drugs | Pegaspargase review: approved in USA/EU as component of multi-agent chemotherapy for ALL |
| [40163215](https://pubmed.ncbi.nlm.nih.gov/40163215/) | 2025 | Phase 2 multicenter | Int J Hematol | Efficacy, safety and PK of lyophilized pegaspargase in Japanese patients with previously untreated ALL |
| [31977001](https://pubmed.ncbi.nlm.nih.gov/31977001/) | 2020 | Review | Blood | "How I treat" review on managing pegasparaginase toxicities in adults with ALL |

---

## Singapore Market Information

Pegaspargase currently has **no registered license in Singapore** (market status: not marketed; 0 registrations on file). No product/authorization details are available to tabulate.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (asparagine-depleting antineoplastic enzyme) |
| Myelosuppression Risk | Low as a direct effect of asparaginase itself (it is not a DNA-damaging cytotoxic); however, it is routinely combined with myelosuppressive multi-agent regimens, so overall regimen-level myelosuppression risk is significant |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Liver function tests, lipase/amylase (pancreatitis risk), coagulation panel (fibrinogen, antithrombin — thrombosis/hemorrhage risk), triglycerides (hypertriglyceridemia), hypersensitivity monitoring during/after infusion, CBC per combination regimen |
| Handling Protection | Yes — standard cytotoxic drug handling precautions required |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication (precursor lymphoblastic lymphoma/leukemia) is supported by multiple completed and ongoing Phase 3 trials with large enrollments and a substantial published literature base, reflecting the drug's already-established mechanistic and clinical role in ALL-spectrum disease (L1 evidence). However, Pegaspargase has no current market authorization in Singapore and this evidence pack lacks local safety labeling (warnings/contraindications) and confirmed MOA data.

**To proceed, the following is needed:**
- HSA-recognized product labeling / package insert (warnings and contraindications) — flagged as a blocking data gap
- Confirmed mechanism of action data from DrugBank or equivalent source
- Local regulatory pathway assessment given the drug is not currently marketed in Singapore
- Drug interaction (DDI) data, currently unavailable ("not_found")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

