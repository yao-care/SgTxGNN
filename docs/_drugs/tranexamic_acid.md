---
layout: default
title: Tranexamic Acid
parent: 僅模型預測 (L5)
nav_order: 1001
evidence_level: L5
indication_count: 10
---

# Tranexamic Acid
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

# Tranexamic Acid: From Heavy Menstrual Bleeding to Amenorrhea (Disease)

## One-Sentence Summary

> Tranexamic acid (TXA) is an antifibrinolytic agent whose established use — noted directly in the evidence pack's own mechanistic analysis — is reducing **heavy menstrual bleeding (menorrhagia)**, not treating amenorrhea.
> The TxGNN model's top prediction points to **Amenorrhea (disease)**, but with only **0 clinical trials** and **2 review-level publications**, and the evidence pack itself flags this as a likely knowledge-graph mapping artifact rather than a genuine therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Heavy menstrual bleeding / menorrhagia (as referenced in the drug's known mechanism; not independently confirmed via Singapore licensing data) |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available as a structured field for this drug (data gap DG002), but the evidence pack's own rationale text describes tranexamic acid as a lysine analogue that competitively blocks lysine-binding sites on plasminogen, inhibiting plasmin activation and thereby reducing fibrinolysis. This antifibrinolytic action is the pharmacological basis for its established use in reducing heavy menstrual bleeding — i.e., it works by **reducing** bleeding, not by suppressing menstruation itself.

This creates a direct mechanistic conflict with the predicted indication of amenorrhea (absence of menstruation). Amenorrhea and heavy menstrual bleeding are, if anything, opposite ends of the same physiological spectrum, and an antifibrinolytic that curbs excess bleeding has no established pathway toward inducing or treating amenorrhea. The two supporting publications reinforce this mismatch: both discuss management of abnormal uterine bleeding and menstrual suppression/prophylaxis in bleeding-prone patients — topics adjacent to menstrual bleeding control, not to amenorrhea treatment.

Given this, the most plausible explanation is that the TxGNN prediction reflects a **disease-ontology mapping error** — the "amenorrhea" node in the knowledge graph may be clustering with menstrual-bleeding-related concepts rather than representing a distinct, clinically accurate target. This should be treated as a data-quality flag requiring verification before any further evaluation, not as a validated repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause (New York, N.Y.) | Reviews pharmacological therapy for abnormal uterine bleeding; discusses agents (including antifibrinolytics) that reduce bleeding volume — the focus is bleeding control, not amenorrhea induction. |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Review/Guideline | Journal of Oncology Pharmacy Practice | Systematic approach to menses prophylaxis and suppression in premenopausal hematologic cancer patients with treatment-related cytopenias; relates to menstrual suppression strategies in a bleeding-risk context, not to amenorrhea as a treatable disease. |

---

## Singapore Market Information

This drug is currently **not marketed** in Singapore under this evidence pack (0 registrations, no license records available). No product-level authorization data can be presented.

---

## Safety Considerations

Structured safety data (key warnings, contraindications, DDI) is not available in this evidence pack (data gap DG001, marked **Blocking** — TFDA/HSA label warnings and contraindications must still be obtained before any safety evaluation). Please refer to the package insert for safety information.

**Additional signal worth flagging:** Other TxGNN predictions for this drug (ranks 2–4: heparin cofactor II deficiency, Factor V excess with spontaneous thrombosis, antithrombin deficiency type 2) all involve congenital thrombophilia. For these, the evidence pack's own analysis notes that tranexamic acid's antifibrinolytic action could theoretically **increase** thrombotic risk rather than provide benefit — the opposite of a therapeutic signal. This reinforces that this evidence pack contains multiple likely knowledge-graph artifacts and at least one potential safety-direction conflict that should be considered when interpreting the top-ranked prediction.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (amenorrhea) directly contradicts the drug's known antifibrinolytic mechanism and is unsupported by any clinical trial evidence; the two available publications discuss the opposite clinical scenario (bleeding management, not amenorrhea treatment). Combined with a Blocking data gap on TFDA/HSA safety labeling and the drug's non-marketed status in Singapore, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- Verify the "amenorrhea (disease)" node mapping in the underlying knowledge graph to rule out an ontology/clustering error
- Obtain TFDA/HSA label data (warnings, contraindications) — currently a Blocking gap (DG001)
- Obtain structured mechanism-of-action data from DrugBank (DG002)
- If the disease mapping is confirmed correct, identify primary literature (not reviews) that directly studies TXA in an amenorrhea context before further evaluation
- Reassess ranks 2–4 as potential **safety contraindication signals** (thrombophilia) rather than repurposing opportunities
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

