---
layout: default
title: Perphenazine
parent: 僅模型預測 (L5)
nav_order: 772
evidence_level: L5
indication_count: 10
---

# Perphenazine
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

# Perphenazine: From Schizophrenia (Psychotic Disorders) to Anxiety Disorder

> **Note on indication selection**: TxGNN's highest-scoring prediction (*retinal dystrophy with or without extraocular anomalies*, 99.96%) and the next eight ranked candidates (myopia subtypes, hydranencephaly, CMT1G, glycosylation disorders, etc.) were reviewed and found to be embedding-based false positives — the evidence pack itself flags all 15 associated PubMed records as ophthalmology/genetics literature with no mention of perphenazine, and no clinical trials exist for any of them. This report instead focuses on **anxiety disorder** (rank 10, score 99.53%), the only candidate in the pack supported by actual clinical trials and literature.

## One-Sentence Summary

Perphenazine is a piperazine-phenothiazine antipsychotic historically used for schizophrenia and psychotic disorders (and, in fixed-dose combination with amitriptyline as Triavil/Etrafon, for mixed anxiety-depression). The TxGNN model's evidence-supported candidate among reviewed predictions is **Anxiety Disorder**, backed by **2 clinical trials** and **20 publications**, though the trials do not directly test antianxiety efficacy and most literature dates from the 1950s–60s.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia / psychotic disorders (general pharmacological background; not present in the evidence pack — Singapore licensing data is empty) |
| Predicted New Indication | Anxiety Disorder |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L3 (dated RCTs / observational studies, no current confirmatory trial) |
| Singapore Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Perphenazine is a piperazine-class phenothiazine that primarily antagonizes the dopamine D2 receptor, with moderate α1-adrenergic, H1-histaminergic, and muscarinic-cholinergic antagonism. This receptor profile produces sedative and anxiolytic-adjacent effects that are pharmacologically plausible independent of its primary antipsychotic action.

Historically, this rationale was already put into clinical practice: perphenazine was combined with amitriptyline as **Triavil/Etrafon**, a fixed-dose combination once marketed specifically for "combined anxiety and depression." Several of the literature entries in this evidence pack (e.g., PMID 4867598, PMID 4554486) directly evaluate that combination in anxious-depressed populations, which is the strongest mechanistic and clinical link supporting this candidate.

However, the rationale is dated. Modern psychiatric guidelines no longer recommend antipsychotics as first-line or routine therapy for uncomplicated anxiety disorder, primarily because the risk of extrapyramidal symptoms, tardive dyskinesia, and metabolic adverse effects outweighs the modest anxiolytic benefit relative to benzodiazepines, SSRIs/SNRIs, or buspirone. The two modern clinical trials identified are not efficacy trials for anxiety — one studies an antioxidant add-on in a mixed-diagnosis population using a perphenazine-containing combination product, and the other is a pharmacovigilance/safety surveillance study (terminated) in geriatric psychiatric inpatients.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05646693](https://clinicaltrials.gov/study/NCT05646693) | Phase 2 | Unknown | 58 | Evaluates combined antioxidant therapy alongside Adepsique® (amitriptyline + perphenazine + diazepam) on oxidative stress/inflammatory markers in chronic tinnitus patients; not a direct anxiety efficacy trial and low relevance (Grade C). |
| [NCT02374567](https://clinicaltrials.gov/study/NCT02374567) | Phase 3 | Terminated | 407 | Pharmacovigilance study of psychopharmacological treatment safety and adverse drug reaction rates in gerontopsychiatric inpatients; safety surveillance only, not an efficacy trial for anxiety, and study was terminated (Grade C). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4867598](https://pubmed.ncbi.nlm.nih.gov/4867598/) | 1968 | RCT (double-blind) | Psychosomatics | Double-blind study of perphenazine-amitriptyline combination for physically-induced psychic disturbances in anxiety and depression. |
| [13726172](https://pubmed.ncbi.nlm.nih.gov/13726172/) | 1961 | RCT | American Journal of Psychiatry | Randomized comparison of psychotherapy alone vs. combined with perphenazine or placebo in neurotic and hyperkinetic children. |
| [14401911](https://pubmed.ncbi.nlm.nih.gov/14401911/) | 1959 | RCT | Journal of Mental Science | Compared perphenazine, sodium amylobarbitone, and placebo in anxious and depressed outpatients. |
| [17017818](https://pubmed.ncbi.nlm.nih.gov/17017818/) | 2006 | Review | Journal of Clinical Psychiatry | Reviews efficacy of typical and atypical antipsychotics for primary/comorbid anxiety symptoms across mood disorders. |
| [14249358](https://pubmed.ncbi.nlm.nih.gov/14249358/) | 1964 | Cohort/small clinical study | Journal of the Medical Association of Georgia | Combined amitriptyline and perphenazine reported for combined depression and anxiety. |
| [4886995](https://pubmed.ncbi.nlm.nih.gov/4886995/) | 1969 | Cohort/small clinical study | Diseases of the Nervous System | Double-blind comparison of thiothixene vs. perphenazine-amitriptyline for psychotic and psychoneurotic depression. |
| [3736271](https://pubmed.ncbi.nlm.nih.gov/3736271/) | 1986 | Review | Medical Clinics of North America | General review of psychiatric emergency management including anxiety presentations; not perphenazine-specific efficacy data. |
| [14149372](https://pubmed.ncbi.nlm.nih.gov/14149372/) | 1964 | Narrative/Review | Psychosomatics | Discusses phenothiazines, including perphenazine, in management of stress and anxiety. |
| [27372312](https://pubmed.ncbi.nlm.nih.gov/27372312/) | 2016 | Review (safety) | CNS Drugs | Reviews antipsychotic-induced somnolence incidence and mechanisms; safety context rather than antianxiety efficacy. |
| [9435993](https://pubmed.ncbi.nlm.nih.gov/9435993/) | 1997 | Review (drug interactions) | Clinical Pharmacokinetics | Reviews SSRI–CNS drug interactions relevant to combination use with agents like perphenazine. |

## Singapore Market Information

Perphenazine currently holds **no registrations in Singapore** (market status: Not Marketed, 0 licenses on record). No product-level authorization data is available for review.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not available in the current evidence pack — the DDI database query returned no results.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only actionable candidate from this evidence pack — anxiety disorder — is supported solely by small, methodologically dated RCTs (1959–1969) and a discontinued fixed-dose combination product; the two contemporary trials identified do not test antianxiety efficacy. Combined with the complete absence of safety data (contraindications, key warnings, DDI) and the drug's unregistered status in Singapore, there is insufficient evidence to proceed further at this time. The nine other TxGNN-ranked candidates in this pack (retinal dystrophy, myopia subtypes, hydranencephaly, CMT1G, etc.) show no clinical or mechanistic support and should not be pursued.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (currently a blocking data gap)
- Formal DrugBank-confirmed mechanism of action data
- A repeat/expanded drug-drug interaction database search (prior query returned no results)
- Modern systematic review or comparative-effectiveness data on perphenazine (or perphenazine-amitriptyline combinations) specifically for anxiety disorder
- Confirmation of Singapore import/access pathway given current "not marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

