---
layout: default
title: Naproxen
parent: Low Evidence (L5)
nav_order: 699
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Naproxen: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Bursitis, rheumatoid arthritis, ankylosing spondylitis, tendinitis…"
monitor_inn: "Naproxen"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "hypermobility of coccyx", "inflammatory spondylopathy", "Kummell disease", "polyarticular juvenile rheumatoid arthritis"]
---

# Naproxen
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

# Naproxen: From Inflammatory and Musculoskeletal Pain Conditions to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Naproxen is a non-steroidal anti-inflammatory drug (NSAID) originally used for rheumatoid arthritis, osteoarthritis, ankylosing spondylitis, gout, tendinitis, bursitis and headache or migraine.
The TxGNN model's top-ranked prediction is **brachydactyly-syndactyly syndrome**, a rare congenital skeletal malformation, but **no clinical trials and no publications** support it, so it is a model prediction only.
Among the other predictions, **inflammatory spondylopathy** (4 clinical trials, 20 publications) and **polyarticular juvenile rheumatoid arthritis** (15 publications) have real supporting evidence, though both largely overlap with established naproxen uses.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bursitis, rheumatoid arthritis, ankylosing spondylitis, tendinitis, gout, migraine, osteoarthritis and related conditions (the Singapore licence records contain no indication text, so this list comes from the knowledge-graph indication data) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome (rank 1) |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 16 |
| Recommended Decision | Hold |

Other predictions with evidence worth noting:

| Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|
| Inflammatory spondylopathy (rank 8) | 98.58% | L1 | Proceed with Guardrails |
| Polyarticular juvenile rheumatoid arthritis (rank 10) | 98.56% | L2 | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, naproxen is a non-selective COX-1/COX-2 inhibitor. It reduces prostaglandin production and so lowers inflammation, pain and fever.

**Top-ranked prediction (brachydactyly-syndactyly syndrome):** This is a rare congenital skeletal malformation. There is no plausible link between COX inhibition and its underlying pathology. The high score likely reflects proximity to skeletal and joint disease nodes in the knowledge graph rather than a pharmacological rationale. The other top-ranked predictions (ranks 2–7, such as acromesomelic dysplasia, brachyolmia and myosclerosis) follow the same pattern: rare genetic skeletal or muscle disorders with no mechanistic support and no studies. At most, naproxen might give symptomatic pain relief in some of them (for example hypermobility of coccyx, myosclerosis, Kummell disease).

