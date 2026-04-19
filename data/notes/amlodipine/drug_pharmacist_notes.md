# Amlodipine: From Hypertension to Intracerebral Hemorrhage Secondary Prevention

## One-Sentence Summary

Amlodipine is a dihydropyridine calcium channel blocker (CCB) widely used for hypertension and stable angina worldwide. The TxGNN model identifies 10 neurological and vascular repurposing candidates; **intracerebral hemorrhage (ICH) secondary prevention** shows the strongest clinical evidence among them, with **5 clinical trials** (including a completed Phase 3 RCT) and **8 publications** identified. The recommended decision for this lead indication is **Proceed with Guardrails**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension; Chronic stable angina; Vasospastic angina |
| Primary Actionable Prediction | Intracerebral Hemorrhage (Secondary Prevention) |
| TxGNN Prediction Score | 99.79% (intracerebral hemorrhage) / 99.94% (top-ranked: brain stem infarction) |
| Evidence Level | L2 — Intracerebral Hemorrhage (lead candidate); L5 for 7 of 10 predictions |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Proceed with Guardrails** (ICH); Hold for 7 of 10 predictions |

---

## All Predicted Indications at a Glance

| TxGNN Rank | Disease | TxGNN Score | Evidence Level | Decision |
|-----------|---------|-------------|----------------|---------|
| 1 | Brain Stem Infarction | 99.94% | L5 | Hold |
| 2 | Pulmonary Hypertension (Lung Disease/Hypoxia) | 99.91% | L5 | ⚠️ Hold — Safety concern |
| 3 | Pulmonary Hypertension (Multifactorial) | 99.91% | L5 | ⚠️ Hold — Safety concern |
| 4 | Malignant Renovascular Hypertension | 99.90% | L4 | Research Question |
| 5 | Malignant Hypertensive Renal Disease | 99.90% | L5 | Hold |
| 6 | Cerebral Artery Occlusion | 99.89% | L3 | Research Question |
| 7 | Braddock Syndrome | 99.88% | L5 | Hold |
| 8 | MRI-Defined Brain Infarct | 99.86% | L4 | Hold |
| 9 | ABri Amyloidosis | 99.84% | L5 | Hold |
| **10** | **Intracerebral Hemorrhage** | **99.79%** | **L2** | **★ Proceed with Guardrails** |

> **Note:** TxGNN prediction score does not correlate with clinical evidence strength. Intracerebral hemorrhage ranks 10th by TxGNN score but 1st by evidence level — making it the primary actionable candidate in this pack.

> ⚠️ **Safety alert (Ranks 2 & 3):** Amlodipine is relatively contraindicated in WHO Group 3 (lung disease/hypoxia) and Group 5 (multifactorial mechanism) pulmonary hypertension. Systemic vasodilation may worsen ventilation-perfusion mismatch and aggravate hypoxaemia. Literature hits for these indications are false positives — general hypoxia biology papers with no relevance to Amlodipine efficacy. These indications should not be pursued.

---

## Why is This Prediction Reasonable?

Amlodipine selectively blocks L-type voltage-gated calcium channels in arterial smooth muscle cells, causing vasodilation, reducing peripheral vascular resistance, and lowering blood pressure. Unlike many antihypertensives, its high lipophilicity enables membrane penetration, which may also confer antioxidant effects observed in experimental models. Its half-life of approximately 35–50 hours provides stable, predictable blood pressure control with once-daily dosing — a practical advantage for long-term secondary prevention.

Hypertension is the single most important modifiable risk factor for intracerebral haemorrhage (ICH), accounting for over 70% of cases. After an initial ICH event, the risk of recurrence remains substantially elevated. Intensive blood pressure reduction (SBP < 130 mmHg) is the cornerstone of secondary prevention, and this creates a direct mechanistic bridge: Amlodipine's antihypertensive mechanism addresses the primary pathophysiological driver of ICH recurrence. The TRIDENT trial — a completed Phase 3 international RCT (n=1,671) — specifically tested a fixed-dose triple combination BP-lowering strategy (including a dihydropyridine CCB) to prevent recurrent stroke in post-ICH patients. The CASE-J trial further provides direct comparative data on Amlodipine (CCB arm) versus Candesartan (ARB) in high-risk Japanese hypertensive patients, with cardiovascular and cerebrovascular events as primary endpoints.

