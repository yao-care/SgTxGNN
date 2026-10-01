---
layout: default
title: Dexlansoprazole
parent: Low Evidence (L5)
nav_order: 319
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Dexlansoprazole: From Erosive Esophagitis/GERD to Active Peptic Ulcer Disease

## One-Sentence Summary

Dexlansoprazole is a dual delayed-release proton pump inhibitor (PPI), originally used for erosive esophagitis and gastroesophageal reflux disease (GERD).
The TxGNN model predicts it may be effective for **active peptic ulcer disease**.
**18 clinical trials** and **3 publications** are linked to this prediction, but most trials test other PPIs or acid-suppressing drugs rather than dexlansoprazole in ulcer patients.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Erosive esophagitis / GERD (from the trial and literature record; the Singapore licence text is blank) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (see the caveat under Clinical Trial Evidence) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the structured record. Based on known pharmacology, dexlansoprazole irreversibly inhibits the gastric H+/K+-ATPase (the proton pump). This reduces stomach acid, and acid suppression is the established basis for healing ulcers.

Peptic ulcer disease is a class-level indication for PPIs. Dexlansoprazole's labelled uses (erosive esophagitis, GERD) are not ulcer indications, so this is an extension within the drug class rather than a completely new mechanism. Its efficacy in acid-related upper gastrointestinal disease is well established, and mechanistically it may be applicable to ulcers.

The main gap is that no trial in this pack shows dexlansoprazole healing ulcers. The high score partly reflects how close the ulcer terms sit to the drug in the knowledge graph.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04784910](https://clinicaltrials.gov/study/NCT04784910) | Phase 3 | Completed | 423 | DWP14012 vs lansoprazole 15 mg for preventing NSAID-induced peptic ulcer (non-inferiority); dexlansoprazole's role is unconfirmed |
| [NCT04840550](https://clinicaltrials.gov/study/NCT04840550) | Phase 3 | Unknown | 390 | Tegoprazan 25 mg vs lansoprazole 15 mg for preventing ulcers in long-term NSAID users |
| [NCT05448001](https://clinicaltrials.gov/study/NCT05448001) | Phase 3 | Completed | 329 | JP-1366 vs an active control in gastric ulcer; drug linkage unconfirmed |
| [NCT06284876](https://clinicaltrials.gov/study/NCT06284876) | Phase 3 | Recruiting | 416 | Ilaprazole 10 mg vs an active control for preventing NSAID-associated peptic ulcer |
| [NCT02761512](https://clinicaltrials.gov/study/NCT02761512) | Phase 3 | Completed | 306 | CJ-12420 vs lansoprazole 30 mg in gastric ulcer (non-inferiority) |
| [NCT05010954](https://clinicaltrials.gov/study/NCT05010954) | Phase 3 | Completed | 400 | LXI-15028 vs lansoprazole 30 mg in duodenal ulcer, up to 6 weeks |
| [NCT00251719](https://clinicaltrials.gov/study/NCT00251719) | Phase 3 | Completed | 2054 | Dexlansoprazole MR 60/90 mg vs lansoprazole 30 mg for healing erosive esophagitis (8 weeks) |
| [NCT00251693](https://clinicaltrials.gov/study/NCT00251693) | Phase 3 | Completed | 2038 | Replicate of the above: dexlansoprazole MR vs lansoprazole in erosive esophagitis |
| [NCT04531475](https://clinicaltrials.gov/study/NCT04531475) | Phase 2 | Completed | 90 | X842 capsules at different doses vs lansoprazole in reflux esophagitis (4 weeks) |
| [NCT07079540](https://clinicaltrials.gov/study/NCT07079540) | Phase 3 | Completed | 380 | X842 50 mg vs lansoprazole in reflux esophagitis, with population pharmacokinetics |

**Caveat:** The only dexlansoprazole-specific Phase 3 trials (NCT00251719, NCT00251693) are in erosive esophagitis, not ulcers. The ulcer trials mainly test other acid-suppressing drugs against lansoprazole, the parent compound of dexlansoprazole (a racemic mixture that contains it). They support PPI-class ulcer benefit but not dexlansoprazole itself. The evidence level of L2 therefore describes the class rather than the drug in this indication.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic review / network meta-analysis | Am J Gastroenterol | Compares potassium-competitive acid blockers with PPIs for healing severe (LA grade C/D) esophagitis |
| [18821474](https://pubmed.ncbi.nlm.nih.gov/18821474/) | 2008 | Review | Curr Opin Investig Drugs | Development of dexlansoprazole, a modified-release enantiomer of lansoprazole, for reflux esophagitis |
| [36150104](https://pubmed.ncbi.nlm.nih.gov/36150104/) | 2022 | Preclinical / mechanistic | J Chin Med Assoc | PPIs including dexlansoprazole suppress vacuolar ATPase and induce endoplasmic reticulum stress; explores the link to gastric cancer risk |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN14486P | DEXILANT DELAYED RELEASE CAPSULE 60mg | Capsule, delayed release |
| SIN14485P | DEXILANT DELAYED RELEASE CAPSULE 30mg | Capsule, delayed release |

Both products are made by Takeda and are oral only. Approved indication text is not included in the record.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Acid suppression is a well-established mechanism for ulcer healing, dexlansoprazole is already marketed in Singapore, and many Phase 3 PPI-class ulcer trials exist. However, none of them shows dexlansoprazole healing ulcers, so any use should be treated as a within-class extension and not an established benefit.

**To proceed, the following is needed:**
- The HSA package insert (warnings and contraindications), which currently blocks safety screening
- Structured mechanism-of-action data for dexlansoprazole
- Confirmation of whether dexlansoprazole is a study arm or comparator in the ulcer trials above (several titles are truncated)
- Dexlansoprazole-specific ulcer efficacy data, for example a head-to-head comparison with lansoprazole or esomeprazole in gastric or duodenal ulcer
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

