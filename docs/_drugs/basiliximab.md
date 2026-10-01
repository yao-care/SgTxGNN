---
layout: default
title: Basiliximab
parent: Medium Evidence (L3-L4)
nav_order: 137
evidence_level: L3
indication_count: 10
---

# Basiliximab
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Basiliximab: From Kidney Transplant Rejection Prophylaxis to Plasma Cell Myeloma

## One-Sentence Summary

Basiliximab is an anti-CD25 (IL-2 receptor) antibody, generally used to prevent acute rejection after organ transplantation. The Singapore registration record does not state an approved indication.
The TxGNN model predicts it may be useful for **Plasma Cell Myeloma**, mainly as an immune-modulating add-on around stem cell transplant.
The evidence is early: **3 related clinical trials** (the only completed myeloma-specific one is Phase 1) and **3 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prophylaxis of acute organ rejection in transplantation (general pharmacology; no indication text in the Singapore record) |
| Predicted New Indication | Plasma cell myeloma |
| TxGNN Prediction Score | 95.61% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on general pharmacology, basiliximab is an antibody that blocks CD25 (the IL-2 receptor alpha chain). CD25 is found on activated T cells and on regulatory T cells (Tregs).

In transplant medicine, blocking this receptor dampens harmful T-cell activity. In myeloma, the idea is different. Tregs recover quickly after autologous stem cell transplant (ASCT) and may suppress the immune response against myeloma cells. Removing them could strengthen post-transplant anti-myeloma immunity. Basiliximab has also been used around allogeneic transplant to prevent graft-versus-host disease (GVHD).

The drug is therefore an **immune-modulating adjunct**, not a direct anti-myeloma cytotoxic. The link between the original use and myeloma is indirect, and the current evidence supports feasibility and safety rather than efficacy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01526096](https://clinicaltrials.gov/study/NCT01526096) | Phase 1 | Completed | 30 | Pilot of regulatory T-cell reduction in myeloma patients undergoing ASCT, testing feasibility and safety. The most direct evidence here. |
| [NCT00975975](https://clinicaltrials.gov/study/NCT00975975) | Phase 2 | Completed | 17 | Basiliximab plus cyclosporine to prevent GVHD after nonmyeloablative allotransplant for blood cancers. The endpoint is GVHD, not myeloma control. Appears to be a small single-arm study. |
| [NCT00594308](https://clinicaltrials.gov/study/NCT00594308) | N/A | Terminated | 10 | Basiliximab plus cyclosporine versus cyclosporine alone for GVHD prevention. Not myeloma-specific, and the small terminated study yields little usable data. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31940591](https://pubmed.ncbi.nlm.nih.gov/31940591/) | 2020 | Clinical study | J Immunother Cancer | Pilot study of Treg depletion around ASCT for myeloma. Tregs recover quickly after ASCT and may inhibit anti-myeloma immunity. |
| [12476283](https://pubmed.ncbi.nlm.nih.gov/12476283/) | 2002 | Clinical study | Bone Marrow Transplant | Basiliximab in 17 patients with steroid-refractory acute GVHD after allogeneic transplant, reported as well tolerated and effective. The group included a few patients with myeloma among other blood cancers. |
| [28320553](https://pubmed.ncbi.nlm.nih.gov/28320553/) | 2017 | Case reports | Am J Kidney Dis | Four patients with myeloma-related kidney failure who received kidney transplants after achieving myeloma control. Background for the transplant setting, not direct evidence for basiliximab. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10441P | SIMULECT FOR INJECTION 20 mg/vial | Injection, powder, for solution | Not stated in the registry record |

## Safety Considerations

Please refer to the package insert for safety information. Drug interaction records were not found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The myeloma evidence is limited to one completed Phase 1 pilot and small transplant-setting studies, with no efficacy data. The Singapore package insert safety information is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications from the HSA website
- Mechanism of action data from DrugBank
- Efficacy data from a Phase 2 or larger myeloma-specific study of Treg depletion
- Clarification of whether the pilot's Treg-depletion approach used basiliximab or another agent

The other nine TxGNN predictions have weaker support. Bronchitis and the hemoglobinopathy entries rest only on transplant-setting evidence, and the rest have no clinical evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

