---
layout: default
title: Tolbutamide
parent: 僅模型預測 (L5)
nav_order: 992
evidence_level: L5
indication_count: 10
---

# Tolbutamide
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

Using no specific coding/debugging skill here — this is a direct content-generation task with an explicit output template supplied in the prompt, so I'll follow it directly.

One note before the report: `predicted_indications[0]` (opsismodysplasia, score 96.8%) is explicitly annotated in its own rationale as *"判斷為 KG 雜訊預測，無實質證據"* (judged as knowledge-graph noise, no substantive evidence) — as are ranks 2, 3, 5–8, and 10. The only candidate with actual literature support and a coherent mechanism is **rank 9 (pancreatic agenesis, L4/S1)**. I've built the report around that candidate rather than the raw top score, since a report recommending action on a candidate the evidence pack itself flags as noise would not be useful. This deviation is flagged here for transparency.

---

# Tolbutamide: From Type 2 Diabetes Mellitus to Pancreatic Agenesis

## One-Sentence Summary

> Tolbutamide is a first-generation sulfonylurea historically used to treat Type 2 diabetes mellitus.
> Among 10 TxGNN-predicted indications, most (including the top-ranked "opsismodysplasia") were flagged by the evidence pack itself as knowledge-graph noise with no biological plausibility.
> The one candidate with a coherent mechanism and supporting literature is **Pancreatic Agenesis** (rank 9, TxGNN score 93.15%), linked via the KATP-channel mechanism shared with permanent neonatal diabetes — but it is supported only by **indirect mechanistic literature (0 clinical trials)**, so the evidence remains preliminary.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (established pharmacological classification; no formal Singapore label text exists as the drug is not registered here) |
| Predicted New Indication | Pancreatic Agenesis (selected over the raw top-ranked prediction — see note above) |
| TxGNN Prediction Score | 93.15% |
| Evidence Level | L4 (preclinical / mechanistic literature only) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed formal MOA documentation for tolbutamide is not available in this evidence pack (marked as a data gap). However, based on well-established pharmacological knowledge reflected in the supporting literature: tolbutamide is a first-generation sulfonylurea that binds SUR1/Kir6.2 (the KATP channel) on pancreatic β-cells, closing the channel and triggering insulin secretion. This is the same mechanism shared by the entire sulfonylurea class.

Pancreatic agenesis and permanent neonatal diabetes mellitus (PNDM) are closely overlapping clinical phenotypes. When PNDM is caused by activating mutations in KCNJ11 or ABCC8 — the genes encoding the KATP channel subunits itself — patients can often be switched from insulin to sulfonylurea therapy, because the channel remains pharmacologically responsive to sulfonylurea binding. This is a clinically established practice with glyburide (a related sulfonylurea) in KATP-channel-mutation PNDM.

The mechanistic argument for tolbutamide in pancreatic agenesis is therefore plausible but **indirect**: pancreatic agenesis is a differential diagnosis/overlapping phenotype of PNDM rather than being definitionally identical to a KATP-channel mutation disorder, and no study in this evidence pack tests tolbutamide directly in pancreatic agenesis patients. The supporting literature is genetic-mechanism and case-based, not interventional.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15115830](https://pubmed.ncbi.nlm.nih.gov/15115830/) | 2004 | Genetic mechanism review | N Engl J Med | Activating mutations in KCNJ11 (Kir6.2 subunit of the KATP channel) cause permanent neonatal diabetes — establishes the genetic basis for sulfonylurea-responsive KATP-channel disease overlapping with pancreatic agenesis |
| [23274908](https://pubmed.ncbi.nlm.nih.gov/23274908/) | 2013 | Basic science | Diabetes | Congenital hyperinsulinism model implicates β-cell KATP-channel-related pathways in islet secretory dysfunction |
| [18438528](https://pubmed.ncbi.nlm.nih.gov/18438528/) | 2008 | Review | Arq Bras Endocrinol Metabol | Review of neonatal diabetes mellitus subtypes, including KATP-channel mutations relevant to differential diagnosis from pancreatic agenesis |
| [10482920](https://pubmed.ncbi.nlm.nih.gov/10482920/) | 1999 | Basic science | Br J Pharmacol | Sulfonylurea pretreatment alters islet KATP-channel responsiveness — direct pharmacological mechanism data for the drug class |
| [3057892](https://pubmed.ncbi.nlm.nih.gov/3057892/) | 1988 | Review | Am J Med | Notes preserved insulin response to intravenous tolbutamide in specific diabetic phenotypes, supporting its use as a β-cell functional probe/therapeutic |
| [15149729](https://pubmed.ncbi.nlm.nih.gov/15149729/) | 2004 | Basic science | Mol Cell Endocrinol | Rat diabetes model retains partial insulin response to tolbutamide, supporting preserved KATP-channel responsiveness in β-cell dysfunction |
| [4593820](https://pubmed.ncbi.nlm.nih.gov/4593820/) | 1974 | Case report | Arch Dis Child | Neonatal hypoglycaemia with congenital pancreatic islet malformation — clinical overlap with pancreatic agenesis-like phenotypes |
| [471523](https://pubmed.ncbi.nlm.nih.gov/471523/) | 1979 | Case report | Padiatr Padol | Beckwith-Wiedemann syndrome with β-cell hyperplasia/hyperinsulinism — illustrates congenital pancreatic developmental disorders affecting insulin secretion |
| [9519717](https://pubmed.ncbi.nlm.nih.gov/9519717/) | 1998 | Basic science | Diabetes | Experimental NIDDM rat model with preserved insulin responsiveness to glucose and sulfonylureas |
| [180358](https://pubmed.ncbi.nlm.nih.gov/180358/) | 1976 | Case series | Mayo Clin Proc | 60-case insulinoma series — clinical context for pancreatic islet/endocrine dysfunction relevant to differential diagnosis |

## Singapore Market Information

Tolbutamide is not currently marketed in Singapore (0 registrations on file). No authorization records are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all marked as data gaps in this evidence pack — this is flagged as a **blocking** gap (DG001) that must be resolved before any safety screening can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to indirect mechanistic and case-based literature (L4) with zero direct clinical trials on pancreatic agenesis; the drug is unregistered in Singapore; and a blocking data gap (missing TFDA-equivalent warnings/contraindications) prevents even a preliminary safety assessment. Additionally, 9 of the 10 TxGNN-predicted indications for this drug — including the highest-scoring one — were assessed as biologically implausible KG artifacts, indicating the model's predictions for this drug should be treated cautiously overall.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/HSA-equivalent label warnings and contraindications) — currently blocking
- Resolve DG002 (formal MOA documentation from DrugBank)
- Genetic confirmation protocol distinguishing KATP-channel-mutation PNDM from other causes of pancreatic agenesis, to identify the subgroup plausibly responsive to sulfonylurea therapy
- A pilot case series or study directly testing tolbutamide (not just the analogous glyburide) in confirmed KATP-channel-mutation pancreatic agenesis/PNDM patients
- Singapore registration pathway assessment, since the drug currently has no market presence here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

