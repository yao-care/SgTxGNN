---
layout: default
title: Orphenadrine
parent: 僅模型預測 (L5)
nav_order: 736
evidence_level: L5
indication_count: 10
---

# Orphenadrine
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

Using judgment as domain expert here (not invoking a process skill — this is a single deterministic report-generation task with an already-fully-specified format).

Note before the report: TxGNN's rank-1 hit by raw score ("retinal dystrophy with or without extraocular anomalies", 99.29%) is explicitly flagged in its own `repurposing_rationale` as a likely knowledge-graph clustering artifact with zero mechanistic plausibility — same for ranks 2–4, 6–10 (all L5/Hold, no literature, no mechanistic link). The only candidate in this pack with real evidence is rank 5 (schizophrenia, L3, "Research Question"). Mechanically taking `predicted_indications[0]` would produce a report about a candidate the evidence pack itself says is a false positive, so I'm featuring the evidence-backed candidate instead and noting why.

---

# Orphenadrine: From Antiparkinsonian/Muscle-Relaxant Use to Schizophrenia (Adjunct for Antipsychotic-Induced Extrapyramidal Symptoms)

## One-Sentence Summary

> Orphenadrine is an antimuscarinic agent historically used for parkinsonism and muscle spasm, and — per the literature retrieved here — specifically to counteract extrapyramidal side effects (EPS) caused by antipsychotic drugs.
> TxGNN's top-scored prediction (retinal dystrophy) is flagged by the model's own rationale as a likely false positive with no mechanistic support; among the ten predictions returned, only **Schizophrenia** carries real supporting evidence — **20 publications**, no clinical trials, and no Singapore market presence.
> The evidence describes orphenadrine as an **adjunct to antipsychotic therapy** (managing drug-induced Parkinsonism/EPS), not a treatment for the core symptoms of schizophrenia itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in Singapore registry (unmarketed). Per literature: antimuscarinic agent for parkinsonism and skeletal muscle spasm |
| Predicted New Indication | Schizophrenia (as adjunct anticholinergic for antipsychotic-induced EPS) |
| TxGNN Prediction Score | 99.13% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for orphenadrine is not available in this pack. Based on the retrieved literature, orphenadrine is an **antimuscarinic (anticholinergic) agent**, structurally related to diphenhydramine-class antihistamines, with additional NMDA-receptor antagonist activity. It has long been used clinically to relieve muscle spasm and Parkinsonian symptoms.

The connection to schizophrenia is indirect: antipsychotics (e.g., haloperidol, phenothiazines) used to treat schizophrenia commonly cause drug-induced Parkinsonism and other extrapyramidal symptoms through dopamine D2 blockade. Anticholinergic agents like orphenadrine are used adjunctively to counteract this side effect, restoring the cholinergic-dopaminergic balance disrupted by antipsychotic treatment. This is the mechanism reflected throughout the retrieved literature (e.g., Altamura et al. 1986/1989; Gerlach et al. 1977; Mindham et al. 1972).

**Important caveat:** this is an adjunct/side-effect-management role, not evidence that orphenadrine treats the core positive/negative symptoms of schizophrenia. TxGNN's disease label "schizophrenia" should be read as "used in schizophrenia patients on antipsychotics," not "treats schizophrenia." The other nine predicted indications in this pack (retinal dystrophy, congenital glycosylation disorder, polymicrogyria syndrome, CMT1G, X-linked myopia variants, glycine encephalopathy, hydranencephaly) all returned zero clinical trials, zero or irrelevant literature, and are explicitly annotated by the model's own rationale as having no mechanistic basis — most likely knowledge-graph clustering artifacts (e.g., co-occurrence with "ophthalmology" or "neurodevelopmental" node clusters) rather than genuine repurposing signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4571143](https://pubmed.ncbi.nlm.nih.gov/4571143/) | 1972 | RCT | Psychological Medicine | Compared amantadine, orphenadrine, and placebo for controlling phenothiazine-induced Parkinsonism |
| [324238](https://pubmed.ncbi.nlm.nih.gov/324238/) | 1977 | RCT | Acta Psychiatrica Scandinavica | Orphenadrine vs. G 31.406 vs. placebo in long-term neuroleptic-treated schizophrenic patients; effects on Parkinsonism, schizophrenic symptoms, depression, anxiety |
| [29341071](https://pubmed.ncbi.nlm.nih.gov/29341071/) | 2018 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Anticholinergic medication (class including orphenadrine) for antipsychotic-induced tardive dyskinesia |
| [10796321](https://pubmed.ncbi.nlm.nih.gov/10796321/) | 2000 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Earlier Cochrane review of anticholinergic medication for neuroleptic-induced tardive dyskinesia |
| [3698889](https://pubmed.ncbi.nlm.nih.gov/3698889/) | 1986 | Cohort | L'Encéphale | Haloperidol + orphenadrine combination in 22 schizophrenic patients; orphenadrine significantly reduced EPS, withdrawal worsened symptoms |
| [2616635](https://pubmed.ncbi.nlm.nih.gov/2616635/) | 1989 | Observational | Pharmacopsychiatry | Naturalistic study of 44 schizophrenic outpatients on haloperidol + orphenadrine for residual neuroleptic-induced Parkinsonian symptoms |
| [3962752](https://pubmed.ncbi.nlm.nih.gov/3962752/) | 1986 | Observational | Acta Neurologica | Orphenadrine plasma levels correlated with amelioration of EPS in haloperidol-treated schizophrenic patients |
| [9965](https://pubmed.ncbi.nlm.nih.gov/9965/) | 1976 | Commentary/Review | British Journal of Clinical Pharmacology | Methodological review of drug-induced Parkinsonism assessment and control-drug efficacy (including orphenadrine) in schizophrenia |
| [13686389](https://pubmed.ncbi.nlm.nih.gov/13686389/) | 1961 | Case Series | Rassegna di Studi Psichiatrici | Combined reserpine + high-dose orphenadrine in chronic schizophrenia |
| [13793294](https://pubmed.ncbi.nlm.nih.gov/13793294/) | 1959 | Case Series | Folia Psychiatrica, Neurologica et Neurochirurgica Neerlandica | Reserpine-induced Parkinsonoid in chronic schizophrenics treated with orphenadrine (Disipal) |

---

## Singapore Market Information

No Singapore product registrations on file — market status is **未上市 (not marketed)**, with 0 total licenses recorded.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: a Blocking data gap exists — HSA-equivalent label warnings/contraindications for orphenadrine have not yet been retrieved. This must be resolved before any safety-dependent decision, per data gap DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence supports orphenadrine only as an adjunct anticholinergic for managing antipsychotic-induced EPS in schizophrenia patients — not as a treatment for schizophrenia itself — and all supporting studies are older observational/cohort designs or reviews of the drug class, not orphenadrine-specific RCTs. The drug is unregistered in Singapore, and a Blocking data gap on label safety information (DG001) prevents any S1 safety evaluation. TxGNN's higher-scored predictions (retinal dystrophy, glycosylation disorder, etc.) are explicitly assessed as likely false positives with no mechanistic or literature support and should not be pursued.

**To proceed, the following is needed:**
- HSA-equivalent label warnings/contraindications for orphenadrine (Blocking gap DG001)
- Confirmed mechanism-of-action data from DrugBank (High-priority gap DG002)
- A precise definition of the intended claim — adjunct EPS management in antipsychotic-treated patients, not primary schizophrenia treatment — before any regulatory or clinical scoping
- Drug interaction data (current DDI query returned no results; needs a proper source query, not confirmation of absence)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

