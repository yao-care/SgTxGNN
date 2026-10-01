---
layout: default
title: Propafenone
parent: Low Evidence (L5)
nav_order: 824
evidence_level: L5
indication_count: 10
---

# Propafenone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Propafenone: From Cardiac Arrhythmia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Propafenone is a class IC antiarrhythmic drug. The registration record in this pack does not state an approved indication, so this is inferred from its drug class.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, but **0 clinical trials** and **3 publications** support this, and none of the three shows a therapeutic benefit.
The literature points the opposite way: it describes propafenone *causing* mania and a psychiatric drug interaction, so this prediction should be treated as a safety signal rather than a repurposing lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration record (class IC antiarrhythmic) |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 (no study supports a therapeutic effect; the pack labels this L4, but the retrieved papers are adverse-event reports and a drug-interaction review) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, propafenone is a class IC sodium channel blocker used for heart rhythm disorders. No plausible therapeutic mechanism for mania has been demonstrated.

The retrieved literature does not support a treatment effect. A 1985 case report describes mania that developed secondary to propafenone. The authors speculated that its chemical similarity to bupropion might give it antidepressant-like activity and cause affective side effects. A 2001 case report describes an organic psychosis from a venlafaxine–propafenone interaction in a patient with bipolar disorder.

The very high TxGNN score is most likely an artifact of proximity in the knowledge graph, not a real pharmacological link. The more promising predicted indication for this drug is catecholaminergic polymorphic ventricular tachycardia (CPVT), which is ranked second. It is discussed in the conclusion.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32124390](https://pubmed.ncbi.nlm.nih.gov/32124390/) | 2020 | Review | Pharmacological Reports | Evaluates harmful drug interactions between antipsychotics and cardiovascular drugs in patients with bipolar disorder or schizophrenia and comorbid cardiovascular disease. It is not evidence of benefit. |
| [2579063](https://pubmed.ncbi.nlm.nih.gov/2579063/) | 1985 | Case report | J Clin Psychiatry | Mania developed secondary to propafenone. The authors described it as a previously unrecognized complication. |
| [11949740](https://pubmed.ncbi.nlm.nih.gov/11949740/) | 2001 | Case report | Int J Psychiatry Med | Organic psychosis from a venlafaxine–propafenone interaction in a patient with bipolar disorder. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00395P | RYTMONORM TABLET 150 mg | Film-coated tablet (oral) | Not stated in the record |

---

## Safety Considerations

- **Psychiatric adverse effects**: Case reports describe propafenone-associated mania (1985) and a neuropsychiatric interaction with venlafaxine (2001). Both are single cases and do not establish incidence.
- **Drug interactions**: The interaction database query returned no entries. This should not be read as an absence of interactions. See the venlafaxine report above.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, and the available literature shows psychiatric harm rather than benefit. No clinical trials exist and no plausible mechanism is supported.

**To proceed, the following is needed:**
- No further work on this indication is recommended unless new supporting evidence appears.
- Obtain the HSA package insert warnings and contraindications, which are currently missing and block safety screening.
- Obtain the mechanism of action data from DrugBank.
- Redirect effort to the rank 2 prediction, **catecholaminergic polymorphic ventricular tachycardia** (score 99.79%, Research Question stage).
  - Preclinical studies show propafenone inhibits RyR2 channels and suppresses calcium waves, similar to flecainide.
  - Clinical support is limited to one 35-year case report (PMID 30820400).
  - A propafenone-specific retrospective series would be needed to move the evidence level up.
  - Class IC proarrhythmia cautions apply.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

