---
layout: default
title: Quetiapine
parent: 僅模型預測 (L5)
nav_order: 836
evidence_level: L5
indication_count: 10
---

# Quetiapine
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

# Quetiapine: From Psychiatric Disorders to Trichotillomania

## One-Sentence Summary

> Quetiapine is a widely used atypical antipsychotic, pharmacologically characterized by 5-HT2A/D2 receptor antagonism, though formal original-indication and MOA records are not available in this evidence pack.
> Among the TxGNN model's top 10 predictions, most (retinal dystrophy, glycosylation disorders, hydranencephaly, microdeletion syndromes, etc.) have **no supporting literature or trials** and appear to be spurious matches; only **Trichotillomania (hair-pulling disorder)** is backed by real evidence — **7 publications**, including case reports specifically describing quetiapine treatment — making it the only indication in this candidate set worth further evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (drug is not registered in Singapore; no license or MOA data on file) |
| Predicted New Indication | Trichotillomania (hair-pulling disorder) |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available as a formal field in this evidence pack. Based on the mechanistic rationale attached to this prediction, quetiapine is known to be an atypical antipsychotic acting via 5-HT2A/D2 receptor antagonism, a mechanism used clinically to modulate serotonergic and dopaminergic pathways involved in impulse and mood regulation.

Trichotillomania is an impulse-control/OCD-spectrum disorder for which treatment options remain limited and evidence-based pharmacotherapy is sparse. The theoretical link is that serotonin-dopamine modulation may reduce compulsive, impulse-driven hair-pulling behavior, similar to how atypical antipsychotics are used off-label in other impulse-control and OCD-related conditions.

It is important to note that the supporting literature consists mainly of case reports and small case series rather than controlled trials, and one publication (PMID 11212595) actually reports quetiapine *exacerbating* obsessive-compulsive symptoms in a patient with comorbid trichotillomania — indicating the evidence is mixed and mechanistically indirect rather than confirmatory.

**Note on other top-ranked predictions:** Ranks 1–7, 9, and 10 (retinal dystrophy, glycosylation disorders, hydranencephaly, chromosomal microdeletion syndrome, polymicrogyria, X-linked myopia, Charcot-Marie-Tooth disease) all scored similarly high (>99.3%) on the TxGNN model but have **zero relevant clinical trials or literature**. Where literature was retrieved (rank 1), manual review found it unrelated to quetiapine or the predicted disease, consistent with a false-positive graph-embedding match. These are not discussed further in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19142421](https://pubmed.ncbi.nlm.nih.gov/19142421/) | 2008 | Case report | Rev Bras Psiquiatr | Case report of quetiapine used for trichotillomania treatment |
| [12405081](https://pubmed.ncbi.nlm.nih.gov/12405081/) | 2002 | Review/Case series | Psychiatry | Overview of trichotillomania pharmacotherapy; describes favorable response to quetiapine in a 33-year-old patient |
| [20833945](https://pubmed.ncbi.nlm.nih.gov/20833945/) | 2010 | Case report | Psychosomatics | Case report and literature review of recurrent Rapunzel syndrome and trichotillomania |
| [11212595](https://pubmed.ncbi.nlm.nih.gov/11212595/) | 2001 | Case report/Review | J Psychiatry Neurosci | Reports quetiapine **exacerbating** obsessive-compulsive symptoms in a patient with comorbid trichotillomania and OCD |
| [27840761](https://pubmed.ncbi.nlm.nih.gov/27840761/) | 2016 | Case report | Case Rep Psychiatry | Trichotillomania as a manifestation of dementia; discusses treatment approaches |
| [38797877](https://pubmed.ncbi.nlm.nih.gov/38797877/) | 2025 | Review | Int J Dermatol | Reviews pharmacological treatment options for trichotillomania; notes lack of established guidelines |
| [17484394](https://pubmed.ncbi.nlm.nih.gov/17484394/) | 2006 | Review | J Pract Nurs | General treatment overview of trichotillomania |

---

## Singapore Market Information

Quetiapine currently holds **no active market authorization** in Singapore (0 registrations on file); no license or approved-indication data is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only credibly-linked prediction (trichotillomania) is supported solely by case reports and small case series (L4), including one report of symptom worsening rather than improvement — this is insufficient evidence to advance past the research-question stage, and the drug also carries no current market authorization in Singapore.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent product label (warnings, contraindications, DDI) — currently a blocking data gap
- Formal mechanism of action (MOA) documentation from DrugBank or product labeling
- A controlled or prospective study evaluating quetiapine specifically for trichotillomania, given the mixed signal in existing case reports
- Re-screening of TxGNN's other top-10 predictions, as the majority show no corroborating evidence and likely reflect model noise rather than genuine repurposing signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

