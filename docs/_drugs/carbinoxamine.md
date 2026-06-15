---
layout: default
title: Carbinoxamine
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 10
---

# Carbinoxamine
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

# Carbinoxamine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Carbinoxamine is a first-generation competitive H1 antihistamine with historical US FDA approval for allergic rhinitis, urticaria, and related allergic conditions.
The TxGNN model predicts it may be effective for **Allergic Urticaria** with a prediction score of **99.99%**.
Direct Carbinoxamine-specific trial and publication data are absent from the current dataset, but the evidence level is rated **L3** based on historical FDA approval precedent and robust class-level mechanistic evidence from H1 antihistamines.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis and allergic conditions (US FDA historical approval) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Carbinoxamine is a first-generation, competitive H1 receptor antagonist. It reversibly blocks histamine binding at peripheral and central H1 receptors, suppressing the downstream cascade of vasodilation, increased vascular permeability, and pruritus that underlies allergic reactions. Although detailed MOA data is not available in the current dataset, Carbinoxamine's pharmacological class is well characterised: it shares the ethylamine scaffold with diphenhydramine and shares the competitive H1 blockade mechanism common to all first-generation antihistamines.

The mechanistic connection to allergic urticaria is direct. The core pathophysiology of allergic urticaria is IgE-mediated mast cell degranulation, releasing histamine that acts on cutaneous H1 receptors to produce the characteristic wheal-and-flare response and pruritus. Carbinoxamine blocks this receptor directly and is therefore positioned to interrupt the effector arm of the disease. At the drug-class level, H1 antihistamines (both first- and second-generation) have Phase 3 RCT support and are recommended as first-line therapy in the EAACI and British guidelines for urticaria.

Critically, US FDA records document a historical approval of Carbinoxamine for urticaria — a regulatory precedent that elevates the evidence rating beyond pure model prediction (L5) to L3, even though no Carbinoxamine-specific clinical trials or publications were identified in this evidence sweep. The principal guardrail is the sedation and anticholinergic burden characteristic of first-generation agents, which distinguishes Carbinoxamine from the better-tolerated second-generation alternatives that now dominate urticaria treatment guidelines.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for Carbinoxamine in allergic urticaria.

---

## Literature Evidence

Currently no related literature available specifically for Carbinoxamine in allergic urticaria.

---

## Singapore Market Information

Carbinoxamine is currently **not registered** in Singapore. No marketing authorisation records are available.

---

## Safety Considerations

Detailed Singapore or TFDA-specific warnings and contraindications are not available in the current dataset. The following class-level considerations apply to first-generation H1 antihistamines:

- **Central Nervous System Sedation**: First-generation antihistamines readily cross the blood-brain barrier due to high lipophilicity, causing sedation, psychomotor impairment, and cognitive effects — a clinically significant concern for patients who drive or operate machinery.
- **Anticholinergic Burden**: Dry mouth, urinary retention, constipation, blurred vision, and tachycardia are class effects. Risk is heightened in elderly patients (listed in the Beers Criteria as potentially inappropriate).
- **High-Risk Populations**: Use with caution in patients with benign prostatic hyperplasia, narrow-angle glaucoma, or significant cardiovascular disease.
- **Drug Interactions**: No interaction records were identified in this dataset. Co-administration with CNS depressants (alcohol, benzodiazepines, opioids) is expected to potentiate sedation based on class pharmacology; confirmation from the originator package insert is required.

Please refer to the US FDA-approved package insert for the complete and authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between Carbinoxamine and allergic urticaria is direct and biologically well-founded — competitive H1 blockade addresses the core effector mechanism of IgE-mediated mast cell histamine release — and a historical US FDA approval precedent for urticaria use establishes regulatory plausibility, justifying advancement beyond a pure research question. However, Singapore has no registered product, no local safety label data exists in this dataset, and the first-generation sedation profile requires explicit risk management relative to second-generation alternatives.

**To proceed, the following is needed:**

- **Regulatory pathway assessment**: Evaluate whether a Singapore New Drug Application, parallel import, or compassionate use pathway is appropriate given the absence of any current HSA registration.
- **Package insert retrieval**: Obtain the full US FDA-approved Carbinoxamine package insert (e.g., Palgic, Karbinal ER) to extract the complete approved indication text, contraindications, warnings, and dosing information — currently a blocking data gap.
- **Mechanism of action documentation**: Retrieve DrugBank DB00748 detailed MOA, pharmacokinetics (protein binding, hepatic metabolism, half-life), and toxicity data to complete the pharmacological dossier.
- **Comparative effectiveness analysis**: Commission a structured literature review comparing first-generation H1 antihistamines vs. second-generation agents (cetirizine, loratadine, bilastine, rupatadine) for allergic urticaria to justify clinical positioning of Carbinoxamine — particularly if sedation is intended as a secondary benefit (e.g., nocturnal pruritus).
- **Safety monitoring plan**: Define risk mitigation for sedation and anticholinergic burden, including patient selection criteria (exclude elderly, BPH, narrow-angle glaucoma), counselling requirements, and contraindicated co-medications.
- **Carbinoxamine-specific evidence search expansion**: Extend literature searches to include older databases (EMBASE pre-1990, WHO ICTRP, historical FDA review documents) to capture pre-digital era clinical data relevant to the drug's established but under-documented evidence base.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

