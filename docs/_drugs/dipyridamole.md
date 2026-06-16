---
layout: default
title: Dipyridamole
parent: 僅模型預測 (L5)
nav_order: 335
evidence_level: L5
indication_count: 10
---

# Dipyridamole
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

The txgnn-pipeline skill is for model training and deployment, not report generation — the system prompt already defines the full report format. I'll proceed to generate the report now.

---

# Dipyridamole: From Antiplatelet/Vasodilator Therapy to Stroke Disorder

## One-Sentence Summary

Dipyridamole is an antiplatelet and vasodilatory drug used globally as a cardiac pharmacological stress agent and, in combination with aspirin (Aggrenox), for secondary prevention of cerebrovascular events — though it is currently not registered in Singapore.
The TxGNN model predicts it may be effective for **Stroke Disorder**,
with **31 clinical trials** and **18 publications** currently supporting this direction, including landmark Phase 3/4 RCTs such as ESPRIT (n=4,500) and PRoFESS (n=20,332) alongside multiple Cochrane systematic reviews providing Level 1 evidence.

> **⚠️ Note on Prediction Ranking**: The TxGNN top prediction (rank 1) was **Prinzmetal angina** (99.99%). However, mechanistic and clinical evidence indicates this represents a **contraindication signal**, not a therapeutic target — dipyridamole can provoke coronary vasospasm in Prinzmetal angina patients and is used as a pharmacological stressor to *diagnose* the condition. This report therefore focuses on **Stroke Disorder (rank 2)** as the highest clinically actionable positive prediction. The Prinzmetal angina signal is addressed in the Safety section.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Antiplatelet therapy / Cardiac pharmacological stress testing (global; not registered in Singapore) |
| Predicted New Indication | Stroke Disorder |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Dipyridamole exerts dual antiplatelet and vasodilatory effects through two complementary mechanisms. First, it inhibits phosphodiesterase (PDE) enzymes in platelets, elevating intracellular cAMP and cGMP concentrations, which reversibly inhibits platelet activation and aggregation. Second, it blocks adenosine reuptake by erythrocytes and vascular cells, raising extracellular adenosine levels to promote vasodilation and improve regional blood flow — including cerebral perfusion. Beyond these primary mechanisms, dipyridamole also demonstrates antioxidant properties and anti-inflammatory activity, which may contribute neuroprotective benefits in the setting of acute ischemic stroke (PMID 20955428; PMID 25697566).

Ischemic stroke is predominantly driven by arterial thromboembolism and in-situ atherothrombosis, where platelet aggregation is central to clot formation. Dipyridamole's antiplatelet mechanism directly addresses this pathology, while its adenosine-mediated vasodilation may additionally improve perfusion in ischemic penumbra zones — the area of brain tissue at risk but potentially salvageable after stroke onset. The combination of aspirin and extended-release dipyridamole (Aggrenox) has been FDA-approved since 1999 specifically for reducing the risk of recurrent ischemic stroke.

