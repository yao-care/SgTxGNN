---
layout: default
title: Magnesium Oxide
parent: 僅模型預測 (L5)
nav_order: 624
evidence_level: L5
indication_count: 10
---

# Magnesium Oxide
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

Using the drug-repurposing evaluation report template supplied in this prompt (no additional skill applies — this is a fully self-contained content-generation task from a provided Evidence Pack, not a coding/debugging/creative-build task that would trigger a process skill).

Before writing, I verified the Evidence Pack directly rather than trusting memory: `original_indications` is `[]`, `taiwan_regulatory.licenses` is `[]` (market_status "未上市", total_licenses 0), `original_moa` is a Data Gap, and — critically — `predicted_indications[0]` (rank 1, "calcium-alkali syndrome," score 0.98) carries a `repurposing_rationale.mechanistic_link` that explicitly flags the sole supporting literature item as describing magnesium oxide as a **cause** of the syndrome, not a treatment. Reporting that as a clean repurposing opportunity without surfacing this would misrepresent the underlying data, so the report leads with that caveat.

---

# Magnesium Oxide: From Antacid/Magnesium Supplement (Unregistered in Singapore) to Calcium-Alkali Syndrome

## One-Sentence Summary

> Magnesium oxide has no on-file original indication in Singapore (it is not currently marketed here) and is generically known worldwide as an antacid, osmotic laxative, and oral magnesium supplement.
> The TxGNN model's top-ranked prediction links it to **Calcium-Alkali Syndrome** with a very high score (**98.00%**), but the only supporting evidence — **1 clinical trial** (low relevance) and **1 case report** — describes magnesium oxide as a **cause** of this syndrome, not a treatment for it.
> This appears to be a reversed-causality artifact rather than a genuine repurposing signal, and is flagged accordingly below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — magnesium oxide is not registered in Singapore. (Generically used elsewhere as an antacid / osmotic laxative / oral magnesium supplement.) |
| Predicted New Indication | Calcium-Alkali Syndrome |
| TxGNN Prediction Score | 98.00% (0.9800) |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for magnesium oxide is not available in this Evidence Pack (Data Gap, high severity — see Conclusion). Based on general pharmacological knowledge, magnesium oxide is an inorganic mineral compound used as an antacid (neutralizes gastric acid), an osmotic laxative, and an oral magnesium/electrolyte supplement — none of which is documented in the Singapore regulatory data here, since the product is not currently registered locally.

Calcium-alkali syndrome (the modern term for what was historically called milk-alkali syndrome) is a condition of hypercalcemia, metabolic alkalosis, and acute kidney injury, classically triggered by excessive intake of calcium and/or absorbable alkali — including magnesium- and calcium-containing antacids/supplements, especially in combination with vitamin D. That overlap in substance class is almost certainly why the TxGNN model assigned a high topological similarity score.

**However, the directionality is inverted.** The single literature item behind this prediction (PMID 19185403) reports calcium-alkali syndrome that developed *because of* combined vitamin D and magnesium oxide administration — i.e., magnesium oxide as an etiological/precipitating agent, not a therapeutic agent. This is a known failure mode for graph-based repurposing models: drug and disease terms that co-occur in the same publication (here, in a causation context) can be scored as if they had a treatment relationship. The score of 98% should therefore be read as a **safety signal warranting caution about magnesium oxide use in patients at risk of hypercalcemia/alkalosis**, not as evidence of a new therapeutic indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04708340](https://clinicaltrials.gov/study/NCT04708340) | Phase 1/2 | Unknown | 237 | Double-blind, placebo-controlled multicenter trial of RJX (Rejuveinix) in COVID-19 patients. Not a magnesium oxide or calcium-alkali syndrome treatment study — graded **Relevance C**; likely indexed via calcium/renal-function keyword overlap rather than a direct match. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19185403](https://pubmed.ncbi.nlm.nih.gov/19185403/) | 2009 | Case Report | American Journal of Kidney Diseases | Describes calcium-alkali syndrome **caused by** combined vitamin D and magnesium oxide administration — magnesium oxide identified here as a causative agent, not a treatment. |

---

## Singapore Market Information

Magnesium oxide currently has **no HSA registrations on file** in this Evidence Pack (`total_licenses = 0`, `market_status = 未上市 / Not Marketed`). No authorization records, product names, or approved indication text are available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data were returned for this compound in this Evidence Pack.

*(Note: the mechanistic caution described above — risk of hypercalcemia/metabolic alkalosis/acute kidney injury with concurrent vitamin D and magnesium oxide use — comes from the literature evidence reviewed for the predicted indication itself, not from a structured safety database, and should be verified against the official package insert once available.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The headline prediction (calcium-alkali syndrome, 98% score) is not a credible repurposing opportunity — the only supporting literature describes magnesium oxide as causing this condition, not treating it. Advancing this candidate on the strength of the TxGNN score alone would be acting on a likely reversed-causality artifact.
- Separately, this Evidence Pack contains a **Blocking** data gap (DG001: no TFDA/HSA package-insert warnings or contraindications available) — no candidate for this drug can be safety-cleared (Stage S1) until that gap is closed, regardless of which indication is pursued.

**To proceed, the following is needed:**
- Obtain and parse the official package insert (TFDA/HSA) for warnings, contraindications, and precautions (DG001, Blocking).
- Obtain detailed mechanism-of-action data via the DrugBank API (DG002, High) to properly assess mechanistic plausibility for any candidate indication.
- If pursuing magnesium oxide repurposing further, redirect attention to the pack's other ranked candidates with stronger and correctly-directed evidence rather than rank 1 — notably **duodenal ulcer (disease)** (rank 8, Evidence Level L2, decision stage S2, "Proceed with Guardrails," supported by multiple mid-20th-century controlled/RCT-type antacid trials) and, to a lesser extent, **gastroduodenitis** and **stomach disease** (both L3, S1, "Research Question"), all of which are mechanistically consistent with magnesium oxide's established antacid action.
- Confirm magnesium oxide's Singapore registration status directly with HSA, since this Evidence Pack shows zero licenses on file.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

