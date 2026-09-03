---
layout: default
title: Midodrine
parent: 僅模型預測 (L5)
nav_order: 666
evidence_level: L5
indication_count: 10
---

# Midodrine
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

# Midodrine: From Orthostatic Hypotension to Broader Hypotensive Disorder Indications

> **Note on indication selection**: This Evidence Pack contains 10 TxGNN-predicted indications for Midodrine. The single highest-scoring prediction (*variably protease-sensitive prionopathy*, score 99.99%) has **zero supporting trials or literature** and is explicitly flagged in the pack's own rationale as "a pure model artifact with no known mechanistic or clinical link." The same is true for 8 of the other 9 candidates (all scored L4–L5, decision stage S0, recommendation "Hold"). Only **Hypotensive Disorder** (rank 4 by score, but the only candidate reaching evidence level **L1** / decision stage **S3**) is backed by substantive clinical trial and literature evidence, including trials that test Midodrine directly. This report therefore focuses on that indication as the actionable finding in the pack.

## One-Sentence Summary

Midodrine is a peripheral α1-adrenergic agonist prodrug whose original approved-use record is missing from the regulatory data on file (Data Gap), though published literature already documents its established role in orthostatic hypotension and secondary hypotensive disorders. The TxGNN model — and, more importantly, real-world trial evidence — supports extending this known pharmacology to a broader set of **Hypotensive Disorders**, including intradialytic hypotension, post-spinal-anesthesia hypotension, spinal-cord-injury-related hypotension, and hypotension in heart failure with reduced ejection fraction, with **9 clinical trials** and **19 publications** currently identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in regulatory record (Data Gap). Literature (PMID 2480881) documents established use in orthostatic hypotension and secondary hypotensive disorders. |
| Predicted New Indication | Hypotensive Disorder (intradialytic, perioperative, SCI-related, HFrEF-related) |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not populated in the drug record (Data Gap), but the evidence pack's own trial and literature sources establish that Midodrine is a prodrug metabolized to its active metabolite **desglymidodrine**, a peripherally selective **α1-adrenergic receptor agonist**. This mechanism produces direct vasoconstriction and blood pressure elevation — a pharmacological action that is already the drug's best-characterized effect (PMID 2480881, 1989 review of its "pharmacological properties and therapeutic use in orthostatic hypotension and secondary hypotensive disorders").

