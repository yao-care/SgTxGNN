---
layout: default
title: Sucralfate
parent: 僅模型預測 (L5)
nav_order: 927
evidence_level: L5
indication_count: 10
---

# Sucralfate
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

# Sucralfate: From Peptic Ulcer Disease to Duodenogastric Reflux

## One-Sentence Summary

Sucralfate is a non-absorbed mucosal protectant historically used for duodenal and gastric ulcer disease (formal original-indication text is not recorded in this evidence pack). The TxGNN model predicts it may also be effective for **Duodenogastric Reflux**, with **no registered clinical trials** but **13 supporting publications**, including at least two randomized controlled trials directly testing sucralfate in bile/alkaline reflux gastritis — a condition mechanistically adjacent to duodenogastric reflux.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (literature consistently describes sucralfate as a duodenal/gastric ulcer mucosal protectant) |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (DrugBank MOA field) is not available for sucralfate in this evidence pack. Based on descriptions found within the supporting literature itself, sucralfate is a basic aluminium salt of sucrose octasulfate that, upon contact with acid, forms a viscous, adhesive gel that binds preferentially to ulcerated or inflamed mucosa. It adsorbs pepsin and **bile acids**, stimulates local bicarbonate and mucus secretion, and forms a physical barrier against further chemical injury — a mechanism explicitly noted as relevant to bile-mediated mucosal damage (PMID 1611711, 2190304).

Duodenogastric reflux (DGR) is defined by retrograde flow of bile-laden duodenal contents into the stomach, producing bile/alkaline reflux gastritis. Because sucralfate's bile-acid-adsorbing and cytoprotective properties were already studied in closely related conditions — post-cholecystectomy alkaline reactive gastritis and dyspepsia associated with duodenogastric reflux gastritis — there is a direct, literature-supported mechanistic bridge between sucralfate's known ulcer-healing action and its candidate use in DGR, even though it has never been formally indicated for DGR.

The strongest support comes from two randomized controlled trials: one comparing sucralfate to placebo in symptomatic alkaline reflux gastritis after gastric surgery (PMID 3839973), and one comparing sucralfate to rabeprazole or no treatment in post-cholecystectomy alkaline reactive gastritis (PMID 12923369) — both testing sucralfate in populations whose pathophysiology overlaps substantially with duodenogastric reflux.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3839973](https://pubmed.ncbi.nlm.nih.gov/3839973/) | 1985 | RCT | Am J Med | Double-blind RCT (n=23) of sucralfate 6g/day vs placebo in alkaline reflux gastritis after Billroth I/II or vagotomy/pyloroplasty |
| [12923369](https://pubmed.ncbi.nlm.nih.gov/12923369/) | 2003 | RCT | Eur J Gastroenterol Hepatol | Randomized trial: sucralfate vs rabeprazole vs no treatment for post-cholecystectomy alkaline reactive gastritis |
| [3475771](https://pubmed.ncbi.nlm.nih.gov/3475771/) | 1987 | RCT | Scand J Gastroenterol Suppl | Prospective randomized trial of sucralfate vs placebo in symptomatic/macroscopic gastritis, comparing GERD vs duodenogastric reflux presentations |
| [1391144](https://pubmed.ncbi.nlm.nih.gov/1391144/) | 1992 | Comparative clinical trial | Minerva Gastroenterol Dietol | 18 patients with DGR-associated dyspepsia treated with cisapride or sucralfate 4g/day for 2 months |
| [17285081](https://pubmed.ncbi.nlm.nih.gov/17285081/) | 2006 | Review | Journal de chirurgie | Comprehensive review of duodenogastric/gastroesophageal bile reflux pathophysiology, diagnosis, and therapeutic management |
| [14723838](https://pubmed.ncbi.nlm.nih.gov/14723838/) | 2004 | Review | Curr Treat Options Gastroenterol | Reviews DGR-induced alkaline esophagitis; notes PPIs as best medical treatment, difficulty of medical/surgical management |
| [6372664](https://pubmed.ncbi.nlm.nih.gov/6372664/) | 1984 | Review | Annu Rev Med | Alkaline reflux (bile) gastritis and esophagitis pathophysiology, diagnosis, and clinical features |
| [3838414](https://pubmed.ncbi.nlm.nih.gov/3838414/) | 1985 | Review | Am J Gastroenterol | ACG committee review of sucralfate's non-ulcer/cytoprotective uses, including gastritis and esophagitis, noting need for further study |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Case series | Eur J Pediatr | First documented pediatric series (n=6) of primary duodenogastric reflux, refractory to classical antacid therapy |
| [2186496](https://pubmed.ncbi.nlm.nih.gov/2186496/) | 1990 | Case series | Terapevticheskii arkhiv | 72 patients with erosive/ulcerous gastroduodenal lesions treated with sucralfate (Antepsin), beneficial effect on pain and healing |

## Singapore Market Information

No marketing authorizations are currently registered in Singapore for sucralfate (0 licenses on file; market status: not marketed).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The meta-level data gap DG001 (missing TFDA/HSA package-insert warnings and contraindications) is flagged as **Blocking**, explicitly preventing entry into the S1 safety-review stage — this overrides the moderate mechanistic and literature-based promise (L3 evidence, two directly relevant RCTs in bile/alkaline reflux gastritis) seen for the duodenogastric reflux indication. Sucralfate is also not currently marketed or registered in Singapore, adding a regulatory-pathway barrier independent of indication-level evidence.

**To proceed, the following is needed:**
- Official HSA/manufacturer package insert data — key warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action from DrugBank or primary pharmacology sources (DG002, High)
- Clarification of Singapore import/registration pathway, since the product currently has zero local licenses
- A dedicated clinical trial or systematic review of sucralfate specifically in duodenogastric reflux (current evidence is drawn from closely related but not identical conditions — alkaline/bile reflux gastritis)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

