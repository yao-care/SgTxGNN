---
layout: default
title: Dexlansoprazole
parent: Low Evidence (L5)
nav_order: 322
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dexlansoprazole: predicted new indication Active peptic ulcer disease (evidence level L5). Approved use: Peptic ulcer disease, gastroesophageal reflux disease, esophagitis…"
monitor_inn: "Dexlansoprazole"
predicted_indications: ["gastroduodenitis", "duodenal obstruction", "achlorhydria", "leather-bottle stomach"]
---

# Dexlansoprazole
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

# Dexlansoprazole: From Peptic Ulcer Disease / GERD to Active Peptic Ulcer Disease

## One-Sentence Summary

Dexlansoprazole is a proton pump inhibitor (PPI) originally used for peptic ulcer disease, gastroesophageal reflux disease (GERD) and esophagitis.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, although this is largely an on-label, mechanism-consistent use rather than true repurposing.
Currently, **2 completed Phase 3 trials** and **3 publications** are listed for this indication. These trials were run in erosive esophagitis, so they support it only indirectly.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, gastroesophageal reflux disease, esophagitis, peptic esophagitis (the Singapore licence records contain no approved indication text) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L1 (see note below) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

*Note: The L1 level reflects two large, completed Phase 3 RCTs. Both studied erosive esophagitis, not ulcer healing, so the support for ulcer endpoints is indirect.*

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established class knowledge, dexlansoprazole is a PPI. It irreversibly inhibits the gastric H+/K+ ATPase (the "proton pump") and suppresses acid secretion. Acid suppression is the core mechanism for healing peptic ulcers.

Peptic ulcer disease is already among the drug's original indications in the knowledge graph. The prediction is therefore consistent with the drug's known pharmacology and with the PPI class. It reflects the closeness of related acid-driven diseases in the knowledge graph, rather than a new therapeutic area.

Other predictions for this drug follow the same pattern:
- **Gastric ulcer** and **duodenal ulcer** are supported indirectly by the same Phase 3 program (L1, Proceed with Guardrails).
- **Gastrojejunal ulcer** (marginal ulcer after gastric bypass) is a research question. The only trial was withdrawn with no participants.
- **Achlorhydria** is a probable false positive, because an acid suppressant has no rationale in a condition with no acid.
- **Peptic ulcer perforation, gastroduodenitis, duodenal obstruction, duodenogastric reflux and leather-bottle stomach** have no clinical evidence. They should stay on Hold.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00251719](https://clinicaltrials.gov/study/NCT00251719) | Phase 3 | Completed | 2054 | Dexlansoprazole MR 60 mg and 90 mg vs lansoprazole 30 mg for 8 weeks in healing erosive esophagitis (indirect support for ulcer healing) |
| [NCT00251693](https://clinicaltrials.gov/study/NCT00251693) | Phase 3 | Completed | 2038 | Companion trial with the same design in erosive esophagitis healing (indirect support) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic review / network meta-analysis | Am J Gastroenterol | Compares P-CAB and PPI efficacy and safety for healing grade C/D esophagitis |
| [18821474](https://pubmed.ncbi.nlm.nih.gov/18821474/) | 2008 | Review | Curr Opin Investig Drugs | Development of dexlansoprazole, a modified-release enantiomer of lansoprazole, for reflux esophagitis |
| [36150104](https://pubmed.ncbi.nlm.nih.gov/36150104/) | 2022 | Preclinical / mechanistic | J Chin Med Assoc | PPIs suppress vacuolar-type ATPase and induce endoplasmic reticulum stress; examines the mechanism behind a reported gastric cancer risk with long-term use |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14486P | DEXILANT DELAYED RELEASE CAPSULE 60mg | Capsule, delayed release | Not stated in the registration record |
| SIN14485P | DEXILANT DELAYED RELEASE CAPSULE 30mg | Capsule, delayed release | Not stated in the registration record |

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** liver disease, gallbladder disease, osteoporosis, postmenopausal osteoporosis and bone fracture. These come from knowledge-graph relationships and should be checked against the package insert.
- **Drug Interactions:** 100 interactions were found in the DDI query. Examples from the listed records:
  - **Major:** acalabrutinib, atazanavir
  - **Moderate:** fosamprenavir, foscarnet, fostamatinib, furosemide, gefitinib, hydrochlorothiazide, amphotericin B, amikacin, amphetamine, ampicillin, bosutinib, bumetanide
  - **Minor:** acetylsalicylic acid, axitinib, brivaracetam, cyanocobalamin
- Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dexlansoprazole is an established PPI already marketed in Singapore. Acid suppression is a well-understood mechanism for ulcer healing, and two large completed Phase 3 trials show efficacy and safety in the related condition of erosive esophagitis. Direct ulcer-healing data are missing, so the evidence for this indication is indirect.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications (the approved indication text is also missing from the registration records)
- Detailed mechanism of action data
- Direct ulcer-healing evidence, for example results from the recruiting Phase 4 trial [NCT07344506](https://clinicaltrials.gov/study/NCT07344506) (H. pylori eradication, n=942)
- Review of the knowledge-graph contraindications (liver disease, bone fracture or osteoporosis) and of the major interactions (acalabrutinib, atazanavir)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

