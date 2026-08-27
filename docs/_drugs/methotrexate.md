---
layout: default
title: Methotrexate
parent: 僅模型預測 (L5)
nav_order: 651
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

# Methotrexate: From Established Oncologic/Autoimmune Indications to Pulmonary Blastoma

## One-Sentence Summary

Methotrexate (MTX, DrugBank DB00563) is an antifolate agent whose established international uses span hematologic malignancies and autoimmune conditions such as rheumatoid arthritis.
The TxGNN model predicts it may be effective for **Pulmonary Blastoma**, but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a pure knowledge-graph-based prediction with no direct or indirect clinical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in the local market; internationally established for hematologic malignancies (e.g., acute lymphoblastic leukemia, lymphomas) and autoimmune diseases (e.g., rheumatoid arthritis) |
| Predicted New Indication | Pulmonary Blastoma |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is currently unavailable (flagged as a High-severity data gap, DG002). Based on known pharmacology, methotrexate is a folate antagonist that inhibits dihydrofolate reductase (DHFR), blocking purine and pyrimidine synthesis and thereby suppressing rapidly dividing cells. This mechanism underlies its established efficacy across a range of hematologic malignancies and its immunomodulatory effect in autoimmune disease.

For Pulmonary Blastoma specifically, however, there is no clinical trial or published literature evidence in this evidence pack. The model's rationale notes that the prediction is likely driven by MTX's existing knowledge-graph connections to other pulmonary or embryonal tumor entities, rather than by any direct or indirect clinical signal specific to pulmonary blastoma.

Because pulmonary blastoma is a rare, biologically distinct pulmonary neoplasm (with both epithelial and blastemal/sarcomatous components), the applicability of a generic antifolate mechanism cannot be assumed from structural similarity alone. This candidate therefore sits at the earliest, most speculative end of the evidence spectrum — a hypothesis generated purely by model structure, not by any accumulated clinical or mechanistic data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Methotrexate currently has no registered product license in the local market (0 registrations; market status: Not Marketed). No authorization records are available to tabulate.

---

## Cytotoxicity

Methotrexate is classified as antineoplastic based on its established use as a conventional cytotoxic chemotherapeutic (antifolate/antimetabolite class), independent of the specific new indication under evaluation.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate/antimetabolite — DHFR inhibitor) |
| Myelosuppression Risk | High — class-effect of antimetabolite chemotherapy; high-dose regimens require leucovorin rescue and hematologic monitoring |
| Emetogenicity Classification | Low (oral, low-dose) to Moderate (high-dose intravenous regimens) |
| Monitoring Items | CBC with differential, renal function (creatinine clearance, critical for MTX elimination), liver function tests, serum MTX levels for high-dose/leucovorin-rescue protocols |
| Handling Protection | Yes — requires handling under cytotoxic/hazardous drug precautions (personal protective equipment, closed-system transfer where applicable) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature support (Evidence Level L5, Decision Stage S0) and is based solely on TxGNN structural inference. In addition, a Blocking-severity data gap (DG001: local safety labeling/warnings and contraindications) prevents this candidate from even entering the S1 safety pre-assessment stage.

**To proceed, the following is needed:**
- Local regulatory safety labeling (warnings/contraindications) to clear the Blocking data gap (DG001)
- Detailed mechanism-of-action data (DG002) to support a mechanistic rationale specific to pulmonary blastoma
- At minimum, preclinical or case-level evidence directly addressing MTX activity in pulmonary blastoma before any further investment
- As an alternative research priority within this same evidence pack, other TxGNN-predicted indications for methotrexate show materially stronger evidence maturity — notably Hodgkin's lymphoma (L2, Decision Stage S2, "Proceed with Guardrails") and small cell lung carcinoma (L2, S1) — and may warrant evaluation ahead of this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

