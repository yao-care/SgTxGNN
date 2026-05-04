---
layout: default
title: Cyclosporine
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Cyclosporine
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

# Cyclosporine: From GVHD Prevention to Chronic Granulomatous Disease

## One-Sentence Summary

Cyclosporine is a calcineurin inhibitor with a well-established role in preventing graft-versus-host disease (GVHD) in allogeneic hematopoietic stem cell transplantation (HSCT) and rejecting in solid organ transplantation.
The TxGNN model predicts it may be effective for **Chronic Granulomatous Disease (CGD, autosomal recessive form)**,
with **1 clinical trial** and **1 publication** currently supporting this direction — primarily in the context of HSCT as a curative therapy for CGD.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | GVHD prophylaxis / organ transplant rejection prevention |
| Predicted New Indication | Granulomatous Disease, Chronic, Autosomal Recessive (CGD) |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data pack. Based on known pharmacology, Cyclosporine is a calcineurin inhibitor that suppresses T-cell activation by blocking calcineurin-mediated transcription of interleukin-2 (IL-2) and other pro-inflammatory cytokines. This immunosuppressive action has made it a standard backbone of transplant immunosuppression regimens and GVHD prophylaxis across multiple organ transplant settings.

Chronic Granulomatous Disease (CGD) is a primary immunodeficiency caused by inherited defects in the NADPH oxidase complex, leading to recurrent life-threatening bacterial and fungal infections and pathological granuloma formation. The only established curative treatment for CGD is allogeneic HSCT. In this clinical scenario, Cyclosporine plays a well-recognised and necessary role as a GVHD prophylaxis agent — enabling the transplant procedure that cures CGD — rather than directly targeting CGD's underlying pathophysiology (NADPH oxidase dysfunction).

The mechanistic link is therefore **indirect and context-limited**: Cyclosporine is not being repurposed to treat CGD per se, but its essential role in the HSCT protocol that cures CGD may be what the TxGNN model's knowledge graph is capturing. The high prediction score (99.68%) likely reflects graph adjacency between Cyclosporine's HSCT/immunosuppression nodes and CGD's curative transplant pathway, rather than a novel biological hypothesis. This distinction is critical for evaluating true repurposing potential.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01917708](https://clinicaltrials.gov/study/NCT01917708) | Phase 1 | Completed | 10 | Assessed tolerability of abatacept (CTLA4-Ig) combined with cyclosporine and mycophenolate mofetil as GVHD prophylaxis in children undergoing unrelated donor HSCT for serious non-malignant diseases including CGD; participants followed for 2 years. Cyclosporine was a background prophylaxis agent, not the primary intervention. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [22078471](https://pubmed.ncbi.nlm.nih.gov/22078471/) | 2012 | Retrospective Cohort | J Allergy Clin Immunol | Demonstrated excellent survival outcomes following matched related donor (MRD) and matched unrelated donor (MUD) HSCT for CGD, supporting the effectiveness of HSCT — within which CsA-based GVHD prophylaxis is standard — as a curative treatment approach. |

---

## Singapore Market Information

Cyclosporine currently has **no registered products** in Singapore's drug regulatory database.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | No registered products found | — | — |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence linking Cyclosporine to CGD is indirect — its role is as a GVHD prophylaxis enabler within HSCT protocols that cure CGD, not as a direct treatment for CGD pathophysiology. The sole clinical trial (NCT01917708, Phase 1, n=10) used Cyclosporine as a background agent alongside abatacept, and the single literature reference is a retrospective HSCT outcomes study. This body of evidence does not constitute a novel repurposing claim distinct from Cyclosporine's established GVHD prophylaxis role; the L3 rating reflects supportive but indirect data.

**To proceed, the following is needed:**

- **Clarification of the repurposing hypothesis**: Is the intended claim (a) optimising CsA-based GVHD prophylaxis regimens specifically for CGD patients undergoing HSCT (a refinement of existing use), or (b) using CsA as a direct immunomodulatory therapy for CGD outside the HSCT context (a genuinely novel claim requiring de novo evidence)?
- **Mechanism of action data (MOA)**: DrugBank API query needed to confirm whether CsA has any biologically plausible direct interaction with CGD pathophysiology (NADPH oxidase pathway, granuloma regulation)
- **Safety data**: Official package insert must be retrieved (TFDA / Singapore HSA) to complete the S1 safety screening, currently blocked per Data Gap DG001
- **Prospective clinical data**: If the novel direct-use hypothesis is pursued, at minimum a prospective case series or pilot study evaluating CsA monotherapy or combination therapy in CGD management outside transplant conditioning would be required before advancing to S2
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

