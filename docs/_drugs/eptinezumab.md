---
layout: default
title: Eptinezumab
parent: 僅模型預測 (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
---

# Eptinezumab
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

# Eptinezumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Eptinezumab (Vyepti) is an anti-CGRP monoclonal antibody approved by the FDA for preventive treatment of episodic and chronic migraine in adults.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** (IHS 1.2.2, formerly basilar-type migraine),
with **0 clinical trials** and **8 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Preventive treatment of episodic and chronic migraine |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on information from the collected literature, Eptinezumab is an intravenous monoclonal antibody that directly targets calcitonin gene-related peptide (CGRP) — a potent vasodilatory neuropeptide abundantly expressed in the trigeminal-vascular axis. By binding to circulating CGRP and blocking its interaction with the CGRP receptor, eptinezumab suppresses neurogenic inflammation and vasodilation in the trigeminovascular system, which is the core pathway underlying migraine attacks.

Migraine with brainstem aura (IHS 1.2.2) is a specific subtype of migraine with aura in which the aura symptoms originate from brainstem structures — presenting as vertigo, tinnitus, diplopia, dysarthria, or ataxia. Since CGRP is expressed throughout brainstem nuclei involved in trigeminovascular signalling (including the trigeminal nucleus caudalis), the mechanistic basis for eptinezumab's potential efficacy in this subtype is biologically plausible and directly parallel to its established effect in broader migraine prevention.

The most directly relevant evidence is a 2022 post-hoc subgroup analysis of the Phase 3 PROMISE-1 and PROMISE-2 trials (PMID 35302389), which examined eptinezumab specifically in patients with self-reported aura and confirmed favourable efficacy and safety. While this does not constitute an independent RCT targeting the brainstem aura subtype, it provides the strongest available indirect evidence. The FDA's approved broad migraine prevention indication implicitly covers aura subtypes, but no dedicated trial has enrolled patients specifically with migraine with brainstem aura.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35302389](https://pubmed.ncbi.nlm.nih.gov/35302389/) | 2022 | Post-hoc RCT Subgroup | *Cephalalgia* | Post-hoc analysis of PROMISE-1 and PROMISE-2: eptinezumab demonstrated efficacy and safety specifically in migraine patients with self-reported aura — most direct evidence for the predicted indication |
| [40229719](https://pubmed.ncbi.nlm.nih.gov/40229719/) | 2025 | RCT | *J Headache Pain* | PACAP38-induced migraine attacks occur independently of CGRP signalling; contextualises mechanistic scope and limits of anti-CGRP therapies including eptinezumab |
| [40341526](https://pubmed.ncbi.nlm.nih.gov/40341526/) | 2025 | Observational | *Headache* | Two cases of genetic migraine syndromes (including chronic migraine with visual aura) showing clinically meaningful response to CGRP antagonist treatment |
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Case Report + Review | *J Clin Medicine* | Anti-CGRP mAbs including eptinezumab may reduce migraine aura frequency; postulated mechanism via inhibition of cortical spreading depression-related CGRP release |
| [40191903](https://pubmed.ncbi.nlm.nih.gov/40191903/) | 2025 | Case Report | *Rev Neurol* | IV eptinezumab successfully managed wearing-off effect in a patient with chronic migraine with aura refractory to two subcutaneous anti-CGRP antibodies |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | *Handb Exp Pharmacol* | Foundational review establishing CGRP as the central mediator in the trigeminovascular cascade; covers aura-associated subtypes and CNS involvement |
| [32699706](https://pubmed.ncbi.nlm.nih.gov/32699706/) | 2020 | Review | *Cureus* | CGRP antagonists (including eptinezumab) effective across episodic and chronic migraine; pathophysiology review covering aura and autonomic features |
| [33550872](https://pubmed.ncbi.nlm.nih.gov/33550872/) | 2021 | Review | *Pain Management* | Contextualises eptinezumab among the four approved anti-CGRP preventive therapies; summarises PROMISE trial outcomes and drug class characteristics |

---

## Singapore Market Information

Eptinezumab is currently **not registered** with the Health Sciences Authority (HSA) in Singapore. No product authorisations have been issued and no licences are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is directly compelling — migraine with brainstem aura shares the identical CGRP-dependent trigeminovascular pathway targeted by eptinezumab, and a post-hoc analysis of two large Phase 3 RCTs specifically confirms efficacy in patients with aura. However, the absence of a dedicated trial for the brainstem aura subtype, combined with no Singapore registration, means clinical deployment requires additional safeguards before proceeding.

**To proceed, the following is needed:**

- Obtain full prescribing information (US FDA label for Vyepti / eptinezumab) to document contraindications, key warnings, and cardiovascular safety considerations
- Confirm whether patients with migraine with brainstem aura (basilar-type migraine) were explicitly included or excluded in the PROMISE-1 and PROMISE-2 protocols — some legacy trial exclusion criteria banned basilar-type migraine due to historical stroke concerns
- Conduct a dedicated prospective study or real-world registry to collect outcome data specifically for the brainstem aura subtype
- Evaluate HSA regulatory pathway for Singapore market entry (import licence or full registration)
- Assess cardiovascular risk profile of the target population, given that anti-CGRP therapy warrants caution in patients with recent cardiovascular events
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

