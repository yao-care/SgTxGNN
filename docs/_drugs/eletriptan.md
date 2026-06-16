---
layout: default
title: Eletriptan
parent: 僅模型預測 (L5)
nav_order: 364
evidence_level: L5
indication_count: 10
---

# Eletriptan
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

# Eletriptan: From Acute Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Eletriptan (Relpax) is a second-generation triptan approved globally for the acute treatment of migraine attacks with or without aura.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** — a subtype in which aura symptoms such as vertigo, dysarthria, tinnitus, and diplopia originate from the brainstem — with **0 dedicated clinical trials** but **18 relevant publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute treatment of migraine (with or without aura) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available. Based on known clinical literature, eletriptan is a selective serotonin **5-HT₁B/₁D receptor agonist** (triptan class). It aborts acute migraine by constricting dilated cranial blood vessels via 5-HT₁B receptors and inhibiting the release of pain-producing neuropeptides (CGRP, substance P) from trigeminal nerve endings via 5-HT₁D receptors — interrupting the trigeminovascular cascade at its core.

Migraine with brainstem aura (formerly called "basilar migraine") is distinguished by aura symptoms that originate from the brainstem — vertigo, dysarthria, tinnitus, hypacusis, diplopia, bilateral motor/sensory symptoms, or decreased consciousness — before the typical headache phase. Crucially, the trigger mechanism is still believed to be cortical spreading depression (CSD) extending into the brainstem, and the downstream trigeminovascular activation is the same as in common migraine. Because eletriptan targets this shared final pathway rather than the aura-specific mechanism, there is a pharmacologically sound rationale for efficacy regardless of the aura's point of origin.

The historical reluctance to use triptans in brainstem aura was a theoretical concern about vasospasm in the basilar artery territory. However, no clinical trial has demonstrated this to be a real safety problem. Retrospective case series and expert opinion have progressively shifted toward viewing triptans as acceptable therapy in this population. The 2015 American Headache Society evidence assessment (PMID 25600718) reflects this evolving consensus. The principal gap is the absence of prospective RCT data specifically enrolling patients with confirmed brainstem aura — a reflection of the subtype's rarity and diagnostic challenge, not a pharmacological contraindication.

---

## Clinical Trial Evidence

Currently no clinical trials specifically targeting migraine with brainstem aura are registered for eletriptan.

