---
layout: default
title: Thrombin
parent: 僅模型預測 (L5)
nav_order: 974
evidence_level: L5
indication_count: 10
---

# Thrombin
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

# Thrombin: From Topical Hemostasis to Primary Release Disorder of Platelets

## One-Sentence Summary

> Thrombin (DrugBank DB11300) is a serine protease that converts fibrinogen to fibrin and is widely used clinically as a topical/local hemostatic agent — a use documented only indirectly in this evidence pack's literature, since Singapore regulatory records (HSA) and formal MOA data are both flagged as data gaps.
> The TxGNN model predicts a possible link to **Primary Release Disorder of Platelets**, with a high similarity score but only **L4 (mechanism/preclinical)** supporting evidence.
> Critically, the evidence pack's own mechanistic review flags this specific link as biologically counterintuitive — thrombin *activates* platelets, it does not correct a granule-release defect — so this candidate should be treated as a low-confidence signal, not a validated repurposing lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in regulatory data on file (Blocking data gap DG001). Literature within this pack indicates established use as a **topical/local hemostatic agent**. |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 96.82% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Thrombin is not available in this evidence pack (data gap DG002). Based on general pharmacology and the literature retrieved here, Thrombin is a coagulation-cascade serine protease that cleaves fibrinogen to fibrin and, at the cellular level, is one of the most potent physiological **activators** of platelets, signaling through the PAR1/PAR4 receptors. Its established clinical role — topical hemostasis during surgery and endoscopic control of variceal bleeding — depends on this activating, pro-coagulant action.

**Primary release disorder of platelets**, however, is a condition in which platelets fail to secrete the contents of their storage granules upon activation — the defect lies *downstream* of activation, not in the activation step itself. Administering an activating agonist like thrombin does not address a release-machinery defect; if anything, the mechanistic literature retrieved here (e.g., studies on thrombin-induced arachidonic acid release and granule secretion in normal platelets) describes thrombin as the *stimulus* used to study release, not a therapy for its failure.

Taken together, this suggests the TxGNN score for this pairing most likely reflects a knowledge-graph co-occurrence artifact — thrombin appears frequently in the literature graph alongside "platelet" and "release" terminology because it is the standard laboratory reagent used to trigger and study platelet release, not because it treats disorders of that process. The evidence pack's own repurposing rationale reaches the same conclusion, which is why the recommendation defaults to **Hold**.

---

## Clinical Trial Evidence

No clinical trials directly test Thrombin as a treatment for primary release disorder of platelets. Of the trials retrieved via knowledge-graph search, only three have completed relevance grading; the majority remain "pending" and, on inspection of their titles/summaries, are unrelated general coagulation, oncology, or COVID-19 studies (KG search noise).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01957852](https://clinicaltrials.gov/study/NCT01957852) | N/A | Completed | 86 | Tested FloSeal, a thrombin-based hemostatic matrix, for reducing intra-abdominal bleeding after cytoreductive surgery + HIPEC. Shows a real-world thrombin-containing product used for **general surgical hemostasis**, not for this specific disease (Grade B — adjacent relevance only). |
| [NCT00043940](https://clinicaltrials.gov/study/NCT00043940) | Phase 3 | Completed | 50 | Tested bivalirudin (not thrombin) as anticoagulant during PCI in heparin-induced thrombocytopenia (HIT) patients (Grade C — not relevant). |
| [NCT05806346](https://clinicaltrials.gov/study/NCT05806346) | N/A | Recruiting | 764 | Compares tranexamic acid dosing strategies for bleeding in cardiac surgery (Grade C — not relevant). |

---

## Literature Evidence

No clinical or therapeutic literature supports using thrombin to treat this disease. The following are the most mechanistically related basic-science/review articles retrieved; all describe thrombin as a platelet **agonist** used to study — not treat — the release reaction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [984037](https://pubmed.ncbi.nlm.nih.gov/984037/) | 1976 | Basic Science | American Journal of Hematology | Thrombin stimulates arachidonic acid release from platelet phospholipids as part of the normal activation/release cascade — thrombin as trigger, not treatment. |
| [1321709](https://pubmed.ncbi.nlm.nih.gov/1321709/) | 1992 | Review | Disease-a-Month | Overview of platelet function disorders across adhesion, aggregation, secretion, and procoagulant phases; thrombin is described as generating the coagulation surface, not as a release-defect therapy. |
| [26584277](https://pubmed.ncbi.nlm.nih.gov/26584277/) | 2015 | Basic Science | Cell Physiol Biochem | Thrombin and collagen-related peptide drive Orai1-mediated calcium entry during platelet activation — mechanistic background on thrombin as an activator. |
| [2016486](https://pubmed.ncbi.nlm.nih.gov/2016486/) | 1991 | Review | J Am Coll Cardiol | Reviews thrombin's role in platelet activation and restenosis after angioplasty — tangential to primary hemostasis biology, not disease-specific therapy. |

---

## Singapore Market Information

Thrombin currently has **no HSA-registered products in Singapore** (0 licenses on file; market status: 未上市 / not marketed). No authorization numbers, product names, or approved-indication text are available for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug–drug interaction data are available in this evidence pack (all fields returned as data gaps; DDI query status: not found). This is documented as a **Blocking** data gap (DG001) that must be resolved before any S1 safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high similarity score (96.82%) to this drug–disease pair, the supporting evidence is limited to mechanism-level literature (L4) with no clinical trials testing this specific use, and the evidence pack's own mechanistic rationale indicates the pairing is biologically implausible — thrombin activates platelets rather than correcting a granule-release defect. Combined with the Blocking data gap on MOA and safety/regulatory labeling, and the drug's complete absence from the Singapore market, this candidate does not meet the bar to advance.

**To proceed, the following is needed:**
- Confirmed MOA and pharmacology data for Thrombin (resolve DG002)
- TFDA/HSA label data — warnings, contraindications, DDI (resolve DG001, Blocking)
- Hematology/expert review confirming whether any paradoxical or localized rationale exists for using a platelet activator in a release-disorder context (currently none identified)

**Note for portfolio prioritization:** Within this same evidence pack, a different predicted indication for Thrombin — *esophageal disease* (rank 5, gastric/esophageal variceal bleeding) — has substantially stronger support: evidence level **L3**, a Grade-1 systematic review/meta-analysis on thrombin for bleeding gastric varices, multiple cohort studies, and an established clinical technique (endoscopic thrombin injection), with a scoring recommendation of **Proceed with Guardrails**. That candidate is a far more credible repurposing lead than the one reported here and may warrant its own dedicated evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

