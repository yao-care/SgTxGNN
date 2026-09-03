---
layout: default
title: Pheniramine
parent: 僅模型預測 (L5)
nav_order: 774
evidence_level: L5
indication_count: 10
---

# Pheniramine
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

# Pheniramine: From Allergic Conditions (Antihistamine Use) to Allergic Urticaria

## One-Sentence Summary

Pheniramine is not currently registered in Singapore, and no original-indication record is available in the source data — as a first-generation H1-antihistamine, it is pharmacologically associated with treating allergic conditions. The TxGNN model's top prediction is **Allergic Urticaria**, supported by **1 clinical trial** (low relevance, atropine/pseudoephedrine study) and **20 literature articles**, though direct pheniramine-specific evidence remains limited and the rationale itself notes this may largely overlap with the drug's already-established antihistaminic use rather than a genuinely new application.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (drug not registered in Singapore; classically used as a first-generation H1-antihistamine for allergic conditions) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Pheniramine is a first-generation H1-antihistamine of the alkylamine class (structurally and pharmacologically related to chlorpheniramine and dexchlorpheniramine), whose primary action is blockade of the histamine H1 receptor — the same pathway implicated in the pathophysiology of allergic urticaria (mast cell histamine release driving wheal-and-flare reactions).

Because histamine-mediated urticaria is the canonical indication for H1-antihistamines as a drug class, the mechanistic link is well established at the class level. However, this is an important caveat rather than a clean confirmation: the underlying evidence review explicitly notes that this predicted pathway is already the antihistamine class's "core business" rather than a truly novel indication for pheniramine specifically — the gap is that pheniramine itself lacks direct comparative trial data, even though closely related molecules (chlorpheniramine, dexchlorpheniramine) have decades of supporting literature.

In other words, the prediction is mechanistically sound but adds limited novelty over pheniramine's known pharmacological class. Its practical value here lies more in confirming a plausible, low-risk indication than in uncovering an unexpected repurposing opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02082054](https://clinicaltrials.gov/study/NCT02082054) | Phase 2 | Unknown | 125 | Dose-ranging study of atropine combined with pseudoephedrine/chlorpheniramine in seasonal allergic rhinitis; evaluated via total nasal symptom scores. **Relevance flagged as Grade C** — the trial centers on atropine dosing, not pheniramine or antihistamine mechanism specifically, and is likely a disease-term mismatch rather than direct drug evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35652393](https://pubmed.ncbi.nlm.nih.gov/35652393/) | 2024 | Review | Curr Rev Clin Exp Pharmacol | Comprehensive review of chlorpheniramine (same alkylamine H1-antihistamine class as pheniramine), covering established and emerging uses including chronic urticaria |
| [39265704](https://pubmed.ncbi.nlm.nih.gov/39265704/) | 2024 | Cohort/Comparative | Eur J Pharm Sci | Phase 1 RCT comparing oral bilastine, parenteral dexchlorpheniramine, and new parenteral bilastine on histamine-induced wheal-and-flare response |
| [18597008](https://pubmed.ncbi.nlm.nih.gov/18597008/) | 2008 | Cohort | Methods Find Exp Clin Pharmacol | Large-scale surveillance (1,742 patients) of sedative profiles of H1-antihistamines across allergic conditions |
| [31852144](https://pubmed.ncbi.nlm.nih.gov/31852144/) | 2019 | Case Report/Pharmacovigilance Review | Medicine | Two cases of chlorpheniramine-induced anaphylaxis plus retrospective pharmacovigilance database review; chlorpheniramine noted as commonly used for urticaria and allergic rhinitis |
| [40324831](https://pubmed.ncbi.nlm.nih.gov/40324831/) | 2025 | Case Report | Indian J Pharmacol | Pheniramine (Avil) + hydrocortisone used for anaphylactic reaction management; reports a serious adverse event (loss of consciousness) with concurrent administration |
| [40125237](https://pubmed.ncbi.nlm.nih.gov/40125237/) | 2025 | Case Report | Cureus | Immediate hypersensitivity reaction to pheniramine itself, in a patient with multiple drug hypersensitivity syndrome |
| [15623181](https://pubmed.ncbi.nlm.nih.gov/15623181/) | 2004 | Pharmacology Study | JPMA | Comparative effects of chlorpheniramine (1st-gen) vs. loratadine (2nd-gen) antihistamine on isolated rabbit trachea, relevant to allergic airway/urticarial mechanism |
| [28601540](https://pubmed.ncbi.nlm.nih.gov/28601540/) | 2017 | Case Report | Am J Med | Atrial fibrillation occurring during anaphylaxis, a condition context in which antihistamines including pheniramine are used |
| [26179134](https://pubmed.ncbi.nlm.nih.gov/26179134/) | 2015 | Case Report | Contact Dermatitis | Palpebral angioedema and allergic contact dermatitis case, illustrating antihistamine-relevant allergic presentations |

---

## Singapore Market Information

Pheniramine currently has **no registered authorizations in Singapore** (0 licenses on file; market status: not marketed). No product name, dosage form, or approved indication text is available from the regulatory data source.

---

## Safety Considerations

Please refer to the package insert for safety information. Official TFDA/HSA-sourced warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack — this is flagged as a **blocking data gap (DG001)**, meaning a formal safety screening (S1 stage) cannot be completed until label-level safety data is obtained.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Class-level mechanistic and literature support for H1-antihistamines in urticaria is strong (L3: reviews and cohort-level studies), but pheniramine-specific evidence is sparse, the top clinical trial match is low-relevance, and the indication substantially overlaps with the drug's already-known antihistaminic use rather than representing a clearly novel repurposing target. A blocking safety data gap (missing official warnings/contraindications) also prevents a complete safety evaluation at this time.

**To proceed, the following is needed:**
- Official Singapore HSA package insert / label data (warnings, contraindications) to resolve the blocking gap (DG001)
- Confirmed mechanism of action documentation from DrugBank (DG002)
- Pheniramine-specific clinical evidence, rather than relying on class-level chlorpheniramine/dexchlorpheniramine data
- Clarification on whether "allergic urticaria" constitutes a meaningfully new indication versus the drug's existing antihistaminic use, before committing repurposing resources
- Regulatory pathway assessment, given the drug is not currently marketed in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

