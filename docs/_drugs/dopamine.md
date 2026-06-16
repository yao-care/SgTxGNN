---
layout: default
title: Dopamine
parent: 僅模型預測 (L5)
nav_order: 342
evidence_level: L5
indication_count: 10
---

# Dopamine
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

# Dopamine: From Hemodynamic Support to Postural Orthostatic Tachycardia Syndrome

## One-Sentence Summary

Dopamine is a catecholamine neurotransmitter and vasopressor, primarily used intravenously for acute cardiovascular support in cardiogenic shock, septic shock, and hemodynamic instability.
The TxGNN model predicts it may be effective for **Postural Orthostatic Tachycardia Syndrome (POTS)**,
with **6 clinical trials** and **7 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute cardiovascular support (hemodynamic instability, cardiogenic/septic shock) |
| Predicted New Indication | Postural Orthostatic Tachycardia Syndrome (POTS) |
| TxGNN Prediction Score | 88.00% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Dopamine is a catecholamine neurotransmitter synthesised endogenously in both the central nervous system and the peripheral organs, including the kidneys. In the renal tubules, locally produced dopamine (derived from L-DOPA via DOPA decarboxylase) acts on D1 and D2 receptors to inhibit sodium reabsorption and promote natriuresis — a pathway distinct from the intravenous vasopressor use seen in critical care.

POTS is a form of dysautonomia characterised by excessive heart rate increase upon standing, often accompanied by plasma volume insufficiency and impaired sodium retention. Research has identified that POTS patients exhibit reduced renal dopamine synthesis and secretion in response to sodium loading, leading to inappropriately high sodium retention, sympathetic overactivation, and failure to adequately expand plasma volume. This creates a mechanistic hypothesis: if renal dopaminergic deficiency underlies the haemodynamic dysregulation in POTS, then restoring or supplementing the renal dopamine pathway could correct the sodium imbalance.

