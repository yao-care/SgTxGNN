---
layout: default
title: Propofol
parent: 僅模型預測 (L5)
nav_order: 826
evidence_level: L5
indication_count: 10
---

# Propofol
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

# Propofol: From General Anesthesia to Migraine Disorder

## One-Sentence Summary

Propofol is a widely used intravenous general anesthetic and sedative agent, primarily employed for induction/maintenance of anesthesia and procedural sedation.
The TxGNN model predicts it may be effective for **Migraine Disorder** (used off-label at subanesthetic doses),
with **5 clinical trials** and **20 publications** currently supporting this direction, including a 2026 American Headache Society guideline update that references parenteral propofol as an emergency department option.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General anesthesia induction/maintenance and procedural sedation (not registered in Singapore; no local license record available) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

A formal, database-sourced mechanism-of-action record for propofol is not currently available in this evidence pack. However, based on the mechanistic literature returned alongside the migraine prediction, propofol is a GABA-A receptor positive allosteric modulator with central depressant, sedative, and antiemetic properties. Animal and human studies indicate that propofol suppresses cortical spreading depression (CSD) — the pathological process believed to underlie migraine aura and pain propagation (e.g., PMID 22390898, mechanistic study on propofol hemisuccinate and CSD suppression).

Propofol's original indication (general anesthesia/sedation) and the predicted new indication (migraine) are connected through this CSD-suppressing property rather than a direct anatomical or disease-category overlap. Clinically, low-dose ("subanesthetic") propofol has already been used off-label as a rescue therapy for refractory migraine in emergency department settings, in both adult and pediatric populations, when first- and second-line agents (NSAIDs, triptans, dopamine antagonists) fail.

This mechanistic rationale is reinforced by a body of clinical evidence: multiple completed RCTs (e.g., PMID 29456086, PMID 35402989, PMID 35573713), a systematic review specifically evaluating propofol for acute migraine in the ED (PMID 31621134), and inclusion of parenteral propofol in the 2026 American Headache Society evidence-based guideline update (PMID 41321235). This combination of plausible mechanism and converging clinical evidence supports the TxGNN prediction as a reasonable research signal, though it remains an off-label, second/third-line use rather than an established indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Phase 2/3 | Completed | 74 | Low-dose propofol as abortive therapy for pediatric migraine in the ED; retrospective data suggested safety and possible superiority over standard treatment |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | N/A | Completed | 40 | Low-dose propofol infusion as abortive treatment for pediatric migraine; evaluated efficacy, safe dosing limits, and duration of effect |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | N/A | Terminated | 12 | Low-dose propofol for severe refractory migraine in the ED as second-line treatment; terminated early, small sample limits evidence strength |
| [NCT03789370](https://clinicaltrials.gov/study/NCT03789370) | N/A | Unknown | 130 | Compared sevoflurane vs. propofol anesthesia maintenance for postoperative headache occurrence; propofol proposed to have protective effect on migraine patients |
| [NCT02443220](https://clinicaltrials.gov/study/NCT02443220) | N/A | Completed | 315 | Electroacupuncture analgesia study in CABG surgery; propofol not the primary study drug, low relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Systematic Review | Academic Emergency Medicine | Systematic review of propofol safety/efficacy for acute migraine treatment in the ED |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | AHS 2025 guideline update on parenteral pharmacotherapies for acute migraine in the ED, including propofol |
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | RCT | Arch Acad Emerg Med | Propofol+granisetron vs. propofol+metoclopramide for acute migraine symptom management |
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | RCT | J Emerg Med | Prospective RCT of low-dose propofol for pediatric migraine, favorable side-effect profile and reduced ED length of stay |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | RCT | Arch Acad Emerg Med | Propofol+sumatriptan combination vs. sumatriptan alone for acute migraine management |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | Cohort/Case Series | Expert Rev Neurother | Drug profile review of subanesthetic-dose propofol for refractory/super-refractory migraine |
| [32638172](https://pubmed.ncbi.nlm.nih.gov/32638172/) | 2020 | Review | Curr Pain Headache Rep | Review of intravenous migraine treatment options in children and adolescents |
| [32410204](https://pubmed.ncbi.nlm.nih.gov/32410204/) | 2020 | Review | Curr Neurol Neurosci Rep | Review of ED/inpatient management of pediatric and adolescent headache |
| [22309235](https://pubmed.ncbi.nlm.nih.gov/22309235/) | 2012 | Review | Headache | Review of rescue therapy for acute migraine, including neuroleptics and propofol |
| [32705803](https://pubmed.ncbi.nlm.nih.gov/32705803/) | 2020 | Commentary/Opinion | Emerg Med Australas | Editorial questioning whether propofol should be used for migraine despite feasibility |

---

## Safety Considerations

Please refer to the package insert for safety information. No Singapore-specific key warnings, contraindications, or drug-drug interaction data are currently available for this candidate (data gap DG001 flagged as **Blocking** — required before a full safety evaluation can proceed).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed RCTs, a dedicated systematic review, and a 2026 AHS guideline update converge on subanesthetic-dose propofol as a plausible ED rescue option for acute/refractory migraine, giving L2-level evidence with clear mechanistic support (CSD suppression). However, propofol is not currently registered in Singapore for this or any indication, and safety-label data (warnings/contraindications) is missing, so the candidate cannot yet clear a full safety review.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent label warnings and contraindications (DG001, blocking)
- Confirmed mechanism-of-action data via DrugBank API (DG002)
- Singapore-specific regulatory pathway assessment, since propofol is currently unregistered locally
- A dedicated adult ED RCT with adequate power, given that NCT02492295 was terminated early with only 12 subjects and existing pediatric data may not generalize
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

