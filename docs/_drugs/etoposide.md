---
layout: default
title: Etoposide
parent: 僅模型預測 (L5)
nav_order: 405
evidence_level: L5
indication_count: 10
---

# Etoposide
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

# Etoposide: From Small Cell Lung Cancer and Lymphomas to Well-Differentiated Fetal Adenocarcinoma of the Lung

## One-Sentence Summary

Etoposide is a topoisomerase II inhibitor forming the backbone of combination regimens for small cell lung cancer, germ cell tumors, and lymphomas — though it carries no Singapore regulatory registration.
The TxGNN model predicts it may be effective for **well-differentiated fetal adenocarcinoma of the lung (WDFAL)**, the adult monophasic subtype of the pulmonary blastoma spectrum.
At present, this direction is supported by **0 clinical trials** and **1 publication** (a case report), placing it firmly in early exploratory territory.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Small cell lung cancer, germ cell tumors, and lymphomas (internationally recognized; no Singapore registration) |
| Predicted New Indication | Well-differentiated fetal adenocarcinoma of the lung |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, etoposide is a semisynthetic epipodophyllotoxin that inhibits topoisomerase II, causing DNA double-strand breaks and arresting cancer cells in the late S / early G2 phase of the cell cycle. Its efficacy in high-proliferation cancers — particularly small cell lung cancer, Ewing sarcoma, and lymphomas — has been established across decades of clinical trials. The mechanistic rationale for extrapolation to lung tumours expressing high levels of topoisomerase II is therefore biologically coherent.

Well-differentiated fetal adenocarcinoma of the lung (WDFAL) is the adult monophasic subtype of the pulmonary blastoma spectrum. Its embryonal glandular component structurally resembles fetal lung epithelium in the pseudoglandular stage and is known to exhibit high proliferative activity. Tumours with rapid cell cycling and elevated topoisomerase II expression are generally considered candidates for sensitivity to etoposide — the same mechanistic logic that underpins its use in pleuropulmonary blastoma in children, which represents the paediatric pole of the same disease spectrum.

However, critical uncertainty exists. WDFAL is a distinct, adult monophasic entity separate from classic biphasic pulmonary blastoma, and direct extrapolation of mechanistic assumptions between subtypes has not been validated. No standard chemotherapy protocol currently exists for WDFAL; the single case report in the literature (PMID 33107372) describes a biphasic pulmonary blastoma patient who received nedaplatin plus paclitaxel — not etoposide — as first-line adjuvant therapy. The TxGNN prediction is therefore a biologically plausible hypothesis rather than an evidence-supported indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33107372](https://pubmed.ncbi.nlm.nih.gov/33107372/) | 2020 | Case Report + Review | J Int Med Res | Classic biphasic pulmonary blastoma patient underwent right upper lobe resection; adjuvant nedaplatin + paclitaxel was used (not etoposide); disease recurred. Review covers the full PB spectrum including WDFAL as a distinct monophasic subtype, noting no standard chemotherapy guidelines exist due to rarity |

---

## Singapore Market Information

Etoposide (DB00773) holds no Singapore (HSA) product registrations. There are no licensed products to display.

---

## Cytotoxicity

Etoposide is an antineoplastic agent (epipodophyllotoxin class; original indications include small cell lung cancer and lymphomas).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Topoisomerase II inhibitor (Epipodophyllotoxin class) |
| Myelosuppression Risk | High — dose-limiting neutropenia and thrombocytopenia are primary toxicities; nadir typically at days 7–14 |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (before each cycle and at nadir), liver function tests, renal function (creatinine), blood pressure (hypotension risk during IV infusion) |
| Handling Protection | Must follow cytotoxic drug handling regulations (closed-system drug transfer, PPE, dedicated disposal) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Well-differentiated fetal adenocarcinoma of the lung is an ultra-rare disease with no registered clinical trials involving etoposide, and the mechanistic extrapolation from the broader pulmonary blastoma spectrum — while biologically plausible — remains unvalidated. The sole supporting publication is a case report of a related but distinct histological entity that did not even use etoposide.

**To proceed, the following is needed:**

- Histopathological confirmation of topoisomerase II expression in WDFAL tumour samples (to validate the mechanistic premise)
- Systematic case series or registry data on chemotherapy use in WDFAL (to establish any clinical precedent)
- Mechanistic similarity analysis between WDFAL and the paediatric pleuropulmonary blastoma / biphasic pulmonary blastoma subtypes where etoposide has been attempted
- Detailed MOA and pharmacokinetic profile from DrugBank API (to address DG002 data gap)
- Safety data from the TFDA package insert and Singapore-relevant sources (to address DG001 data gap before any clinical consideration)
- Given etoposide's absence from the Singapore market, a regulatory pathway assessment (compassionate use or import) would be required prior to any investigational use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

