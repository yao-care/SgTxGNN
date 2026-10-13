---
layout: default
title: Isosorbide Mononitrate
parent: Low Evidence (L5)
nav_order: 557
evidence_level: L5
indication_count: 10
---

# Isosorbide Mononitrate
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

# Isosorbide Mononitrate: From Angina-Type Vasodilator Use to Hypertrichosis (Predicted)

## One-Sentence Summary

Isosorbide mononitrate is an oral nitric oxide (NO) donor vasodilator marketed in Singapore as modified-release 60 mg tablets. The approved indication text is not recorded in the data compiled for this report.
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are **0 clinical trials** and **0 publications** for this prediction, so it rests on model output alone.
The only disease among the top 10 predictions with any published literature is pulmonary arterial hypertension (2 indirect publications).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the approved indication text on both Singapore licences is blank) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, isosorbide mononitrate is an organic nitrate that releases nitric oxide, activates soluble guanylate cyclase and raises cGMP, which produces vasodilation.

A link to hypertrichosis is speculative at best. One could argue that increased skin blood flow might influence hair follicles, as is proposed for minoxidil, which acts through a different mechanism. No data compiled for this report support this idea. The very high score is most likely an artefact of the knowledge graph, which clusters hair-related diseases together.

The same applies to the other hair and congenital predictions (Ambras syndrome, alopecia, hypotrichosis, alopecia areata, hair shaft abnormalities). These are genetic, structural or autoimmune conditions that a vasodilator would not be expected to alter.

The one biologically plausible prediction among the top 10 is **pulmonary arterial hypertension** (score 99.94%, rank 10). The NO-cGMP pathway is a validated PAH target, as with sildenafil and riociguat. However, organic nitrates have limited use in PAH because of tolerance, systemic hypotension and ventilation-perfusion mismatch.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for hypertrichosis or for any of the other top 10 predicted indications.

---

## Literature Evidence

No literature is available for hypertrichosis. The only literature among the top 10 predictions relates to pulmonary arterial hypertension and is indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16422873](https://pubmed.ncbi.nlm.nih.gov/16422873/) | 2005 | Clinical hemodynamic study | J Sex Med | Hemodynamic effects of sildenafil combined with isosorbide mononitrate in men with coronary artery disease and erectile dysfunction (not PAH) |
| [29705351](https://pubmed.ncbi.nlm.nih.gov/29705351/) | 2018 | Preclinical animal study | Life Sci | Stimulation of NO-sensitive soluble guanylate cyclase in monocrotaline-induced pulmonary hypertensive rats |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10515P | IMDEX CR TABLET 60 mg | Film-coated tablet | Not recorded |
| SIN01996P | IMDUR DURULES TABLET 60 mg | Film-coated tablet | Not recorded |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not taken from label text): hypotensive disorder, hypertrophic cardiomyopathy, myocardial infarction, coronary thrombosis, hemoglobinopathy, anaemia (including macrocytic anaemia), hyperthyroidism, Graves disease, thyrotoxicosis and intracerebral haemorrhage.
- **Drug Interactions**: 189 interactions were identified. Those listed include moderate-level interactions with bupropion, morphine, dronabinol, nabilone, opium, sapropterin, rosiglitazone and the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin). Omeprazole is a minor interaction.
- **Combination with PDE5 inhibitors** (such as sildenafil) is a concern because of profound hypotension. This is a contraindicated interaction.
- Nitrates may raise intracranial pressure, which is relevant to the Dandy-Walker syndrome prediction.

Please refer to the package insert for full safety information, as label warnings and contraindications were not available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The hypertrichosis prediction has no clinical trials, no literature and no plausible mechanism (Evidence Level L5). The high score likely reflects knowledge-graph clustering of hair disorders. Pulmonary arterial hypertension is more plausible biologically (Evidence Level L4), but the evidence is indirect and organic nitrates have known limitations in PAH, so it should be treated as a research question rather than a candidate for action.

**To proceed, the following is needed:**
- The HSA package insert, covering approved indications, warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Direct clinical or mechanistic evidence for the proposed indication, for example whether NO donation affects hair follicle biology
- For PAH, a review of whether nitrate tolerance, hypotension and PDE5 inhibitor co-prescription issues can be managed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

