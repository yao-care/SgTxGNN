---
layout: default
title: Lenvatinib
parent: 僅模型預測 (L5)
nav_order: 581
evidence_level: L5
indication_count: 10
---

# Lenvatinib
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

# Lenvatinib: From Global-Approved Oncology Indications (Not Registered in Singapore) to Liposarcoma

## One-Sentence Summary

Lenvatinib is a multi-target tyrosine kinase inhibitor (VEGFR1–3/FGFR1–4/PDGFRα/KIT/RET) that is **not currently registered in Singapore** (0 local licenses); it is globally approved elsewhere for cancers such as differentiated thyroid cancer, hepatocellular carcinoma, and renal cell carcinoma (in combination regimens). The TxGNN model's top-ranked prediction in this evidence pack is **Liposarcoma**, supported by **1 completed clinical trial** and **4 publications**, representing an early-stage research signal rather than an established indication.

> **Note on data provenance**: the evidence pack's `original_indications` and `taiwan_regulatory.licenses` fields are both empty (Singapore market status = 未上市 / Not Marketed, 0 registrations). The "globally approved" indications referenced above are well-established public drug-label facts for this DrugBank entity (DB09078 = Lenvatinib), not sourced from local Singapore regulatory data, which this pack does not contain.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in local (Singapore) regulatory data — 0 registrations on file. Lenvatinib is globally approved elsewhere for thyroid cancer, hepatocellular carcinoma, and renal cell carcinoma (combination therapy) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L3 |
| Singapore Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data from DrugBank is currently a data gap for this evidence pack. Based on the available evidence, Lenvatinib is a multi-target tyrosine kinase inhibitor with anti-angiogenic activity against VEGFR, FGFR, and PDGFRα — a mechanism already validated in multiple approved oncology indications (e.g., thyroid cancer, RCC, HCC) elsewhere in the world.

The TxGNN signal for liposarcoma is grounded in a specific clinical rationale: lenvatinib's anti-angiogenic/anti-vascular-remodeling activity combined with eribulin's anti-mitotic chemotherapy mechanism has shown synergy in preclinical sarcoma models. This combination was tested directly in advanced adipocytic sarcoma (including liposarcoma) and leiomyosarcoma in a completed Phase Ib/II single-arm trial (LEADER study, NCT03526679, n=30), which reported objective responses.

It is important to note this is combination-therapy evidence (lenvatinib + eribulin), not evidence for lenvatinib monotherapy, and the supporting trial is small and non-randomized. The mechanistic plausibility is reasonable, but the clinical evidence base remains preliminary.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03526679](https://clinicaltrials.gov/study/NCT03526679) | Phase 1/2 | Completed | 30 | Single-arm study of lenvatinib (anti-angiogenic) plus eribulin (anti-mitotic chemotherapy) in inoperable or metastatic adipocytic sarcoma (including liposarcoma) and leiomyosarcoma; assessed safety and efficacy of the combination (LEADER study) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36129471](https://pubmed.ncbi.nlm.nih.gov/36129471/) | 2022 | Trial (Phase 1b/2, single-arm) | Clinical Cancer Research | Primary publication of the LEADER study (NCT03526679); reports safety and efficacy of lenvatinib plus eribulin in advanced liposarcoma and leiomyosarcoma |
| [39103896](https://pubmed.ncbi.nlm.nih.gov/39103896/) | 2024 | Preclinical/Biomarker Study | Experimental Hematology & Oncology | Identifies CDK4 as a prognostic biomarker in soft tissue sarcoma and demonstrates synergistic effect of CDK4 inhibition in dedifferentiated liposarcoma sequential treatment — contextual biology, not lenvatinib-specific |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical Combination Study | Anticancer Research | Eribulin (lenvatinib's combination partner in the LEADER trial) shows broad-spectrum preclinical antitumor activity, including relevance to liposarcoma, when combined with mechanistically different anticancer agents |
| [34326745](https://pubmed.ncbi.nlm.nih.gov/34326745/) | 2021 | Case Report | Case Reports in Oncology | Individualized combination treatment (targeting + surgery + chemotherapy) achieved notable tumor size reduction in a dedifferentiated liposarcoma patient with lung metastasis |

---

## Singapore Market Information

Lenvatinib is currently **not registered** in Singapore — the evidence pack lists 0 authorizations. No product listing, dosage form, or approved indication text is available locally.

---

## Cytotoxicity

Lenvatinib is an antineoplastic agent (multi-target tyrosine kinase inhibitor used across multiple cancer indications, and evaluated here in combination with the chemotherapy agent eribulin for liposarcoma), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor; anti-angiogenic — VEGFR1-3/FGFR1-4/PDGFRα/KIT/RET), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (no toxicity data available in this evidence pack; note that when used in combination with eribulin, the combination partner's own myelosuppression profile — commonly neutropenia — should be anticipated) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(This evidence pack currently has no populated key warnings, contraindications, or drug-interaction data — flagged internally as data gap DG001, "TFDA 仿單警語/禁忌," severity: Blocking.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for the liposarcoma indication rests on a single completed, small (n=30), single-arm Phase Ib/II combination trial (lenvatinib + eribulin) plus supportive preclinical and case-report literature, with no randomized controlled trial in this specific indication — consistent with the assigned Evidence Level L3. This is a plausible research signal but not yet sufficient to proceed with guardrails.

**To proceed, the following is needed:**
- Randomized controlled trial data specifically in liposarcoma / soft tissue sarcoma (current evidence is single-arm only)
- Clarification of lenvatinib's independent contribution versus the eribulin combination partner
- TFDA/HSA package insert warnings and contraindications (currently a **Blocking** data gap — DG001)
- Detailed mechanism-of-action data from DrugBank (currently a **High**-severity data gap — DG002)
- Drug-drug interaction data (current query status: not found)
- A local (Singapore) regulatory pathway assessment, since Lenvatinib currently holds zero registrations in this market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

