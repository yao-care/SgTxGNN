---
layout: default
title: Cabozantinib
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 10
---

# Cabozantinib
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

# Cabozantinib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Cabozantinib (Cabometyx) is an oral multi-kinase inhibitor targeting VEGFR, MET, and AXL, established as a standard-of-care treatment for renal cell carcinoma and other solid tumors.
The TxGNN model predicts it may be effective for **Liposarcoma**, with **1 active Phase 2 clinical trial** and **1 Phase 1 publication** currently supporting this direction.
Evidence is early-stage but mechanistically grounded, warranting dedicated clinical investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Renal cell carcinoma (no Singapore HSA registration data available) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L2 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Cabozantinib is an oral small-molecule tyrosine kinase inhibitor (TKI) that simultaneously inhibits VEGFR1/2/3, MET (hepatocyte growth factor receptor), and AXL — three pathways central to tumor angiogenesis, invasiveness, and acquired resistance to antiangiogenic therapy. This broad multi-target profile has proven effective across multiple cancer types that rely on tumor vasculature for growth and metastatic spread.

Liposarcoma, especially the dedifferentiated subtype (DD-LPS), displays angiogenesis-dependent growth through VEGFR expression, providing a direct mechanistic basis for anti-VEGFR therapy. Beyond angiogenesis, a subset of DD-LPS tumors harbors upregulated MET signaling alongside the characteristic CDK4/MDM2 amplification, creating an additional actionable target for cabozantinib's MET-inhibitory arm. This dual-pathway rationale — anti-angiogenic plus anti-MET — mirrors why cabozantinib outperforms single-pathway VEGFR inhibitors in other solid tumors.

It is important to note the limitations: cabozantinib does not directly inhibit CDK4 or MDM2, the primary oncogenic drivers in most liposarcomas. Sarcomas are also highly heterogeneous tumors, making efficacy prediction more uncertain than in RCC. The current investigational strategy therefore pairs cabozantinib with immune checkpoint inhibitors (ipilimumab + nivolumab) to broaden therapeutic impact, rather than relying on TKI monotherapy alone.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | Active, Not Recruiting | 66 | Randomized trial comparing ipilimumab + nivolumab alone vs. combined with cabozantinib in advanced soft tissue sarcoma (including liposarcoma). Tests whether adding cabozantinib's multi-kinase inhibition to dual immunotherapy improves outcomes. Trial initiated October 2023; expected completion May 2026. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 Prospective | American Journal of Clinical Oncology | Neoadjuvant Phase 1 trial evaluating the safety of concurrent cabozantinib and radiation therapy in extremity soft tissue sarcoma. Addresses longstanding concern that combining cabozantinib with radiation may increase fistula or perforation risk; provides foundational safety data for multimodal sarcoma regimens. |

---

## Singapore Market Information

Cabozantinib is **not registered** with the Health Sciences Authority (HSA) in Singapore. No product authorizations or approved indications are on record.

Any use in Singapore would require access through special compassionate use pathways, clinical trial enrolment, or individual patient import schemes pending future HSA registration.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Multi-kinase inhibitor (VEGFR/MET/AXL; not conventional cytotoxic) |
| Myelosuppression Risk | Low to moderate — thrombocytopenia and neutropenia are reported but not the dominant toxicity class; less severe than conventional chemotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function (ALT/AST/bilirubin), renal function (serum creatinine), thyroid function (TSH), CBC with differential, blood pressure, urine protein/creatinine ratio, electrolytes (calcium, potassium, magnesium) |
| Handling Protection | Standard oral targeted therapy precautions apply; full cytotoxic hazardous drug handling protocols are not universally required, but individual institutional policies should be consulted |

---

## Safety Considerations

Detailed Singapore-specific or TFDA safety data (warnings, contraindications, drug interactions) is not available in the current Evidence Pack.

Please refer to the Cabometyx (cabozantinib) package insert for complete safety information. Key areas of concern documented in international labeling include: hemorrhagic events, gastrointestinal perforations and fistulas, thromboembolic events, hypertension, hepatotoxicity, wound healing complications, and embryo-fetal toxicity.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The TxGNN model assigns a high prediction score (99.83%) and an active Phase 2 randomized trial is currently exploring cabozantinib combined with dual immunotherapy in soft tissue sarcoma; however, the primary oncogenic drivers of liposarcoma (CDK4/MDM2) lie outside cabozantinib's target profile, making efficacy uncertain without dedicated subtype-specific data.

**To proceed, the following is needed:**

- **Primary readout from NCT05836571** — the Phase 2 randomized trial result (expected May 2026) is the critical gating data point before any repurposing decision
- **Biomarker-driven patient selection** — prospective assessment of MET overexpression, AXL upregulation, and VEGFR dependency in liposarcoma tumor biopsies to define the likely responding subpopulation
- **Safety documentation** — full package insert review plus TFDA/HSA regulatory assessment to establish safety monitoring requirements for this new indication
- **Mechanism of action documentation** — formal DrugBank/pharmacology review to support regulatory and clinical development planning (currently a data gap)
- **Singapore access strategy** — given non-marketed status in Singapore, an HSA special access scheme assessment or clinical trial pathway must be established before patient enrolment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

