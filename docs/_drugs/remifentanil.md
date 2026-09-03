---
layout: default
title: Remifentanil
parent: 僅模型預測 (L5)
nav_order: 851
evidence_level: L5
indication_count: 10
---

# Remifentanil
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

# Remifentanil: From Anesthesia Analgesia to Common Cold

## One-Sentence Summary

> Remifentanil is an ultra-short-acting μ-opioid receptor agonist used as an analgesic adjunct during general anesthesia; no formal original indication record was found in the regulatory data provided.
> TxGNN predicts a possible association with **Common Cold** (viral upper respiratory infection), scoring **98.68%**,
> but the supporting evidence — **2 clinical trials** and **2 publications**, none actually studying common cold — indicates this is most likely a knowledge-graph co-occurrence artifact rather than a genuine pharmacological relationship.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not documented in evidence pack. Per drug class, Remifentanil is clinically used as an ultra-short-acting opioid analgesic adjunct in general anesthesia. |
| Predicted New Indication | Common Cold |
| TxGNN Prediction Score | 98.68% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on known clinical context, Remifentanil is an ultra-short-acting μ-opioid receptor agonist used solely as an analgesic component during general anesthesia. It has no established pharmacological pathway relevant to common cold, which is a self-limiting viral upper respiratory infection.

The evidence review flags this prediction as likely a **knowledge-graph co-occurrence artifact**: opioid analgesics are frequently mentioned in surgical/anesthesia literature alongside a wide range of unrelated conditions purely because patients undergoing surgery may incidentally have a cold, not because the drug treats it. Both clinical trials retrieved for this indication are perioperative airway-management studies (video laryngeal mask airway comparison, paravertebral nerve blocks) with no relevance to respiratory infection treatment — both were graded "C" (low relevance) in the underlying review.

Neither of the two associated publications addresses common cold either: one examines pain from propofol injection, the other describes awake craniotomy technique for glioma resection. There is no mechanistic, clinical, or literature basis connecting Remifentanil to common cold treatment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06950957](https://clinicaltrials.gov/study/NCT06950957) | N/A | Recruiting | 64 | Compares video laryngeal mask airway vs. endotracheal tube for airway safety during septoplasty; unrelated to common cold treatment (relevance grade C). |
| [NCT06841822](https://clinicaltrials.gov/study/NCT06841822) | N/A | Recruiting | 168 | Evaluates paravertebral nerve block techniques for hemodynamic stability during thoracoscopic lung lobectomy; unrelated to common cold treatment (relevance grade C). |

Neither trial evaluates Remifentanil for common cold; both are incidental perioperative anesthesia studies.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21179290](https://pubmed.ncbi.nlm.nih.gov/21179290/) | 2010 | RCT | Korean J Anesthesiol | Evaluates combination of cold (temperature) propofol and remifentanil pretreatment to reduce propofol injection pain — unrelated to common cold (URI) treatment. |
| [25909573](https://pubmed.ncbi.nlm.nih.gov/25909573/) | 2015 | Review/Case series | J Neurosurg | Describes awake craniotomy technique for glioma resection over a 27-year period; remifentanil mentioned as an anesthetic component, not related to common cold. |

---

## Singapore Market Information

No marketing authorization records were found. Remifentanil is currently **not marketed** in Singapore according to the regulatory data provided (0 registrations).

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: A blocking data gap (DG001) was identified — official product-label warnings/contraindications have not yet been retrieved, which prevents a full S1 safety pre-assessment.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but evidence level is L5 (model prediction only) with no clinical trial or literature evidence actually studying Remifentanil for common cold. The retrieved trials and publications are incidental anesthesia-context mentions, and the underlying mechanistic rationale in the evidence pack itself concludes this is likely a knowledge-graph co-occurrence artifact rather than a real signal.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank (DG002)
- Official TFDA/HSA label warnings and contraindications (DG001, currently blocking safety pre-assessment)
- If further repurposing exploration is desired, consider prioritizing the higher-evidence candidate in this pack — **headache disorder** (rank 9, evidence level L3, recommendation "Research Question") — though existing trials there are also perioperative analgesia studies rather than dedicated headache-disorder trials, and opioid use for primary headache treatment is discouraged by current clinical guidelines
- Regulatory pathway assessment, since the drug is not currently marketed in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

