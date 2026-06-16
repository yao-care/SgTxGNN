---
layout: default
title: Emicizumab
parent: 僅模型預測 (L5)
nav_order: 366
evidence_level: L5
indication_count: 10
---

# Emicizumab
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

# Emicizumab: From Congenital Hemophilia A to Acquired Coagulation Factor Deficiency

## One-Sentence Summary

Emicizumab (Hemlibra®) is a bispecific monoclonal antibody approved globally for prophylaxis in congenital Hemophilia A, acting by directly bridging activated Factor IXa and Factor X to restore the missing cofactor function of Factor VIII. The TxGNN model predicts it may be effective for **Acquired Coagulation Factor Deficiency** — primarily Acquired Hemophilia A (AHA), where autoantibodies neutralize endogenous Factor VIII — a mechanistically near-identical scenario to its approved indication. This repurposing direction is supported by **3 published Phase 2/3 clinical trials** and **19 publications**, making it the highest-confidence candidate among 10 predicted indications evaluated in this multi-indication report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Congenital Hemophilia A prophylaxis (with and without inhibitors) |
| Predicted New Indication | Acquired Coagulation Factor Deficiency (Acquired Hemophilia A) |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Emicizumab is a humanized bispecific IgG4 antibody engineered to simultaneously bind activated Factor IXa (FIXa) and Factor X (FX), physically bridging them in a manner that mimics the cofactor activity of activated Factor VIII (FVIIIa). In normal hemostasis, FVIIIa serves as a scaffold that dramatically accelerates FIXa-mediated FX activation within the intrinsic tenase complex — a rate-limiting step in thrombin generation. By substituting for this structural role rather than replacing the FVIII protein itself, emicizumab generates its hemostatic effect entirely independent of FVIII presence or activity.

In Acquired Hemophilia A (AHA), patients — typically elderly adults with no prior bleeding history — spontaneously develop inhibitory autoantibodies against their own FVIII, resulting in severe and often life-threatening bleeding. The root pathophysiology is functionally identical to congenital Hemophilia A with inhibitors: FVIII activity is effectively zero, and bypassing agents (recombinant FVIIa, activated prothrombin complex concentrate) are required for acute bleed control. Crucially, because emicizumab does not resemble FVIII structurally, **anti-FVIII autoantibodies cannot neutralize it** — making its mechanism not just compatible with AHA, but ideally suited to it.

