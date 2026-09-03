---
layout: default
title: Pentoxifylline
parent: 僅模型預測 (L5)
nav_order: 768
evidence_level: L5
indication_count: 10
---

# Pentoxifylline
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

# Pentoxifylline: From Intermittent Claudication to Ischemic Disease

## One-Sentence Summary

Pentoxifylline is a methylxanthine-derivative haemorheologic agent; the evidence pack does not contain a Singapore-registered indication (the drug is not currently marketed locally), but the supporting literature identifies its historical use for intermittent claudication/peripheral arterial disease and cerebrovascular disease.
The TxGNN model predicts it may be effective for **Ischemic Disease**, with **8 clinical trials** and **19 publications** currently supporting this direction, though "ischemic disease" is a broad category spanning peripheral, cerebral, renal, and cardiac subtypes.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in Singapore regulatory data (drug not marketed locally); literature identifies intermittent claudication / peripheral arterial disease and cerebrovascular disease as historical indications |
| Predicted New Indication | Ischemic Disease |
| TxGNN Prediction Score | 98.98% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank (flagged as a data gap). Based on the supporting literature in this evidence pack, pentoxifylline is a non-selective phosphodiesterase inhibitor that increases red blood cell deformability, reduces blood/plasma viscosity, inhibits platelet aggregation, and suppresses pro-inflammatory cytokines such as TNF-α — collectively improving microcirculation and tissue perfusion.

These haemorheologic and anti-inflammatory properties map directly onto the pathophysiology of ischemic disease, where impaired blood flow and microvascular dysfunction are central. The literature base already documents pentoxifylline's use across multiple ischemic subtypes: peripheral vascular disease/intermittent claudication (its original registered use since 1974), cerebrovascular insufficiency and vascular dementia, liver and intestinal ischemia-reperfusion injury, and ischemic colitis.

