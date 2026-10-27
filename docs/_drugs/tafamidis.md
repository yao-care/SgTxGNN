---
layout: default
title: Tafamidis
parent: Low Evidence (L5)
nav_order: 949
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tafamidis: predicted new indication Primary amyloidosis . Note: the top-ranked prediction by score is \"pr… (evidence level L5). Approved use: Amyloidosis"
monitor_inn: "Tafamidis"
predicted_indications: ["primary release disorder of platelets", "thrombocytopenic purpura", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "acquired amyloid peripheral neuropathy", "primary hyperoxaluria", "dermis disease", "biotin metabolic disease", "mixed-type autoimmune hemolytic anemia"]
---

# Tafamidis
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

## Tafamidis: From Amyloidosis to Primary Amyloidosis
{: .text-alpha }

## One-Sentence Summary

Tafamidis is a transthyretin (TTR) stabiliser, originally used to treat amyloidosis, particularly the transthyretin (ATTR) forms.
The TxGNN model predicts it may be effective for **Primary Amyloidosis** (the highest-ranked prediction with supporting evidence), supported by **20 publications** including a Phase 3 RCT, and **no registered clinical trials** in the data compiled for this report.
This is largely an on-label or near-label ATTR indication rather than true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Amyloidosis (including AH, AL and ATTRV122I amyloidosis, per the knowledge graph); the Singapore licence has no indication text on file |
| Predicted New Indication | Primary amyloidosis (best-supported prediction). Note: the top-ranked prediction by score is "primary release disorder of platelets" (89.27%), which has no supporting evidence |
| TxGNN Prediction Score | 85.00% (primary amyloidosis); the top-ranked prediction scores 89.27% |
| Evidence Level | L1 (primary amyloidosis); L2 for the secondary prediction, acquired amyloid peripheral neuropathy |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails (primary amyloidosis, ATTR subtype only); Hold for the platelet and other non-amyloid predictions |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the DrugBank record compiled for this report. However, pharmacology data show that tafamidis binds the thyroxine-binding sites of the TTR tetramer and stabilises its structure. This prevents dissociation into monomers, the rate-limiting step of amyloid fibril formation. It stabilises both wild-type and mutant TTR.

The link to the predicted indication is credible only for the ATTR subtype. The Phase 3 ATTR-ACT trial (PMID 30145929) showed that tafamidis reduced all-cause mortality and cardiovascular hospitalisations in transthyretin amyloid cardiomyopathy. **Important caveat:** "primary amyloidosis" usually refers to AL (light-chain) amyloidosis, where TTR stabilisation is not the relevant mechanism. The supporting evidence therefore applies to ATTR, not AL.

For the second-ranked evidence-backed prediction, **acquired amyloid peripheral neuropathy**, TTR stabilisation is plausible. Reviews describe tafamidis use in ATTR polyneuropathy, and it is approved in some regions for early-stage hereditary ATTR polyneuropathy. The pivotal data are in hereditary disease, so extension to acquired or wild-type disease with neuropathy is extrapolated.

The other top predictions (platelet disorders, thrombocytopenic purpura, pseudo-von Willebrand disease, Glanzmann thrombasthenia, primary hyperoxaluria, dermis disease, biotin metabolic disease, autoimmune haemolytic anaemia) have no identifiable mechanistic link to TTR stabilisation. They are graph-based predictions only, without clinical or literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered. Note that ATTR-ACT (the Phase 3 trial cited in the literature below) is not listed as a registered trial in the data compiled for this report.

## Literature Evidence

