---
layout: default
title: Pirfenidone
parent: 僅模型預測 (L5)
nav_order: 790
evidence_level: L5
indication_count: 10
---

# Pirfenidone
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

# Pirfenidone: From Idiopathic Pulmonary Fibrosis to Fibroblastic Neoplasm (1 of 10 Candidate Indications)

## One-Sentence Summary

Pirfenidone is an oral antifibrotic agent referenced in the evidence pack as approved for **idiopathic pulmonary fibrosis (IPF)**. TxGNN generated **10 candidate repurposing indications**, but 9 of them (including the top-ranked "extracutaneous mastocytoma," score 99.71%) have **zero supporting clinical trials or literature** and are classified Hold/L5. Only one candidate — **Fibroblastic Neoplasm** (e.g. Dupuytren's disease, desmoid tumour) — has actual literature support (L3), though it comes with a conflicting safety signal: two case reports of sarcoma/dermatofibroma occurring after pirfenidone use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic Pulmonary Fibrosis (IPF) — referenced in rationale text; not separately confirmed via `original_indications` (field empty) |
| Predicted New Indication (evidence-supported) | Fibroblastic Neoplasm (rank 9/10, the only candidate with literature evidence) |
| TxGNN Prediction Score | 99.23% (fibroblastic neoplasm); highest-scoring candidate overall is extracutaneous mastocytoma at 99.71% but has no evidence |
| Evidence Level | L3 (fibroblastic neoplasm); all other 9 candidates are L5 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

**Note on the top TxGNN-ranked candidate:** "Extracutaneous mastocytoma" (rank 1, score 99.71%) is a KIT-mutation-driven mast cell disease with no mechanistic overlap to pirfenidone's TGF-β pathway and no supporting trials/literature — this appears to be a knowledge-graph topology artifact rather than a genuine signal, and is not further detailed below.

---

## All Predicted Indications (TxGNN Ranking)

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|------|------|------|
| 1 | Extracutaneous mastocytoma | 99.71% | L5 | Hold |
| 2 | Dermatofibrosarcoma protuberans | 99.41% | L5 | Hold |
| 3 | Aggressive systemic mastocytosis | 99.33% | L5 | Hold |
| 4 | Heart fibrosarcoma | 99.29% | L5 | Hold |
| 5 | Conventional fibrosarcoma | 99.26% | L5 | Hold |
| 6 | Familial Mediterranean fever | 99.25% | L5 | Hold |
| 7 | Kidney fibrosarcoma | 99.24% | L5 | Hold |
| 8 | Hepatic infarction | 99.24% | L5 | Hold |
| **9** | **Fibroblastic neoplasm** | **99.23%** | **L3** | **Research Question** |
| 10 | Low grade fibromyxoid sarcoma | 99.19% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank (flagged as a data gap). Based on literature cited in this evidence pack, pirfenidone is known as an oral, non-cytotoxic antifibrotic agent that inhibits TGF-β1, PDGF, EGF and FGF-mediated cytokine signalling, reducing fibroblast/myofibroblast proliferation and collagen synthesis. This mechanism underlies its approval for idiopathic pulmonary fibrosis.

Fibroblastic neoplasm covers a family of fibroblast/myofibroblast-driven proliferative diseases (e.g., Dupuytren's disease, desmoid tumour). Since TGF-β1 is a key stimulator of myofibroblast activity in these conditions — the same pathway pirfenidone targets in IPF — there is genuine mechanistic overlap, and this is the one candidate among the 10 predictions with in vitro and pilot clinical evidence behind it.

However, this mechanistic plausibility is counterbalanced by an important safety signal: two independent case reports describe pirfenidone use preceding **undifferentiated pleomorphic sarcoma** and **aggravated multiple dermatofibromas**. This suggests the drug's effect on fibroblast/myofibroblast biology may not be uniformly anti-proliferative across all fibroblastic lesions, and the direction of effect (therapeutic vs. potentially pro-tumorigenic) may depend on the malignancy grade of the target lesion. This must be resolved before any indication in this disease family is pursued further.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for fibroblastic neoplasm. (A small uncontrolled pilot study exists — see Literature Evidence below — but it is not a registered clinical trial.)

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12907346](https://pubmed.ncbi.nlm.nih.gov/12907346/) | 2003 | Pilot Clinical Trial (uncontrolled) | Am J Gastroenterology | Pilot study of pirfenidone in FAP-associated desmoid tumours; broad-spectrum antifibrotic agent reported to block TGF-β1, PDGF, EGF, FGF and prevent new fibrotic lesion formation |
| [27835939](https://pubmed.ncbi.nlm.nih.gov/27835939/) | 2016 | Preclinical (in vitro) | BMC Musculoskeletal Disorders | Pirfenidone inhibits TGF-β1-mediated myofibroblast activity in Dupuytren's disease-derived fibroblasts |
| [30927912](https://pubmed.ncbi.nlm.nih.gov/30927912/) | 2019 | Preclinical (mechanistic) | BMC Musculoskeletal Disorders | Pirfenidone modulates TGF-β1 non-SMAD signalling pathways in Dupuytren's disease fibroblasts |
| [35129055](https://pubmed.ncbi.nlm.nih.gov/35129055/) | 2022 | Preclinical (drug delivery) | Pharmaceutical Development and Technology | Local injectable pirfenidone formulation proposed to halt progression of Dupuytren's nodules to cords |
| [29702057](https://pubmed.ncbi.nlm.nih.gov/29702057/) | 2018 | Case Report (safety signal) | The Permanente Journal | Undifferentiated pleomorphic sarcoma reported following pirfenidone use — potential pro-tumorigenic signal |
| [32572469](https://pubmed.ncbi.nlm.nih.gov/32572469/) | 2020 | Case Report (safety signal) | Rheumatology (Oxford) | Multiple eruptive dermatofibromas aggravated by pirfenidone (with mycophenolate mofetil) in a systemic sclerosis patient |

---

## Singapore Market Information

Pirfenidone currently has **no marketing authorization on file** — `taiwan_regulatory.market_status` is "未上市" (Not Marketed) with 0 registered licenses. No dosage form or brand information is available.

---

## Safety Considerations

Official safety label data (key warnings, contraindications, drug interactions) is not available — flagged as a **blocking data gap (DG001)**, meaning this candidate cannot yet complete a formal safety review (S1 stage).

**Literature-reported safety signal (not from official labeling):**
- Two case reports link pirfenidone use to fibroblastic/soft-tissue lesion changes: undifferentiated pleomorphic sarcoma occurring after treatment ([PMID 29702057](https://pubmed.ncbi.nlm.nih.gov/29702057/)), and aggravation of multiple eruptive dermatofibromas in a systemic sclerosis patient on combination therapy ([PMID 32572469](https://pubmed.ncbi.nlm.nih.gov/32572469/)). These are uncontrolled observations but directly relevant to the fibroblastic neoplasm indication and should not be overlooked.

For all other safety information, please refer to the official package insert once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Official regulatory safety data (warnings/contraindications) is a blocking gap that prevents this candidate from completing initial safety review, the drug is not currently marketed in Singapore, and 9 of 10 TxGNN-predicted indications have no supporting evidence at all. The one indication with literature support — fibroblastic neoplasm — carries a genuine but unresolved safety concern (case reports of sarcoma/dermatofibroma following pirfenidone use) that must be investigated before any "Go" or "Proceed with Guardrails" decision.

**To proceed, the following is needed:**
- Obtain official package insert / regulatory safety label (warnings, contraindications, DDI) — currently blocking
- Confirm authoritative MOA data from DrugBank or product labeling
- Pharmacovigilance review of the sarcoma/dermatofibroma safety signal (PMID 29702057, 32572469) to determine causality and risk boundary
- If advancing the fibroblastic neoplasm indication, design a controlled trial building on the FAP-desmoid tumour pilot study (PMID 12907346) with adequate sample size
- Assess Singapore market entry feasibility, given zero current registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

