---
layout: default
title: Tagraxofusp
parent: 僅模型預測 (L5)
nav_order: 941
evidence_level: L5
indication_count: 10
---

# Tagraxofusp
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

# Tagraxofusp: From Blastic Plasmacytoid Dendritic Cell Neoplasm to Pre-Malignant Neoplasm

## One-Sentence Summary

> Tagraxofusp is a CD123-targeted diphtheria toxin fusion protein, publicly known to be approved for **Blastic Plasmacytoid Dendritic Cell Neoplasm (BPDCN)**.
> TxGNN's top-scored prediction for this drug (esotropia) was flagged by the model's own rationale as biologically implausible noise and is not reported here.
> The most defensible candidate is **Pre-malignant Neoplasm** (CD123⁺ myeloid pre-malignant states), supported indirectly by **5 clinical trials** in AML measurable residual disease (MRD) and myelofibrosis — but with **no direct trials or literature** for this disease label itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in Singapore regulatory data (drug not marketed); publicly referenced indication is Blastic Plasmacytoid Dendritic Cell Neoplasm (BPDCN), per trial documentation in this evidence pack |
| Predicted New Indication | Pre-malignant Neoplasm |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on information within this evidence pack, tagraxofusp is a protein–drug conjugate combining a diphtheria toxin payload with a CD123 (IL3RA)-targeting moiety, and is already approved for BPDCN, a CD123-expressing hematologic malignancy.

The rationale for extending into "pre-malignant neoplasm" rests on the observation that CD123 is also expressed on malignant/pre-malignant clones in myeloproliferative conditions — such as higher-risk myelofibrosis and measurable residual disease (MRD) in AML — which are biologically upstream of, or overlapping with, frank malignancy. This gives a plausible mechanistic bridge from BPDCN to pre-malignant myeloid states.

However, this bridge is indirect: none of the five supporting trials actually enroll patients with a diagnosis of "pre-malignant neoplasm." They study AML-MRD, relapsed/refractory pediatric hematologic malignancies, CD123⁺ AML (with a related but distinct molecule, IMGN632), and intermediate-risk myelofibrosis. The disease label itself appears to be a broad ontology match rather than a directly studied indication.

**Note on model output quality:** TxGNN's single highest-scoring prediction for this drug was "esotropia" (99.73% score), which the evidence pack's own mechanistic review explicitly characterizes as model noise with no biological plausibility (an eye-muscle/neuromuscular condition unrelated to a CD123-targeted antineoplastic toxin). It is excluded from this report. Several other top-10 candidates (inner ear neoplasm, benign tongue neoplasm, chondroid hamartoma, cystic neoplasm, thyroglossal duct cyst, non-seminomatous lesion) show the same pattern — near-identical scores with no supporting mechanism, trials, or literature — and one candidate ("ductular or ductular proliferation") returned 20 literature hits that are all hepatic fibrosis studies unrelated to tagraxofusp, a clear keyword-collision artifact. This cluster of near-tied, low-specificity scores (rank ~4210–4377 out of the full candidate list) suggests these are tail-end, low-confidence outputs rather than a genuine top signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07148180](https://clinicaltrials.gov/study/NCT07148180) | Phase 1/2 | Recruiting | 31 | Tagraxofusp + azacitidine + venetoclax targeting measurable residual disease (MRD) in AML; indirect relevance as MRD represents residual pre-malignant clonal disease |
| [NCT06414681](https://clinicaltrials.gov/study/NCT06414681) | Early Phase 1 | Not yet recruiting | 20 | Tagraxofusp + pacritinib in intermediate-1 or higher myelofibrosis after prior JAK inhibitor failure; myelofibrosis is a pre-malignant/borderline myeloid neoplasm, giving the closest mechanistic link, though still an early, small pilot study |
| [NCT05476770](https://clinicaltrials.gov/study/NCT05476770) | Phase 1 | Recruiting | 54 | Tagraxofusp with/without chemotherapy in pediatric relapsed/refractory CD123⁺ hematologic malignancies; confirms CD123-targeting mechanism but studies frank malignancy, not pre-malignant disease |
| [NCT03113643](https://clinicaltrials.gov/study/NCT03113643) | Phase 1 | Recruiting | 72 | SL-401 (tagraxofusp) + azacitidine ± venetoclax in relapsed/refractory AML, treatment-naive AML unfit for induction, BPDCN, and high-risk MDS |
| [NCT03386513](https://clinicaltrials.gov/study/NCT03386513) | Phase 1/2 | Active, not recruiting | 179 | IMGN632 (a different CD123-targeted agent, not tagraxofusp) monotherapy in CD123⁺ AML; relevant only as supporting evidence for the CD123 target class |

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Tagraxofusp is not currently registered in Singapore (0 authorizations on file; market status: Not marketed). No product-level licensing information is available at this time.

---

## Cytotoxicity

Tagraxofusp is an antineoplastic agent (CD123-targeted protein-toxin conjugate approved for a hematologic malignancy).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CD123-directed diphtheria toxin fusion protein / immunotoxin) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking-severity data gap exists on TFDA/local label warnings and contraindications, which by definition prevents entry into initial safety screening (S1). In addition, the drug's mechanism of action is not yet documented in this evidence pack, and the only evidence-backed candidate indication (pre-malignant neoplasm) is supported solely by indirect trials in AML-MRD and myelofibrosis rather than direct studies of the stated disease label. The model's top-ranked prediction for this drug (esotropia) is assessed as noise and provides no basis for action.

**To proceed, the following is needed:**
- Official label warnings and contraindications (source: TFDA/originator label) — required to clear the Blocking gap (DG001)
- Mechanism of action detail via DrugBank API (DG002)
- Clarification of how "pre-malignant neoplasm" maps to actual trial populations (myelofibrosis, AML-MRD) before treating it as a discrete indication
- Continued monitoring of NCT07148180 (recruiting through 2030) and NCT06414681 (myelofibrosis pilot) as they mature
- Reassessment of TxGNN's top-ranked output (esotropia) as a likely model artifact, flagged for model-maintainer review rather than further clinical evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

