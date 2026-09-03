---
layout: default
title: Tacrolimus
parent: 僅模型預測 (L5)
nav_order: 937
evidence_level: L5
indication_count: 10
---

# Tacrolimus
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

Using no additional skill — this is a direct report-generation task fully specified by the prompt template; proceeding directly.

# Tacrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

> Tacrolimus (DB00864) is a calcineurin inhibitor whose topical formulation (Protopic) is established for atopic dermatitis, and whose systemic formulation is used for organ transplant rejection prophylaxis.
> The TxGNN model predicts it may also be effective for **Seborrheic Dermatitis**,
> with **2 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic Dermatitis (topical Protopic); systemic tacrolimus is separately used for organ transplant rejection prophylaxis — no formal Singapore-registered indication text available |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (MOA marked as a data gap). Based on known pharmacology, tacrolimus is a calcineurin inhibitor that blocks the NFAT signaling pathway in T cells, downregulating antigen-specific T-cell activation and pro-inflammatory cytokine release. Its topical formulation (Protopic) has proven efficacy in atopic dermatitis, and this same anti-inflammatory mechanism is the rationale for extending its use to other inflammatory skin conditions.

Seborrheic dermatitis is a chronic inflammatory dermatological disease that, like atopic dermatitis, involves T-cell-mediated cutaneous inflammation, with an additional component of inflammatory response to Malassezia yeast colonization. Because topical tacrolimus suppresses local inflammatory cytokine release without the skin-atrophy risk associated with long-term topical corticosteroid use, it is mechanistically well-suited to seborrheic dermatitis, particularly for maintenance therapy on sensitive facial skin — a rationale directly supported by completed Phase 3/4 trials and multiple RCTs identified below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Evaluated tacrolimus ointment (Protopic) for maintenance treatment of severe facial seborrheic dermatitis in adults, aiming to reduce relapse frequency and steroid use |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Assessed proactive once/twice-weekly use of 0.1% tacrolimus ointment to maintain remission and reduce exacerbation incidence in adult facial seborrheic dermatitis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | RCT | J Am Acad Dermatol | Multicenter, double-blind RCT comparing tacrolimus 0.1% vs ciclopiroxolamine 1% for long-term maintenance therapy in severe facial seborrheic dermatitis |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | RCT | Ann Parasitol | Compared efficacy of sertaconazole 2% cream vs tacrolimus 0.03% cream in 60 patients with seborrheic dermatitis |
| [39219446](https://pubmed.ncbi.nlm.nih.gov/39219446/) | 2024 | Systematic Review/Network Meta-Analysis (Cochrane) | Clin Exp Allergy | Network meta-analysis of topical anti-inflammatory treatments, including calcineurin inhibitors, for inflammatory eczema/dermatitis |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Cohort/Clinical study | Ann Dermatol | Evaluated 0.1% tacrolimus ointment as maintenance therapy to reduce flare-ups in facial seborrheic dermatitis, extending the atopic dermatitis maintenance model |
| [12833030](https://pubmed.ncbi.nlm.nih.gov/12833030/) | 2003 | Open-label pilot study | J Am Acad Dermatol | 18 patients treated with 0.1% tacrolimus for up to 28 days; 61% achieved complete clearance of seborrheic dermatitis |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Reviewed facial seborrheic dermatitis pathophysiology and therapeutic horizons, including topical calcineurin inhibitors |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic Review | Am J Clin Dermatol | Systematic review of topical treatments (antifungals, keratolytics, corticosteroids, calcineurin inhibitors) for facial seborrheic dermatitis |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Reviewed pathophysiology, safety, and efficacy of topical calcineurin inhibitors specifically in seborrheic dermatitis |
| [37067129](https://pubmed.ncbi.nlm.nih.gov/37067129/) | 2023 | Clinical study | Indian J Dermatol Venereol Leprol | Compared oral itraconazole + topical tacrolimus vs topical tacrolimus alone for maintenance treatment of seborrheic dermatitis in Vietnam |
| [15461548](https://pubmed.ncbi.nlm.nih.gov/15461548/) | 2004 | Review | Expert Opin Pharmacother | Reviewed tacrolimus ointment use in atopic dermatitis and other inflammatory cutaneous diseases, including seborrheic dermatitis |

---

## Singapore Market Information

Tacrolimus currently has no registered product license in Singapore under this evidence pack (market status: 未上市 / Not Marketed; 0 registrations). No authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3/4 trials (NCT02004860, NCT01591070) plus multiple RCTs (e.g., PMID 33010323, 24171300) directly support tacrolimus's efficacy for maintenance treatment of facial seborrheic dermatitis, giving this candidate an L1 evidence level. However, tacrolimus is not currently registered in Singapore and this is an off-label repurposing indication, so guardrails are warranted before clinical adoption.

**To proceed, the following is needed:**
- Formal MOA and product labeling data (currently a blocking data gap)
- Singapore/TFDA package insert warnings, contraindications, and drug interaction data
- Regulatory pathway assessment given the drug is not currently marketed in Singapore
- Confirmation of dosing/formulation (topical ointment concentration) applicable to seborrheic dermatitis specifically, distinct from the approved atopic dermatitis indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