Selected publications for primary amyloidosis (the highest-priority RCT and meta-analysis first, then reviews and real-world data):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30145929](https://pubmed.ncbi.nlm.nih.gov/30145929/) | 2018 | RCT | N Engl J Med | Tafamidis in transthyretin amyloid cardiomyopathy (ATTR-ACT); it binds TTR and prevents tetramer dissociation and amyloidogenesis |
| [41282536](https://pubmed.ncbi.nlm.nih.gov/41282536/) | 2025 | Meta-analysis | Eur Heart J Open | Network meta-analysis comparing tafamidis, acoramidis, patisiran and vutrisiran in ATTR cardiac amyloidosis |
| [40889572](https://pubmed.ncbi.nlm.nih.gov/40889572/) | 2025 | Systematic review / meta-analysis | J Card Fail | Harmonised data from Phase 3 placebo-controlled trials of ATTR-specific drugs in ATTR-CM |
| [38441582](https://pubmed.ncbi.nlm.nih.gov/38441582/) | 2024 | Review | JAMA | Review of transthyretin cardiac amyloidosis, the most common amyloidosis causing cardiomyopathy |
| [39819772](https://pubmed.ncbi.nlm.nih.gov/39819772/) | 2025 | Review | Curr Opin Cardiol | New therapies for ATTR and AL cardiac amyloidosis |
| [35414852](https://pubmed.ncbi.nlm.nih.gov/35414852/) | 2022 | Review | Methodist DeBakey Cardiovasc J | Overview of current and experimental cardiac amyloidosis treatments |
| [41334760](https://pubmed.ncbi.nlm.nih.gov/41334760/) | 2025 | Cohort | J Am Heart Assoc | Tafamidis reduced death and acute heart failure hospitalisation in octogenarians with ATTR cardiac amyloidosis |
| [41317156](https://pubmed.ncbi.nlm.nih.gov/41317156/) | 2025 | Real-world cohort | Eur J Heart Fail | Real-world phenotype and survival in wild-type ATTR-CM patients treated with tafamidis |
| [42266139](https://pubmed.ncbi.nlm.nih.gov/42266139/) | 2026 | Systematic review / network meta-analysis | Eur J Neurol | Pharmacological interventions for hereditary ATTR with polyneuropathy |
| [39556242](https://pubmed.ncbi.nlm.nih.gov/39556242/) | 2025 | Open-label extension (acoramidis) | Circulation | Long-term efficacy and safety of the comparator TTR stabiliser acoramidis |

For acquired amyloid peripheral neuropathy, the evidence is review-level (for example [PMID 25604431](https://pubmed.ncbi.nlm.nih.gov/25604431/) and [PMID 26662359](https://pubmed.ncbi.nlm.nih.gov/26662359/)), plus a 2026 cohort on acquired ATTR amyloidosis ([PMID 41493356](https://pubmed.ncbi.nlm.nih.gov/41493356/)). No primary RCT of tafamidis in this population was supplied.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15894P | VYNDAMAX SOFT GELATIN CAPSULE 61MG | Capsule (oral) | Indication text not available |

## Safety Considerations

**Drug Interactions** (13 entries in the interaction data; 12 are formal interaction records, 1 is a pharmacology target record):
- **Major:** Ozanimod
- **Moderate:** Rosuvastatin, Deferasirox, Eltrombopag, Lusutrombopag, Artesunate, Axitinib, Methotrexate, Irinotecan (including the liposomal form), Belinostat, Imatinib

Several of these (for example rosuvastatin, methotrexate, imatinib and irinotecan) are substrates or inhibitors of transporters such as BCRP. This is consistent with tafamidis acting as a BCRP inhibitor, but the data compiled for this report do not state the mechanism, so it should be confirmed against the product label.

Warnings and contraindications from the package insert were not available. Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (primary amyloidosis, ATTR subtype only). **Hold** for all non-amyloid predictions.

**Rationale:**
- Tafamidis has strong Phase 3 evidence (ATTR-ACT) in transthyretin amyloid cardiomyopathy, so the evidence level for this prediction is L1. However, this is essentially an on-label or near-label ATTR use, not novel repurposing, and it does not apply to AL amyloidosis.
- The higher-scoring platelet, haematological, metabolic and dermatological predictions have no mechanistic rationale, no trials and no literature. They should not be pursued.

**To proceed, the following is needed:**
- Clarify the target population: confirm that "primary amyloidosis" is restricted to ATTR and excludes AL amyloidosis
- Obtain the Singapore package insert (approved indication, warnings, contraindications), as these are currently missing and block the safety screening
- Obtain detailed mechanism-of-action data from DrugBank
- Confirm the approved indication for VYNDAMAX against the proposed use (the indication text on file is empty)
- For acquired or wild-type ATTR neuropathy, gather direct clinical evidence beyond reviews before any extension of use
- Review the major interaction with ozanimod and the moderate interactions in the intended patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

