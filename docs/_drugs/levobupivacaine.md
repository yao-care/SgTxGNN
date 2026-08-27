---
layout: default
title: Levobupivacaine
parent: 僅模型預測 (L5)
nav_order: 588
evidence_level: L5
indication_count: 10
---

# Levobupivacaine
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

# Levobupivacaine: From Regional Anesthesia to Gastroduodenitis

## One-Sentence Summary

Levobupivacaine is an amide local anesthetic (the S-enantiomer of bupivacaine) used for surgical and regional anesthesia via Na⁺ channel blockade. The TxGNN model's top-ranked prediction is **Gastroduodenitis**, with a **99.09%** prediction score, but this pairing is currently supported by **zero clinical trials** and **zero publications** — it is a model-only association. Across the 10 candidate indications reviewed in this evidence pack, only two (hypertensive disorder, exostosis) have any real-world trial or literature data at all, and even those describe anesthesia-related observations rather than therapeutic efficacy for the new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local/regional anesthesia (surgical anesthesia & postoperative pain management) — drug is not registered in Singapore, so no official label text is available |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature identified) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is currently unavailable (flagged as a High-severity data gap). Based on information embedded elsewhere in this evidence pack, Levobupivacaine acts as a **Na⁺ channel blocker**, the mechanism shared by all amide local anesthetics, and its efficacy in regional/surgical anesthesia is well established.

However, gastroduodenitis is driven primarily by *H. pylori* infection, NSAID-induced mucosal injury, and gastric acid hypersecretion — a pathophysiology with no established connection to peripheral neuronal Na⁺ channel blockade. The evidence pack's own mechanistic assessment for this pairing states it is "a purely indirect TxGNN knowledge-graph association, with no supporting clinical evidence."

This is in fact one of the weaker rationales among the 10 candidates evaluated for this drug. For context, three lower-ranked candidates have at least a plausible procedural or class-effect link to Levobupivacaine's known anesthetic mechanism (occipital nerve block for migraine; hemodynamic effects during regional anesthesia in hypertensive patients; nerve block as an analgesic adjunct in exostosis surgery) — whereas gastroduodenitis does not. The full ranking is below.

### Other Candidate Indications in This Evidence Pack

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|-----------------|-----------------|-----------------|
| 1 | Gastroduodenitis | 99.09% | L5 | S0 | Hold |
| 2 | Peptic ulcer disease | 98.95% | L5 | S0 | Hold |
| 3 | Gout | 98.75% | L5 | S0 | Hold |
| 4 | Rhinitis | 98.47% | L5 | S0 | Hold |
| 5 | Bronchitis | 97.89% | L5 | S0 | Hold |
| 6 | Migraine disorder | 97.59% | L5 | S0 | Research Question |
| 7 | Migraine with brainstem aura | 97.56% | L5 | S0 | Hold |
| 8 | Exostosis | 96.76% | L4 | S0 | Hold |
| 9 | Hypertensive disorder | 96.19% | L4 | S1 | Hold |
| 10 | Ankylosing spondylitis | 96.16% | L5 | S0 | Hold |

Ranks 8 and 9 are the only candidates with actual clinical trial or literature evidence; both are detailed below for completeness even though neither is the top-ranked candidate.

---

## Clinical Trial Evidence (Gastroduodenitis — Rank 1)

Currently no related clinical trials registered.

## Literature Evidence (Gastroduodenitis — Rank 1)

Currently no related literature available.

---

### Supplementary Evidence: Hypertensive Disorder (Rank 9, L4/S1)

This is the only candidate in the batch that reached decision stage S1. The evidence is real but is directional against a therapeutic-efficacy interpretation — it consists of anesthesia trials that merely *monitor* hemodynamic effects (blood pressure, heart rate) in patients who already have hypertension or pregnancy-induced hypertension, not trials testing Levobupivacaine as an antihypertensive treatment.

