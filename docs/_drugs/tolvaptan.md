---
layout: default
title: Tolvaptan
parent: Low Evidence (L5)
nav_order: 995
evidence_level: L5
indication_count: 10
---

# Tolvaptan
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

# Tolvaptan: From Its Registered Use to Polycystic Kidney Disease 3 (With or Without Polycystic Liver Disease)

## One-Sentence Summary

Tolvaptan is an oral vasopressin V2 receptor antagonist marketed in Singapore under three registrations. The registration records do not state its approved indication.
The TxGNN model predicts it may be effective for **polycystic kidney disease 3 with or without polycystic liver disease**.
This direction has **0 registered clinical trials** in the Evidence Pack but **20 publications**, including two pivotal RCTs in the closely related ADPKD (autosomal dominant polycystic kidney disease).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (based on ADPKD RCTs; not specific to the PKD3 subtype) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

A structured mechanism-of-action entry is not available for tolvaptan in this dataset. The literature and the repurposing analysis describe it as a selective vasopressin V2 receptor antagonist. Blocking V2 lowers renal cAMP, which drives cyst fluid secretion and cyst-epithelial proliferation in ADPKD.

PKD3 (GANAB-related) belongs to the ADPKD spectrum and shares the same cystic phenotype, so the mechanism plausibly applies. The literature describes tolvaptan as the only approved therapy targeting ADPKD progression. It is supported by the landmark TEMPO 3:4 trial and a later-stage ADPKD trial.

Two limits apply. The pivotal Phase 3 trials enrolled mostly PKD1/PKD2 patients, so extending the results to the GANAB subtype is an inference. The polycystic liver component is also not an established tolvaptan target.

The other nine predicted indications are much weaker. Most have no trials or literature, and several have no plausible V2 mechanism, so they are on Hold or are research questions only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT | N Engl J Med | Landmark trial of tolvaptan in ADPKD, motivated by preclinical evidence that V2 antagonists inhibit cyst growth and slow kidney function decline |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT | N Engl J Med | Tolvaptan in later-stage ADPKD. The earlier trial showed slower kidney volume growth and eGFR decline but more aminotransferase and bilirubin elevations |
| [38091246](https://pubmed.ncbi.nlm.nih.gov/38091246/) | 2024 | Randomized trial (post hoc) | Pediatr Nephrol | Rapid-progression risk estimation in children aged 5-17 from the pediatric tolvaptan trial NCT02964273 |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Consensus statement | Nephrol Dial Transplant | ERA/ERKNet/PKD International consensus on starting and monitoring tolvaptan in ADPKD |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Guideline | J Hepatol | EASL guideline on cystic liver diseases, including polycystic liver disease |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Meta-analysis | Nefrologia | Systematic review of tolvaptan efficacy and safety in ADPKD |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Systematic review | Cochrane Database Syst Rev | Interventions for preventing ADPKD progression, including disease-modifying agents |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | ADPKD review: the most common inherited kidney disorder, causing 5-10% of kidney failure in the US and Europe |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | Polycystic kidney/liver disease; tolvaptan in ADPKD can slow renal function decline and cyst growth |
| [37089056](https://pubmed.ncbi.nlm.nih.gov/37089056/) | 2023 | Review | Korean J Intern Med | Tolvaptan preserved kidney function and reduced kidney volume growth, mainly in rapidly progressing ADPKD |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN15934P | SAMSCA TABLET 15MG | Tablet |
| SIN16607P | JINARC TABLET 15MG | Tablet |
| SIN16608P | JINARC TABLET 30MG | Tablet |

The approved indication text is not recorded for these registrations.

## Safety Considerations

- **Hepatotoxicity**: The ADPKD literature reports more aminotransferase and bilirubin elevations with tolvaptan. Liver function monitoring is a mandatory guardrail.
- **Neonatal and pediatric use**: Safety data are limited. The evidence consists of a neonatal case report and one pediatric trial in ADPKD.

Please refer to the package insert for other safety information, including warnings, contraindications and drug interactions.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two Phase 3 RCTs in ADPKD, plus guidelines and consensus statements, strongly support the V2/cAMP mechanism. However, no trial specifically addresses PKD3 (GANAB-related), and liver safety is a known concern.

**To proceed, the following is needed:**
- The HSA package insert, to establish warnings, contraindications and approved indications
- Structured mechanism-of-action data from DrugBank
- Evidence in GANAB-related PKD3 patients, or expert confirmation that extrapolation from PKD1/PKD2 trials is acceptable
- A liver function monitoring plan before and during treatment
- A decision on whether the polycystic liver component should be treated as an indication or excluded
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

