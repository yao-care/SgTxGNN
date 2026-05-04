---
layout: default
title: Camphor
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 10
---

# Camphor
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

# Camphor: From Traditional Counterirritant to Migraine Disorder

## One-Sentence Summary

Camphor (DB01744) is a naturally occurring bicyclic monoterpenoid with a long history of topical use as a counterirritant, but it currently holds no formally registered indication in Singapore.
The TxGNN model predicts it may have potential in **Migraine Disorder**, with **0 clinical trials** and **5 publications** retrieved — however, the available literature is largely non-supportive and includes adverse-event signals.
Given the speculative mechanistic basis and absence of direct efficacy evidence, this prediction is best treated as a **research question** rather than an actionable repurposing candidate at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not formally registered (traditionally used as topical counterirritant/analgesic) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Camphor is a bicyclic monoterpenoid (C₁₀H₁₆O) naturally derived from the camphor tree (*Cinnamomum camphora*). Detailed MOA data is not currently available from the evidence pack, but the published pharmacology literature identifies camphor as a partial **TRPV1 agonist** and **TRPM8 agonist** — both transient receptor potential (TRP) ion channels expressed in trigeminal sensory neurons. TRPV1 activation within the trigeminal vascular pathway is a well-recognised driver of neurogenic inflammation in migraine, while TRPM8 modulates cold-sensing and pain inhibition pathways. On this basis, the TxGNN model's prediction of a mechanistic link to migraine is biologically plausible at the receptor level.

Camphor also has documented modulating activity at **GABA-A receptors** (mild antagonism at higher concentrations). Because cortical spreading depression (CSD) — the electrophysiological event underlying migraine aura — is influenced by the excitatory/inhibitory balance in cortical circuits, there is a theoretical, though unverified, pathway through which camphor might affect migraine susceptibility. Traditional topical application of camphor-containing preparations for headache has historical precedent in several traditional medicine systems, lending indirect cultural plausibility to the prediction.

However, the available clinical literature contradicts a simple therapeutic narrative. Two case reports (PMIDs 34373243 and 35856604) specifically document **cluster headaches triggered** by toothpastes containing camphor and eucalyptus essential oils. This suggests that rather than relieving trigeminally-mediated head pain, TRPV1 activation by camphor may provoke it in susceptible individuals — an important adverse signal that must be resolved before any therapeutic hypothesis can advance. The mechanistic link therefore remains both unverified and facing contradictory clinical evidence.

---

## Clinical Trial Evidence

Currently no clinical trials specifically evaluating Camphor for migraine disorder have been registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/) | 2021 | Case Report | BMJ Case Reports | Two cases of cluster headache temporally linked to toothpastes containing camphor and eucalyptus essential oils — **adverse signal**, not efficacy evidence |
| [35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/) | 2022 | Case Series | Headache | Five cases of cluster headache attributed to toothpastes with pro-convulsant essential oils including camphor — reinforces the adverse signal above |
| [593588](https://pubmed.ncbi.nlm.nih.gov/593588/) | 1977 | Case Series / Historical | Minerva Medica | Historical report on therapy for essential hemicrania; camphor referenced in historical therapeutic context — no abstract available, extremely limited relevance |
| [27058833](https://pubmed.ncbi.nlm.nih.gov/27058833/) | 2016 | Historical Review | Z Kinder Jugendpsychiatr Psychother | Overview of neuropsychopharmacology in the 1940s–50s; camphor mentioned among historical substances used in neurology — indirect relevance only |
| [36404301](https://pubmed.ncbi.nlm.nih.gov/36404301/) | 2022 | Phase 3 RCT | J Headache Pain | DRAGON study evaluating **erenumab** (anti-CGRP monoclonal antibody) for chronic migraine in Asian patients — **not related to Camphor**; retrieved as a false positive |

> ⚠️ **Evidence Quality Notice**: None of the five retrieved publications provide efficacy evidence for camphor in migraine. Two papers document camphor-containing products as a potential headache **trigger**. The Phase 3 RCT (PMID 36404301) evaluates erenumab, not camphor, and should be excluded from evidence scoring.

---

## Safety Considerations

No formal safety data (package insert warnings, contraindications, or drug interaction records) was retrievable for this assessment. Based on known pharmacology and retrieved literature, the following concerns are flagged:

- **Potential Headache-Triggering Risk**: Published case reports indicate camphor-containing preparations may provoke cluster headache episodes in susceptible individuals (PMIDs 34373243, 35856604).
- **CNS Excitability Concern**: Camphor is known to lower seizure threshold and cause CNS stimulation at supratherapeutic doses (GABA-A antagonism). Systemic formulations would require careful dose control.
- **Drug Interaction Data**: No DDI data was retrievable. This gap must be addressed before any clinical use is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for camphor in migraine disorder rests entirely on a theoretical mechanistic hypothesis (L4), and the only directly relevant clinical literature contains **adverse signals** — camphor has been associated with triggering rather than relieving trigeminally-mediated head pain. A hold is appropriate until the mechanistic hypothesis can be disambiguated from these adverse findings in controlled preclinical settings.

**To proceed, the following is needed:**
- Dedicated **preclinical studies** (in vitro and in vivo) evaluating camphor's net effect on trigeminal pain pathways at clinically relevant, sub-toxic concentrations
- Clarification of **route-specific and dose-dependent effects**: topical versus systemic delivery may produce meaningfully different outcomes on TRPV1/TRPM8 activation
- Resolution of the **adverse signal**: mechanistic studies to determine whether camphor activates versus desensitises TRPV1 in trigeminal ganglia under migraine-relevant conditions
- **MOA data** from DrugBank (flagged Data Gap DG002)
- **Safety and contraindication data** from the Singapore Health Sciences Authority (flagged Data Gap DG001)
- A formal **risk-benefit assessment** before any clinical study design is considered, given the seizure risk profile of camphor at higher doses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