The prediction is strongly supported by decades of clinical trial evidence. ESPS-2 (PMID 8981292) first demonstrated that modified-release dipyridamole 400 mg/day alone or combined with aspirin significantly reduced stroke recurrence versus placebo. The ESPRIT trial (n=4,500) subsequently confirmed the superiority of aspirin + dipyridamole over aspirin alone after cerebral ischemia of arterial origin. Multiple Cochrane systematic reviews (PMID 12535415; 16625549; 17636684) and individual patient data meta-analyses (PMID 15569877; 23871093) corroborate these findings. The TxGNN prediction therefore confirms and validates an existing clinically proven use rather than proposing a purely experimental indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00161070](https://clinicaltrials.gov/study/NCT00161070) | Phase 4 | Completed | 4,500 | **ESPRIT**: Aspirin + dipyridamole vs aspirin alone after cerebral ischemia of arterial origin; foundational RCT establishing combination superiority for stroke secondary prevention |
| [NCT00153062](https://clinicaltrials.gov/study/NCT00153062) | Phase 4 | Completed | 20,332 | **PRoFESS**: Extended-release dipyridamole + aspirin (Aggrenox) vs clopidogrel ± telmisartan for prevention of second stroke in recently-stroked high-risk patients |
| [NCT00311402](https://clinicaltrials.gov/study/NCT00311402) | Phase 3 | Completed | 1,295 | **JASAP**: Aggrenox twice daily vs aspirin 81mg once daily for recurrent brain infarction prevention; key evidence in Japanese/Asian population |
| [NCT00238667](https://clinicaltrials.gov/study/NCT00238667) | Phase 3 | Completed | 250 | **CADISS**: Antiplatelet therapy (including dipyridamole options) vs anticoagulation in acute cervical artery dissection-associated stroke |
| [NCT00562588](https://clinicaltrials.gov/study/NCT00562588) | Phase 4 | Completed | 551 | **EARLY**: Aggrenox initiated within 24 hours of stroke onset vs delayed 7-day ASA pretreatment; evaluating optimal timing of dipyridamole initiation |
| [NCT01295567](https://clinicaltrials.gov/study/NCT01295567) | Phase 4 | Completed | 95 | Dipyridamole pretreatment for protection against ischemia-reperfusion injury in elective CABG patients; mechanistic validation of cardioprotective effects |
| [NCT01661322](https://clinicaltrials.gov/study/NCT01661322) | Phase 3 | Terminated | 3,096 | Triple antiplatelet therapy (aspirin + clopidogrel + dipyridamole) vs aspirin + dipyridamole in high-risk recent TIA/ischemic stroke; terminated early, but substantial Phase 3 dataset |
| [NCT00738894](https://clinicaltrials.gov/study/NCT00738894) | N/A | Completed | 664 | **REDUCE**: PFO closure + antiplatelet management (including dipyridamole option) vs antiplatelet management alone for recurrent stroke/TIA in PFO patients |
| [NCT00465270](https://clinicaltrials.gov/study/NCT00465270) | N/A | Completed | 980 | **RESPECT**: PFO closure vs standard-of-care antiplatelet treatment (including aspirin + dipyridamole arm) for recurrent embolic stroke prevention |
| [NCT02630862](https://clinicaltrials.gov/study/NCT02630862) | N/A | Completed | 240 | Aspirin + dipyridamole antioxidant and antithrombotic effects in carotid revascularization patients; approved in Italy for secondary cerebral embolism prevention |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11786451](https://pubmed.ncbi.nlm.nih.gov/11786451/) | 2002 | Meta-analysis | BMJ | Antithrombotic Trialists' Collaboration: antiplatelet regimens including dipyridamole combinations significantly reduce death, MI, and stroke in high-risk vascular patients |
| [12535415](https://pubmed.ncbi.nlm.nih.gov/12535415/) | 2003 | Cochrane Review | Cochrane Database | Dipyridamole for stroke and vascular event prevention: dipyridamole added to aspirin yields significant additional risk reduction over aspirin alone |
| [15569877](https://pubmed.ncbi.nlm.nih.gov/15569877/) | 2005 | Meta-analysis | Stroke | Individual patient data meta-analysis from multiple RCTs: dipyridamole ± aspirin reduces recurrent ischemic stroke and other vascular events after TIA/stroke |
| [16625549](https://pubmed.ncbi.nlm.nih.gov/16625549/) | 2006 | Cochrane Review | Cochrane Database | Updated Cochrane review: aspirin + dipyridamole associated with 22% relative risk reduction vs aspirin alone for cerebrovascular events |
| [17636684](https://pubmed.ncbi.nlm.nih.gov/17636684/) | 2007 | Cochrane Review | Cochrane Database | Second Cochrane update confirming dipyridamole efficacy; patients with limited cerebral ischaemia face 4–11% annual vascular event risk, which combination therapy substantially reduces |
| [23871093](https://pubmed.ncbi.nlm.nih.gov/23871093/) | 2013 | Meta-analysis | J Neurological Sciences | Meta-analysis of RCTs: aspirin + dipyridamole significantly reduces stroke recurrence compared to aspirin alone after TIA or stroke; recommended in American guidelines |
| [8981292](https://pubmed.ncbi.nlm.nih.gov/8981292/) | 1996 | RCT | J Neurological Sciences | **ESPS-2**: Modified-release dipyridamole 400 mg/day ± aspirin significantly reduces stroke and stroke/death vs placebo; seminal trial establishing dipyridamole efficacy |
| [30649687](https://pubmed.ncbi.nlm.nih.gov/30649687/) | 2019 | Cohort | CNS Drugs | Nationwide case-control: dipyridamole + clopidogrel effective for secondary stroke prevention in aspirin-intolerant patients following acute myocardial infarction |
| [20955428](https://pubmed.ncbi.nlm.nih.gov/20955428/) | 2010 | Review | Ann NY Acad Sci | Dipyridamole in acute stroke: anti-inflammatory and neuroprotective mechanisms beyond antiplatelet activity; rationale for earlier initiation in acute settings |
| [18174451](https://pubmed.ncbi.nlm.nih.gov/18174451/) | 2008 | Review | Arterioscler Thromb Vasc Biol | Translational therapeutics of dipyridamole: PDE inhibition raises cAMP/cGMP in platelets; potentiates endothelial NO effects; comprehensive mechanistic review |

---

## Singapore Market Information

Dipyridamole is currently **not registered in Singapore**. There are no Health Sciences Authority (HSA) product authorizations on record (total licenses = 0).

For reference, the aspirin + dipyridamole combination (Aggrenox / Asasantin Retard) is approved in over 30 markets including:
- United States (FDA, 1999) — stroke secondary prevention
- European Union (EMA) — stroke secondary prevention
- Japan (PMDA) — recurrent brain infarction prevention (JASAP data)

A new HSA submission would be required to bring this product to the Singapore market.

---

## Safety Considerations

No Singapore HSA prescribing information is available. Safety data below is derived from published literature and general pharmacological knowledge.

**Critical Safety Signal — Prinzmetal (Variant) Angina:**
The TxGNN model's highest-ranked prediction (rank 1, 99.99%) was Prinzmetal angina, but mechanistic and clinical evidence identifies this as a **contraindication signal**. Dipyridamole blocks adenosine reuptake, causing extracellular adenosine accumulation; in patients with vasospastic coronary disease, this can paradoxically trigger coronary artery spasm and induce ischemia (PMID 3421166; PMID 633593). Dipyridamole is clinically used as a pharmacological stress agent to *provoke and diagnose* variant angina — not as a treatment. **Dipyridamole should be avoided in patients with Prinzmetal angina or coronary vasospasm.**

**Drug Interaction — Metformin (Pharmacokinetic):**
A Phase 4 study (NCT01613755, n=18) found that dipyridamole inhibits the equilibrative nucleoside transporter hENT4, potentially reducing metformin gastrointestinal absorption. This is clinically relevant as diabetic patients post-TIA or stroke are frequently co-prescribed both agents.

Please refer to the Aggrenox or Persantin package insert for complete prescribing information, including:
- Increased bleeding risk with concurrent anticoagulant or other antiplatelet use
- Headache (common; vasodilatory mechanism, typically transient)
- Bronchoconstriction risk in patients with severe asthma or COPD (adenosine-mediated)
- Hypotension risk in patients with hemodynamic instability

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Aspirin + dipyridamole (Aggrenox) is an FDA-approved, guideline-endorsed therapy for secondary prevention of ischemic stroke, supported by L1 evidence from multiple Phase 3/4 RCTs (ESPRIT n=4,500; PRoFESS n=20,332), Cochrane systematic reviews, and meta-analyses. The TxGNN prediction for stroke disorder confirms this established clinical utility. The key barrier to Singapore use is the absence of local market registration, not a lack of clinical evidence. However, the Prinzmetal angina safety signal (rank 1 prediction) underscores that careful patient selection is essential.

**To proceed, the following is needed:**

- **HSA registration pathway**: Determine whether an existing approved combination product (Aggrenox) or monotherapy (Persantin) can be submitted through HSA's abridged or full registration pathway; evaluate whether a local bioequivalence study is required
- **Complete safety data retrieval**: Obtain and review the FDA/EMA-approved package inserts for all contraindications, warnings, and drug interactions, particularly for vasospastic conditions (Prinzmetal angina) and bronchospasm-prone patients
- **Metformin DDI monitoring protocol**: Establish clinical guidance for patients co-prescribed dipyridamole and metformin, including possible metformin dose adjustment or enhanced glycaemic monitoring
- **Patient selection criteria**: Define contraindication list before any formulary addition — explicitly excluding patients with known coronary vasospasm, severe hypotension, or active bleeding disorders
- **Alignment with local neurology practice**: Cross-reference with Singapore Neurological Association and Ministry of Health clinical practice guidelines for antiplatelet use in ischemic stroke/TIA secondary prevention
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

