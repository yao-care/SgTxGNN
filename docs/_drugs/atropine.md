---
layout: default
title: Atropine
parent: Low Evidence (L5)
nav_order: 122
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Atropine: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the available Singapore licence records"
---

# Atropine
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

# Atropine: From Antimuscarinic Therapy to Migraine Disorder

## One-Sentence Summary

Atropine is a non-selective muscarinic antagonist that is marketed in Singapore as injections, an eye drop and oral tablets.
The TxGNN model predicts it may be effective for **migraine disorder**, but the prediction is supported by **0 clinical trials** and only preclinical or indirect literature.
Evidence is limited to model prediction and mechanistic hypotheses, so this should be treated as an early research question rather than a ready candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available Singapore licence records |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, atropine is a non-selective muscarinic cholinergic antagonist, and its use as an antimuscarinic is well established. Mechanistically, it may be applicable to migraine.

Cholinergic signalling in meningeal mast cells and trigeminal afferents may contribute to neurogenic inflammation and pain in migraine. Blocking muscarinic receptors could plausibly modulate this pathway.

There are important caveats. The supporting literature is mostly rodent or guinea pig work, or is unrelated (anisodamine pharmacology, adverse-event reports). A mouse study on the related predicted indication, migraine with brainstem aura, found that muscarinic activation, not blockade, inhibited cortical spreading depression, which suggests the direction of effect could be opposite to atropine's action. No human efficacy data exist for migraine.

## Clinical Trial Evidence

No clinical trials are registered for migraine disorder.

For context, the closely related predicted indication **headache disorder** (rank 8) has two trials in which atropine is only part of a comparator:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03997006](https://clinicaltrials.gov/study/NCT03997006) | Phase 4 | Completed | 60 | IV aminophylline vs IV neostigmine/atropine mixture for post-dural puncture headache; atropine's independent contribution cannot be assessed |
| [NCT04910477](https://clinicaltrials.gov/study/NCT04910477) | Phase 3 | Completed | 90 | Nebulized dexmedetomidine vs neostigmine/atropine vs saline for post-dural puncture headache after caesarean section; atropine is part of the active comparator |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Review | J Appl Toxicol | Pharmacology of anisodamine, an atropine derivative and non-specific cholinergic antagonist; not migraine-specific |
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | Preclinical | Eur J Neurosci | Meningeal mast cell-mediated cholinergic modulation of neurogenic inflammation in a rat migraine model |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | Clinical physiology study | Cephalalgia | In four patients with chronic paroxysmal hemicrania, systemic atropine reduced attack-related sweating, tearing and nasal secretion |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | Preclinical | Exp Neurol | Parasympathetic ganglion stimulation induced plasma protein extravasation in rat dura mater, relevant to the neurogenic inflammation hypothesis |
| [10193781](https://pubmed.ncbi.nlm.nih.gov/10193781/) | 1999 | Preclinical | Br J Pharmacol | Guinea pig basilar artery study of drugs linked to migraine; atropine used as a background agent |
| [8930196](https://pubmed.ncbi.nlm.nih.gov/8930196/) | 1996 | Preclinical | J Pharmacol Exp Ther | Central cholinergic system involvement in sumatriptan-induced antinociception in rodents |

Several other retrieved items (e.g. topiramate adverse events, botulinum toxin complications) do not address atropine for migraine and are omitted.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN07360P | Atropine Injection BP 600 mcg/ml | Injection | Not listed |
| SIN03441P | Atropine Sulphate Injection 0.6 mg/ml | Injection | Not listed |
| SIN15611P | Martindale Pharma Atropine Sulfate Solution for Injection 600 mcg/ml | Injection, solution | Not listed |
| SIN04140P | Alcon Atropine Sulfate Eye Drops 1% | Solution | Not listed |
| SIN05379P | Dhamotil Tablet | Tablet, film coated | Not listed |

One further licence, SIN09095P (Sun-Dianox Tablet), is also valid. All six are single-ingredient products.

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified. The ones listed below are mostly Moderate, with a few Minor:
  - Additive anticholinergic or sedative effects are likely with Moderate-level agents such as hyoscyamine, aclidinium, amitriptyline, chlorpheniramine and amantadine.
  - Opioids and CNS depressants (fentanyl, alfentanil, codeine, dihydrocodeine, tramadol, ethanol) are also flagged as Moderate.
  - Other Moderate interactions include botulinum toxin type A, acebutolol, acetylcholine and galantamine.
  - Minor interactions include acetaminophen and hydrochlorothiazide.
- **Condition-specific risks from the literature**: Atropine's mydriatic and cycloplegic effects can raise intraocular pressure, which is a concern in angle-closure settings. A case report described reversible cerebral vasoconstriction syndrome after neostigmine/atropine given for post-dural puncture headache.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction rests on a high model score plus preclinical and mechanistic literature, with no registered trials and no human efficacy data. Some findings (the cortical spreading depression study) point in the opposite direction from atropine's action.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Singapore-registered products, and approved indication text (currently absent from the licence records)
- Detailed mechanism of action data
- Evidence that muscarinic blockade, rather than activation, is beneficial in human migraine
- A route-of-administration assessment, since available forms are injectable, ophthalmic and oral and no migraine-appropriate route has been defined
- Any controlled clinical data, starting with an exploratory study of atropine alone

**Other predicted indications (for reference):** Evidence is weak across the list. Headache disorder (L2, trials only for neostigmine/atropine combinations) and trigeminal autonomic cephalalgia (L4, one 1984 clinical report on atropine for cluster headache) are the most directly related. Open-angle and primary hereditary glaucoma are likely misleading associations, since atropine raises glaucoma risk rather than treating it. Atrophoderma vermiculata, ulerythema ophryogenesis and nephrogenic syndrome of inappropriate antidiuresis rest on prediction scores alone.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

