---
layout: default
title: Piperacillin
parent: 僅模型預測 (L5)
nav_order: 787
evidence_level: L5
indication_count: 10
---

# Piperacillin
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

# Piperacillin: From Bacterial Infections to Rheumatoid Arthritis

## One-Sentence Summary

> Piperacillin is a broad-spectrum penicillin-class antibiotic used to treat bacterial infections (no specific indication text was provided in this evidence pack). The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but this prediction is supported by **0 clinical trials** and only incidental literature co-occurrence — the drug's own repurposing rationale in this evidence pack explicitly states there is **no known mechanistic link** between piperacillin's antibacterial action and RA's autoimmune pathology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (Piperacillin is a beta-lactam antibiotic for bacterial infections; no license/indication text available) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on general pharmacological knowledge, piperacillin is an extended-spectrum penicillin that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins — a mechanism with no known relevance to the TNF-α/IL-6-mediated synovial inflammation that drives rheumatoid arthritis.

The evidence pack's own rationale for this candidate is explicit: **"無。Piperacillin 為抗生素，與 RA 自體免疫病理機轉（TNF-α、IL-6 介導的滑膜炎）無已知作用路徑"** — there is no known mechanistic pathway connecting piperacillin to RA pathology. The associated literature does not describe piperacillin treating RA; instead, every relevant paper describes RA patients (often on immunosuppressants like methotrexate, etanercept, or upadacitinib) who developed a **secondary bacterial infection** that was then treated with piperacillin/tazobactam or another antibiotic. This is a classic confounding pattern for knowledge-graph models: the drug and disease co-occur frequently in the literature because immunosuppressed RA patients are more prone to infection, not because the drug treats RA itself.

Given this, the high TxGNN score should be interpreted as a statistical artifact of literature co-occurrence rather than a biologically plausible repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37599303](https://pubmed.ncbi.nlm.nih.gov/37599303/) | 2023 | Case Report | Orthopädie (Heidelberg) | RA patient on upadacitinib developed prosthetic knee infection; treated with piperacillin/tazobactam for concurrent pneumonia — antibiotic used for infection, not RA. |
| [22605835](https://pubmed.ncbi.nlm.nih.gov/22605835/) | 2012 | Case Report | BMJ Case Reports | RA patient on methotrexate/etanercept developed purulent pericarditis; empirical piperacillin-tazobactam started for infection, not disease-modifying therapy. |
| [36945293](https://pubmed.ncbi.nlm.nih.gov/36945293/) | 2023 | Case Report | Cureus | RA patient in remission developed recurrent pleural effusion; no piperacillin/RA treatment link, purely a comorbidity case report. |
| [38343452](https://pubmed.ncbi.nlm.nih.gov/38343452/) | 2024 | Case Report | Proc (Bayl Univ Med Cent) | Low-dose methotrexate toxicity causing pancytopenia in an RA patient; unrelated to piperacillin. |
| [34178513](https://pubmed.ncbi.nlm.nih.gov/34178513/) | 2021 | Case Report | Cureus | Methotrexate-induced pancytopenia in RA; diagnostic challenge case, no antibiotic repurposing relevance. |
| [1921823](https://pubmed.ncbi.nlm.nih.gov/1921823/) | 1991 | Case Report | Med J Aust | Accidental methotrexate overdose causing pancytopenia in an RA patient; no piperacillin relevance. |
| [41268563](https://pubmed.ncbi.nlm.nih.gov/41268563/) | 2025 | Case Report | Front Immunol | 20-year RA patient on immunosuppressants developed E. coli bullous erysipelas/septic shock; antibiotics used to treat the infection, not RA. |
| [30371923](https://pubmed.ncbi.nlm.nih.gov/30371923/) | 2019 | Case Report | Orthopedics | RA patient on long-term prednisone developed emphysematous osteomyelitis; treated with antibiotic-loaded intramedullary rods, not systemic RA therapy. |
| [17576563](https://pubmed.ncbi.nlm.nih.gov/17576563/) | 2007 | Case Report | Rheumatol Int | Felty's syndrome (RA variant) patient with granulocytopenia developed disseminated candidiasis; infection management case, not RA treatment. |

All identified literature describes **antibiotic treatment of infections occurring in RA patients**, not treatment of RA itself. No RCTs, systematic reviews, or mechanistic studies support this indication.

---

## Singapore Market Information

Piperacillin currently has no registration records in Singapore (0 licenses; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were not available in this evidence pack — flagged as a Blocking data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.94%), there is zero clinical trial evidence, no mechanistic plausibility, and the available literature reflects confounded co-occurrence (antibiotics treating infections in RA patients) rather than any direct therapeutic signal for RA itself. Evidence level is L5 — model prediction only.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed mechanism of action data from DrugBank — currently a High-severity gap (DG002)
- Preclinical or mechanistic evidence for any immunomodulatory effect of piperacillin (none currently exists)
- Re-evaluation of this candidate is not recommended until independent, disease-modifying (not infection-related) evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