The main caveat is that "ischemic disease" as predicted by TxGNN is an extremely broad disease category. The mechanism is plausible across organ systems, but clinical actionability requires narrowing to a specific subtype (e.g., peripheral arterial ischemia, post-stroke ischemia, or acute coronary syndrome) rather than treating "ischemic disease" as a single indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02951299](https://clinicaltrials.gov/study/NCT02951299) | Phase 2/3 | Unknown | 140 | Investigates pentoxifylline for renoprotection after acute kidney injury in critically ill/sepsis patients. Note: registry title field is anomalous (shows PI title, not study title). |
| [NCT01377285](https://clinicaltrials.gov/study/NCT01377285) | Phase 4 | Unknown | 350 | Multicenter RCT of pentoxifylline + valsartan vs. placebo + valsartan for renoprotection and cardiovascular outcomes in CKD stage 3–4 over 3 years. |
| [NCT01625845](https://clinicaltrials.gov/study/NCT01625845) | Phase 2 | Completed | 36 | Pentoxifylline vs. placebo in older primary-care patients with late-life depression (no CVD history); evaluates depressive symptoms and arterial function/coronary calcification risk. |
| [NCT06344390](https://clinicaltrials.gov/study/NCT06344390) | Phase 1/2 | Recruiting | 200 | Pentoxifylline for cognitive impairment after ischemic stroke (PSCIND); assesses cerebral blood flow, blood oxygenation/metabolism, and neuroelectrical signaling. |
| [NCT01469624](https://clinicaltrials.gov/study/NCT01469624) | NA | Unknown | N/A | Evaluates pentoxifylline's protective effect against contrast-induced nephropathy in high-risk patients (CKD, diabetes, CHF, anemia, advanced age). |
| [NCT01718288](https://clinicaltrials.gov/study/NCT01718288) | Phase 4 | Completed | 150 | Optimization of therapy in Fontaine stage IIb severe peripheral ischemia, comparing surgery/endovascular-eligible vs. medical-therapy-only patients on pain-free walking distance. |
| [NCT07088328](https://clinicaltrials.gov/study/NCT07088328) | NA | Not yet recruiting | 30 | RCT of pentoxifylline for nephroprotection after perinatal asphyxia in neonates, using cystatin C, NIRS oxygenation, and renal Doppler. |
| [NCT04367935](https://clinicaltrials.gov/study/NCT04367935) | Phase 2/3 | Completed | 43 | Pilot study of pentoxifylline's effect on endothelial dysfunction and oxidative stress biomarkers in Acute Coronary Syndrome patients. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20799759](https://pubmed.ncbi.nlm.nih.gov/20799759/) | 2010 | Review | Paediatric Drugs | Systematic review of pentoxifylline for sepsis, NEC, and chronic lung disease in preterm neonates. |
| [3308412](https://pubmed.ncbi.nlm.nih.gov/3308412/) | 1987 | Review | Drugs | Classic pharmacodynamic/pharmacokinetic review; documents original use for peripheral vascular disease, cerebrovascular disease, and microcirculatory disorders. |
| [6350013](https://pubmed.ncbi.nlm.nih.gov/6350013/) | 1983 | Review | European Neurology | Reviews pentoxifylline's effect on red-cell deformability and regional blood flow in cerebrovascular disease. |
| [24143911](https://pubmed.ncbi.nlm.nih.gov/24143911/) | 2014 | Review | Journal of Investigative Surgery | Reviews pentoxifylline's anti-TNF-α and haemorheological effects in organ ischemia-reperfusion, including liver. |
| [32936393](https://pubmed.ncbi.nlm.nih.gov/32936393/) | 2021 | Review | International Journal of Colorectal Disease | Reviews diagnostic methods and drug therapies (including pentoxifylline) for ischemic colitis. |
| [34647189](https://pubmed.ncbi.nlm.nih.gov/34647189/) | 2021 | Review | Diabetes Therapy | Reviews pentoxifylline's effects on diabetes complications including peripheral arterial disease, ischemic heart disease, and cerebrovascular disease. |
| [33553684](https://pubmed.ncbi.nlm.nih.gov/33553684/) | 2021 | Preclinical/Mechanistic | Biochemistry and Biophysics Reports | qRT-PCR study of PAG1/miR-1206/SNHG14 gene expression modulation by pentoxifylline in cardiac ischemia-reperfusion. |
| [2393054](https://pubmed.ncbi.nlm.nih.gov/2393054/) | 1990 | Cohort | American Journal of Surgery | Pre/post study of 101 patients on oral pentoxifylline for peripheral vascular disease across disease severity stages, using ankle/arm Doppler indices. |
| [8824491](https://pubmed.ncbi.nlm.nih.gov/8824491/) | 1996 | Preclinical | Transplantation | Rat model showing pentoxifylline protects against cyclosporine nephrotoxicity in the ischemic kidney. |
| [35642056](https://pubmed.ncbi.nlm.nih.gov/35642056/) | 2022 | Preclinical | Journal of Neuroinflammation | Pentoxifylline alleviates ischemic white matter injury via Mertk-mediated myelin clearance in a vascular dementia model. |

---

## Singapore Market Information

Pentoxifylline is not currently registered or marketed in Singapore (0 registrations on file in this evidence pack).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted "ischemic disease" indication is supported by 8 clinical trials (including completed Phase 2/3 and Phase 4 studies, e.g., NCT04367935 in ACS and NCT01718288 in severe peripheral ischemia) and 19 publications spanning cerebrovascular, hepatic, intestinal, renal, and peripheral ischemic conditions — meeting the L2 evidence bar. However, the disease label itself is too broad for direct clinical application and must be narrowed to a specific subtype before further development.

**To proceed, the following is needed:**
- Singapore/local product label — warnings and contraindications (flagged as a **Blocking** data gap; currently unavailable, blocks entry into safety pre-assessment)
- Formal DrugBank mechanism-of-action data (flagged as a **High**-severity data gap)
- A resolved drug-drug interaction profile (current DDI query returned "not found")
- Selection of a specific ischemic-disease subtype (e.g., peripheral arterial ischemia or post-stroke cognitive impairment) to define a testable clinical protocol
- Assessment of the registration/import pathway, since the drug is not currently marketed in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

