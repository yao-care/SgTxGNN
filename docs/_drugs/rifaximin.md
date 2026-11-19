---
layout: default
title: Rifaximin
parent: Low Evidence (L5)
nav_order: 867
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-20
description: "Rifaximin: predicted new indication Oral candidiasis (evidence level L5). Approved use: Hepatic encephalopathy, hepatic coma"
monitor_inn: "Rifaximin"
predicted_indications: ["oral candidiasis", "commissural lip fistula", "osteoradionecrosis of the mandible", "burning mouth syndrome", "oral leukoedema", "candidiasis"]
---

# Rifaximin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Rifaximin: From Hepatic Encephalopathy to Oral Candidiasis
{: .text-alpha }

## One-Sentence Summary

Rifaximin is a poorly absorbed oral antibiotic, originally used for hepatic encephalopathy and hepatic coma.
The TxGNN model predicts it may be effective for **oral candidiasis**, but there are **0 clinical trials** and only **1 publication** for this prediction, and that publication points to a possible harm signal rather than a benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatic encephalopathy, hepatic coma (the licence record has no approved indication text) |
| Predicted New Indication | Oral candidiasis |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for rifaximin: "Rifaximin is an antibacterial drug. […] Rifaximin is a semi-synthetic derivative of rifampin and acts by binding to the beta-subunit of bacterial DNA-dependent RNA polymerase blocking one of the steps in transcription. This results in inhibition of bacterial protein synthesis and consequently inhibits the growth of bacteria." ([DailyMed: Xifaxan (rifaximin) prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7afafa63-3236-4212-9589-045db6b01c0b), label version 2025-08-27; accessed 2026-11-19.) Based on known information, rifaximin is a non-absorbable, gut-targeted antibiotic. Its efficacy in hepatic encephalopathy is thought to come from reducing gut bacteria that produce toxins. Mechanistically, there is no clear reason it would apply to oral candidiasis.

The only available publication (PMID 34180023) suggests the opposite of a benefit. In patients receiving allogeneic stem cell transplants, rifaximin use favoured infections with micafungin-resistant *Candida* species. A likely explanation is that disrupting gut bacteria allows yeast to overgrow. Rifaximin has no known antifungal activity.

The high TxGNN score therefore comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The same pattern appears in other top-ranked predictions: candidiasis in general (score 0.9915) is supported only by observational studies that suggest risk, not benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohort | Annals of Hematology | In allogeneic stem cell transplant recipients, rifaximin use favoured micafungin-resistant *Candida* infections. This is a harm signal, not evidence of benefit. |

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN14761P | XIFAXAN Film-coated Tablet 550mg | TABLET, FILM COATED | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Knowledge-graph contraindications** (from the TxGNN knowledge graph, not from label text): *Clostridium difficile* colitis and perinatal necrotizing enterocolitis.
- **Drug interactions**: 69 interactions were identified in total. One is rated Major: live cholera vaccine (*Vibrio cholerae* CVD 103-HgR strain). The others in the data compiled for this report are rated Moderate, for example warfarin, cyclosporine, tolvaptan, cabozantinib, apalutamide, darolutamide, brigatinib, capmatinib, encorafenib, enasidenib, elagolix, eliglustat, daclatasvir, ledipasvir, alpelisib, bempedoic acid, elexacaftor, istradefylline and picosulfuric acid.
- The observational signal above also suggests that rifaximin may promote *Candida* overgrowth, which is relevant to this proposed use.

Please refer to the package insert for the full warnings and contraindications, as label text was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials, and the only study on oral candidiasis suggests rifaximin may favour *Candida* infections rather than treat them. The high model score is not backed by clinical or mechanistic evidence. The other top predictions (commissural lip fistula, osteoradionecrosis of the mandible, oral leukoedema, burning mouth syndrome, closed-angle glaucoma, a rare neurodevelopmental disorder and opiate dependence) are prediction-only with no supporting data.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Singapore regulator (HSA), since safety screening cannot proceed without them
- Mechanism of action data
- Evidence that rifaximin has a therapeutic effect on oral candidiasis, which currently appears unlikely
- Among the other predictions, HIV infection is the only one with some indirect evidence. It is worth tracking as a research question, but the evidence is marginal or negative (PMIDs 25214516 and 31583331), and the only registered trial (NCT01654939) was withdrawn with no participants enrolled.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Xifaxan (rifaximin) prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7afafa63-3236-4212-9589-045db6b01c0b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

