---
layout: default
title: Vitamin D
parent: 僅模型預測 (L5)
nav_order: 1063
evidence_level: L5
indication_count: 10
---

# Vitamin D
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

# Vitamin D: From Calcium/Bone Metabolism Support to Primary Release Disorder of Platelets

## One-Sentence Summary

Vitamin D (DrugBank DB11094) is broadly known as a fat-soluble secosteroid used for calcium/phosphate homeostasis and bone-related conditions; the specific approved-indication text was not provided in this evidence pack. The TxGNN model predicts potential relevance to **Primary Release Disorder of Platelets**, but this is supported by only **11 clinical trials** (nearly all unrelated to platelet disorders on manual review) and **4 publications** (mostly decades-old case reports on a different disease, myelofibrosis). The evidence is indirect and does not currently support clinical action.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (Vitamin D is generally used for calcium/bone metabolism disorders; no formal indication text available) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 93.11% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this specific product entry is not available. Based on known pharmacology, Vitamin D (via its active metabolite 1,25-dihydroxyvitamin D3, calcitriol) acts through the vitamin D receptor (VDR) to regulate calcium/phosphate homeostasis, and separately has documented roles as a differentiation-inducing agent in megakaryocyte/platelet biology.

The repurposing rationale here is weak and indirect: the only mechanistic support comes from 1980s–1990s case reports in which 1,25-dihydroxyvitamin D3 was used as a differentiation inducer in **myelofibrosis** (a bone marrow fibrosis disorder involving megakaryocyte proliferation), not in primary platelet release disorder itself. These are distinct disease entities. The high TxGNN score most likely reflects a shared "platelet/megakaryocyte" node in the underlying knowledge graph rather than a validated, disease-specific mechanism.

Critically, none of the 11 retrieved clinical trials directly studies Vitamin D in patients with primary platelet release disorder — the trial set is dominated by unrelated COVID-19, cardiac rehabilitation, sepsis, and transplant-immunosuppression studies. This is a case where a graph-based prediction carries a high similarity score but lacks a coherent, disease-specific clinical rationale.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04845971](https://clinicaltrials.gov/study/NCT04845971) | Phase 2 | Completed | 97 | GcMAF oral immunotherapy in COVID-19 pneumonia; not related to platelet disorders |
| [NCT05393362](https://clinicaltrials.gov/study/NCT05393362) | N/A | Completed | 65 | Cardiac rehabilitation biomechanics in elderly heart failure patients; graded low relevance (unrelated to platelet disorders) |
| [NCT07087561](https://clinicaltrials.gov/study/NCT07087561) | N/A | Recruiting | 360 | Nutritional support + health education after colorectal cancer surgery; no platelet-disorder focus |
| [NCT05711810](https://clinicaltrials.gov/study/NCT05711810) | Phase 4 | Completed | 1 | Single-subject study on SARS-CoV-2 spike protein circulation; unrelated |
| [NCT03980132](https://clinicaltrials.gov/study/NCT03980132) | Phase 4 | Completed | 184 | Lugol solution before thyroidectomy in Graves' disease; graded low relevance |
| [NCT06907212](https://clinicaltrials.gov/study/NCT06907212) | N/A | Enrolling by invitation | 100 | Adipocyte transcriptional network changes in obesity; unrelated |
| [NCT00596947](https://clinicaltrials.gov/study/NCT00596947) | Phase 4 | Terminated | 18 | Corticosteroid withdrawal in kidney transplant patients; unrelated |
| [NCT04659486](https://clinicaltrials.gov/study/NCT04659486) | N/A | Unknown | 100 | Pediatric/adolescent COVID-19 recovery-phase study; unrelated |
| [NCT04537559](https://clinicaltrials.gov/study/NCT04537559) | N/A | Unknown | 240,000 | COVID-19 pandemic impact on non-COVID hospital morbidity/mortality; unrelated |
| [NCT04291508](https://clinicaltrials.gov/study/NCT04291508) | Phase 2 | Completed | 488 | IV Vitamin C or acetaminophen in sepsis-induced hypotension/respiratory failure; graded low relevance, not a platelet-disorder trial |

*Note: None of the retrieved trials directly investigates Vitamin D as a treatment for primary release disorder of platelets. Manual relevance grading (where available) confirms most are off-target.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10640215](https://pubmed.ncbi.nlm.nih.gov/10640215/) | 1998 | Review | Bailliere's Clinical Haematology | Discusses idiopathic myelofibrosis pathogenesis, including megakaryocyte hyperplasia and growth factor release — a related but distinct disease from primary platelet release disorder |
| [2811498](https://pubmed.ncbi.nlm.nih.gov/2811498/) | 1989 | Case series | Medicina Clinica | Reports beneficial effect of 1,25-dihydroxyvitamin D3 in 2 cases of myelofibrosis via megakaryocyte differentiation induction; not primary platelet release disorder |
| [27885969](https://pubmed.ncbi.nlm.nih.gov/27885969/) | 2016 | Conference abstract | Critical Care | Multi-topic ICU symposium abstract collection; no specific platelet-disorder or vitamin D finding of relevance |
| [31637855](https://pubmed.ncbi.nlm.nih.gov/31637855/) | 2019 | Cohort (veterinary) | J Vet Emerg Crit Care | Serum 25-OH-D in critically ill dogs; different species, not applicable to human platelet disorders |

*Note: Literature evidence is sparse, dated, and centers on myelofibrosis rather than primary release disorder of platelets specifically.*

---

## Singapore Market Information

Vitamin D (this product entry, DB11094) currently has no marketing authorization or registered license in Singapore (0 registrations). No product/dosage form data is available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. No specific warnings, contraindications, or drug-interaction data were available in this evidence pack — notably, the TFDA/label safety review (key warnings and contraindications) is flagged as a **Blocking** data gap in the evidence pack and must be resolved before any safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link is indirect (based on a different disease, myelofibrosis, via a shared knowledge-graph node) and no clinical trial in the evidence pack directly studies Vitamin D for primary release disorder of platelets. Combined with a blocking gap in TFDA label/safety data, this candidate does not meet the bar to proceed.

**To proceed, the following is needed:**
- Resolve the blocking safety data gap (TFDA label warnings/contraindications) — required before any S1 safety screening
- Obtain confirmed mechanism of action (MOA) documentation from DrugBank/regulatory sources
- Identify at least one clinical trial or mechanistic study directly addressing Vitamin D (or its active metabolites) in primary platelet release disorder, rather than myelofibrosis by analogy
- Clarify the drug's confirmed original approved indication(s) to properly assess indication-to-indication similarity

*Note: Among the other candidates evaluated in this evidence pack, "hypoparathyroidism" (rank 9, evidence level L2, decision stage S3) is substantially better supported — it reflects an already-established standard-of-care use of active vitamin D analogs (calcitriol) rather than a novel repurposing hypothesis, and may warrant separate reporting if a hypoparathyroidism-focused report is needed.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

