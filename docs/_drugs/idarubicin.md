---
layout: default
title: Idarubicin
parent: 僅模型預測 (L5)
nav_order: 499
evidence_level: L5
indication_count: 10
---

# Idarubicin
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

# Idarubicin: From Acute Myeloid Leukemia to Bulbar Polio

## One-Sentence Summary

Idarubicin is an anthracycline cytotoxic antibiotic used as a core component of Acute Myeloid Leukemia (AML) induction chemotherapy — most notably the "7+3" regimen (idarubicin + cytarabine).
The TxGNN model predicts it may be effective for **Bulbar Polio**, the highest-ranked novel indication (score 97.05%);
however, this prediction is currently supported by **0 clinical trials** and **0 publications**, and the mechanistic rationale is weak — likely reflecting knowledge graph node-association noise rather than genuine biological plausibility.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute Myeloid Leukemia (AML induction therapy) — based on established medical use; no Singapore regulatory record available |
| Predicted New Indication | Bulbar Polio |
| TxGNN Prediction Score | 97.05% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Idarubicin is a semi-synthetic anthracycline antibiotic that inhibits Topoisomerase II (Topo II) and intercalates into DNA, thereby blocking DNA replication and transcription. It is a conventional cytotoxic agent primarily active against rapidly dividing malignant cells, and is a standard component of AML induction therapy.

Bulbar Polio is a severe form of poliovirus infection affecting the brainstem, causing cranial nerve dysfunction and respiratory failure. Its pathological mechanism involves viral cytolysis of motor neurons — a fundamentally different process from the neoplastic, proliferative diseases for which Idarubicin was designed. There is no established mechanistic pathway by which Topo II inhibition or DNA intercalation would offer therapeutic benefit in a viral neurological disease.

The high TxGNN score (97.05%) for this prediction is most likely attributable to knowledge graph topological noise — where cytotoxic drug nodes and neurological disease nodes are linked through indirect associations — rather than any biologically meaningful connection. This prediction does not warrant further investigation in its current form.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Idarubicin is **not currently registered** in Singapore. No Health Sciences Authority (HSA) licenses have been identified for this drug. Clinical use, if needed, would require importation via Special Access Route (SAR) or a compassionate use application.

---

## Cytotoxicity

Idarubicin is an anthracycline cytotoxic antibiotic. The Cytotoxicity section is therefore applicable.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Anthracycline class (Topoisomerase II inhibitor / DNA intercalator) |
| Myelosuppression Risk | **High** — Severe myelosuppression (neutropenia, thrombocytopenia, anaemia) is the primary dose-limiting toxicity; nadir typically occurs 10–14 days after administration |
| Cardiotoxicity Risk | **High** — Cumulative cardiotoxicity (dilated cardiomyopathy, reduced LVEF) is a class-specific anthracycline risk; requires monitoring of cumulative lifetime dose |
| Emetogenicity Classification | Moderate to High — prophylactic antiemetic therapy required |
| Monitoring Items | CBC with differential (at least twice weekly during induction), baseline and serial cardiac function (echocardiography or MUGA scan), liver function, renal function, electrolytes, uric acid |
| Handling Protection | Must be handled under cytotoxic drug precautions: biological safety cabinet preparation, personal protective equipment (double gloves, gown, eye protection), waste disposal per cytotoxic regulations |

---

## Safety Considerations

Detailed safety data (package insert warnings, contraindications, and drug interactions) were not available in this Evidence Pack. Please refer to the manufacturer's package insert for complete safety information, particularly regarding:

- Cardiac toxicity and cumulative dose limits
- Myelosuppression management
- Use in hepatic impairment (dose adjustment required)
- Pregnancy and lactation contraindications

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN-predicted indication for Idarubicin — Bulbar Polio — has no clinical trials, no supporting literature, and no mechanistic plausibility: a viral neurological disease and a DNA-intercalating cytotoxic agent have no known therapeutic connection. All 10 ranked predictions either received a "Hold" (L5, no evidence) or a cautious "Research Question" (L4, indirect drug-class extrapolation only), with none reaching actionable evidence.

**To proceed with any further evaluation, the following is needed:**

- **Reframe the query:** Rather than evaluating Idarubicin against its highest TxGNN-scored predictions (which are biologically implausible), focus on oncological indications where anthracyclines already have indirect evidence — e.g., **Ganglioneuroblastoma** (rank 7, L4) or **Hodgkin Lymphoma** (rank 10, L4), both of which have mechanistic drug-class rationale
- **Retrieve MOA data from DrugBank API** to enable formal mechanistic linkage analysis (DG002 remediation)
- **Retrieve Singapore/HSA package insert warnings and contraindications** (DG001 remediation) before any safety assessment
- **Confirm Singapore registration pathway**: Since Idarubicin is not currently marketed in Singapore, a Special Access Route (SAR) or parallel import pathway evaluation is required before any clinical use discussion
- **Search for direct Idarubicin evidence in AML-adjacent haematological malignancies** to identify any indication with existing clinical trial data that might support a legitimate repurposing case

> ⚠️ *This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

