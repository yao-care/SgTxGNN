---
layout: default
title: Febuxostat
parent: Medium Evidence (L3-L4)
nav_order: 414
evidence_level: L4
indication_count: 10
---

# Febuxostat
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Febuxostat: From Hyperuricemia to Renal Hypouricemia

## One-Sentence Summary

Febuxostat is a non-purine selective xanthine oxidase inhibitor that lowers serum uric acid and is used for hyperuricemia and gout.
The TxGNN model predicts it may be useful for **renal hypouricemia** with a very high score, but only **1 loosely related clinical trial** and **2 publications (a review and a case-level hypothesis report)** exist.
The mechanism runs against the disease biology (these patients already have low uric acid), so this prediction is best treated as a **model artifact or a narrow hypothesis**, not a validated lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperuricemia / gout (general drug knowledge; the indication text is blank in the Singapore registration records) |
| Predicted New Indication | Hypouricemia, renal |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank are not currently available. Febuxostat is known to be a non-purine selective xanthine oxidase (XO) inhibitor that lowers serum urate by reducing urate production.

Renal hypouricemia is the opposite situation. Serum urate is already very low (below 2 mg/dL) because defective renal urate reabsorption (for example, loss of function in URAT1 or GLUT9) causes urate to be lost in the urine. Lowering urate further is mechanistically counterintuitive and could be harmful. The high TxGNN score probably reflects proximity to the urate pathway in the knowledge graph rather than a real therapeutic fit.

The only plausible rationale is a narrow hypothesis. Patients with renal hypouricemia are prone to exercise-induced acute kidney injury (EIAKI). XO inhibition might reduce XO-derived oxidative stress and so help prevent EIAKI. A 2023 Japanese report describes a teenage footballer with familial renal hypouricemia (URAT1 compound heterozygous mutations) and recurrent EIAKI. Hydration alone failed to prevent episodes, and febuxostat was considered as prophylaxis. This is a single-patient observation and is unproven.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Prospective controlled study of how uric acid control affects stone recurrence and renal function in patients with calculi and hyperuricemia (Shanghai Xu-hui Central Hospital). The registry title is only a department name, and the trial appears to be about conventional urate lowering in hyperuricemia, not renal hypouricemia. Relevance grade C, so it cannot be counted as direct evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Review/Hypothesis (single-patient report) | Internal Medicine (Tokyo) | Proposes non-purine selective XO inhibitors such as febuxostat for preventing EIAKI in renal hypouricemia. The patient was a 16-year-old football player with familial renal hypouricemia (URAT1 mutations) and recurrent EIAKI despite hydration. The abstract available here is truncated, so the outcome is not confirmed. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia (serum urate below 2 mg/dL) for rheumatologists, covering its causes. It provides background on the disease, not evidence that febuxostat helps. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14959P | FEBURIC® Film Coated Tablets 80 mg | Tablet, film coated | Not listed in registration records |
| SIN17054P | FEBUGOUT F.C. Tablets 80 mg | Tablet, film coated | Not listed in registration records |

Both products are oral tablets.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for febuxostat in the current query.

Febuxostat carries a hepatotoxicity warning, which should be weighed in any off-label use. Further urate lowering in a patient who already has very low urate could also be harmful.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism (further urate lowering in already-hypouricemic patients) is counterintuitive. The only support is a single-patient hypothesis report and one trial that is unrelated to renal hypouricemia. The high TxGNN score most likely reflects graph proximity to the urate pathway.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications (currently a blocking gap)
- Mechanism-of-action data from DrugBank
- Full text and outcome of the 2023 EIAKI report, plus any further case series or controlled data
- A safety assessment of urate lowering in patients with URAT1/GLUT9 defects
- Consideration of other candidates from the same prediction list. Partial HPRT deficiency (rank 2) and Lesch-Nyhan syndrome (rank 3) have a more coherent mechanism for hyperuricemia control, although evidence is limited to case reports. Febuxostat would not be expected to treat the neurological features of Lesch-Nyhan syndrome.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

