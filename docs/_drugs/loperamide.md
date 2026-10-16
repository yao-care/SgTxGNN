---
layout: default
title: Loperamide
parent: Low Evidence (L5)
nav_order: 612
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Loperamide: predicted new indication Acute contagious conjunctivitis (evidence level L5). Approved use: Diarrheal disease, dysentery"
monitor_inn: "Loperamide"
predicted_indications: ["acute contagious conjunctivitis", "amebic dysentery", "conjunctivitis", "gastroduodenitis", "pseudomembranous conjunctivitis", "chronic follicular conjunctivitis", "conjunctival folliculosis", "serous conjunctivitis except viral", "parasitic conjunctivitis", "Angelucci syndrome"]
---

# Loperamide
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

# Loperamide: From Diarrheal Disease to Acute Contagious Conjunctivitis

## One-Sentence Summary

Loperamide is an antimotility drug originally used to treat diarrheal disease and dysentery symptoms.
The TxGNN model predicts it may be effective for **acute contagious conjunctivitis**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The high score appears to be a model artifact rather than biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diarrheal disease, dysentery (the Singapore registrations list no approved indication text) |
| Predicted New Indication | Acute contagious conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Loperamide is generally known as a peripheral mu-opioid receptor agonist that acts on gut myenteric neurons to reduce motility.

This mechanism does not plausibly extend to acute infectious conjunctivitis. That condition is driven by bacterial or viral pathogens, and an antimotility agent has no known antimicrobial or anti-inflammatory action on the ocular surface. The high score is most likely a graph-propagation artifact, caused by the diarrhea and infection neighbourhood in the knowledge graph.

The same pattern applies to the other top-ranked predictions. Six of the ten are conjunctivitis variants (conjunctivitis, pseudomembranous, chronic follicular, folliculosis, serous, and parasitic), plus Angelucci syndrome, an old term for allergic conjunctivitis with autonomic features. Several share identical scores, which is consistent with an ontology-driven artifact rather than independent evidence.

Two other top-ranked predictions point toward harm rather than benefit:
- **Amebic dysentery (score 99.95%)**: Loperamide does not treat the *Entamoeba histolytica* infection. A 2007 case report describes fulminant amoebic colitis following heavy loperamide use, and antimotility agents have been linked to toxic megacolon in infectious gastroenteritis.
- **Gastroduodenitis (score 99.77%)**: A 2026 case report describes loperamide-induced respiratory depression in severe gastrointestinal inflammation, likely due to increased systemic absorption through a compromised mucosa.

## Clinical Trial Evidence

Currently no related clinical trials registered for acute contagious conjunctivitis, or for any of the other top ten predicted indications.

## Literature Evidence

Currently no related literature available for acute contagious conjunctivitis.

For other predicted indications, the following publications were found. They bear mainly on safety:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Review | Am J Med | Nonfluid therapy of acute diarrhea; nonspecific agents can reduce diarrhea and other symptoms of enteric infection (amebic dysentery prediction) |
| [17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/) | 2007 | Case report | J Travel Med | Fulminant amoebic colitis and toxic megacolon, possibly influenced by heavy loperamide use (amebic dysentery prediction) |
| [41924411](https://pubmed.ncbi.nlm.nih.gov/41924411/) | 2026 | Case report | Cureus | Loperamide-induced respiratory depression in severe chemotherapy-related GI inflammation (gastroduodenitis prediction) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN06212P | IMODIUM CAPSULE 2 mg | Capsule | Not listed |
| SIN05587P | VACONTIL CAPSULE 2 mg | Capsule | Not listed |
| SIN05595P | LOPERAX CAPSULE 2 mg | Capsule | Not listed |
| SIN06525P | LORPA SYRUP 1mg/5ml | Syrup | Not listed |
| SIN07107P | DIATROL CAPSULE 2 mg | Capsule | Not listed |

There are 10 valid single-ingredient registrations in total (9 capsule and syrup products beyond those above include ABYDIUM, COLODIUM, LORAMIDE, ELDOPER, and DIATROL SYRUP). All are oral forms; no ophthalmic formulation is registered.

## Safety Considerations

- **Contraindication-type signals (knowledge graph, not label text)**: liver disease, gallbladder disease, paralytic ileus, intestinal obstruction, familial visceral myopathy, dysentery, diarrheal disease, infectious diarrheal disease, intestinal infectious disease.
- **Drug Interactions**: 100 interactions were identified. Examples rated Major include abiraterone, ranitidine, fosamprenavir, and gemfibrozil. Examples rated Moderate include codeine, dihydrocodeine, tramadol, chlorpheniramine, cetirizine, salbutamol, and ethanol (additive CNS or opioid effects are a likely concern for several of these).
- **Case-report safety signals**: Toxic megacolon risk in invasive amebic colitis, and respiratory depression with increased systemic absorption in severe GI inflammation.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, literature, or plausible mechanistic support. The score most likely reflects knowledge-graph propagation. The available evidence for related predictions (amebic dysentery, gastroduodenitis) indicates safety risks rather than therapeutic opportunity.

**To proceed, the following is needed:**
- Mechanism of action data to assess any biological link
- Package insert warnings and contraindications from the HSA
- Any preclinical or clinical evidence in ocular conditions (none currently exists)
- Evaluation of whether an ophthalmic route would even be feasible, as only oral forms are registered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

