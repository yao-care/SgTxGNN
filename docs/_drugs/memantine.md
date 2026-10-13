---
layout: default
title: Memantine
parent: Low Evidence (L5)
nav_order: 647
evidence_level: L5
indication_count: 10
---

# Memantine
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

# Memantine: From Alzheimer's Dementia to Pulmonary Hypertension

## One-Sentence Summary

Memantine is an NMDA receptor antagonist. The Singapore registration data compiled for this report do not state its approved indication, but the drug is generally used for dementia in Alzheimer's disease. The TxGNN model predicts it may be effective for **pulmonary hypertension**, but **no clinical trials** and only **2 loosely related publications** support this direction, so the prediction rests almost entirely on computation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the HSA licence data (generally used for Alzheimer's dementia) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, memantine is a non-competitive NMDA receptor antagonist. Its efficacy in its original use is established, and mechanistically it may be applicable to pulmonary hypertension.

Some preclinical work links the glutamate/NMDA receptor axis to pulmonary arterial hypertension, acute lung injury and metabolic regulation. NMDA receptors are also expressed in the pulmonary vasculature. However, the retrieved literature does not test memantine in pulmonary hypertension, so the link is plausible but unproven. The high TxGNN score is a computational prediction only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33500723](https://pubmed.ncbi.nlm.nih.gov/33500723/) | 2021 | Preclinical/Mechanistic | Theranostics | Activating NMDA receptors affects insulin sensitivity and lipid metabolism. The paper notes the glutamate/NMDAR axis has been implicated in pulmonary arterial hypertension, but it does not test memantine for this disease. |
| [41739394](https://pubmed.ncbi.nlm.nih.gov/41739394/) | 2026 | Phase 1 PK/safety | Clinical Drug Investigation | MN-08, a nitrate derivative of memantine, is under development for pulmonary arterial hypertension. This study assessed its safety and pharmacokinetics in healthy Chinese volunteers. It is a different compound, tested in healthy people rather than patients. |

---

## Singapore Market Information

All 8 registrations are valid single-ingredient oral film-coated tablets (10 mg). The licence records contain no approved indication text. The five listed below are a selection.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12315P | Ebixa Tablet 10 mg | Tablet, film coated | Not stated in the licence record |
| SIN15609P | Admenta 10 Film Coated Tablet 10 mg | Tablet, film coated | Not stated in the licence record |
| SIN15599P | Avanten Film-Coated Tablets 10 mg | Tablet, film coated | Not stated in the licence record |
| SIN15120P | Marixino Film-Coated Tablets 10 mg | Tablet, film coated | Not stated in the licence record |
| SIN14801P | Nemdatine Film Coated Tablet 10 mg | Tablet, film coated | Not stated in the licence record |

---

## Safety Considerations

- **Disease associations from the knowledge graph (not label text)**: liver disease, gallbladder disease and impaired renal function are linked to memantine as contraindication-type relationships. These need confirmation against the package insert.
- **Drug Interactions**: 100 interactions were found. The 20 reviewed here include:
  - **Moderate**: anticholinergic or antimuscarinic agents, namely hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, methscopolamine, propantheline, scopolamine, trospium and mepenzolate.
  - **Minor**: ranitidine, metformin, cimetidine and potassium citrate.
  - **Unknown severity**: glimepiride, doxycycline, lansoprazole, loperamide, famotidine and acetylsalicylic acid.

Package insert warnings and contraindications were not available. Please refer to the package insert for the full safety profile.

---

## Other Predicted Indications Worth Noting

The pulmonary hypertension prediction ranks first by score but has the weakest evidence. Other predictions in the same list have considerably more support:

| Predicted Indication | Evidence Level | Support |
|------|------|------|
| Migraine disorder | L1 (assigned cautiously) | One completed Phase 3 trial, [NCT04698525](https://clinicaltrials.gov/study/NCT04698525) (memantine vs sodium valproate for episodic migraine prophylaxis, n=33). Also several meta-analyses and systematic reviews, including [33961371](https://pubmed.ncbi.nlm.nih.gov/33961371/) and [34352118](https://pubmed.ncbi.nlm.nih.gov/34352118/). Reviews describe the evidence as limited ("big promise but little evidence"). |
| Migraine with brainstem aura | L2 | Indirect: a placebo-controlled RCT in migraine without aura ([26638119](https://pubmed.ncbi.nlm.nih.gov/26638119/)). |
| Rheumatoid arthritis | L4 | Preclinical only, including an animal arthritis model ([22134197](https://pubmed.ncbi.nlm.nih.gov/22134197/)). |

The remaining predictions (kyphoscoliotic heart disease, nephrogenic syndrome of inappropriate antidiuresis, atrophoderma vermiculata, ulerythema ophryogenesis and brachydactyly-syndactyly syndrome) have no supporting trials or literature.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pulmonary hypertension prediction scores very high (99.54%), but there are no clinical trials and no published studies testing memantine itself in this disease. The only clinical-stage link is a Phase 1 study of a different compound, the memantine derivative MN-08, in healthy volunteers. This is a model-generated hypothesis at evidence level L5.

**To proceed, the following is needed:**
- Preclinical studies of memantine in pulmonary hypertension models, since the NMDA receptor link in the pulmonary vasculature is still indirect
- Safety review of memantine for pulmonary hypertension patients, including the renal and hepatic associations and anticholinergic interactions noted above
- The HSA package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism of action data (MOA)
- Review of progress on MN-08 as a possible route to this indication
- Consideration of migraine, where trial and meta-analysis evidence already exists, as a more evidence-backed repurposing direction. A larger, adequately powered trial would be needed to confirm it.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

