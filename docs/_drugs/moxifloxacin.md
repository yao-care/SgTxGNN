---
layout: default
title: Moxifloxacin
parent: 僅模型預測 (L5)
nav_order: 682
evidence_level: L5
indication_count: 10
---

# Moxifloxacin
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

# Moxifloxacin: From Bacterial Infections to Bubonic Plague

## One-Sentence Summary

Moxifloxacin is a fluoroquinolone antibiotic used broadly for bacterial infections; it is not currently registered or marketed in Singapore. Among 10 TxGNN-predicted indications in this evidence pack, most (including the top-ranked "hyperamylasemia," score 99.98%) have **zero supporting evidence** and are model artifacts. The one candidate with genuine mechanistic and preclinical support is **Bubonic Plague (Yersinia pestis infection)**, backed by **6 preclinical/in-vitro publications** (no clinical trials, no local safety data on file).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Singapore-approved indication on file — the product is not currently marketed here. Based on known pharmacology, moxifloxacin is a fluoroquinolone used for respiratory tract, skin/soft-tissue, and other bacterial infections. |
| Predicted New Indication | Bubonic Plague (Yersinia pestis infection) |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L3 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Structured mechanism-of-action data for moxifloxacin is not populated in this evidence pack (DrugBank field flagged as a data gap, DG002). However, the supporting literature converges on a well-established pharmacological rationale: moxifloxacin is a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV, blocking DNA replication. This mechanism gives it direct antibacterial activity against *Yersinia pestis*, the causative organism of plague.

Critically, this is not a novel mechanistic leap — other fluoroquinolones in the same class (ciprofloxacin, levofloxacin) are already approved for plague treatment under the FDA Animal Rule pathway (efficacy shown via animal models and in vitro data, since human RCTs are not ethically feasible for a rare, high-mortality biothreat pathogen). Multiple animal and in vitro pharmacodynamic studies in this pack directly demonstrate moxifloxacin's potency against *Y. pestis*, including full survival protection in mouse models of systemic and pneumonic plague. The prediction is therefore best understood as class-extension: moxifloxacin extending an indication already validated for its pharmacological siblings, rather than a mechanistically novel therapeutic hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21115791](https://pubmed.ncbi.nlm.nih.gov/21115791/) | 2011 | In vitro PK/PD model | Antimicrobial Agents and Chemotherapy | Hollow-fiber PK/PD model used to derive a moxifloxacin dosing regimen that maximizes *Y. pestis* kill and suppresses resistance emergence |
| [20052916](https://pubmed.ncbi.nlm.nih.gov/20052916/) | 2009 | Animal/Experimental | Antibiotiki i khimioterapiia | Moxifloxacin (ED50 5.5–14.0 mg/kg), levofloxacin, and lomefloxacin showed high efficacy against FI+ and FI- *Y. pestis* strains in a mouse model |
| [15555886](https://pubmed.ncbi.nlm.nih.gov/15555886/) | 2004 | Animal/Experimental | International Journal of Antimicrobial Agents | Oral moxifloxacin and gatifloxacin gave full protection in a BALB/c mouse model of systemic and pneumonic plague, comparable to ciprofloxacin |
| [21486959](https://pubmed.ncbi.nlm.nih.gov/21486959/) | 2011 | In vitro PK/PD model | Antimicrobial Agents and Chemotherapy | Comparative in vitro PK/PD study benchmarking candidate antibiotics, including moxifloxacin, against *Y. pestis* relative to the streptomycin gold standard |
| [29623187](https://pubmed.ncbi.nlm.nih.gov/29623187/) | 2018 | Case Report | Therapeutic Advances in Drug Safety | Case of moxifloxacin-induced tinnitus in an older adult; notes FDA-recommended fluoroquinolone use is restricted to specific infections including plague — a safety signal, not efficacy evidence |
| [26210091](https://pubmed.ncbi.nlm.nih.gov/26210091/) | 2015 | Case Report | Ticks and Tick-borne Diseases | Case of *Francisella tularensis* (tularemia, a different pathogen) in China; low direct relevance to *Y. pestis*/moxifloxacin efficacy |

## Other TxGNN-Predicted Indications (Screened Out)

The remaining 9 candidates in this evidence pack ranked higher by raw TxGNN score but carry materially weaker evidence:

- **Hyperamylasemia, polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, premalignant hematological system disease, hematological disease with acquired peripheral neuropathy, hematopoietic/lymphoid neoplasm** — no clinical trials, no relevant literature (or one unrelated case report). Evidence Level L4–L5, decision stage S0, **Hold**. These read as knowledge-graph co-occurrence noise rather than real drug–disease signals.
- **Monoclonal gammopathy** (L4, S1, Research Question) and **congenital hematological disorder** (L3, S1, Research Question) — the underlying evidence actually describes moxifloxacin treating *opportunistic infections* (e.g., Nocardiosis) in immunocompromised hematology patients, not the hematological disease itself. This is a supportive-care use case, not a new indication for the disease.

None of these are recommended for further evaluation at this time.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (research track only)**

**Rationale:**
The bubonic plague signal has real mechanistic and preclinical support consistent with an already-approved drug class, unlike the other 9 candidates in this pack, which are unsupported model artifacts. However, moxifloxacin has no clinical trial data for plague, no Singapore market presence, and no local safety label on file.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001 (TFDA/HSA label warnings and contraindications) — required before any S1 safety review can begin
- Resolve high-priority data gap DG002 (confirmed mechanism-of-action documentation from DrugBank)
- Local registration/import pathway assessment, since the product is currently not marketed in Singapore
- Confirm whether an Animal Rule-style regulatory pathway (as used for ciprofloxacin/levofloxacin in plague) is applicable, given the absence of feasible human RCTs
- Do not advance the other 9 predicted indications without new evidence — current data does not support further action
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

