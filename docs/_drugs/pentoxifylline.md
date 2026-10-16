---
layout: default
title: Pentoxifylline
parent: High Evidence (L1-L2)
nav_order: 777
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Pentoxifylline: predicted new indication Ischemic disease (evidence level L2). Approved use: Peripheral vascular disease, intermittent claudication…"
monitor_inn: "Pentoxifylline"
predicted_indications: ["ischemic disease", "intracranial arteriosclerosis", "vascular ectasia", "Monckeberg arteriosclerosis", "angiodysplasia", "priapism", "venous thromboembolism", "fibrocartilaginous embolism", "non-inflammatory vasculopathy", "congenital renal artery stenosis"]
---

# Pentoxifylline
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Pentoxifylline: From Peripheral Vascular Disease to Ischemic Disease

## One-Sentence Summary

Pentoxifylline is a hemorheologic agent originally used to treat peripheral vascular disease and intermittent claudication.
The TxGNN model predicts it may be effective for **ischemic disease**,
with **4 clinical trials** (1 completed Phase 2/3 pilot study) and **20 publications** currently supporting this direction, although most of the evidence is indirect or preclinical.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peripheral vascular disease, intermittent claudication, peripheral arterial disease (the Singapore licence has no indication text on file) |
| Predicted New Indication | Ischemic disease |
| TxGNN Prediction Score | 98.98% |
| Evidence Level | L2 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on published literature, pentoxifylline is a methylxanthine hemorheologic agent and non-selective phosphodiesterase inhibitor. It lowers blood viscosity, improves red blood cell deformability, reduces platelet aggregation, and suppresses TNF-alpha.

Its original indication, peripheral arterial disease, is itself a form of limb ischemia. These effects target reduced microvascular perfusion and inflammation, which are shared features of ischemia in other organs. Early clinical studies extend this rationale to acute coronary syndrome (endothelial dysfunction) and to cognitive impairment after ischemic stroke. Preclinical work also shows protection of ischemic white matter.

Note that "ischemic disease" is a broad category. The supporting studies cover different organs and mostly use surrogate endpoints, so the prediction should be read as a general direction rather than proof of efficacy in a specific condition.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04367935](https://clinicaltrials.gov/study/NCT04367935) | Phase 2/3 | Completed | 43 | Pilot study of endothelial function and oxidative stress biomarkers in acute coronary syndrome |
| [NCT06344390](https://clinicaltrials.gov/study/NCT06344390) | Phase 1/2 | Unknown | 200 | Cognitive impairment after ischemic stroke; examines brain electrical activity and metabolism |
| [NCT01625845](https://clinicaltrials.gov/study/NCT01625845) | Phase 2 | Completed | 36 | Anti-inflammatory approach to late-life depression and coronary artery disease risk; ischemia is a secondary focus |
| [NCT07088328](https://clinicaltrials.gov/study/NCT07088328) | Not applicable | Not yet recruiting | 30 | Nephroprotection after perinatal asphyxia in neonates; only loosely related |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3308412](https://pubmed.ncbi.nlm.nih.gov/3308412/) | 1987 | Review | Drugs | Pentoxifylline improves red cell deformability and reduces viscosity and platelet aggregation; used in peripheral and cerebrovascular disease |
| [11728242](https://pubmed.ncbi.nlm.nih.gov/11728242/) | 2000 | Review | Heart Disease | Pentoxifylline and cilostazol are available for symptomatic treatment of intermittent claudication |
| [35642056](https://pubmed.ncbi.nlm.nih.gov/35642056/) | 2022 | Preclinical | J Neuroinflammation | Protects ischemic white matter via Mertk-mediated myelin clearance in a vascular dementia model |
| [24143911](https://pubmed.ncbi.nlm.nih.gov/24143911/) | 2014 | Review | J Invest Surg | Reviews pentoxifylline in liver ischemia and reperfusion, including its TNF-alpha inhibition |
| [25361018](https://pubmed.ncbi.nlm.nih.gov/25361018/) | 2014 | Preclinical | J Invest Surg | Pentoxifylline compared with tadalafil in a rat model of ischemic colitis |
| [25518035](https://pubmed.ncbi.nlm.nih.gov/25518035/) | 2014 | Preclinical | Clinics (Sao Paulo) | Vardenafil and pentoxifylline tested in a rat model of ischemic colitis |
| [22289998](https://pubmed.ncbi.nlm.nih.gov/22289998/) | 2011 | Preclinical | Ulus Travma Acil Cerrahi Derg | Effect of pentoxifylline and vinpocetine on healing of ischemic colon anastomosis |
| [32364620](https://pubmed.ncbi.nlm.nih.gov/32364620/) | 2020 | Review | Cochrane Database Syst Rev | Pharmacological treatments for Buerger's disease (an ischemic vascular condition) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10727P | TRENLIN 400 SR TABLET 400 mg (Duopharma Manufacturing (Bangi) Sdn. Bhd.) | Film-coated tablet | Not specified in the registration record |

## Safety Considerations

- **Contraindications (from knowledge graph, not label text)**: kidney disease, pyoureter, blood coagulation disease.
- **Drug Interactions**: 100 interactions were identified, and the 20 reviewed were all rated Moderate. Main groups:
  - Antidiabetic agents, which may raise hypoglycaemia risk: insulins (aspart, degludec, detemir, glargine, glulisine, human), sulfonylureas (chlorpropamide, glimepiride, glipizide, glyburide, acetohexamide), and glinides (repaglinide, nateglinide).
  - Acetylsalicylic acid, which has antiplatelet effects and may add to bleeding risk.
  - Cimetidine, obeticholic acid, and mannitol.
- **Bleeding risk**: Pentoxifylline's antiplatelet and fibrinolytic effects may raise bleeding risk in bleeding-prone conditions. A case report of pentoxifylline-induced thrombocytopenia has also been published.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Pentoxifylline is already marketed in Singapore and has a plausible mechanism for ischemic conditions. One completed Phase 2/3 pilot study (n=43) supports the direction, but it is small and uses a surrogate endpoint. The remaining trials are early-phase, unknown-status, or only indirectly related. The evidence supports further research rather than clinical adoption.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Singapore regulator, which are currently missing and block safety screening
- Detailed mechanism of action data
- A narrower target indication (for example, coronary or cerebral ischemia) with larger randomized trials and clinical endpoints
- A bleeding and glycaemic monitoring plan for patients on antiplatelets, anticoagulants, or antidiabetic drugs, and for those with kidney disease or coagulation disorders
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

