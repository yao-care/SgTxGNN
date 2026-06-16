---
layout: default
title: Doxorubicin
parent: 僅模型預測 (L5)
nav_order: 348
evidence_level: L5
indication_count: 10
---

# Doxorubicin
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

# Doxorubicin: From Broad-Spectrum Antineoplastic Use to Ewing Sarcoma

## One-Sentence Summary

Doxorubicin is a foundational anthracycline antineoplastic agent widely established in oncology for treating breast cancer, lymphomas, leukemias, and sarcomas globally, though it currently holds no Singapore market registration.
The TxGNN model predicts it may be effective for **Ewing Sarcoma**,
with **multiple completed Phase III RCTs** and over **20 publications** supporting this direction — making it one of the strongest repurposing candidates in this analysis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum antineoplastic (breast cancer, lymphoma, leukemia, sarcoma) — no Singapore registration on file |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Doxorubicin is an anthracycline antibiotic that exerts its antitumour effect primarily through two mechanisms: intercalating into the DNA double helix and inhibiting topoisomerase II, both of which trigger double-strand DNA breaks and halt cell replication. This mode of action is particularly potent against rapidly dividing tumour cells.

Ewing sarcoma is driven by the EWS-FLI1 fusion protein — a transcriptional driver that locks tumour cells in a state of aggressive, high-rate proliferation. This biological vulnerability makes Ewing sarcoma cells exquisitely sensitive to doxorubicin's DNA-damaging mechanism. Indeed, doxorubicin is the backbone of the internationally accepted VAC/IE regimen (vincristine–doxorubicin–cyclophosphamide alternating with ifosfamide–etoposide), which has been the standard of care for Ewing sarcoma for decades across North America, Europe, and Asia.