**Clinical Trials**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06014957](https://clinicaltrials.gov/study/NCT06014957) | N/A | Unknown | 60 | Compares hemodynamic effects of spinal anesthesia vs. saddle block using levobupivacaine during TURP in elderly cardiac/hypertensive patients — an anesthesia-technique comparison, not an antihypertensive efficacy study. |
| [NCT02699827](https://clinicaltrials.gov/study/NCT02699827) | Phase 4 | Completed | 60 | Adding magnesium sulphate to epidural levobupivacaine for elective Caesarean section in preeclampsia patients — endpoint is anesthesia/analgesia quality, not blood pressure control. |
| [NCT02497040](https://clinicaltrials.gov/study/NCT02497040) | Phase 4 | Completed | 90 | Scalp block with bupivacaine vs. levobupivacaine for hemodynamic response to head-pinning — measures blood pressure as a side-effect endpoint of anesthesia, not a treatment outcome. |

**Literature**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26894153](https://pubmed.ncbi.nlm.nih.gov/26894153/) | 2016 | RCT | J Clin Diagn Res | Compares epidural bupivacaine, levobupivacaine, and dexmedetomidine in vascular surgery patients (many with hypertension); focus is anesthetic safety/efficacy, not hypertension treatment. |
| [28415943](https://pubmed.ncbi.nlm.nih.gov/28415943/) | 2017 | RCT | J Int Med Res | Scalp block with bupivacaine vs. levobupivacaine and its hemodynamic response during craniotomy. |
| [24258467](https://pubmed.ncbi.nlm.nih.gov/24258467/) | 2014 | Cohort | J Anesth | Interscalene block technique and its influence on adverse hemodynamic (hypertensive) events. |
| [32025936](https://pubmed.ncbi.nlm.nih.gov/32025936/) | 2019 | Cohort | JA Clin Rep | Peripheral nerve blocks with echocardiographic monitoring in a hypertrophic cardiomyopathy patient — perioperative case management. |
| [30417244](https://pubmed.ncbi.nlm.nih.gov/30417244/) | 2019 | Review | J Anesth | Practical guide for managing systemic toxicity from local anesthetics (general safety reference). |
| [17019175](https://pubmed.ncbi.nlm.nih.gov/17019175/) | 2001 | Review | Curr Opin Anaesthesiol | Alpha-2 agonists (e.g., clonidine) in regional anesthesia — antihypertensive effect belongs to the adjunct, not to levobupivacaine itself. |
| [18420857](https://pubmed.ncbi.nlm.nih.gov/18420857/) | 2008 | Review | Anesth Analg | General anesthesia's effect on CNS/cardiovascular toxicity of local anesthetics. |

*(Remaining literature entries in the source pack — e.g., PMID 40866214, 41003844, 27687315, 41018326, 18401551, 40125527, 24447815 — are case reports of regional anesthesia in patients who happen to have hypertension-adjacent comorbidities, and do not bear on antihypertensive efficacy.)*

### Supplementary Evidence: Exostosis (Rank 8, L4/S0)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36344405](https://pubmed.ncbi.nlm.nih.gov/36344405/) | 2022 | Case Report | Rev Esp Anestesiol Reanim | Costoclavicular brachial plexus block using 0.25% levobupivacaine for analgesia during pediatric osteotomy for multiple cartilaginous exostoses. Levobupivacaine is used here purely as a regional analgesic for surgery, not as a treatment for the exostosis (bone overgrowth) itself. |

---

## Singapore Market Information

Levobupivacaine currently has **no product registrations in Singapore** (market status: Not Marketed; 0 licenses on file). No dosage forms, brand names, or approved indication text are available from local regulatory sources.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available in this evidence pack (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (gastroduodenitis, 99.09% score) has no supporting clinical trials or literature and is explicitly flagged in the source data as an indirect knowledge-graph association without a plausible disease mechanism.
- The only candidate that reached decision stage S1 (hypertensive disorder, rank 9) is supported solely by anesthesia-related hemodynamic monitoring studies, not by evidence of antihypertensive efficacy — this does not constitute a repurposing signal.
- The drug is not currently marketed in Singapore, so there is no existing regulatory foothold to build on.

**To proceed, the following is needed:**
- TFDA/HSA product label (warnings and contraindications) — this is a **blocking** data gap that currently prevents any safety pre-assessment (S1).
- Confirmed mechanism-of-action data from the DrugBank API.
- If the migraine hypothesis (rank 6, "Research Question") is pursued, a dedicated literature search specific to Levobupivacaine's use in occipital nerve block for migraine — the current rationale relies on class-effect extrapolation from bupivacaine/lidocaine, not direct evidence.
- Continued monitoring for new trials/publications before revisiting the gastroduodenitis, peptic ulcer, gout, rhinitis, bronchitis, or ankylosing spondylitis candidates, none of which currently have any supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

