---
layout: default
title: Fremanezumab
parent: 僅模型預測 (L5)
nav_order: 453
evidence_level: L5
indication_count: 10
---

# Fremanezumab
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

# Fremanezumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

> Fremanezumab is a fully humanized anti-CGRP monoclonal antibody originally used for the preventive treatment of episodic and chronic migraine. The TxGNN model predicts it may also be effective for **migraine with brainstem aura**, a rare migraine subtype, with **0 clinical trials** but **20 supporting publications** (largely mechanistic and real-world observational studies) currently identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine prevention (episodic and chronic migraine) — inferred from supporting literature; no formal Singapore label on file |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data from DrugBank is not currently available for this candidate. Based on the literature retrieved, however, fremanezumab is known to be a fully humanized IgG2Δa monoclonal antibody that selectively binds and neutralizes calcitonin gene-related peptide (CGRP), preventing it from activating trigeminovascular neurons that drive migraine pain (PMID 28642283). CGRP is considered a central mediator of migraine pathophysiology across subtypes (PMID 30725283).

Migraine with brainstem aura (formerly known as basilar-type migraine) shares the same underlying trigeminovascular and CGRP-mediated pathway as the episodic/chronic migraine for which fremanezumab is already used, and both are believed to involve cortical spreading depression (CSD) — the electrophysiological wave thought to underlie aura symptoms. Preclinical work has directly tested this link: fremanezumab was shown to reduce the propagation rate and shorten the cortical recovery period of CSD in an animal model with a compromised blood-brain barrier (PMID 31895266), and does not worsen CSD-induced arterial dilatation or plasma protein extravasation (PMID 31127003) — findings relevant specifically to the aura mechanism rather than only migraine pain.

Clinically, this mechanistic plausibility is reinforced by real-world evidence: a post-hoc analysis of the phase 3b FOCUS study found comparable efficacy and quality-of-life benefits in fremanezumab-treated patients with and without aura or associated neurological dysfunction (PMID 35302681), and case reports/small case series specifically describe anti-CGRP monoclonal antibodies (including fremanezumab) being used in migraine with aura and hemiplegic migraine, a related aura subtype (PMID 35268319, 38332541, 41618146, 40264646). No evidence in this pack is specific to a randomized trial in the brainstem-aura subtype itself, so the rationale remains mechanistic and observational rather than confirmatory.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Case report/Review | Journal of Clinical Medicine | Reviews case reports on anti-CGRP mAbs (incl. fremanezumab) for migraine aura prevention; notes therapeutic effect on aura remains poorly documented despite proven efficacy on headache pain |
| [38332541](https://pubmed.ncbi.nlm.nih.gov/38332541/) | 2024 | Observational case series | CNS Neuroscience & Therapeutics | Case series specifically assessing anti-CGRP-targeted therapy's effect on migraine aura; limited clinical evidence exists but supports possible benefit |
| [41618146](https://pubmed.ncbi.nlm.nih.gov/41618146/) | 2026 | Case series / quantitative analysis | The Journal of Headache and Pain | Individual patient data analysis of anti-CGRP mAb effectiveness/safety in hemiplegic migraine, a rare aura subtype systematically excluded from RCTs |
| [40264646](https://pubmed.ncbi.nlm.nih.gov/40264646/) | 2025 | Case report/Review | Frontiers in Neurology | Case report plus literature review of anti-CGRP mAb efficacy in hemiplegic migraine, given the lack of RCT data in this population |
| [31127003](https://pubmed.ncbi.nlm.nih.gov/31127003/) | 2019 | Preclinical/mechanistic | The Journal of Neuroscience | Shows fremanezumab does not worsen CSD-induced arterial dilatation/plasma protein extravasation, informing CGRP's specific role in migraine with aura |
| [31895266](https://pubmed.ncbi.nlm.nih.gov/31895266/) | 2020 | Preclinical/mechanistic | Pain | Fremanezumab slows CSD propagation rate and shortens cortical recovery period in rats with compromised blood-brain barrier — direct mechanistic link to the aura substrate |
| [28642283](https://pubmed.ncbi.nlm.nih.gov/28642283/) | 2017 | Preclinical/mechanistic | The Journal of Neuroscience | Foundational study demonstrating fremanezumab selectively inhibits CGRP-driven trigeminovascular neuron activation |
| [35302681](https://pubmed.ncbi.nlm.nih.gov/35302681/) | 2022 | Post-hoc subgroup analysis (Phase 3b FOCUS) | European Journal of Neurology | Fremanezumab shows comparable efficacy and quality-of-life improvement in patients with and without aura/associated neurological dysfunction |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | Handbook of Experimental Pharmacology | Reviews CGRP's central pathophysiological role in migraine, including the aura subgroup, supporting the biological rationale for CGRP-targeted therapy |
| [35775208](https://pubmed.ncbi.nlm.nih.gov/35775208/) | 2022 | Review/Observational | Cephalalgia | Examines effects of erenumab, fremanezumab, and galcanezumab on migraine's central/prodromal symptoms, an area poorly studied in prior RCTs |

---

## Singapore Market Information

Fremanezumab is not currently registered or marketed in Singapore (0 licenses on file). No product authorization data is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong — fremanezumab's CGRP-blocking action directly targets pathways implicated in cortical spreading depression, the presumed substrate of migraine aura — and is reinforced by real-world subgroup data and case series in aura-related migraine subtypes. However, evidence is limited to L3 (observational/case-series level), with no clinical trials specifically enrolling migraine with brainstem aura, and the drug is not currently marketed in Singapore.

**To proceed, the following is needed:**
- TFDA/HSA package insert data on warnings and contraindications (currently a blocking data gap)
- Structured DrugBank mechanism-of-action data to formally confirm the CGRP-pathway linkage
- Dedicated clinical trial or larger cohort data specifically enrolling migraine with brainstem aura (rather than aura in general or hemiplegic migraine)
- Confirmation of Singapore/HSA regulatory registration pathway, given the drug is not currently marketed locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

