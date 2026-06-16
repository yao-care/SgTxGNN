---
layout: default
title: Ketamine
parent: 僅模型預測 (L5)
nav_order: 510
evidence_level: L5
indication_count: 10
---

# Ketamine
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

# Ketamine: From Anesthesia/Procedural Sedation to Headache Disorder

## One-Sentence Summary

Ketamine is a dissociative anesthetic and potent NMDA receptor antagonist, clinically established for anesthesia induction, procedural sedation, and acute pain management worldwide.
The TxGNN model predicts it may be effective for **Headache Disorder** (including migraine, cluster headache, and chronic daily headache),
with **at least 3 high-grade directly relevant clinical trials** (including an ongoing Phase 3 multicentre RCT) and multiple supporting publications currently backing this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anesthesia induction and procedural sedation |
| Predicted New Indication | Headache Disorder |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ketamine is a non-competitive NMDA (N-methyl-D-aspartate) receptor antagonist that blocks glutamate-gated ion channels in the central nervous system. At sub-dissociative doses (typically 0.1–0.3 mg/kg IV), it produces potent analgesia without full dissociative effects, which makes it feasible for use in pain conditions outside of the operating room. Although detailed formal MOA data was not available in this evidence pack, the drug's core mechanism—NMDA blockade—is highly relevant to headache pathophysiology.

Headache disorders, especially migraine and cluster headache, are now understood to involve excessive glutamatergic signalling and NMDA receptor–mediated central sensitization at the trigeminal nucleus caudalis. Ketamine can interrupt this cascade through two complementary routes: (1) **direct suppression of cortical spreading depolarization (CSD)**, the electrophysiological substrate of migraine aura, as demonstrated in both animal models and a randomised intranasal study; and (2) **reversal of spinal wind-up and central sensitization**, which "resets" the chronically sensitized pain networks responsible for refractory or daily headache. This is mechanistically analogous to how ketamine is already used to treat other centrally sensitized pain states such as complex regional pain syndrome (CRPS) and fibromyalgia.

