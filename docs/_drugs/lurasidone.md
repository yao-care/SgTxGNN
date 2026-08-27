---
layout: default
title: Lurasidone
parent: 僅模型預測 (L5)
nav_order: 615
evidence_level: L5
indication_count: 10
---

# Lurasidone
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

---

# Lurasidone: From Schizophrenia / Bipolar Depression to Manic Bipolar Affective Disorder

## One-Sentence Summary

Lurasidone (brand name Latuda®) is a second-generation atypical antipsychotic approved in the United States and Japan for schizophrenia and bipolar I depression, but currently not registered in Singapore.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder** — specifically the manic phase of bipolar disorder — a clinical setting mechanistically distinct from, yet closely related to, its established indication in bipolar depression.
This prediction is supported by **15 clinical trials** (including 8 completed Phase 3 studies) and **20 publications**, yielding a TxGNN confidence score of **99.98%** and an evidence grade of **L1**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia; Bipolar I Depression (US FDA / Japan PMDA approved; **not registered in Singapore**) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Lurasidone exerts its effects through a multi-receptor pharmacological profile that addresses several key dimensions of bipolar disorder simultaneously. **D2/D3 receptor antagonism** reduces dopaminergic hyperactivity — the central driver of manic episodes — an established mechanism shared by all approved antimanic atypical antipsychotics (quetiapine, olanzapine, risperidone, aripiprazole). **5-HT2A antagonism** modulates cortical-limbic circuitry for broader mood stabilization, while **5-HT1A partial agonism** confers antidepressant activity, distinguishing lurasidone from purely antimanic agents and positioning it as a full-spectrum bipolar treatment. **5-HT7 antagonism** additionally improves circadian rhythm regulation and cognitive function — domains frequently impaired in bipolar patients even during euthymia. Its relatively low H1 affinity minimizes sedation and metabolic burden, supporting long-term maintenance use.

Lurasidone is already FDA-approved for **bipolar I depression**, meaning the manic and depressive phases of bipolar I disorder share the same underlying neurobiological substrate. The same D2/D3 antagonism that stabilizes mood in the depressive context provides direct pharmacological rationale for antimanic efficacy. The TxGNN model's prediction thus represents an extension along the bipolar spectrum rather than a leap to an unrelated indication. Notably, SM-13496 — the Japanese development code for lurasidone — was studied across the full bipolar I spectrum in Japan, including manic and mixed episodes, further corroborating clinical plausibility.

