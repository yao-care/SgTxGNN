---
layout: default
title: Apremilast
parent: Low Evidence (L5)
nav_order: 104
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Apremilast: predicted new indication Migraine disorder (evidence level L5). Approved use: Psoriatic arthritis"
monitor_inn: "Apremilast"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "pulmonary hypertension", "migraine with or without aura, susceptibility to", "kyphoscoliotic heart disease", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Apremilast
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

## Apremilast: From Psoriatic Arthritis to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Apremilast is an oral PDE4 inhibitor, originally used to treat psoriatic arthritis.
The TxGNN model predicts it may be effective for **migraine disorder**,
but currently there are **0 clinical trials** and **0 publications** supporting this specific direction; the prediction rests on the model score alone.

Note: the highest-ranked prediction with actual supporting studies is rheumatoid arthritis (3 clinical trials, 1 Phase 2 RCT). It is discussed below as a reference point.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriatic arthritis (the Singapore licence records contain no approved indication text) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 98.66% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known information, apremilast is a small-molecule inhibitor of phosphodiesterase 4 (PDE4). By blocking PDE4 it raises intracellular cAMP, which dampens pro-inflammatory mediators such as TNF-alpha, IL-17 and IL-23. Its efficacy in psoriatic arthritis is established.

A neuroinflammatory or cAMP-mediated link to migraine is conceivable, since PDE4 is highly expressed in the brain and has been reviewed as a target in neurological disorders. However, no trials or publications specific to apremilast in migraine were retrieved. Headache is also a known adverse event of apremilast, which argues for caution. The prediction should be treated as a hypothesis only.

**Other predictions for context:**
- **Rheumatoid arthritis (score 98.09%, L2):** biologically plausible and the best-supported alternative. A Phase 2 RCT exists (PMID 25779750), but no Phase 3 programme or approval followed, suggesting modest efficacy compared with existing RA therapies.
- **Migraine with brainstem aura, pulmonary hypertension, and migraine susceptibility:** no supportive evidence (L5).
- **Kyphoscoliotic heart disease, brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome, atrophoderma vermiculata, ulerythema ophryogenesis:** no plausible mechanistic link and no evidence (L5). These scores likely reflect graph-based artefacts.

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine disorder.

For reference, trials registered for the best-supported alternative prediction, rheumatoid arthritis:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01285310](https://clinicaltrials.gov/study/NCT01285310) | Phase 2 | Terminated | 237 | Randomised, double-blind, placebo-controlled study of two apremilast doses in active RA with inadequate response to methotrexate; reason for termination should be checked |
| [NCT01250548](https://clinicaltrials.gov/study/NCT01250548) | Phase 2 | Completed | 34 | Small controlled trial comparing apremilast with placebo in active RA; hypothesis-generating only |
| [NCT01204138](https://clinicaltrials.gov/study/NCT01204138) | Phase 2 | Withdrawn | 0 | Cross-over study of apremilast with TNF inhibition in active RA; no participants enrolled, so no evidence |

## Literature Evidence

Currently no related literature available for migraine disorder.

For reference, key publications for rheumatoid arthritis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25779750](https://pubmed.ncbi.nlm.nih.gov/25779750/) | 2015 | RCT | Arthritis & Rheumatology | Phase 2 placebo-controlled study of apremilast in active RA with inadequate response to methotrexate |
| [20525198](https://pubmed.ncbi.nlm.nih.gov/20525198/) | 2010 | Preclinical | Arthritis Research & Therapy | Apremilast inhibited spontaneous TNF-alpha production from human RA synovial cells and ameliorated experimental arthritis |
| [30072998](https://pubmed.ncbi.nlm.nih.gov/30072998/) | 2018 | Preclinical | Frontiers in Immunology | Apremilast ameliorated arthritis in a mouse model by suppressing Th1/Th17 cells and enhancing regulatory T cells |
| [26097790](https://pubmed.ncbi.nlm.nih.gov/26097790/) | 2014 | Pharmacokinetic study | Clin Pharmacol Drug Dev | Assessed the pharmacokinetic effect of co-administering apremilast and methotrexate in RA and PsA |
| [24797159](https://pubmed.ncbi.nlm.nih.gov/24797159/) | 2014 | Review | Drugs | Overview of apremilast's first global approval for psoriatic arthritis and development in other conditions |
| [32673703](https://pubmed.ncbi.nlm.nih.gov/32673703/) | 2020 | Review | Pharmacological Research | PDE4 as a therapeutic target in neurological disorders (indirectly relevant to the migraine hypothesis) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15203P | OTEZLA TABLET 30 MG | Tablet, film coated | Not stated in the licence record |
| SIN15202P | OTEZLA TABLET STARTER PACK | Tablet, film coated | Not stated in the licence record |

## Safety Considerations

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for safety information.

**Drug Interactions:** 75 interactions were identified. Examples of those graded **Major**:
- Lumacaftor
- Fosphenytoin
- Apalutamide

Several of these are strong enzyme inducers, which may reduce apremilast exposure. Moderate interactions include dexamethasone, bosentan, bexarotene, deferasirox, griseofulvin and others. One minor interaction (armodafinil) was also listed. Only the first 20 of the 75 interactions were available for review.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction has a high model score (98.66%) but no clinical trials or literature, so it remains at L5 (model prediction only). Headache is a known adverse event of apremilast, which weighs against a benefit. Among all predictions, only rheumatoid arthritis has a Phase 2 RCT, and it did not advance to Phase 3.

**To proceed, the following is needed:**
- Mechanism of action data and a review of PDE4/cAMP involvement in migraine pathophysiology
- Preclinical or exploratory clinical evidence of apremilast in migraine, with an analysis of headache as an adverse event
- Package insert warnings and contraindications from HSA, and the approved indication text for the Singapore licences
- Clarification of why the Phase 2 RA trial (NCT01285310) was terminated, if RA is pursued instead
- Review of the full DDI list, particularly with enzyme inducers
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

