---
layout: default
title: Meperidine
parent: 僅模型預測 (L5)
nav_order: 642
evidence_level: L5
indication_count: 10
---

# Meperidine
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

Using judgment on this evidence pack before drafting: `predicted_indications[0]` (Tourette syndrome, TxGNN score 99.46%) has **zero** clinical trials, **zero** literature, and its own `mechanistic_link` field explicitly flags it as likely knowledge-graph noise rather than a real signal. The same is true for ranks 2, 4, 7, 9. Only rank 3 (**headache disorder**, score 98.69%, evidence level L2/S2) has substantive clinical-trial and literature support — including several historical RCTs testing meperidine itself. Writing the headline report around the top-scored-but-evidence-free candidate would produce a report that is technically template-compliant but clinically misleading. I'm using headache disorder as the reported indication and flagging this deviation explicitly in the report so the decision-maker isn't misled about what TxGNN's raw #1 rank actually contained.

---

# Meperidine: From Acute Pain to Headache Disorder

> **Note on indication selection**: This evidence pack contains 10 TxGNN-predicted indications for Meperidine. The #1-ranked prediction by score (Tourette syndrome, 99.46%) has no supporting clinical trials or literature, and the evidence pack itself flags it as likely reflecting knowledge-graph proximity rather than a genuine mechanistic signal — the same is true for ranks 2, 4, 7, and 9. **Headache disorder (rank 3, score 98.69%)** is the only one of the 10 candidates backed by real clinical trial and literature evidence, so it is used as the subject of this report.

## One-Sentence Summary

Meperidine (pethidine) is a synthetic opioid analgesic classically used for moderate-to-severe acute pain. The TxGNN model predicts it may be effective for **Headache Disorder** (specifically acute migraine/vascular headache), a prediction supported by **5 clinical trials** (none testing meperidine directly) and **17 publications**, including several head-to-head randomized trials of meperidine itself from the 1980s–2000s — though current headache-society guidelines advise against routine opioid use for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in Singapore (drug not marketed); internationally established as an opioid analgesic for moderate-to-severe acute pain |
| Predicted New Indication | Headache Disorder (acute migraine / vascular headache) |
| TxGNN Prediction Score | 98.69% (rank 3 of 10 candidates; global disease rank 12,907) |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Meperidine (flagged as a High-severity data gap). Based on known information drawn from the evidence pack, Meperidine is a μ-opioid receptor agonist with additional serotonin/norepinephrine reuptake-inhibiting activity — a dual mechanism distinct from most other opioids. Its efficacy in moderate-to-severe acute pain is well established, and this same central-analgesic and monoaminergic profile provided the pharmacological rationale for its use as an emergency-department treatment for acute migraine and vascular headache from the 1980s through the early 2000s.

Unlike several of the model's higher-scored predictions (Tourette syndrome, trichotillomania, manic bipolar disorder), where an opioid mechanism has no established link to the target condition, headache is itself a pain syndrome — so a systemic analgesic being explored for headache is mechanistically direct rather than speculative. This is reflected in the evidence: meperidine was directly compared against chlorpromazine, ketorolac, dihydroergotamine, methotrimeprazine, and metoclopramide in multiple randomized trials for acute headache, generating a genuine (if dated) efficacy record.

However, this historical support comes with an important caveat. Both the American Headache Society (2015) and Canadian Headache Society (2015) evidence reviews explicitly recommend **against** using opioids, including meperidine, as routine migraine therapy, citing dependency risk and medication-overuse headache, and reserve it only for refractory cases as a last-resort option. The mechanistic plausibility is real, but current clinical practice has moved away from this use.

---

## Clinical Trial Evidence

