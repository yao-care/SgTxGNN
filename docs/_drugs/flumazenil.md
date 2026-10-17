---
layout: default
title: Flumazenil
parent: Medium Evidence (L3-L4)
nav_order: 438
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Flumazenil: predicted new indication Migraine disorder (evidence level L4). Approved use: Not stated in the Singapore licence records"
monitor_inn: "Flumazenil"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "kyphoscoliotic heart disease", "pulmonary hypertension", "osteoarthritis susceptibility", "migraine with or without aura, susceptibility to", "ulerythema ophryogenesis", "restless legs syndrome", "pyelonephritis"]
---

# Flumazenil
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Flumazenil: From Benzodiazepine Reversal to Migraine Disorder

## One-Sentence Summary

Flumazenil is a GABA-A receptor benzodiazepine-site antagonist, marketed in Singapore as an injectable. The TxGNN model predicts it may be effective for **migraine disorder**. Support is weak: there are **no registered clinical trials** and **8 publications**, mostly case reports and preclinical studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records (all six licences have empty indication text) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 97.24% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Flumazenil is known to be a competitive antagonist at the benzodiazepine binding site of the GABA-A receptor. Its established clinical use is reversing benzodiazepine sedation. This is general pharmacology and is not drawn from the compiled data.

The link to migraine rests on the idea that GABAergic signalling contributes to migraine pathophysiology:

- A 2024 rat study found that extrasynaptic δ-subunit GABA-A receptors mediate resistance to a migraine-like phenotype.
- A 2004 animal study showed that midazolam's modulation of trigeminovascular pain transmission was antagonised by flumazenil.
- Several case reports and a case series describe stupor or coma, sometimes in migraine, that responded to flumazenil. This suggests endogenous benzodiazepine-like compounds (endozepines) may play a role in some patients.

Flumazenil is an antagonist, so the direction of any therapeutic effect in migraine is unclear. The very high TxGNN score is a computational prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9601618](https://pubmed.ncbi.nlm.nih.gov/9601618/) | 1998 | Case report | Cephalalgia | Flumazenil-responsive stupor |
| [9350386](https://pubmed.ncbi.nlm.nih.gov/9350386/) | 1997 | Case series | Cephalalgia | Two children with recurrent stupor and raised endozepine-4 levels; flumazenil given in one |
| [10637870](https://pubmed.ncbi.nlm.nih.gov/10637870/) | 1999 | Case report | Revista de Neurologia | Coma associated with migraine (basilar-type) |
| [25319965](https://pubmed.ncbi.nlm.nih.gov/25319965/) | 2015 | Case report | Cephalalgia | Steroid-responsive cerebral vasogenic edema in status migrainosus and persistent aura; no flumazenil benefit shown |
| [38724972](https://pubmed.ncbi.nlm.nih.gov/38724972/) | 2024 | Preclinical (animal) | J Headache Pain | Extrasynaptic δGABA-A receptors mediate resistance to migraine-like phenotype in rats |
| [15193528](https://pubmed.ncbi.nlm.nih.gov/15193528/) | 2004 | Preclinical (animal) | Brain Research | Midazolam's GABA-A modulation of trigeminovascular nociception was antagonised by flumazenil |
| [26675662](https://pubmed.ncbi.nlm.nih.gov/26675662/) | 2014 | Preclinical/mechanistic | BBA Clinical | Altered GABA-A receptor function in SCA6 and familial hemiplegic migraine type 1 |
| [28777735](https://pubmed.ncbi.nlm.nih.gov/28777735/) | 2017 | Preclinical (indirect) | J Basic Clin Physiol Pharmacol | GABAergic involvement in the anticonvulsant effect of a plant extract; only indirectly relevant |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15210P | Flumazenil-Baxter Solution for Injection 1 mg/10 ml | Injection, solution | Not stated in the compiled data |
| SIN01509P | Anexate Injection 0.5 mg/5 ml | Injection | Not stated in the compiled data |
| SIN17223P | GP-Flumazenil Solution for I.V. Injection 0.5 mg/5 ml | Injection, solution | Not stated in the compiled data |
| SIN15750P | Flumazenil-Hameln Injection 0.1 mg/ml | Solution, sterile | Not stated in the compiled data |
| SIN15610P | Flumazenil Kabi Solution for Injection or Infusion 0.1 mg/ml | Injection, solution | Not stated in the compiled data |

A sixth licence, SIN15209P (Flumazenil-Baxter 0.5 mg/5 ml), is also valid. All six are single-ingredient injectable products.

## Safety Considerations

- **Contraindications flagged by the knowledge graph** (disease associations from the TxGNN knowledge graph, not package-insert text): epilepsy, liver disease, gallbladder disease, heart disease, cardiovascular disease, anxiety disorder and anxiety.
- **Drug interactions**: 58 interactions were identified. Those with a stated severity include:
  - **Major**: amitriptyline, clomipramine, desipramine, doxepin (including topical), maprotiline.
  - **Moderate**: alprazolam, chlordiazepoxide, clobazam, clonazepam, clorazepic acid, diazepam, lorazepam, midazolam.
  - **Minor**: baclofen, nalmefene.
  - Several others, including morphine, omeprazole, atropine and naloxone, are of unknown severity.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score, case reports and animal studies, with no clinical trials. Flumazenil is an antagonist, so the direction of any benefit in migraine is unclear. The evidence level is L4.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website, to support safety screening. The knowledge-graph flags for epilepsy and cardiovascular disease need verification.
- Mechanism of action data from DrugBank.
- Clarification of whether flumazenil would be expected to help or worsen migraine, for example through further preclinical work or a small exploratory study.
- Consolidation of the overlapping migraine predictions, such as "migraine with or without aura, susceptibility to", into one research question.
- Confirmation of the approved indications on the Singapore licences, which are currently blank.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

