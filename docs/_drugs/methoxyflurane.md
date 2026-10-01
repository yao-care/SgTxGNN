---
layout: default
title: Methoxyflurane
parent: Low Evidence (L5)
nav_order: 653
evidence_level: L5
indication_count: 10
---

# Methoxyflurane
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

# Methoxyflurane: From Acute Pain to Insomnia

## One-Sentence Summary

Methoxyflurane is an inhaled analgesic (marketed in Singapore as Penthrox) used for short-term relief of acute trauma pain.
The TxGNN model ranks **insomnia** as its top predicted new indication, with a high score of 98.0%. This prediction rests on the graph model alone, with **0 clinical trials** and **0 publications** supporting it.
Among the 10 predicted indications, only **anxiety** has meaningful supporting data (5 trials, 20 publications), and that data mostly concerns procedural anxiety.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute pain (inhaled analgesic). The Singapore licence record does not state an indication text. |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 98.01% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Based on general class pharmacology, methoxyflurane is a halogenated ether anaesthetic that enhances GABA-A and glycine receptor activity. That makes a sedative effect plausible, which is the likely basis for the model linking it to insomnia.

The link is weak in practice. Anaesthetic-induced unconsciousness is not physiological sleep. A short-acting inhaled agent with dose-related kidney toxicity is also a poor fit for a chronic condition like insomnia. Nothing in the retrieved data (no trials, no literature) supports the prediction, so the score reflects graph proximity only.

## Clinical Trial Evidence

Currently no related clinical trials registered for insomnia.

## Literature Evidence

Currently no related literature available for insomnia.

## Other Predicted Indications

Nine other predicted indications were scored, all at 94–98%. Only anxiety has usable evidence.

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Migraine disorder | 97.96% | L5 | Extension from acute pain is conceivable, but no supporting trials or literature |
| Migraine with brainstem aura | 97.62% | L5 | Likely reflects graph proximity to the parent migraine node |
| Dysthymic disorder | 97.16% | L5 | No plausible mechanism for a chronic mood disorder; repeated exposure raises safety concerns |
| Migraine with or without aura, susceptibility to | 96.51% | L5 | The 20 retrieved papers are about epilepsy/migraine genetics, and none involve methoxyflurane |
| Atrophoderma vermiculata | 95.71% | L5 | Rare skin condition; likely a graph artifact |
| Neurotic disorder | 94.95% | L5 | Broad legacy category overlapping with anxiety; no term-specific evidence |
| Ulerythema ophryogenesis | 94.95% | L5 | Rare skin condition; likely a graph artifact |
| **Anxiety disorder** | 94.42% | L4 | Preclinical and case-level data plus procedural trials, described below |
| **Anxiety** | 94.40% | **L3** | Strongest signal, described below |

### Anxiety (strongest signal)

Methoxyflurane shows diazepam-like and anxiolytic-like effects in mouse studies. Clinically, procedural anxiety relief has been documented alongside analgesia. The signal is best framed as **procedural anxiolysis**, not treatment of an anxiety disorder, because no trial has anxiety as its primary endpoint.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07192198](https://clinicaltrials.gov/study/NCT07192198) | Phase 2 | Completed | 40 | Penthrox as an adjunct to local anaesthetic in urologic procedures; assesses pain tolerance and anxiety. No results available. |
| [NCT07017452](https://clinicaltrials.gov/study/NCT07017452) | Phase 3 | Not yet recruiting | 48 | Methoxyflurane + lorazepam + oral opioid vs deep IV sedation during Rezum therapy for BPH (non-inferiority) |
| [NCT04618497](https://clinicaltrials.gov/study/NCT04618497) | Phase 3 | Completed | 40 | Pilot of methoxyflurane for pain control after musculoskeletal injury in the emergency department |
| [NCT06495372](https://clinicaltrials.gov/study/NCT06495372) | Phase 3 | Recruiting | 192 | Methoxyflurane vs placebo for pain in oral and dental emergencies |
| [NCT06750302](https://clinicaltrials.gov/study/NCT06750302) | Phase 1/2 | Recruiting | 100 | Methoxyflurane vs placebo for pain in coblation and sinus procedures |
| [NCT07295054](https://clinicaltrials.gov/study/NCT07295054) | Phase 4 | Not yet recruiting | 110 | 3 mL inhaled methoxyflurane vs placebo for IUD insertion pain |

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40769179](https://pubmed.ncbi.nlm.nih.gov/40769179/) | 2025 | RCT | Can Urol Assoc J | Methoxyflurane as an adjunct to local anaesthesia for pain and anxiety in scrotal surgery |
| [38923825](https://pubmed.ncbi.nlm.nih.gov/38923825/) | 2024 | RCT | J Med Imaging Radiat Oncol | MONITOR trial: methoxyflurane for procedural sedation and pain in interventional radiology |
| [24644183](https://pubmed.ncbi.nlm.nih.gov/24644183/) | 2014 | RCT | BMJ Support Palliat Care | Double-blind placebo-controlled study for bone marrow biopsy pain |
| [21884146](https://pubmed.ncbi.nlm.nih.gov/21884146/) | 2011 | Clinical study | Aust Dent J | Methoxyflurane vs nitrous oxide for dental anxiety in third molar extraction |
| [40170612](https://pubmed.ncbi.nlm.nih.gov/40170612/) | 2025 | Review | Curr Opin Support Palliat Care | Use in cancer patients for procedures causing anxiety, discomfort and pain |
| [36970443](https://pubmed.ncbi.nlm.nih.gov/36970443/) | 2023 | Cohort | J Contemp Brachytherapy | Pain and symptom relief for gynaecologic brachytherapy applicator removal |
| [22925206](https://pubmed.ncbi.nlm.nih.gov/22925206/) | 2014 | Case series | Int Wound J | Pain and anxiety relief during burn wound care |
| [10036607](https://pubmed.ncbi.nlm.nih.gov/10036607/) | 1999 | Preclinical (mouse) | Exp Clin Psychopharmacol | Methoxyflurane fully substituted for diazepam in discrimination tests |
| [8894586](https://pubmed.ncbi.nlm.nih.gov/8894586/) | 1996 | Preclinical (mouse) | Eur J Pharmacol | Effects of abused inhalants in the elevated plus-maze, an anxiety model |
| [5143658](https://pubmed.ncbi.nlm.nih.gov/5143658/) | 1971 | Case report | Br J Psychiatry | Report of dependence on a related agent (Pentrane) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14854P | PENTHROX INHALATION LIQUID 99.9% (Medical Developments International Limited) | Inhalant | Not stated in the licence record |

## Safety Considerations

- **Drug Interactions**: No interactions were found in the database query.
- **Risk considerations noted in the prediction rationale**: dose-related kidney toxicity, liver toxicity, and abuse/dependence potential. These weigh against repeated or chronic use.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (insomnia) has no trial or literature support, and the drug's profile (short-acting, organ toxicity, dependence risk) does not suit a chronic sleep disorder. The anxiety signal (L3) is more promising, but it reflects procedural anxiolysis alongside pain relief, not treatment of an anxiety disorder.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (this blocks safety screening)
- Mechanism-of-action data from DrugBank
- For anxiety: confirmation of whether the completed and ongoing trials measured anxiety prospectively, especially NCT07192198
- A safety assessment for repeated dosing
- For insomnia: no evidence at present, so a preclinical or pilot rationale would be needed before any further evaluation

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

