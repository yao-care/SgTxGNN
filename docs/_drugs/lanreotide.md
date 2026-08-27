---
layout: default
title: Lanreotide
parent: 僅模型預測 (L5)
nav_order: 571
evidence_level: L5
indication_count: 10
---

# Lanreotide
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

# Lanreotide: From Neuroendocrine Tumor–Associated Endocrine Syndromes to Polycystic Kidney Disease 3 (with or without Polycystic Liver Disease)

## One-Sentence Summary

> Lanreotide is a somatostatin analogue; within this evidence pack it is referenced (via a related octreotide trial) as a therapy of choice for controlling endocrine syndromes associated with neuroendocrine tumors. The TxGNN model's 10 predicted indications are dominated by low-confidence, mechanistically unsupported hits (e.g., hypertrichosis, Dandy-Walker syndrome), but one stands out: **Polycystic Kidney Disease 3 (with or without Polycystic Liver Disease)**, which has a genuine mechanistic rationale (SSTR2/cAMP pathway) and **20 supporting publications**, though **zero clinical trials were returned by this pack's own structured trial query**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Singapore/HSA data (drug unmarketed). Evidence pack context: lanreotide, like octreotide, is described as a therapy of choice for endocrine syndromes associated with neuroendocrine tumors (per NCT00990535 trial description) |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease |
| TxGNN Prediction Score | 98.84% (rank 11735 of all candidates; not the top-scoring hit, but the only one with credible supporting evidence) |
| Evidence Level | L1 (as scored in the pack) — see caveat below |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

**Caveat on Evidence Level:** The pack scores this indication as L1, but this rating relies on an externally-verified Phase 3 RCT (DIPAK-1) that is **not** part of this pack's structured `evidence.clinical_trials` results (which returned 0 trials). The 20 literature items returned are background reviews on ADPKD/PLD biology, not trial reports. Treat "L1" as provisional pending independent confirmation of the DIPAK-1 data.

---

## Why is This Prediction Reasonable?

Detailed, validated mechanism-of-action data for lanreotide is not available in this pack (`original_moa: [Data Gap]`). However, the repurposing rationale supplied with this candidate provides mechanistic detail: lanreotide is a somatostatin analogue that activates Gαi-coupled somatostatin receptor 2 (SSTR2), which inhibits cAMP production. Aberrant cAMP signaling is a well-established driver of cyst formation and growth in polycystic kidney and liver disease, so SSTR2 activation is proposed to reduce cystic epithelial proliferation and fluid secretion — this is the accepted pharmacological basis for somatostatin analogues in ADPKD/ADPLD.

Of the 10 TxGNN predictions in this pack, most (hypertrichosis, Dandy-Walker malformation, hair shaft abnormalities, genetic alopecia, thoracic malformation, etc.) are explicitly flagged in their own rationale text as lacking any mechanistic link, likely reflecting knowledge-graph node-proximity noise or ontology term collisions rather than real biology. Polycystic kidney/liver disease is the one prediction in this set with (a) a coherent, textbook-consistent mechanism, and (b) drug-specific literature support — including PMID 26126910, "Lanreotide and its Potential Applications in Polycystic Kidney and Liver Diseases," which directly discusses lanreotide's use in this disease class via SSTR-mediated cAMP blockade.

