---
layout: default
title: Atezolizumab
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 10
---

# Atezolizumab
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

# Atezolizumab: From Urothelial Carcinoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Atezolizumab (Tecentriq) is an anti-PD-L1 monoclonal antibody globally approved for urothelial carcinoma, non-small cell lung cancer, and several other cancers, though it has no current registrations in Singapore.
The TxGNN model predicts it may be effective for **Prostatic Urethra Urothelial Carcinoma**,
with **2 clinical trials** (including 1 completed Phase 2 study, N=172) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Urothelial carcinoma (globally approved; no Singapore registration on record) |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Atezolizumab is a humanized IgG1 monoclonal antibody that blocks PD-L1 (Programmed Death-Ligand 1), preventing it from binding to its receptors PD-1 and B7.1 on T cells. This blockade reverses T-cell exhaustion and restores anti-tumour immune surveillance. It is globally approved (as Tecentriq, Roche/Genentech) for multiple tumour types — most relevantly, urothelial carcinoma (first-line cisplatin-ineligible and second-line settings) — reflecting its established activity across the urothelial system including bladder, renal pelvis, ureter, and urethra.

Prostatic urethra urothelial carcinoma is anatomically continuous with the bladder and shares the same urothelial cell lineage. Critically, prostatic urethral involvement is a recognised staging and prognostic factor in non-muscle-invasive bladder cancer (NMIBC) trials — meaning patients in existing atezolizumab urothelial studies very likely include cases of prostatic urethral disease. Both locations exhibit similarly high PD-L1 expression rates and tumour mutational burden (TMB), the two key biomarkers that predict response to PD-L1 checkpoint inhibition.

The TxGNN prediction therefore represents a biologically coherent extension of atezolizumab's established urothelial indication to a histologically identical tumour at an anatomically adjacent site, rather than a leap into uncharted territory. The strong mechanistic rationale is further supported by the completed Phase 2 evidence in BCG-unresponsive NMIBC — a patient population where prostatic urethral evaluation is routine clinical practice.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02844816](https://clinicaltrials.gov/study/NCT02844816) | Phase 2 | Completed | 172 | Atezolizumab monotherapy in BCG-unresponsive recurrent/refractory NMIBC. Immunotherapy may enable the immune system to attack cancer and inhibit tumour growth and spread. Prostatic urethral involvement is a standard evaluation in this population, making this the most directly applicable completed trial. |
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1b | Active, Not Recruiting | 914 | Cabozantinib + Atezolizumab dose-escalation in multiple solid tumours explicitly including urothelial carcinoma of the bladder, renal pelvis, ureter, and **urethra**. Primarily a safety/tolerability study; no prostatic urethral sub-analysis, but urethra is named in the study scope. Data still accumulating. |

---

## Literature Evidence

Currently no related literature available specifically for prostatic urethra urothelial carcinoma in combination with atezolizumab.

---

## Singapore Market Information

Atezolizumab currently has **no registered products in Singapore** (0 authorizations on record as of 2026-04-05). A regulatory filing pathway assessment with the Health Sciences Authority (HSA) would be required before any clinical use in Singapore.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted immunotherapy (Anti-PD-L1 monoclonal antibody; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low (immune-mediated haematological events possible but uncommon; far less myelosuppressive than chemotherapy) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function (AST, ALT, bilirubin), renal function, thyroid function (TSH/free T4), fasting blood glucose, and clinical surveillance for immune-related adverse events (irAEs) at every infusion visit |
| Handling Protection | Standard biologic/monoclonal antibody handling protocols apply; dedicated cytotoxic drug handling precautions are not required, but institutional irAE management protocols must be established before initiating treatment |

---

## Safety Considerations

Detailed Singapore-specific warnings and contraindications are not available as atezolizumab holds no local registration. Please refer to the global Tecentriq prescribing information (Roche/Genentech) for comprehensive safety data, which includes:

- **Key Warnings**: Immune-related adverse events (irAEs) including pneumonitis, hepatitis, colitis, endocrinopathies (hypothyroidism, adrenal insufficiency, type 1 diabetes), nephritis, and dermatitis; infusion-related reactions
- **Drug Interactions**: No clinically significant pharmacokinetic interactions identified (monoclonal antibody, not CYP-metabolised); concomitant immunosuppressants may blunt therapeutic effect

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The combination of a completed Phase 2 trial in a closely overlapping urothelial population (BCG-unresponsive NMIBC, N=172), atezolizumab's existing global approval for urothelial carcinoma spanning multiple anatomical sites including the urethra, and a well-established PD-L1–driven mechanistic rationale collectively justify advancing this repurposing hypothesis — provided the evidence gaps below are addressed.

**To proceed, the following is needed:**

- **Sub-group/sub-site analysis**: Request or review prostatic urethral involvement data from NCT02844816 to determine if this cohort had documented prostatic urethral disease and its associated outcomes
- **HSA registration assessment**: Evaluate the pathway for atezolizumab registration in Singapore, potentially leveraging global approvals via abridged or recognition routes
- **Dedicated Phase 2 design**: Plan a prospective study specifically addressing prostatic urethra urothelial carcinoma, potentially as a sub-study within a broader NMIBC or upper-tract urothelial carcinoma trial
- **Biomarker profiling**: Confirm PD-L1 expression, TMB, and MSI status in prostatic urethral tumour specimens to identify the patient population most likely to respond
- **MOA documentation**: Complete the DrugBank API query (DG002) to formalise the mechanism of action record in the evidence pack
- **Safety data for Asian populations**: Review irAE profiles from Asian patient subgroups in existing trials, as immune-related toxicity patterns may differ from Western populations

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All predictions are generated by the TxGNN computational model and must be interpreted within the context of the supporting evidence presented.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

