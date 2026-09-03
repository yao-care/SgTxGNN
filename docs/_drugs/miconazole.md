---
layout: default
title: Miconazole
parent: 僅模型預測 (L5)
nav_order: 664
evidence_level: L5
indication_count: 10
---

# Miconazole
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

# Miconazole: From Fungal Infections to Acne

## One-Sentence Summary

Miconazole is an imidazole-class antifungal agent, originally used to treat superficial and systemic fungal infections such as dermatophytosis and candidiasis. The TxGNN model predicts it may also be effective for **Acne**, but this direction is currently supported by only **1 clinical trial** and **4 publications**, most of which are indirect (in vitro activity or related skin conditions rather than miconazole in acne vulgaris itself).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal infections (dermatophytosis, candidiasis — imidazole antifungal class) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Miconazole is an imidazole antifungal that inhibits fungal lanosterol 14α-demethylase, blocking ergosterol synthesis, and also inhibits fungal peroxidases; its efficacy in superficial and systemic fungal infections is well established.

The link to acne is indirect. *Propionibacterium acnes* (a bacterium implicated in acne pathogenesis) has shown in vitro susceptibility to azole antifungals, and Malassezia folliculitis — a condition frequently misdiagnosed as acne vulgaris — responds to miconazole. This creates a plausible mechanistic rationale, but it is built on adjacent conditions and in vitro data rather than direct evidence in true acne vulgaris.

The one paired clinical trial (NCT01244256) tests a different combination product (beclometasone + gentamicin + clotrimazole), not miconazole itself, and was suspended — it offers only weak, indirect support. Overall, the mechanistic story is biologically reasonable but has not been tested directly in miconazole-treated acne patients.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Evaluated a beclometasone + gentamicin + clotrimazole combination cream (not miconazole) in contaminated dermatosis with bilateral lesions; only indirectly related via shared azole antifungal class |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Review | Expert Opinion on Pharmacotherapy | Overview of miconazole's multifaceted effects on skin disorders |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Clinical/split-face study | Skin Research and Technology | Split-face assessment of mild inflammatory catamenial acne; notes oral contraceptives may help but do not clear skin |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Case series | Clinical and Experimental Dermatology | Pityrosporum (Malassezia) folliculitis frequently misdiagnosed as acne vulgaris, confirmed by histology and microscopy |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro | Biological & Pharmaceutical Bulletin | Azole antifungal agents show in vitro activity against *Propionibacterium acnes* isolated from acne vulgaris patients |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for miconazole in acne is limited to mechanistic plausibility and in vitro/indirect data (L4, Research Question stage); the only paired trial tests an unrelated combination product and was suspended. Critically, this candidate also has a **Blocking** data gap — TFDA package insert warnings/contraindications are unavailable, which prevents any initial safety assessment (S1), and the drug is not currently marketed in Singapore.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (Blocking gap, required before any safety review)
- Confirmed DrugBank mechanism-of-action data
- Direct clinical evidence of miconazole (not combination products) specifically in acne vulgaris
- Completed DDI query (currently not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

