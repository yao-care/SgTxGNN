---
layout: default
title: Ticlopidine
parent: Medium Evidence (L3-L4)
nav_order: 989
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Ticlopidine: predicted new indication Rheumatoid arthritis (evidence level L4). Approved use: Not stated in the Singapore licence records (approved indication text…"
monitor_inn: "Ticlopidine"
predicted_indications: ["rheumatoid arthritis", "female breast carcinoma", "obsolete familial combined hyperlipidemia", "homozygous familial hypercholesterolemia", "hypoalphalipoproteinemia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "HIV infectious disease", "leprosy", "multiple endocrine neoplasia"]
---

# Ticlopidine
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

## Ticlopidine: From Platelet Aggregation Inhibition to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Ticlopidine is an oral antiplatelet drug (P2Y12 / ADP receptor antagonist) that is currently marketed in Singapore as a single-ingredient film-coated tablet.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are **no registered clinical trials** and only **2 small, older clinical studies** (1985 and 1989) among the 5 publications retrieved, so the prediction rests mainly on computation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records (approved indication text is empty) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 98.91% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, ticlopidine is a thienopyridine P2Y12 (ADP receptor) antagonist that inhibits platelet aggregation and may improve blood filterability.

Platelet activation and microvascular dysfunction are thought to contribute to inflammation in rheumatoid arthritis, which gives a plausible but unproven link. Two small studies looked at this idea. A 1985 study (22 patients) reported clinical improvement and changes in serum sulphydryl levels, technetium index and ESR after 18 months of low-dose ticlopidine. A 1989 double-blind study (two groups of 20 patients on an NSAID) reported improved ESR and whole blood filterability versus placebo. These are indirect, laboratory-oriented observations in small groups, and they do not establish clinical efficacy. The high TxGNN score is a computational prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3000794](https://pubmed.ncbi.nlm.nih.gov/3000794/) | 1985 | Clinical study | Eur J Clin Pharmacol | In 22 RA patients, ticlopidine 250 mg/day for 18 months was associated with fewer involved joints, lower technetium index and ESR, and higher serum sulphydryl levels |
| [2790405](https://pubmed.ncbi.nlm.nih.gov/2790405/) | 1989 | Double-blind study | Br J Rheumatol | Versus placebo in 20 patients per group on an NSAID, ticlopidine significantly improved ESR (-28%) and whole blood filterability |
| [7893538](https://pubmed.ncbi.nlm.nih.gov/7893538/) | 1994 | Case report | No To Shinkei | Clinicopathologic conference on a 78-year-old RA patient with hemiparesis and renal failure; not evidence of efficacy |
| [19765672](https://pubmed.ncbi.nlm.nih.gov/19765672/) | 2010 | Review | Clin Gastroenterol Hepatol | Diseases and drugs that raise the risk of acute large bowel ischaemia; safety context only |
| [41689871](https://pubmed.ncbi.nlm.nih.gov/41689871/) | 2026 | Preclinical study | Drug Metab Dispos | CYP2C19 inactivation by bicuculline and its effect on clopidogrel pharmacokinetics; drug-interaction context, not related to RA efficacy |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11692P | APO-TICLOPIDINE TABLET 250 mg | Film-coated tablet | Not stated |
| SIN10054P | TIPIDIN TABLET 250 mg | Film-coated tablet | Not stated |
| SIN10367P | TIODIN TABLET 250 mg | Film-coated tablet | Not stated |

All three registrations are valid single-ingredient oral products.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from drug-disease links in the TxGNN knowledge graph, not from label text): thrombocytopenia, thrombocytopenic purpura, neutropenia, agranulocytosis, inherited aplastic anemia, Diamond-Blackfan anemia, blood coagulation disease, active peptic ulcer disease, intracerebral hemorrhage, cholestasis (including benign recurrent and familial intrahepatic forms), hyperlipidemia (including familial), leukemia, and ascorbic acid deficiency/scurvy.
- **Haematological signal from the literature**: the retrieved papers note that ticlopidine carries a higher frequency of thrombotic thrombocytopenic purpura and neutropenia than clopidogrel. This is a major safety consideration for any new long-term use.
- **Drug Interactions**: 100 interactions were identified in total. The main moderate-level interactions in the first 20 listed are acetylsalicylic acid, cimetidine, bupropion, alosetron, eluxadoline, nitisinone, fenfluramine and dexfenfluramine. Minor interactions include corticosteroids (hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, triamcinolone) and antacids (aluminium, magnesium and calcium salts). Corticosteroids and NSAIDs are commonly used in RA, so co-medication needs review.

Please also refer to the package insert for label warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for rheumatoid arthritis is a very high TxGNN score and two small, decades-old studies with indirect or laboratory outcomes. There are no registered trials. Ticlopidine's known risks of serious blood disorders (neutropenia, TTP, agranulocytosis) are a poor fit for a chronic inflammatory disease where safer options exist.

**To proceed, the following is needed:**
- The Singapore package insert (warnings, contraindications, approved indications), since the licence records have no indication text
- Mechanism of action data from DrugBank
- Confirmatory, adequately powered randomised trials with clinical RA outcomes (such as joint counts and standard disease activity scores)
- A benefit-risk assessment against current RA therapies, with a haematological monitoring plan
- Review of interactions with commonly used RA medicines (NSAIDs, corticosteroids)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

