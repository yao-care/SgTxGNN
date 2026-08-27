---
layout: default
title: Fondaparinux
parent: 僅模型預測 (L5)
nav_order: 447
evidence_level: L5
indication_count: 10
---

# Fondaparinux
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

Using the evidence pack provided, here is the drug repurposing evaluation report for Fondaparinux.

---

# Fondaparinux: From Anticoagulation Therapy to Primary Release Disorder of Platelets

## One-Sentence Summary

Fondaparinux (DrugBank DB00569) is a synthetic indirect Factor Xa inhibitor used clinically for anticoagulation; its specific original approved indication is not recorded in this evidence pack (the drug is currently **not marketed in Singapore**). The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, with a prediction score of **93.06%**, but the supporting evidence base is thin — only **2 clinical trials** and **2 publications**, and the evidence pack itself flags a likely disease-ontology mismatch between the predicted term and the actual disease studied in the cited trials (heparin-induced thrombocytopenia, HIT, rather than a platelet-storage disorder).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (`original_indications` is empty; drug is unmarketed in Singapore). Trial context in the evidence pack indicates use in anticoagulation (e.g., atrial fibrillation cardioversion, HIT management). |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 93.06% (rank 30,547) |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Fondaparinux is flagged as a data gap (`original_moa: [Data Gap]`, DG002, High severity) and could not be pulled from DrugBank at this cutoff. However, the evidence pack's own repurposing-rationale field describes Fondaparinux as an **indirect Factor Xa inhibitor that does not bind platelet factor 4 (PF4)** — the pharmacological basis for its established use as an anticoagulant alternative in patients with heparin-induced thrombocytopenia (HIT), since it can avoid the PF4-mediated immune cross-reaction that drives HIT.

Critically, the evidence pack raises a strong internal caveat about this specific prediction: the target disease label "primary release disorder of platelets" most likely corresponds to a **congenital platelet storage pool disease**, a *bleeding* disorder — not HIT, which is an immune-mediated *thrombotic* disorder. Both associated clinical trials (NCT00911300, NCT01178333) are actually about HIT and anticoagulation management, not about platelet storage pool disease. This strongly suggests a **knowledge-graph/disease-ontology mapping error** rather than a genuine mechanistic link between Fondaparinux and this specific predicted indication. Until this label mismatch is manually verified against a standard disease ontology (e.g., MONDO/UMLS), the high TxGNN score for this indication should be treated with caution rather than as direct support for a bleeding-disorder indication.

Additionally, one of the two supporting literature records (PMID 30018843, a case report on palliative chemotherapy in metastatic adenocarcinoma) does not appear topically related to Fondaparinux or platelet disorders at all, which further weakens confidence in the current evidence linkage for this specific candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00911300](https://clinicaltrials.gov/study/NCT00911300) | Phase 2 | Completed | 349 | International, multicentre, randomised pilot study testing whether Fondaparinux is effective and safe for preventing thromboembolic/bleeding events in atrial fibrillation patients undergoing electrical cardioversion, compared with heparin and vitamin-K antagonists. Relevance graded **B** (indirect) — population appears to be HIT-related rather than the predicted platelet-release disorder. |
| [NCT01178333](https://clinicaltrials.gov/study/NCT01178333) | N/A | Completed | 668 | HIT-RADIO: retrospective analysis of patients with a positive heparin PF-4 antibody test, examining incidence and outcomes (platelet counts, thrombosis, amputation, death). Non-interventional; relevance graded **C** (weak, epidemiological background only). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28646118](https://pubmed.ncbi.nlm.nih.gov/28646118/) | 2017 | Review | Blood | Review of direct oral anticoagulants (DOACs, e.g., rivaroxaban) for treatment of serologically confirmed HIT, based on the Hamilton (Canada) clinical experience; relevant to the anticoagulant-in-HIT context but does not directly evaluate Fondaparinux. |
| [30018843](https://pubmed.ncbi.nlm.nih.gov/30018843/) | 2017 | Case Report | Journal of the Advanced Practitioner in Oncology | Case report on palliative chemotherapy and palliative care in a patient with metastatic adenocarcinoma of unknown origin; topic does not appear related to Fondaparinux or platelet disorders — likely a low-relevance/mismatched literature link. |

---

## Singapore Market Information

Fondaparinux is currently **not registered or marketed in Singapore** (`total_licenses: 0`, `market_status: 未上市`). No license records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `key_warnings`, `contraindications`, and drug-drug interaction data are all recorded as data gaps in this evidence pack. In particular, DG001 — "TFDA/HSA label warnings/contraindications" — is flagged as a **Blocking** severity gap, meaning this candidate cannot yet complete even the initial safety screening stage (S1) until label data is retrieved and parsed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate cannot proceed past initial safety screening because the package-insert warnings/contraindications data is a **Blocking** gap (DG001), and the drug has no current market presence in Singapore (0 registrations). Furthermore, the top-ranked predicted indication itself carries a flagged, unresolved disease-ontology mismatch between the TxGNN label and the disease actually studied in the supporting trials, which undermines confidence in the evidence level (L3) currently assigned.

**To proceed, the following is needed:**
- Retrieve and parse HSA/TFDA package insert warnings and contraindications (DG001, Blocking)
- Obtain Fondaparinux mechanism-of-action data via DrugBank API (DG002, High)
- Manually verify whether "primary release disorder of platelets" is the correct disease-ontology mapping for the cited HIT-related trials and literature, or whether this is a knowledge-graph labeling error
- Re-screen literature evidence (particularly PMID 30018843) for actual topical relevance to Fondaparinux
- Confirm Singapore/regional regulatory pathway feasibility given the drug is currently unmarketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

