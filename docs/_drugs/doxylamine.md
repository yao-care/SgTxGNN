---
layout: default
title: Doxylamine
parent: 僅模型預測 (L5)
nav_order: 350
evidence_level: L5
indication_count: 10
---

# Doxylamine
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

# Doxylamine: From Sleep Aid / Nausea of Pregnancy to Allergic Urticaria

## One-Sentence Summary

Doxylamine is a first-generation H1 antihistamine with anticholinergic properties, widely used over the counter as a sleep aid and as a first-line treatment for nausea and vomiting of pregnancy (NVP).
The TxGNN model predicts it may be effective for **Allergic Urticaria** with a score of **99.85%** — while no Doxylamine-specific clinical trials or publications were identified for this indication, this prediction carries strong biological plausibility as H1 antihistamines are the established first-line standard of care for urticaria under international guidelines (WHO/EAACI).
Doxylamine is **not currently registered** in Singapore.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Sleep aid (insomnia); Nausea and vomiting of pregnancy |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 (Class-level mechanistic evidence) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data from DrugBank is not yet available for this report. Based on known pharmacology and the evidence pack's repurposing rationale, Doxylamine is a **first-generation H1 receptor antagonist** (antihistamine) with significant anticholinergic and sedative properties. Its efficacy in promoting sleep (via central H1 and muscarinic blockade) and suppressing pregnancy-related nausea (via antihistamine and anticholinergic pathways at the vomiting centre) is well established in international literature.

The mechanistic link between Doxylamine and allergic urticaria is **direct and strong**. Allergic urticaria is driven by IgE-mediated or non-IgE-mediated mast cell degranulation, which releases histamine that triggers the characteristic wheal-and-flare reaction, vasodilation, and pruritus via H1 receptors in the skin. H1 receptor blockade directly suppresses all of these histamine-mediated responses — this is precisely the pharmacological mechanism shared by all H1 antihistamines, which are unanimously recommended as first-line treatment in international urticaria guidelines (EAACI/GA²LEN/EDF/WAO 2022 revision). The TxGNN score of 0.9985 reflects this direct pharmacological class effect rather than a speculative new use.

The primary clinical limitation is Doxylamine's **first-generation sedating profile**. Compared to second-generation antihistamines (cetirizine, fexofenadine, loratadine), Doxylamine crosses the blood-brain barrier readily, leading to substantially greater daytime drowsiness, cognitive impairment, and anticholinergic side effects. This limits its suitability for chronic urticaria management or patients who need to remain alert, though the sedative effect may be advantageous in specific subpopulations (e.g., urticaria with concurrent sleep disturbance or nocturnal itch predominance).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Doxylamine specifically in allergic urticaria.

---

## Literature Evidence

Currently no related literature available for Doxylamine specifically in allergic urticaria.

> **Note:** The absence of Doxylamine-specific evidence does not undermine the prediction. Class-level evidence for H1 antihistamines in urticaria is extensive; the gap reflects that researchers typically study second-generation agents rather than Doxylamine for this indication.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Formal safety data (key warnings, contraindications, and drug-drug interaction data) were not retrievable in this evaluation cycle. Clinically, as a first-generation anticholinergic antihistamine, Doxylamine is known to carry risks of sedation, urinary retention, dry mouth, and constipation; these should be evaluated before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Doxylamine's H1 receptor blockade mechanism aligns directly with the pharmacological basis of allergic urticaria treatment — this is a class-level therapeutic effect supported by extensive indirect evidence, not a speculative repurposing hypothesis. The primary guardrails concern its sedating first-generation profile and its current absence from the Singapore market, both of which require active management before deployment.

**To proceed, the following is needed:**

- Retrieve formal MOA and safety data from DrugBank (currently a data gap blocking S1 safety triage)
- Obtain and parse the package insert (e.g., from TFDA or EMA/FDA sources) to document contraindications and key warnings
- Assess Singapore HSA registration pathway — Doxylamine is not currently marketed; determine if an existing OTC or Rx registration in a comparable jurisdiction (e.g., FDA, EMA) can support a local application
- Define target patient subpopulation: identify clinical scenarios where Doxylamine's sedating profile offers a net advantage over second-generation antihistamines (e.g., urticaria with nocturnal symptom predominance or co-existing insomnia)
- Conduct a structured head-to-head positioning analysis versus cetirizine/loratadine for urticaria — clarify where Doxylamine adds unique value vs. where it is inferior
- Search for class-level evidence (any H1 antihistamine RCTs in urticaria) to upgrade the evidence grade from L4 toward L2/L3
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

