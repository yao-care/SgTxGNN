---
layout: default
title: Magnesium Sulfate
parent: 僅模型預測 (L5)
nav_order: 625
evidence_level: L5
indication_count: 10
---

# Magnesium Sulfate
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

# Magnesium Sulfate: From No Registered Indication (Singapore) to Preeclampsia/Eclampsia

## One-Sentence Summary

Magnesium sulfate (DrugBank DB00653) currently has **no marketing authorization** and no recorded approved indication in the Singapore regulatory dataset used for this evaluation. The TxGNN model predicts it may be effective for **Preeclampsia/Eclampsia**, with **50 clinical trials** and **20 publications** currently supporting this direction — notably, this mechanism-disease link already reflects an internationally established standard of care (WHO/ACOG guidelines) rather than a novel discovery.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — drug is not registered/marketed in Singapore (no `approved_indication_text` available) |
| Predicted New Indication | Preeclampsia/Eclampsia |
| TxGNN Prediction Score | 99.9992% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed, formally-sourced mechanism-of-action data for magnesium sulfate is currently a data gap in this evidence pack (DrugBank query returned a match, but MOA text was not populated). However, the model's own repurposing rationale for this specific drug–disease pair provides a clear pharmacological explanation: the magnesium ion (Mg²⁺) acts as an **NMDA receptor antagonist** and **calcium-channel blocker**, which reduces neuronal excitability and relieves cerebral vasospasm and edema. This is the accepted mechanism underlying seizure prevention in preeclampsia/eclampsia.

Importantly, this is not an exploratory or speculative pairing — magnesium sulfate for eclamptic seizure prophylaxis and treatment is already an **internationally established standard of care** under WHO and ACOG guidelines. The TxGNN prediction here effectively reconfirms decades of accumulated clinical evidence rather than proposing a genuinely new therapeutic hypothesis, which is why the score is extremely high (99.9992%) and is backed by dozens of completed randomized trials.