It is critically important to note that the research direction supported by this evidence is **oral L-DOPA or dietary dopa supplementation** (e.g., via fava beans) — not intravenous dopamine. Intravenous dopamine is unlikely to be appropriate here, as its β1-adrenergic stimulation would directly worsen tachycardia. The TxGNN prediction therefore points to the dopaminergic system as a therapeutic target, with the relevant intervention being oral/prodrug formulations that augment renal dopamine synthesis rather than systemic IV administration.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00685919](https://clinicaltrials.gov/study/NCT00685919) | Phase 2/3 | Completed | 32 | Investigated how inhibiting kidney dopamine synthesis with carbidopa affects urinary sodium excretion; compared POTS patients with healthy volunteers to characterise renal dopamine deficiency in POTS |
| [NCT01563107](https://clinicaltrials.gov/study/NCT01563107) | N/A | Completed | 38 | Examined the effect of low- vs. high-sodium diets on urinary sodium and dopamine excretion in POTS, testing whether the renin-angiotensin-aldosterone system and renal dopamine respond appropriately to dietary sodium changes |
| [NCT01547117](https://clinicaltrials.gov/study/NCT01547117) | N/A | Completed | 38 | Assessed whether high dietary sodium appropriately expands plasma volume in POTS and whether plasma renin activity, aldosterone, and renal dopamine modulate this response |
| [NCT01064739](https://clinicaltrials.gov/study/NCT01064739) | Early Phase 1 | Completed | 14 | Tested dietary catecholamine sources (notably fava beans, high in L-DOPA) for diuretic effects on renal sodium handling in POTS patients; supports oral L-DOPA supplementation strategy over IV dopamine |
| [NCT00001418](https://clinicaltrials.gov/study/NCT00001418) | N/A | Completed | 335 | PET scanning study of sympathetic innervation using fluorodopamine tracer in neurocardiological disorders including POTS; characterised autonomic dysfunction patterns rather than testing dopamine as therapy |
| [NCT00748228](https://clinicaltrials.gov/study/NCT00748228) | N/A | Terminated | 22 | The only trial directly testing dopamine as an intervention for orthostatic tolerance; study was terminated before completion and did not yield conclusive evidence — termination reason requires review |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [29937049](https://pubmed.ncbi.nlm.nih.gov/29937049/) | 2018 | Systematic Review/Meta-analysis | Mayo Clinic Proceedings | Evaluated the evidence base for all POTS treatments in light of a consensus statement; found a lack of options with clear benefit-to-risk ratios, underscoring the unmet need for validated therapies |
| [28522107](https://pubmed.ncbi.nlm.nih.gov/28522107/) | 2017 | Prospective Cohort | Autonomic Neuroscience | Characterised neurohumoral and haemodynamic responses to head-up tilt in high-norepinephrine vs. normal-norepinephrine POTS subtypes; supports catecholamine pathway involvement |
| [26608337](https://pubmed.ncbi.nlm.nih.gov/26608337/) | 2016 | Observational | Am J Physiol Heart Circ Physiol | Identified distinct neurohumoral biomarker profiles in adolescents with orthostatic intolerance; suggested dopamine-related profiles may predict treatment response |
| [32606041](https://pubmed.ncbi.nlm.nih.gov/32606041/) | 2020 | Case Series | J Investigative Medicine | Retrospective chart review of 47 POTS patients treated with bupropion (a norepinephrine and dopamine reuptake inhibitor); found potential benefit, supporting the role of dopaminergic pathways in POTS management |
| [12102462](https://pubmed.ncbi.nlm.nih.gov/12102462/) | 2002 | Review | Clinical Autonomic Research | Reviewed catecholamine abnormalities in autonomic disorders; documented that dopamine beta-hydroxylase (DBH) deficiency — which elevates dopamine and eliminates norepinephrine — causes severe orthostatic hypotension, illustrating the inverse relationship between dopamine and sympathetic vascular tone |
| [12403667](https://pubmed.ncbi.nlm.nih.gov/12403667/) | 2002 | Review | Circulation | Investigated cardiac sympathetic innervation and function in POTS and neurocardiogenic presyncope; confirmed orthostatic intolerance occurs without persistent sympathetic neurocirculatory failure, providing mechanistic context |
| [16601453](https://pubmed.ncbi.nlm.nih.gov/16601453/) | 2006 | Case Report | Current Opinion in Cardiology | Described familial POTS with a norepinephrine transporter gene mutation; provided genetic evidence for catecholamine pathway involvement in POTS pathogenesis |

---

## Singapore Market Information

Dopamine (DB00988) is **not currently registered** in Singapore. There are no active product licences, and the market status is confirmed as unmarketed. Any clinical use would require special import authorisation or compassionate use arrangement through the Health Sciences Authority (HSA).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence supports a biologically plausible mechanistic link between renal dopaminergic deficiency and POTS pathophysiology, validated by multiple completed physiological studies and a systematic review confirming unmet treatment need. However, the critical distinction between **intravenous dopamine** (inappropriate — would worsen tachycardia) and **oral L-DOPA/dietary dopamine precursors** (the relevant intervention target) must be resolved before any clinical programme can proceed.

**To proceed, the following is needed:**

- **Mechanistic clarification**: Formally distinguish between systemic IV dopamine use and renal-targeted oral dopa supplementation as the actual repurposing strategy; current TxGNN candidate may require reformulation as an L-DOPA or dopamine prodrug programme
- **Route of administration study**: Confirm whether an oral dopaminergic formulation can selectively augment renal dopamine without increasing systemic β1-adrenergic stimulation
- **Subtype stratification**: Identify which POTS subtypes (e.g., hypovolaemic POTS with documented renal dopamine deficiency) are most likely to respond
- **Termination review for NCT00748228**: Retrieve and analyse the reason for early termination of the only direct dopamine-in-orthostatic-tolerance trial; safety data from this study is critical
- **Singapore regulatory pathway**: As the drug is unregistered in Singapore, a Clinical Trial Authorisation (CTA) from HSA would be required for any prospective clinical evaluation
- **Safety profile**: Obtain complete prescribing information, warning labels, and contraindication data to assess whether POTS-specific populations (predominantly young women of reproductive age) face particular risks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

