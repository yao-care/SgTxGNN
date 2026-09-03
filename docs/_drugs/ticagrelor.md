---
layout: default
title: Ticagrelor
parent: 僅模型預測 (L5)
nav_order: 978
evidence_level: L5
indication_count: 10
---

# Ticagrelor
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

# Ticagrelor: From Acute Coronary Syndrome to Intracranial Arteriosclerosis

## One-Sentence Summary

> Ticagrelor is an oral P2Y12 receptor antagonist established for antiplatelet therapy in acute coronary syndrome (ACS) and percutaneous coronary intervention (PCI).
> The TxGNN model predicts it may be effective for **Intracranial Arteriosclerosis**,
> with **12 clinical trials** and **3 publications** currently supporting this direction, including an ongoing Phase 3 RCT designed specifically for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Coronary Syndrome / Dual Antiplatelet Therapy after PCI (per literature evidence; no formal indication text available — not marketed in Singapore) |
| Predicted New Indication | Intracranial arteriosclerosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from a structured source (e.g., DrugBank API) is not available for this evidence pack. Based on the supporting literature and trial descriptions collected, ticagrelor is a reversible, direct-acting oral P2Y12 receptor antagonist that inhibits ADP-mediated platelet activation and aggregation, and also raises local adenosine levels via inhibition of equilibrative nucleoside transporter 1 (ENT-1) — an effect associated with additional vasodilatory and anti-ischemic properties. Its efficacy in reducing atherothrombotic events (myocardial infarction, stroke, cardiovascular death) after ACS and PCI has been well established in large Phase 3 programs (e.g., PLATO, referenced across the literature set).

Intracranial arteriosclerosis (intracranial atherosclerotic disease, ICAD) shares the same underlying atherothrombotic pathophysiology as coronary and peripheral artery disease — platelet-mediated plaque instability and thrombus formation causing vessel occlusion or embolic stroke. Standard care for symptomatic ICAD (clopidogrel + aspirin) still carries a high residual stroke recurrence risk, which is the direct rationale behind the CAPTIVA trial (NCT05047172), which is testing whether ticagrelor (alone or combined with rivaroxaban) outperforms clopidogrel in this population. This mechanistic continuity — a platelet inhibitor moving from coronary/peripheral atherothrombosis to cerebral atherothrombosis — is a biologically coherent basis for the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Phase 3 | Recruiting | 1,683 | CAPTIVA: rivaroxaban and/or ticagrelor vs. clopidogrel for lowering 1-year ischemic stroke, ICH, or vascular death in intracranial vascular atherostenosis |
| [NCT04948749](https://clinicaltrials.gov/study/NCT04948749) | N/A | Recruiting | 792 | DREAM-PRIDE: drug-eluting stent + aggressive medical treatment vs. medical treatment alone for symptomatic intracranial atherosclerotic disease |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | N/A | Recruiting | 100 | Pilot RCT: genotype-guided P2Y12 inhibitor selection vs. conventional clopidogrel in symptomatic ICAD |
| [NCT06058130](https://clinicaltrials.gov/study/NCT06058130) | N/A | Unknown | 2,171 | Anticoagulation vs. anticoagulation + antiplatelet therapy in acute ischemic stroke with AFib and extracranial/intracranial artery stenosis |
| [NCT01732822](https://clinicaltrials.gov/study/NCT01732822) | Phase 3 | Completed | 13,885 | EUCLID: ticagrelor vs. clopidogrel for CV death, MI and ischemic stroke in peripheral artery disease |
| [NCT01813435](https://clinicaltrials.gov/study/NCT01813435) | Phase 3 | Completed | 15,991 | GLOBAL LEADERS: ticagrelor + aspirin (1mo) then ticagrelor monotherapy vs. standard DAPT after stent implantation |
| [NCT02605447](https://clinicaltrials.gov/study/NCT02605447) | Phase 4 | Completed | 2,009 | EVOLVE Short DAPT: safety of 3-month DAPT in high bleeding-risk PCI patients |
| [NCT03620760](https://clinicaltrials.gov/study/NCT03620760) | Phase 4 | Unknown | 2,036 | Low-dose vs. standard-dose ticagrelor in unstable angina after DES implantation |
| [NCT07164859](https://clinicaltrials.gov/study/NCT07164859) | Phase 3 | Not Yet Recruiting | 1,700 | SOLOPCI: very short DAPT followed by P2Y12 monotherapy in elderly PCI patients |
| [NCT07354828](https://clinicaltrials.gov/study/NCT07354828) | N/A | Not Yet Recruiting | 3,500 | Quality control standard system for DAPT-based coronary revascularization in CAD |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | Trial Design (Phase 3) | International Journal of Stroke | Describes the CAPTIVA trial rationale: standard clopidogrel+aspirin therapy for symptomatic ICAS leaves high residual stroke risk up to 12 months, motivating comparison with ticagrelor-based regimens |
| [38252758](https://pubmed.ncbi.nlm.nih.gov/38252758/) | 2024 | Review | Stroke | Focused update on intracranial atherosclerosis, summarizing current knowledge gaps and treatment approaches |
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Retrospective Observational | Journal of Neurointerventional Surgery | Ticagrelor 60mg BID + aspirin compared with aspirin/clopidogrel for intracranial stenting; supports feasibility of ticagrelor-based DAPT in neurointervention |

---

## Singapore Market Information

Ticagrelor is currently **not marketed** in Singapore under this evidence pack — no product registrations (SIN numbers) were found, so no authorization or approved indication text is available.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available in this evidence pack (this is flagged as a **Blocking** data gap — see DG001 — preventing formal S1 safety assessment).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale is sound and one purpose-built Phase 3 RCT (CAPTIVA) is actively investigating ticagrelor for intracranial arteriosclerosis, but it has not yet reported results, and no completed trial or approved label directly supports this indication. Combined with the absence of Singapore market presence and a **Blocking** safety data gap (no TFDA-equivalent warnings/contraindications available), the evidence is not yet sufficient to proceed.

**To proceed, the following is needed:**
- Obtain the full drug label / warnings / contraindications (closing DG001) before any safety-stage review
- Retrieve formal DrugBank MOA record (closing DG002) to strengthen mechanistic justification
- Monitor completion and results of CAPTIVA (NCT05047172) and DREAM-PRIDE (NCT04948749)
- Clarify the local regulatory pathway, given ticagrelor currently has zero registrations in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

