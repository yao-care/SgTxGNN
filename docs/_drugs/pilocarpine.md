---
layout: default
title: Pilocarpine
parent: 僅模型預測 (L5)
nav_order: 783
evidence_level: L5
indication_count: 10
---

# Pilocarpine
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

# Pilocarpine: From Glaucoma (Muscarinic Miotic Therapy) to Primary Hereditary Glaucoma

## One-Sentence Summary

Pilocarpine is a muscarinic (M3) receptor agonist with a globally established role in reducing intraocular pressure and stimulating salivary flow, though it is not currently registered or marketed in Singapore.
The TxGNN model's top-ranked prediction is **Primary Hereditary Glaucoma** (score 99.83%), but this specific genetic subtype currently has **0 clinical trials** and **0 publications** directly supporting it — the prediction is a mechanistic extrapolation from pilocarpine's well-documented efficacy in general open-angle glaucoma (see Ranks 3–4 below, which carry extensive L1 evidence).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / ocular hypertension (miotic agent) — globally established use; not currently registered in Singapore |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Pilocarpine is a direct-acting muscarinic (M3) receptor agonist. It induces ciliary muscle contraction and pupillary miosis, which mechanically opens the trabecular meshwork and promotes aqueous humor outflow through Schlemm's canal — this is the classic, decades-validated mechanism behind pilocarpine's use as a first-line glaucoma agent. The same M3 stimulation acting on salivary gland acinar cells also explains its separate established use as a sialogogue in xerostomia (e.g., Salagen).

Primary hereditary glaucoma is not a distinct disease at the receptor-pharmacology level — it is a genetically-determined subset of open-angle glaucoma (often linked to mutations such as *MYOC*) that shares the same downstream pathophysiology: impaired trabecular outflow leading to elevated intraocular pressure. Because pilocarpine's mechanism acts on the outflow pathway itself rather than on the upstream genetic lesion, it is biologically plausible that the drug would still lower IOP in hereditary forms of the disease.

However, TxGNN's high score here reflects proximity in the knowledge graph to "glaucoma" broadly, not evidence specific to the hereditary subtype. As the model's own rationale notes, the mechanistic link "can only be extrapolated from general open-angle glaucoma" — no trial or publication in this evidence pack has enrolled or studied a hereditary/genetically-defined glaucoma population specifically. This is why the evidence level here is L5 despite the very strong biological rationale.

---

## Clinical Trial Evidence

Currently no clinical trials are registered specifically for **Primary Hereditary Glaucoma**.