Multiple Phase 3 and Phase 4 randomised trials are either completed or actively recruiting for headache-specific indications. Notably, the ongoing **KetHead Study** (NCT05306899) is a multicentre Phase 3 RCT specifically designed to provide definitive evidence for IV ketamine in chronic daily headache. The 2025 American Headache Society (AHS) guideline update has already acknowledged ketamine as a consideration for parenteral headache management in emergency settings (PMID 41321235). Taken together, the mechanistic plausibility, breadth of clinical trial activity, and early guideline recognition make this a well-supported and actionable repurposing signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT05306899](https://clinicaltrials.gov/study/NCT05306899) | Phase 3 | Recruiting | 56 | KetHead Study: Multicentre placebo-controlled RCT of high-dose IV ketamine (1 mg/kg/h × 6 h) for chronic daily headache; aims to provide the highest-level direct evidence for this indication |
| [NCT04814381](https://clinicaltrials.gov/study/NCT04814381) | Phase 4 | Recruiting | 90 | RCT evaluating single infusion of ketamine combined with magnesium sulfate for refractory chronic cluster headache; based on positive case series showing NMDA antagonism can interrupt attack cycles |
| [NCT02697071](https://clinicaltrials.gov/study/NCT02697071) | N/A (RCT) | Completed | 34 | Randomised double-blind placebo-controlled trial of sub-dissociative ketamine for acute migraine-type headache in the ED; assessed pain score reduction and recurrence prevention |
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Phase 3 | Completed | 80 | THINK Trial: Single-blind RCT comparing intranasal sub-dissociative ketamine vs standard-of-care therapy for primary headache syndromes presenting to the ED |
| [NCT04179266](https://clinicaltrials.gov/study/NCT04179266) | Phase 1/2 | Completed | 23 | Proof-of-concept trial of intranasal ketamine aqueous spray for acute cluster headache attacks; demonstrated feasibility and safety of the non-IV route |
| [NCT06608277](https://clinicaltrials.gov/study/NCT06608277) | Phase 2 | Recruiting | 175 | Multicentre RCT comparing ketamine, stellate ganglion block, and their combination vs sham for traumatic brain injury–associated headache and PTSD; will provide comparative effectiveness data |
| [NCT02657031](https://clinicaltrials.gov/study/NCT02657031) | Phase 4 | Completed | 54 | CHECK Trial: Multicentre double-blind RCT comparing low-dose ketamine vs prochlorperazine (Compazine) for control of headache in ED patients |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Unknown | 60 | Sub-dissociative ketamine vs ketorolac for acute tension-type headache in the ED; evaluates NRS pain reduction as the primary endpoint |
| [NCT04860713](https://clinicaltrials.gov/study/NCT04860713) | Phase 4 | Completed | 5 | Exploratory trial of oral ketamine + aspirin vs rimegepant for acute headache in the ED; sample too small for definitive conclusions but demonstrates interest in oral formulation |
| [NCT06968624](https://clinicaltrials.gov/study/NCT06968624) | Phase 4 | Not Yet Recruiting | 50 | Single low-dose IV esketamine for postherpetic neuralgia with comorbid depression; relevant to the neuropathic pain–headache mechanistic overlap |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [35356451](https://pubmed.ncbi.nlm.nih.gov/35356451/) | 2022 | Retrospective Cohort | Frontiers in Neurology | Inpatient IV ketamine and lidocaine infusions for headache disorders; demonstrated clinically meaningful pain reduction with acceptable safety profile across multiple headache subtypes |
| [34919214](https://pubmed.ncbi.nlm.nih.gov/34919214/) | 2022 | Review | Drugs | Comprehensive review of pharmacotherapy for cluster headache; notes ketamine as an emerging option for drug-resistant chronic cluster headache, including combination with magnesium |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Review of Neurotherapeutics | Update on pharmacotherapy for trigeminal neuralgia; identifies ketamine alongside cannabinoids as a promising adjuvant or monotherapy option for craniofacial pain syndromes |
| [37421541](https://pubmed.ncbi.nlm.nih.gov/37421541/) | 2023 | Review | Current Pain and Headache Reports | Evidence-based review of CRPS; documents ketamine's mechanism of reversing central sensitization—a pathological process shared with refractory headache |
| [32189074](https://pubmed.ncbi.nlm.nih.gov/32189074/) | 2020 | Review | Current Neurology and Neuroscience Reports | Review of ED and inpatient headache management in adults; covers ketamine as a salvage option for status migrainosus and refractory primary headache |
| [32410204](https://pubmed.ncbi.nlm.nih.gov/32410204/) | 2020 | Review | Current Neurology and Neuroscience Reports | Review of ED and inpatient headache management in children and adolescents; discusses intranasal ketamine as an abortive migraine option in the paediatric setting |

---

## Singapore Market Information

Ketamine (DB01221) is currently **not registered** with the Health Sciences Authority (HSA) of Singapore. There are no active marketing authorisations on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No registered products found |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between ketamine's NMDA antagonism and headache pathophysiology is well-established, multiple Phase 3/4 RCTs specifically targeting headache disorders are completed or ongoing, and the 2025 AHS guideline has acknowledged its clinical relevance—collectively constituting L2-level evidence with a clear pathway toward L1.

**To proceed, the following is needed:**

- **Regulatory pathway clarification:** Ketamine is currently not registered in Singapore; an unregistered drug import or named-patient programme authorisation from HSA would be required for any clinical use.
- **HSA package insert procurement:** Safety data (warnings, contraindications, specific drug–drug interactions) must be retrieved from the approved package insert before any clinical risk assessment can be completed (Data Gap DG001).
- **MOA documentation:** Formal DrugBank MOA data should be retrieved to complete the mechanistic rationale section and support regulatory submissions (Data Gap DG002).
- **Results from KetHead Study (NCT05306899):** Awaiting completion in June 2026; these Phase 3 results will either elevate evidence to L1 or clarify the dose and patient-selection parameters.
- **Patient risk stratification protocol:** Given ketamine's known dissociative and abuse-potential profile, a patient selection and monitoring protocol (excluding psychiatric history, substance use disorder) must be developed before clinical implementation.
- **Formulation strategy:** Determine whether IV (inpatient) or intranasal (acute outpatient/ED) delivery is the primary target route, as regulatory and logistics requirements differ substantially.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

