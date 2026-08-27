---
layout: default
title: Methylnaltrexone
parent: 僅模型預測 (L5)
nav_order: 653
evidence_level: L5
indication_count: 10
---

# Methylnaltrexone
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

Using judgment on this evidence pack before drafting: rank 1 ("congenital hypotrichosis milia") is the technical `predicted_indications[0]`, but its own `repurposing_rationale` explicitly states there is *zero* mechanistic or empirical support, and the same is true for ranks 2–6, 8, 10 (rank 9 is even flagged as an obsolete ontology term). The only candidate with any literature backing and a stage beyond S0/Hold is **rank 7, "respiratory failure"** (L4, S1, "Research Question"). Reporting on rank 1 as if it were the lead candidate would misrepresent the evidence pack's own analysis, so this report focuses on the one indication the data actually supports, and documents why the others were screened out.

---

# Methylnaltrexone: From Opioid-Induced Constipation to Respiratory Failure (Opioid-Induced Respiratory Depression)

## One-Sentence Summary

> Methylnaltrexone is a peripherally-restricted μ-opioid receptor antagonist (PAMORA class) whose established use is opioid-induced constipation.
> Among 10 indications predicted by TxGNN, only **Respiratory Failure** (rank 7, score 71.98%) carries any supporting literature — **2 indirect publications, no clinical trials** — while the other 9 top-ranked candidates (including the nominal #1 hit) have no mechanistic or empirical support at all and are excluded from further evaluation below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Opioid-induced constipation (OIC) — based on internationally approved labeling; not present in the Singapore regulatory dataset supplied (licenses list is empty) |
| Predicted New Indication | Respiratory Failure (opioid-induced respiratory depression context) |
| TxGNN Prediction Score | 71.98% (rank 7 of candidate list; graph rank 44,697) |
| Evidence Level | L4 (preclinical/mechanistic literature only, no trials) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for methylnaltrexone is flagged as a data gap in this evidence pack (`DG002`, High severity). Based on generally available pharmacological knowledge and the rationale text generated alongside this prediction, methylnaltrexone is a peripherally-selective μ-opioid receptor antagonist that does not cross the blood-brain barrier — it blocks opioid effects in peripheral tissues (e.g., the gut, where it treats opioid-induced constipation) while preserving central analgesia.

The proposed link to respiratory failure follows the same logic applied to a different peripheral/receptor-adjacent target: opioid-induced respiratory depression is mediated substantially through μ1-opioid receptors, including peripheral and vagal pathways. A drug that selectively blocks peripheral μ-opioid activity could, in theory, blunt opioid-induced respiratory suppression without reversing central pain control — this is a recognized research direction for PAMORA-class drugs (opioid-induced respiratory depression, OIRD), not a novel hypothesis invented by this model.

However, this remains a mechanistic hypothesis, not a validated one. The evidence pack contains only two indirect publications (below) and **no clinical trials testing methylnaltrexone in respiratory failure or OIRD specifically**. The evidence level is therefore capped at L4, and the decision stage is S1 ("Research Question") — appropriate for hypothesis generation, not for clinical or regulatory action.

**Note on the other 9 predicted indications:** Ranks 1–6, 8, and 10 (congenital hypotrichosis milia, hypotrichosis simplex of the scalp, exercise-induced malignant hyperthermia, common cold, alopecia, diffuse alopecia areata, familial periodic paralysis, trigeminal autonomic cephalalgia) each returned zero clinical trials and zero literature hits, and each rationale text explicitly states there is no known mechanistic link to opioid receptor pharmacology. Rank 9 ("obsolete hyperuricemia (disease)") is additionally flagged as a deprecated ontology term and is likely a data-quality artifact rather than a real signal. None of these are carried forward.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41087032](https://pubmed.ncbi.nlm.nih.gov/41087032/) | 2025 | Preclinical/Pharmacology | American Journal of Physiology – Lung Cellular and Molecular Physiology | Compared peripheral vs. central μ1-opioid receptor contributions to fentanyl-induced apnea and respiratory depression in conscious rats; supports peripheral μ-opioid receptor blockade as a candidate strategy against opioid-induced respiratory depression |
| [21164413](https://pubmed.ncbi.nlm.nih.gov/21164413/) | 2010 | Other/Commentary | Critical Care Medicine | General commentary on ICU life-support and multi-organ-failure management; not specific to methylnaltrexone or opioid pharmacology, limited direct relevance |

---

## Singapore Market Information

Methylnaltrexone is **not currently registered** in Singapore — the evidence pack lists 0 authorizations and no license records.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all marked as unavailable in this evidence pack — `DG001`, Blocking severity — and must be sourced from HSA/manufacturer labeling before any safety review proceeds.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Only indirect, preclinical-level literature supports a mechanistic link between methylnaltrexone and opioid-induced respiratory depression (L4, S1 "Research Question" stage) — there are no clinical trials testing this indication, no MOA confirmation, and no safety label data available, and the drug is not marketed in Singapore. This is a plausible research hypothesis, not an evidence base sufficient for clinical or regulatory advancement.

**To proceed, the following is needed:**
- Resolve `DG001` (Blocking): obtain official HSA/manufacturer package insert for warnings, contraindications, and DDI data
- Resolve `DG002`: confirm mechanism of action via DrugBank API/pharmacology reference rather than relying on general knowledge
- Re-run literature/trial search using more specific terms ("methylnaltrexone" + "opioid-induced respiratory depression"/"OIRD") — the current "respiratory failure" query is broad and only returned 2 indirect hits
- If mechanistic rationale holds up, scope a preclinical or early-phase mechanistic study evaluating peripheral μ-opioid blockade in opioid-induced respiratory depression
- Do not pursue ranks 1–6, 8, or 10 further — each lacks any clinical, literature, or mechanistic support per the evidence pack's own analysis, and rank 9 appears to be a deprecated/obsolete disease-term artifact rather than a genuine signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

