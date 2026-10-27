---
layout: default
title: Terbinafine
parent: Low Evidence (L5)
nav_order: 966
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Terbinafine: predicted new indication Creeping myiasis (evidence level L5). Approved use: Tinea pedis, tinea corporis, tinea unguium…"
monitor_inn: "Terbinafine"
predicted_indications: ["creeping myiasis", "furuncular myiasis", "wound myiasis", "myiasis", "toxoplasmosis", "blastomycosis", "echinococcus granulosus infectious disease"]
---

# Terbinafine
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

## Terbinafine: From Tinea (Dermatophyte Skin Infections) to Creeping Myiasis
{: .text-alpha }

## One-Sentence Summary

Terbinafine is an antifungal originally used for tinea infections such as tinea pedis, tinea corporis, tinea unguium and pityriasis versicolor.
The TxGNN model predicts it may be effective for **creeping myiasis**, a skin infestation by fly larvae.
**No clinical trials** and **no publications** currently support this prediction, and the plausibility of a real drug effect is very low.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, tinea corporis, tinea unguium, pityriasis versicolor and other dermatophyte infections (the Singapore registry entries do not state approved indication text) |
| Predicted New Indication | Creeping myiasis |
| TxGNN Prediction Score | 96.74% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

It is not, based on the data compiled for this report. Detailed mechanism data is not available in the source record, but terbinafine is known to inhibit fungal squalene epoxidase, an enzyme in ergosterol synthesis. This depletes ergosterol and causes squalene to accumulate, which kills dermatophytes.

Creeping myiasis is a parasitic infestation by fly larvae, which are arthropods. They have no ergosterol pathway and no relevant drug target. The two conditions are both skin diseases, which probably explains the graph similarity. The high score looks like an artifact of the knowledge graph, where myiasis subtypes score almost identically (96.74% for creeping, furuncular and wound myiasis). It is unlikely to be a real pharmacological signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

For context, the closely related myiasis predictions in the same output retrieved only two papers:
- A diagnostic case report of furuncular myiasis in a boy whose lesion did not respond to several drugs, including terbinafine (PMID 25016125).
- A case report of chromoblastomycosis with concurrent myiasis in a kidney transplant recipient (PMID 39081689).

Neither shows a terbinafine benefit against myiasis.

## Singapore Market Information

Terbinafine has 8 valid single-ingredient registrations in Singapore (oral tablets, creams, a gel and a spray). The registry entries do not state approved indication text. Five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN06932P | Lamisil Tablet 250 mg | Tablet, film coated |
| SIN16925P | Fungifex Tablet 250 mg | Tablet |
| SIN07623P | Lamisil Cream 1% | Cream |
| SIN10617P | Lamisil Dermgel 1% | Gel |
| SIN15413P | Dermafin Cream 10 mg/g | Cream |

## Safety Considerations

- **Drug Interactions**: 100 interactions are listed. The main ones are:
  - Major: eliglustat.
  - Moderate: morphine, naltrexone, ondansetron, dexfenfluramine, fenfluramine.
  - Minor: cimetidine.
  - The remaining entries have unclassified severity.
- **Conditions flagged in the knowledge graph** (not taken from package insert text): kidney disease, liver disease, gallbladder disease, systemic lupus erythematosus (including pediatric), pyoureter and substance abuse/dependence. These need confirmation against the official package insert.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- There is no plausible mechanism, no trials and no supportive literature. The only retrieved papers are case reports that do not show efficacy.
- The score of 96.74% reflects similarity within the knowledge graph rather than evidence of benefit. It does not justify moving this indication forward.

**To proceed, the following is needed:**
- Any direct experimental evidence (in vitro or in vivo) that terbinafine acts on fly larvae.
- The package insert warnings and contraindications from the Singapore regulator, which were not available for this report.
- Detailed mechanism of action data.

**Alternative directions:** Other predictions from the same model have a much stronger rationale and are better candidates for further evaluation. These are tinea manuum and superficial mycosis, both at evidence level L3 and recommended "Proceed with Guardrails". They largely extend or restate terbinafine's existing antifungal use. Guardrails would include susceptibility testing because of emerging terbinafine-resistant dermatophytes, hepatic monitoring, and management of drug interactions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

