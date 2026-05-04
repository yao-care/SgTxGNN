---
layout: default
title: Bemiparin
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Bemiparin
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

# Bemiparin: From Deep Vein Thrombosis to Pulmonary Embolism

## One-Sentence Summary

Bemiparin is a second-generation low-molecular-weight heparin (LMWH) established internationally for the treatment of deep vein thrombosis (DVT) and prophylaxis of venous thromboembolism (VTE), though it is currently not registered in Singapore.
The TxGNN model predicts it may be effective for **Pulmonary Embolism (PE)** — the most life-threatening extension of DVT — with **10 clinical trials** and **8 publications** currently supporting this direction.
Among all 10 TxGNN-predicted indications, pulmonary embolism (model rank 9, score 87.92%) is the only prediction carrying actual clinical evidence (L1) and an actionable recommendation; the higher-ranked predictions (ranks 1–8, all platelet bleeding disorders) are mechanistically contradicted by Bemiparin's anticoagulant mode of action and carry a uniform **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | DVT treatment and VTE prophylaxis (established in international markets; not registered in Singapore) |
| Predicted New Indication | Pulmonary Embolism |
| TxGNN Prediction Score | 87.92% |
| Evidence Level | L1 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Methodology note:** This report features pulmonary embolism (TxGNN rank 9) rather than the top-ranked prediction (rank 1: primary release disorder of platelets, score 98.71%), because ranks 1–8 are mechanistically contradicted — using an anticoagulant to treat platelet-mediated bleeding disorders would worsen haemorrhage. PE (rank 9) is the highest-ranked prediction supported by both mechanistic logic and direct clinical evidence.

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Bemiparin is a second-generation LMWH with the lowest molecular weight among approved LMWHs, a prolonged half-life (~5.2 hours vs. enoxaparin's ~4.4 hours), and the highest anti-Factor Xa/anti-Factor IIa activity ratio (~8:1). By inhibiting Factor Xa, Bemiparin suppresses thrombin generation and subsequent fibrin clot propagation — the core mechanism underlying both DVT and PE pathophysiology.

Pulmonary embolism is the direct and most dangerous consequence of untreated deep vein thrombosis: dislodged thrombus migrates through the venous circulation to occlude pulmonary arteries. DVT and PE are therefore two clinical presentations of the same disease — venous thromboembolism. International guidelines from the American College of Chest Physicians (ACCP) and the European Society of Cardiology (ESC) list LMWH as a first-line therapy for both acute DVT and PE treatment and secondary prevention. A comprehensive 2014 review (PMID 24657810) explicitly states Bemiparin is "indicated for the acute treatment of deep vein thrombosis **with or without pulmonary embolism**." TxGNN's prediction thus validates an internationally recognised but Singapore-unregistered indication.

Regarding the higher-ranked TxGNN predictions: ranks 1–8 (including primary release disorder of platelets, Glanzmann thrombasthenia, pseudo-von Willebrand disease, Scott syndrome, and fetal/neonatal alloimmune thrombocytopenia) all represent conditions where haemostasis is already impaired due to platelet dysfunction or thrombocytopenia. Applying an anticoagulant in these settings would worsen — not treat — the underlying bleeding tendency. These high TxGNN scores most likely reflect indirect graph-node proximity between coagulation pathway entities and platelet biology in the knowledge graph, not a genuine therapeutic signal. All carry a **Hold** recommendation and are excluded from further clinical analysis in this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01880216](https://clinicaltrials.gov/study/NCT01880216) | Phase 3 | Completed | 312 | Multi-national, multi-centre RCT comparing Bemiparin vs. Enoxaparin for acute DVT treatment; directly evaluates VTE therapy efficacy and safety, including PE as a primary outcome endpoint |
| [NCT00219973](https://clinicaltrials.gov/study/NCT00219973) | Phase 3 | Completed | 526 | Double-blind, placebo-controlled RCT evaluating 28-day vs. 8-day Bemiparin VTE prophylaxis in oncological abdominal/pelvic surgery; landmark trial establishing Bemiparin's extended prophylaxis evidence |
| [NCT01727427](https://clinicaltrials.gov/study/NCT01727427) | N/A | Completed | 695 | Large prospective observational study on LMWH treatment of unsuspected PE in cancer patients; directly relevant to PE management paradigm |
| [NCT01164046](https://clinicaltrials.gov/study/NCT01164046) | Phase 3 | Terminated | 56 | Long-term LMWH anticoagulation in cancer patients with DVT or PE; terminated early due to recruitment difficulties — conclusions limited, but design directly addresses PE |
| [NCT04420299](https://clinicaltrials.gov/study/NCT04420299) | Phase 2 | Terminated | 81 | Randomised single-blind study of Bemiparin at therapeutic vs. prophylactic dose in hospitalised COVID-19 patients; provides interim VTE-range safety data, terminated at 81 subjects |
| [NCT01588171](https://clinicaltrials.gov/study/NCT01588171) | N/A | Completed | 7,020 | Large RCT comparing Bemiparin vs. Enoxaparin for post-delivery VTE prophylaxis (vaginal and caesarean); major safety dataset (one PE case documented among 7,020 participants) |
| [NCT01630148](https://clinicaltrials.gov/study/NCT01630148) | N/A | Completed | 774 | Bemiparin thromboprophylaxis after benign gynaecological surgery; VTE prevention in elective surgical setting |
| [NCT02795065](https://clinicaltrials.gov/study/NCT02795065) | N/A | Completed | 100 | Bemiparin vs. Enoxaparin for VTE prevention in ICU patients; indirect PE prevention evidence in critically ill population |
| [NCT05569681](https://clinicaltrials.gov/study/NCT05569681) | N/A | Recruiting | 2,400 | Ongoing RCT comparing Bemiparin dose regimens for post-surgical thromboprophylaxis in morbidly obese patients; results expected October 2026 |
| [NCT04508855](https://clinicaltrials.gov/study/NCT04508855) | N/A | Withdrawn | 0 | DOAC-to-LMWH switch study in cancer patients with atrial fibrillation; withdrawn before enrolment — no usable data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [29214507](https://pubmed.ncbi.nlm.nih.gov/29214507/) | 2018 | RCT | Clin Drug Investig | Once-daily Bemiparin vs. twice-daily Enoxaparin for acute DVT; patients with DVT carry inherent PE risk — demonstrates Bemiparin's non-inferiority in acute VTE treatment |
| [22242023](https://pubmed.ncbi.nlm.nih.gov/22242023/) | 2011 | RCT | Obstet Gynecol Int | 646 women randomised to 5-day vs. 10-day postcesarean Bemiparin; one PE event documented, supporting the drug's haemostatic profile in the peripartum period |
| [24657810](https://pubmed.ncbi.nlm.nih.gov/24657810/) | 2014 | Review | Vasc Pharmacol | Comprehensive Bemiparin review; explicitly confirms its indication for "acute treatment of DVT with or without pulmonary embolism" and VTE prophylaxis across surgical and medical patients |
| [31030749](https://pubmed.ncbi.nlm.nih.gov/31030749/) | 2019 | Review | Prog Mol Biol Transl Sci | LMWH clinical applications overview; lists Bemiparin as one of 8 officially approved LMWHs with established VTE indications including PE |
| [17532688](https://pubmed.ncbi.nlm.nih.gov/17532688/) | 2005 | Prospective Cohort | Clin Drug Investig | Bemiparin safety and utilisation in medical inpatients; demonstrated suppression of hypercoagulability markers in acutely ill patients with heart failure — relevant to VTE prevention |
| [20384389](https://pubmed.ncbi.nlm.nih.gov/20384389/) | 2010 | Cohort | Clin Drug Investig | ANCIANOS study: Bemiparin thromboprophylaxis in elderly medical patients in real-world clinical practice; important non-surgical population safety data |
| [16545251](https://pubmed.ncbi.nlm.nih.gov/16545251/) | 2006 | Cohort | Arch Bronconeumol | Home VTE prophylaxis in COPD patients; supports Bemiparin use in extended outpatient prophylaxis, relevant to PE prevention in high-risk chronic disease populations |
| [22935839](https://pubmed.ncbi.nlm.nih.gov/22935839/) | 2012 | Cohort | Semergen | Bemiparin thromboprophylaxis for non-surgical traumatic lower limb injury with immobilisation; outpatient LMWH use supporting accessibility and safety profile |

---

## Singapore Market Information

Bemiparin currently has **no registered products in Singapore**. There are 0 HSA authorisations on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No registration found |

> Bemiparin is commercially available in Spain, several EU-adjacent markets, and parts of the Middle East and Latin America, primarily under the brand name **Hibor** (Rovi Pharmaceuticals). It is approved in those markets for DVT treatment (with or without PE) and VTE prophylaxis. Singapore currently has no equivalent registered product.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (key warnings, contraindications, and drug-drug interactions) were not retrievable for this Evidence Pack. DDI query returned no results; TFDA prescribing information was not parsed. Remediation requires downloading the full prescribing information PDF from the relevant regulatory authority and querying the DrugBank API for complete interaction data.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bemiparin has robust Phase 3 RCT support (NCT01880216, NCT00219973) and a peer-reviewed body of literature confirming its efficacy and safety for VTE treatment and prophylaxis — a clinical spectrum that formally encompasses pulmonary embolism. Review literature explicitly lists PE treatment as an approved indication in other jurisdictions. The L1 evidence classification reflects the quality and volume of existing data; the primary barrier to Singapore use is the absence of HSA registration rather than any unresolved clinical question.

**To proceed, the following is needed:**

- **Regulatory pathway**: Initiate HSA registration process; identify an appropriate reference jurisdiction (EU or ICH-aligned market) for abridged submission
- **Safety dossier**: Retrieve and review the full prescribing information (package insert) to document warnings, contraindications, and special population restrictions (renal impairment, pregnancy, HIT risk)
- **DDI profile**: Conduct formal drug-drug interaction analysis via DrugBank API or literature review; current dataset returned no results
- **MOA documentation**: Confirm mechanism of action data from DrugBank to complete mechanistic justification for the submission dossier
- **Local pharmacovigilance plan**: Establish post-market surveillance plan aligned with HSA requirements, including platelet count monitoring protocol and haemorrhage reporting thresholds
- **Dosing guidance for Asian populations**: Review any PK/PD data from Asian cohorts, given body weight differences that may affect anti-Xa target attainment

---

*This report is generated for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Data cut-off: 10 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

