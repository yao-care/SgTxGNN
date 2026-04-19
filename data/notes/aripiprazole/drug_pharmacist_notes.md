# Aripiprazole: From Schizophrenia to Major Affective Disorder

## One-Sentence Summary

Aripiprazole is a second-generation (atypical) antipsychotic, originally approved globally for the treatment of schizophrenia and bipolar I disorder, though currently not registered in Singapore.
The TxGNN model predicts it may be effective for **Major Affective Disorder** (encompassing major depressive disorder and bipolar disorder),
with **multiple completed Phase 3 RCTs** and **20 publications** currently supporting this direction — yielding an overall evidence level of **L1**.

> **Note:** Aripiprazole already holds FDA approval for adjunctive treatment of major depressive disorder and bipolar I disorder globally. Its "not marketed" status in Singapore represents a **regulatory access gap**, not an evidence gap.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia; Bipolar I Disorder (global approvals) |
| Predicted New Indication | Major Affective Disorder |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Aripiprazole is a dopamine D2/D3 partial agonist and serotonin 5-HT1A partial agonist with 5-HT2A antagonism — a dual-mechanism profile often described as "dopamine-serotonin system stabiliser." Its partial agonist activity at D2 receptors allows it to stabilise mesolimbic dopamine overactivity without the full blockade seen with older antipsychotics, while the 5-HT1A partial agonism and 5-HT2A antagonism enhance serotonergic and dopaminergic transmission in the prefrontal cortex. This combination directly addresses the neurobiological substrates underlying both the manic/psychotic pole and the depressive pole of major affective disorders.

The mechanistic bridge to major affective disorder is well-established: dysregulation of the dopamine-serotonin axis is central to the pathophysiology of both major depressive disorder (MDD) and bipolar disorder. Aripiprazole's ability to modulate reward circuitry and prefrontal function without causing metabolic burden or sedation distinguishes it from other second-generation antipsychotics used in mood disorders. The US FDA has already approved aripiprazole as an adjunctive treatment for MDD (Abilify, 2007) and for acute mania and maintenance treatment of bipolar I disorder — providing high-confidence external validation for the TxGNN prediction.

