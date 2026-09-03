---
layout: default
title: Riociguat
parent: 僅模型預測 (L5)
nav_order: 862
evidence_level: L5
indication_count: 10
---

# Riociguat
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

# Riociguat: From Pulmonary Arterial Hypertension to PAH Associated with Connective Tissue Disease

## One-Sentence Summary

Riociguat is a soluble guanylate cyclase (sGC) stimulator originally developed for pulmonary arterial hypertension (PAH, WHO Group 1) and chronic thromboembolic pulmonary hypertension. Evidence in this pack points to a mechanistically coherent extension into **PAH associated with connective tissue disease (CTD-PAH)** — a recognized PAH subtype rather than an unrelated new indication — supported by a **dedicated PATENT-1/PATENT-2 subgroup RCT** and **12 related publications**, including a systematic review and an EULAR treatment guideline. A closely related subtype, **PAH associated with congenital heart disease (CHD-PAH)**, shows similar-strength evidence and is discussed alongside it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (WHO Group 1) — established from clinical literature; no Singapore label text available since the product is not locally registered |
| Predicted New Indication | Pulmonary Arterial Hypertension Associated with Connective Tissue Disease (CTD-PAH) |
| TxGNN Prediction Score | 91.55% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

A structured mechanism-of-action record is not available for this drug in the evidence pack (data gap). However, the supporting literature consistently and repeatedly identifies riociguat as a **soluble guanylate cyclase (sGC) stimulator** that acts through the NO–sGC–cGMP pathway to produce pulmonary vasodilation and anti-proliferative effects on pulmonary vascular smooth muscle. This is the drug's approved mechanism for WHO Group 1 PAH.

CTD-PAH is not a novel, unrelated disease — it is one of the main clinical subtypes within the WHO Group 1 PAH classification (alongside idiopathic PAH, heritable PAH, CHD-PAH, and others). Because the sGC-cGMP mechanism operates independently of the underlying etiology of pulmonary vascular remodeling, applying riociguat to CTD-PAH represents a direct, mechanism-consistent extension rather than a speculative cross-indication leap. This is reinforced by a prospectively-planned subgroup analysis from the pivotal PATENT-1/PATENT-2 phase III program (PMID 27457511) specifically evaluating riociguat in PAH-CTD patients, plus a systematic review/meta-analysis (PMID 38378970) and an EULAR clinical guideline for systemic sclerosis (PMID 27941129) that references vasodilator therapy for this population.

A closely related candidate, **PAH associated with congenital heart disease (CHD-PAH, rank 6)**, shows the same evidence tier (L2) via a dedicated PATENT-1 CHD subgroup analysis (PMID 26135803), reflecting the same underlying logic. By contrast, several top-scoring TxGNN predictions in this pack (Ambras-type hypertrichosis, odontal malformation syndrome, Dandy-Walker syndrome, hair shaft abnormality, isolated hypertrichosis — ranks 1–5) have no mechanistic plausibility and no supporting clinical or literature evidence; these are best interpreted as knowledge-graph embedding noise and are appropriately flagged "Hold" rather than pursued.

---

## Clinical Trial Evidence

Currently no clinical trials registered specifically for riociguat in CTD-PAH are present in this evidence pack. (Note: a related trial, NCT07356778, evaluating sotatercept — not riociguat — was identified under the neighboring CHD-PAH candidate and is included there only as field-activity context, not as direct evidence for CTD-PAH.)

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27457511](https://pubmed.ncbi.nlm.nih.gov/27457511/) | 2017 | RCT (PATENT-1/2 subgroup) | Annals of the Rheumatic Diseases | Prospectively-planned analysis of riociguat efficacy/safety in the PAH-CTD subgroup of the pivotal PATENT-1/2 phase III program |
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic Review / Meta-analysis | Internal and Emergency Medicine | Pooled RCT/subgroup data on CTD-PAH treatment outcomes (functional class, survival, 6-MWD) |
| [27941129](https://pubmed.ncbi.nlm.nih.gov/27941129/) | 2017 | Clinical Guideline (EULAR) | Annals of the Rheumatic Diseases | Updated EULAR recommendations for systemic sclerosis treatment, including PAH-directed vasodilator therapy |
| [33131480](https://pubmed.ncbi.nlm.nih.gov/33131480/) | 2020 | Review | Kardiologiia | Reviews the role of riociguat specifically in PAH associated with systemic connective tissue disease |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review | Pharmaceuticals (Basel) | Recent advances in treatment of PAH associated with connective tissue disease |
| [28671485](https://pubmed.ncbi.nlm.nih.gov/28671485/) | 2017 | Case Series / Switch Study | Pulmonary Circulation | Case series switching PDE-5 inhibitor to riociguat in PAH-CTD patients |
| [31090367](https://pubmed.ncbi.nlm.nih.gov/31090367/) | 2019 | Registry / Cohort | Terapevticheskii Arkhiv | National PAH registry data on prevalence, clinical course, and therapy, including CTD-associated cases |
| [40331647](https://pubmed.ncbi.nlm.nih.gov/40331647/) | 2025 | Prospective Observational | Kardiologiia | Long-term survival and prognostic factor analysis in PAH associated with connective tissue/rheumatic disease |
| [39985455](https://pubmed.ncbi.nlm.nih.gov/39985455/) | 2025 | Basic Science (preclinical) | Rheumatology (Oxford) | Characterizes a next-generation sGC activator (avenciguat) building on riociguat's sGC-stimulator mechanism in SSc models |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | General review of PAH diagnosis and treatment landscape |

---

## Singapore Market Information

Riociguat is currently **not marketed in Singapore** — no local product registrations exist in the evidence pack (0 licenses). Market entry would require full HSA registration and label development.

---

## Safety Considerations

Please refer to the package insert for safety information. Structured warnings, contraindications, and drug-interaction data were not available in this evidence pack (flagged as a **Blocking** data gap for the safety pre-screen stage).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The CTD-PAH prediction is mechanistically sound and supported by a dedicated phase III subgroup RCT, a systematic review, and a clinical guideline — reaching evidence level L2. This is not a speculative repurposing signal but a clinically-recognized PAH subtype within the drug's existing pharmacological class of use. The same logic applies to the neighboring CHD-PAH candidate (rank 6), which should be evaluated jointly.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent label warnings and contraindications (currently a Blocking data gap — DG001)
- Structured mechanism-of-action documentation from DrugBank (High-priority gap — DG002)
- Confirmation of local (Singapore) regulatory pathway status, since the product is currently unregistered
- Drug-drug interaction data (none currently on file) before any clinical protocol design
- Independent assessment of the CHD-PAH candidate (rank 6) as a parallel or combined submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

