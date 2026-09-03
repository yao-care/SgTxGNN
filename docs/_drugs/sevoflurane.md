---
layout: default
title: Sevoflurane
parent: 僅模型預測 (L5)
nav_order: 901
evidence_level: L5
indication_count: 10
---

# Sevoflurane
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

# Sevoflurane: From General Anesthesia to Prinzmetal Angina

## One-Sentence Summary

Sevoflurane is an inhalational general anesthetic used to induce and maintain surgical anesthesia. The TxGNN model's top prediction suggests possible efficacy for **Prinzmetal Angina**, but this is currently a **model-only prediction with no supporting clinical trials or literature**, and available data actually points in the opposite direction (inhalational anesthetics are associated with coronary spasm risk, not benefit).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text on file) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Singapore Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on general pharmacological knowledge, Sevoflurane is an inhalational general anesthetic that acts primarily by enhancing inhibitory GABA-A receptor conductance and antagonizing NMDA receptors, producing central nervous system depression and loss of consciousness. It has no established original indication text in this dataset, but its clinical use as a surgical anesthetic is well known.

There is no coherent mechanistic pathway linking Sevoflurane's central anesthetic action to Prinzmetal angina, which is caused by focal coronary artery vasospasm. In fact, the evidence pack's own rationale notes that some inhalational anesthetics have been clinically associated with **triggering or worsening coronary spasm** — a safety signal that runs counter to, rather than supports, this predicted indication. This top-ranked prediction, along with most of the other nine candidates (Tourette syndrome, fibromyalgia, tendinitis, myositis variants, trichotillomania, migraine, etc.), appears to reflect knowledge-graph node proximity effects rather than genuine pharmacological rationale — none currently have supporting treatment-intent clinical trials, and where literature exists, it discusses Sevoflurane's use *as an anesthetic during surgery* for patients who happen to have these conditions, not its use *to treat* the conditions themselves.

## Clinical Trial Evidence

Currently no related clinical trials registered for Prinzmetal Angina.

*(Note: Across all 10 predicted indications, only one loosely related trial exists — [NCT03789370](https://clinicaltrials.gov/study/NCT03789370) for migraine disorder — which studies postoperative headache as a side effect of Sevoflurane anesthesia, not treatment efficacy.)*

## Literature Evidence

Currently no related literature available for Prinzmetal Angina.

## Singapore Market Information

Sevoflurane has no registered licenses in Singapore (0 registrations, market status: 未上市/Not marketed). No authorization table is available.

## Safety Considerations

Please refer to the package insert for safety information.

*(Both key warnings and contraindications are marked as data gaps in the source pack; no drug interaction data was found.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trials, no literature, and no plausible mechanistic link supporting Prinzmetal angina as an indication — it is a pure L5 model prediction, and the available safety context (coronary spasm risk with inhalational anesthetics) actively argues against pursuing it. The drug is also not currently marketed in Singapore, and core safety data (warnings, contraindications, MOA) are flagged as blocking data gaps in the source pack.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (currently blocking data gap, DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Any preclinical or mechanistic literature specifically linking Sevoflurane to coronary vasospasm modulation (to resolve the apparent contradiction with known coronary spasm risk)
- Re-evaluation against lower-ranked but better-evidenced candidates (e.g., tendinitis, fibromyalgia) if a repurposing signal is still considered worth pursuing, though these too currently lack treatment-intent evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

