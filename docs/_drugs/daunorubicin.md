---
layout: default
title: Daunorubicin
parent: 僅模型預測 (L5)
nav_order: 304
evidence_level: L5
indication_count: 10
---

# Daunorubicin
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

# Daunorubicin: From Acute Leukemia to Hodgkin's Lymphoma

## One-Sentence Summary

Daunorubicin is a classic anthracycline antibiotic originally established as a cornerstone therapy for acute myeloid leukemia (AML) and acute lymphoblastic leukemia (ALL). The TxGNN model predicts it may be effective for **Hodgkin's Lymphoma**, with **50 clinical trials** and **20 publications** currently supporting this direction — primarily through anthracycline class-effect extrapolation from doxorubicin-based ABVD regimens, plus one direct early-phase clinical study of liposomal daunorubicin in relapsed/refractory lymphoma (PMID 9387047, 1997).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute leukemia (AML, ALL) |
| Predicted New Indication | Hodgkin's Lymphoma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Daunorubicin is an anthracycline antibiotic that acts by intercalating into DNA double strands and inhibiting topoisomerase II, thereby blocking DNA replication and transcription in rapidly proliferating cells. It is one of the oldest cytotoxic agents in oncology, central to leukemia induction protocols for decades. Although detailed MOA documentation is not currently available in this evidence pack, daunorubicin shares the same core pharmacophore and mechanism with its structural analog doxorubicin (adriamycin) — differing only by a single hydroxyl group on the sugar moiety.

Hodgkin's lymphoma is defined by the presence of malignant Reed-Sternberg cells, which exhibit exceptionally high proliferative activity and are exquisitely sensitive to topoisomerase II inhibition. The current global standard of care for advanced-stage Hodgkin's lymphoma — the ABVD regimen (adriamycin/doxorubicin, bleomycin, vinblastine, dacarbazine) — places an anthracycline at its center. Phase 3 landmark trials (PMID 29224502, 39413375) have further refined this standard, consistently confirming doxorubicin as the backbone drug in frontline combination regimens achieving complete response rates of 88–94%.

