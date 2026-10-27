---
layout: default
title: Caspofungin
parent: Low Evidence (L5)
nav_order: 217
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Caspofungin: predicted new indication Gastrin secretion abnormality (evidence level L5). Approved use: Esophageal candidiasis, candidemia"
monitor_inn: "Caspofungin"
predicted_indications: ["gastrin secretion abnormality", "punctate epithelial keratoconjunctivitis", "abnormality of glucagon secretion", "HIV infectious disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "exposure keratitis", "congenital candidiasis", "neonatal candidiasis", "candida glabrata"]
---

# Caspofungin
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

## Caspofungin: From Esophageal Candidiasis and Candidemia to Gastrin Secretion Abnormality
{: .text-alpha }

## One-Sentence Summary

> Caspofungin is an echinocandin antifungal, originally used to treat esophageal candidiasis and candidemia.
> The TxGNN model's top-ranked prediction is **gastrin secretion abnormality**, with a very high score (99.4%).
> However, there are **0 clinical trials** and **0 publications** supporting it, so this looks like a knowledge-graph artifact rather than a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Esophageal candidiasis, candidemia (taken from knowledge-graph indication links, because the Singapore licence records contain no indication text) |
| Predicted New Indication | Gastrin secretion abnormality |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Caspofungin inhibits 1,3-beta-D-glucan synthase, an enzyme that fungal cells need to build their cell wall. Detailed mechanism data was not available in the compiled data, but this is the established mechanism of the echinocandin class. It explains why the drug works against *Candida* infections.

This mechanism gives no plausible link to gastrin secretion abnormality. Mammalian cells do not have this target, and nothing known connects fungal cell-wall synthesis to gastrin regulation. The high score most likely reflects the structure of the knowledge graph rather than biology. In practice, the prediction is unsupported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Eight valid single-ingredient registrations are in the compiled data (no cancelled or combination licences). The records contain no approved-indication text, so that column is omitted. The five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN11762P | Cancidas Powder for Injection 50 mg/vial | Injection, powder, for solution |
| SIN15857P | Pergilas Powder for Concentrate for Solution for Infusion 50 mg/vial | Injection, powder, lyophilized, for solution |
| SIN15856P | Pergilas Powder for Concentrate for Solution for Infusion 70 mg/vial | Injection, powder, lyophilized, for solution |
| SIN15686P | Fupascin Powder for Concentrate for Solution for Infusion 70 mg/vial | Injection, powder, lyophilized, for solution |
| SIN15687P | Fupascin Powder for Concentrate for Solution for Infusion 50 mg/vial | Injection, powder, lyophilized, for solution |

All products are injectable. The other three registrations are Caspocan 50 mg and Dalvocans 50 mg and 70 mg.

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (not taken from label text): liver disease, gallbladder disease, potassium deficiency disease.
- **Drug Interactions**: 81 known interactions were found.
  - Major: dexamethasone.
  - Moderate: naltrexone.
  - Many others have an unclassified severity, including pantoprazole, omeprazole, lansoprazole, vancomycin, amphotericin B, prednisone, hydrocortisone, simvastatin and potassium chloride.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction has no clinical or literature support. The drug's mechanism has no identifiable connection to gastrin secretion, so it should not be pursued.
- Among the other TxGNN predictions, **neonatal candidiasis** is the one with the most evidence (L2, Proceed with Guardrails). Two Phase 2 trials support it:
  - NCT00330395: open-label safety and pharmacokinetics study, 16 patients, completed.
  - NCT01945281: randomized trial against amphotericin B, 51 patients, terminated early.
- Neonatal candidiasis is an extension of the existing antifungal indication, not a new mechanism. Other predictions (HIV-related fungal infections, congenital candidiasis, *Candida glabrata*) rest mostly on case reports, reviews and resistance studies.

**To proceed, the following is needed:**
- For gastrin secretion abnormality: a plausible mechanistic hypothesis and preclinical data before any further evaluation.
- If the neonatal candidiasis direction is pursued: the reason NCT01945281 was terminated, neonatal dosing guidance, hepatic monitoring, and a drug-interaction review.
- Singapore package insert warnings and contraindications, which are still missing from the compiled data.
- Mechanism of action data from DrugBank.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

