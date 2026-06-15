---
layout: default
title: Daratumumab
parent: 僅模型預測 (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
---

# Daratumumab
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

# Daratumumab: From Multiple Myeloma to Indolent Plasma Cell Myeloma

## One-Sentence Summary

Daratumumab (Darzalex®) is an anti-CD38 monoclonal antibody with established global approval for multiple myeloma across multiple treatment lines, though it is currently not registered in Singapore.
The TxGNN model predicts it may be effective for **Indolent Plasma Cell Myeloma** (smouldering multiple myeloma), with **1 clinical trial** and **5 publications** currently supporting this direction — a biologically plausible extension of its existing oncological indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple myeloma (global approval; not registered in Singapore) |
| Predicted New Indication | Indolent Plasma Cell Myeloma |
| TxGNN Prediction Score | 98.13% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacological knowledge, Daratumumab is a fully human IgG1κ monoclonal antibody targeting CD38 — a transmembrane glycoprotein constitutively overexpressed on the surface of clonal plasma cells. It kills malignant cells through multiple immune-mediated mechanisms: complement-dependent cytotoxicity (CDC), antibody-dependent cellular cytotoxicity (ADCC), antibody-dependent cellular phagocytosis (ADCP), and direct cross-linking-induced apoptosis. A 2017 mechanistic study (PMID 28915615) specifically confirmed CD38 expression throughout the myeloma bone niche, providing a direct rationale for use across the full plasma cell dyscrasia spectrum.

Indolent plasma cell myeloma — clinically synonymous with smouldering multiple myeloma (SMM) — is a premalignant precursor stage defined by elevated clonal plasma cells and M-protein without end-organ damage. Because SMM plasma cells express CD38 at levels comparable to active myeloma cells, Daratumumab's mechanism is directly applicable. The fundamental question is not biological plausibility but clinical timing: whether early CD38-targeted intervention prevents irreversible end-organ damage (renal failure, bone destruction, hypercalcaemia) associated with progression to active disease.

This scientific rationale is reflected in the emerging clinical literature. A landmark 2026 review in *Nature Reviews Clinical Oncology* (PMID 41571958) discusses the therapeutic shift toward early intervention in SMM, positioning anti-CD38 therapy as a central strategy. Externally, the Phase 3 AQUILA trial (NCT03301220, not yet captured in this Evidence Pack) demonstrated that subcutaneous daratumumab significantly delayed progression from high-risk SMM to active myeloma, reinforcing the TxGNN prediction with high-level clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04136756](https://clinicaltrials.gov/study/NCT04136756) | Phase 1 | Completed | 30 | Dose escalation of NKTR-255 (IL-15 receptor agonist) as monotherapy or in doublet with daratumumab SC (DARZALEX FASPRO™) in relapsed/refractory haematological malignancies including myeloma; evaluated safety and recommended Phase 2 dose of the combination |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41571958](https://pubmed.ncbi.nlm.nih.gov/41571958/) | 2026 | Review | Nature Reviews Clinical Oncology | Comprehensive review of SMM diagnosis using 2014 IMWG SLiM-CRAB criteria, risk stratification, and management; positions early anti-CD38 intervention as an emerging standard approach to prevent irreversible morbidity |
| [28915615](https://pubmed.ncbi.nlm.nih.gov/28915615/) | 2017 | Mechanistic Study | Oncotarget | Defines CD38 expression by flow cytometry and immunohistochemistry across the myeloma bone niche including indolent disease; establishes mechanistic basis for daratumumab use and its potential to inhibit osteoclast formation |
| [40257478](https://pubmed.ncbi.nlm.nih.gov/40257478/) | 2025 | Case Report | Annals of Hematology | Rapid-onset ulceronecrotic leukocytoclastic vasculitis as a rare paraneoplastic initial manifestation of smouldering IgG kappa myeloma; illustrates systemic inflammatory consequences and the clinical urgency of early identification |
| [32736600](https://pubmed.ncbi.nlm.nih.gov/32736600/) | 2020 | Case Report | BMC Gastroenterology | Disseminated crystal storing histiocytosis secondary to indolent multiple myeloma presenting as colonic mass; highlights systemic morbidity of untreated indolent plasma cell disorders and the need for effective early-stage therapy |
| [34514307](https://pubmed.ncbi.nlm.nih.gov/34514307/) | 2021 | Case Report | European Heart Journal Case Reports | Concomitant aortic valve papillary fibroelastoma and cardiac AL amyloidosis; illustrates the life-threatening cardiac complications arising from plasma cell dyscrasias and the importance of plasma cell-directed therapy |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy — fully human anti-CD38 IgG1κ monoclonal antibody; not a conventional cytotoxic agent |
| Myelosuppression Risk | Moderate — anaemia, neutropenia, and thrombocytopenia are reported adverse effects, occurring more frequently in combination regimens (e.g., with bortezomib, lenalidomide, or dexamethasone) than with daratumumab monotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | Complete blood count (CBC) with differential; serum protein electrophoresis (distinguish therapeutic antibody from M-protein); hepatitis B virus serology before initiating treatment; infusion reaction monitoring during and after each administration |
| Handling Protection | Standard biologic/monoclonal antibody handling precautions apply; does not require hazardous cytotoxic chemotherapy handling protocols (non-alkylating, non-DNA damaging) |

---

## Safety Considerations

Full Singapore HSA / TFDA prescribing information was not available in the current Evidence Pack. Pending retrieval of the complete package insert, the following clinically important areas should be reviewed before use:

- **Infusion-related reactions**: Reported in approximately 40% of patients, predominantly with the first infusion; premedication with antihistamines, antipyretics, and corticosteroids is standard
- **Immunosuppression and infection risk**: Daratumumab depletes CD38⁺ natural killer cells and regulatory T cells; monitor for opportunistic infections and consider antiviral prophylaxis
- **Interference with blood bank testing**: CD38 is expressed on red blood cells; daratumumab causes pan-agglutination in indirect antiglobulin tests, potentially masking alloantibodies — blood bank must be notified prior to transfusion
- **Hypogammaglobulinaemia**: Cumulative immunoglobulin depletion with prolonged use; consider immunoglobulin replacement in recurrent infections

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The 98.13% TxGNN prediction score is strongly supported by direct biological plausibility — indolent plasma cell myeloma shares the identical CD38-expressing plasma cell target as active myeloma, and the mechanistic literature confirms this. A 2026 *Nature Reviews* article and the externally known Phase 3 AQUILA trial data collectively elevate the evidence quality for this indication well beyond the L3 designation captured in this Evidence Pack alone.

**To proceed, the following is needed:**
- Retrieve and parse the full Singapore HSA (or TFDA) package insert to complete the mandatory safety evaluation (DG001 — currently Blocking severity)
- Supplement the Evidence Pack with the AQUILA Phase 3 trial (NCT03301220): daratumumab SC in high-risk SMM — this is the pivotal dataset missing from the current evidence collection
- Obtain DrugBank MOA data to formalise the mechanistic rationale section (DG002 — currently High severity)
- Clarify target patient subgroup: high-risk SMM (as per AQUILA eligibility) vs. low-risk/standard-risk SMM, where the benefit-risk ratio differs substantially
- Assess Singapore regulatory pathway: given non-registration status (0 licences), evaluate whether a compassionate use, clinical trial access, or full new drug application approach is most appropriate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

