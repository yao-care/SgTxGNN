---
layout: default
title: Trifluoperazine
parent: 僅模型預測 (L5)
nav_order: 1014
evidence_level: L5
indication_count: 10
---

# Trifluoperazine
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

Using the evidence pack as provided (no external assumptions beyond what appears in the literature/JSON), here is the report:

# Trifluoperazine: From Psychotic Disorders to Manic Bipolar Affective Disorder

## One-Sentence Summary

> Trifluoperazine is a phenothiazine-class antipsychotic, historically used for psychotic disorders such as schizophrenia (as referenced throughout the supporting literature, though not separately confirmed by a formal indication record in this evidence pack).
> The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**,
> with **0 clinical trials** and **20 publications** currently supporting this direction — evidence remains largely mechanistic and historical rather than confirmatory.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in evidence pack (`original_indications` empty); literature context indicates use as a typical antipsychotic for psychotic disorders/schizophrenia |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Based on the supporting literature in this evidence pack, Trifluoperazine belongs to the phenothiazine class of typical antipsychotics. One review directly in the evidence set (PMID 40926568, *J Appl Toxicol* 2026) states that "phenothiazine derivatives have been used for decades as antipsychotic drugs in multiple mental health and physical conditions treatment (schizophrenia, **mania in bipolar disorder**, and psychosis)" — indicating this drug class already has an established, if underdocumented, role in mania management.

Mechanistically, mania has been linked to dopaminergic overactivity: an early case study in the evidence pack (PMID 970489, *Am J Psychiatry* 1976) reports that pimozide, a dopamine receptor blocker, exerted an antimanic effect, supporting a "dopaminergic mechanism in mania." As Trifluoperazine is also a dopamine receptor antagonist, this provides a plausible pharmacological rationale for its potential antimanic activity, consistent with the TxGNN prediction. A 1963 double-blind study (PMID 14084030) further documents Trifluoperazine's real-world use in combination regimens for mood-disorder maintenance, suggesting prior clinical familiarity with this drug in affective illness, even though it was not the primary study endpoint.

Overall, the connection between the original antipsychotic use and the predicted manic bipolar indication is biologically coherent (shared dopaminergic mechanism, same drug class already used off-label in mania), but the supporting evidence consists mainly of older case reports, narrative reviews, and drug-class commentary rather than dedicated randomized trials in bipolar mania.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14084030](https://pubmed.ncbi.nlm.nih.gov/14084030/) | 1963 | Double-blind study | Current Ther Res Clin Exp | Withdrawal of trifluoperazine from patients maintained on tranylcypromine + trifluoperazine combination, evaluated in a double-blind design |
| [40926568](https://pubmed.ncbi.nlm.nih.gov/40926568/) | 2026 | Review | J Appl Toxicol | States phenothiazine derivatives (incl. trifluoperazine class) have long been used for mania in bipolar disorder, psychosis, and schizophrenia |
| [17017818](https://pubmed.ncbi.nlm.nih.gov/17017818/) | 2006 | Review | J Clin Psychiatry | Reviews efficacy of typical and atypical antipsychotics for anxiety symptoms co-occurring with bipolar disorder |
| [24943390](https://pubmed.ncbi.nlm.nih.gov/24943390/) | 2014 | Cross-sectional survey | J Clin Psychopharmacol | Documents real-world prescribing patterns of antipsychotics (including for bipolar affective disorder) in psychiatric inpatients |
| [970489](https://pubmed.ncbi.nlm.nih.gov/970489/) | 1976 | Case study | Am J Psychiatry | Supports a dopaminergic mechanism in mania; dopamine-blocking agents show antimanic effect |
| [6636782](https://pubmed.ncbi.nlm.nih.gov/6636782/) | 1983 | Case study | Wien Klin Wochenschr | MAO inhibitor plus lithium/neuroleptic combinations in rapid-cycling bipolar manic-depressive patients |
| [3935307](https://pubmed.ncbi.nlm.nih.gov/3935307/) | 1985 | Case report | Can J Psychiatry | Case of bipolar disorder in an adolescent, treatment and differential diagnosis discussed |
| [2102674](https://pubmed.ncbi.nlm.nih.gov/2102674/) | 1990 | Case report | Br J Psychiatry | Neuroleptic malignant syndrome following trifluoperazine + carbamazepine overdose |
| [14309092](https://pubmed.ncbi.nlm.nih.gov/14309092/) | 1965 | Clinical study | Int J Neuropsychiatry | Evaluates haloperidol (comparator antipsychotic class) in schizophrenic and manic patients |
| [19461391](https://pubmed.ncbi.nlm.nih.gov/19461391/) | 2009 | Review | J Psychiatr Pract | Reviews use and safety of antipsychotics (including in bipolar-related pregnancies) |

---

## Singapore Market Information

Trifluoperazine currently has no marketing authorization recorded in Singapore (`market_status: 未上市`, `total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. Note: this evidence pack flags a **Blocking** data gap (DG001 — TFDA/HSA label warnings and contraindications not yet retrieved), which currently prevents formal safety pre-assessment (S1 stage).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The drug is not currently marketed in Singapore, no clinical trials support the predicted indication, and a **Blocking** safety data gap (missing label warnings/contraindications) prevents entry into the safety pre-assessment stage. Supporting literature is mechanistic/historical rather than confirmatory (Evidence Level L4).

**To proceed, the following is needed:**
- Retrieve official label warnings and contraindications (DG001, Blocking) via HSA/TFDA product insert
- Obtain confirmed mechanism of action data from DrugBank (DG002)
- Complete literature classification (currently marked "pending" study type/tier/relevance for all 20 references)
- Assess feasibility of a Singapore registration pathway before further repurposing work
- If proceeding, prioritize designing a dedicated clinical study or systematic review specifically evaluating trifluoperazine in bipolar mania, given the absence of direct trial evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