The predicted new indication, "Hypotensive Disorder," is not a mechanistically distant repurposing candidate — it is a **direct extension of Midodrine's known pharmacology** into related clinical contexts: intradialytic hypotension in critically ill patients with acute kidney injury (NCT03431194), post-spinal-anesthesia hypotension in elderly hip arthroplasty patients (NCT05548985), chronic/orthostatic hypotension in spinal cord injury (multiple trials), and hypotension associated with heart failure with reduced ejection fraction (NCT06405555). Because the regulatory "original indication" field is a data gap rather than a confirmed absence of approved use, this prediction should be read as **evidence consolidation of an established mechanism across adjacent hypotensive syndromes**, rather than a novel-mechanism hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03431194](https://clinicaltrials.gov/study/NCT03431194) | NA | Completed | 80 | Randomized trial: oral Midodrine effective for intradialytic hypotension in critically ill AKI patients (direct drug/indication match) |
| [NCT05548985](https://clinicaltrials.gov/study/NCT05548985) | NA | Completed | 58 | RCT: oral Midodrine for prophylaxis against post-spinal-anesthesia hypotension in elderly hip arthroplasty patients (direct match) |
| [NCT06405555](https://clinicaltrials.gov/study/NCT06405555) | Phase 2/3 | Not yet recruiting | 56 | Pilot open-label RCT of Midodrine in HFrEF patients with hypotension (direct match) |
| [NCT02307565](https://clinicaltrials.gov/study/NCT02307565) | Phase 3 | Completed | 19 | Midodrine-induced acute BP increase linked to improved cognitive function in spinal cord injury (SCI) patients |
| [NCT05839652](https://clinicaltrials.gov/study/NCT05839652) | Phase 4 | Recruiting | 25 | Pharmacological/non-pharmacological anti-hypotensive treatment for orthostatic hypotension in SCI |
| [NCT01030874](https://clinicaltrials.gov/study/NCT01030874) | NA | Completed | 356 | Multidisciplinary intervention trial for orthostatic hypotension in a rehabilitation unit |
| [NCT02893553](https://clinicaltrials.gov/study/NCT02893553) | Phase 2 | Completed | 21 | Effect of normalizing blood pressure on cerebral blood flow in hypotensive SCI individuals |
| [NCT02307526](https://clinicaltrials.gov/study/NCT02307526) | Phase 2 | Completed | 10 | Acetylcholinesterase inhibition (comparator approach) for orthostatic hypotension in SCI |
| [NCT03037879](https://clinicaltrials.gov/study/NCT03037879) | NA | Completed | 10 | Midodrine-mediated 30-day BP elevation to treat cognitive deficits in SCI |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38205630](https://pubmed.ncbi.nlm.nih.gov/38205630/) | 2024 | Scientific Statement | Hypertension (AHA) | AHA statement on orthostatic hypotension as a comorbidity of hypertension; discusses pressor therapy considerations |
| [2480881](https://pubmed.ncbi.nlm.nih.gov/2480881/) | 1989 | Review | Drugs | Foundational review of Midodrine's pharmacology and use in orthostatic and secondary hypotension |
| [25644760](https://pubmed.ncbi.nlm.nih.gov/25644760/) | 2015 | RCT | Hepatology | Randomized trial: terlipressin+albumin vs. Midodrine+octreotide+albumin for hepatorenal syndrome (direct Midodrine use) |
| [37978969](https://pubmed.ncbi.nlm.nih.gov/37978969/) | 2024 | Clinical Practice Update | Gastroenterology | AGA expert review on vasoactive drugs (including Midodrine) in cirrhosis-associated hypotension/renal dysfunction |
| [39619823](https://pubmed.ncbi.nlm.nih.gov/39619823/) | 2024 | Clinical Study | Topics in Spinal Cord Injury Rehabilitation | 30-day Midodrine administration vs. placebo on BP, cerebral blood flow velocity, and cognition in SCI |
| [32979782](https://pubmed.ncbi.nlm.nih.gov/32979782/) | 2020 | Review | Autonomic Neuroscience | Pharmacologic treatment overview of neurogenic orthostatic hypotension, including pressor agents |
| [28050656](https://pubmed.ncbi.nlm.nih.gov/28050656/) | 2017 | Consensus Statement | Journal of Neurology | Consensus panel recommendations for screening, diagnosis, and treatment of neurogenic OH |
| [35029940](https://pubmed.ncbi.nlm.nih.gov/35029940/) | 2022 | Review | American Family Physician | Practical clinical approach to diagnosing and managing orthostatic hypotension |
| [38123372](https://pubmed.ncbi.nlm.nih.gov/38123372/) | 2024 | Review / Expert Position | Revue Neurologique | Expert position statement on orthostatic hypotension management, including supine hypertension trade-offs |
| [31996627](https://pubmed.ncbi.nlm.nih.gov/31996627/) | 2020 | Review | Continuum (Minneapolis, Minn.) | Management review of orthostatic hypotension with emphasis on neurogenic OH |

---

## Singapore Market Information

Midodrine currently has **no registered product license** on file (market status: Not Marketed; 0 registrations). No local authorization, product name, dosage form, or approved indication text is available to report.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all unavailable in the current evidence pack — flagged as Data Gap DG001, a **Blocking** gap that prevents completion of the S1 safety screening stage.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Nine clinical trials — three testing Midodrine directly with matching indications (intradialytic hypotension, post-spinal-anesthesia hypotension, HFrEF-related hypotension) — plus 19 supporting publications place this prediction at evidence level L1, the strongest in the pack. However, the drug has no Singapore market presence and safety data (warnings, contraindications, DDI) is entirely missing, which blocks a full risk assessment.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain package insert warnings/contraindications, e.g., via TFDA or manufacturer labeling, to complete S1 safety screening
- Resolve DG002 (High): confirm formal mechanism-of-action documentation via DrugBank API to support the mechanistic rationale
- Confirm original approved indication(s) on record, since the current "Data Gap" makes it unclear whether this is genuine repurposing or an extension of an already-established use
- If pursuing local development, initiate a Singapore market registration pathway, as none currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

