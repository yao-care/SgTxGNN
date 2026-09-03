---
layout: default
title: Nifedipine
parent: 僅模型預測 (L5)
nav_order: 704
evidence_level: L5
indication_count: 10
---

# Nifedipine
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

# Nifedipine: From Hypertension/Angina to Migraine with Brainstem Aura

## One-Sentence Summary

Nifedipine is a dihydropyridine calcium channel blocker (CCB) whose established uses are hypertension and angina pectoris. The TxGNN model predicts it may be effective for **migraine with brainstem aura**, but this is currently supported only by **2 publications** and **no dedicated clinical trials** — and the evidence that does exist is discouraging rather than supportive, so this candidate should be treated with caution.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, angina pectoris (dihydropyridine CCB class) — specific regulatory indication text not available in this evidence pack |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 92.63% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this candidate is not available (Data Gap). Based on known pharmacology, Nifedipine is a dihydropyridine calcium channel blocker; its efficacy in hypertension and angina pectoris is well established, and mechanistically CCBs have long been proposed for migraine prophylaxis through inhibition of calcium influx into cerebrovascular smooth muscle, reducing vascular reactivity and cortical spreading depression-related vasomotor changes — a mechanism already validated clinically for the related CCB flunarizine.

However, the prediction here targets a specific migraine **subtype** — migraine with brainstem aura — rather than migraine in general. All identified literature addresses migraine/migraine-with-aura as a broad category, with no evidence specific to the brainstem aura subtype. This distinction matters clinically: some guidance is cautious about vasoactive agents in brainstem aura, since theoretical vasodilation could aggravate brainstem-mediated symptoms (e.g., vertigo, ataxia, diplopia) rather than relieve them.

Notably, the two directly relevant publications are not supportive: a double-blind controlled trial (Hoffert et al., 1992) found nifedipine *increased* headache intensity compared to vehicle and concluded it is **not useful** as an abortive treatment for migraine with aura, while a review (Montastruc & Senard, 1992) states that CCB efficacy in migraine prophylaxis, including nifedipine, "cannot be considered as firmly demonstrated." Broader migraine-disorder literature (not the aura subtype) is mixed — some RCTs report benefit (e.g., Lamsudin 1993, Shukla 1995) while others report no benefit and significant side effects (e.g., McArthur 1989, Albers 1989) — reinforcing that this signal, while mechanistically plausible, is not yet clinically validated for the specific predicted subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1423566](https://pubmed.ncbi.nlm.nih.gov/1423566/) | 1992 | RCT | Cephalalgia | Double-blind controlled trial of nifedipine as abortive treatment for acute migraine-with-aura attacks; nifedipine increased headache intensity vs. vehicle — concluded not useful as an abortive treatment |
| [1353873](https://pubmed.ncbi.nlm.nih.gov/1353873/) | 1992 | Review | Pathologie-biologie | Review of calcium antagonists (verapamil, diltiazem, nifedipine) for migraine prophylaxis; concludes efficacy is not firmly demonstrated due to trial design limitations |

---

## Singapore Market Information

Nifedipine has no registered product licenses in the Singapore evidence pack (market status: not marketed; 0 registrations). No authorization table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/HSA label warnings and contraindications are a documented Blocking data gap for this candidate — see Next Steps.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only subtype-specific evidence (2 publications, no trials) is negative or inconclusive rather than supportive, and there is a plausible theoretical safety concern (vasodilation potentially aggravating brainstem-type aura symptoms) that has not been ruled out. Broader migraine literature shows mixed results, and MOA and safety label data required for a formal S1 review are both missing.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent package insert data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- Subtype-specific clinical evidence (trials or observational studies) for migraine with brainstem aura, not just migraine in general
- Formal safety assessment of vasoactive-agent use in brainstem aura before any further development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

