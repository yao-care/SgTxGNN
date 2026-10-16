---
layout: default
title: Gabapentin
parent: Low Evidence (L5)
nav_order: 461
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Gabapentin: predicted new indication Myofascial pain syndrome . The top-ranked prediction by score is acne… (evidence level L5). Approved use: Restless legs syndrome"
monitor_inn: "Gabapentin"
predicted_indications: ["acne (disease)", "adolescent/adult onset autosomal dominant epilepsy with auditory features", "epilepsy with generalized tonic-clonic seizures", "myofascial pain syndrome", "visual epilepsy", "active cochlear Meniere disease", "active vestibular Meniere disease", "active cochleovestibular Meniere disease", "trigeminal nerve neoplasm", "osteoarthritis susceptibility"]
---

# Gabapentin
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

# Gabapentin: From Restless Legs Syndrome and Postherpetic Neuralgia to Myofascial Pain Syndrome

## One-Sentence Summary

Gabapentin was originally used for restless legs syndrome and postherpetic neuralgia, and it is also an established antiseizure drug.
The TxGNN model's top-ranked prediction is acne, which has no supporting evidence, so this report focuses on the best-supported prediction, **myofascial pain syndrome**. It has **4 clinical trials** (all in the related condition fibromyalgia) and **8 publications**, including one randomized controlled trial in chronic masticatory muscle pain.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Restless legs syndrome; postherpetic neuralgia (from the knowledge graph, as no approved indication text is available for the Singapore licences) |
| Predicted New Indication | Myofascial pain syndrome (evidence-supported prediction). The top-ranked prediction by score is acne (98.46%), with no clinical trials or literature. |
| TxGNN Prediction Score | 92.97% (myofascial pain syndrome); 98.46% (acne, rank 1) |
| Evidence Level | L2 (myofascial pain syndrome); L5 (acne) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 14 |
| Recommended Decision | Proceed with Guardrails (myofascial pain syndrome); Hold (acne) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. From the supporting literature, gabapentin binds the alpha-2-delta subunit of voltage-gated calcium channels. This reduces the release of excitatory neurotransmitters and dampens central sensitization and neuropathic-type pain signalling.

Postherpetic neuralgia, one of gabapentin's original indications, is a neuropathic pain condition. Myofascial pain syndrome is a chronic regional muscle pain condition. Persistent muscle pain is thought to involve central sensitization, so the pain pathways plausibly overlap. This is the mechanistic basis for the prediction.

The evidence is largely indirect. Most trials were run in fibromyalgia, a related but distinct condition. The closest evidence is a 12-week randomized controlled trial of gabapentin in chronic masticatory muscle pain (PMID 17030096).

The other high-scoring predictions are weaker. Acne and the Meniere disease subtypes rest on graph prediction alone. Epilepsy-related predictions have a class-level rationale but no disease-specific trials. The trigeminal nerve neoplasm label matches only pain-symptom literature, not treatment of the tumour.

## Clinical Trial Evidence

All trials below are for myofascial pain syndrome, the best-supported prediction. They were run in fibromyalgia, so they are indirect evidence.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00057278](https://clinicaltrials.gov/study/NCT00057278) | Phase 2/3 | Completed | 150 | Gabapentin in Fibromyalgia Trial (GIFT): safety and effectiveness for fibromyalgia pain |
| [NCT01107574](https://clinicaltrials.gov/study/NCT01107574) | Phase 3 | Completed | 41 | Gabapentin, osteopathic manipulative medicine, or both for fibromyalgia. Small sample, and the combination design confounds the gabapentin effect. |
| [NCT05384210](https://clinicaltrials.gov/study/NCT05384210) | N/A | Unknown | 75 | Milnacipran vs gabapentin vs combination in fibromyalgia |
| [NCT02052414](https://clinicaltrials.gov/study/NCT02052414) | N/A | Completed | 34 | Open-label, non-randomized study of Gralise (gabapentin) in fibromyalgia. Uncontrolled and small. |

No clinical trials are registered for the other predicted indications (acne, epilepsy subtypes, Meniere disease subtypes, trigeminal nerve neoplasm, osteoarthritis susceptibility).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17030096](https://pubmed.ncbi.nlm.nih.gov/17030096/) | 2007 | RCT | Pain | 12-week RCT (50 patients) of gabapentin for chronic masticatory muscle pain |
| [25905532](https://pubmed.ncbi.nlm.nih.gov/25905532/) | 2015 | Open-label cohort | J Oral Facial Pain Headache | Stepped treatment with tricyclic antidepressants and gabapentin in persistent myofascial pain |
| [40110636](https://pubmed.ncbi.nlm.nih.gov/40110636/) | 2025 | Review | Muscle & Nerve | Update on myofascial pain syndrome: characteristics, causes, diagnosis and treatment |
| [9303258](https://pubmed.ncbi.nlm.nih.gov/9303258/) | 1997 | Clinical study | Clin J Pain | Effect of gabapentin on pain scores and opiate use in neuropathic pain |
| [37142285](https://pubmed.ncbi.nlm.nih.gov/37142285/) | 2023 | Case report | BMJ Case Reports | Levator ani syndrome (a myofascial pain condition) presenting with vaginal pain |
| [32627323](https://pubmed.ncbi.nlm.nih.gov/32627323/) | 2020 | Case report | Am J Med Genet A | Benefit of gabapentin in two children with Noonan syndrome and neuropathic pain |

## Singapore Market Information

Fourteen valid single-ingredient licences are registered. The licence data do not include approved indication text. The five main ones are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08302P | NEURONTIN CAPSULE 400 mg | Capsule | Not stated in licence data |
| SIN08303P | NEURONTIN CAPSULE 300 mg | Capsule | Not stated in licence data |
| SIN17166P | GRALISE EXTENDED RELEASE TABLETS 300 MG | Extended-release tablet | Not stated in licence data |
| SIN17165P | GRALISE EXTENDED RELEASE TABLETS 600 MG | Extended-release tablet | Not stated in licence data |
| SIN13677P | Gabapentin Sandoz Capsules 300mg | Capsule | Not stated in licence data |

All products are oral (capsules or extended-release tablets).

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (graph-derived, not from label text): anxiety disorder, neurotic disorder, dysthymic disorder, kidney disease, pyoureter.
- **Drug Interactions**: 100 interactions were found. The main ones are:
  - **Major**: morphine and liposomal morphine.
  - **Moderate**: dronabinol, nabilone, metoclopramide, opium, sibutramine.
  - **Minor**: cimetidine and antacids (magnesium oxide, magnesium carbonate, magnesium hydroxide, aluminium hydroxide, magaldrate).
- **Literature notes**: gabapentin may be misused, especially with opioids, and it has psychiatric and behavioural side effects.

Please refer to the package insert for key warnings and formal contraindications, as label data were not available.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (myofascial pain syndrome); Hold (acne and the other predictions without evidence)**

**Rationale:**
- For myofascial pain syndrome, the mechanism is plausible. There is one RCT in a closely related muscle pain condition (masticatory myalgia) and several fibromyalgia trials. However, no trial directly targets myofascial pain syndrome.
- Acne, the Meniere disease subtypes and osteoarthritis susceptibility have no clinical evidence. The epilepsy-related and trigeminal nerve neoplasm predictions have only indirect evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, which are currently missing and blocking safety screening.
- Detailed mechanism of action data, for example from DrugBank.
- A trial or systematic review that directly addresses myofascial pain syndrome.
- A safety plan for patients taking opioids, and for patients with kidney disease or psychiatric comorbidity.
- A check of the 12-week masticatory myalgia RCT for effect size and risk of bias.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

