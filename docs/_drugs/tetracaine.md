---
layout: default
title: Tetracaine
parent: Low Evidence (L5)
nav_order: 976
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "Tetracaine"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "bronchitis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acne keloid", "hydroa vacciniforme, familial", "amyopathic dermatomyositis", "cauda equina syndrome", "irritable bowel syndrome"]
description: "Tetracaine: predicted new indication Acrodermatitis chronica atrophicans (evidence level L5). Approved use: Not recorded in the local data"
---

# Tetracaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Tetracaine: Acrodermatitis chronica atrophicans
{: .text-alpha }

## One-Sentence Summary

Tetracaine is an ester-type local anaesthetic, with dermatitis as its original indication, and marketed in Singapore as eye drops and a topical cream.
The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans**, but there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 3 of 3) |
| Number of Registrations | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Tetracaine is known as an ester local anaesthetic that blocks sodium channels, which produces local numbness. It has no recognised antimicrobial or anti-inflammatory activity.

Acrodermatitis chronica atrophicans is a late-stage skin manifestation of Borrelia infection and is treated with antibiotics. No mechanistic link to tetracaine could be identified. The high score most likely reflects the model's network proximity to dermatological indications rather than real biology, so the prediction should be treated as a hypothesis only.

Other top-ranked predictions show the same pattern. Neonatal dermatomyositis, amyopathic dermatomyositis, hydroa vacciniforme, pediatric connective-tissue-disease-associated interstitial lung disease, bronchitis, irritable bowel syndrome and pityriasis simplex all have no supporting trials or literature and no plausible disease-modifying mechanism. Two predictions have some linked evidence:
- **Acne keloid (rank 5):** the evidence concerns procedural pain relief only, not treatment of the disease.
- **Cauda equina syndrome (rank 8):** the literature shows tetracaine can cause this condition after spinal use, so this is a safety signal rather than a repurposing opportunity.

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top predicted indication (acrodermatitis chronica atrophicans).

For reference, one trial was found for the rank-5 prediction, acne keloid:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02372786](https://clinicaltrials.gov/study/NCT02372786) | Phase 4 | Completed | 30 | Randomized, double-blind comparison of 7% lidocaine/7% tetracaine cream vs 2.5% lidocaine/2.5% prilocaine cream for pain during laser treatment of acne keloidalis nuchae and tattoo removal. It tests procedural anaesthesia, not disease treatment. |

## Literature Evidence

Currently no related literature is available for the top predicted indication (acrodermatitis chronica atrophicans).

For reference, selected publications for other predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27377616](https://pubmed.ncbi.nlm.nih.gov/27377616/) | 2017 | RCT | Br J Dermatol | Lidocaine/tetracaine cream vs lidocaine/prilocaine cream for anaesthesia during laser treatment of acne keloidalis nuchae and tattoo removal (two randomized trials). Procedural pain relief only. |
| [9033758](https://pubmed.ncbi.nlm.nih.gov/9033758/) | 1996 | Review | Ann Fr Anesth Reanim | Neurotoxicity of intrathecally administered agents, including spinal cord and nerve root lesions. |
| [10876464](https://pubmed.ncbi.nlm.nih.gov/10876464/) | 2000 | Review | AANA J | Transient neurologic symptoms associated with spinal anaesthesia. |
| [30625770](https://pubmed.ncbi.nlm.nih.gov/30625770/) | 2009 | Case report | Korean J Anesthesiol | Cauda equina syndrome after spinal anaesthesia with 0.5% hyperbaric tetracaine plus epinephrine. |
| [11685003](https://pubmed.ncbi.nlm.nih.gov/11685003/) | 2001 | Case report | Anesthesiology | Cauda equina syndrome after spinal tetracaine, with 20-year electromyographic follow-up. |
| [8017646](https://pubmed.ncbi.nlm.nih.gov/8017646/) | 1994 | Preclinical (in vitro) | Anesthesiology | High concentrations of local anaesthetics caused irreversible conduction block in isolated nerve. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN04204P | Minims Tetracaine Hydrochloride Eye Drops 1% w/v | Solution | Not stated in the registration record |
| SIN04188P | Minims Tetracaine Hydrochloride Eye Drops 0.5% w/v | Solution | Not stated in the registration record |
| SIN14793P | Pliaglis Cream 70mg/g + 70mg/g | Cream | Not stated in the registration record |

## Safety Considerations

- **Contraindications (associations, not label text):** The following conditions are associated with tetracaine and should be checked against the package insert:
  - Neurological and neuromuscular: epilepsy, myasthenia gravis (including adult-onset), neuromuscular junction disease, butyrylcholinesterase deficiency
  - Cardiac and respiratory: heart disease, cardiovascular disease, sudden cardiac arrest, heart conduction disease, respiratory failure
  - Organ function and metabolic: kidney disease, liver disease, gallbladder disease, pyoureter, hyperthyroidism, Graves disease, thyrotoxicosis
  - Eye: uveitis, panuveitis, iris disease, ciliary body disease, eye infectious disease, conjunctivitis
- **Drug Interactions:** 32 interactions were recorded in total. Examples from the 20 listed:
  - **Major:** nitrous acid, liposomal bupivacaine
  - **Moderate:** other local anaesthetics (lidocaine, benzocaine, cocaine, proparacaine, oxybuprocaine, cinchocaine); benzodiazepines (alprazolam, chlordiazepoxide, clobazam, clonazepam, diazepam, estazolam); sulfonamides (sulfasalazine, sulfamethoxazole)
  - **Minor:** hyaluronidase
- **Neurotoxicity signal:** Published case reports and preclinical studies link intrathecal tetracaine to cauda equina syndrome and persistent nerve deficits.

Package insert warnings were not available in the data compiled for this report. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials or literature for acrodermatitis chronica atrophicans and no plausible mechanism, since the disease is infectious and antibiotic-treated. The same holds for most other top predictions, and the cauda equina syndrome result is a safety signal rather than a therapeutic one.

**To proceed, the following is needed:**
- Mechanism of action data, to allow a proper mechanistic-link analysis
- Package insert warnings and contraindications from the Singapore regulator (HSA), which are needed before safety screening
- Approved indication text for the three Singapore licences
- Any preclinical or clinical evidence for a disease-relevant effect, if a new indication is to be pursued
- Review of whether the original dermatitis indication is supported
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

