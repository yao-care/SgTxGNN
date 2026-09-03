---
layout: default
title: Tirofiban
parent: 僅模型預測 (L5)
nav_order: 985
evidence_level: L5
indication_count: 10
---

# Tirofiban
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

# Tirofiban: From Acute Coronary Syndrome to Primary Release Disorder of Platelets

## One-Sentence Summary

Tirofiban is a GPIIb/IIIa (integrin αIIbβ3) receptor antagonist, originally used to inhibit platelet aggregation in acute coronary syndrome (ACS) and percutaneous coronary intervention (PCI).
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, but the supporting evidence is indirect — **2 clinical trials** (neither studying this specific disorder) and **3 publications** on tirofiban's general platelet pharmacology — and the prediction carries a notable mechanistic contradiction that should be resolved before further evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Coronary Syndrome (ACS) / Percutaneous Coronary Intervention (inferred from drug class and supporting trial context; no Singapore-specific label text available since the product is not marketed here) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 96.27% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured MOA data was not available in the regulatory record, but the evidence pack's own literature confirms tirofiban's mechanism: it is a small-molecule, non-peptide antagonist of the platelet GPIIb/IIIa (integrin αIIbβ3) receptor, blocking fibrinogen binding and thereby inhibiting platelet aggregation. Clinically it is used alongside aspirin/clopidogrel in ACS and around PCI/CABG to reduce ischemic events — consistent with the trial evidence retrieved (NSTE-ACS, elective PCI, CABG).

**This raises a directional concern.** "Primary release disorder of platelets" refers to a group of hereditary/acquired platelet function disorders in which platelets fail to release granule contents properly, causing a **bleeding tendency** — not a thrombotic one. Tirofiban further suppresses platelet aggregation. Administering an aggregation inhibitor to patients whose platelets already cannot function normally would be expected to worsen bleeding risk rather than correct the underlying release defect.

This mirrors the explicit contradiction the evidence pack itself flags for the rank-2 candidate, Glanzmann thrombasthenia (also a congenital GPIIb/IIIa-related bleeding disorder), which was already scored **L5 / Hold** with a documented rationale of likely knowledge-graph false positive (shared protein node → false directionality). The rank-1 candidate here shows the same pattern: neither supporting trial (aneurysmal SAH platelet suppression, NSTE-ACS/CABG antiplatelet therapy) actually studies platelet release disorders — both are about *reducing* platelet activity in thrombotic settings, not correcting a release defect. The mechanistic link should be treated as unconfirmed pending expert pharmacology review.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03691727](https://clinicaltrials.gov/study/NCT03691727) | Phase 1/2a | Completed | 30 | Randomized, double-blind, single-center study comparing standard care alone vs. standard care + tirofiban (Aggrastat) in aneurysmal subarachnoid hemorrhage — not a study of platelet release disorders. |
| [NCT01863134](https://clinicaltrials.gov/study/NCT01863134) | Phase 4 | Completed | 140 | Studied eptifibatide (a related GPIIb/IIIa antagonist, not tirofiban) in high-risk NSTE-ACS patients undergoing urgent CABG. |

Neither trial directly evaluates efficacy in primary release disorder of platelets; both relate only to the shared GPIIb/IIIa mechanism class.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12204495](https://pubmed.ncbi.nlm.nih.gov/12204495/) | 2002 | RCT (TOPSTAR trial) | Journal of the American College of Cardiology | Additional temporary GPIIb/IIIa inhibition with tirofiban did not further reduce troponin release after elective PCI in patients pretreated with aspirin and clopidogrel. |
| [16682384](https://pubmed.ncbi.nlm.nih.gov/16682384/) | 2006 | RCT (ELISA-2 trial) | European Heart Journal | Compared dual vs. triple antiplatelet pretreatment (including GPIIb/IIIa inhibition) in NSTE-ACS patients undergoing early catheterization. |
| [16287613](https://pubmed.ncbi.nlm.nih.gov/16287613/) | 2005 | Case series / observational | Platelets | Identified two subgroups of tirofiban-induced thrombocytopenia caused by drug-dependent antibodies against GPIIb/IIIa, associated with platelet activation and increased ischemic events — a safety signal, not efficacy evidence for a platelet release disorder. |

None of these publications directly study tirofiban's use in a primary platelet release disorder; all describe its established antiplatelet/ACS pharmacology or an adverse thrombocytopenia mechanism.

---

## Singapore Market Information

Tirofiban currently has **no marketing authorization in Singapore** — 0 registered products, no license records available for review.

---

## Safety Considerations

Detailed prescribing information (key warnings, contraindications, drug-drug interactions) is not currently available for this candidate. Notably, the evidence pack flags this as a **blocking data gap** — without a validated label/warnings source, this candidate cannot proceed to formal safety review.

One relevant safety signal did surface in the literature evidence: tirofiban has been associated with drug-dependent antibody-mediated thrombocytopenia, in some cases accompanied by platelet activation and increased ischemic events (PMID 16287613) — this should be factored into any future risk assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication presents a mechanistic contradiction — an antiplatelet aggregation inhibitor proposed for a bleeding-type platelet release disorder — that closely parallels a pattern the evidence pack already identifies as a likely knowledge-graph false positive for a related candidate (Glanzmann thrombasthenia, rank 2). Combined with the absence of any trial or literature directly studying this disorder, and a blocking gap in safety/label data, this candidate is not ready to advance.

**To proceed, the following is needed:**
- Package insert / regulatory safety data (warnings, contraindications) — currently blocking S1 safety review
- Confirmed source-cited mechanism of action documentation
- Expert hematology review clarifying the pathophysiologic directionality between GPIIb/IIIa antagonism and primary platelet release disorders (to rule out false-positive graph inference)
- Any disease-specific preclinical or clinical evidence, if it exists, that was not captured by the current literature/trial search
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

