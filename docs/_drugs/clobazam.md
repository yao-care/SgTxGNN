---
layout: default
title: Clobazam
parent: 僅模型預測 (L5)
nav_order: 238
evidence_level: L5
indication_count: 10
---

# Clobazam
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

# Clobazam: From Epilepsy (Lennox-Gastaut Syndrome) to Febrile Infection-Related Epilepsy Syndrome

## One-Sentence Summary

Clobazam is a 1,5-benzodiazepine antiepileptic drug internationally approved for adjunctive treatment of seizures in Lennox-Gastaut syndrome (LGS), though it is not currently registered in Singapore.
The TxGNN model's top prediction is **febrile infection-related epilepsy syndrome (FIRES)** — a catastrophic form of new-onset refractory status epilepticus — with **no registered clinical trials** and **2 case-level publications** directly supporting this specific application.
This report is part of a 10-indication multi-prediction analysis; the strongest clinical evidence within this dataset (L1, FDA-approved) relates to **childhood-onset epileptic encephalopathy (LGS)**, where clobazam is already an established treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lennox-Gastaut syndrome; epilepsy adjunctive therapy (FDA approved 2011; not registered in Singapore) |
| Predicted New Indication | Febrile Infection-Related Epilepsy Syndrome (FIRES) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 (case reports only; no clinical trials) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Clobazam is a 1,5-benzodiazepine — structurally distinct from the more familiar 1,4-benzodiazepines such as diazepam and clonazepam. Detailed mechanism of action data from DrugBank was not available in this Evidence Pack (Data Gap DG002). Based on established pharmacology, clobazam acts as a positive allosteric modulator of GABA-A receptors, enhancing chloride ion channel opening frequency and broadly suppressing neuronal excitability across multiple seizure types. Its 1,5-isomer configuration confers a relatively more favorable sedation and cognitive side-effect profile compared to 1,4-benzodiazepines — a pharmacologically meaningful distinction when managing critically ill FIRES patients who are already heavily sedated.

FIRES is a rare, life-threatening epilepsy syndrome occurring predominantly in previously healthy children: a febrile illness triggers new-onset, medically refractory status epilepticus that fails conventional antiepileptics, necessitating high-dose IV anesthetic agents (midazolam, barbiturates/thiopental) for seizure suppression. The core mechanistic rationale for clobazam in FIRES is its potential as an **oral GABA-A agonist during the IV sedation weaning phase** — one of the most clinically challenging transitions in FIRES management. A patient who has been maintained on IV thiopental or midazolam for weeks requires a pharmacological bridge to oral therapy, and clobazam's GABA-A mechanism makes it a theoretically appropriate candidate.

The key piece of direct evidence is a 2025 case report (PMID 39958143): a 13-year-old boy with FIRES who developed thiopental dependency was successfully weaned using perampanel and ultimately achieved seizure freedom maintained on **clobazam + levetiracetam**. This directly places clobazam in a real FIRES treatment pathway. Supportively, a 2022 case series (PMID 35770765) demonstrated enteral lorazepam — another benzodiazepine — as an effective weaning substitute for midazolam in FIRES patients, validating the broader concept of enteral BZD substitution in this syndrome.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Clobazam in febrile infection-related epilepsy syndrome (FIRES).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Case Report | Cureus | 13-year-old FIRES patient with thiopental dependency; perampanel facilitated barbiturate weaning; seizure freedom achieved and maintained on clobazam + levetiracetam — direct evidence of clobazam use in FIRES |
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Case Series | Epileptic Disorders | Enteral lorazepam as effective weaning substitute for midazolam-dependent FIRES patients; demonstrates the clinical feasibility of enteral BZD substitution in FIRES management |

---

## Prediction Landscape Summary (All 10 Predicted Indications)

