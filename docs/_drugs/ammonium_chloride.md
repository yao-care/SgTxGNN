---
layout: default
title: Ammonium Chloride
parent: 僅模型預測 (L5)
nav_order: 93
evidence_level: L5
indication_count: 10
---

# Ammonium Chloride
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

# Ammonium Chloride: From Expectorant to Acute Laryngopharyngitis

## One-Sentence Summary

Ammonium chloride is a traditional expectorant and urinary acidifier, historically used as an ingredient in cough preparations and for urinary pH correction, with no registered indication in Singapore.
The TxGNN model predicts it may be effective for **Acute Laryngopharyngitis**, currently supported by **0 clinical trials** and **0 publications** for this specific indication.
The evidence base is solely model-driven (Evidence Level L5), placing this at the earliest speculative stage and requiring substantial further research before any clinical consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; traditionally used as expectorant and urinary acidifier |
| Predicted New Indication | Acute Laryngopharyngitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (Model prediction only, no actual studies) |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacological knowledge, ammonium chloride acts primarily as a **systemic acidifying agent** and **expectorant**: it lowers urinary and systemic pH by donating hydrogen ions following hepatic metabolism of the ammonium ion, and stimulates the secretory cells of the respiratory mucosa to increase mucus production while reducing its viscosity, thereby facilitating airway clearance.

The theoretical link to acute laryngopharyngitis rests on this expectorant property. By promoting secretion from the pharyngolaryngeal mucous membranes, ammonium chloride may in principle assist in clearing inflammatory secretions that accumulate during acute upper respiratory tract infection. The acidifying effect on local tissue microenvironments has also been proposed to inhibit bacterial colonisation, as many respiratory pathogens thrive under neutral to mildly alkaline conditions.

However, this mechanistic rationale is highly indirect and speculative. Acute laryngopharyngitis is predominantly viral in aetiology and is managed with symptomatic care; the direct contribution of an expectorant to mucosal inflammation resolution has never been rigorously demonstrated in a controlled study for this condition. The high TxGNN score most likely reflects a knowledge graph structural association with upper respiratory tract disease categories rather than a validated pharmacological signal. The prediction should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Ammonium chloride is currently not registered in Singapore. No marketing authorisations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug–drug interaction data were not available in this Evidence Pack (Data Gap DG001). Safety characterisation is a blocking requirement before any further evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score is very high (99.94%), the evidence base for this specific indication consists entirely of a model output with no supporting clinical trials, no published literature, and unresolved safety data gaps — conditions that preclude any further advancement at this stage.

**To proceed, the following is needed:**

- **Resolve safety data gaps**: Obtain the package insert / prescribing information to establish key warnings, contraindications, and known drug interactions (Data Gap DG001 — Blocking severity)
- **Characterise the mechanism of action**: Query DrugBank API to retrieve full MOA data (Data Gap DG002 — High severity)
- **Targeted literature review**: Conduct a broader search to identify any pre-clinical or observational data supporting ammonium chloride in pharyngolaryngeal inflammation beyond what was retrieved in this evidence cycle
- **Consider higher-evidence candidates**: The TxGNN prediction for **Headache Disorder** (Rank 7) reached Evidence Level L4 with five historical clinical publications directly involving ammonium chloride (including case series from the 1950s on achlorhydric migraine); this indication may represent a more tractable starting point for a mechanistic re-evaluation study
- **Mechanistic validation**: If the expectorant hypothesis for laryngopharyngitis is to be pursued, an in vitro study using pharyngolaryngeal mucosal cell models (e.g., secretion volume and viscosity assays) should be designed to generate primary evidence before any human study is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

