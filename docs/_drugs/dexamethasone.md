---
layout: default
title: Dexamethasone
parent: 僅模型預測 (L5)
nav_order: 233
evidence_level: L5
indication_count: 10
---

# Dexamethasone
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

# Dexamethasone: From Inflammatory & Autoimmune Conditions to Alopecia Areata

## One-Sentence Summary

Dexamethasone is a potent synthetic glucocorticoid widely used as an anti-inflammatory and immunosuppressive agent across a broad range of clinical conditions — from allergic reactions and autoimmune diseases to supportive care in oncology — though no Singapore HSA registration is currently on file.
The TxGNN model predicts it may be effective for **Alopecia Areata (AA)**, with **no directly relevant registered clinical trials** but **20 publications** (including 1 RCT and multiple prospective cohorts) specifically examining Dexamethasone in AA treatment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anti-inflammatory and immunosuppressive therapy (no Singapore HSA registration on file) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current structured record. Based on well-established pharmacology, Dexamethasone is a synthetic glucocorticoid that binds the glucocorticoid receptor (GR-α) and broadly suppresses immune activation — inhibiting T cell proliferation, downregulating key pro-inflammatory cytokines (IL-2, IFN-γ, TNF-α), and suppressing antigen presentation by dendritic cells.

Alopecia Areata is a CD8+ T-cell-mediated autoimmune disease in which cytotoxic T lymphocytes breach the immune privilege of the hair follicle, causing non-scarring hair loss. The pathogenic cytokine signature (IFN-γ/IL-2-dominant) maps directly onto Dexamethasone's inhibitory targets, making the mechanistic rationale for use in AA biologically coherent and well-grounded.

In clinical practice, Dexamethasone has been deployed specifically in an "oral mini-pulse" (OMP) regimen for AA — typically 5 mg on two consecutive days per week — an intermittent schedule deliberately designed to deliver meaningful immunosuppression while minimising HPA axis suppression and the systemic adverse effects associated with daily corticosteroid use. This positions Dexamethasone as a practical, accessible alternative particularly in settings where JAK inhibitors (baricitinib, ritlecitinib) are unavailable, unaffordable, or contraindicated.

---

## Clinical Trial Evidence

