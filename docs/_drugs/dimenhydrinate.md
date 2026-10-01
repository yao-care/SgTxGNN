---
layout: default
title: Dimenhydrinate
parent: Medium Evidence (L3-L4)
nav_order: 328
evidence_level: L4
indication_count: 10
---

# Dimenhydrinate
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

# Dimenhydrinate: From Motion Sickness to Allergic Urticaria

## One-Sentence Summary

Dimenhydrinate is an oral antihistamine-type drug that is generally known for nausea and motion sickness, although the Singapore registration records do not state an indication.
The TxGNN model predicts it may be effective for **allergic urticaria**, but **0 clinical trials** and only **1 publication** (a dog pharmacokinetic study with no efficacy data) currently relate to this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in Singapore registration records (motion sickness/nausea is the drug's general known use) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Dimenhydrinate is a salt of diphenhydramine and 8-chlorotheophylline. Diphenhydramine is a first-generation H1 antagonist. Blocking H1 receptors should reduce the wheal-and-flare reaction that histamine causes in urticaria. The high TxGNN score is consistent with this H1-antagonist class effect.

Detailed mechanism-of-action data for dimenhydrinate are not available in this record. The link to urticaria therefore rests on class-level reasoning about diphenhydramine, not on dimenhydrinate-specific data.

The only supporting paper is a pharmacokinetic study in healthy dogs. It shows diphenhydramine exposure after dimenhydrinate dosing, and it measured the effect on histamine-induced wheals. It provides no efficacy data in patients with urticaria, so the evidence is indirect.

## Clinical Trial Evidence

Currently no related clinical trials registered for allergic urticaria.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Pharmacokinetic study (dogs) | Veterinary Dermatology | Pilot study comparing diphenhydramine exposure after oral or IV diphenhydramine and oral dimenhydrinate in healthy dogs, with a pharmacodynamic look at histamine-induced wheal formation. Dimenhydrinate has been reported to give better oral absorption of diphenhydramine. |

## Singapore Market Information

Eight registrations exist. Five are listed below, and none has an approved indication text in the record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN03013P | DIMENATE TABLET 50 mg | Tablet | Not stated in record |
| SIN03403P | NOVOMIN TABLET 50 mg | Tablet | Not stated in record |
| SIN02765P | DIMENHYDRINATE TABLETS 50 mg | Tablet | Not stated in record |
| SIN03550P | NOVOMIN SYRUP 15 mg/5 ml | Syrup | Not stated in record |
| SIN02519P | APO-DIMENHYDRINATE TABLET 50 mg | Tablet | Not stated in record |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high and the H1-blockade rationale is plausible. However, the evidence is only a pharmacokinetic study in dogs, with no human efficacy data, and the Singapore package insert safety data have not yet been obtained. The other nine predictions (cold urticaria, nasal cavity disease, common cold, pharyngitis, acute laryngopharyngitis, generic urticaria, recalcitrant atopic dermatitis, angioedema, atopic IgE responsiveness) rest on model output alone. The few linked trials and papers are unrelated to dimenhydrinate or the predicted indication.

**To proceed, the following is needed:**
- The HSA package insert (warnings and contraindications), which is a blocking item for safety screening
- Detailed mechanism-of-action data from DrugBank
- Human clinical evidence of dimenhydrinate or diphenhydramine in urticaria, such as a literature search for RCTs or systematic reviews
- Confirmation of the approved indications and available routes for the registered Singapore products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

