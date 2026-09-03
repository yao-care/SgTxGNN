---
layout: default
title: Tislelizumab
parent: 僅模型預測 (L5)
nav_order: 987
evidence_level: L5
indication_count: 10
---

# Tislelizumab
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

# Tislelizumab: From Advanced Solid Tumors to Mixed-Type Autoimmune Hemolytic Anemia

## One-Sentence Summary

Tislelizumab is an anti-PD-1 immune checkpoint inhibitor used in oncology (e.g., esophageal cancer, NSCLC, per literature in this evidence pack); it is not currently registered or marketed in Singapore.
The TxGNN model's top prediction is **Mixed-Type Autoimmune Hemolytic Anemia**, but this candidate has **no clinical trials and no supporting literature (L5)**.
More importantly, the drug's own mechanism argues *against* this prediction — PD-1 inhibitors are well documented to **cause**, not treat, immune-mediated hemolytic anemia as an adverse event, and this pattern repeats across most of the top 10 TxGNN hits for this drug (see note below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced solid tumors (e.g., esophageal cancer, NSCLC) — inferred from literature within this evidence pack; no official Singapore-approved indication text exists as the drug is not registered |
| Predicted New Indication | Mixed-type autoimmune hemolytic anemia |
| TxGNN Prediction Score | 93.76% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on literature cited within the pack, Tislelizumab is a humanized IgG4 anti-PD-1 monoclonal antibody that blocks the PD-1/PD-L1 checkpoint pathway to reactivate anti-tumor T-cell immunity, and is used for advanced solid tumors including esophageal cancer.

This mechanism does **not** support the top-ranked prediction. Autoimmune hemolytic anemia is a recognized immune-related adverse event (irAE) of PD-1 inhibitors — releasing the "brake" on T cells can trigger autoimmune attack on red blood cells, the opposite of a therapeutic effect. The evidence pack's own rationale explicitly flags this as a likely **reversed-direction artifact**: TxGNN appears to have learned "drug–disease co-occurrence" from adverse-event reporting data rather than a genuine treatment relationship. No clinical trial or publication in this pack supports using Tislelizumab to *treat* autoimmune hemolytic anemia.

**Batch-level pattern warning:** This is not an isolated issue. Of the top 10 TxGNN candidates for this drug, at least 6 (ranks 1, 2, 4, 5, 8, 10 — hemolytic anemias, PNH, CD59 deficiency, dermatomyositis) follow the same reversed-mechanism pattern, and the two candidates with actual literature support (rank 3: dermatitis; rank 6: proteinuria) are populated almost entirely by case reports and pharmacovigilance studies describing Tislelizumab-**induced** SJS/TEN, DRESS, agranulocytosis, and renal thrombotic microangiopathy — i.e., adverse-event evidence, not therapeutic evidence. This suggests a systematic confound in this prediction batch that should be flagged before further evaluation of any candidate in this set.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for mixed-type autoimmune hemolytic anemia.

---

## Literature Evidence

Currently no related literature available for mixed-type autoimmune hemolytic anemia.

---

## Singapore Market Information

Tislelizumab is currently **not registered or marketed in Singapore** (0 authorizations on file).

---

## Cytotoxicity

Tislelizumab is an oncology therapeutic (immune checkpoint inhibitor), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 immune checkpoint inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low direct myelosuppression; however, literature in this pack documents a rare case of Tislelizumab-induced agranulocytosis (PMID 38910480), so hematologic monitoring is still warranted |
| Emetogenicity Classification | Low (immune checkpoint inhibitors are minimally emetogenic as monotherapy) |
| Monitoring Items | CBC with differential, liver function, renal function/urinalysis (proteinuria, TMA reported — PMID 40528285, 40420929), thyroid function, skin examination (SJS/TEN, DRESS reported — PMID 41346629, 40447060, 41268547) |
| Handling Protection | Standard precautions for parenteral monoclonal antibody administration; not classified under conventional cytotoxic drug handling regulations, but institutional hazardous-drug policy should be confirmed |

---

## Safety Considerations

No formal safety data (warnings, contraindications, or drug interactions) is available in this evidence pack — please refer to the package insert for safety information once available.

**Note from literature evidence in this pack:** although not part of the formal `safety` dataset, publications retrieved for other candidate indications (dermatitis, proteinuria) document severe immune-related adverse events attributed to Tislelizumab, including Stevens-Johnson syndrome/toxic epidermal necrolysis, DRESS syndrome, agranulocytosis, and renal thrombotic microangiopathy. These should be factored into any future safety review of this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (mixed-type autoimmune hemolytic anemia) has no clinical or literature support (L5) and is mechanistically contradicted by known PD-1 inhibitor pharmacology — the condition is a documented adverse effect of this drug class, not a treatable target. The broader prediction batch shows the same reversed-direction pattern, indicating a likely systematic issue with this TxGNN run for Tislelizumab rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (currently blocking — DG001)
- Confirmed mechanism of action data from DrugBank (currently high-impact gap — DG002)
- Manual review of NCT07190027 (rank 3, dermatitis) to confirm whether it studies Tislelizumab as an irAE-management trial rather than a dermatitis treatment trial, before any further action on that candidate
- If pursuing this drug for repurposing evaluation at all, request a re-run or manual audit of the TxGNN prediction batch to rule out adverse-event/therapeutic-relationship confounding before evaluating lower-ranked candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