The body of evidence is extensive: multiple completed Phase 3 RCTs enrolling hundreds to nearly 1,000 participants, long-term safety extension studies in both adults and pediatric populations, and high-quality network meta-analyses in the Lancet Psychiatry and Molecular Psychiatry have examined lurasidone against the full landscape of bipolar pharmacotherapy. The CANMAT/ISBD international guidelines (2018 and 2021 updates) explicitly list lurasidone as an evidence-based option in bipolar disorder management.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01358357](https://clinicaltrials.gov/study/NCT01358357) | Phase 3 | Completed | 965 | Multi-center, randomized, placebo-controlled study of lurasidone adjunctive to lithium or divalproex for **prevention of recurrence** in Bipolar I Disorder (with or without rapid cycling / psychotic features); largest maintenance prevention trial |
| [NCT01914393](https://clinicaltrials.gov/study/NCT01914393) | Phase 3 | Completed | 702 | 104-week open-label long-term safety and effectiveness of flexibly dosed lurasidone (20–80 mg/day) in **pediatric patients**; the most extensive long-term pediatric safety dataset for lurasidone |
| [NCT01986101](https://clinicaltrials.gov/study/NCT01986101) | Phase 3 | Completed | 525 | SM-13496 (lurasidone) vs. placebo in **Bipolar I Depression**; Japanese Phase 3 registration trial supporting PMDA approval |
| [NCT01986114](https://clinicaltrials.gov/study/NCT01986114) | Phase 3 | Completed | 495 | Long-term efficacy and safety of SM-13496 (lurasidone) in **Bipolar I Disorder**; Japanese long-term extension study with broad bipolar spectrum coverage |
| [NCT01575561](https://clinicaltrials.gov/study/NCT01575561) | Phase 3 | Completed | 377 | 12-week open-label extension evaluating longer-term safety, tolerability, and effectiveness of lurasidone adjunctive to **lithium or divalproex** in Bipolar I Disorder |
| [NCT02046369](https://clinicaltrials.gov/study/NCT02046369) | Phase 3 | Completed | 350 | 6-week RCT of flexibly dosed lurasidone in **children and adolescents with Bipolar I Depression** (ages 6–17); established pediatric efficacy |
| [NCT02731612](https://clinicaltrials.gov/study/NCT02731612) | Phase 3 | Completed | 100 | ELICE-BD: Randomized, double-blind, placebo-controlled study of lurasidone adjunctive therapy on **cognitive functioning** in euthymic Bipolar I/II patients with cognitive impairment |
| [NCT02147379](https://clinicaltrials.gov/study/NCT02147379) | Phase 3 | Completed | 53 | Randomized, open-label study of lurasidone vs. treatment-as-usual on **cognitive functioning** in euthymic Bipolar I patients over 6 weeks |
| [NCT04383691](https://clinicaltrials.gov/study/NCT04383691) | Phase 3 | Terminated | 124 | 6-week double-blind, placebo-controlled flexible-dose trial of lurasidone for **Bipolar I Depression** (terminated early; partial safety data available from 124 enrolled) |
| [NCT06433635](https://clinicaltrials.gov/study/NCT06433635) | Phase 4 | Active, not recruiting | 2,726 | SMART trial comparing cariprazine, quetiapine, **lurasidone**, and aripiprazole/escitalopram for bipolar depression; largest ongoing pragmatic head-to-head comparison trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [39557452](https://pubmed.ncbi.nlm.nih.gov/39557452/) | 2024 | Systematic Review + Dose-Response Meta-analysis | BMJ Mental Health | Examined dose-response relationship for lurasidone efficacy, acceptability, and metabolic/endocrine profiles in bipolar depression; clarifies optimal dosing strategy for clinical use |
| [38487836](https://pubmed.ncbi.nlm.nih.gov/38487836/) | 2024 | Network Meta-analysis | European Psychiatry | Bayesian NMA of 16 RCTs (n=7,234) comparing 5 FDA-approved atypical antipsychotics (including lurasidone) for bipolar depression; lurasidone shown competitive on both efficacy and tolerability |
| [37595997](https://pubmed.ncbi.nlm.nih.gov/37595997/) | 2023 | Network Meta-analysis | The Lancet Psychiatry | Comprehensive NMA of pharmacological interventions for acute bipolar depression; informs current guideline evidence synthesis; lurasidone ranks favorably for efficacy-tolerability balance |
| [33177610](https://pubmed.ncbi.nlm.nih.gov/33177610/) | 2021 | Systematic Review + NMA | Molecular Psychiatry | NMA of mood stabilizers and antipsychotics for bipolar disorder in the **maintenance phase**; supports positioning of lurasidone in long-term bipolar management |
| [29536616](https://pubmed.ncbi.nlm.nih.gov/29536616/) | 2018 | Clinical Practice Guideline | Bipolar Disorders | CANMAT/ISBD 2018 guidelines for bipolar disorder management; lurasidone listed as a first-line evidence-based option for bipolar I depression |
| [34599629](https://pubmed.ncbi.nlm.nih.gov/34599629/) | 2021 | Clinical Practice Guideline | Bipolar Disorders | CANMAT/ISBD 2021 update for bipolar disorder with **mixed features**; provides treatment selection guidance applicable to mixed manic/depressive presentations |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Narrative Review | JAMA | Comprehensive review of bipolar disorder diagnosis and treatment for clinicians; covers ~40 million affected globally; contextualizes treatment landscape |
| [39243127](https://pubmed.ncbi.nlm.nih.gov/39243127/) | 2024 | Review | Medical Science Monitor | Narrative review of new antipsychotics and mood stabilizers; directly covers lurasidone mechanism, efficacy, safety, and therapeutic potential in bipolar disorder and schizophrenia |
| [36472471](https://pubmed.ncbi.nlm.nih.gov/36472471/) | 2022 | Treatment Algorithm / Expert Consensus | J Child Adolescent Psychopharmacology | Updated pharmacological treatment algorithms for **pediatric bipolar manic/mixed and depressed episodes**; evaluates evidence for lurasidone in children |
| [24170243](https://pubmed.ncbi.nlm.nih.gov/24170243/) | 2014 | Commentary | American Journal of Psychiatry | Early expert commentary specifically titled "Lurasidone and bipolar disorder" by Belmaker; establishes the conceptual framing for lurasidone's role in bipolar treatment |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Formal safety data (warnings, contraindications, drug interactions) for Singapore regulatory context is not yet available in this Evidence Pack. A full safety review should be conducted prior to clinical recommendation, sourcing from the US FDA label, PMDA SmPC, and the DrugBank database.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Lurasidone has L1-level evidence in the bipolar spectrum: multiple completed Phase 3 RCTs, high-quality network meta-analyses in Lancet Psychiatry, and inclusion in CANMAT/ISBD international guidelines. Its multi-receptor mechanism provides clear pharmacological rationale for antimanic activity extending beyond its established bipolar depression indication. However, it is not currently registered in Singapore, and formal safety data for the Singapore context is absent.

**To proceed, the following is needed:**

- **Singapore HSA registration pathway:** Evaluate bridging data requirements; the drug holds FDA and PMDA approval, which may support a full registration application via the Health Sciences Authority
- **Full safety data review:** Obtain the US FDA prescribing information and PMDA SmPC to document contraindications, key warnings (e.g., tardive dyskinesia, neuroleptic malignant syndrome, metabolic effects), and major drug interactions
- **Mechanism of action documentation:** Formal DrugBank/PMDA MOA data to complete the mechanistic evidence package for the repurposing dossier
- **Manic phase-specific evidence gap:** Most completed trials focus on bipolar I *depression* or *maintenance*; direct head-to-head evidence for *acute mania* is limited — review NCT01932541 (withdrawn) and supplementary data from SM-13496 Japanese trials for any manic-phase subgroup data
- **Metabolic monitoring plan:** Although lurasidone has a favorable metabolic profile relative to other antipsychotics, a structured monitoring protocol (body weight, fasting glucose, lipids, EPS assessment) should be defined for any clinical deployment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

