---
layout: default
title: Methoxyflurane
parent: 僅模型預測 (L5)
nav_order: 653
evidence_level: L5
indication_count: 10
---

# Methoxyflurane
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

Using the evidence pack's actual support pattern — TxGNN's top-ranked hits (insomnia, migraine, dysthymia, etc.) carry zero clinical/literature evidence (L5/Hold), while the pack's real, well-supported signal is **anxiety** (rank 10: L3, decision-stage S2, "Proceed with Guardrails," with 6 trials and 20 publications). I'm building the report around that indication rather than the bare top-score entry, since it's the only one this evidence pack can actually substantiate.

# Methoxyflurane: From Procedural Analgesia to Anxiety

## One-Sentence Summary

Methoxyflurane is an inhaled halogenated-ether agent used as a self-administered analgesic in acute and procedural pain settings (e.g., trauma, minor surgical/dental procedures); it is **not currently marketed in Singapore**.
The TxGNN model predicts it may also be effective for **Anxiety**, with **6 clinical trials** and **20 publications** currently supporting this direction — several of them randomized controlled trials evaluating anxiety and pain jointly during medical procedures.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute/procedural pain (inhaled analgesic); no Singapore-approved indication text is available since the product is not registered locally |
| Predicted New Indication | Anxiety |
| TxGNN Prediction Score | 94.40% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for methoxyflurane is not available in this evidence pack (flagged as a High-severity data gap — DrugBank MOA lookup pending). Based on the information that is available, methoxyflurane is a halogenated-ether inhalational anesthetic/analgesic, self-administered via a handheld inhaler (Penthrox), whose established efficacy is in acute and procedural pain relief.

The link to anxiety is indirect but biologically plausible: at sub-anesthetic inhaled doses, methoxyflurane produces central nervous system depression and sedation. Animal discriminative-stimulus studies found that methoxyflurane fully substitutes for diazepam's effects in mice, suggesting it shares part of the benzodiazepine central-depressant pathway. This overlap plausibly explains why methoxyflurane has repeatedly been observed — across burn wound care, dental extractions, brachytherapy applicator removal, and interventional radiology — to reduce not just pain but also procedural anxiety as a secondary effect. Importantly, this appears to be a sedative/analgesic side effect rather than a targeted anxiolytic mechanism, so it should be framed as adjunctive periprocedural anxiety relief rather than a standalone anxiety-disorder treatment.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04618497](https://clinicaltrials.gov/study/NCT04618497) | Phase 3 | Completed | 40 | Pilot study of methoxyflurane (Penthrox) for ED musculoskeletal pain; anxiety only a possible secondary measure, not the primary endpoint |
| [NCT07295054](https://clinicaltrials.gov/study/NCT07295054) | Phase 4 | Not yet recruiting | 110 | Double-blind placebo-controlled RCT of inhaled methoxyflurane for pain during IUD insertion; may capture procedural anxiety |
| [NCT06495372](https://clinicaltrials.gov/study/NCT06495372) | Phase 3 | Recruiting | 192 | METODO trial: methoxyflurane vs placebo for dental/oral emergency pain |
| [NCT06750302](https://clinicaltrials.gov/study/NCT06750302) | Phase 1/2 | Recruiting | 100 | Methoxyflurane (Penthrox) vs placebo for pain during minor sinus/coblation procedures; anxiety not a primary endpoint |
| [NCT07017452](https://clinicaltrials.gov/study/NCT07017452) | Phase 3 | Not yet recruiting | 48 | Non-inferiority trial of oral methoxyflurane+lorazepam+percocet vs deep IV sedation during REZUM therapy for BPH — combination includes an anxiolytic (lorazepam) |
| [NCT07192198](https://clinicaltrials.gov/study/NCT07192198) | Phase 2 | Completed | 40 | Pilot RCT of inhaled methoxyflurane as adjunct to local anesthesia for urologic procedures, assessing pain tolerance and anxiety levels |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40769179](https://pubmed.ncbi.nlm.nih.gov/40769179/) | 2025 | RCT | Can Urol Assoc J | Methoxyflurane + local anesthesia reduced pain and periprocedural anxiety vs local anesthesia alone in scrotal surgery |
| [38923825](https://pubmed.ncbi.nlm.nih.gov/38923825/) | 2024 | RCT | J Med Imaging Radiat Oncol | MONITOR trial: methoxyflurane evaluated for procedural sedation/pain management in interventional radiology |
| [24644183](https://pubmed.ncbi.nlm.nih.gov/24644183/) | 2014 | RCT | BMJ Support Palliat Care | Randomized, double-blind, placebo-controlled trial showing methoxyflurane safety/efficacy for bone marrow biopsy procedural pain |
| [39174051](https://pubmed.ncbi.nlm.nih.gov/39174051/) | 2025 | RCT | Reg Anesth Pain Med | Methoxyflurane inhaler + local anesthesia reduced procedural pain during genicular nerve block for knee osteoarthritis |
| [23810328](https://pubmed.ncbi.nlm.nih.gov/23810328/) | 2013 | RCT | Gastrointest Endosc | Multicenter RCT comparing patient-controlled inhaled methoxyflurane to conventional sedation for colonoscopy |
| [21884146](https://pubmed.ncbi.nlm.nih.gov/21884146/) | 2011 | Comparative study | Aust Dent J | Inhaled methoxyflurane reduced dental anxiety during third molar extraction, compared to nitrous oxide sedation |
| [40170612](https://pubmed.ncbi.nlm.nih.gov/40170612/) | 2025 | Review | Curr Opin Support Palliat Care | Review of inhaled methoxyflurane use in cancer patients for anxiety, discomfort, and pain during diagnostic/therapeutic procedures |
| [39269255](https://pubmed.ncbi.nlm.nih.gov/39269255/) | 2024 | Review | Curr Opin Support Palliat Care | Review of inhaled methoxyflurane for acute pain in non-cancer settings, self-administered with rapid onset/offset |
| [36970443](https://pubmed.ncbi.nlm.nih.gov/36970443/) | 2023 | Cohort | J Contemp Brachytherapy | Inhaled methoxyflurane used for pain and symptom relief (including anxiety) during gynecologic brachytherapy applicator removal |
| [22925206](https://pubmed.ncbi.nlm.nih.gov/22925206/) | 2014 | Cohort | Int Wound J | Case series on inhaled methoxyflurane for pain and anxiety relief during burn wound care procedures |

## Singapore Market Information

Methoxyflurane currently has **no registered license in Singapore** (`market_status`: 未上市, `total_licenses`: 0). No product listing is available for this evaluation.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not yet available for this drug — flagged as a Blocking data gap requiring TFDA/HSA label retrieval.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple RCTs (bone marrow biopsy, colonoscopy, interventional radiology, scrotal surgery, genicular nerve block) consistently show methoxyflurane reduces periprocedural anxiety alongside pain, giving L3-level observational/RCT support — but all evidence is for adjunctive, procedure-related anxiety relief, not treatment of a standalone anxiety disorder, so guardrails on indication scope are warranted.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (currently blocking — DG001)
- Confirmed mechanism of action from DrugBank (currently missing — DG002)
- A dedicated trial with anxiety (not procedural pain) as the primary endpoint to distinguish anxiolytic effect from general sedation
- Singapore-specific regulatory pathway assessment, since the drug is not currently registered locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

