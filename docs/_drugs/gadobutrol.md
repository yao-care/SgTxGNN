---
layout: default
title: Gadobutrol
parent: 僅模型預測 (L5)
nav_order: 458
evidence_level: L5
indication_count: 10
---

# Gadobutrol
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

# Gadobutrol: From CNS MRI Contrast Enhancement to Peripheral Arterial Disease Diagnosis

## One-Sentence Summary

Gadobutrol (Gadovist) is a high-concentration (1.0 mol/L) macrocyclic gadolinium-based contrast agent (GBCA) primarily used for MRI enhancement of the central nervous system and whole-body imaging.
The TxGNN model's highest-evidence prediction suggests it may serve a diagnostic role in **Peripheral Arterial Disease (PAD)**, with **4 clinical trials** and **20 publications** currently supporting this direction.
It is important to note that this represents a **diagnostic**, rather than therapeutic, repurposing — Gadobutrol's role in PAD is as a contrast medium for CE-MRA (contrast-enhanced MR angiography), not as a treatment agent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | CNS MRI enhancement (brain and spine); whole-body MR angiography |
| Predicted New Indication | Peripheral Arterial Disease (PAD) |
| TxGNN Prediction Score | 76.72% (rank #2 by evidence quality; rank #1 BPH has no supporting evidence) |
| Evidence Level | L1 (2 completed Phase 4 RCTs directly comparing Gadobutrol in PAD) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on TxGNN Rank Interpretation:** The model's rank 1 prediction (Benign Prostatic Hyperplasia, score 83.2%) has zero clinical trial or literature support and is mechanistically implausible. This report focuses on PAD (rank 2, score 76.7%), which carries the strongest evidence and a coherent mechanistic rationale.

---

## Why is This Prediction Reasonable?

Gadobutrol is a macrocyclic, extracellular gadolinium chelate formulated at a uniquely high concentration of 1.0 mol/L — twice that of conventional 0.5 mol/L GBCAs. This high molarity shortens T1 relaxation time more efficiently, producing superior vessel-to-background contrast even at lower injection volumes. The physical mechanism is straightforward: **high [Gd]→ enhanced MRI signal → superior vascular delineation**.

In the context of peripheral arterial disease, contrast-enhanced MR angiography (CE-MRA) is the established non-invasive reference standard for assessing stenosis severity, lesion extent, and guiding revascularisation decisions. Gadobutrol's concentration advantage is particularly valuable in multi-station CE-MRA protocols covering the entire runoff vasculature from the aorta to the foot — a technically demanding study where bolus timing and signal-to-noise ratio are critical. The high relaxivity of Gadobutrol allows lower gadolinium doses (0.1 mmol/kg) while maintaining diagnostic image quality, which also carries safety benefits in patients with comorbid renal dysfunction.

The TxGNN knowledge graph likely identifies this connection through the shared pathway: **Gadobutrol ↔ MR angiography ↔ vascular disease diagnosis**, reflecting real-world clinical practice rather than a novel therapeutic mechanism. While this does not constitute pharmacological drug repurposing in the conventional sense, it does represent an **expansion of the diagnostic indication** for Gadobutrol into peripheral vascular imaging — an application already well-supported by high-quality clinical evidence but potentially not yet formally registered in all markets.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01026389](https://clinicaltrials.gov/study/NCT01026389) | Phase 4 | Completed | 189 | Head-to-head RCT comparing Gadovist® (Gadobutrol) vs Dotarem® (gadoterate) CE-MRA in abdominal and lower limb arterial disease — the largest PAD diagnostic comparison trial |
| [NCT00955617](https://clinicaltrials.gov/study/NCT00955617) | Phase 4 | Completed | 20 | Intra-individual crossover comparison of Gadobutrol vs gadoterate in CE-MRA for clinically significant abdominal/lower limb arterial disease |
| [NCT02917213](https://clinicaltrials.gov/study/NCT02917213) | N/A | Completed | 92 | Prospective observational study assessing quantitative cardiac and vascular MRI (including Gadobutrol) for predicting thromboembolic complications including peripheral arterial embolism post-MI |
| [NCT05685160](https://clinicaltrials.gov/study/NCT05685160) | N/A | Enrolling by Invitation | 75 | Imaging comparison of intermetatarsal bursitis vs Morton's neuroma using MRI with contrast — limited direct relevance to PAD diagnosis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [26001243](https://pubmed.ncbi.nlm.nih.gov/26001243/) | 2015 | RCT | AJR Am J Roentgenol | Large-scale randomised prospective study demonstrating non-inferiority of gadoterate vs Gadobutrol at 3T MRA in peripheral arterial occlusive disease, using DSA as reference — establishes Gadobutrol as diagnostic benchmark |
| [12928960](https://pubmed.ncbi.nlm.nih.gov/12928960/) | 2003 | Prospective Cohort | Eur Radiol | Multi-centre blinded study (n=203) comparing Gadobutrol CE-MRA vs intra-arterial DSA in peripheral vascular disease — demonstrated high diagnostic accuracy for pelvic and peripheral arteries |
| [22848033](https://pubmed.ncbi.nlm.nih.gov/22848033/) | 2012 | Prospective RCT | J Magn Reson Imaging | Single-centre randomised crossover double-blind study comparing 0.5M gadoterate vs 1.0M Gadobutrol in peripheral MRA at 3T for abdominal/lower limb arterial disease |
| [20959539](https://pubmed.ncbi.nlm.nih.gov/20959539/) | 2010 | Prospective Cohort | Radiology | Evaluated a 3T MRA protocol combining continuous table movement with time-resolved TWIST-MRA using single-dose Gadobutrol (0.1 mmol/kg) in peripheral arterial occlusive disease |
| [23188773](https://pubmed.ncbi.nlm.nih.gov/23188773/) | 2013 | Prospective Comparative | J Magn Reson Imaging | Compared CE-MRA vs DSA in lower extremity arterial disease, confirming high diagnostic accuracy for stenosis grading in symptomatic peripheral arterial occlusive disease |
| [15149986](https://pubmed.ncbi.nlm.nih.gov/15149986/) | 2004 | Prospective Cohort | AJR Am J Roentgenol | Whole-body 3D CE-MRA with Gadobutrol in 51 patients with PAD; demonstrated feasibility of single-injection whole-body vascular coverage compared to DSA |
| [19652610](https://pubmed.ncbi.nlm.nih.gov/19652610/) | 2009 | Prospective Cohort | Invest Radiol | Proof-of-concept for peripheral CTM MRA combined with time-resolved TWIST-MRA using single low dose of Gadobutrol (0.1 mmol/kg) at 3.0T |
| [12677513](https://pubmed.ncbi.nlm.nih.gov/12677513/) | 2003 | Prospective Cohort | RoFo | Early clinical results for 1.0M Gadobutrol CE-MRA vs intra-arterial DSA in peripheral arterial occlusive disease — established early evidence base |
| [24893292](https://pubmed.ncbi.nlm.nih.gov/24893292/) | 2014 | Prospective Comparative | PLoS One | Compared enhancement characteristics and image quality of Gadobutrol vs gadoterate in low-dose time-resolved 3T MRA at calf station — relevant for distal PAD assessment |
| [21031523](https://pubmed.ncbi.nlm.nih.gov/21031523/) | 2010 | Prospective Comparative | J Magn Reson Imaging | Inter-individual prospective comparison of gadobenate dimeglumine vs Gadobutrol in CE run-off MRA of the lower extremities for diagnostic accuracy and image quality |

---

## Singapore Market Information

Gadobutrol is currently **not registered** with the Health Sciences Authority (HSA) of Singapore. No product authorisations are on file.

> Gadobutrol (marketed as Gadovist® by Bayer and as Gadavist® in North America) holds regulatory approval in multiple major markets including the European Union, United States, Japan, and Australia for MRI enhancement of CNS and body imaging. A formal registration application to HSA would be required before clinical use in Singapore.

---

## Safety Considerations

No HSA-specific package insert warnings or contraindications data were available for this review. No drug-drug interaction data were identified in the query log.

Please refer to the originator's package insert (Gadovist®, Bayer) for complete safety information. Key class-related considerations for gadolinium-based contrast agents include:

- **Nephrogenic Systemic Fibrosis (NSF):** Risk in patients with severe renal impairment (eGFR < 30 mL/min/1.73 m²). Gadobutrol is a macrocyclic GBCA with a more stable chelate structure than linear agents, associated with lower NSF risk.
- **Gadolinium Retention:** Long-term gadolinium deposition in the brain and other tissues has been reported for all GBCAs; macrocyclic agents including Gadobutrol show lower retention than linear agents.
- **Hypersensitivity Reactions:** As with all contrast media, anaphylactoid reactions are possible; resuscitation facilities should be available.
- **Renal Function Monitoring:** Screen for renal impairment before administration; dose adjustment or avoidance may be required in renally compromised patients.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for Gadobutrol in peripheral arterial disease diagnosis is substantial and of high quality — two completed Phase 4 RCTs and multiple prospective cohort studies consistently demonstrate diagnostic non-inferiority or equivalence to the reference standard (DSA), with a clear and well-understood mechanistic basis. This is not a speculative pharmacological repurposing but an evidence-grounded **diagnostic indication expansion** backed by L1-level evidence.

**To proceed, the following is needed:**

- **HSA Registration:** Gadobutrol is not currently registered in Singapore. A regulatory submission to HSA is required. The existing EU and US approval dossiers (Gadovist® / Gadavist®) provide a strong foundation for a submission.
- **Formal Safety Data for Singapore Label:** Obtain and translate the complete package insert (warnings, contraindications, NSF risk communication) to fulfil HSA label requirements.
- **Renal Safety Protocol:** Establish a local institutional protocol for pre-administration eGFR screening, consistent with international radiology society guidelines (ACR, ESUR) for macrocyclic GBCA use.
- **MOA Documentation:** Formal documentation of the gadolinium chelate mechanism for regulatory dossier completeness.
- **Post-Market Surveillance Plan:** Given gadolinium retention signals across the class, a pharmacovigilance plan aligned with MHC/HSA requirements should be prepared.

> **Research Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

