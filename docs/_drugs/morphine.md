---
layout: default
title: Morphine
parent: Medium Evidence (L3-L4)
nav_order: 689
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Morphine: predicted new indication Myofascial pain syndrome (evidence level L4). Approved use: Diarrhoeal disease"
monitor_inn: "Morphine"
predicted_indications: ["myofascial pain syndrome", "manic bipolar affective disorder", "Tourette syndrome", "restless legs syndrome", "attention deficit hyperactivity disorder, inattentive type", "migraine disorder", "trichotillomania", "methemoglobinemia", "migraine with brainstem aura", "specific developmental disorder"]
---

# Morphine
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

# Morphine: From Diarrhoeal Disease to Myofascial Pain Syndrome

## One-Sentence Summary

Morphine is an opioid analgesic that the knowledge graph links to diarrhoeal disease as its original indication.
The TxGNN model predicts it may be effective for **myofascial pain syndrome**,
but there are **0 clinical trials** and only **indirect literature** (10 publications, mostly related pain conditions) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diarrhoeal disease (per the knowledge graph; the Singapore licence records contain no indication text) |
| Predicted New Indication | Myofascial pain syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, morphine is a mu-opioid receptor agonist with well-established analgesic activity. Myofascial pain has a nociceptive component, so a plausible mechanistic link exists.

However, the link is weak in practice. Opioids are not recommended as standard treatment for myofascial pain. The retrieved literature is mostly indirect: opioid use in related chronic pain conditions, a stretching-exercise cohort in "legacy pain" patients, and a randomized trial of morphine as an adjunct in surgical myofascial infiltration (not a trial in myofascial pain syndrome itself).

The original indication (diarrhoeal disease) is pharmacologically unrelated to myofascial pain, so the prediction does not rest on indication similarity.

**Other predictions ranked by the model**

Some other predictions have more supporting evidence than the top-ranked one:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 4 | **Restless legs syndrome** | 99.47% | L3 | Opioids are recognised as an option for refractory RLS; supported by a national registry with up to 5-year follow-up and intrathecal morphine reports. Recommendation: Research Question |
| 2 | Manic bipolar affective disorder | 99.64% | L5 | Only animal-model and conceptual links; doubtful |
| 3 | Tourette syndrome | 99.48% | L5 | Reviews and preclinical work only |
| 6 | Migraine disorder | 99.32% | L4 | Guidelines generally discourage opioids; potential for harm |
| 5, 7–10 | ADHD (inattentive), trichotillomania, methemoglobinaemia, migraine with brainstem aura, specific developmental disorder | 99.06–99.34% | L5 | No meaningful supporting evidence |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for myofascial pain syndrome.

(For reference, the only registered trial among the ten predictions relates to restless legs syndrome: [NCT01476124](https://clinicaltrials.gov/study/NCT01476124), a Phase 1, completed, 18-participant crossover study of the pharmacokinetics and tolerability of morphine with gabapentin enacarbil in healthy volunteers. It does not assess efficacy.)

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41664327](https://pubmed.ncbi.nlm.nih.gov/41664327/) | 2026 | RCT | Asian Spine J | Dexmedetomidine plus morphine vs plain ropivacaine for myofascial infiltration in spinal fusion surgery (adjunct use, not myofascial pain syndrome) |
| [35066974](https://pubmed.ncbi.nlm.nih.gov/35066974/) | 2022 | Cohort | Pain Pract | Structured stretching programme for myofascial pain and opioid use in "legacy pain" patients |
| [39793344](https://pubmed.ncbi.nlm.nih.gov/39793344/) | 2025 | Clinical study | Eur J Obstet Gynecol Reprod Biol | Pudendal nerve block for perioperative pain after botulinum toxin injection for myofascial pelvic pain; not morphine-specific |
| [21419546](https://pubmed.ncbi.nlm.nih.gov/21419546/) | 2011 | Review | J Oral Maxillofac Surg | Long-term opioid use in temporomandibular joint dysfunction can be neither supported nor refuted by current evidence |
| [16967674](https://pubmed.ncbi.nlm.nih.gov/16967674/) | 2006 | Review | J Calif Dent Assoc | Medications, infusions and injections for differential diagnosis of orofacial pain |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN05508P | MST CONTINUS TABLET 30 mg | Tablet, film coated | Not stated in the data |
| SIN05506P | MST CONTINUS TABLET 10 mg | Tablet, film coated | Not stated in the data |
| SIN00757P | DBL MORPHINE SULFATE INJECTION 10 mg/ml | Injection | Not stated in the data |
| SIN16891P | MORPHINE SULFATE KALCEKS SOLUTION FOR INJECTION 10MG/ML | Injection, solution | Not stated in the data |
| SIN13598P | Morphine-hameln 10 mg/ml Injection | Injection, solution | Not stated in the data |

Both oral (modified-release tablet) and injectable forms are available locally. All 5 registrations are valid single-ingredient products.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (not label text) include: hypertension, orthostatic hypotension, long QT syndrome/torsades de pointes, liver failure and liver disease, kidney disease, COPD, epilepsy, pancreatitis, gallbladder disease, hypothyroidism, psychotic and other mental disorders, anxiety disorders, gastric ulcer, and potassium deficiency.

**Drug Interactions** (100 interactions found; examples):
- **Major:** fentanyl, codeine, dihydrocodeine, tramadol, butalbital, dichloralphenazone, alprazolam, ethanol (additive central nervous system and respiratory depression is the main concern)
- **Moderate:** chlorpheniramine, cetirizine, nifedipine, hydrochlorothiazide, metformin, alfentanil, among others

For warnings and label contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (myofascial pain syndrome) has no registered trials and only indirect literature, and opioids are not a recommended standard treatment for it. Among the ten predictions, restless legs syndrome has the strongest support (L3, with registry and case-series data) and is the most reasonable candidate to take forward as a research question.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- For restless legs syndrome: a controlled morphine-specific efficacy study, plus a risk assessment covering dependence, dose escalation and sleep-disordered breathing
- For myofascial pain syndrome: direct comparative evidence against standard care, with a clear opioid-risk justification
- A safety plan addressing the major interactions with other opioids, benzodiazepines and alcohol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