The analogy is precise: approved indication (congenital HA with inhibitors) and AHA are distinguished only by the cause of FVIII loss — genetic deletion versus autoimmune destruction. Published Phase 2/3 trials including the GTH-AHA-EMI study (*Lancet Haematology*, 2023) and the AGEHA Phase 3 program (*J Thromb Haemost*, 2023/2025) confirm that emicizumab prophylaxis substantially reduces bleeding burden in AHA, enables deferral of aggressive immunosuppression, and may improve survival in the characteristically frail AHA patient population.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT04398628](https://clinicaltrials.gov/study/NCT04398628) | N/A | Recruiting | 3,000 | ATHN Transcends: Large observational registry covering safety, effectiveness, and treatment practices across non-neoplastic hematologic disorders, including AHA patients treated with emicizumab. Provides real-world background data; not an interventional efficacy trial for emicizumab specifically. |

*Note: The pivotal interventional studies (GTH-AHA-EMI Phase 2 and AGEHA Phase 3) are published as completed trial results and are captured in the literature section below.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36696195](https://pubmed.ncbi.nlm.nih.gov/36696195/) | 2023 | Phase 3 Prospective | J Thromb Haemost | AGEHA Phase 3: First prospective multicenter study of emicizumab in AHA; demonstrated favorable benefit-risk profile alongside immunosuppressive therapy in Cohort 1 |
| [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/) | 2023 | Phase 2 Single-arm | Lancet Haematology | GTH-AHA-EMI: Emicizumab prophylaxis protected AHA patients from bleeding and allowed deferral of immunosuppression during the critical first 12 weeks of management |
| [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/) | 2025 | Phase 3 Final Analysis | Thromb Haemost | AGEHA final analysis: Confirmed benefit in both IST-eligible (Cohort 1) and IST-ineligible (Cohort 2) AHA patients; supports long-term subcutaneous prophylaxis |
| [40795229](https://pubmed.ncbi.nlm.nih.gov/40795229/) | 2025 | Prospective Cohort | Blood Advances | 2-year GTH-AHA-EMI follow-up: Sustained survival benefit and reduced serious infections by postponing aggressive immunosuppression in frail patients |
| [39361769](https://pubmed.ncbi.nlm.nih.gov/39361769/) | 2024 | Retrospective Cohort | Blood Advances | Real-world US multicenter study (62 patients, 12 hemophilia treatment centers): Off-label emicizumab effective in AHA; validates Phase 2/3 findings in routine clinical practice |
| [38049124](https://pubmed.ncbi.nlm.nih.gov/38049124/) | 2024 | Expert Consensus | Haemostaseologie | GTH-AHA Working Group consensus recommendations: Practical guidance on emicizumab initiation, dosing, monitoring, and integration with immunosuppression in AHA |
| [39536818](https://pubmed.ncbi.nlm.nih.gov/39536818/) | 2025 | Narrative Review | J Thromb Haemost | Comprehensive review of emicizumab in the AHA era: epidemiology, pathophysiology, diagnosis, and current treatment approach including emicizumab prophylaxis strategies |
| [38395066](https://pubmed.ncbi.nlm.nih.gov/38395066/) | 2025 | Review | Semin Thromb Hemost | Innovative therapies for AHA: positions emicizumab within an evolving landscape including novel bypassing agents, non-replacement hemostatic drugs, and immunotherapy |
| [36795341](https://pubmed.ncbi.nlm.nih.gov/36795341/) | 2023 | Review | Blood Transfusion | Pros and cons of emicizumab in AHA: discusses prophylaxis vs. on-demand use, co-administration risks with aPCC, and measurement challenges in the presence of FVIII activity |
| [36280447](https://pubmed.ncbi.nlm.nih.gov/36280447/) | 2022 | Review | Transfus Med Rev | Advances in AHA: comprehensive overview of emicizumab's emerging role, including use in patients with concurrent thrombotic risk factors — a clinically important AHA subgroup |

---

## Singapore Market Information

Emicizumab is not currently registered with Singapore's Health Sciences Authority (HSA). No marketing authorization records are on file.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No Singapore registrations on record |

*For reference: Emicizumab (Hemlibra®) is approved in the United States (FDA, 2017 for congenital HA with inhibitors; 2019 without inhibitors), the European Union (EMA), Japan (PMDA), and multiple other jurisdictions. Singapore HSA registration status should be confirmed directly with the HSA drug database.*

---

## Safety Considerations

Formal Singapore package insert warnings and contraindications are not available in the current evidence pack. Please refer to the Hemlibra® prescribing information and HSA-approved documentation for complete safety data.

**Key safety signals identified from published literature:**
- **Thrombotic Microangiopathy (TMA) / Thromboembolism**: Serious events reported when emicizumab is co-administered with activated prothrombin complex concentrate (aPCC/FEIBA). Concurrent use should be avoided or strictly managed with close monitoring.
- **Thrombotic Thrombocytopenic Purpura (TTP)**: Emicizumab's pro-coagulant mechanism may worsen microvascular thrombosis in TTP — this indication is mechanistically contraindicated and should not be pursued.
- **Injection site reactions**: Common with subcutaneous administration; generally mild.
- **Laboratory monitoring**: Emicizumab interferes with standard one-stage clotting assays; specialized chromogenic assays are required to accurately measure FVIII activity in patients receiving emicizumab.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three published Phase 2/3 clinical trials and a substantial real-world evidence base establish that emicizumab prophylaxis is effective and generally well-tolerated in Acquired Hemophilia A, a condition with a mechanistically near-identical FVIII bypass requirement to the drug's approved congenital indication. The evidence meets L1 criteria, and regulatory precedent exists globally for this use.

**To proceed, the following is needed:**
- Resolve the blocking data gap: obtain the official HSA/TFDA prescribing information PDF to complete formal safety screening (currently prevents entry into S1 safety review)
- Confirm Singapore HSA registration pathway — determine whether off-label use under existing global approvals is feasible, or whether a local indication extension application is required
- Complete DrugBank MOA documentation query (pending) to support the mechanistic rationale section in any regulatory submission
- Develop an AHA-specific monitoring protocol addressing: plasma emicizumab level measurement (requires chromogenic assay), concomitant bypassing agent restrictions, and thrombotic event surveillance
- Evaluate feasibility in Singapore's hemophilia treatment center network — AHA incidence is low (~1–4 per million/year), requiring specialized hematology infrastructure
- Do not pursue the **TTP** indication (Rank 8): mechanistically contraindicated, risk of harm
- Flag **"flood factor deficiency"** (Rank 10) as a likely ontology mapping error; clarify disease entity before any further evaluation

---

## Summary of All Predicted Indications

| Rank | Indication | TxGNN Score | Evidence Level | Decision | Notes |
|------|-----------|-------------|---------------|---------|-------|
| 5 | Acquired Coagulation Factor Deficiency | 99.90% | **L1** | **Proceed with Guardrails** | Primary candidate; Phase 2/3 trial data available |
| 3 | Glanzmann Thrombasthenia | 99.98% | L4 | Research Question | Mechanistically plausible; only background observational data |
| 1 | Pseudo-von Willebrand Disease | 99.99% | L5 | Hold | Mechanistic mismatch; GPIbα gain-of-function may be worsened |
| 2 | Primary Release Disorder of Platelets | 99.99% | L5 | Hold | Indirect mechanism; no clinical evidence |
| 4 | Scott Syndrome | 99.92% | L5 | Hold | Ultra-rare (<100 cases worldwide); theoretical basis only |
| 6 | Bleeding Diathesis (Collagen Receptor Defect) | 99.86% | L5 | Hold | Distal compensation only; no supporting evidence |
| 7 | Hemorrhagic Disorder (Constitutional Thrombocytopenia) | 99.85% | L5 | Hold | Quantity defect, not coagulation factor; limited relevance |
| 8 | Thrombotic Thrombocytopenic Purpura | 99.61% | L5 | **Hold ⚠️** | **Safety concern**: pro-coagulant mechanism may worsen TTP |
| 9 | Fetal/Neonatal Alloimmune Thrombocytopenia | 99.52% | L5 | Hold | Immune-mediated platelet destruction; mechanism incompatible; neonatal safety unknown |
| 10 | Flood Factor Deficiency | 99.40% | L5 | Hold ⚠️ | Terminology unclear — likely ontology mapping error; do not act without clarification |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

