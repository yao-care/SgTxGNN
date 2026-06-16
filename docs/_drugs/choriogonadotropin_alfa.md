---
layout: default
title: Choriogonadotropin Alfa
parent: 僅模型預測 (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
---

# Choriogonadotropin Alfa
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

# Choriogonadotropin Alfa: From Fertility Treatment to Peptic Esophagitis

## One-Sentence Summary

Choriogonadotropin alfa is a recombinant form of human chorionic gonadotropin (hCG), primarily used in assisted reproductive technology (ART) to trigger final follicular maturation and ovulation induction.
The TxGNN model predicts it may be relevant to **Peptic Esophagitis**, with a prediction score of **98.44%**.
However, **no clinical trials and no publications** currently support this direction — and mechanistic evidence suggests hCG may act as a **risk factor** rather than a therapeutic agent for this condition.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Assisted reproductive technology (ART); ovulation induction |
| Predicted New Indication | Peptic Esophagitis |
| TxGNN Prediction Score | 98.44% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Choriogonadotropin alfa is a recombinant hCG that binds to the luteinizing hormone/choriogonadotropin receptor (LHCGR), triggering a cAMP-mediated signalling cascade. Its primary role in fertility treatment is to mimic the endogenous LH surge, stimulating ovulation and corpus luteum formation with subsequent progesterone production.

The predicted link to peptic esophagitis is mechanistically counterintuitive and warrants careful interpretation. The repurposing rationale embedded in this Evidence Pack explicitly states that hCG → progesterone elevation → decreased lower esophageal sphincter (LES) tone → increased gastric acid reflux → esophageal mucosal injury. Clinical observations during pregnancy — a physiological state characterised by markedly elevated endogenous hCG — consistently show a parallel increase in gastroesophageal reflux disease (GERD) severity. Hyperemesis gravidarum (associated with high hCG peaks) has also been linked to esophageal mucosal damage.

This mechanistic profile strongly suggests that **hCG is more likely a promoter of peptic esophagitis than a treatment for it**. The high TxGNN prediction score may reflect graph topology effects within the knowledge graph — diseases in the same ontological cluster (esophageal disorders) tend to co-score highly — rather than a genuine therapeutic relationship. The prediction should be interpreted as a **biological signal requiring critical scrutiny**, not a straightforward repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Choriogonadotropin alfa is currently **not registered** in Singapore. No marketing authorisations were found in the regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No drug interaction data, key warnings, or contraindication data were available in this Evidence Pack. Before any further evaluation, the full prescribing information (SmPC/package insert) for Choriogonadotropin alfa must be reviewed for relevant warnings, contraindications (e.g. hormone-sensitive conditions, thromboembolic risk, ovarian hyperstimulation syndrome), and known drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction scores at L5 (model prediction only, no supporting studies), and critically, the mechanistic evidence available in this pack points in the **opposite direction** — hCG is implicated as a physiological promoter of esophageal acid exposure, not a protective or therapeutic agent. Proceeding with repurposing development for this indication is not justified at this stage.

**To proceed, the following is needed:**

- **Mechanism clarification**: Determine whether any independent pathway (beyond the progesterone-LES axis) could support a therapeutic role for hCG in peptic esophagitis
- **Preclinical evidence**: Animal or *in vitro* data demonstrating mucosal protective effects of hCG in esophageal tissue models would be required before human studies could be contemplated
- **Safety data gap resolution**: Obtain full prescribing information (MOA, key warnings, contraindications) for Choriogonadotropin alfa — currently classified as a Blocking data gap (DG001, DG002)
- **Singapore registration assessment**: If development proceeds, a regulatory pathway assessment for Singapore would be required given zero current registrations
- **Re-evaluation of prediction rationale**: Consider whether the KG high score reflects a true disease-modifying opportunity or a knowledge graph topology artefact (esophageal disease cluster co-scoring)

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

