---
layout: default
title: Rifaximin
parent: Medium Evidence (L3-L4)
nav_order: 867
evidence_level: L4
indication_count: 10
---

# Rifaximin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Rifaximin: From Hepatic Encephalopathy to Oral Candidiasis

## One-Sentence Summary

Rifaximin is a poorly absorbed oral antibiotic, originally used for hepatic encephalopathy and hepatic coma.
The TxGNN model predicts it may be effective for **oral candidiasis**, but there are **0 clinical trials** and only **1 publication** for this prediction, and that publication points to a possible harm signal rather than a benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatic encephalopathy, hepatic coma (the licence record has no approved indication text) |
| Predicted New Indication | Oral candidiasis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, rifaximin is a non-absorbable, gut-targeted antibiotic. Its efficacy in hepatic encephalopathy is thought to come from reducing gut bacteria that produce toxins. Mechanistically, there is no clear reason it would apply to oral candidiasis.

The only available publication (PMID 34180023) suggests the opposite of a benefit. In patients receiving allogeneic stem cell transplants, rifaximin use favoured infections with micafungin-resistant *Candida* species. A likely explanation is that disrupting gut bacteria allows yeast to overgrow. Rifaximin has no known antifungal activity.

The high TxGNN score therefore looks like an association within the knowledge graph rather than evidence of efficacy. The same pattern appears in other top-ranked predictions: candidiasis in general (score 99.15%) is supported only by observational studies that suggest risk, not benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohort | Annals of Hematology | In allogeneic stem cell transplant recipients, rifaximin use favoured micafungin-resistant *Candida* infections. This is a harm signal, not evidence of benefit. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14761P | XIFAXAN Film-coated Tablet 550mg (Alfasigma S.p.A.) | Film-coated tablet (oral) | Not stated in the licence record |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