**Predictions with real evidence:**
- **Inflammatory spondylopathy (axial spondyloarthritis):** NSAIDs are first-line therapy. Ankylosing spondylitis and spondyloarthropathy are already among naproxen's listed original indications, so this is an established use rather than true repurposing.
- **Polyarticular juvenile rheumatoid arthritis:** NSAIDs including naproxen are long-standing symptomatic therapy in juvenile arthritis. It overlaps with the adult rheumatoid arthritis indication and is an established paediatric use.

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction (brachydactyly-syndactyly syndrome). The trials below relate to **inflammatory spondylopathy** (rank 8).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01208207](https://clinicaltrials.gov/study/NCT01208207) | Phase 3 | Completed | 1015 | Randomised, double-blind trial of two etoricoxib doses against an active comparator in ankylosing spondylitis; the stated aim is to compare with naproxen over 6 weeks of spinal pain (comparator role to be verified in the full record) |
| [NCT00844805](https://clinicaltrials.gov/study/NCT00844805) | Phase 3 | Completed | 158 | Infliximab plus naproxen vs placebo plus naproxen in early active axial spondyloarthritis; naproxen is background therapy, so evidence is indirect |
| [NCT00367211](https://clinicaltrials.gov/study/NCT00367211) | Phase 3 | Completed | 400 | 6-month trial of gastric ulcer incidence with PN 200 vs naproxen in patients at risk of NSAID-associated ulcers |
| [NCT04115098](https://clinicaltrials.gov/study/NCT04115098) | Phase 2 | Terminated | 42 | N-of-1 trials comparing COX-2-selective and non-selective COX inhibitors in axial spondyloarthritis |

## Literature Evidence

No publications are available for the top-ranked prediction. The publications below relate to **inflammatory spondylopathy** and **polyarticular juvenile rheumatoid arthritis**. Priority is given to randomised trials, then reviews.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15692986](https://pubmed.ncbi.nlm.nih.gov/15692986/) | 2005 | RCT | Arthritis Rheum | Two doses of meloxicam vs naproxen oral suspension in juvenile idiopathic arthritis, with 3-month and 12-month efficacy and safety |
| [6395321](https://pubmed.ncbi.nlm.nih.gov/6395321/) | 1984 | Clinical study (double-blind) | Scand J Rheumatol | Naproxen vs aspirin over 24 weeks in 80 children; both effective, with fewer discontinuations for adverse reactions on naproxen (5 vs 20) |
| [26834216](https://pubmed.ncbi.nlm.nih.gov/26834216/) | 2016 | Cochrane review | J Rheumatol | Benefits and harms of NSAIDs in axial spondyloarthritis |
| [40676732](https://pubmed.ncbi.nlm.nih.gov/40676732/) | 2025 | N-of-1 trials | Rheumatology (Oxford) | Bayesian N-of-1 trials of celecoxib, meloxicam and naproxen for individualising NSAID therapy in axial spondyloarthritis |
| [2202585](https://pubmed.ncbi.nlm.nih.gov/2202585/) | 1990 | Review | Drugs | Naproxen pharmacology and therapeutic use in rheumatic diseases and pain states |
| [22258995](https://pubmed.ncbi.nlm.nih.gov/22258995/) | 2012 | Cochrane review | Cochrane Database Syst Rev | Pain management in inflammatory arthritis with gastrointestinal or liver comorbidity |
| [15163279](https://pubmed.ncbi.nlm.nih.gov/15163279/) | 2004 | Review | Expert Opin Pharmacother | Aceclofenac reported as effective as naproxen and others in ankylosing spondylitis |
| [9435402](https://pubmed.ncbi.nlm.nih.gov/9435402/) | 1997 | Review | Rev Hosp Clin | NSAIDs are first-line in juvenile chronic arthritis; naproxen is often preferred for equivalent efficacy and lower toxicity than salicylates |
| [16582683](https://pubmed.ncbi.nlm.nih.gov/16582683/) | 2006 | Review | Curr Opin Rheumatol | NSAID cardiovascular safety and their disease-modifying role in ankylosing spondylitis |
| [1173774](https://pubmed.ncbi.nlm.nih.gov/1173774/) | 1975 | Preclinical/pharmacology | Arzneimittel-Forschung | Early chemistry and pharmacology of naproxen, with anti-inflammatory activity in rodents |

## Singapore Market Information

There are 16 valid single-ingredient registrations in Singapore; none are cancelled. The records contain no approved-indication text. Main authorisations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08430P | SODEN TABLET 275 mg | Film-coated tablet | Not listed |
| SIN16449P | PRONAXEN ORAL SUSPENSION 25 MG/ML | Suspension | Not listed |
| SIN05295P | APO-NAPROXEN TABLET 250 mg | Tablet | Not listed |
| SIN12440P | ALEVE TABLET 220 mg (OTC Pack) | Film-coated tablet | Not listed |
| SIN09953P | SUNPROX 550 TABLET 550 mg | Film-coated tablet | Not listed |

## Safety Considerations

- **Contraindications / diseases of concern (knowledge-graph data, not label text):** hypertension, liver failure and liver disease, kidney disease, congestive heart failure, coronary artery disease, myocardial infarction, stroke and cerebrovascular disorders, blood coagulation disorders, anaemia, diabetes mellitus and diabetic ketoacidosis, epilepsy, osteoporosis, gallbladder disease, obesity and substance abuse/dependence, among others.
- **Drug interactions:** 100 interactions are recorded. The sample reviewed is all of Moderate severity, including:
  - acid-suppressing drugs (famotidine, ranitidine, cimetidine, rabeprazole, dexlansoprazole)
  - corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone)
  - acetylsalicylic acid
  - metformin and chlorpropamide
  - mesalazine and balsalazide
  - aprepitant
  - potassium citrate and potassium bicarbonate
  - bowel-preparation agents (picosulfuric acid, polyethylene glycol)
- Please refer to the package insert for the official warnings, which were not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, brachydactyly-syndactyly syndrome)

**Rationale:**
- The prediction has no clinical trials, no literature and no mechanistic link to COX inhibition. The score likely reflects graph proximity rather than pharmacology.
- The two predictions with evidence, inflammatory spondylopathy (L1) and polyarticular juvenile rheumatoid arthritis (L2), merit **Proceed with Guardrails**. They are largely established uses rather than true repurposing. Guardrails are cardiovascular, gastrointestinal, renal and bleeding risk with long-term use, paediatric dosing, and the heavy interaction burden.

**To proceed, the following is needed:**
- Official package insert warnings and contraindications from the Singapore regulator (HSA)
- Mechanism-of-action data from DrugBank
- Verification in the full record that naproxen is the comparator in NCT01208207
- For the rare skeletal syndromes, any preclinical or mechanistic evidence before further consideration
- A paediatric dosing and safety monitoring plan for juvenile arthritis
- Confirmation of the approved indications on the Singapore licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

