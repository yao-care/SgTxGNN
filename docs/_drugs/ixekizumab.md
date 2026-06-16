---
layout: default
title: Ixekizumab
parent: 僅模型預測 (L5)
nav_order: 508
evidence_level: L5
indication_count: 10
---

# Ixekizumab
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

# Ixekizumab: From Axial Spondyloarthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Ixekizumab (Taltz) is a high-affinity monoclonal antibody that selectively targets interleukin-17A (IL-17A), globally approved for moderate-to-severe plaque psoriasis, psoriatic arthritis, and axial spondyloarthritis — however, it is currently not registered in Singapore.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis** (TxGNN rank #1, score 97.53%),
with **1 peripherally related clinical trial** and **no directly supporting publications** available for this specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; globally approved for plaque psoriasis, psoriatic arthritis, and axial spondyloarthritis |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 97.53% |
| Evidence Level | L4 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known clinical and scientific context, Ixekizumab is a high-affinity IgG4 monoclonal antibody that selectively neutralises IL-17A — a key pro-inflammatory cytokine produced primarily by Th17 cells and innate lymphoid cells (ILC3). Its established efficacy across inflammatory arthritis has been confirmed in multiple Phase 3 RCTs including SPIRIT-P1/P2 (psoriatic arthritis) and COAST-V/W/X (radiographic and non-radiographic axial spondyloarthritis).

The proposed link to rheumatoid vasculitis carries theoretical biological plausibility: IL-17A promotes vascular endothelial cell activation, neutrophil infiltration, and vessel wall remodelling — all of which contribute to vascular inflammation in ANCA-associated vasculitis and rheumatoid arthritis (RA)-related vasculopathy. Th17-driven vascular wall damage is a recognised contributor to systemic inflammatory vasculopathy in advanced RA.

However, this mechanistic link remains speculative at present. No clinical trial has been designed specifically to evaluate Ixekizumab in rheumatoid vasculitis, and no published literature directly addresses this indication. The TxGNN model's high prediction score likely reflects topological proximity in the knowledge graph between spondyloarthritis/RA nodes and vasculitis nodes, rather than direct biological evidence supporting this repurposing hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Immunosuppressant management in rheumatology patients undergoing elective total shoulder arthroplasty — compares different perioperative hold durations on flare incidence, pain scores (VAS), functional outcomes (PROMIS), and wound complications; not a trial of Ixekizumab for rheumatoid vasculitis treatment |

> ⚠️ The only retrieved trial is Grade C (tangential relevance). It addresses perioperative immunosuppressant logistics in broad rheumatology patients — not the therapeutic efficacy of Ixekizumab in rheumatoid vasculitis. No dedicated clinical trials for this indication are currently registered.

---

## Literature Evidence

Currently no related literature available for Ixekizumab in rheumatoid vasculitis.

---

## Singapore Market Information

Ixekizumab is currently not registered in Singapore. No product authorizations or license records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite being TxGNN's top-ranked prediction for Ixekizumab (97.53%), rheumatoid vasculitis is supported only by mechanistic inference (L4). There are no dedicated clinical trials and no published literature directly addressing this indication; the single retrieved trial evaluates perioperative immunosuppressant management — not vasculitis efficacy. Proceeding without any clinical anchor point is premature, particularly given that the drug is not yet registered in Singapore even for its well-established indications.

**To proceed, the following is needed:**

- **Establish Singapore registration** for existing globally approved indications (psoriatic arthritis, axial spondyloarthritis) as a prerequisite before exploring rheumatoid vasculitis
- **Confirm MOA data** from DrugBank or published sources to formally characterise IL-17A's mechanistic role in rheumatoid vasculitis pathogenesis
- **Preclinical evidence search**: identify any animal models or in vitro studies demonstrating IL-17A inhibition reduces vascular inflammation in RA-associated vasculitis
- **Case series / off-label use review**: search for any case reports or real-world safety signals of Ixekizumab use in vasculitic RA
- **Safety data gap closure**: obtain full package insert (TFDA or FDA label) to review warnings, contraindications, and infection risk profile — critical given that rheumatoid vasculitis patients tend to have more severe, immunocompromised disease

> 📌 **Note on related predictions with stronger evidence:** While rheumatoid vasculitis ranks #1 by TxGNN score, two other predicted indications — **Inflammatory Spondylopathy** (rank #6, L1, 26 clinical trials, 20 publications) and **Vertebral Disease** (rank #9, L1, 4 Phase 3 trials including COAST-V/W/X, 20 publications) — have substantially stronger evidence bases and may represent more actionable repurposing or registration pathways for Singapore. These should be evaluated in separate reports.

---
*This report is for research reference only and does not constitute medical advice. All repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

