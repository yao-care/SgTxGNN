---
layout: default
title: Leuprolide
parent: 僅模型預測 (L5)
nav_order: 586
evidence_level: L5
indication_count: 10
---

# Leuprolide
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

Using the txgnn-pipeline skill context (multi-country deployment conventions) alongside the detailed v5 report prompt supplied directly in your message — the user-supplied template is treated as the authoritative spec here. I verified every field cited below actually exists in the Evidence Pack JSON before writing it into the report.

A few things worth flagging before the report: `original_moa` is `"[Data Gap]"`, `original_indications` is an empty array, and Singapore market status is "未上市" (not marketed, 0 licenses) — so the "Original Indication" and "Singapore Market Information" sections have very little to extract. I did not invent an official original-indication field; where I reference prostate cancer / endometriosis context, that's drawn directly from the trial titles, literature abstracts, and `repurposing_rationale` text already present in the pack (NCT00002881's title, and the rank-8 endometriosis literature), not outside knowledge. I also omitted the Cytotoxicity section entirely — the pack contains no DrugBank category data and no cancer-labeled `original_indications`, so antineoplastic status can't be verified from the data given (rule 1 and 2 both fail; leuprolide is a hormonal GnRH agonist, not a conventional cytotoxic class under rule 3).

---

# Leuprolide: From Hormone-Dependent Disease to Osteoarthritis

## One-Sentence Summary

> Leuprolide is a GnRH agonist whose evidence in this pack points to use in hormone-dependent conditions (e.g., prostate cancer under androgen deprivation therapy, and endometriosis), though the pack itself does not supply a formal original-indication record.
> The TxGNN model predicts potential efficacy for **Osteoarthritis**, but this is currently backed by only **1 clinical trial** and **1 publication** — and both are actually about metastatic prostate cancer, not osteoarthritis.
> The proposed mechanism also runs **counter to known pharmacology**: arthralgia is a documented adverse effect of androgen-deprivation therapy, not a treatment target, so this top-ranked prediction should be treated as a likely false signal rather than a genuine repurposing lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available as a structured field (not registered in Singapore); trial/literature context suggests hormone-dependent conditions such as prostate cancer (androgen deprivation therapy) and endometriosis |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for leuprolide in this evidence pack. Based on the context available (trial titles and literature abstracts), leuprolide functions as a GnRH agonist used in hormone-dependent conditions such as prostate cancer (as part of androgen deprivation therapy) and endometriosis; its efficacy in those settings is well established in the broader literature, but the pack itself does not provide a verified mechanistic link to osteoarthritis.

More importantly, the pack's own repurposing rationale flags this prediction as likely **spurious**: GnRH agonists suppress sex hormones (testosterone/estrogen), and sex hormones are known to have a protective effect on joint cartilage. In clinical practice, long-term androgen deprivation therapy (the most common use of leuprolide) is known to **induce** arthralgia/joint symptoms as a side effect — it does not treat osteoarthritis. This suggests the TxGNN model may have picked up a "drug ↔ joint-related adverse event" co-occurrence signal in the knowledge graph and misread it as a therapeutic association, rather than genuine treatment evidence.

Both retrieved evidence items (one clinical trial, one publication) reinforce this concern: neither is actually about osteoarthritis — both concern metastatic/recurrent prostate cancer. There is currently no evidence in this pack that supports a genuine therapeutic effect of leuprolide on osteoarthritis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002881](https://clinicaltrials.gov/study/NCT00002881) | Phase 3 | Completed | N/A | Trial of orchiectomy/LHRH analog + flutamide ± suramin/hydrocortisone in metastatic prostate cancer. Not related to osteoarthritis — flagged in the pack as Relevance Grade C: overlap is due to leuprolide being a shared medication, not a shared disease target. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20133250](https://pubmed.ncbi.nlm.nih.gov/20133250/) | 2010 | Case Report | Clinical Breast Cancer | Case of metastatic prostatic adenocarcinoma presenting with breast skin changes mimicking inflammatory breast carcinoma. Not related to osteoarthritis. |

---

## Singapore Market Information

Leuprolide currently has no marketing authorization recorded in Singapore in this evidence pack (market status: not marketed, 0 registrations), so no product/authorization table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: this evidence pack flags TFDA/HSA package-insert warnings and contraindications as a Blocking data gap (DG001) — this must be resolved before any Stage 1 safety review can proceed. Mechanism-of-action data is also flagged as a High-severity gap (DG002).)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (osteoarthritis) has no genuine supporting evidence in this pack — the single clinical trial and single publication retrieved are both about metastatic prostate cancer, not osteoarthritis — and the proposed mechanism runs opposite to known pharmacology (arthralgia is a recognized adverse effect of androgen deprivation therapy, not a treatment target). This is consistent with the pack's own scoring of Evidence Level L5 / Decision Stage S0 / Recommendation "Hold" for this indication.

**Worth noting:** among the 10 predicted indications in this pack, rank 8 ("arthropathy") is the only one with a materially different evidence profile — Evidence Level L4, Decision Stage S1, recommendation "Research Question" — supported by a plausible mechanism (leuprolide suppressing catamenial/endometriosis-related joint pain) and 3 literature items (a case report, a cohort study, and a GnRH-agonist case report on catamenial joint pain). If this line of repurposing is pursued further, "arthropathy" (specifically catamenial/endometriosis-associated joint pain) is a substantially more credible candidate than "osteoarthritis" and should be evaluated as a separate candidate rather than folded into this one.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings, contraindications, and DDI data (DG001 — currently Blocking; safety review cannot start without it)
- Verified mechanism-of-action data from DrugBank API (DG002)
- A structured original-indication record (the pack's `original_indications` field is currently empty)
- If pursuing the joint-pain signal, dedicated evidence review of rank 8 ("arthropathy") as its own candidate, distinct from this osteoarthritis prediction
- No further investment recommended into the osteoarthritis-specific signal unless new, disease-matched evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

