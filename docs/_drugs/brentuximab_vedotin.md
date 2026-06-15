---
layout: default
title: Brentuximab Vedotin
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 10
---

# Brentuximab Vedotin
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

# Brentuximab Vedotin: From Hodgkin Lymphoma/sALCL to Follicular Lymphoma

## One-Sentence Summary

Brentuximab vedotin (Adcetris) is an anti-CD30 antibody-drug conjugate internationally approved for relapsed/refractory classical Hodgkin lymphoma and systemic anaplastic large cell lymphoma, though it is currently not registered in Singapore.
The TxGNN model predicts it may be effective for **Follicular Lymphoma (FL)**, based on the CD30-targeting mechanism applicable to CD30-positive FL subtypes such as Grade 3B and histologically transformed FL.
Currently, **6 clinical trials** and **20 publications** are associated with this direction, though meaningful direct evidence is confined to 1 active Phase 2 trial and 2 terminated trials with enrolled patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hodgkin lymphoma and systemic anaplastic large cell lymphoma (international approval; not registered in Singapore) |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on known information, brentuximab vedotin is an antibody-drug conjugate (ADC) comprising an anti-CD30 monoclonal antibody linked to monomethyl auristatin E (MMAE), a potent microtubule-disrupting cytotoxic agent. Upon binding to CD30 on the tumour cell surface, the conjugate is internalised and MMAE is released intracellularly, triggering cell cycle arrest and apoptosis. Efficacy is therefore entirely dependent on tumour CD30 expression, making biomarker-driven patient selection the central requirement for any new indication.

Follicular lymphoma in its classic low-grade form is typically CD30-negative. However, Grade 3B FL and histologically transformed FL (particularly transformation to diffuse large B-cell lymphoma or anaplastic large cell lymphoma) can acquire meaningful CD30 positivity, creating a biologically rational and druggable subpopulation. The mechanistic hypothesis has been adopted in clinical practice: NCT04587687 is an ongoing Phase 2 trial specifically investigating brentuximab vedotin plus bendamustine in relapsed/refractory FL, and NCT01805037 explicitly enrolled CD30-positive FL and mantle cell lymphoma patients alongside other CD30+ lymphoma types.

A published case report (PMID 32476657) provides direct supporting evidence: a patient with Grade I FL that transformed to CD30+ ALK1-negative anaplastic large cell lymphoma achieved complete response to brentuximab vedotin combined with high-dose methotrexate. While this represents a transformed rather than de novo FL setting, it validates the CD30-targeting rationale in patients with FL-origin tumours that acquire CD30 expression.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04587687](https://clinicaltrials.gov/study/NCT04587687) | Phase 2 | Recruiting | 23 | BV + bendamustine for relapsed/refractory follicular lymphoma; the only trial directly focused on this combination in FL; results pending (expected completion December 2026) |
| [NCT01805037](https://clinicaltrials.gov/study/NCT01805037) | Phase 1/2 | Terminated | 20 | BV + rituximab as frontline therapy for CD30+ and/or EBV+ lymphomas; design explicitly included CD30+ FL patients, confirming the mechanistic hypothesis has been clinically operationalised; partial safety data available |
| [NCT02594163](https://clinicaltrials.gov/study/NCT02594163) | Phase 2 | Terminated | 25 | Randomised BV + rituximab + bendamustine vs. rituximab + bendamustine for R/R CD30+ diffuse large B-cell lymphoma; terminated early with 25 enrolled; preliminary safety reference for BV-based B-cell lymphoma combinations |

> Three additional trials (NCT02623920, NCT04138875, NCT04795869) were withdrawn before any patient enrolment and contribute no interpretable data.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [32476657](https://pubmed.ncbi.nlm.nih.gov/32476657/) | 2020 | Case Report | Gulf Journal of Oncology | Complete response in Grade I FL that transformed to CD30+ ALK1– ALCL following treatment with BV + high-dose methotrexate; directly supports the CD30-targeting rationale in the FL context |
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | Review | Leukemia Research Reports | Comprehensive review of immunotherapy in indolent non-Hodgkin lymphoma including FL; discusses CD30-directed strategies and the emerging role of novel agents in this disease category |
| [38028985](https://pubmed.ncbi.nlm.nih.gov/38028985/) | 2023 | Case Report | Case Reports in Hematology | FL transformation to EBV+ DLBCL and EBV+ classical Hodgkin lymphoma; illustrates the biological plasticity of FL and its capacity to acquire CD30 expression upon transformation |
| [28967896](https://pubmed.ncbi.nlm.nih.gov/28967896/) | 2018 | Review | Bone Marrow Transplantation | Review of post-autologous SCT maintenance in lymphomas including FL; contextualises the role of novel agents, including BV, in the post-transplant consolidation strategy |

> The majority of retrieved publications (16 of 20) concern peripheral T-cell lymphoma, where BV has established evidence. These were excluded from the table as they do not directly inform the FL indication.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted cytotoxic — Antibody-Drug Conjugate (ADC); anti-CD30 antibody linked to MMAE (monomethyl auristatin E), a tubulin polymerisation inhibitor |
| Myelosuppression Risk | Moderate to High — neutropenia is the most frequently reported dose-limiting toxicity; anaemia and thrombocytopenia also observed |
| Emetogenicity Classification | Low to Moderate |
| Monitoring Items | Complete blood count with differential (prior to each cycle), peripheral neuropathy assessment, liver function tests (ALT/AST/bilirubin), renal function, and serum electrolytes |
| Handling Protection | Must be handled in accordance with cytotoxic drug handling regulations; reconstitution should be performed in a biological safety cabinet; appropriate personal protective equipment required |

---

## Safety Considerations

Please refer to the package insert for safety information. No Singapore-specific package insert data is available as the drug is not currently registered in Singapore. The internationally approved prescribing information (FDA/EMA label for Adcetris) should be consulted, with particular attention to peripheral neuropathy (a cumulative dose-dependent toxicity), pulmonary toxicity, and infusion-related reactions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
An ongoing Phase 2 trial (NCT04587687) directly investigates brentuximab vedotin in relapsed/refractory follicular lymphoma, and the CD30-targeting mechanism is biologically plausible in CD30-positive FL subtypes. However, the majority of FL tumours are CD30-negative, and broader application without mandatory biomarker screening carries a high risk of exposing non-responding patients to unnecessary toxicity.

**To proceed, the following is needed:**
- **Mandatory CD30 IHC testing** prior to any treatment consideration — brentuximab vedotin should only be considered in FL patients with confirmed CD30 expression
- **Full MOA and safety documentation** — obtain package insert from FDA/EMA approval for complete warnings, contraindications, and drug interaction profile (currently data gaps DG001 and DG002)
- **Await NCT04587687 results** — this trial (expected completion December 2026) will provide the first FL-specific efficacy and safety data for this combination; no clinical decision should be made without this information
- **Singapore regulatory pathway** — the drug is not registered in Singapore; any use would require a Clinical Trial Certificate, compassionate use application, or Special Access Route via HSA
- **Patient stratification strategy** — define the target FL subgroup (Grade 3B, transformed FL, or CD30 ≥ threshold by IHC) before designing any local feasibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

