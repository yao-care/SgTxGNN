---
layout: default
title: Fenofibrate
parent: 僅模型預測 (L5)
nav_order: 418
evidence_level: L5
indication_count: 10
---

# Fenofibrate
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

# Fenofibrate: From Hypertriglyceridemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Fenofibrate is a fibrate-class lipid-lowering drug and PPARα agonist, globally established for the treatment of hypertriglyceridemia and mixed dyslipidemia, though it currently holds no registered products in Singapore.
The TxGNN model predicts it may offer adjunctive benefit in **Homozygous Familial Hypercholesterolemia (HoFH)**,
with **1 clinical trial** and **11 publications** identified in support of this direction — however, none directly evaluate Fenofibrate as the primary treatment agent for this condition.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertriglyceridemia / Mixed Dyslipidemia (globally established; no Singapore HSA registration found) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrievable from DrugBank in this query cycle. Based on well-established pharmacology and the mechanistic information synthesised within this Evidence Pack, Fenofibrate is a fibrate-class drug that functions as a potent agonist of PPARα (peroxisome proliferator-activated receptor alpha). It works primarily by activating lipoprotein lipase (LPL) and suppressing apoC-III synthesis — the endogenous LPL inhibitor — while simultaneously promoting apoA-I gene transcription. The net result is a substantial reduction in triglycerides (40–50%), VLDL clearance improvement, and a modest HDL increase (10–20%). Its direct effect on LDL-cholesterol is comparatively limited, typically in the range of 10–15%.

Homozygous Familial Hypercholesterolemia (HoFH) is a severe monogenic disorder characterised by biallelic mutations in the LDL receptor gene (LDLR), resulting in near-complete or complete inability to clear LDL from circulation. Patients typically present with LDL-C exceeding 500 mg/dL from early childhood, leading to aggressive premature atherosclerosis. The current standard of care centres on maximally tolerated statins, PCSK9 inhibitors, evinacumab, and LDL apheresis — all targeting the LDL axis directly.

The mechanistic overlap between Fenofibrate and HoFH is narrow. Since HoFH's core defect lies entirely in LDL receptor function, and Fenofibrate's principal actions are on the TG/VLDL/HDL axis, it cannot meaningfully address the primary pathology. The only direct HoFH-related clinical observation for Fenofibrate is a single case report within a 1984 case series (PMID 6593751), where one HoFH patient showed the greatest proportional LDL-C fall among type II hyperlipoproteinemia patients. Fenofibrate may carry limited adjunctive value in the subset of HoFH patients who also present with hypertriglyceridaemia (mixed phenotype), but this does not constitute a repurposing opportunity with adequate mechanistic alignment. The TxGNN high prediction score likely reflects network proximity between HoFH disease nodes and Fenofibrate's lipid metabolism targets in the knowledge graph, rather than a strong direct therapeutic match.

---

## Clinical Trial Evidence

