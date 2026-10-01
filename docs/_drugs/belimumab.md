---
layout: default
title: Belimumab
parent: Low Evidence (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
---

# Belimumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Belimumab: From Systemic Lupus Erythematosus to Primary Release Disorder of Platelets

## One-Sentence Summary

Belimumab is a biologic that blocks the B-cell survival factor BLyS (BAFF). It is best known for treating systemic lupus erythematosus, although the supplied Singapore registration record does not state its approved indication.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, with a very high score.
Only **1 clinical trial** was found, and it studied a different disease, and there are **0 publications**, so this prediction is essentially unsupported.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Systemic lupus erythematosus (general drug knowledge; not stated in the supplied Singapore licence records) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Belimumab neutralizes soluble BLyS (BAFF), which reduces B-cell survival and autoantibody production. That is why it suits antibody-driven autoimmune diseases.

Primary platelet release disorders, however, are intrinsic defects in platelet function. They are not driven by B cells or BAFF, so there is no credible mechanistic link. The very high TxGNN score reflects proximity in the knowledge graph rather than a real biological connection.

The predictions ranked 2 to 8 and 10 (including pseudo-von Willebrand disease, autosomal dominant macrothrombocytopenia and two granulomatous diseases) also lack a plausible mechanism or any evidence. Two are only speculative: Glanzmann thrombasthenia (rank 3) and fetal and neonatal alloimmune thrombocytopenia (rank 4). Neither has supporting data.

The one prediction with a biologically plausible rationale is **inflammatory bowel disease** (rank 9, score 97.76%). BAFF is reported to be elevated in IBD mucosa and serum (PMIDs [35054212](https://pubmed.ncbi.nlm.nih.gov/35054212/) and [27655102](https://pubmed.ncbi.nlm.nih.gov/27655102/)). Even so, no IBD-specific belimumab efficacy trial could be confirmed, so it stays at L4.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01610492](https://clinicaltrials.gov/study/NCT01610492) | Phase 2 | Completed | 14 | Open-label mechanistic study of belimumab in anti-PLA2R antibody-positive idiopathic membranous glomerulonephropathy. It is a different disease with no platelet endpoint, so it gives no support for this indication. |

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14211P | Benlysta Powder for Solution for Infusion 120mg | Lyophilized powder for injection | Not stated in the supplied record |
| SIN14212P | Benlysta Powder for Solution for Infusion 400mg | Lyophilized powder for injection | Not stated in the supplied record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has no supporting mechanism, no relevant trials and no literature (L5). The only registered trial concerns a different disease, and the high TxGNN score does not reflect real biological or clinical support.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications and approved indication), which is currently missing and blocks safety screening
- Confirmation of the approved indication and mechanism of action from DrugBank
- A shift of review focus to inflammatory bowel disease, the only prediction with a plausible mechanism, starting with verification of the registry record for NCT03844061 to confirm its target condition
- Any IBD-specific belimumab efficacy data, before considering a higher evidence level
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