**Supporting evidence (extrapolated from general open-angle glaucoma — Ranks 3 & 4 in this evidence pack):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00803803](https://clinicaltrials.gov/study/NCT00803803) | Phase 4 | Completed | 37 | Dose-response study of pilocarpine 2% concentrations on intraocular pressure in glaucoma patients |
| [NCT02754570](https://clinicaltrials.gov/study/NCT02754570) | NA | Completed | 27 | Diurnal/nocturnal effect of pilocarpine (as adjunct to latanoprost) on IOP and ocular perfusion pressure |
| [NCT03654885](https://clinicaltrials.gov/study/NCT03654885) | Phase 4 | Completed | 158 | XEN-45 gel stent vs trabeculectomy in refractory open-angle glaucoma; pilocarpine used as background comparator therapy |
| [NCT04005079](https://clinicaltrials.gov/study/NCT04005079) | Phase 3 | Withdrawn | 0 | Planned RCT of pilocarpine after combined cataract/Trabectome surgery; withdrawn with no enrollment |
| [NCT02613013](https://clinicaltrials.gov/study/NCT02613013) | NA | Unknown | 240 | Laser iridoplasty/iridotomy trial for angle closure with multi-mechanism basis; low direct relevance (non-pharmacologic) |

*Note: none of these trials enrolled a genetically-defined hereditary glaucoma population; they are cited as mechanistic support only.*

---

## Literature Evidence

Currently no literature is available specifically on **Primary Hereditary Glaucoma** and pilocarpine.

**Supporting evidence (extrapolated from general open-angle glaucoma):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10509848](https://pubmed.ncbi.nlm.nih.gov/10509848/) | 1999 | RCT | Clinical Therapeutics | Dorzolamide vs pilocarpine as adjunctive therapy in open-angle glaucoma/ocular hypertension |
| [18721251](https://pubmed.ncbi.nlm.nih.gov/18721251/) | 2008 | RCT | Acta Ophthalmologica | Latanoprost vs pilocarpine/timolol fixed combination in POAG/ocular hypertension |
| [15846712](https://pubmed.ncbi.nlm.nih.gov/15846712/) | 2005 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Medical vs surgical interventions for open-angle glaucoma |
| [22972069](https://pubmed.ncbi.nlm.nih.gov/22972069/) | 2012 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Updated review: medical vs surgical interventions for open-angle glaucoma |
| [27347646](https://pubmed.ncbi.nlm.nih.gov/27347646/) | 2016 | RCT | JAMA Ophthalmology | Effect of pilocarpine on the Schlemm canal in healthy and open-angle glaucoma eyes |
| [36548467](https://pubmed.ncbi.nlm.nih.gov/36548467/) | 2023 | Cohort | Journal of Glaucoma | Outflow structure changes after pilocarpine in POAG vs healthy individuals (OCT-based) |
| [7916025](https://pubmed.ncbi.nlm.nih.gov/7916025/) | 1994 | RCT | Journal of Ocular Pharmacology | Metipranolol-pilocarpine fixed-dose combinations in ocular hypertension/POAG |

---

## Singapore Market Information

No registrations found — Pilocarpine is currently **not marketed** in Singapore (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data are currently available in this evidence pack (identified as a Blocking data gap — see Conclusion below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (Primary Hereditary Glaucoma) has a strong TxGNN score and a biologically coherent mechanism, but zero direct clinical trial or literature support — it is an extrapolation from the drug's well-established general open-angle glaucoma pharmacology rather than an independently validated finding. Combined with the absence of any Singapore-specific safety/label data, this indication cannot currently progress past a screening stage.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (Blocking gap — DG001)
- Formal, sourced mechanism-of-action documentation from DrugBank (DG002)
- A clinical trial or registry study enrolling a genetically-confirmed hereditary/juvenile-onset glaucoma population to test whether trabecular response to pilocarpine differs from sporadic POAG
- Consideration of Singapore market entry pathway, since the drug currently holds zero local registrations

---

## Appendix: Full Ranking Overview (All 10 Predicted Indications)

Given this evidence pack contains 10 TxGNN-predicted indications, the table below summarizes the full picture for context. Two candidates — general open-angle glaucoma and oral candidiasis/burning mouth syndrome — carry materially stronger evidence than the top-ranked hereditary glaucoma prediction and may warrant separate, dedicated evaluation.

| Rank | Disease | Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------|----------------|----------------|-----------------|
| 1 | Primary hereditary glaucoma | 99.83% | L5 | S0 | Hold |
| 2 | Oral candidiasis | 98.90% | L4 | S1 | Research Question |
| 3 | Glaucoma 1, open angle | 98.75% | L1 | S3 | Proceed with Guardrails |
| 4 | Open angle glaucoma | 98.64% | L1 | S3 | Proceed with Guardrails |
| 5 | Osteoradionecrosis of the mandible | 98.60% | L5 | S0 | Hold |
| 6 | Commissural lip fistula | 98.58% | L5 | S0 | Hold |
| 7 | Burning mouth syndrome | 98.56% | L4 | S1 | Research Question |
| 8 | Oral leukoedema | 98.56% | L5 | S0 | Hold |
| 9 | Chronic tic disorder | 96.89% | L5 | S0 | Hold |
| 10 | Benign shuddering attacks | 96.81% | L5 | S0 | Hold |

*Note: Ranks 3 and 4 represent the same underlying disease entity (open-angle glaucoma) under different ontology labels, both reflecting pilocarpine's long-established, decades-validated clinical use — not a novel repurposing candidate. Ranks 2 and 7 (oral candidiasis, burning mouth syndrome) represent the most credible genuinely novel candidates, both linked mechanistically to pilocarpine's sialogogue effect on hyposalivation, but require dedicated interventional studies before advancing further.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

