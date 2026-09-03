---
layout: default
title: Selinexor
parent: 僅模型預測 (L5)
nav_order: 893
evidence_level: L5
indication_count: 10
---

# Selinexor
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

Using the TxGNN evidence pack directly. Note: I selected **progesterone-receptor negative breast cancer (rank 3)** rather than the top-ranked prediction (drug-induced osteoporosis) as the lead candidate — the evidence pack's own rationale for rank 1 states it contradicts known Selinexor bone-safety signals and should be treated as likely model noise. Rank 3 is the only candidate with an actual completed clinical trial and a coherent, correct mechanistic rationale.

---

# Selinexor: From an XPO1-Targeted Oncology Agent to Progesterone-Receptor Negative Breast Cancer

## One-Sentence Summary

> Selinexor is a Selective Inhibitor of Nuclear Export (SINE) targeting XPO1/CRM1; its originally approved indication is not recorded in this evidence pack (data gap).
> The TxGNN model predicts potential efficacy in **Progesterone-Receptor Negative Breast Cancer** (including triple-negative breast cancer),
> currently supported by **1 completed Phase 2 clinical trial** and **no dedicated literature**, placing this at an early, hypothesis-generating stage of evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current evidence pack (data gap — DG002) |
| Predicted New Indication | Progesterone-Receptor Negative Breast Cancer |
| TxGNN Prediction Score | 97.20% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed drug-level mechanism-of-action data is not yet available in this evidence pack (flagged as Data Gap DG002, remediation pending via DrugBank API). However, the evidence-specific rationale attached to this prediction describes Selinexor as an XPO1/CRM1 nuclear export inhibitor: it blocks the export of tumour-suppressor proteins (p53, FOXO3a, IκB, etc.) out of the nucleus, causing their intranuclear accumulation, reactivation, and induction of apoptosis in cancer cells.

Triple-negative and progesterone-receptor negative breast cancers frequently show XPO1 overexpression and p53 pathway dysregulation, which provides a plausible mechanistic rationale for this indication. This is corroborated by a completed, investigator-initiated Phase 2 trial testing single-agent Selinexor specifically in metastatic triple-negative breast cancer.

The main limitation is specificity: the mechanistic link to hormone-receptor status (rather than TNBC broadly) has not been established, and the supporting trial was small and uncontrolled — so this should be read as a credible research signal rather than confirmed efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02402764](https://clinicaltrials.gov/study/NCT02402764) | Phase 2 | Completed | 10 | Investigator-initiated study of single-agent Selinexor (KPT-330) in metastatic triple-negative breast cancer, evaluating efficacy, safety, and tolerability. Small, single-arm, exploratory (Grade A relevance per evidence review, but limited by sample size and lack of a control arm). |

---

## Literature Evidence

Currently no related literature available for this indication.

---

## Singapore Market Information

Selinexor is currently **not marketed** in Singapore (0 registrations, no license records available). No product/dosage-form information can be extracted from this evidence pack.

---

## Cytotoxicity

Selinexor is an antineoplastic agent (XPO1/CRM1-targeted small molecule used in oncology).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Selective Inhibitor of Nuclear Export) |
| Myelosuppression Risk | Not quantified in this evidence pack; please refer to the package insert |
| Emetogenicity Classification | Not quantified in this evidence pack; please refer to the package insert |
| Monitoring Items | Please refer to package insert warnings and precautions |
| Handling Protection | Follow institutional cytotoxic/hazardous drug handling protocol pending label confirmation |

---

## Safety Considerations

Please refer to the package insert for safety information. Drug-level safety data (key warnings, contraindications, drug-drug interactions) are currently a **blocking data gap (DG001)** — the Singapore/TFDA label has not yet been retrieved and parsed, so no formal safety pre-screening (S1) can be completed at this time.

---

## Other Predicted Indications (Screened, Low Confidence)

For completeness, 9 additional indications were predicted by TxGNN for Selinexor but are **not recommended for further action** at this time:

- **HER2-positive breast carcinoma** (rank 2, L4) — only indirect literature (an endometrial cancer review), no direct trial evidence.
- **Squamous cell lung carcinoma** (rank 7, L4) — two relevant Phase 1/2 trials exist but one was **terminated** and the other **withdrawn with zero enrollment**, suggesting feasibility/safety concerns rather than support.
- **Drug-induced osteoporosis** (rank 1, L5) — the highest TxGNN score, but the evidence pack's own rationale flags this as likely **model noise**: known Selinexor safety signals (bone density concerns, weight loss) point in the *opposite* direction from a therapeutic indication.
- **Normal breast-like subtype, PR-positive breast cancer, gestational trophoblastic neoplasm, cervical neuroblastoma, schwannoma of jugular foramen** (ranks 4, 5, 8, 9, 10; all L5) — no supporting trials or literature.
- **Breast tumor luminal A/B** (rank 6, L5) — the 19 retrieved "literature" hits are an artifact of a "B" keyword mismatch (B-cell biology, hepatitis B vaccines) and are not genuine evidence for this indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Only one small, uncontrolled Phase 2 trial (N=10) supports the leading credible candidate (PR-negative/triple-negative breast cancer), and drug-level MOA and safety data remain unverified (blocking data gap). This is sufficient to justify a research question but not to proceed toward a formal repurposing pathway.

**To proceed, the following is needed:**
- Retrieve and parse the TFDA/HSA package insert for warnings, contraindications, and DDI (DG001, blocking)
- Confirm mechanism of action via DrugBank API (DG002)
- Additional controlled trial data (ideally randomized, larger N) in PR-negative/TNBC populations
- Re-review the "drug-induced osteoporosis" prediction against known bone-safety signals before any further use — likely exclude as a model artifact
- Disregard low-evidence (L5) predictions unless new trial or literature evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

