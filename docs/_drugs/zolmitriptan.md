---
layout: default
title: Zolmitriptan
parent: 僅模型預測 (L5)
nav_order: 1079
evidence_level: L5
indication_count: 10
---

# Zolmitriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Zolmitriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Zolmitriptan is a selective 5-HT1B/1D receptor agonist (triptan) long established for the acute treatment of migraine attacks. The TxGNN model's top-ranked prediction for this drug is **Migraine with Brainstem Aura**, but this is a case where a very high similarity score does not translate into a safe or actionable repurposing signal — the evidence base consists only of narrative reviews (**0 clinical trials, 19 literature items**), and several of those reviews explicitly flag triptans as a **relative contraindication** in this specific migraine subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine (acute treatment of migraine attacks, with or without typical aura) — inferred from literature evidence; no Singapore license data available |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (structured MOA field) is not available for this record. Based on the literature contained in the evidence pack, zolmitriptan is a selective 5‑HT1B/1D receptor agonist ("triptan"). It relieves migraine by constricting cranial blood vessels and inhibiting the release of vasoactive neuropeptides from trigeminovascular afferents, thereby aborting the acute migraine attack and its associated symptoms (nausea, photophobia, phonophobia).

Migraine with brainstem aura (formerly "basilar-type migraine") is a clinical subtype within the broader migraine spectrum, which explains why a knowledge-graph model would place it close to zolmitriptan in embedding space — both share the parent concept "migraine." However, this is precisely where the prediction needs scrutiny rather than acceptance at face value: this subtype has traditionally been treated as a **relative contraindication** for triptans, out of concern that vasoconstrictive activity could theoretically worsen brainstem ischemia during an aura episode. The literature retrieved (e.g., PMID 11903526, "Triptans in the treatment of basilar migraine and migraine with prolonged aura") discusses this controversy directly rather than providing supportive efficacy data.

In short, the mechanistic overlap is real (same disease family, same receptor pathway), but the direction of the mechanistic argument in the literature is cautionary, not supportive. This is why the evidence level is capped at L3 (reviews/discussion only) and the recommendation is Hold rather than a more favorable decision.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11903526](https://pubmed.ncbi.nlm.nih.gov/11903526/) | 2001 | Review | Headache | Discusses use of triptans, including zolmitriptan, in basilar migraine and migraine with prolonged aura — the core reference for the historical caution around triptan use in this subtype |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | Review/Meta-analysis | J Headache Pain | Compares frovatriptan against rizatriptan, zolmitriptan and almotriptan specifically in migraine with aura |
| [22644173](https://pubmed.ncbi.nlm.nih.gov/22644173/) | 2012 | RCT subgroup analysis | Neurol Sci | Subgroup of a multicenter double-blind RCT comparing frovatriptan 2.5mg vs zolmitriptan 2.5mg specifically in migraine with aura (n=18 aura subgroup) |
| [25538676](https://pubmed.ncbi.nlm.nih.gov/25538676/) | 2014 | Review | Frontiers in Neurology | Reviews treatment options for vestibular migraine, a brainstem-symptom-related migraine variant; notes RCTs specific to this subtype remain scarce |
| [18624801](https://pubmed.ncbi.nlm.nih.gov/18624801/) | 2008 | RCT | Cephalalgia | Randomized comparison of six triptans (including zolmitriptan) in patients with migraine and early cutaneous allodynia |
| [12083998](https://pubmed.ncbi.nlm.nih.gov/12083998/) | 2002 | Review | Expert Opin Pharmacother | General review of zolmitriptan's clinical applications in migraine, including onset of action and symptom relief |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Evidence Assessment/Guideline | Headache | American Headache Society updated evidence assessment of acute migraine pharmacotherapies |
| [10473025](https://pubmed.ncbi.nlm.nih.gov/10473025/) | 1999 | Review | Drugs | Comprehensive review of zolmitriptan's efficacy and tolerability across RCTs in moderate-to-severe migraine |
| [9399012](https://pubmed.ncbi.nlm.nih.gov/9399012/) | 1997 | Preclinical Pharmacology | Cephalalgia | Preclinical pharmacology establishing zolmitriptan's central and peripheral 5-HT1B/1D activity |
| [9399016](https://pubmed.ncbi.nlm.nih.gov/9399016/) | 1997 | Postmarketing tolerability | Cephalalgia | Pooled tolerability data from >3,000 subjects treated with zolmitriptan across clinical studies |

---

## Singapore Market Information

Zolmitriptan currently holds **no marketing authorization in Singapore** (0 registrations, market status: Not Marketed). No product listing, dosage form, or approved indication text is available from local regulatory records.

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: While structured safety fields (key warnings, contraindications, DDI) are not populated in this evidence pack, the literature review itself indicates that migraine with brainstem aura has historically been treated as a **relative contraindication** for triptan-class drugs due to theoretical vasoconstrictive risk in the vertebrobasilar territory. This should be treated as a material safety signal pending confirmation from the official product label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for this indication is very high, but the supporting evidence consists entirely of narrative reviews with no supporting clinical trials, and part of that literature actively raises a safety concern rather than an efficacy signal — triptans have traditionally been considered relatively contraindicated in migraine with brainstem aura. Proceeding on this candidate without resolving the safety question would be premature.

**To proceed, the following is needed:**
- Official product label warnings/contraindications for zolmitriptan specific to basilar-type migraine / migraine with brainstem aura (currently a Blocking data gap, DG001)
- Structured mechanism of action data from DrugBank (currently a High-severity data gap, DG002)
- A formal risk-benefit reassessment by a clinician/pharmacist before any further evaluation of this specific subtype

**Note on alternative candidates:** Two other predictions in this same evidence pack — **Headache Disorder** and **Trigeminal Autonomic Cephalalgia** (cluster headache) — carry a much stronger evidence base (Evidence Level L1, multiple completed Phase 3 RCTs, recommendation "Proceed with Guardrails") and represent label-adjacent, mechanistically consistent extensions of zolmitriptan's existing triptan pharmacology. These are likely better candidates to prioritize than migraine with brainstem aura.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

