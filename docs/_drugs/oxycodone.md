---
layout: default
title: Oxycodone
parent: 僅模型預測 (L5)
nav_order: 742
evidence_level: L5
indication_count: 10
---

# Oxycodone
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

# Oxycodone: From Pain Management to Restless Legs Syndrome

*Note: TxGNN's #1-ranked prediction ("methemoglobinemia") is explicitly flagged in the evidence pack as likely model noise/false-positive — the rationale states μ-opioid agonism has no known link to hemoglobin oxidation. This report instead focuses on the #2-ranked candidate, **Restless Legs Syndrome (RLS)**, which is the only prediction in this evidence pack with substantive clinical and literature support.*

## One-Sentence Summary

> Oxycodone is a semi-synthetic μ-opioid receptor agonist used globally for moderate-to-severe pain management.
> The TxGNN model predicts it may be effective for **Restless Legs Syndrome**,
> with **1 completed Phase 3 RCT** and **20 supporting publications** currently backing this direction —
> notably, a prolonged-release oxycodone/naloxone combination is already approved in parts of Europe as second-line therapy for severe refractory RLS.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate-to-severe pain (opioid analgesic; no Singapore-specific approved indication text available in this dataset) |
| Predicted New Indication | Restless Legs Syndrome |
| TxGNN Prediction Score | 90.35% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is not available in the evidence pack (MOA field is a data gap). Based on well-established pharmacology, Oxycodone is a μ-opioid receptor agonist used for analgesia. The proposed mechanistic link for RLS is that the pathology of RLS involves relative hypofunction of the endogenous opioid system alongside central dopaminergic and sensorimotor circuit dysregulation — opioid receptor agonists are known to relieve the sensory discomfort and urge-to-move symptoms of RLS.

This is not a novel hypothesis generated purely from graph structure: a prolonged-release oxycodone/naloxone (OXN PR) combination has already been approved in several European countries as a second-line/third-line treatment for severe idiopathic RLS in patients who fail or cannot tolerate dopaminergic agents (pramipexole, ropinirole, rotigotine) or α2δ ligands (gabapentin, pregabalin). The TxGNN prediction therefore reflects an established, clinically validated repurposing pathway rather than an untested signal, which is consistent with its high evidence level (L1) relative to the other candidates in this evidence pack (most of which are L4–L5 with weak or contradictory mechanistic rationale).

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01112644](https://clinicaltrials.gov/study/NCT01112644) | Phase 3 | Completed | 205 | Randomized, double-blind, placebo-controlled, multicenter trial demonstrating superior efficacy of prolonged-release oxycodone/naloxone (OXN PR) vs. placebo in improving RLS symptom severity in moderate-to-severe idiopathic RLS with daytime symptoms. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39324694](https://pubmed.ncbi.nlm.nih.gov/39324694/) | 2025 | Guideline | J Clin Sleep Med | AASM clinical practice guideline for treatment of RLS/PLMD in adults and pediatric patients. |
| [26966363](https://pubmed.ncbi.nlm.nih.gov/26966363/) | 2016 | Case series/Review | Neuropsychiatric Disease and Treatment | Reviews role of prolonged-release oxycodone-naloxone specifically in intractable RLS. |
| [26135898](https://pubmed.ncbi.nlm.nih.gov/26135898/) | 2015 | Review | CNS Drugs | Dedicated review of oxycodone/naloxone PR (Targin/Targiniq), approved in Europe for second-line treatment of severe refractory RLS after dopaminergic failure. |
| [35026088](https://pubmed.ncbi.nlm.nih.gov/35026088/) | 2022 | Review/Commentary | Tidsskrift for den Norske Laegeforening | Commentary specifically addressing "Oxycodone to treat restless legs syndrome?" |
| [29756335](https://pubmed.ncbi.nlm.nih.gov/29756335/) | 2018 | Evidence-based review | Movement Disorders | Updated evidence-based review noting oxycodone/naloxone has accrued sufficient data to be considered efficacious for RLS. |
| [27355187](https://pubmed.ncbi.nlm.nih.gov/27355187/) | 2016 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Systematic review of opioids (including oxycodone) for RLS treatment. |
| [30244828](https://pubmed.ncbi.nlm.nih.gov/30244828/) | 2018 | Review | The Lancet Neurology | Comorbidities, treatment, and pathophysiology overview of RLS, covering opioid therapy positioning. |
| [27964861](https://pubmed.ncbi.nlm.nih.gov/27964861/) | 2017 | Review | Sleep Medicine | Discusses mechanisms of opioid action (incl. oxycodone) in relieving RLS sensory and motor symptoms. |
| [33985652](https://pubmed.ncbi.nlm.nih.gov/33985652/) | 2021 | Review | Sleep Medicine Clinics | Notes opioids such as oxycodone extended-release with naloxone as approved second-line RLS treatment in Europe. |
| [27310338](https://pubmed.ncbi.nlm.nih.gov/27310338/) | 2016 | Review | Expert Opinion on Drug Metabolism & Toxicology | Pharmacological and clinical aspects of opioids, including oxycodone, in RLS treatment. |

## Singapore Market Information

Oxycodone currently has no marketing authorization registered in this dataset (0 authorizations, market status: Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack; DDI query returned no results.)

As a general class consideration, oxycodone is a controlled opioid substance and — independent of any RLS-specific data gap — carries well-established class-wide risks (respiratory depression, dependence/abuse potential, sedation) that must be assessed before any indication expansion.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT and a consistent body of literature (including an AASM guideline and a Cochrane systematic review) support oxycodone/naloxone PR's efficacy in severe refractory RLS, and this combination is already approved for this use in parts of Europe — this is evidence-backed repurposing, not a speculative model signal. However, Oxycodone is currently unregistered in Singapore and lacks local safety documentation, so guardrails are required before any local development.

**To proceed, the following is needed:**
- TFDA/HSA package insert data — key warnings and contraindications (currently blocking, per data gap DG001)
- Confirmed mechanism-of-action documentation from DrugBank (data gap DG002)
- Confirmation of local availability of the prolonged-release oxycodone/naloxone (OXN PR) formulation specifically, since plain oxycodone alone was not the studied product
- Drug-drug interaction data (current query returned no results)
- Opioid-specific risk mitigation/monitoring plan (abuse, dependence, respiratory depression) given controlled-substance status

*Other candidates in this evidence pack (methemoglobinemia, myofascial pain syndrome, common cold, headache disorder, tendinitis, and several rare hematologic/myositis conditions) were assessed at L3–L5 evidence with Hold recommendations due to absent or contradictory mechanistic support, and are not pursued further at this time.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

