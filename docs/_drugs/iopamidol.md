---
layout: default
title: Iopamidol
parent: 僅模型預測 (L5)
nav_order: 539
evidence_level: L5
indication_count: 10
---

# Iopamidol
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

# Iopamidol: From Iodinated Contrast Imaging to Prinzmetal Angina

## One-Sentence Summary

Iopamidol is a non-ionic, low-osmolality iodinated contrast medium with decades of established clinical use in CT scanning, coronary/pulmonary angiography, myelography, and CT-lymphography. The TxGNN model predicts it may have a new therapeutic role in **Prinzmetal angina** (variant angina, driven by coronary artery vasospasm), with a prediction score of **98.57%**. However, there are currently **no clinical trials** and **no published studies** directly supporting this specific indication — the prediction rests entirely on model inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Iodinated contrast medium for CT imaging, angiography, myelography, and lymphography |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 98.57% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Iopamidol. Based on known information, Iopamidol is a non-ionic triiodobenzoate compound used exclusively as a diagnostic contrast agent. It enhances X-ray attenuation through its high iodine content and has been extensively characterised for its low osmolality and minimal ionic charge — properties that make it significantly less cardiotoxic than older ionic contrast media such as diatrizoate.

Prinzmetal angina (variant angina) is caused by episodic focal coronary artery vasospasm rather than fixed atherosclerotic obstruction. The TxGNN model's prediction may be capturing a vascular physiology signal within the knowledge graph: Iopamidol has a well-documented, comparatively inert haemodynamic profile in high-risk cardiovascular patients. Several included pulmonary hypertension studies (ranks 9 in this pack) confirm that, unlike ionic agents, Iopamidol causes only modest changes in vascular resistance and pulmonary artery pressure. This vasomotor neutrality, if reflected in coronary vasculature, could theoretically inform research into vasospasm modulation.

However, a direct pharmacological mechanism by which Iopamidol could therapeutically prevent or reverse coronary vasospasm remains entirely speculative. Iopamidol is currently used only as a diagnostic tool, not as a vasoactive agent. The TxGNN prediction likely reflects indirect graph-level co-associations (e.g., shared vascular pathways, angiography procedure nodes) rather than a direct drug–disease pharmacology relationship. Independent expert cardiology and pharmacology review is strongly recommended before any further investment in this direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Iopamidol is not currently registered with the Health Sciences Authority (HSA) of Singapore. No marketing authorisations were identified in the regulatory database.

> **Note:** Iopamidol is approved and widely marketed in other major jurisdictions (e.g., USA as Isovue®, EU, Japan). The absence of Singapore registration would need to be addressed before any clinical application within Singapore.

---

## Safety Considerations

No safety data (warnings, contraindications, or drug interactions) was retrieved in this Evidence Pack. Key safety considerations known from global product labelling include:

- **Contrast-induced nephropathy**: Risk is elevated in patients with pre-existing renal impairment, diabetes, or dehydration; adequate hydration and monitoring of renal function are required.
- **Hypersensitivity reactions**: Range from mild (flushing, urticaria) to severe anaphylactoid reactions; pre-medication with corticosteroids and antihistamines should be considered in high-risk patients.
- **Thyroid dysfunction**: Iodinated contrast can interfere with thyroid function tests and trigger thyrotoxicosis in susceptible individuals.

Please refer to the originator package insert (e.g., Isovue® full prescribing information) for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical, observational, or preclinical evidence directly linking Iopamidol to a therapeutic effect in Prinzmetal angina. The high TxGNN score (98.57%) is likely driven by indirect vascular-pathway associations in the knowledge graph rather than a validated pharmacological mechanism. A diagnostic contrast agent repurposed for coronary vasospasm therapy represents a significant mechanistic leap that requires independent scientific justification before any resources are committed.

**To proceed, the following is needed:**
- A mechanistic hypothesis explaining how Iopamidol could therapeutically modulate coronary vasospasm (consult cardiology and vascular pharmacology experts)
- Targeted literature search for any preclinical data on iodinated contrast agents and coronary artery tone regulation
- Full safety profile review: obtain and parse the originator package insert for contraindications, warnings, and known drug interactions relevant to coronary disease patients
- Regulatory pathway assessment: Iopamidol is not registered in Singapore; HSA marketing authorisation would be required before any clinical investigation
- TxGNN model interpretability review: examine which graph edges or node associations are driving this prediction to determine if the signal has genuine therapeutic relevance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

