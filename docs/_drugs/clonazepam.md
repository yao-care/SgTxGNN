---
layout: default
title: Clonazepam
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 10
---

# Clonazepam
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

# Clonazepam: From Epilepsy & Anxiety Disorders to Restless Legs Syndrome

## One-Sentence Summary

Clonazepam is a high-potency benzodiazepine used internationally for epileptic seizures (including status epilepticus), panic disorder, and movement-related sleep disorders, though it currently holds no Singapore market registration.
The TxGNN model predicts it may be effective for **Restless Legs Syndrome (RLS)**, with **0 registered clinical trials** but **20 publications** — including a Cochrane systematic review and an AASM clinical practice guideline — currently supporting this direction.
Evidence is rated at Level L3 (observational studies and systematic reviews), reflecting moderate but clinically meaningful support as a second-line therapy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Epilepsy, status epilepticus, and panic/anxiety disorders (internationally recognised; no Singapore HSA registration) |
| Predicted New Indication | Restless Legs Syndrome (RLS) |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L3 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrievable from the queried drug database. Based on known pharmacology, Clonazepam is a positive allosteric modulator of GABA-A receptors: it prolongs chloride ion channel opening, thereby enhancing inhibitory neurotransmission throughout the central nervous system. This broad CNS dampening effect underlies its utility across epilepsy, panic disorder, and movement-related sleep disturbances.

Restless Legs Syndrome is a sensorimotor disorder characterised by an irresistible urge to move the legs, worsening at rest and at night, frequently accompanied by Periodic Limb Movement Disorder (PLMD). While dopaminergic dysfunction is the primary driver, abnormal corticospinal hyperexcitability also plays a role. Clonazepam's GABA-A enhancement directly addresses this hyperexcitability component — suppressing the frequency of periodic limb movements during sleep and reducing corticospinal excitability — thereby improving nocturnal discomfort and sleep continuity.

Dopamine agonists (pramipexole, ropinirole) remain the recognised first-line treatment for RLS. However, Clonazepam is consistently described in treatment guidelines and systematic reviews as a second-line option, particularly for patients with comorbid PLMD or those who fail dopaminergic therapy. A 2001 placebo-controlled sleep laboratory study (PMID 11313161) directly demonstrated its acute efficacy. A 2024 retrospective analysis of 16,694 RLS patients found approximately 25% were treated with benzodiazepines (PMID 38708125), confirming substantial real-world use. The 2017 Cochrane review (PMID 28319266) and the 2025 AASM clinical practice guideline (PMID 39324694) both acknowledge clonazepam within the therapeutic landscape for RLS/PLMD.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Clonazepam in Restless Legs Syndrome.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39324694](https://pubmed.ncbi.nlm.nih.gov/39324694/) | 2025 | Clinical Practice Guideline | J Clin Sleep Med | AASM 2025 guideline for RLS and PLMD treatment in adults and paediatric patients; positions clonazepam within the evidence-based treatment framework |
| [28319266](https://pubmed.ncbi.nlm.nih.gov/28319266/) | 2017 | Cochrane Systematic Review | Cochrane Database Syst Rev | Systematic review of benzodiazepines (especially clonazepam) for RLS; confirms limited but real clinical benefit for sleep initiation and quality; notes prior AASM review found insufficient evidence for first-line use |
| [11313161](https://pubmed.ncbi.nlm.nih.gov/11313161/) | 2001 | Placebo-Controlled Sleep Study | Eur Neuropsychopharmacol | Direct placebo-controlled acute sleep laboratory study with 1 mg clonazepam in RLS/PLMD patients; significant improvement in objective and subjective sleep quality demonstrated |
| [38708125](https://pubmed.ncbi.nlm.nih.gov/38708125/) | 2024 | Historical Review | Tremor Other Hyperkinetic Mov | Identified 17 published articles on clonazepam use in RLS/PLMS; ~25% of 16,694 surveyed RLS patients were treated with benzodiazepines, confirming widespread real-world clinical use |
| [36692194](https://pubmed.ncbi.nlm.nih.gov/36692194/) | 2023 | Systematic Review & Meta-Analysis | J Clin Sleep Med | Meta-analysis of pharmacological responsiveness of periodic limb movements in RLS; assessed relative efficacy of benzodiazepines vs dopaminergic agents in suppressing PLMS |
| [31942156](https://pubmed.ncbi.nlm.nih.gov/31942156/) | 2019 | Randomised Open-Label Study | J Mid-Life Health | Prospective RCT comparing clonazepam vs nortriptyline in women >40 years with RLS; directly evaluated symptom rate, frequency, and severity with clonazepam |
| [18925578](https://pubmed.ncbi.nlm.nih.gov/18925578/) | 2008 | Evidence-Based Review (MDS Task Force) | Mov Disord | Movement Disorder Society systematic evidence review; classified clonazepam as "likely efficacious" for RLS based on available trial data |
| [24363103](https://pubmed.ncbi.nlm.nih.gov/24363103/) | 2014 | Treatment Review | Neurotherapeutics | Comprehensive RLS treatment review; describes clonazepam's role as an alternative/adjunctive option particularly for PLMD-predominant presentations |
| [17876423](https://pubmed.ncbi.nlm.nih.gov/17876423/) | 2007 | Expert Consensus | Arq Neuropsiquiatr | Brazilian RLS Study Group consensus on diagnosis and management; includes clonazepam in the treatment algorithm alongside dopaminergic agents |
| [6380197](https://pubmed.ncbi.nlm.nih.gov/6380197/) | 1984 | Randomised Double-Blind Crossover Trial | Acta Neurol Scand | Earliest RCT of clonazepam in RLS (n=6 patients); significant efficacy over placebo for subjective sleep quality and leg dysaesthesia; authors concluded clonazepam is safe and effective, warranting long-term confirmation |

---

## Singapore Market Information

Clonazepam is currently **not registered** in Singapore. No Health Sciences Authority (HSA) product licences are on record, and the drug is classified as not marketed in the Singapore regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clonazepam has a pharmacologically plausible mechanism for RLS (GABA-A enhancement reducing PLMD frequency and corticospinal hyperexcitability), is recognised as a second-line option in multiple international guidelines and systematic reviews, and has direct placebo-controlled clinical data dating back to 2001. However, it is not a first-line treatment, the evidence base does not reach L1/L2 standards for this specific indication, and meaningful safety guardrails are required given its dependence and tolerance profile.

**To proceed, the following is needed:**

- **Regulatory gap resolution**: Obtain Clonazepam package insert (TFDA or equivalent) to document official approved indications, key warnings, and contraindications — currently a blocking data gap
- **MOA documentation**: Retrieve formal mechanism of action data from DrugBank API (DB01068)
- **Dependence and tolerance monitoring plan**: Efficacy is reported to decline after 2–4 weeks of continuous use; a structured short-term use protocol (≤4 weeks) with a pre-specified tapering strategy is required to mitigate rebound RLS/insomnia on discontinuation
- **Augmentation risk assessment**: Evaluate interaction with concurrent dopaminergic therapy, as combined use may affect augmentation risk in long-term RLS management
- **Population-specific safeguards**: Elderly patients (fall risk from sedation), patients with obstructive sleep apnoea (respiratory depression risk), and those with a history of substance use disorder require explicit exclusion criteria or enhanced monitoring protocols
- **Drug interaction screening**: Formal assessment of interactions with CNS depressants, opioids, and anticonvulsants commonly co-prescribed in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

