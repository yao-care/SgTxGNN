---
layout: default
title: Ticagrelor
parent: Low Evidence (L5)
nav_order: 988
evidence_level: L5
indication_count: 10
---

# Ticagrelor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Ticagrelor: From Acute Coronary Syndrome to Intracranial Arteriosclerosis

## One-Sentence Summary

Ticagrelor is an oral antiplatelet drug (a P2Y12 inhibitor) originally used for acute coronary syndrome and peripheral arterial disease.
The TxGNN model predicts it may be effective for **intracranial arteriosclerosis**,
with **2 clinical trials** and **2 publications** currently supporting this direction. Most of this evidence is indirect, and the largest trial has no results yet.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome, peripheral vascular disease, intermittent claudication, peripheral arterial disease (the Singapore licence records contain no approved-indication text) |
| Predicted New Indication | Intracranial arteriosclerosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 (rated on the data compiled for this report; the Phase 3 trial for this specific indication has not yet reported results, so direct evidence is closer to L2–L3) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, ticagrelor is a reversible P2Y12 platelet receptor inhibitor. It reduces platelet aggregation and thrombosis, and its efficacy in acute coronary syndrome is established.

Symptomatic intracranial atherosclerotic stenosis shares the same underlying biology as coronary disease. Platelet-driven thrombosis and artery-to-artery embolism can cause recurrent stroke, so P2Y12 inhibition is mechanistically plausible. The direct clinical evidence is still limited. The CAPTIVA trial compares ticagrelor, rivaroxaban and clopidogrel strategies but has not reported results. The ticagrelor-versus-clopidogrel stroke/TIA data (PMID 34708996) come from patients carrying CYP2C19 loss-of-function alleles, not specifically from intracranial stenosis.

The same data also include a broader "ischemic disease" prediction. It is supported by many large cardiovascular trials, but it largely overlaps with ticagrelor's existing coronary indication, so repurposing novelty is limited.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Phase 3 | Active, not recruiting | 1683 | CAPTIVA: tests whether rivaroxaban, ticagrelor or both are superior to clopidogrel for lowering 1-year ischemic stroke, intracerebral hemorrhage or vascular death in intracranial atherostenosis. No results yet. |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | N/A | Recruiting | 100 | Pilot trial of genotype-guided P2Y12 inhibitor selection (including ticagrelor) versus clopidogrel in symptomatic intracranial atherosclerotic disease. Limited power. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohort | J Neurointerv Surg | Experience with ticagrelor 60 mg twice daily plus aspirin, compared with aspirin plus clopidogrel, for intracranial stenting |
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | Review (trial design) | Int J Stroke | Design and early progress of CAPTIVA, comparing dual antithrombotic regimens with clopidogrel plus aspirin in symptomatic intracranial stenosis |

Related stroke/TIA evidence from outside this specific indication: the CHANCE-2 trial in CYP2C19 loss-of-function carriers (PMID 34708996) compared ticagrelor with clopidogrel.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15294P | BRILINTA TABLET 60 MG | Film-coated tablet | Not recorded |
| SIN17211P | TICASPAN 90 FILM-COATED TABLETS 90MG | Film-coated tablet | Not recorded |
| SIN14120P | Brilinta Tablet 90 mg | Film-coated tablet | Not recorded |

All three licences are valid single-ingredient oral products.

---

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not label text)**: liver failure, liver disease, gallbladder disease, intracranial hemorrhage. The last is especially relevant to intracranial disease, and CAPTIVA includes intracerebral hemorrhage as an endpoint.
- **Drug Interactions**: 100 interactions were identified. Examples:
  - **Major**: clarithromycin
  - **Moderate**: aspirin (acetylsalicylic acid), morphine, simvastatin, dexamethasone, budesonide, aprepitant, miconazole, saxagliptin
- **Bleeding risk**: antiplatelet therapy, especially combined with aspirin or anticoagulants, increases bleeding risk. Several of the compiled studies focus on bleeding reduction strategies.

Package insert warnings were not available in the data compiled for this report. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ticagrelor is already marketed in Singapore, and its mechanism fits intracranial atherosclerosis. The key Phase 3 trial (CAPTIVA, n=1683) has not reported results, and the other supporting evidence is indirect or small. The risk of intracranial hemorrhage requires careful patient selection and monitoring.

**To proceed, the following is needed:**
- CAPTIVA results, to confirm whether ticagrelor-containing regimens beat clopidogrel
- HSA package insert warnings and contraindications (currently missing)
- Mechanism of action data from DrugBank
- A bleeding-risk management plan, especially for patients with prior intracranial hemorrhage, liver disease, or concurrent strong CYP3A inhibitors such as clarithromycin
- Confirmation of the approved indications for the three Singapore licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