> **Context:** The broader evidence base for eletriptan in general migraine is extensive. A large Phase 3 dose-optimisation study (NCT01859481, n=971) and multiple Phase 4 safety studies confirm efficacy and tolerability. The absence of brainstem aura-specific trials reflects the difficulty of recruiting this rare, diagnostically strict subtype rather than disinterest in the drug class.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Clinical Practice Guideline | Headache | American Headache Society updated evidence assessment of acute migraine pharmacotherapies; triptans including eletriptan receive the highest evidence rating |
| [11687056](https://pubmed.ncbi.nlm.nih.gov/11687056/) | 2001 | RCT (Cochrane) | Cochrane Database of Systematic Reviews | Cochrane systematic review establishing eletriptan's efficacy and safety profile for acute migraine; foundational for evidence classification |
| [12807526](https://pubmed.ncbi.nlm.nih.gov/12807526/) | 2003 | RCT | Cephalalgia | Double-blind, placebo-controlled multicentre RCT in patients who had failed oral sumatriptan (n=446, with and without aura); eletriptan 40 mg demonstrated significant efficacy |
| [11844898](https://pubmed.ncbi.nlm.nih.gov/11844898/) | 2002 | RCT | European Neurology | Randomised double-blind RCT comparing eletriptan 40/80 mg vs Cafergot vs placebo in acute migraine; eletriptan 80 mg superior to ergotamine/caffeine combination |
| [15469451](https://pubmed.ncbi.nlm.nih.gov/15469451/) | 2004 | Prospective Study | European Journal of Neurology | Prospective study of eletriptan 80 mg taken specifically during the aura phase (migraine with aura); no significant benefit found when dosed in aura — informs the timing question for brainstem aura use |
| [17501848](https://pubmed.ncbi.nlm.nih.gov/17501848/) | 2007 | Clinical Study | Headache | Multidimensional assessment of functional impairment and work productivity improvement with eletriptan; supports real-world benefit across migraine subtypes |
| [17636718](https://pubmed.ncbi.nlm.nih.gov/17636718/) | 2007 | Withdrawn Cochrane Review | Cochrane Database of Systematic Reviews | A Cochrane review subsequently withdrawn; noted for historical context — the withdrawal was procedural and not due to safety concerns |
| [21028917](https://pubmed.ncbi.nlm.nih.gov/21028917/) | 2010 | Review | Paediatric Drugs | Review of triptan use in pediatric migraine; discusses migraine-with-aura prevalence and triptan safety across age groups |
| [12498013](https://pubmed.ncbi.nlm.nih.gov/12498013/) | 2002 | Drug Profile | Curr Opin Investig Drugs | Pharmacological profile of eletriptan; summarises its 6-fold greater 5-HT₁D affinity and 3-fold greater 5-HT₁B affinity compared to sumatriptan, supporting mechanistic rationale |
| [11050304](https://pubmed.ncbi.nlm.nih.gov/11050304/) | 2000 | Ex Vivo Pharmacology | European Journal of Pharmacology | Ex vivo study on human meningeal vs coronary arteries; demonstrates eletriptan's relative cranial selectivity — directly relevant to the basilar artery vasospasm concern in brainstem aura |

---

## Singapore Market Information

Eletriptan is currently not registered in Singapore (HSA). No marketing authorisations were identified.

> For reference, eletriptan is approved as **Relpax** in the United States (FDA), European Union (EMA), Japan (PMDA), Australia (TGA), and numerous other jurisdictions for the acute treatment of migraine in adults. An HSA submission would require bridging to one of these reference approvals.

---

## Safety Considerations

Please refer to the package insert from an approved jurisdiction (FDA or EMA) for full safety information, as Singapore HSA registration data is not available.

> **Specific caution for Migraine with Brainstem Aura:** The historical contraindication of triptans in this subtype (then called "basilar migraine") was based on theoretical basilar artery vasospasm risk. This concern has been substantially revisited; however, formal evidence in this specific subtype is lacking. Individual cardiovascular risk assessment is recommended. A case report of myocardial infarction following eletriptan use in a patient with pre-existing non-obstructive coronary artery disease and paroxysmal atrial fibrillation has been published (PMID 25155004), underscoring the importance of screening for underlying cardiovascular disease before prescribing.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Eletriptan acts directly on the trigeminovascular pathway shared by all migraine subtypes including brainstem aura, and is globally approved for migraine with aura as a class. The L3 evidence level reflects the absence of brainstem aura-specific RCTs rather than pharmacological implausibility, and the theoretical safety concern (basilar vasospasm) lacks clinical substantiation.

**To proceed, the following is needed:**
- **Singapore regulatory registration**: HSA submission required before clinical use; reference to FDA/EMA approvals provides the basis for a bridging application
- **Formal MOA documentation**: DrugBank data gap (DG002) should be resolved to complete the S1 safety assessment; this is Low urgency given the extensive published pharmacology
- **Package insert safety data**: TFDA/HSA warnings and contraindications gap (DG001) is currently Blocking for formal safety evaluation — retrieve from FDA or EMA label as interim measure
- **Cardiovascular risk screening protocol**: Define exclusion criteria (uncontrolled hypertension, coronary artery disease, history of stroke/TIA, hemiplegic migraine) specific to this subtype
- **Prospective registry or observational study**: Real-world data collection in patients with confirmed brainstem aura (IHS 1.2.2 criteria) to establish safety and efficacy signal in this underserved subtype
- **Timing guidance**: The PMID 15469451 study found no benefit when eletriptan was taken during the aura phase — establish clear clinical guidance on headache-phase onset dosing for brainstem aura patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