> ⚠️ **Important caveat**: All 13 trials retrieved from ClinicalTrials.gov involve Dexamethasone as a supportive or adjunct agent in **oncology settings** (anti-emesis, myeloma backbone, dexamethasone suppression testing) — none were specifically designed to investigate Dexamethasone for Alopecia Areata. The table below reflects the most informative of these for context; they do not constitute AA-targeted evidence.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02288078](https://clinicaltrials.gov/study/NCT02288078) | Phase 2 | Unknown | 74 | Prophylactic dexamethasone for fatigue/malaise from regorafenib in metastatic colorectal cancer — steroid used as supportive care only |
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | Completed | 380 | Abnormal steroid metabolome (MACS) and bone strength/body composition — relates to glucocorticoid physiology broadly, not AA |
| [NCT02685826](https://clinicaltrials.gov/study/NCT02685826) | Phase 1/2 | Completed | 56 | Durvalumab + lenalidomide ± dexamethasone in newly diagnosed multiple myeloma — dexamethasone as combination backbone |

No dedicated clinical trials registered on ClinicalTrials.gov specifically for Dexamethasone in Alopecia Areata were identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | RCT | Dermatologic Therapy | Randomized open-label trial comparing dexamethasone OMP vs DPCP contact sensitization in severe pediatric AA (n=30 children <18 y); evaluates efficacy and safety of both modalities in non-progressive severe AA |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | Systematic Review + NMA | Archives of Dermatological Research | Network meta-analysis comparing systemic steroids, oral JAK inhibitors, and contact immunotherapy for severe AA (SALT ≥50%); provides head-to-head efficacy and safety ranking across treatment classes |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | Prospective Cohort | Journal of Clinical Medicine | Real-world evidence on dexamethasone mini-pulse OMP in AA; assesses treatment effectiveness, adverse event profile, and predictors of successful response in a clinical practice setting |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | Case Series + Focused Review | Journal of Dermatological Treatment | Documents durable remission of severe AA with dexamethasone OMP as an alternative when JAK inhibitors are contraindicated or inaccessible; includes a literature review of the corticosteroid pulse approach |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | Prospective Cohort | Dermatologic Therapy | Multicentric European study of oral dexamethasone mini-pulse for moderate-to-severe AA, including extensive subtypes (totalis/universalis); evaluates feasibility as a lower-cost alternative to JAK inhibitors |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | Prospective Cohort | Dermatologic Therapy | Compares 1-day vs 3-day IV dexamethasone pulse regimens combined with topical clobetasol in severe pediatric AA (n=73, age 1–18 y); >50% scalp regrowth used as primary endpoint |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review / Dosing Guideline | Pediatric Dermatology | Systematic review of pulse-dose corticosteroid therapy (PDCT) dosing regimens in children with AA; evaluates reported schedules, side effects, and current evidence gaps |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Prospective Cohort (Long-term) | Dermatologic Therapy | Long-term follow-up (median 96 months) of oral dexamethasone pulse + topical corticosteroid in 65 children/adolescents with severe AA (>30% scalp involvement); reports sustained response and relapse rates |
| [16707886](https://pubmed.ncbi.nlm.nih.gov/16707886/) | 2006 | Prospective Comparative Study | Dermatology (Basel) | Head-to-head comparison of three systemic corticosteroid modalities (including dexamethasone) for extensive AA; reports efficacy, relapse rates, and side-effect profiles across regimens |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | Prospective Observational | Journal of Dermatology | One of the earliest prospective studies of twice-weekly 5 mg dexamethasone oral pulse in 30 patients with widespread AA; evaluates terminal hair regrowth at ≥12 weeks of treatment |

---

## Singapore Market Information

Dexamethasone currently has **no registered products** with Singapore's HSA (Health Sciences Authority). No license authorization data is available for this analysis. Formal registration would be required before any clinical use pathway can be established.

---

## Safety Considerations

Please refer to the package insert for safety information.

> As a synthetic glucocorticoid, Dexamethasone carries well-established class-level risks that are particularly relevant to the intended mini-pulse dosing schedule in AA. These include HPA axis suppression (dose- and duration-dependent), increased susceptibility to infections, osteoporosis and avascular necrosis with prolonged use, and metabolic effects such as hyperglycaemia, weight gain, and dyslipidaemia. Growth suppression is a specific concern in paediatric patients — a population with substantial representation in the existing evidence base. The mini-pulse schedule (2 consecutive days per week) is expressly designed to reduce these risks compared to continuous daily dosing.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic fit between Dexamethasone's glucocorticoid immunosuppression and the CD8+ T-cell-driven pathogenesis of Alopecia Areata is well-established. The evidence base includes 1 published RCT (severe paediatric AA), a 2024 systematic review and network meta-analysis positioning systemic steroids within the treatment landscape, and at least 5 prospective cohort studies specifically using Dexamethasone OMP in AA — collectively supporting its status as a clinically validated off-label option, particularly where JAK inhibitors are inaccessible or contraindicated.

**To proceed, the following is needed:**
- **Singapore registration pathway**: Dexamethasone has 0 HSA-licensed products on file; a registration or import/supply strategy must be established before clinical use
- **Package insert and safety data**: Full TFDA/HSA-compliant warnings, contraindications, and DDI profile are currently flagged as data gaps — required before formal S1 safety evaluation can be completed
- **Structured dosing protocol**: The mini-pulse regimen (dose, frequency, duration, tapering schedule) should be formalised for the Singapore patient population, with separate considerations for adult and paediatric cases
- **Safety monitoring plan**: HPA axis function, fasting glucose, bone density (for long-term use), and growth parameters (paediatric patients) should be defined as mandatory monitoring items
- **Positioning relative to JAK inhibitors**: A clinical decision framework clarifying when Dexamethasone OMP is preferred over, or used alongside, approved AA therapies (baricitinib, ritlecitinib) in the Singapore formulary context

---

*This report is generated for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

