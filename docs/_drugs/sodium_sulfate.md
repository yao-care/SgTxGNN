---
layout: default
title: Sodium Sulfate
parent: 僅模型預測 (L5)
nav_order: 913
evidence_level: L5
indication_count: 10
---

# Sodium Sulfate
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

# Sodium Sulfate: From Bowel Preparation to Dyspepsia

## One-Sentence Summary

Sodium sulfate (DrugBank DB09472) is pharmacologically known as an osmotic laxative, most commonly used as a component of bowel-preparation solutions prior to colonoscopy.
The TxGNN model predicts it may be effective for **dyspepsia**, but the supporting evidence is limited and largely indirect — **3 clinical trials** (mostly low relevance) and **4 publications** (all animal colitis models, not direct treatment evidence) were retrieved, and several other candidate indications in this evidence pack appear to stem from confusion with the unrelated compound *dextran sodium sulfate (DSS)*.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bowel preparation / osmotic laxative (based on known pharmacology; no formal Singapore-registered indication text available) |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for sodium sulfate (flagged as a data gap in this evidence pack). Based on known pharmacology, sodium sulfate acts as an osmotic laxative used in bowel-cleansing regimens; it has no established receptor or pathway link to upper-GI functional symptoms such as dyspepsia.

The clinical trial and literature evidence retrieved for this candidate does not directly support the prediction. The one trial most related to the drug (bowel-preparation microbiome study) measures gut microbiota changes rather than dyspepsia outcomes, and the literature set consists entirely of animal colitis models using *dextran sodium sulfate (DSS)* — a chemically and pharmacologically distinct compound used to induce experimental colitis — where "dyspepsia" appears only as incidental background terminology (e.g., describing donepezil side effects or a herbal formula's traditional use), not as a treatment outcome for sodium sulfate itself.

Given the absence of MOA data, the lack of a plausible mechanistic link, and the risk that several retrieved records reflect drug-name confusion (sodium sulfate vs. dextran sodium sulfate), the current evidence does not meaningfully support repurposing toward dyspepsia.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06339697](https://clinicaltrials.gov/study/NCT06339697) | Phase 4 | Completed | 194 | Compared bowel-prep laxatives (incl. compounded sodium picosulfate/PEG) on gut microbiome composition after colon polypectomy; endpoint is microbiome recovery, not dyspepsia efficacy (Relevance: B) |
| [NCT07310927](https://clinicaltrials.gov/study/NCT07310927) | Phase 2/3 | Recruiting | 140 | Alginate vs. sucralfate for GERD symptom relief with PPIs; unrelated to sodium sulfate (Relevance: C) |
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Phase 2/3 | Unknown | 150 | Oxycodone vs. pregabalin for post-operative pain control; unrelated to this drug or indication (Relevance: C) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33918638](https://pubmed.ncbi.nlm.nih.gov/33918638/) | 2021 | Animal model (DSS colitis) | Molecules | Studied DSS-induced GI injury effects on donepezil pharmacokinetics in pigs; "dyspepsia" cited only as a background donepezil side effect, not a treatment outcome |
| [36614242](https://pubmed.ncbi.nlm.nih.gov/36614242/) | 2023 | Animal model (colitis) | Int J Mol Sci | Anti-colitis effects of atractylodin (an herbal compound); dyspepsia mentioned as a traditional use of the herb, unrelated to sodium sulfate |
| [40391232](https://pubmed.ncbi.nlm.nih.gov/40391232/) | 2025 | Animal model (UC) | J Inflamm Res | Evaluated a TCM formula (Si-Ni Decoction) for ulcerative colitis; dyspepsia referenced only as historical indication of the formula |
| [34207410](https://pubmed.ncbi.nlm.nih.gov/34207410/) | 2021 | Animal model (DSS colitis) | Pharmaceuticals | DSS-induced GI injury combined with galantamine in pigs; not related to sodium sulfate treatment of dyspepsia |

**Note:** None of the retrieved literature involves sodium sulfate as a therapeutic agent for dyspepsia; all four studies use dextran sodium sulfate (DSS) as a colitis-induction tool in animal models, a distinct compound from the candidate drug.

## Singapore Market Information

Sodium sulfate currently has **no marketing authorization** in Singapore (market status: 未上市 / Not Marketed, 0 registrations on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (dyspepsia) lacks a plausible mechanistic rationale, and the associated clinical trial and literature evidence is either low-relevance or reflects apparent confusion with the unrelated compound dextran sodium sulfate (DSS). Combined with missing MOA data and no current Singapore market presence, the evidence does not support proceeding at this stage. This pattern of DSS/sodium sulfate conflation also affects several lower-ranked candidates in this evidence pack (e.g., dry eye syndrome, stomach disease, sclerosing cholangitis), further reducing confidence in the overall prediction set.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for sodium sulfate (DrugBank query — currently a High-severity data gap, DG002)
- TFDA/HSA label warnings and contraindications (currently a Blocking data gap, DG001)
- Re-screening of literature/trial evidence to exclude records referring to dextran sodium sulfate rather than sodium sulfate itself
- If pursued further, a dedicated mechanistic hypothesis connecting osmotic laxative pharmacology to dyspepsia symptomatology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

