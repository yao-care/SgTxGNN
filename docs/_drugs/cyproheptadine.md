---
layout: default
title: Cyproheptadine
parent: Medium Evidence (L3-L4)
nav_order: 288
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Cyproheptadine: predicted new indication Allergic urticaria (evidence level L4). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "Cyproheptadine"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic", "nasopharyngitis", "rosacea conjunctivitis", "headache disorder", "trigeminal autonomic cephalalgia"]
---

# Cyproheptadine
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

## Cyproheptadine: From Allergic Rhinitis and Urticaria to Allergic Urticaria
{: .text-alpha }

## One-Sentence Summary

Cyproheptadine is a first-generation antihistamine with serotonin-blocking activity, originally used for allergic and vasomotor rhinitis, the common cold, allergic conjunctivitis, urticaria and angioedema.
The TxGNN model predicts it may be effective for **allergic urticaria**, but there are **no registered clinical trials** and only **9 publications** (1961-1995), mostly older and uncontrolled.
Urticaria is already within its established uses, so this prediction is largely a restatement of existing use rather than true repurposing. The stronger new signal is in **cold urticaria**, which has several double-blind comparative studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, atopic/papillary/vernal conjunctivitis, familial dermatographia, urticaria, angioedema (the Singapore licence record contains no indication text) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold (for allergic urticaria as a new indication). See the Conclusion for cold urticaria (Proceed with Guardrails) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, cyproheptadine is a first-generation H1 antihistamine with 5-HT2 (serotonin) antagonist and anticholinergic activity. Its efficacy in allergic conditions is long established, and histamine-driven wheal and itch are the plausible mechanism in urticaria.

Allergic urticaria sits within the drug's existing indications (urticaria, angioedema, allergic dermatoses), so the model is largely rediscovering a known use. The supporting literature is dated and consists of clinical evaluations and comparisons, for example against hydroxyzine and ketotifen, rather than modern controlled trials.

The same mechanism also supports **cold urticaria**, a histamine-mediated physical urticaria, where cyproheptadine has historically been a reference treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7488341](https://pubmed.ncbi.nlm.nih.gov/7488341/) | 1995 | Double-blind crossover comparison | Asian Pac J Allergy Immunol | Cyproheptadine vs ketotifen in 6 Thai children with cold urticaria |
| [812662](https://pubmed.ncbi.nlm.nih.gov/812662/) | 1976 | Comparative evaluation | Curr Ther Res | Relative efficacy of cyproheptadine vs hydroxyzine for itch in allergic dermatoses |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review | Drugs | Review of acrivastine in allergic rhinitis and urticaria (indirect evidence for cyproheptadine) |
| [1305812](https://pubmed.ncbi.nlm.nih.gov/1305812/) | 1992 | Diagnostic study | Asian Pac J Allergy Immunol | Ice cube test in children; positive tests fell after 4 weeks of cyproheptadine |
| [13685954](https://pubmed.ncbi.nlm.nih.gov/13685954/) | 1961 | Clinical study | Br Med J | Cyproheptadine in urticaria |
| [14106555](https://pubmed.ncbi.nlm.nih.gov/14106555/) | 1964 | Clinical evaluation | J Assoc Physicians India | Evaluation in allergic dermatosis |
| [14138414](https://pubmed.ncbi.nlm.nih.gov/14138414/) | 1964 | Clinical study | Arerugi | Serotonin inhibitors in childhood allergic diseases |
| [14347187](https://pubmed.ncbi.nlm.nih.gov/14347187/) | 1965 | Combination-drug study | Rev Lyon Med | Cyproheptadine plus dexamethasone in inflammatory and allergic dermatoses |
| [4382319](https://pubmed.ncbi.nlm.nih.gov/4382319/) | 1967 | Clinical study | Med Lett Drugs Ther | Cyproheptadine for allergic and pruritic dermatoses |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN06637P | PILIAN TABLET 4 mg (Yung Shin Pharmaceutical) | Tablet (oral) | Indication text not recorded in the licence data |

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** hypertension, peptic ulcer disease, benign prostatic hyperplasia, ocular hypertension, angle-closure glaucoma, hyperthyroidism/Graves disease/thyrotoxicosis, and bladder neck obstruction.
- **Drug Interactions:** 100 interactions were identified.
  - **Major:** potassium citrate and potassium chloride.
  - **Moderate (selected):** anticholinergics (atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, trospium), opioids (morphine, opium, loperamide), cannabinoids (dronabinol, nabilone), metoclopramide, fenfluramine and eluxadoline.
- **Practical cautions** noted in the evidence: sedation, anticholinergic effects, and extra care in children and the elderly.

The package insert warnings and contraindications were not available for this report. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold** (for allergic urticaria as a new indication)

**Rationale:**
Allergic urticaria is already an existing use of cyproheptadine, and the supporting evidence is old, mostly uncontrolled, and has no registered trials (L4). It offers little new value as a repurposing target.

**Other predicted indications from the same analysis:**
- **Cold urticaria (score 99.76%, L3, Proceed with Guardrails):** the strongest candidate. Several small double-blind comparative studies exist (e.g., PMIDs 334082, 6480953, 2901993) against chlorpheniramine, hydroxyzine, doxepin and acrivastine. Second-generation antihistamines are now preferred first-line, so cyproheptadine would play a niche or second-line role, with guardrails for sedation, anticholinergic effects, and paediatric and elderly use.
- **Headache disorder / migraine prophylaxis (L4) and trigeminal autonomic cephalalgia (L3):** Research Question. A 2024 preliminary study supports use in paroxysmal hemicrania (PMID 39434953), but it is small and uncontrolled.
- **Nasal cavity disease, acute laryngopharyngitis, recalcitrant atopic dermatitis, atopic IgE responsiveness, nasopharyngitis and rosacea conjunctivitis (L5):** Hold. These are model predictions only, with no supporting evidence, and several overlap with existing indications.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- For cold urticaria, a review of current guideline positioning against second-generation antihistamines, and ideally a prospective controlled study
- For migraine and paroxysmal hemicrania, a prospective controlled study, plus a review of the serotonergic interaction with SSRIs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