In the Singapore context, the drug's absence from the local market reflects a regulatory submission gap rather than any clinical uncertainty. The breadth and quality of global evidence — including large Phase 3 multi-centre RCTs in treatment-resistant depression (TRD), MDD augmentation, and bipolar maintenance — makes this one of the most evidence-rich repurposing candidates in the dataset. The TxGNN score of 99.62% further reinforces that the knowledge-graph topology strongly links aripiprazole to affective disorder biology.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01421342](https://clinicaltrials.gov/study/NCT01421342) | Phase 3 | Completed | 1,522 | VA VAST-D: Compared aripiprazole augmentation vs. bupropion-SR augmentation vs. bupropion-SR switch in Veterans with MDD unresponsive to first-line antidepressants; primary outcome was symptom remission at 12 weeks |
| [NCT00095758](https://clinicaltrials.gov/study/NCT00095758) | Phase 3 | Completed | 1,200 | Randomised, double-blind, placebo-controlled 14-week study of adjunctive aripiprazole for MDD patients with inadequate response to ongoing antidepressant therapy; core Phase 3 registration trial |
| [NCT00261443](https://clinicaltrials.gov/study/NCT00261443) | Phase 4 | Completed | 1,270 | Long-term maintenance study of aripiprazole combined with lithium or valproate in bipolar I disorder patients partially non-responsive to mood stabiliser monotherapy |
| [NCT00277212](https://clinicaltrials.gov/study/NCT00277212) | Phase 4 | Completed | 1,169 | Double-blind maintenance study of aripiprazole combined with lamotrigine in bipolar I disorder following recent manic or mixed episode |
| [NCT01567527](https://clinicaltrials.gov/study/NCT01567527) | Phase 3 | Completed | 731 | 52-week, placebo-controlled trial of aripiprazole intramuscular depot (OPC-14597) for maintenance treatment in bipolar I disorder; assessed time to recurrence of any mood episode |
| [NCT00876343](https://clinicaltrials.gov/study/NCT00876343) | Phase 3 | Completed | 586 | Placebo-controlled, parallel-group study of aripiprazole as adjunctive therapy with SSRI or SNRI in MDD patients; conducted across multiple centres |
| [NCT02046564](https://clinicaltrials.gov/study/NCT02046564) | Phase 3 | Completed | 412 | Evaluated the fixed-dose combination ASC-01 (aripiprazole/sertraline) vs. sertraline monotherapy in MDD patients with incomplete response to sertraline |
| [NCT03423680](https://clinicaltrials.gov/study/NCT03423680) | Phase 3 | Recruiting | 390 | 8-week confirmatory study of aripiprazole adjunctive to mood stabiliser for major depressive episodes in bipolar I or II disorder; ongoing with results expected post-2025 |
| [NCT00110461](https://clinicaltrials.gov/study/NCT00110461) | Phase 3 | Completed | 296 | Tested two doses of aripiprazole in children and adolescents with bipolar I disorder (manic or mixed episode); key paediatric safety and efficacy dataset |
| [NCT00704860](https://clinicaltrials.gov/study/NCT00704860) | Phase 4 | Completed | 27 | Investigated aripiprazole augmentation in treatment-resistant depression (TRD) with neuroimaging (raclopride/F-DOPA PET and fMRI) to characterise dopaminergic mechanism; directly supports TRD subpopulation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38669232](https://pubmed.ncbi.nlm.nih.gov/38669232/) | 2024 | Meta-analysis of RCTs | PLoS One | First and largest systematic review and meta-analysis of RCTs evaluating aripiprazole or bupropion augmentation and switching in TRD/MDD; demonstrated significant efficacy and acceptable safety profile for aripiprazole augmentation |
| [36961650](https://pubmed.ncbi.nlm.nih.gov/36961650/) | 2023 | RCT | CNS Drugs | Randomised, open-label, pivotal pharmacokinetic/safety study of aripiprazole 2-month long-acting injectable (960 mg) in schizophrenia and bipolar I disorder; confirmed PK equivalence and safety enabling extended dosing interval |
| [38219278](https://pubmed.ncbi.nlm.nih.gov/38219278/) | 2024 | Systematic Review | Neuropsychopharmacology Reports | Frequentist network meta-analysis comparing brexpiprazole, aripiprazole, and placebo for Japanese MDD patients inadequately responsive to antidepressants; confirmed efficacy and characterised tolerability differences relevant to Asian populations |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Review | JAMA | Comprehensive review of bipolar disorder diagnosis and treatment covering ~8 million US adults and ~40 million globally; positions aripiprazole within contemporary treatment algorithms |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematic Review / Network Meta-analysis | Journal of Affective Disorders | Network meta-analysis comparing augmentation agents in adult TRD; aripiprazole ranked among the most efficacious and well-tolerated augmentation options |
| [37149344](https://pubmed.ncbi.nlm.nih.gov/37149344/) | 2023 | Review | Psychiatric Clinics of North America | Reviewed pharmacotherapy for TRD; highlighted that atypical antipsychotics — particularly aripiprazole and brexpiprazole — are the most widely studied augmentation agents with FDA approval |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematic Review | Psychological Medicine | Comprehensive meta-analysis of antipsychotics as monotherapy and adjunctive therapy in MDD; first analysis to systematically examine both treatment roles across the drug class |
| [34167174](https://pubmed.ncbi.nlm.nih.gov/34167174/) | 2021 | Systematic Review / Meta-analysis | Primary Care Companion for CNS Disorders | Assessed long-term (≥6 months) efficacy and safety of adjunctive aripiprazole in MDD; remission rates and adverse effect profile confirmed sustained benefit |
| [37746943](https://pubmed.ncbi.nlm.nih.gov/37746943/) | 2023 | Systematic Review / Network Meta-analysis | Medicine | Compared and ranked four atypical antipsychotics (including aripiprazole) for adjuvant treatment of MDD; provided direct comparative efficacy and safety data |
| [25963405](https://pubmed.ncbi.nlm.nih.gov/25963405/) | 2016 | Review | Asia-Pacific Psychiatry | Reviewed three FDA-approved antipsychotics for adjunctive MDD treatment (quetiapine, aripiprazole, olanzapine); noted these agents are effective at sub-antipsychotic doses and discussed receptor-profile mechanisms — directly relevant to the Asia-Pacific regulatory context |

---

## Singapore Market Information

Aripiprazole currently has **no registered products** in Singapore (HSA). The drug is not listed in any active or historical licence under the Health Sciences Authority.

> This is a **regulatory access gap**. Aripiprazole holds approvals in the United States (FDA), European Union (EMA), Japan (PMDA), and multiple other jurisdictions for schizophrenia, bipolar I disorder, and adjunctive treatment of MDD. A full HSA registration dossier submission would be required to bring this product to the Singapore market.

---

## Safety Considerations

Formal safety data (package insert warnings, contraindications, and drug–drug interaction records) were not retrievable for this evaluation cycle.

> Please refer to the originator package insert (Abilify® / Otsuka Pharmaceutical) and the FDA prescribing information for complete safety information, including black-box warnings for increased mortality in elderly patients with dementia-related psychosis, suicidality in paediatric and young adult patients, and impulse-control disorders (pathological gambling, hypersexuality, binge eating) associated with dopamine partial agonism.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Aripiprazole is one of the best-evidenced drugs in this repurposing dataset for major affective disorder: multiple completed Phase 3 RCTs in MDD augmentation and bipolar maintenance, FDA and EMA approved indications, and an established mechanistic rationale firmly rooted in dopamine-serotonin stabilisation. The L1 evidence level and 99.62% TxGNN score together indicate that the scientific case is settled — the remaining barriers are regulatory and pharmacovigilance in nature, not evidentiary.

**To proceed, the following is needed:**

- **HSA Registration Submission**: Prepare a full Common Technical Document (CTD) dossier for HSA submission, leveraging existing FDA/EMA approval as a reference pathway (potentially via the HSA Abridged Evaluation route)
- **Safety Package Retrieval**: Download and parse the current FDA prescribing information and EMA SmPC to populate the complete warnings, contraindications, and drug interaction profile required for the S1 safety screen
- **MOA Documentation**: Obtain the formal DrugBank mechanism-of-action entry (DB01238) to complete the mechanistic linkage analysis
- **Local Risk Management Plan**: Develop a Singapore-specific Risk Management Plan (RMP) addressing the impulse-control disorder (ICD) black-box warning, particularly for the MDD augmentation indication where doses and patient populations may differ from the schizophrenia setting
- **Pharmacoeconomic Assessment**: Conduct a cost-effectiveness evaluation in the Singapore healthcare context, given that multiple generic aripiprazole formulations are available globally