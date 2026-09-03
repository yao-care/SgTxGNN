---
layout: default
title: Sumatriptan
parent: 僅模型預測 (L5)
nav_order: 935
evidence_level: L5
indication_count: 10
---

# Sumatriptan
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

# Sumatriptan: From Migraine to Migraine With Brainstem Aura

## One-Sentence Summary

> Sumatriptan is a selective 5-HT1B/1D receptor agonist globally established for the acute treatment of migraine and cluster headache, though it is currently **not registered in Singapore**.
> The TxGNN model predicts it may be effective for **Migraine With Brainstem Aura**, but this specific subtype is supported by **0 clinical trials** and **18 publications**, several of which raise safety concerns rather than confirm efficacy.
> The prediction score is very high, but the underlying evidence is observational/mechanistic rather than trial-based, and the drug class carries a known relative caution in this exact population.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine, acute treatment (well-established globally; no Singapore registration on file) |
| Predicted New Indication | Migraine With Brainstem Aura |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Sumatriptan is a selective 5-HT1B/1D (and partially 5-HT1F) receptor agonist. Its established mechanism is constriction of dilated cranial/dural blood vessels and inhibition of vasoactive neuropeptide (CGRP, substance P) release from trigeminal nerve terminals, which together abort migraine attacks driven by trigeminovascular activation. The formal `original_moa` field is flagged as a data gap, but this mechanism is well documented in the pharmacological literature and is directly referenced across the evidence in this pack.

Migraine with brainstem aura (formerly "basilar-type migraine") shares the same trigeminovascular activation pathway as typical migraine, which is why the TxGNN model links it so strongly to sumatriptan. However, this subtype specifically involves symptoms attributable to brainstem or posterior-circulation dysfunction, and triptans — as vasoconstrictive agents — have traditionally been treated as **relatively contraindicated** in this population due to theoretical concern about vasospasm in posterior-circulation vessels. This is not a simple mechanistic extension; it is a case where the same mechanism that treats ordinary migraine could pose a distinct safety concern in the very subtype being predicted.

Supporting literature in this pack (e.g., PMID 11903526, reviewing triptan use specifically in basilar migraine and prolonged aura, and PMID 25841032, showing reduced sumatriptan efficacy in migraine with aura vs. without aura) reflects this exact tension: real-world/clinical experience exists, but it points toward caution and reduced efficacy rather than clear-cut benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11903526](https://pubmed.ncbi.nlm.nih.gov/11903526/) | 2001 | Review | Headache | Reviews triptan use in basilar migraine and migraine with prolonged aura, specifically addressing neurologic symptom concerns |
| [1313746](https://pubmed.ncbi.nlm.nih.gov/1313746/) | 1992 | RCT | Cephalalgia | Double-blind, placebo-controlled trial of oral sumatriptan 200mg in acute migraine **with aura**, showing 70–85% efficacy |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Clinical Study | Neurology | Found **reduced** treatment response to sumatriptan in migraine with aura vs. without aura |
| [8559405](https://pubmed.ncbi.nlm.nih.gov/8559405/) | 1996 | Clinical Study | Neurology | Examined subcutaneous sumatriptan's effect specifically on the aura phase of migraine |
| [25841027](https://pubmed.ncbi.nlm.nih.gov/25841027/) | 2015 | Editorial | Neurology | Commentary questioning whether presence of aura predicts migraine severity or triptan response |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review/Guideline | Headache | American Headache Society evidence-based assessment of acute migraine pharmacotherapies, including triptans |
| [23657930](https://pubmed.ncbi.nlm.nih.gov/23657930/) | 2014 | RCT | Phytotherapy Research | Double-blind RCT comparing ginger powder vs. sumatriptan for acute migraine |
| [21469920](https://pubmed.ncbi.nlm.nih.gov/21469920/) | 2011 | Review | Expert Rev Neurother | Reviews needle-free subcutaneous sumatriptan (Sumavel DosePro) approval for migraine with/without aura and cluster headache |
| [11318886](https://pubmed.ncbi.nlm.nih.gov/11318886/) | 2001 | RCT | Headache | Compared isometheptene combination vs. sumatriptan succinate for migraine with or without aura |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | Handbook of Clinical Neurology | Reviews status migrainosus, a persistent/refractory migraine complication relevant to difficult-to-treat aura variants |

---

## Singapore Market Information

Sumatriptan currently has **no market authorization on record in Singapore** (0 licenses; market status: 未上市/Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data were available in this evidence pack (all fields flagged as data gaps).

Note: independent of the missing structured safety data, the literature above (PMID 11903526) reflects a long-standing clinical caution that triptans are relatively contraindicated in migraine with brainstem/basilar aura due to their vasoconstrictive mechanism — this should be treated as a safety-relevant signal even though it does not appear in the structured `safety` block.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the actual evidence base is L3 (no trials, observational/review-level literature only), and the strongest disease-specific literature (PMID 11903526, 25841032) points toward reduced efficacy and a traditional relative contraindication for vasoconstrictive triptans in this specific brainstem-aura subtype — the opposite of a green light. Combined with zero market presence in Singapore, this prediction is not ready to advance.

**To proceed, the following is needed:**
- Package insert / HSA-equivalent safety data confirming current labeling on basilar/brainstem aura (DG001)
- Confirmed DrugBank MOA record to formally replace the current data gap (DG002)
- A structured risk assessment specifically addressing vasoconstriction risk in posterior-circulation migraine before any clinical exploration
- Consideration of the better-evidenced predictions in this same pack — **headache disorder** (L1, Proceed with Guardrails) and **trigeminal autonomic cephalalgia/cluster headache** (L2, Proceed with Guardrails) — which reflect sumatriptan's actual established use pattern and carry substantially stronger trial support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

