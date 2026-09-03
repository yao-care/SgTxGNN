---
layout: default
title: Selegiline
parent: 僅模型預測 (L5)
nav_order: 890
evidence_level: L5
indication_count: 10
---

# Selegiline
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

# Selegiline: From Parkinson's Disease/Depression to Schizophrenia (Negative Symptoms)

## One-Sentence Summary

> Selegiline is a selective MAO-B inhibitor traditionally used for Parkinson's disease (oral) and major depressive disorder (transdermal).
> The TxGNN model's top *evidence-backed* prediction is **Schizophrenia** — specifically as an adjunct treatment for negative symptoms —
> with **1 clinical trial** and **20 publications** currently supporting this direction, including two placebo-controlled RCTs with mixed results.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (registration data absent; known approved uses: Parkinson's disease, major depressive disorder) |
| Predicted New Indication | Schizophrenia (negative symptoms, as antipsychotic augmentation) |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L2 |
| Singapore Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

**Note on ranking:** TxGNN's top-10 output is dominated by ultra-rare congenital/genetic disorders (ranks 1, 3, 5, 6, 10) and refractive/ophthalmic conditions (ranks 4, 7, 8, 9) with no clinical trials, no literature, and no plausible mechanistic link to MAO-B inhibition — these are treated as noise. **Schizophrenia (rank 2)** is the only prediction with substantive clinical and literature support and is therefore the focus of this report.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Selegiline is not available in this evidence pack (data gap, remediation pending via DrugBank API). Based on known pharmacology, Selegiline is a selective, irreversible **MAO-B inhibitor**; at higher oral doses (≥20 mg/day) it loses selectivity and also inhibits MAO-A, producing broader monoaminergic effects. It is established for Parkinson's disease (oral) and major depressive disorder (transdermal patch), both of which involve monoamine (dopamine/norepinephrine/serotonin) dysregulation.

Schizophrenia's negative symptoms (avolition, blunted affect, social withdrawal) have long been linked to a hypothesized **mesocortical dopamine deficiency**, distinct from the mesolimbic dopamine excess driving positive symptoms. This provides a mechanistic rationale for low-dose Selegiline as an **antipsychotic augmentation agent** rather than a standalone treatment: by mildly boosting prefrontal dopaminergic/noradrenergic tone, it may counteract the dopamine-blunting effect of antipsychotics without worsening positive symptoms. An additional proposed pathway is Selegiline's antioxidant/neuroprotective property, potentially mitigating oxidative stress implicated in schizophrenia pathophysiology.

Notably, this is not a de novo hypothesis — it has been directly tested in humans across at least three RCTs/pilot studies (1996–2008) and is the subject of a 2023 systematic review/meta-analysis, giving this prediction meaningfully more grounding than the other nine candidates in this evidence pack, all of which are pure model output with no supporting studies.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00456976](https://clinicaltrials.gov/study/NCT00456976) | Early Phase 1 | Completed | 70 | Randomized, placebo-controlled trial of Selegiline augmentation of antipsychotics for negative symptoms in inpatients with chronic schizophrenia. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15677608](https://pubmed.ncbi.nlm.nih.gov/15677608/) | 2005 | RCT | Am J Psychiatry | Double-blind, placebo-controlled, multicenter trial of Selegiline augmentation for negative symptoms in outpatients with schizophrenia. |
| [8627275](https://pubmed.ncbi.nlm.nih.gov/8627275/) | 1996 | RCT | J Nerv Ment Dis | Pilot study of low-dose Selegiline (5mg bid) augmentation for negative symptoms, testing the dopamine-deficiency hypothesis. |
| [17972359](https://pubmed.ncbi.nlm.nih.gov/17972359/) | 2008 | RCT | Hum Psychopharmacol | Double-blind RCT of Selegiline add-on to risperidone for negative symptoms; results contradictory to earlier positive findings. |
| [37087864](https://pubmed.ncbi.nlm.nih.gov/37087864/) | 2023 | Review (Meta-analysis) | Eur Neuropsychopharmacol | Systematic review/meta-analysis of Selegiline efficacy and safety across psychiatric disorders (oral and transdermal formulations). |
| [17405823](https://pubmed.ncbi.nlm.nih.gov/17405823/) | 2007 | Review | Ann Pharmacother | Review of Selegiline's role in treating negative symptoms of schizophrenia. |
| [10080262](https://pubmed.ncbi.nlm.nih.gov/10080262/) | 1999 | Case series | Compr Psychiatry | Case series (n=3) showing improvement in negative symptoms and functioning with Selegiline add-on; no adverse effects observed. |
| [8102552](https://pubmed.ncbi.nlm.nih.gov/8102552/) | 1993 | RCT | Biol Psychiatry | Placebo-controlled trial of Selegiline for neuroleptic-induced tardive dyskinesia (related movement-disorder comorbidity in schizophrenia). |
| [7901857](https://pubmed.ncbi.nlm.nih.gov/7901857/) | 1993 | — | Pharmacopsychiatry | Selegiline for neuroleptic-induced parkinsonism. |
| [36561338](https://pubmed.ncbi.nlm.nih.gov/36561338/) | 2022 | Review | Front Pharmacol | Historical review of MAO inhibitors' role in psychopharmacology, including catatonia. |
| [35624406](https://pubmed.ncbi.nlm.nih.gov/35624406/) | 2022 | Review | J Neural Transm | Review of neurodevelopmental pathogenesis in neuropsychiatric disorders, referencing Selegiline's introduction and mechanism. |

**Note:** Additional retrieved literature (PMIDs 22533871, 26848926, 29552749, 23152218, 17253492, 19194522, 17262163, 7831475, 10752567, 16930948) primarily addresses antipsychotic side-effect management (sexual dysfunction, tardive dyskinesia) or general schizophrenia treatment reviews with only tangential Selegiline relevance; they are not listed individually above but support the broader context of adjunctive psychiatric use.

---

## Singapore Market Information

Selegiline is currently **not marketed** in Singapore (0 registrations on file). No licensing/authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are currently not available in this evidence pack — flagged as Blocking data gap DG001, pending TFDA label retrieval.)

**Known class-level consideration (not from evidence pack, general pharmacology):** MAO-B inhibitors carry a risk of hypertensive crisis with tyramine-rich foods at high doses and serious interactions with serotonergic agents (e.g., SSRIs, SNRIs, meperidine) via serotonin syndrome risk — this is particularly relevant given the proposed use alongside antipsychotics/other psychotropics, and must be formally verified against the official label before proceeding.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While Selegiline-as-schizophrenia-augmentation has real clinical trial and RCT support (L2), the trial evidence is small-scale, dated (1993–2008), and contradictory — one double-blind RCT (Bodkin 2005) and a pilot study (Bodkin 1996) reported benefit, while another RCT (Amiri 2008) did not replicate this. A 2023 meta-analysis exists but was not yet classified for direction of effect in this evidence pack. Additionally, the drug is not currently registered in Singapore, and critical safety data (contraindications, DDI, warnings) is blocked pending label retrieval — this alone prevents movement past initial safety screening (S1).

**To proceed, the following is needed:**
- Retrieve and parse official Selegiline package insert (warnings/contraindications) — DG001, Blocking
- Obtain confirmed mechanism of action from DrugBank — DG002, High priority
- Classify the 2023 meta-analysis (PMID 37087864) findings for direction/strength of effect in psychiatric indications
- Assess feasibility of Singapore market entry (no current registration) or evaluate as off-label/named-patient pathway
- If proceeding to research stage: define target population (negative-symptom-predominant schizophrenia), dosing (low-dose, MAO-B selective range), and serotonergic drug interaction screening protocol given concurrent antipsychotic/psychotropic use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

