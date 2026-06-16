---
layout: default
title: Desvenlafaxine
parent: 僅模型預測 (L5)
nav_order: 315
evidence_level: L5
indication_count: 10
---

# Desvenlafaxine
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

# Desvenlafaxine: From Major Depressive Disorder to Obsessive-Compulsive Disorder

## One-Sentence Summary

Desvenlafaxine (brand name Pristiq) is the primary active metabolite of venlafaxine and a serotonin-norepinephrine reuptake inhibitor (SNRI), approved by the US FDA for the treatment of major depressive disorder (MDD).
The TxGNN model predicts it may also be effective for **Obsessive-Compulsive Disorder (OCD)**, supported by mechanistic plausibility via serotonergic activity shared with established OCD treatments — however, both retrieved clinical trials are mismatched to OCD and no direct Desvenlafaxine OCD trial exists, with the strongest indirect support coming from **1 RCT** of its parent compound venlafaxine and **2 additional publications**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major Depressive Disorder (US FDA-approved; not registered in Singapore) |
| Predicted New Indication | Obsessive-Compulsive Disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the provided dataset. Based on established pharmacology, Desvenlafaxine is an SNRI that inhibits the reuptake of both serotonin (5-HT) and norepinephrine (NE) at the presynaptic transporter, thereby increasing the synaptic availability of both monoamines. Unlike its parent drug venlafaxine, Desvenlafaxine exhibits a more balanced serotonin-to-norepinephrine inhibition ratio and does not require hepatic CYP2D6 activation, giving it a more predictable pharmacokinetic profile.

The serotonin dysregulation hypothesis is central to OCD pathophysiology. Current first-line pharmacotherapy for OCD consists of SSRIs and the tricyclic antidepressant clomipramine, all of which primarily enhance serotonergic neurotransmission. As an SNRI with potent serotonin reuptake inhibition, Desvenlafaxine shares this mechanistic core. Critically, venlafaxine — Desvenlafaxine's direct parent compound — demonstrated non-inferior efficacy to paroxetine in the first randomised double-blind SNRI trial in OCD (PMID 14624187, n=150), providing strong class-level and pharmacological precedent.

Despite this mechanistic rationale, Desvenlafaxine itself has no direct OCD clinical trial data. The two trials retrieved are both mismatched: one tested Desvenlafaxine in postpartum depression, and the other evaluated troriluzole as an OCD adjunct in patients who had inadequate responses to existing treatments including Desvenlafaxine (where the drug appears only as background medication). The prediction therefore remains at the mechanistic-analogy level (L4) and requires dedicated clinical investigation before further development can be justified.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01527786](https://clinicaltrials.gov/study/NCT01527786) | Phase 3 | Completed | 25 | Desvenlafaxine in postpartum depression — estimates proportion of women returning to functional status after treatment; **mismatched indication, not OCD** |
| [NCT03299166](https://clinicaltrials.gov/study/NCT03299166) | Phase 2/3 | Completed | 426 | Troriluzole (glutamate modulator) as adjunctive OCD therapy in patients with inadequate response to SSRI, clomipramine, venlafaxine, or Desvenlafaxine; Desvenlafaxine is a background treatment option, **not the investigational drug** |

> ⚠️ Both trials are classified as **Grade C** (mismatched data). No direct Desvenlafaxine OCD interventional trial is currently registered on ClinicalTrials.gov.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [14624187](https://pubmed.ncbi.nlm.nih.gov/14624187/) | 2003 | RCT | Journal of Clinical Psychopharmacology | Venlafaxine vs paroxetine in OCD (n=150, double-blind): both agents showed comparable efficacy; first randomised SNRI trial in OCD — provides direct class-level mechanistic support for Desvenlafaxine |
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Review | Expert Opinion on Pharmacotherapy | Updated review of double-blind studies on serotonergic antidepressants in OCD; confirms central role of the 5-HT system in OCD and summarises evidence for SNRI use |
| [36686097](https://pubmed.ncbi.nlm.nih.gov/36686097/) | 2022 | Review | Cureus | Postpartum depression review noting OCD as a downstream complication of untreated PPD — tangential; does not evaluate Desvenlafaxine for OCD |
| [40224942](https://pubmed.ncbi.nlm.nih.gov/40224942/) | 2025 | Case Report | Psychiatry and Clinical Psychopharmacology | Risperidone augmentation for antidepressant-resistant somatic symptom disorder and OCD — Desvenlafaxine not assessed as a study agent |

---

## Singapore Market Information

Desvenlafaxine currently has **no registered products in Singapore**. No authorisation records are available in the regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the serotonergic mechanism of Desvenlafaxine is biologically plausible for OCD and its parent compound venlafaxine has demonstrated efficacy in a head-to-head OCD RCT, Desvenlafaxine itself has no direct OCD clinical trial evidence, both retrieved trials are mismatched, and the drug is entirely absent from the Singapore market — making a development or procurement decision premature at this stage.

**To proceed, the following is needed:**

- **Clinical evidence gap**: Commission or identify a dedicated Phase 2 pilot trial of Desvenlafaxine in OCD to generate direct efficacy and tolerability data
- **MOA confirmation**: Obtain full DrugBank pharmacological profile (serotonin vs. norepinephrine reuptake inhibition ratios) to substantiate mechanistic differentiation from SSRIs in OCD
- **Safety data**: Download and parse TFDA/FDA prescribing information to capture black-box warnings, contraindications, and key drug interactions (currently all [Data Gap])
- **Regulatory pathway**: Assess Singapore HSA registration requirements and identify any bridging study obligations for a new OCD indication
- **Clinical positioning**: Benchmark against first-line OCD agents (fluvoxamine, sertraline, fluoxetine, clomipramine) to establish potential differentiation; consider whether Desvenlafaxine's CYP2D6-independent metabolism offers a practical advantage in treatment-resistant or augmentation settings

> **Note on a stronger candidate within this analysis:** The rank-8 prediction, **Dysthymic Disorder / Persistent Depressive Disorder**, carries substantially higher-quality evidence — including a completed Phase 4 RCT of Desvenlafaxine vs. placebo specifically in chronic depression (NCT01537068, n=59) and a dedicated open-label Dysthymia monotherapy study (NCT01948895, n=30) — and was scored **L2 / Proceed with Guardrails**. If prioritisation is required, the Dysthymia indication merits accelerated evaluation ahead of the OCD prediction.

---

*⚠️ Disclaimer: This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

