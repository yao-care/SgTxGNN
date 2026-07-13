---
layout: default
title: Macitentan
parent: 僅模型預測 (L5)
nav_order: 574
evidence_level: L5
indication_count: 10
---

# Macitentan
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

# Macitentan: From Pulmonary Arterial Hypertension to Pulmonary Arteriovenous Malformation

## One-Sentence Summary

Macitentan (Opsumit®) is a dual endothelin receptor antagonist (ERA) with established global approval for pulmonary arterial hypertension (PAH), though it carries no Singapore registration to date.
The TxGNN model ranks **pulmonary arteriovenous malformation (PAVM)** as its highest-scoring new indication (98.89%), yet this prediction is backed by **no clinical trials** and **no published literature**, and the mechanistic rationale is not compelling.
Of the 10 TxGNN predictions in this evidence pack, two PAH subtypes — CHD-associated PAH (rank #2) and connective tissue disease-associated PAH (rank #5) — carry substantially stronger evidence (L3 each) and represent the more clinically actionable repurposing opportunities.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary Arterial Hypertension (globally approved; not registered in Singapore) |
| Predicted New Indication | Pulmonary Arteriovenous Malformation (PAVM) |
| TxGNN Prediction Score | 98.89% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Macitentan is a dual endothelin receptor antagonist that binds both ETA and ETB receptors with high affinity and unusually slow receptor-dissociation kinetics — a pharmacological feature that distinguishes it from earlier ERA agents such as bosentan. In pulmonary vascular disease, the ET-1 axis is a key driver of vasoconstriction, smooth muscle proliferation, and adventitial fibrosis. By blocking both receptor subtypes, Macitentan reduces pulmonary vascular resistance and attenuates pathological remodeling. The SERAPHIN Phase 3 trial confirmed that Macitentan significantly reduces morbidity and mortality in PAH, and the drug is now approved in over 80 countries under the brand name Opsumit®.

Pulmonary arteriovenous malformation (PAVM) is a fundamentally different disease: it is a structural vascular defect in which pulmonary arteries connect directly to pulmonary veins, bypassing the capillary bed entirely. This creates an anatomical right-to-left shunt without any known involvement of the ET-1 signaling pathway. The pathophysiology of PAVM is driven by embryological vascular development defects (often linked to hereditary hemorrhagic telangiectasia / HHT), not by vasoactive mediator imbalance. Accordingly, the standard of care is transcatheter embolization — a mechanical intervention to physically occlude the abnormal channel.

Macitentan's ERA mechanism has no direct intervention point on a structural shunt, and there is no preclinical or clinical precedent for ERA use in PAVM. The high TxGNN prediction score (98.89%) most plausibly reflects indirect knowledge graph proximity through shared "pulmonary vascular disease" ontology nodes — a recognized false-positive pattern in graph neural network drug repurposing models when target diseases share broad categorical overlap with an approved indication but diverge mechanistically.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
PAVM is a structural vascular malformation addressed by embolization; Macitentan's endothelin receptor antagonist mechanism lacks any pathophysiologically relevant target in this disease, and the high TxGNN score is assessed as a knowledge graph artifact rather than a clinically meaningful signal.

**To proceed, the following is needed:**
- Preclinical evidence demonstrating ET-1 pathway involvement in PAVM pathogenesis (currently absent in the literature)
- Published case series or mechanistic studies linking ERA therapy to PAVM outcomes

**Priority recommendation — redirect evaluation to the following indications in this evidence pack, which have genuine mechanistic grounding and existing real-world evidence:**

| Rank | Indication | Evidence Level | Trials | Publications | Decision |
|------|-----------|---------------|--------|-------------|---------|
| #2 | PAH associated with Congenital Heart Disease (CHD-PAH) | L3 | 2 (1 active Phase 3 platform: NCT05179876) | 18 (incl. direct real-world cohort studies 2017–2026) | **Proceed with Guardrails** |
| #5 | PAH associated with Connective Tissue Disease (CTD-PAH) | L3 | 2 | 18 (incl. systematic review PMID 38378970 + multiple real-world cohort studies 2022–2025) | **Proceed with Guardrails** |

Both CHD-PAH and CTD-PAH share the same ET-1 overactivation pathway as idiopathic PAH, are formally classified as WHO Group 1 PAH, and already appear as subgroups in the SERAPHIN trial that established Macitentan's global approval. The real-world evidence base for these subtypes is active and growing. These are the highest-yield targets for a Singapore drug access or clinical development strategy.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

