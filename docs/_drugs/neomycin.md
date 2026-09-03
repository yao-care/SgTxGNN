---
layout: default
title: Neomycin
parent: 僅模型預測 (L5)
nav_order: 697
evidence_level: L5
indication_count: 10
---

# Neomycin
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

# Neomycin: From Bacterial Infections to Irritable Bowel Syndrome

## One-Sentence Summary

Neomycin is a non-absorbable aminoglycoside antibiotic traditionally used for intestinal bacterial infections and gut decontamination.
The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome** (specifically methane-associated, constipation-predominant IBS),
with **2 clinical trials** and **14 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections / intestinal decontamination (general drug classification; specific licensed indication text not available in this evidence pack) |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 98.55% |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed official mechanism-of-action data for Neomycin is not available in this evidence pack. Based on available evidence, Neomycin is a non-absorbable aminoglycoside antibiotic that acts locally within the intestinal lumen with minimal systemic absorption. It suppresses methane-producing gut organisms (e.g., *Methanobrevibacter smithii*) and reduces small intestinal bacterial overgrowth (SIBO) — a mechanism directly relevant to constipation-predominant IBS (IBS-C), where excess methane production is associated with prolonged colonic transit time.

The link between Neomycin's traditional use (intestinal antisepsis/decontamination) and the predicted new indication (IBS-C) is mechanistically coherent rather than coincidental: both center on modulating gut flora. This is not a broad, speculative embedding similarity — it is supported by a targeted human RCT (Pimentel 2006, PMID 16832617) showing that symptom improvement in C-IBS correlated with the degree of methane reduction on breath testing, i.e., a dose-response relationship between microbial suppression and clinical benefit.

A combination regimen (rifaximin + neomycin) has also been directly compared to neomycin alone in a double-blind, placebo-controlled RCT (NCT00945334), reinforcing that Neomycin's antibacterial effect on methanogens is an actionable, testable hypothesis in this population — not merely a graph-embedding artifact.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00945334](https://clinicaltrials.gov/study/NCT00945334) | NA | Completed | 37 | Double-blind, placebo-controlled comparison of Neomycin alone vs. Rifaximin + Neomycin in methane-positive, constipation-predominant IBS. |
| [NCT00259155](https://clinicaltrials.gov/study/NCT00259155) | Phase 2 | Completed | 92 | Multicenter RCT of Rifaximin for SIBO/IBS; Neomycin serves as a historical antibiotic comparator (~20-25% efficacy in normalizing lactulose breath test), not the primary intervention — indirect relevance. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16832617](https://pubmed.ncbi.nlm.nih.gov/16832617/) | 2006 | RCT | Digestive Diseases and Sciences | Subanalysis of a double-blind RCT: Neomycin improved constipation-predominant IBS specifically in methane-positive subjects; benefit correlated with methane elimination. |
| [19996983](https://pubmed.ncbi.nlm.nih.gov/19996983/) | 2010 | RCT/Cohort | Journal of Clinical Gastroenterology | Rifaximin + Neomycin combination was most effective among three antibiotic regimens in methane-positive IBS patients. |
| [12591062](https://pubmed.ncbi.nlm.nih.gov/12591062/) | 2003 | RCT | The American Journal of Gastroenterology | Double-blind, randomized, placebo-controlled study showing normalization of lactulose breath test correlates with IBS symptom improvement after antibiotic treatment. |
| [24788320](https://pubmed.ncbi.nlm.nih.gov/24788320/) | 2014 | Review | Digestive Diseases and Sciences | Reviews antibiotic treatment of C-IBS; notes rifaximin + neomycin superior to neomycin alone in methane-positive subjects. |
| [30288076](https://pubmed.ncbi.nlm.nih.gov/30288076/) | 2018 | Review | Clinical and Experimental Gastroenterology | Reviews mechanism, gut microbiota impact, and safety of antibiotic therapy (rifaximin-focused) in IBS. |
| [22298980](https://pubmed.ncbi.nlm.nih.gov/22298980/) | 2011 | Review | Gastroenterology & Hepatology | Reviews the role of gut flora and antibiotics, including neomycin, in IBS pathophysiology and treatment. |
| [26819502](https://pubmed.ncbi.nlm.nih.gov/26819502/) | 2016 | Review | World Journal of Gastroenterology | Proposes infectious/SIBO-based etiology of IBS, supporting rationale for antimicrobial therapy. |
| [31363445](https://pubmed.ncbi.nlm.nih.gov/31363445/) | 2019 | Review | Cureus | Reviews the link between methane production and constipation-predominant IBS. |
| [24666019](https://pubmed.ncbi.nlm.nih.gov/24666019/) | 2014 | Review | Current Medical Research and Opinion | Reviews the emerging role of antimicrobials, including neomycin, in IBS management. |
| [40240267](https://pubmed.ncbi.nlm.nih.gov/40240267/) | 2025 | Cohort | Revista de Gastroenterología de México | Prospective comparative study of three antibiotic regimens (including neomycin) for SIBO treatment in IBS patients. |

## Singapore Market Information

Neomycin is currently not marketed in Singapore and has no registered authorizations in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A targeted RCT (PMID 16832617) and a supporting double-blind trial (NCT00945334) demonstrate a mechanistically coherent, dose-response relationship between Neomycin's antimethanogenic effect and IBS-C symptom improvement, meeting L2 evidence criteria. However, the drug is not currently marketed in Singapore, and formal safety/prescribing data are missing.

**To proceed, the following is needed:**
- Official product label warnings and contraindications (currently a blocking data gap preventing S1 safety review)
- Documented mechanism of action from an authoritative source (e.g., DrugBank)
- Confirmation of Singapore regulatory pathway/registration status given the drug is not currently marketed
- A larger, confirmatory Phase 3 RCT specifically in methane-positive, constipation-predominant IBS
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