The TxGNN knowledge graph prediction is therefore not a speculative leap but a computational confirmation of a well-established clinical practice. Multiple cooperative group trials — including the landmark EURO-EWING and Children's Oncology Group (COG) studies — have consistently placed doxorubicin at the centre of Ewing sarcoma treatment. The absence of a Singapore regulatory registration reflects a market access gap, not a clinical evidence gap.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Completed | 278 | Randomised controlled trial evaluating dose intensification versus standard therapy in non-metastatic Ewing sarcoma; both arms used doxorubicin as the treatment backbone. Key question was whether higher intensity improves outcomes over standard VAC/IE. |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Completed | 642 | COG trial adding vincristine-topotecan-cyclophosphamide to established 5-drug standard regimen (including doxorubicin) in non-metastatic Ewing sarcoma. Established doxorubicin-containing standard as the control reference. |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Completed | 587 | Randomised trial comparing chemotherapy intensification through interval compression (AEWS0031-era) versus standard regimens in Ewing sarcoma and PNET; doxorubicin-containing regimens tested in both arms. |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | Unknown | 1,200 | EURO-E.W.I.N.G.99 — major European cooperative trial studying combination chemotherapy ± stem cell transplantation in Ewing sarcoma; doxorubicin integral to induction. |
| [NCT03011528](https://clinicaltrials.gov/study/NCT03011528) | Phase 2 | Completed | 45 | CombinaiR3: direct efficacy study in Ewing sarcoma patients with primary extrapulmonary dissemination; multidrug chemotherapy including doxorubicin evaluated prospectively. |
| [NCT00002643](https://clinicaltrials.gov/study/NCT00002643) | Phase 2 | Completed | 130 | POG pilot study of intensive chemotherapy with growth factor support in newly diagnosed metastatic Ewing sarcoma; doxorubicin-containing regimen directly evaluated for this high-risk group. |
| [NCT06820957](https://clinicaltrials.gov/study/NCT06820957) | Phase 2/3 | Active, not recruiting | 437 | Randomised trial of vincristine-irinotecan-regorafenib (VIrR) combined with VDC/IE versus standard VDC/IE alone in newly diagnosed metastatic Ewing sarcoma; doxorubicin (within VDC) is the experimental backbone. |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Active, not recruiting | 312 | COG AEWS1221: randomised trial adding IGF-1R monoclonal antibody ganitumab to interval-compressed VDC/IE (including doxorubicin) in newly diagnosed metastatic Ewing sarcoma. |
| [NCT03277924](https://clinicaltrials.gov/study/NCT03277924) | Phase 1/2 | Completed | 197 | International multicentre trial combining sunitinib and/or nivolumab with chemotherapy (doxorubicin as backbone) in advanced soft tissue and bone sarcomas including Ewing; assessed feasibility of immunotherapy addition. |
| [NCT00001209](https://clinicaltrials.gov/study/NCT00001209) | Phase 1 | Completed | 120 | NIH pilot establishing safety of vincristine–adriamycin–cyclophosphamide alternating with ifosfamide–VP16 in Ewing sarcoma and high-risk sarcomas; foundational evidence for the current VAC/IE standard. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT (Phase III) | The Lancet | EE2012 international randomised trial directly comparing European (VIDE induction + doxorubicin-based consolidation) versus US (VDC/IE) chemotherapy strategies in newly diagnosed Ewing sarcoma; demonstrated equivalent outcomes between the two major doxorubicin-containing regimens. |
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | Landmark COG trial showing that adding ifosfamide and etoposide to standard doxorubicin-containing chemotherapy significantly improved event-free survival in newly diagnosed Ewing sarcoma and PNET of bone; established the VAC/IE combination as standard of care. |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | COG AEWS0031: randomised trial demonstrating that interval compression of VDC/IE cycles (including doxorubicin) significantly improved event-free survival vs. standard scheduling in localised Ewing sarcoma; shifted clinical practice toward 2-week cycle compression. |
| [35427190](https://pubmed.ncbi.nlm.nih.gov/35427190/) | 2022 | RCT | J Clin Oncol | Ewing 2008R3 international trial (12 countries) evaluating high-dose treosulfan/melphalan consolidation versus standard continuation therapy following doxorubicin-based induction in high-risk Ewing sarcoma. |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | Randomised Phase III | J Clin Oncol | COG AEWS1221: randomised phase III trial adding IGF-1R antibody ganitumab to interval-compressed VDC/IE (doxorubicin-containing) in metastatic Ewing sarcoma; showed no added benefit from ganitumab, confirming the doxorubicin backbone remains the gold standard. |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | International RCT | Trials | EURO EWING 2012 protocol paper detailing the largest prospective Ewing sarcoma trial to date comparing two established regimens, both containing doxorubicin as an essential component. |
| [37651654](https://pubmed.ncbi.nlm.nih.gov/37651654/) | 2023 | Long-term RCT follow-up | J Clin Oncol | Long-term outcomes from COG AEWS0031 confirming durable benefit of interval-compressed VDC/IE (doxorubicin-backbone); provides 10+ year follow-up data on survival and late effects. |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | Comprehensive review of Ewing sarcoma treatment history and current management; documents the role of doxorubicin-based multiagent chemotherapy in raising survival from < 10% to ~75% for localised disease. |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Narrative Review | J Clin Oncol | International collaborative review of Ewing sarcoma management strategies; discusses risk-adapted use of doxorubicin-containing regimens across cooperative groups globally. |
| [1833556](https://pubmed.ncbi.nlm.nih.gov/1833556/) | 1991 | Dose-Intensity Analysis | J Natl Cancer Inst | Systematic dose-intensity analysis across published Ewing sarcoma trials demonstrating that doxorubicin dose intensity is among the most significant predictors of favourable outcome; provided mechanistic rationale for dose-dense scheduling. |

---

## Singapore Market Information

Doxorubicin is currently **not registered** in Singapore. No Health Sciences Authority (HSA) product licences are on file. This is a market access gap rather than a clinical evidence deficit — doxorubicin is included in international treatment guidelines (ESMO, NCCN, COSS/GPOH) and is available through institutional procurement or compassionate use pathways in most jurisdictions.

---

## Cytotoxicity

Doxorubicin is a conventional cytotoxic anthracycline antibiotic and qualifies for this section.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Anthracycline class (DNA intercalator / Topoisomerase II inhibitor) |
| Myelosuppression Risk | **High** — dose-limiting toxicity is myelosuppression, particularly neutropenia and thrombocytopenia; nadir typically at 10–14 days post-administration |
| Emetogenicity Classification | **Moderate to High** — requires prophylactic antiemetics (5-HT3 antagonist ± NK1 antagonist); single-agent doxorubicin classified as moderate-to-high emetogenic risk |
| Monitoring Items | CBC with differential (before each cycle and at nadir), cardiac function (echocardiogram or MUGA scan at baseline and after cumulative dose thresholds), liver and renal function, left ventricular ejection fraction (LVEF) — cumulative dose limit typically 450–550 mg/m² without cardioprotection |
| Handling Protection | Must comply with cytotoxic drug handling regulations; vesicant — extravasation causes severe tissue necrosis; requires closed-system drug transfer devices and personnel protective equipment |

**Additional note:** Anthracycline-related cardiotoxicity is a well-established late effect. In paediatric Ewing sarcoma patients, long-term cardiac surveillance is mandatory given cumulative doses and young age at exposure. Dexrazoxane co-administration should be considered in protocols where cumulative doxorubicin dose is expected to exceed 300 mg/m².

---

## Safety Considerations

Detailed Singapore (HSA) package insert warnings and contraindications are not available in the current evidence pack as Doxorubicin is not registered locally. No drug-drug interaction data was retrieved from the DDI database.

Please refer to internationally available package inserts (US FDA, EMA, or originator label) for full safety information, including:
- Cardiotoxicity warnings (cumulative dose-dependent)
- Vesicant extravasation risk
- Secondary malignancy risk (therapy-related AML — relevant given the monocytic leukemia safety signal identified in Rank 6 analysis)
- Contraindications in pre-existing heart failure or severe hepatic impairment

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Doxorubicin in Ewing sarcoma is not a repurposing hypothesis — it is already the global standard of care backbone supported by multiple completed Phase III RCTs across COG, EURO-EWING, and cooperative groups in 12+ countries. The L1 evidence designation is solidly established. The primary issue is Singapore market access, not clinical evidence.

**To proceed, the following is needed:**

- **Regulatory pathway**: Determine the appropriate HSA import or compassionate use mechanism for doxorubicin in Singapore; evaluate whether named-patient import, unregistered product access, or institution-level procurement applies
- **Formal MOA documentation**: Retrieve full DrugBank/FDA label data to populate the MOA field and support institutional pharmacovigilance filings
- **Cumulative cardiotoxicity management plan**: Define LVEF monitoring intervals, cumulative dose thresholds, and dexrazoxane co-administration criteria appropriate to the Ewing sarcoma protocol being deployed
- **Secondary malignancy risk acknowledgment**: Document the therapy-related AML signal (11q23 MLL rearrangement risk) in the consent process, particularly for paediatric patients
- **Paediatric pharmacokinetic data**: For patients under 10 years, age-adjusted doxorubicin dosing should be referenced (PMID 21095926 — paediatric PK study)
- **Protocol alignment**: Confirm which international protocol (COG AEWS1221-era VDC/IE, or EURO-EWING EE2012 VIDE-based) will be followed, as the two strategies have now been directly compared (PMID 36522207) and shown equivalent efficacy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

