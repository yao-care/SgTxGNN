---
layout: default
title: Tacrolimus
parent: Low Evidence (L5)
nav_order: 947
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tacrolimus: predicted new indication Seborrheic dermatitis (evidence level L5). Approved use: Atopic eczema / atopic dermatitis"
monitor_inn: "Tacrolimus"
predicted_indications: ["seborrheic dermatitis", "parapsoriasis", "acute lichenoid pityriasis", "acrodermatitis chronica atrophicans", "rheumatoid arthritis", "acne keloid", "psoriasis", "neonatal dermatomyositis", "exanthem (disease)"]
---

# Tacrolimus
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

# Tacrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

Tacrolimus is a calcineurin inhibitor, originally used for atopic eczema (atopic dermatitis).
The TxGNN model predicts it may be effective for **seborrheic dermatitis**,
with **2 clinical trials** (one Phase 3, one Phase 4, both completed) and **20 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic eczema / atopic dermatitis (the Singapore licence records contain no indication text) |
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 (see note below) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* By the strict rules (at least two completed Phase 3 RCTs), seborrheic dermatitis has one completed Phase 3 trial and one completed Phase 4 trial. L1 is the level assigned in the compiled data, but it is somewhat generous. A conservative reading would put it between L2 and L1.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known information, tacrolimus is a calcineurin inhibitor. It blocks NFAT-dependent T-cell activation and the release of pro-inflammatory cytokines. Its efficacy in atopic dermatitis is well established, and the topical ointment is registered in Singapore.

Seborrheic dermatitis is a chronic, relapsing inflammatory skin disease of the face and scalp. Its inflammation is partly driven by immune responses to *Malassezia* yeast. Atopic and seborrheic dermatitis share this inflammatory, T-cell-related component, so topical calcineurin inhibition is a plausible treatment. Topical tacrolimus is also steroid-sparing, which matters for long-term facial use.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Tacrolimus ointment (Protopic) as maintenance treatment of severe facial seborrheic dermatitis in adults, aiming to reduce relapses and steroid use |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Proactive once- or twice-weekly 0.1% tacrolimus ointment to keep adult facial seborrheic dermatitis in remission and reduce flares |

