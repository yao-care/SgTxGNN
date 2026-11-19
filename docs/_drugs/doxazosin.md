---
layout: default
title: Doxazosin
parent: Low Evidence (L5)
nav_order: 351
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
monitor_inn: "Doxazosin"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
description: "Doxazosin: predicted new indication Migraine disorder (evidence level L5). In Singapore: 1 HSA registration (1 valid)"
---

# Doxazosin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Doxazosin: Migraine disorder
{: .text-alpha }

## One-Sentence Summary

Doxazosin is an alpha-1 adrenergic blocker originally used to treat hypertension and benign prostatic hyperplasia.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **no registered clinical trials** and only **1 publication** (a small case series) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9920 |
| Evidence Level | L5 (model prediction with only a small uncontrolled case series; no trials) |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for doxazosin: "Benign Prostatic Hyperplasia (BPH) The symptoms associated with benign prostatic hyperplasia (BPH), such as urinary frequency, nocturia, weak stream, hesitancy, and incomplete emptying are related to two components, anatomical (static) and functional (dynamic). The static component is related to an increase in prostate size caused, in part, by a proliferation of smooth muscle cells in the prostatic stroma. […] Studies in normal human subjects have shown that doxazosin competitively antagonized the pressor effects of phenylephrine (an alpha 1 agonist) and the systolic pressor effect of norepinephrine." ([DailyMed: Cardura (doxazosin) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5e1f5e49-2da1-43ab-9795-228a8bcc5a82), label version 2023-10-15; accessed 2026-11-19.) Based on known pharmacology, doxazosin is an alpha-1 adrenergic receptor antagonist. It relaxes vascular smooth muscle (lowering blood pressure) and prostatic smooth muscle (easing urinary symptoms).

The link to migraine is plausible but indirect. Adrenergic signalling and vascular tone regulation have been proposed to contribute to migraine, and other agents acting on the adrenergic system (for example propranolol and clonidine) are used for prophylaxis. The very high TxGNN score is a computational prediction only and is not backed by trial data. Mechanistic similarity between the original and new indications has not yet been assessed.

Other predictions from the model, such as migraine with brainstem aura, are likely inherited from the general migraine node. They are not pursued in this report.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Review (small case series) | Headache | Ten migraine patients in a neurology practice were given terazosin or doxazosin. Nearly all had fewer or milder migraines, but 5 stopped the drug because of side effects. No serious adverse reactions were reported. |

This is a single, very small, uncontrolled report. It is hypothesis-generating only.

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN05014P | CARDURA TABLET 2 mg | TABLET | Valid |

<!-- licenses:end -->

Manufacturer: Pfizer Manufacturing Deutschland GmbH. This is the only valid single-ingredient registration.

## Safety Considerations

**Contraindications / cautions from the drug–disease knowledge graph** (these come from the knowledge graph, not from the package insert): multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, hypotensive disorder, liver failure, liver disease, gallbladder disease, pyloric stenosis, intestinal obstruction, priapism, and intraoperative floppy iris syndrome.

Of particular relevance to a migraine population:
- Orthostatic and general hypotension are a concern, since blood pressure lowering is the main pharmacological effect.
- In the one small case series, 5 of 10 patients stopped treatment because of side effects.

**Drug Interactions**: The interaction query found 100 interacting drugs. Most of those shown are Moderate-level:
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, triamcinolone
- SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
- Central nervous system (CNS) agents: morphine, opium, bupropion, dronabinol, nabilone
- Clarithromycin

Interactions with calcitriol, clotrimazole and cimetidine are of unknown severity.

The package insert warnings and contraindications for the Singapore-registered product have not been reviewed. Please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests mainly on a computational score and a single small, uncontrolled 1997 case series. There are no registered trials, and the mechanistic rationale is indirect. Doxazosin is already marketed in Singapore, which lowers access barriers, but the evidence is not yet sufficient to move forward. The migraine hypothesis may be kept as a research question.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- A systematic literature search for alpha-1 blockers (e.g., prazosin, terazosin) in migraine prophylaxis, and a check of international trial registries
- Assessment of tolerability, especially hypotension, in migraine patients
- A controlled study (for example, a small randomised pilot) if the literature review supports the hypothesis

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cardura (doxazosin) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5e1f5e49-2da1-43ab-9795-228a8bcc5a82) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