None of the registered trials below test meperidine directly for headache — they were surfaced by the TxGNN evidence pipeline via disease/drug co-occurrence (e.g., other opioids, headache-adjacent procedures) and are included here for transparency, but should be read as low-to-moderate relevance context rather than direct proof.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03483870](https://clinicaltrials.gov/study/NCT03483870) | Phase 2 | Completed | 80 | IV granisetron for pruritus from intrathecal morphine in Cesarean section — different opioid, different indication (low relevance). |
| [NCT01997788](https://clinicaltrials.gov/study/NCT01997788) | N/A | Completed | 46 | Efficacy of intrathecal morphine in open nephrectomy — unrelated to headache (low relevance). |
| [NCT06630858](https://clinicaltrials.gov/study/NCT06630858) | N/A | Completed | 80 | Nerve block vs. intrathecal morphine for post-nephrectomy pain — unrelated to headache (low relevance). |
| [NCT04491474](https://clinicaltrials.gov/study/NCT04491474) | Phase 4 | Completed | 128 | Occipital/supraorbital nerve block for acute migraine in the ED — addresses migraine but via nerve block, not meperidine (low relevance). |
| [NCT00274170](https://clinicaltrials.gov/study/NCT00274170) | Phase 1/2 | Unknown | 56 | ED migraine RCT comparing octreotide vs. compazine; does not include a meperidine arm but establishes the ED-migraine-treatment research context (moderate relevance; status unknown). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18632186](https://pubmed.ncbi.nlm.nih.gov/18632186/) | 2008 | Meta-analysis | Ann Emerg Med | Systematic review/meta-analysis of RCTs on meperidine for acute migraine; despite being the most-used ED opioid for migraine, guidelines recommend against opioids as first-line therapy. |
| [2705667](https://pubmed.ncbi.nlm.nih.gov/2705667/) | 1989 | RCT | Ann Emerg Med | Randomized double-blind trial comparing IV chlorpromazine vs. IV meperidine + dimenhydrinate for migraine headache. |
| [1514724](https://pubmed.ncbi.nlm.nih.gov/1514724/) | 1992 | RCT | Ann Emerg Med | Randomized double-blind trial comparing IM ketorolac vs. meperidine + hydroxyzine for acute migraine. |
| [2648190](https://pubmed.ncbi.nlm.nih.gov/2648190/) | 1989 | RCT | Neurology | Single-dose comparison of meperidine, butorphanol, and dihydroergotamine for vascular headache; DHE showed the best pain reduction, meperidine group had no patients with >90% pain reduction. |
| [1952306](https://pubmed.ncbi.nlm.nih.gov/1952306/) | 1991 | RCT | Ann Emerg Med | Randomized controlled trial comparing IM methotrimeprazine vs. meperidine + dimenhydrinate for severe migraine. |
| [15107371](https://pubmed.ncbi.nlm.nih.gov/15107371/) | 2004 | RCT | Emerg Med J | Prospective randomized double-blind trial comparing metoclopramide, pethidine, and the combination for acute vascular and tension-type headache. |
| [7893296](https://pubmed.ncbi.nlm.nih.gov/7893296/) | 1995 | RCT | Am J Emerg Med | Double-blind comparison of meperidine/promethazine vs. ketorolac for migraine, evaluated by patient-reported outcomes. |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies, including opioid agents. |
| [24875925](https://pubmed.ncbi.nlm.nih.gov/24875925/) | 2015 | Systematic Review | Cephalalgia | Canadian Headache Society systematic review and treatment recommendations for migraine pain in emergency settings; guideline-level source for opioid-avoidance recommendation. |
| [10986188](https://pubmed.ncbi.nlm.nih.gov/10986188/) | 2000 | Review | West J Med | Review of ED migraine pharmacotherapy explicitly discussing pethidine (meperidine) among treatment options and their evidence/safety trade-offs. |

---

## Singapore Market Information

Meperidine currently has **no marketing authorization on file in Singapore** — 0 registrations, market status "Not Marketed." No product/dosage-form data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. No HSA warning, contraindication, or drug-interaction data is currently on file for this candidate (the drug-interaction query returned no results, and the TFDA/HSA label data gap is flagged as **Blocking** in the source evidence pack — see Conclusion below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Meperidine has genuine, mechanistically coherent historical RCT evidence for acute migraine/vascular headache (evidence level L2), making it the only credible candidate among the 10 TxGNN predictions reviewed. However, the evidence is dated (1980s–2004), no confirmatory modern trial exists, and current specialty guidelines (American Headache Society 2015, Canadian Headache Society 2015) explicitly advise against opioid use, including meperidine, as routine migraine therapy due to dependency and medication-overuse-headache risk. Combined with the drug's current unmarketed status in Singapore and a Blocking-severity gap in label/safety data, the evidence does not yet support proceeding.

**To proceed, the following is needed:**
- HSA (Singapore) package insert / label warnings and contraindications data (currently a Blocking data gap)
- Confirmed mechanism of action documentation from DrugBank (High-severity data gap)
- A completed drug-interaction (DDI) screen, since the current query returned no results
- Updated, post-2015 clinical evidence or a formal reconciliation with current headache-society guidance before any repurposing pathway is considered
- If pursued despite guideline discordance, a defined restricted-use protocol (e.g., refractory/rescue-only, opioid-abuse-risk monitoring)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