The rationale text also references, as an **externally verified** data point (i.e., sourced outside this pack's structured trial/literature queries), a completed multicenter Phase 3 RCT — DIPAK-1 (NCT01616927, ~309 patients across 4 Dutch centers; Meijer et al., *JAMA* 2018, PMID 30422235) — reporting that lanreotide significantly slowed total kidney volume (TKV) growth in ADPKD but did **not** meet its primary endpoint of slowing eGFR decline. This is a meaningful efficacy signal but not an unambiguous positive trial, and it could not be independently confirmed against this pack's own `clinicaltrials`/`pubmed` query results, which returned 0 and 20 hits respectively (none of which is the DIPAK-1 publication itself).

---

## Clinical Trial Evidence

Currently no related clinical trials registered (per this pack's structured `clinicaltrials.gov` query for Lanreotide + polycystic kidney disease 3).

*Note: the rationale text references an externally-verified trial, DIPAK-1 ([NCT01616927](https://clinicaltrials.gov/study/NCT01616927)), that did not surface in this pack's own trial query — see "Why is This Prediction Reasonable?" above. This should be independently re-verified before use in any decision document.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26126910](https://pubmed.ncbi.nlm.nih.gov/26126910/) | 2015 | Review | Current Topics in Medicinal Chemistry | Reviews lanreotide's mechanism (SSTR-mediated cAMP blockade) and rationale for use in polycystic kidney and liver disease — the most drug-specific source in this set |
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Review | Lancet | Overview of ADPKD as a systemic disorder, including liver cysts as a key extrarenal manifestation |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clinics in Liver Disease | Describes ADPKD/polycystic liver disease clinical course; notes tolvaptan's effect on ADPKD as a comparator for disease-modifying therapy |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Clinical Guideline (EASL) | Journal of Hepatology | EASL guideline covering diagnosis and management of cystic liver diseases, including polycystic liver disease |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Review | J Am Soc Nephrol | Genetic overlap and shared pathogenesis between ADPKD and ADPLD |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | Advances in Kidney Disease and Health | Genetic spectrum of polycystic kidney/liver disease and resulting phenotypes; ciliopathy-centered pathogenesis |
| [34724412](https://pubmed.ncbi.nlm.nih.gov/34724412/) | 2022 | Review | Annual Review of Pathology | Mechanisms and treatment advances in polycystic liver disease |
| [28317394](https://pubmed.ncbi.nlm.nih.gov/28317394/) | 2017 | Review | Expert Rev Gastroenterol Hepatol | Update on pathophysiology and management of polycystic liver disease, framed as a ciliopathy/cholangiopathy |
| [36200122](https://pubmed.ncbi.nlm.nih.gov/36200122/) | 2022 | Review | Hepatic Medicine: Evidence and Research | Pathophysiology, diagnosis, and treatment overview of polycystic liver disease |
| [37943238](https://pubmed.ncbi.nlm.nih.gov/37943238/) | 2023 | Review | Advances in Kidney Disease and Health | Extrarenal manifestations and complications of polycystic liver disease in ADPKD |

---

## Singapore Market Information

Lanreotide is currently **not marketed** in Singapore under this evidence pack's regulatory data (0 registrations on file). No HSA authorization records, product names, dosage forms, or approved indication text are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Important:** This is currently a **Blocking** data gap (DG001) — the drug's package insert warnings and contraindications have not yet been retrieved, so a full safety pre-assessment (S1) cannot be completed for this candidate. No drug-drug interaction data was found (query status: not found, 0 interactions).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The only credibly-supported indication among the 10 TxGNN predictions (PKD3/PLD) rests on an efficacy signal (DIPAK-1) that missed its primary endpoint and was not independently confirmed within this pack's own trial/literature queries.
- A **Blocking** safety data gap (package insert warnings/contraindications not yet retrieved) prevents completion of the initial safety assessment (S1) regardless of efficacy evidence.
- Lanreotide is currently unmarketed in Singapore, adding a regulatory-pathway question on top of the evidence gaps.

**To proceed, the following is needed:**
- Retrieve and review the HSA/manufacturer package insert (warnings, contraindications) to close DG001 (Blocking)
- Obtain verified mechanism-of-action documentation for lanreotide to close DG002 (High)
- Independently retrieve and verify the DIPAK-1 trial record (NCT01616927) and its published outcomes (PMID 30422235), since it did not appear in this pack's structured evidence
- Reassess the other 9 TxGNN-predicted indications only if new mechanistic or trial evidence emerges — as currently documented, they lack any credible support and should remain at Hold/S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