The key open question for this specific evaluation is regulatory, not scientific: magnesium sulfate has **zero registered licenses and is not marketed in Singapore** under the data reviewed here. Before any local claims or guardrailed use can be recommended, the regulatory pathway, local prescribing information, and safety labeling need to be established or sourced from the relevant Singapore health authority.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00004399](https://clinicaltrials.gov/study/NCT00004399) | N/A | Completed | 2000 | Compared nimodipine vs. magnesium sulfate for preventing eclamptic seizures in severe preeclampsia |
| [NCT01492608](https://clinicaltrials.gov/study/NCT01492608) | Phase 3 | Completed | 560 | Antenatal MgSO4 for fetal neuroprotection — assessed reduction in cerebral palsy/death risk in preterm infants (MASP-STUDY) |
| [NCT02317146](https://clinicaltrials.gov/study/NCT02317146) | Phase 2/3 | Completed | 280 | Evaluated shortened (6h) vs. standard (24h) postpartum MgSO4 duration in severe preeclampsia |
| [NCT02307201](https://clinicaltrials.gov/study/NCT02307201) | Phase 2/3 | Completed | 1114 | Multicenter RCT on postpartum MgSO4 duration after ≥8h of pre-delivery treatment in severe preeclampsia |
| [NCT03412552](https://clinicaltrials.gov/study/NCT03412552) | N/A | Completed | 1238 | ICU management study; MgSO4 used for seizure control in severe preeclampsia/eclampsia, tracked maternal-fetal outcomes |
| [NCT01846156](https://clinicaltrials.gov/study/NCT01846156) | Phase 3 | Completed | 240 | Compared standard vs. newer MgSO4 dosing protocols for severe preeclampsia |
| [NCT00666133](https://clinicaltrials.gov/study/NCT00666133) | N/A | Completed | 304 | Evaluated MgSO4 seizure prophylaxis/treatment approaches for preeclampsia in low-resource settings |
| [NCT03164304](https://clinicaltrials.gov/study/NCT03164304) | Phase 4 | Completed | 222 | Compared 1g/h vs. 2g/h IV maintenance dose of MgSO4 in severe preeclampsia |
| [NCT04474704](https://clinicaltrials.gov/study/NCT04474704) | N/A | Completed | 53 | Pilot RCT using non-invasive cardiac monitoring to guide postpartum MgSO4 discontinuation timing |
| [NCT01801410](https://clinicaltrials.gov/study/NCT01801410) | Phase 3 | Completed | 602 | RCT of labour induction methods in preeclamptic women receiving MgSO4 for seizure prevention |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16978425](https://pubmed.ncbi.nlm.nih.gov/16978425/) | 2006 | Review | Obstetrical & Gynecological Survey | Reviews cerebral perfusion changes in preeclampsia and the rationale for MgSO4 alternatives |
| [2288560](https://pubmed.ncbi.nlm.nih.gov/2288560/) | 1990 | Review | American Journal of Obstetrics and Gynecology | Argues MgSO4 is the ideal anticonvulsant for preeclampsia-eclampsia based on decades of evidence |
| [2672428](https://pubmed.ncbi.nlm.nih.gov/2672428/) | 1989 | Mechanistic Review | Stroke | Proposes Mg opposes calcium-dependent vasospasm, explaining anticonvulsant/antivasospastic benefit in eclampsia |
| [9794688](https://pubmed.ncbi.nlm.nih.gov/9794688/) | 1998 | Review | Obstetrics and Gynecology | Reviews efficacy, benefits, and risks of MgSO4 seizure prophylaxis in preeclampsia/eclampsia |
| [39110688](https://pubmed.ncbi.nlm.nih.gov/39110688/) | 2024 | Qualitative Study | PLoS ONE | Nurse-midwife perspectives reveal knowledge gaps in MgSO4 dosing/toxicity monitoring (Tanzania) |
| [17441885](https://pubmed.ncbi.nlm.nih.gov/17441885/) | 2007 | Clinical Study | Journal of Obstetrics and Gynaecology Research | Measured ionized vs. total serum magnesium during MgSO4 therapy in severe preeclampsia-eclampsia |
| [31527059](https://pubmed.ncbi.nlm.nih.gov/31527059/) | 2019 | Commentary | Global Health, Science and Practice | Highlights health-system requirements (training, equipment) for effective MgSO4 use in resource-limited settings |
| [41054655](https://pubmed.ncbi.nlm.nih.gov/41054655/) | 2025 | Review | Cureus | Reviews MgSO4 pharmacology and evidence across obstetric and pediatric emergency indications |
| [1566765](https://pubmed.ncbi.nlm.nih.gov/1566765/) | 1992 | Experimental Study | American Journal of Obstetrics and Gynecology | Demonstrated central anticonvulsant effect of MgSO4 on hippocampal seizures in an animal model |
| [25353716](https://pubmed.ncbi.nlm.nih.gov/25353716/) | 2015 | Review | Acta Obstetricia et Gynecologica Scandinavica | Evaluates interventions, including MgSO4, to reduce preeclampsia/eclampsia-related maternal mortality in low-income countries |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between magnesium sulfate and preeclampsia/eclampsia is exceptionally well supported — multiple completed Phase 2/3/4 randomized trials (including large studies with n=1114–2000) plus international guideline endorsement (WHO/ACOG) confirm this is established, guideline-level standard of care rather than an unproven prediction. However, the drug has **zero registered licenses and is not marketed in Singapore** in the dataset reviewed, so local regulatory status, labeling, and safety information cannot currently be confirmed — this "Guardrails" status reflects the regulatory/documentation gap, not scientific uncertainty about efficacy.

**To proceed, the following is needed:**
- Singapore-specific prescribing information / package insert warnings and contraindications (currently a **Blocking** data gap — required before any S1 safety initial assessment)
- Formal DrugBank-sourced mechanism-of-action documentation (currently a **High** severity data gap)
- Confirmation of drug interaction (DDI) profile — current query returned no results
- Assessment of the regulatory pathway for registering magnesium sulfate in Singapore, given its current unmarketed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