This is a multi-indication analysis (candidate ID: TW-DB00349-multi). All TxGNN predictions are presented below, ordered by rank:

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|------------|---------------|---------|
| 1 | Febrile infection-related epilepsy syndrome (FIRES) | 99.82% | L4 | Research Question |
| 2 | Perioral myoclonia with absences | 99.79% | L5 | Hold |
| 3 | Cryptogenic late-onset epileptic spasms | 99.77% | L5 | Hold |
| 4 | Atypical childhood epilepsy with centrotemporal spikes | 99.77% | L3 | Research Question |
| 5 | Photosensitive occipital lobe epilepsy | 99.77% | L4 | Hold |
| **6** | **Childhood onset epileptic encephalopathy (LGS)** ★ | **99.59%** | **L1** | **Proceed with Guardrails** |
| 7 | Benign occipital epilepsy | 99.58% | L2 | Proceed with Guardrails |
| 8 | Early-onset epileptic encephalopathy due to GRIN2A mutation | 99.40% | L5 | Hold |
| 9 | Restless legs syndrome | 99.30% | L5 | Hold |
| 10 | Polymicrogyria with optic nerve hypoplasia | 99.09% | L5 | Hold |

★ **Highest-actionability signal in this analysis**: Childhood onset epileptic encephalopathy (primarily LGS) is backed by Phase 3 RCT data (CONTAIN trial), FDA approval (2011), and 20 supporting publications including Cochrane reviews, ILAE Task Force reports, and AAN/AES practice guidelines. This indication should be the primary near-term focus for any Singapore access pathway discussion.

---

## Singapore Market Information

Clobazam is not currently registered in Singapore with HSA. No licensed products or approved indications are on record. Clinicians seeking to use clobazam for patients in Singapore would need to access it through the HSA Special Access Route (SAR) for unregistered medicines or via a licensed importer.

---

## Safety Considerations

Please refer to the package insert for safety information. Detailed safety data — including HSA/TFDA warnings, contraindications, and drug-drug interactions — were not available in this Evidence Pack (Data Gaps DG001 and DG002). As a benzodiazepine-class antiepileptic, clinicians should be aware of the following class-level considerations:

- **Sedation and CNS depression**: Particularly relevant in the FIRES/ICU context where patients are already on multiple sedating agents
- **Tolerance and dependence**: Risk with prolonged use, especially in the chronic maintenance phase of epilepsy management
- **Respiratory depression**: Monitor closely when used in combination with other CNS depressants or during IV-to-oral sedation transitions

---

## Conclusion and Next Steps

**Decision: Hold (Research Question) — for FIRES (Top TxGNN Prediction)**

**Rationale:**
Evidence for clobazam specifically in FIRES is currently limited to one directly relevant case report (PMID 39958143, 2025), providing proof-of-concept but insufficient grounds for formal clinical deployment. The mechanistic basis is sound, but prospective data are entirely absent.

**High-priority parallel action — Childhood Onset Epileptic Encephalopathy (Rank 6, L1 evidence):**
The broader category of childhood-onset epileptic encephalopathy, particularly Lennox-Gastaut syndrome, has robust Phase 3 RCT support and FDA approval. This constitutes the strongest actionable signal from this multi-indication analysis and should be prioritized for Singapore access pathway exploration.

**To advance the FIRES research question, the following is needed:**

- Retrieve full MOA data from DrugBank API (remediate Data Gap DG002)
- Obtain HSA/TFDA prescribing information PDF to establish complete warnings, contraindications, and DDI profile (remediate Data Gap DG001)
- Conduct a systematic literature review on benzodiazepine use in FIRES/NORSE management protocols beyond the 2 identified publications
- Design a prospective observational study or multi-center case registry for FIRES patients receiving clobazam as oral maintenance therapy after IV sedation weaning
- Convene a multidisciplinary expert panel (pediatric neurology + pediatric critical care) to evaluate feasibility and protocol design

**For Childhood Onset Epileptic Encephalopathy (Proceed with Guardrails):**

- Initiate HSA Special Access Route (SAR) application targeting LGS in pediatric patients
- Benchmark against the 2025 comprehensive LGS treatment algorithm (PMID 39854828) and ILAE Task Force recommendations (PMID 26122601)
- Establish a pediatric safety monitoring protocol, including CBC, liver and renal function, behavioral adverse event tracking (reference: PMID 36194365)
- Review real-world pediatric tolerability data (PMID 35749975: large-cohort multicenter study of clobazam effectiveness in pediatric epilepsy)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

