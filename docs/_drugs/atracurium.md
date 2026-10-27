---
layout: default
title: Atracurium
parent: Low Evidence (L5)
nav_order: 120
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Atracurium: predicted new indication Myofascial pain syndrome (evidence level L5). Approved use: Not stated in the Singapore licence records. Pharmacologically…"
monitor_inn: "Atracurium"
predicted_indications: ["myofascial pain syndrome", "nephrogenic syndrome of inappropriate antidiuresis", "methemoglobinemia", "common cold", "conjunctivitis", "idiopathic granulomatous myositis", "myositis fibrosa", "tendinitis", "methemoglobinemia, alpha type", "fibromyalgia"]
---

# Atracurium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Atracurium: From Neuromuscular Blockade to Myofascial Pain Syndrome
{: .text-alpha }

## One-Sentence Summary

Atracurium is a non-depolarizing neuromuscular blocker used as an injectable muscle relaxant. The TxGNN model predicts it may be effective for **myofascial pain syndrome**, but **no clinical trials and no directly relevant publications** currently support this prediction. It rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records. Pharmacologically, atracurium is a neuromuscular blocker |
| Predicted New Indication | Myofascial pain syndrome |
| TxGNN Prediction Score | 94.10% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Atracurium is known to be a non-depolarizing neuromuscular blocker. It antagonises nicotinic acetylcholine receptors at the motor end plate, which relaxes skeletal muscle.

Myofascial trigger points involve sustained local muscle contraction and dysfunctional end-plate activity. Muscle relaxation is therefore a plausible conceptual link. However, systemic neuromuscular blockade requires ventilatory support, so it is not practical for outpatient pain management. The link is prediction-only, with no supporting trials or literature.

The other nine predictions ranked by the model are weaker still:

- **Nephrogenic syndrome of inappropriate antidiuresis (93.90%)**: this is caused by AVPR2 gain-of-function mutations, which are unrelated to nicotinic receptor blockade. The score is likely a knowledge-graph artifact.
- **Methemoglobinemia (92.63%) and methemoglobinemia, alpha type (88.24%)**: no mechanistic rationale exists. The only retrieved paper describes prilocaine-induced methemoglobinemia during anaesthesia, where atracurium was merely a co-administered drug.
- **Common cold (92.56%)**: the retrieved paper is a cohort study on perioperative hypersensitivity, in which neuromuscular blockers are known triggers. This is a safety signal, not therapeutic evidence.
- **Conjunctivitis (90.08%)**: atracurium has no known anti-inflammatory or antimicrobial activity.
- **Idiopathic granulomatous myositis (88.71%) and myositis fibrosa (88.71%)**: the links rest only on muscle-tissue association. The identical scores suggest a shared graph neighbourhood rather than independent evidence.
- **Tendinitis (88.27%)**: no credible mechanism, and systemic blockade is not appropriate.
- **Fibromyalgia (88.00%)**: neuromuscular blockade does not target central sensitisation. The retrieved paper concerns postoperative myalgia after succinylcholine, which is not fibromyalgia treatment.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was retrieved for the top-ranked prediction (myofascial pain syndrome). The only publications found relate to lower-ranked predictions and are indirect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9095707](https://pubmed.ncbi.nlm.nih.gov/9095707/) | 1996 | Clinical study (likely RCT, inferred from title) | AANA Journal | 50 surgical patients; tested whether atracurium pretreatment reduces succinylcholine-induced fasciculations and myalgias. This concerns postoperative muscle pain, not fibromyalgia treatment (related to the rank 10 prediction) |
| [25902325](https://pubmed.ncbi.nlm.nih.gov/25902325/) | 2015 | Prospective cohort | Anesthesia and Analgesia | Incidence of perioperative hypersensitivity reactions, including those to neuromuscular blockers. A safety signal, not therapeutic evidence (related to the common cold prediction) |
| [7653798](https://pubmed.ncbi.nlm.nih.gov/7653798/) | 1995 | Case report / clinical observation (inferred from title) | Der Anaesthesist | Prilocaine-induced methemoglobinemia after anaesthesia induction. Atracurium appears only as a co-administered drug (related to the methemoglobinemia prediction) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14533P | Atracurium-hameln Injection 10mg/ml | Injection, solution | Not stated in available records |
| SIN16945P | NOTRIXUM Injection 10mg/ml | Injection, solution | Not stated in available records |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease edges, not label text): potassium deficiency, hypotensive disorder, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, myasthenia gravis (including adult-onset), neuromuscular junction disease, Lambert-Eaton myasthenic syndrome, malignant hyperthermia (including exercise-induced), and lung disease.
- **Drug Interactions**: 47 interactions were identified. The 20 shown in the data include the following:
  - **Major**: paromomycin, kanamycin, neomycin, polymyxin B, streptomycin. These aminoglycoside and polymyxin antibiotics may potentiate neuromuscular blockade.
  - **Moderate**: doxycycline, tetracycline, minocycline, vancomycin, several amphotericin B formulations, magnesium sulfate, magnesium chloride, mannitol, metoclopramide, and topical neomycin.
  - **Minor**: ranitidine, ranitidine (bismuth citrate).
- **Hypersensitivity**: a cohort study in the data identifies neuromuscular blockers such as atracurium as triggers of perioperative hypersensitivity reactions.

Please also refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by model score only, with no clinical trials and no directly relevant literature (L5). Systemic neuromuscular blockade requires ventilatory support, which makes outpatient use for myofascial pain impractical. Atracurium also carries many knowledge-graph contraindication signals and major drug interactions.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank
- Package insert warnings and contraindications from the HSA website
- Preclinical or early clinical evidence for local or low-dose use in myofascial pain, if the hypothesis is pursued
- Route and formulation feasibility assessment, since the available forms are intravenous injections only
- Review of the DDI and contraindication profile for the intended population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

