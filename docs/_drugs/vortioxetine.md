---
layout: default
title: Vortioxetine
parent: 僅模型預測 (L5)
nav_order: 1067
evidence_level: L5
indication_count: 10
---

# Vortioxetine
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

# Vortioxetine: From Major Depressive Disorder to Neurotic Disorder

## One-Sentence Summary

Vortioxetine is a multimodal serotonergic antidepressant currently approved internationally for major depressive disorder (MDD).
The TxGNN model predicts it may be effective for **Neurotic Disorder** (an older diagnostic category spanning mild depressive and anxiety presentations),
with **1 large real-world cohort study** and **1 published case review** currently supporting this direction. Note: Singapore-specific regulatory approval data and formal mechanism-of-action documentation are not yet available for this candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major Depressive Disorder (based on known international use; no Singapore license record available) |
| Predicted New Indication | Neurotic Disorder |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from the formal regulatory record is not available for Vortioxetine. Based on the literature evidence contained in this evidence pack, Vortioxetine is a multimodal serotonergic antidepressant — it inhibits the serotonin transporter (SERT) while acting as an antagonist at 5-HT3, 5-HT7 and 5-HT1D receptors, a partial agonist at 5-HT1B, and a full agonist at 5-HT1A. Its efficacy in major depressive disorder has been well established through multiple Phase 3 randomized controlled trials, and mechanistically this broad serotonergic modulation may extend to related mood and anxiety presentations.

"Neurotic disorder" is an older diagnostic classification that encompasses mixed anxiety and mild-to-moderate depressive symptomatology. Because it overlaps conceptually with conditions already addressed by serotonergic antidepressants, there is partial mechanistic plausibility for Vortioxetine's use in this category. However, as the rationale notes, the indication definition itself is diagnostically imprecise by modern standards (it maps loosely onto ICD-9-era terminology), and no clinical trial in the evidence pack specifically targets this diagnosis.

The single supporting clinical trial (NCT04446039) is a large real-world claims-database cohort study comparing antidepressant utilization patterns broadly, not a study designed around "neurotic disorder" specifically — it was graded "B" relevance for this reason. The one literature reference is a case-based review of neurotic depression treatment, which is a related but distinct concept from the ranked disease term. Taken together, the evidence supports biological plausibility but not diagnosis-specific clinical validation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04446039](https://clinicaltrials.gov/study/NCT04446039) | N/A (Real-world cohort) | Completed | 370,212 | Nationwide claims database study comparing medication utilization patterns and adverse outcome risk across commonly used antidepressants; not specific to neurotic disorder diagnosis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31006795](https://pubmed.ncbi.nlm.nih.gov/31006795/) | 2019 | Review (case report) | Zhurnal nevrologii i psikhiatrii imeni S.S. Korsakova | Case-based discussion of neurotic depression, noting benefit of combined antidepressant and cognitive behavioral therapy approach; not Vortioxetine-specific. |

---

## Singapore Market Information

No Singapore license or registration records are currently available for Vortioxetine in this evidence pack (0 licenses on file). Market status is confirmed as **not marketed**.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-drug interaction data were retrievable at this time (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication "Neurotic Disorder" is currently supported only by indirect evidence (L2) — a broad real-world antidepressant utilization study and a single non-Vortioxetine-specific case review — rather than a diagnosis-targeted trial. Combined with a **blocking data gap** on TFDA/Singapore label warnings and contraindications (DG001) and the absence of formal mechanism-of-action documentation (DG002), the candidate is not yet ready to advance past the research-question stage.

**To proceed, the following is needed:**
- Obtain official Singapore/regional package insert data (warnings, contraindications) to clear the blocking safety gap (DG001)
- Confirm formal mechanism-of-action documentation via DrugBank API (DG002)
- Seek trials or literature specifically diagnosing "neurotic disorder" (ICD-9 300.x spectrum) rather than general antidepressant-utilization studies
- Consider that closely related predicted indications in this evidence pack — **neurotic depression** and **melancholia** — carry substantially stronger evidence (L1, multiple Phase 3 RCTs, "Proceed with Guardrails") and may represent a more actionable repurposing pathway than "neurotic disorder" itself, since both map closely onto the already-approved MDD indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