Results of these trials were not included in the compiled data.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Clinical study | Annals of Dermatology | Maintenance therapy of facial seborrheic dermatitis with 0.1% tacrolimus ointment |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic review | American Journal of Clinical Dermatology | Topical treatments for facial seborrheic dermatitis (antifungals, keratolytics, corticosteroids) |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | American Journal of Clinical Dermatology | Topical calcineurin inhibitors are a safe alternative to corticosteroids, which have limited long-term use |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | Journal of Drugs in Dermatology | Current status and therapeutic horizons of facial seborrheic dermatitis |
| [39219446](https://pubmed.ncbi.nlm.nih.gov/39219446/) | 2024 | Systematic review / network meta-analysis | Clinical & Experimental Allergy | Topical anti-inflammatory treatments for eczema (indirect evidence) |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | Clinical trial | Annals of Parasitology | Sertaconazole 2% cream vs tacrolimus 0.03% cream in 60 patients with seborrheic dermatitis |
| [31476936](https://pubmed.ncbi.nlm.nih.gov/31476936/) | 2019 | Review | Journal of Cutaneous Medicine and Surgery | Off-label use of topical calcineurin inhibitors in dermatologic disorders |
| [17685874](https://pubmed.ncbi.nlm.nih.gov/17685874/) | 2007 | Review | Expert Opinion on Investigational Drugs | New roles for topical tacrolimus beyond atopic dermatitis |
| [11770914](https://pubmed.ncbi.nlm.nih.gov/11770914/) | 2001 | Review | Seminars in Cutaneous Medicine and Surgery | Topical tacrolimus and pimecrolimus for psoriasis, seborrheic dermatitis, lichen planus and other conditions |
| [15461548](https://pubmed.ncbi.nlm.nih.gov/15461548/) | 2004 | Review | Expert Opinion on Pharmacotherapy | Tacrolimus ointment for atopic dermatitis and other inflammatory skin diseases |

## Singapore Market Information

There are 20 valid single-ingredient licences. The licence records contain no approved indication text. Five main authorisations are shown below, including the topical ointments most relevant to this prediction.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12523P | Protopic Ointment 0.03% | Ointment | Not recorded |
| SIN12524P | Protopic Ointment 0.1% | Ointment | Not recorded |
| SIN09649P | Prograf Capsules 1 mg | Capsule | Not recorded |
| SIN09639P | Prograf Concentrate for Infusion 5 mg/ml | Injection | Not recorded |
| SIN14134P | Advagraf Prolonged Release Hard Capsules 1 mg | Extended-release capsule | Not recorded |

Only the two Protopic ointments are topical. The remaining licences are oral or injectable systemic products.

## Safety Considerations

- **Contraindications flagged by the knowledge graph (not label text):** hypertension, long QT syndrome and torsades de pointes, liver failure, kidney disease, epilepsy, diabetes mellitus and hyperglycaemia, active infections (including herpes simplex and herpes zoster), lymphoma and other cancers, and progressive multifocal leukoencephalopathy. These relate mainly to systemic use.
- **Drug Interactions:** 100 interactions were identified. Major-level examples include amphotericin B, loperamide, mesalazine, omeprazole and balsalazide. Moderate-level examples include metformin, famotidine, corticosteroids (hydrocortisone, dexamethasone, budesonide) and aprepitant. These matter chiefly for systemic tacrolimus; topical exposure is minimal.
- **Long-term safety of topical use:** The cancer-risk question for topical calcineurin inhibitors has been examined in a systematic review and meta-analysis (PMID 36370744). It should be monitored.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 trial and a completed Phase 4 trial directly address tacrolimus ointment in facial seborrheic dermatitis. They are supported by a clinical maintenance study and several reviews. The drug is already marketed in Singapore as a topical ointment, and its mechanism is shared with the approved atopic dermatitis use.

**To proceed, the following is needed:**
- Published results of NCT02004860 and NCT01591070 (efficacy and relapse rates)
- Formal mechanism of action data
- The HSA package insert warnings and contraindications
- Confirmation of the approved indication wording in Singapore
- A long-term safety plan for facial use, covering infections and the cancer-risk question
- Comparison with standard care (antifungals, topical steroids)

### Other Predicted Indications (Brief)

| Indication | Score | Evidence Level | Recommendation | Comment |
|------|------|------|------|------|
| Dermatitis | 99.17% | L1 | Proceed with Guardrails | Largely overlaps the original atopic dermatitis indication, so it adds little as a new signal |
| Rheumatoid arthritis | 98.71% | L1 | Proceed with Guardrails | Many Phase 3/4 trials and meta-analyses of systemic tacrolimus. It is a systemic use, so monitor nephrotoxicity, interactions, infection and malignancy |
| Psoriasis | 98.66% | L1 | Proceed with Guardrails | Phase 3 tacrolimus cream trials exist. Best suited to facial and intertriginous disease; thick plaques respond poorly |
| Parapsoriasis | 99.24% | L4 | Research Question | Case reports only |
| Acute lichenoid pityriasis | 98.90% | L4 | Research Question | Case reports only |
| Exanthem | 98.59% | L2 | Research Question | Nonspecific label; the trials are mostly in oral lichen planus |
| Acrodermatitis chronica atrophicans | 98.73% | L5 | Hold | No evidence; immunosuppression could be counterproductive in this Borrelia-related condition |
| Acne keloid | 98.68% | L4 | Hold | The literature suggests an adverse association rather than a benefit |
| Neonatal dermatomyositis | 98.60% | L5 | Hold | No direct evidence |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