The sole clinical trial retrieved is **not a Fenofibrate study**. It is listed here for HoFH disease context only:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label study of alirocumab (PCSK9 inhibitor, 75–150 mg Q2W by body weight) in children and adolescents aged 8–17 years with HoFH. Evaluated LDL-C reduction at weeks 12, 24, and 48. **Study drug is Alirocumab, not Fenofibrate** — included for HoFH disease management background only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Case-series | Pharmacological Research Communications | 22 patients with primary type II hyperlipoproteinemia (13 IIa, 9 IIb) treated with fenofibrate 300 mg/day for 4–12 months. In the FH subgroup, mean LDL-C fell 31%; **the one HoFH patient showed the largest absolute fall in total and LDL cholesterol** — the only direct HoFH-Fenofibrate data point in this dataset |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | PK Study | Pharmacotherapy | Lomitapide PK interaction study with fenofibrate and other lipid-lowering agents (atorvastatin, simvastatin, rosuvastatin, ezetimibe, niacin) in HoFH patients — establishes that fenofibrate co-administration with lomitapide is pharmacokinetically characterised in this population |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Review | Internal Medicine Journal | Liver transplantation for HoFH in the era of emerging therapies; notes that standard lipid-lowering drugs, including fenofibrate, are insufficient for HoFH control alone |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocrine Practice | AACE/ACE dyslipidemia management and cardiovascular prevention guidelines; provides HoFH treatment framework placing fibrates as adjuncts for residual hypertriglyceridaemia only |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Annals of the New York Academy of Sciences | Pharmacologic and surgical treatment of dyslipidaemic children including FH; mentions fenofibrate among agents trialled with variable success across paediatric dyslipidemias |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart Journal | Overview of traditional and novel non-statin lipid-lowering agents; clearly states the primary monotherapy indication for fenofibrate is fasting TG >500 mg/dL to reduce pancreatitis risk; modest cardiovascular event reduction |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart Journal | Discusses LDL-C lowering strategies and PCSK9 inhibitors for severe hypercholesterolaemia; provides current HoFH treatment landscape context |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Review | Pharmacotherapy | Ezetimibe as first selective cholesterol absorption inhibitor; discusses combination approaches for severe hypercholesterolaemia including HoFH scenarios |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Review | Current Atherosclerosis Reports | Dyslipidaemia management in pregnancy, including discussion of fibrates as contraindicated; provides safety context for fenofibrate across special populations |
| [9627539](https://pubmed.ncbi.nlm.nih.gov/9627539/) | 1998 | Review | Canadian Journal of Cardiology | Advances in lipid-lowering therapy with attention to TG-rich lipoproteins as CAD risk factors; fenofibrate positioned within the broader dyslipidaemia management narrative |

---

## Singapore Market Information

Fenofibrate currently has **no registered products** in the Singapore HSA database.

> No authorization records are available for this drug in Singapore. This is notable given Fenofibrate's established global regulatory status (FDA-approved in the US, EMA-approved in Europe under brand names such as TriCor and Lipanthyl). Verification against the current HSA product database is recommended, as the data gap may reflect a registry query limitation rather than true absence of market access.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note**: Safety data including key warnings, contraindications, and drug interaction information could not be retrieved in this query cycle. Fenofibrate is contraindicated in severe hepatic or renal impairment, pre-existing gallbladder disease, and during pregnancy. Clinically significant drug interactions include potentiation of warfarin anticoagulation (INR monitoring required) and increased risk of myopathy when co-administered with statins. These should be verified against the full prescribing information before any clinical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Fenofibrate's primary pharmacological mechanism — PPARα-mediated reduction of triglycerides and VLDL — is mechanistically misaligned with HoFH, a disorder driven entirely by LDL receptor dysfunction and severely elevated LDL-C. The drug is unlikely to provide clinically meaningful benefit as a primary HoFH therapy; its role, if any, is limited to adjunctive management of co-existing hypertriglyceridaemia in a mixed HoFH phenotype. The single direct evidence point (one HoFH patient in a 1984 case series) and the absence of any dedicated Fenofibrate trial in HoFH patients place this at Evidence Level L4, insufficient to support advancement.

**To proceed, the following is needed:**

- Confirm Singapore HSA registration status independently (current data shows 0 registrations, which may reflect a query gap)
- Retrieve complete DrugBank MOA and safety profile data (DG001, DG002 data gaps must be resolved before any safety assessment)
- Define a specific clinical question: is Fenofibrate being evaluated as (a) primary HoFH therapy, or (b) adjunctive therapy for TG management in mixed-phenotype HoFH patients? The latter is more defensible but still requires prospective data
- Assess whether a formal mechanistic study or small case-series in HoFH patients with concurrent hypertriglyceridaemia could generate hypothesis-generating data
- Prioritise higher-evidence predicted indications from this same model output — notably **hyperlipoproteinemia (Rank 2, Evidence Level L1)** and **familial hypercholesterolemia (Rank 3, Evidence Level L3)** — where direct Fenofibrate clinical evidence is substantially stronger and advancement decisions are more actionable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

