---
layout: default
title: Propafenone
parent: 僅模型預測 (L5)
nav_order: 824
evidence_level: L5
indication_count: 10
---

# Propafenone
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

Using the drug-repurposing evaluation report template to produce the requested output.

# Propafenone: From Cardiac Arrhythmias to Manic Bipolar Affective Disorder

## One-Sentence Summary

> Propafenone is a Class IC antiarrhythmic agent, historically used to treat cardiac arrhythmias such as atrial fibrillation and ventricular tachycardia.
> The TxGNN model's top-ranked prediction is that it may be effective for **Manic Bipolar Affective Disorder**,
> but the only supporting literature (**0 clinical trials, 3 publications**) actually describes propafenone **inducing** mania/psychosis rather than treating it — the evidence points in the opposite direction of the prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cardiac arrhythmias (Class IC antiarrhythmic; not captured in this dataset's regulatory records) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on known pharmacology, propafenone is a Class IC sodium channel blocker with weak beta-adrenergic blocking and mild local-anaesthetic/anticholinergic activity, and its efficacy in cardiac arrhythmias (atrial fibrillation, ventricular tachyarrhythmias) is well established.

There is no established pharmacological rationale connecting sodium-channel blockade to mood stabilisation, and the three retrieved publications do not support a therapeutic application in mania. On the contrary, two case reports (PMID 11949740, PMID 2579063) describe propafenone **inducing** an organic psychosis or manic episode in patients, and a review (PMID 32124390) discusses harmful drug-drug interactions between antipsychotics and cardiovascular medications rather than any antimanic effect. This is a case of causal-direction mismatch — the model appears to have picked up a co-occurrence signal from adverse-event literature rather than genuine therapeutic evidence, which is why the internal scoring already flags this as evidence level L4 with a "Hold" recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32124390](https://pubmed.ncbi.nlm.nih.gov/32124390/) | 2020 | Review | Pharmacological Reports | Reviews harmful drug-drug interactions between antipsychotics and cardiovascular drugs (including propafenone) in patients with bipolar disorder/schizophrenia comorbid with CVD — not an efficacy study |
| [11949740](https://pubmed.ncbi.nlm.nih.gov/11949740/) | 2001 | Case Report | International Journal of Psychiatry in Medicine | Organic psychosis triggered by a venlafaxine-propafenone interaction in a patient with bipolar affective disorder |
| [2579063](https://pubmed.ncbi.nlm.nih.gov/2579063/) | 1985 | Case Report | The Journal of Clinical Psychiatry | Mania secondary to propafenone administration — described as a drug-induced adverse psychiatric effect, not a treatment benefit |

---

## Singapore Market Information

Propafenone currently has no marketing authorisation on record in Singapore (0 registrations); no license data is available to summarise.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Detailed HSA-equivalent label warnings/contraindications and DDI data are marked as a Blocking data gap (DG001) in this evidence pack. Based on the literature retrieved for this indication, be aware of a documented interaction risk between propafenone and venlafaxine/antipsychotics that may precipitate psychiatric adverse events — this should be confirmed against the official label once available.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Manic Bipolar Affective Disorder) is not supported by real-world evidence — the only literature retrieved describes propafenone as a *cause* of mania/organic psychosis, not a treatment for it, and no clinical trials exist. Proceeding would require reversing the causal direction implied by the source data, which is not defensible without new experimental evidence.

**To proceed, the following is needed:**
- Independent pharmacological or preclinical evidence of a genuine antimanic mechanism for propafenone (none currently exists)
- Resolution of the Blocking data gap on official label warnings/contraindications (DG001) before any further safety evaluation
- Confirmed mechanism-of-action data (DG002) to properly assess biological plausibility
- Consideration of other candidates in this evidence pack with stronger, mechanistically coherent support — notably **Catecholaminergic Polymorphic Ventricular Tachycardia** (rank 2, L3, Proceed with Guardrails; multiple mechanistic studies show class I antiarrhythmics including propafenone block RyR2-mediated Ca²⁺ leak) and **Incessant Infant Ventricular Tachycardia** (rank 5, L3, Proceed with Guardrails; supported by paediatric case series), both of which align with propafenone's known antiarrhythmic mechanism and warrant separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