Beyond blood pressure control, multiple animal studies demonstrate that Amlodipine reduces neuronal injury after cerebral ischaemia by blocking calcium overload-mediated excitotoxicity and scavenging reactive oxygen species — mechanisms potentially relevant to both haemorrhagic and ischaemic brain injury contexts. This preclinical basis also supports the Research Question recommendation for cerebral artery occlusion (Rank 6, L3 evidence), where five consistent rodent middle cerebral artery occlusion studies confirm neuroprotective effects.

---

## Clinical Trial Evidence (Intracerebral Hemorrhage — Lead Indication)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1,671 | TRIDENT: Multicentre international double-blind RCT of fixed-dose triple-pill BP-lowering therapy (including CCB) vs. standard care in post-ICH patients; primary endpoint: time to first recurrent stroke |
| [NCT00134160](https://clinicaltrials.gov/study/NCT00134160) | Phase 4 | Completed | 1,000 | CASE-J sub-study: High-dose ARB (Candesartan) monotherapy vs. ARB + CCB (Amlodipine) combination in elderly Japanese hypertensive patients at high cardiovascular risk; cardiovascular events as primary endpoint |
| [NCT03264352](https://clinicaltrials.gov/study/NCT03264352) | Phase 4 | Recruiting | 11,414 | IPAD: Antihypertensive treatment in type 2 diabetes with high-normal BP; broad cardiovascular/cerebrovascular event prevention; not ICH-specific but relevant to BP strategy |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT Cognitive Sub-study: Effect of intensive BP lowering on cognitive decline post-ICH; terminated due to insufficient enrolment — no usable data |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | Phase NA | Terminated | 4 | TRIDENT MRI Sub-study: Imaging biomarkers of BP lowering in post-ICH patients; terminated early — provides contextual background only |

---

## Literature Evidence (Intracerebral Hemorrhage — Lead Indication)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | RCT Design Paper | Int J Stroke | TRIDENT trial rationale and design: confirms CCB-containing triple-pill strategy as the intervention for ICH secondary prevention |
| [14717341](https://pubmed.ncbi.nlm.nih.gov/14717341/) | 2003 | RCT Protocol | Hypertension Research | CASE-J trial design: Candesartan vs. Amlodipine in 1,000 high-risk Japanese hypertensive patients; cardiovascular event endpoints — direct comparative Amlodipine data |
| [23053838](https://pubmed.ncbi.nlm.nih.gov/23053838/) | 2013 | Observational Study | Neurological Sciences | Atenolol in acute hypertensive ICH (n=138); comparative evaluation of antihypertensive agents on mortality, SIRS, and 3-month outcomes |
| [17077518](https://pubmed.ncbi.nlm.nih.gov/17077518/) | 2006 | Pharmacological Study | Biol Pharm Bull | Benidipine (dihydropyridine CCB, same class as Amlodipine) improves cerebral blood flow autoregulation in spontaneously hypertensive rats; class-level mechanistic support |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Narrative Review | Cardiovasc Drugs Therapy | Calcium channel antagonist mechanisms in severe hypertension; rationale for CCBs targeting calcium overload in vascular smooth muscle |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Case Report | Ann Pharmacother | ⚠️ Probable Amlodipine-induced angioedema in a patient with right thalamic haemorrhagic stroke — safety signal requiring monitoring in ICH population |
| [26698202](https://pubmed.ncbi.nlm.nih.gov/26698202/) | 2015 | Case Report | BMJ Case Reports | PRES following rapid antihypertensive withdrawal (including Amlodipine) post-bariatric surgery in a patient with ICH history — highlights risks of abrupt discontinuation |
| [37489780](https://pubmed.ncbi.nlm.nih.gov/37489780/) | 2024 | Case Report | Current Drug Safety | Tizanidine-induced hypotension in stroke patient on multiple antihypertensives; safety context for multi-drug BP regimens in neurological patients |

---

## Additional Evidence: Cerebral Artery Occlusion (Research Question, L3)

Five animal studies directly tested Amlodipine in rodent middle cerebral artery occlusion (tMCAO) models and consistently demonstrated neuroprotective effects. No human clinical trials have directly tested Amlodipine for this indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21538457](https://pubmed.ncbi.nlm.nih.gov/21538457/) | 2011 | Animal Study | J Neuroscience Research | Amlodipine ± atorvastatin in metabolic syndrome rats after 90-min tMCAO: reduced infarct size via anti-apoptotic and anti-autophagic mechanisms |
| [20971084](https://pubmed.ncbi.nlm.nih.gov/20971084/) | 2011 | Animal Study | Brain Research | Amlodipine + atorvastatin synergistic neuroprotection after tMCAO in Zucker metabolic rats; combination superior to either agent alone |
| [17904110](https://pubmed.ncbi.nlm.nih.gov/17904110/) | 2007 | Animal Study | Brain Research | CCBs with antioxidative properties (including Amlodipine) prevent neuronal damage in focal ischaemia in rats; antioxidant mechanism implicated |
| [17070425](https://pubmed.ncbi.nlm.nih.gov/17070425/) | 2006 | Animal Study | Am J Hypertension | Amlodipine reduces stroke size after focal brain ischaemia in apolipoprotein E-deficient mice; L-type calcium channel blockade confirmed as mechanism |
| [21276424](https://pubmed.ncbi.nlm.nih.gov/21276424/) | 2011 | Animal Study | Brain Research | Combined Amlodipine + atorvastatin protection against ischaemic stroke in Zucker rats: infarct volume reduction and immune cell infiltration data |

---

## Safety Considerations

**Key safety signals identified from literature review:**

- **Angioedema**: PMID 19299323 documents probable Amlodipine-induced angioedema in a thalamic haemorrhagic stroke patient. While angioedema is more classically associated with ACE inhibitors, it has been reported with CCBs. Active monitoring is warranted in post-ICH patients.
- **Not for acute ICH blood pressure management**: Amlodipine's oral route and slow onset make it unsuitable for the acute phase of ICH, where rapid and titratable BP control is required (intravenous agents such as labetalol or nicardipine are preferred acutely). Amlodipine's role is exclusively in chronic secondary prevention.
- **Pulmonary hypertension**: Amlodipine is relatively contraindicated in WHO Group 3 and Group 5 pulmonary hypertension (Predictions 2 and 3 in this pack). Systemic vasodilation can worsen ventilation-perfusion mismatch. These two indications should not be pursued.
- **Drug interactions**: No DDI data was retrieved in this evidence pack. Full drug interaction review is required before clinical use.

Full prescribing information (HSA-registered label or international equivalent such as FDA label or EMA SmPC) must be consulted for complete warnings, contraindications, and drug interactions prior to any clinical decision.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TRIDENT Phase 3 RCT (n=1,671, completed) provides Level 2 evidence supporting CCB-inclusive intensive blood pressure-lowering therapy for ICH secondary prevention. Combined with CASE-J direct comparative data on Amlodipine in high-risk hypertensive patients with cerebrovascular endpoints, and a mechanistically coherent rationale (BP reduction targeting the primary driver of ICH recurrence), intracerebral haemorrhage secondary prevention is the most actionable repurposing candidate in this Evidence Pack.

**To proceed, the following is needed:**
- Confirm TRIDENT final efficacy results and identify whether Amlodipine specifically was the CCB used in the fixed-dose triple combination
- Obtain full Amlodipine prescribing information (via HSA or FDA/EMA label) to complete safety profiling (Key Warnings, Contraindications, DDI)
- Assess HSA registration pathway and feasibility for Singapore market (currently 0 active registrations)
- Conduct population-specific analysis for Asian/Singaporean ICH patient populations, including ethnicity-related pharmacokinetic considerations
- Develop safety monitoring plan including: angioedema surveillance, guidance on acute vs. chronic-phase usage, and BP target protocol (SBP < 130 mmHg)
- Evaluate **cerebral artery occlusion** as a secondary research question: 5 consistent animal studies (L3) demonstrate neuroprotection via calcium overload blockade and antioxidant mechanisms — a Phase 2 proof-of-concept human study would be the logical next step