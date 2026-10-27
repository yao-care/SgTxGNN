---
layout: default
title: Pinazepam
parent: Low Evidence (L5)
nav_order: 794
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pinazepam: predicted new indication Insomnia (evidence level L5). Approved use: Not recorded in the Singapore licence data (literature suggests anxie…"
monitor_inn: "Pinazepam"
predicted_indications: ["insomnia (disease)", "alcohol withdrawal delirium", "antidepressant type abuse", "barbiturate abuse", "hallucinogen abuse", "anxiety", "sleep disorder, initiating and maintaining sleep", "anxiety disorder", "alcohol withdrawal", "dysthymic disorder"]
---

# Pinazepam
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

## Pinazepam: From Anxiety (Benzodiazepine Anxiolytic) to Insomnia
{: .text-alpha }

## One-Sentence Summary

Pinazepam is a benzodiazepine that the body converts into N-desmethyldiazepam (nordazepam), and it is marketed in Singapore as an oral capsule. No approved indication text is recorded for it in the data compiled for this report.
The TxGNN model predicts it may be effective for **insomnia** (top-ranked prediction), but there are currently **no clinical trials and no publications** directly supporting this indication.
The evidence is a computational prediction only (Level L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Singapore licence data (literature suggests anxiety) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, pinazepam is a 1,4-benzodiazepine prodrug. It is converted mainly by N-dealkylation into N-desmethyldiazepam (nordazepam), a long-acting positive allosteric modulator of the GABA-A receptor. This class produces sedative, hypnotic and anxiolytic effects.

Because GABA-A potentiation underlies the sedative-hypnotic action of benzodiazepines, the link to insomnia is mechanistically plausible. A 1984 review, however, describes pinazepam as having a comparatively low hypnotic effect and limited motor impairment in animals. This weakens the case for insomnia specifically. The high TxGNN score is a graph-based association, not clinical evidence.

**Other predictions for context:**
- **Sleep disorder (initiating and maintaining sleep):** essentially the same entity as insomnia, with no supporting studies.
- **Anxiety and anxiety disorder:** the only predictions with literature (L3), but these likely overlap with the drug's original use, so they are closer to on-label use than true repurposing.
- **Alcohol withdrawal and alcohol withdrawal delirium:** benzodiazepines are standard of care, but no pinazepam-specific evidence exists and established agents are available.
- **Antidepressant, barbiturate and hallucinogen abuse:** identical scores across these terms suggest a generic graph artifact with weak or no rationale.
- **Dysthymic disorder:** no strong mechanistic rationale, and no evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for insomnia.

## Literature Evidence

Currently no related literature available for insomnia.

For the related predicted indication **anxiety / anxiety disorder**, the following publications were found (most relevant first):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6147192](https://pubmed.ncbi.nlm.nih.gov/6147192/) | 1984 | Review | Clinical Therapeutics | Review of pinazepam's pharmacology and therapeutic efficacy. Controls anxiety and aggression in animals, with low hypnotic effect and less toxicity than diazepam |
| [12907](https://pubmed.ncbi.nlm.nih.gov/12907/) | 1976 | Open-label trial | La Clinica Terapeutica | Open clinical trial of pinazepam (no abstract available) |
| [7006888](https://pubmed.ncbi.nlm.nih.gov/7006888/) | 1980 | Clinical study | La Clinica Terapeutica | Clinical research in gastrointestinal psychosomatic diseases (no abstract available) |
| [28903606](https://pubmed.ncbi.nlm.nih.gov/28903606/) | 2017 | Review | Drug Metabolism Reviews | Metabolic profile of oxazepam and related benzodiazepines, including pinazepam, with clinical and forensic aspects |
| [6809477](https://pubmed.ncbi.nlm.nih.gov/6809477/) | 1982 | Pharmacokinetic | Eur J Clin Pharmacol | Pinazepam acts as a prodrug; its metabolite reaches higher plasma levels than the parent shortly after a 10 mg oral dose |
| [6147314](https://pubmed.ncbi.nlm.nih.gov/6147314/) | 1983 | Pharmacokinetic | Int J Clin Pharmacol Res | Kinetics in six healthy volunteers after a single 10 mg oral dose |
| [6150857](https://pubmed.ncbi.nlm.nih.gov/6150857/) | 1984 | Pharmacokinetic | Eur J Clin Pharmacol | Placental transfer of pinazepam and its metabolite in 25 women at term |
| [26359](https://pubmed.ncbi.nlm.nih.gov/26359/) | 1978 | Preclinical | Arzneimittel-Forschung | In rats, pinazepam was more than twice as active as diazepam in reducing conditioned emotional response |
| [240369](https://pubmed.ncbi.nlm.nih.gov/240369/) | 1975 | Preclinical/Toxicology | Arzneimittel-Forschung | Lower toxicity, hypnotic and muscle-relaxant activity than diazepam |
| [6124406](https://pubmed.ncbi.nlm.nih.gov/6124406/) | 1982 | Preclinical PK | Drug Metab Dispos | Rapid absorption and conversion to N-desmethyldiazepam in rats, with a liver first-pass effect |

These studies are mostly pharmacokinetic or preclinical, dated, and not randomized controlled trials.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN01038P | DOMAR CAPSULE 5 mg (Polipharm Co Ltd) | Capsule (oral) | Not recorded |

## Safety Considerations

- **Drug Interactions:** No interaction records were found for this drug.
- **Knowledge-graph contraindications:** No drug-disease contraindication edges were found.

Please refer to the package insert for warnings and contraindications. As a benzodiazepine, dependence, abuse liability, sedation and fetal exposure are class concerns, and placental transfer has been documented for pinazepam and its metabolite (PMID 6150857).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction rests only on a model score, with no trials or literature, and early animal data suggest pinazepam has a relatively low hypnotic effect. The better-supported indications (anxiety) are probably the drug's original use rather than true repurposing.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications, approved indication), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Clinical efficacy data for pinazepam in insomnia, such as sleep studies or comparisons with established hypnotics
- A comparison against existing benzodiazepines and other hypnotics already marketed in Singapore
- A dependence and abuse-risk assessment for any sleep-related use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

