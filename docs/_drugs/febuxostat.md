---
layout: default
title: Febuxostat
parent: 僅模型預測 (L5)
nav_order: 414
evidence_level: L5
indication_count: 10
---

# Febuxostat
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

# Febuxostat: From Gout / Hyperuricemia to Renal Hypouricemia

## One-Sentence Summary

Febuxostat is a non-purine selective xanthine oxidase (XO) inhibitor, established in clinical use for the treatment of gout and hyperuricemia.
The TxGNN model predicts it may be effective for **Renal Hypouricemia (hypouricemia, renal)** — a rare inherited urate transport disorder — with **1 clinical trial** and **2 publications** currently supporting this direction.
This represents a paradoxical application: the drug lowers uric acid, yet the target population already has abnormally low serum urate; the therapeutic goal is prevention of exercise-induced acute kidney injury (EIAKI), not further uric acid reduction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gout / Hyperuricemia (XO inhibitor) |
| Predicted New Indication | Renal Hypouricemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Febuxostat is a non-purine selective inhibitor of xanthine oxidoreductase (XOR), the enzyme responsible for the final two steps of purine catabolism — converting hypoxanthine to xanthine, and xanthine to uric acid. Unlike allopurinol, febuxostat inhibits both the oxidized and reduced forms of XOR and does not require metabolic activation. The primary approved use is the chronic management of hyperuricemia in patients with gout.

Renal hypouricemia (RHUC) is caused by loss-of-function mutations in renal urate transporters, most commonly URAT1 (SLC22A12) or GLUT9 (SLC2A9). Patients have very low serum uric acid (<2 mg/dL) but paradoxically high urinary uric acid excretion. The key complication is exercise-induced acute kidney injury (EIAKI): during anaerobic exercise, a surge in hypoxanthine and xanthine is processed by XOR, generating large amounts of reactive oxygen species (ROS) and uric acid within the renal tubules. Because tubular reabsorption of uric acid is absent, supersaturation and ROS-mediated tubular injury can cause acute kidney injury.

The therapeutic rationale for febuxostat in RHUC is therefore not to lower serum uric acid further, but to reduce intratubular XOR activity and the resulting ROS burst during exercise. By suppressing XOR upstream, febuxostat may prevent the oxidative insult that triggers EIAKI. One case report (PMID 36754409) describes this hypothesis in a 16-year-old athlete with familial RHUC and recurrent EIAKI where standard hydration prophylaxis had failed, proposing febuxostat as a preventive strategy. This mechanistic rationale is biologically coherent, though it remains largely hypothesis-driven with very limited clinical validation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Prospective controlled study examining the effect of uric acid control on stone recurrence and renal function in patients with hyperuricemia-related calculi. Indirectly relevant to the renal hypouricemia context; Phase 4 indicates prior safety data, but unknown status precludes efficacy conclusions. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Review / Hypothesis | Internal Medicine (Tokyo) | Case of 16-year-old football player with familial RHUC (URAT1 compound heterozygous mutations) and recurrent EIAKI refractory to hydration prophylaxis; proposes non-purine selective XOR inhibitors (including febuxostat) as a preventive strategy by reducing intratubular ROS generation during exercise. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia for rheumatologists covering etiology, classification, and clinical complications including EIAKI; provides foundational clinical context for the renal hypouricemia indication but does not specifically evaluate febuxostat. |

---

## Singapore Market Information

Febuxostat is currently **not registered** in Singapore. No product authorizations are on record.

> Note: Febuxostat (e.g., Adenuric®, Uloric®) is approved in the EU, US, Japan, and Taiwan for gout and hyperuricemia, but no Singapore Health Sciences Authority (HSA) registration data was retrieved for this candidate.

---

## Safety Considerations

Detailed package insert warnings, contraindications, and drug interaction data were not available in the current evidence pack.

> Please refer to the approved package insert (EU SmPC for Adenuric® or FDA label for Uloric®) for full safety information, including the FDA black box warning regarding cardiovascular risk (increased risk of cardiovascular death observed in the CARES trial vs. allopurinol).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic hypothesis for febuxostat in renal hypouricemia is biologically plausible and internally consistent, but the current evidence base consists of a single hypothesis-level case report and one narrative review — neither constitutes clinical efficacy data. The Phase 4 trial identified (NCT04398251) addresses hyperuricemia with renal calculi rather than RHUC directly, and its unknown status means results are inaccessible. Furthermore, febuxostat is not registered in Singapore, and no local safety data exist.

**To proceed, the following is needed:**

- **Mechanistic validation**: Prospective pharmacodynamic study in RHUC patients measuring intratubular ROS, post-exercise serum creatinine, and urinary biomarkers (NGAL, KIM-1) before and after febuxostat prophylaxis
- **Safety profile confirmation**: Review of febuxostat cardiovascular risk data in the context of young athletic patients (the primary RHUC-affected population), given the FDA cardiovascular warning
- **Singapore regulatory pathway**: As febuxostat is unregistered in Singapore, a Health Products Regulation Group (HPRG) compassionate use or clinical trial authorization would be required for any local investigation
- **Rare disease network engagement**: Given the ultra-rare nature of RHUC (~1/1,000,000), international collaboration through ORPHA networks or the Japanese RHUC registry is essential to reach sufficient patient numbers for any formal study
- **Allopurinol comparison data**: Allopurinol has been used anecdotally in RHUC-EIAKI; a head-to-head comparison justifying febuxostat's additional cost/risk would strengthen the clinical rationale

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require prospective clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