Most critically, a 1997 early-phase clinical evaluation (PMID 9387047) directly assessed liposomally encapsulated daunorubicin (DaunoXome) in 19 patients with relapsed or refractory lymphoma, demonstrating one complete response and two partial responses at the higher dose schedule (120 mg/m² every 21 days), with no clinically significant cardiac deterioration. This provides the most direct clinical bridge between daunorubicin specifically — not merely the anthracycline class — and lymphoma treatment efficacy. Given these converging lines of evidence, the TxGNN model's prediction is mechanistically sound and clinically plausible.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00025064](https://clinicaltrials.gov/study/NCT00025064) | Phase 2 | Unknown | 260 | Hodgkin's disease in children and adolescents; combination chemotherapy regimens ± radiation or stem cell transplant; anthracycline-containing backbone |
| [NCT00736320](https://clinicaltrials.gov/study/NCT00736320) | Phase 3 | Unknown | 1,150 | HD16: first-line treatment optimization in early-stage Hodgkin's lymphoma using FDG-PET stratification; ABVD (doxorubicin) backbone — primary indirect class-effect evidence |
| [NCT00049595](https://clinicaltrials.gov/study/NCT00049595) | Phase 3 | Completed | 552 | BEACOPP vs ABVD in Stage III–IV Hodgkin's lymphoma; anthracyclines are central to both treatment arms |
| [NCT00025259](https://clinicaltrials.gov/study/NCT00025259) | Phase 3 | Completed | 1,734 | Dose-intensive, response-based chemotherapy ± radiation for intermediate-risk pediatric Hodgkin's disease; established pediatric HL chemotherapy framework |
| [NCT00678327](https://clinicaltrials.gov/study/NCT00678327) | Phase 3 | Completed | 1,202 | FDG-PET response-adapted therapy in newly diagnosed advanced Hodgkin's lymphoma; validated PET-guided anthracycline dosing strategy |
| [NCT01777152](https://clinicaltrials.gov/study/NCT01777152) | Phase 3 | Completed | 452 | Brentuximab Vedotin + CHP vs CHOP in CD30-positive mature T-cell lymphomas; doxorubicin-containing CHOP backbone with direct anthracycline comparator arm |
| [NCT01771107](https://clinicaltrials.gov/study/NCT01771107) | Phase 1/2 | Completed | 41 | AVD + Brentuximab Vedotin in Stage II–IV HIV-associated Hodgkin's lymphoma; confirmed tolerability of anthracycline-containing regimens in this population |
| [NCT02398240](https://clinicaltrials.gov/study/NCT02398240) | Phase 2 | Completed | 40 | Risk-adapted therapy with Brentuximab Vedotin + combination chemotherapy for all stages of newly diagnosed Hodgkin's lymphoma in children and young adults |
| [NCT00920153](https://clinicaltrials.gov/study/NCT00920153) | Phase 3 | Terminated | 442 | Comparison of three therapy regimens in previously untreated Hodgkin's lymphoma; early termination — anthracycline-containing arms provided relevant safety data |
| [NCT06377566](https://clinicaltrials.gov/study/NCT06377566) | Phase 2 | Recruiting | 71 | BV-AVD in newly diagnosed early-stage bulky Hodgkin's lymphoma using PET-adapted and metabolic tumor volume-guided approach |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39413375](https://pubmed.ncbi.nlm.nih.gov/39413375/) | 2024 | Phase 3 RCT | N Engl J Med | Nivolumab + AVD vs ABVD in advanced-stage classic Hodgkin's lymphoma; doxorubicin-containing AVD as control arm confirms anthracycline backbone efficacy |
| [29224502](https://pubmed.ncbi.nlm.nih.gov/29224502/) | 2018 | Phase 3 RCT | N Engl J Med | Brentuximab Vedotin + AVD vs ABVD in Stage III–IV Hodgkin's lymphoma; landmark trial establishing anthracycline as irreplaceable backbone in frontline HL treatment |
| [35830649](https://pubmed.ncbi.nlm.nih.gov/35830649/) | 2022 | Phase 3 RCT Follow-up | N Engl J Med | 5-year overall survival data from BV+AVD vs ABVD trial; confirmed durable long-term benefit of anthracycline-containing regimens with improved progression-free survival |
| [36322844](https://pubmed.ncbi.nlm.nih.gov/36322844/) | 2022 | Phase 3 RCT | N Engl J Med | Brentuximab Vedotin + chemotherapy in pediatric high-risk Hodgkin's lymphoma; efficacy of adding targeted CD30 therapy to anthracycline backbone in children |
| [9387047](https://pubmed.ncbi.nlm.nih.gov/9387047/) | 1997 | Phase 1/Early Phase 2 | Investig New Drugs | **Direct daunorubicin evidence**: Liposomal daunorubicin (DaunoXome) in 19 relapsed/refractory lymphoma patients; 1 CR + 2 PR at 120 mg/m² q21d; no clinically significant cardiac toxicity — key bridge study |
| [28365830](https://pubmed.ncbi.nlm.nih.gov/28365830/) | 2017 | Review | Curr Oncol Rep | Optimal therapy for early-stage Hodgkin's lymphoma: risk-adapted and response-adapted strategies; discusses evolving role of radiotherapy alongside anthracycline chemotherapy |
| [30139285](https://pubmed.ncbi.nlm.nih.gov/30139285/) | 2018 | Review | Expert Rev Hematol | Sequencing novel therapies in relapsed Hodgkin's lymphoma; ABVD achieves CR in up to 88% of advanced-stage patients; frames anthracycline-based frontline standard |
| [36271128](https://pubmed.ncbi.nlm.nih.gov/36271128/) | 2022 | Retrospective Cohort | Sci Rep | Interim FDG-PET predictive value in 245 HL patients treated with ABVD; iPET2 and iPET4 results guide anthracycline-based therapy decisions in clinical practice |
| [14584273](https://pubmed.ncbi.nlm.nih.gov/14584273/) | 2003 | Review | Gan to Kagaku Ryoho | Overview of hematologic tumor chemotherapy; notes ABVD as HL standard and daunorubicin's established role in AML — contextualises anthracycline class across hematologic malignancies |
| [378369](https://pubmed.ncbi.nlm.nih.gov/378369/) | 1979 | Historical Analysis | Cancer Treat Rep | Comparative analysis of daunorubicin vs adriamycin across cancer types; defines distinct pharmacological roles and limitations of both anthracyclines — foundational class reference |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — Anthracycline class (DNA intercalating agent and topoisomerase II inhibitor) |
| Myelosuppression Risk | High — Dose-limiting leukopenia and neutropenia are expected; thrombocytopenia and anaemia also occur; nadir typically at Days 10–14 post-infusion |
| Emetogenicity Classification | Moderate to High |
| Monitoring Items | Full blood count with differential (prior to each cycle), liver function tests, renal function, serum uric acid; **cardiac function monitoring is mandatory** — ECG and echocardiography or MUGA scan before initiation and at regular intervals; cumulative lifetime dose must be tracked to prevent irreversible cardiomyopathy |
| Handling Protection | Classified as a vesicant — strict intravenous extravasation precautions required; must be handled following cytotoxic drug handling regulations with appropriate PPE |

---

## Safety Considerations

Please refer to the package insert for complete safety information, as local prescribing data and drug-drug interaction data were not available in this evidence pack.

> **Important:** Daunorubicin carries a well-established risk of **cumulative dose-dependent cardiomyopathy**, a class effect shared with all anthracyclines. Careful cardiac function monitoring and strict lifetime cumulative dose limits are essential. As a **vesicant**, extravasation during intravenous administration can cause severe local tissue necrosis. These risks are particularly relevant if repurposing for Hodgkin's lymphoma, where patients may already have received or may receive other cardiotoxic agents (e.g., bleomycin-related pulmonary toxicity under ABVD).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The anthracycline class effect provides a mechanistically robust and clinically well-supported indirect bridge to Hodgkin's lymphoma — a disease in which doxorubicin-based ABVD has been the global standard of care for decades. The 1997 liposomal daunorubicin study (PMID 9387047) offers direct, albeit early-phase and small-scale, evidence of activity in relapsed/refractory lymphoma with a manageable cardiac profile, lending meaningful biological plausibility beyond pure class extrapolation. However, the absence of any contemporary Phase 2/3 trials specifically designed for daunorubicin in Hodgkin's lymphoma, combined with no Singapore market registration, means any clinical development must proceed within a clearly defined research framework.

**To proceed, the following is needed:**
- Complete mechanism of action documentation (DrugBank full profile, pharmacokinetic parameters)
- Singapore HSA regulatory package insert review and local safety database search
- Full drug-drug interaction (DDI) profile, especially interactions with bleomycin and vinblastine (standard ABVD co-medications)
- Comparative PK/PD analysis between daunorubicin and doxorubicin in lymphoma settings to determine dose equivalency
- Formal cardiotoxicity risk assessment at lymphoma-appropriate doses vs. established leukemia protocols
- Prospective clinical trial design (preferably Phase 1b/2) evaluating daunorubicin — or its liposomal formulation — in relapsed/refractory Hodgkin's lymphoma, particularly in patients ineligible for bleomycin in ABVD or as part of a reduced-cardiotoxicity strategy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

