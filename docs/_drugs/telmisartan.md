---
layout: default
title: Telmisartan
parent: 僅模型預測 (L5)
nav_order: 950
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan: From Hypertension to Intracerebral Hemorrhage (Recurrence Prevention)

## One-Sentence Summary

> Telmisartan is an angiotensin II receptor blocker (ARB) originally used to treat hypertension.
> TxGNN generated 10 candidate indications for this drug, but 7 of them have **zero supporting trials or literature** and are flagged internally as low-confidence score artifacts.
> The one exception is **Intracerebral Hemorrhage (secondary prevention)**, supported by a completed Phase 3 RCT (TRIDENT, n=1,671) and **12 mechanistic/clinical publications** — this is the only candidate in the pack that clears the bar for further evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (ARB class — Singapore-specific label text not available, see data gaps) |
| Predicted New Indication | Intracerebral Hemorrhage (recurrence prevention) |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this specific evidence pack is not available (data gap). Based on general pharmacological knowledge, telmisartan is an angiotensin II type 1 (AT1) receptor blocker that also acts as a partial PPARγ agonist. Beyond blood-pressure lowering, this dual action gives it antioxidative, anti-inflammatory, and antiapoptotic properties in vascular and neural tissue — effects that have been studied specifically in the context of intracerebral hemorrhage (ICH) and hemorrhagic stroke models.

The link between hypertension control and ICH is mechanistically direct: uncontrolled blood pressure is the dominant modifiable risk factor for both first and recurrent intracerebral hemorrhage. Telmisartan's established antihypertensive efficacy therefore transfers naturally to a secondary-prevention role in ICH survivors. Preclinical studies further show AT1 blockade reduces apoptosis, inflammation, and oxidative stress in rat ICH and subarachnoid hemorrhage models, and improves cerebral vascular remodeling — a plausible biological basis beyond simple blood-pressure reduction.

Clinically, this rationale has already been tested: the TRIDENT trial evaluated a fixed-dose "Triple Pill" antihypertensive strategy (which typically includes an ARB) specifically to prevent recurrent stroke in patients with a history of ICH, and completed with over 1,600 patients enrolled. This is meaningfully different from the other 9 TxGNN candidates in this pack, most of which have no clinical or literature support and are explicitly annotated as likely knowledge-graph co-occurrence artifacts (e.g., Prinzmetal angina, ABri amyloidosis, Braddock syndrome).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1,671 | TRIDENT main trial — fixed low-dose "Triple Pill" BP-lowering strategy (on top of standard care) to reduce recurrent stroke in patients with prior ICH; directly relevant, largest and most complete evidence source. |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study; terminated early with only 1 participant, minimal evidentiary value. |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | N/A | Terminated | 4 | TRIDENT MRI sub-study; terminated early with only 4 participants, minimal evidentiary value. |

**Note:** TRIDENT tested a combination antihypertensive pill, not telmisartan monotherapy — the trial supports the BP-control strategy generally rather than being a telmisartan-specific efficacy study.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | RCT Protocol | Int J Stroke | Rationale and design of the TRIDENT trial for recurrent ICH prevention using combination BP-lowering therapy. |
| [15834293](https://pubmed.ncbi.nlm.nih.gov/15834293/) | 2005 | RCT (preclinical model) | J Hypertens | Telmisartan reverses cerebral arteriolar remodeling in hypertensive rats, comparable to ramipril. |
| [24636673](https://pubmed.ncbi.nlm.nih.gov/24636673/) | 2014 | Cohort | Int J Stroke | PRoFESS trial sub-analysis: race-ethnic differences in ischemic vs. hemorrhagic stroke recurrence under secondary prevention (including ARB-based regimens). |
| [19148963](https://pubmed.ncbi.nlm.nih.gov/19148963/) | 2009 | Clinical correspondence | N Engl J Med | Discussion of telmisartan for prevention of cardiovascular events (ONTARGET/TRANSCEND context). |
| [40045320](https://pubmed.ncbi.nlm.nih.gov/40045320/) | 2025 | Preclinical | J Neuroinflammation | Angiotensin II-induced hypertension model shows cerebral microhemorrhage development, supporting the RAAS–ICH mechanistic link. |
| [27078703](https://pubmed.ncbi.nlm.nih.gov/27078703/) | 2016 | Preclinical | Neurol Res | Telmisartan reduces oxidative stress and vasospasm after subarachnoid hemorrhage in animal model. |
| [17538008](https://pubmed.ncbi.nlm.nih.gov/17538008/) | 2007 | Preclinical | J Pharmacol Exp Ther | AT1 receptor blockade (telmisartan) reduces apoptosis, inflammation, and oxidative stress in normotensive rats with experimental ICH. |
| [22957022](https://pubmed.ncbi.nlm.nih.gov/22957022/) | 2012 | Preclinical | PLoS One | Telmisartan vs. candesartan: differential effects on pial arteriole diameter in hypertensive rats, relevant to cerebral vascular protection. |
| [28868047](https://pubmed.ncbi.nlm.nih.gov/28868047/) | 2017 | Preclinical | Front Neurol | Heme-induced inflammasome activation drives vasospasm after intraventricular hemorrhage — mechanistic backdrop for anti-inflammatory ARB effects. |

---

## Singapore Market Information

Telmisartan currently has **no registration records** in the Singapore dataset used for this evaluation (`market_status: 未上市`, `total_licenses: 0`). No product-level information (authorization number, product name, dosage form, approved indication) is available.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data were available in this evidence pack (all flagged as data gaps — see below).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT (TRIDENT, n=1,671) plus a coherent, multi-study mechanistic base (anti-inflammatory, antioxidative, antiapoptotic effects on cerebral vasculature) support intensive ARB-inclusive blood-pressure control for recurrent ICH prevention. However, TRIDENT tested a combination pill rather than telmisartan alone, so the evidence supports the *strategy* more directly than the *specific drug*, warranting guardrails rather than a full Go.

**To proceed, the following is needed:**
- Telmisartan-specific mechanism of action (MOA) data (currently a data gap, High severity) — needed to strengthen the mechanistic case independent of TRIDENT's combination-pill design.
- HSA/TFDA-equivalent label warnings and contraindications (currently a blocking data gap) — required before any Stage 1 safety evaluation can proceed, particularly given the ARB class's known caution in renal hypoperfusion states.
- Subgroup or post-hoc analysis of TRIDENT (or similar trials) isolating telmisartan's individual contribution, if available.
- A Singapore market-entry assessment, since telmisartan currently holds no local registration.

**Note on data gaps:** Two items from the evidence pack could not be resolved within this evaluation — TFDA/HSA-equivalent label warnings/contraindications (Blocking; requires downloading and parsing the official package insert) and detailed MOA data (High priority; requires a DrugBank API query). These require external data retrieval and are flagged separately rather than folded into the analysis above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

