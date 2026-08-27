---
layout: default
title: Potassium Iodide
parent: 僅模型預測 (L5)
nav_order: 674
evidence_level: L5
indication_count: 10
---

# Potassium Iodide
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

Using the report template supplied in the system prompt (this is a direct content-generation task from the given Evidence Pack — no additional codebase skill applies), here is the evaluation report.

Note on data handling: `drug.original_indications` is empty and `original_moa` is flagged `[Data Gap]` (DG002), and `taiwan_regulatory.licenses` is empty (drug not marketed, DG001 also flags missing official label data). Per the "no [Data Gap] token, no guessing" rules, I've stated plainly where data is missing rather than inventing specifics, and used `predicted_indications[0]` (nasal cavity disease) as the lead candidate per the template's field mapping.

---

# Potassium Iodide: From an Undocumented Original Indication to Nasal Cavity Disease

## One-Sentence Summary

> The original approved indication and mechanism of action for Potassium Iodide are not documented in this evidence pack (a confirmed data gap — see below). The TxGNN model predicts potential activity against **Nasal Cavity Disease**, with **0 clinical trials** and **4 case-report-level publications** (mostly veterinary) currently supporting this direction — evidence is exploratory and hypothesis-generating only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — DrugBank record was located, but indication and mechanism-of-action text was not extracted (data gap DG002) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.95% (rank 1,107 among candidate list) |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Potassium Iodide is not available in this evidence pack (data gap DG002), so a full mechanistic justification cannot be constructed from sourced data alone. Based on the supporting literature that *is* available, the rationale is built around potassium iodide's long-recognized role as an adjunct treatment for subcutaneous/deep fungal infections (most notably sporotrichosis, historically treated with saturated solution of potassium iodide, SSKI). The proposed mechanism involves immune-modulatory and antifungal-adjunct activity, which is biologically plausible for extension to nasal-cavity fungal disease.

The literature identified for this candidate consists of case reports of rhinofacial fungal infections — rhinofacial pythiosis in sheep, mycotic rhinitis (Aspergillus fumigatus) in a horse, Pseudallescheria boydii nasal infection in a horse, and one human case of nasofacial zygomycosis where potassium iodide produced a rapid clinical response. These reports describe the nasal cavity as a site of fungal disease responsive to iodide-based therapy, which is consistent with the TxGNN prediction linking Potassium Iodide to "nasal cavity disease" as a broad disease category.

However, three of the four supporting reports are veterinary, and the sole human report is a single case from 1994 with no controls. This is a plausible mechanistic hypothesis rather than a validated indication signal, and it should not be read as evidence of efficacy in common nasal cavity conditions (e.g., allergic rhinitis, sinusitis) — the supporting evidence is specific to invasive fungal rhinitis/rhinofacial mycoses, a narrow and uncommon subset of "nasal cavity disease."

## Clinical Trial Evidence

Currently no related clinical trials registered for Nasal Cavity Disease.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7997795](https://pubmed.ncbi.nlm.nih.gov/7997795/) | 1994 | Case report (human) | Revista do Instituto de Medicina Tropical de São Paulo | Human case of nasofacial zygomycosis (nasal cavity mucosa involvement); rapid clinical response to potassium iodide therapy |
| [34902797](https://pubmed.ncbi.nlm.nih.gov/34902797/) | 2022 | Case report (veterinary) | Journal de mycologie médicale | Potassium iodide successfully used to treat rhinofacial pythiosis (Pythium insidiosum) in sheep, a disease causing nasal cavity masses and facial deformity |
| [39576399](https://pubmed.ncbi.nlm.nih.gov/39576399/) | 2024 | Case report (veterinary) | Veterinary Research Communications | Mycotic rhinitis (Aspergillus fumigatus) in a horse treated with topical clotrimazole plus oral potassium iodide |
| [10976304](https://pubmed.ncbi.nlm.nih.gov/10976304/) | 2000 | Case report (veterinary) | Journal of the American Veterinary Medical Association | Pseudallescheria boydii nasal cavity infection in a horse treated with topical miconazole and intravenous sodium iodide (related iodide compound, not potassium iodide specifically) |

## Singapore Market Information

Potassium Iodide currently has no marketing authorization on record in Singapore — market status is "Not Marketed" with 0 registered licenses. No product/dosage-form data is available to tabulate.

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-drug interaction data were retrievable in this evidence pack (DDI query returned no results), and this is compounded by a **Blocking**-severity data gap (DG001): official label warnings/contraindications have not yet been obtained, which by itself prevents this candidate from entering the S1 initial safety review stage.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The supporting evidence for a nasal cavity disease indication consists entirely of case reports (three veterinary, one human, from 1994–2024) with no clinical trials or controlled studies, and the mechanism-of-action data needed to justify biological plausibility is itself a documented gap (DG002). Combined with the **Blocking** safety data gap (DG001) — which explicitly prevents progression to the S1 safety evaluation stage — this candidate is not ready to advance beyond a research question.

**To proceed, the following is needed:**
- Official label/package-insert safety data (warnings, contraindications) to resolve the Blocking data gap (DG001) and unlock S1 safety review
- Drug mechanism-of-action data from DrugBank to substantiate the mechanistic rationale (DG002)
- Controlled or comparative clinical evidence beyond isolated case reports, ideally in human rhinofacial fungal disease rather than veterinary cases
- Clarification of which specific nasal cavity disease subtype (e.g., invasive fungal rhinitis specifically, not nasal cavity disease broadly) the prediction should be scoped to, since the current supporting literature is narrow

**Additional note:** Two lower-priority candidates in this evidence pack — *tracheal disease* (rank 9, L4) and *laryngitis* (rank 10, L3, the strongest evidence base in this pack with 16 literature citations and 1 completed Phase 4 RCT) — appear, on inspection of the underlying rationale, to reflect potassium iodide's well-established role in preoperative preparation for Graves' disease thyroidectomy rather than genuinely novel indications. These may warrant separate triage as label-extension/practice-consolidation questions rather than new repurposing candidates.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

