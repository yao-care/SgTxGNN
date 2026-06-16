---
layout: default
title: Digoxin
parent: 僅模型預測 (L5)
nav_order: 326
evidence_level: L5
indication_count: 10
---

# Digoxin
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

# Digoxin: From Heart Failure / Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a classic cardiac glycoside with over two centuries of clinical use, primarily prescribed for systolic heart failure and ventricular rate control in atrial fibrillation. The TxGNN model ranks **Prinzmetal Angina** as its top new indication candidate (score 99.81%), but mechanistic analysis reveals this prediction is biologically contradictory — Digoxin's Na⁺/K⁺-ATPase inhibition in vascular smooth muscle may worsen rather than relieve coronary vasospasm, and no supporting clinical trials exist. Across all 10 predicted indications in this multi-candidate evaluation, evidence quality is generally weak (L4–L5), with the sole notable exception of **Stroke Disorder** (rank 10, L3 evidence, 23 clinical trials, 20 publications), which merits a separate focused review.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Heart failure; ventricular rate control in atrial fibrillation (globally recognized; not registered in Singapore) |
| Predicted New Indication (Top-Ranked) | Prinzmetal Angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of HSA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Digoxin inhibits the Na⁺/K⁺-ATPase pump in cardiomyocytes, causing intracellular sodium to rise, which in turn reduces Na⁺/Ca²⁺ exchanger activity and elevates intracellular calcium. The resulting increase in calcium availability enhances cardiac contractility (positive inotropic effect). Digoxin also exerts vagotonic (parasympathomimetic) effects that slow AV nodal conduction — explaining its long-standing role in controlling ventricular rate during atrial fibrillation. These dual mechanisms underpin its traditional use in heart failure and arrhythmia.

Prinzmetal Angina (vasospastic angina) arises from episodic coronary artery spasm unrelated to fixed atherosclerotic plaque. Standard treatment focuses on calcium channel blockers and nitrates, which relax vascular smooth muscle by reducing intracellular calcium. Digoxin's mechanism points in precisely the opposite direction: by inhibiting Na⁺/K⁺-ATPase in vascular smooth muscle cells, it can raise intracellular calcium in the coronary arterial wall, potentially increasing vasomotor tone and worsening spasm. There is no clinical trial evidence, and neither retrieved literature publication provides direct mechanistic support for Digoxin in Prinzmetal Angina treatment.

The TxGNN model's high-confidence prediction likely reflects graph-proximity reasoning — Digoxin and Prinzmetal Angina both occupy heavily interconnected cardiovascular nodes in the knowledge graph, generating high co-occurrence scores that do not translate into therapeutic relevance. This case illustrates a critical validation step for all knowledge graph-based drug repurposing: mechanistic plausibility review must follow every high-confidence algorithmic output, and a high TxGNN score alone is not sufficient grounds for advancement.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Prinzmetal Angina.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Narrative Review | Acta Physiologica et Pharmacologica Bulgarica | Circadian rhythms in antihypertensive treatment — broad cardiovascular pharmacology context; no direct Digoxin–Prinzmetal link |
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Case Series / Narrative Review | Chinese Medical Sciences Journal | Re-evaluation of angina decubitus mechanism; identifies hemodynamic changes (elevated pulmonary artery diastolic pressure) before angina onset — Digoxin not discussed as a treatment intervention |

> **Important caveat**: Neither publication directly supports Digoxin as a treatment for Prinzmetal Angina. Both are indirect and retrieved via cardiovascular co-occurrence, not therapeutic relevance.

---

## Singapore Market Information

Digoxin has **no HSA product registration** and is not commercially marketed in Singapore. No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Detailed Singapore/Taiwan safety warnings, contraindications, and drug interaction data were not available in this Evidence Pack. Clinicians should consult the originator prescribing information (e.g., Lanoxin package insert) for current warnings, particularly regarding narrow therapeutic index, digoxin toxicity monitoring, and electrolyte interactions.

---

## Appendix: Multi-Indication Summary

This Evidence Pack evaluated 10 predicted indications. All carry a "Hold" recommendation except Stroke Disorder, which is flagged as a "Research Question" warranting further investigation.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Clinical Trials | Publications |
|------|---------------------|------------|---------------|----------------|-----------------|--------------|
| 1 | Prinzmetal Angina | 99.81% | L4 | Hold | 0 | 2 (indirect) |
| 2 | Duodenal Obstruction | 99.70% | L5 | Hold | 0 | 1 (case report) |
| 3 | Duodenal Ulcer | 99.59% | L5 | Hold | 0 | 5 (DDI/comorbidity) |
| 4 | Duodenogastric Reflux | 99.53% | L5 | Hold | 0 | 0 |
| 5 | Ischemic Stroke Susceptibility (obsolete) | 99.29% | L5 | Hold | 0 | 0 |
| 6 | Hypoalphalipoproteinemia | 99.20% | L5 | Hold | 0 | 0 |
| 7 | Homozygous Familial Hypercholesterolemia | 98.98% | L5 | Hold | 0 | 0 |
| 8 | Nephrogenic Syndrome of Inappropriate Antidiuresis | 98.83% | L5 | Hold | 0 | 0 |
| 9 | Thrombotic Disease | 98.75% | L4 | Hold | 2 (observational) | 0 |
| **10** | **Stroke Disorder** | **98.19%** | **L3** | **Research Question** | **23** | **20** |

> Ranks 5 (obsolete disease ontology term) and 7 (LDL receptor pathway unrelated to Digoxin's mechanism) are particularly low-priority candidates.

---

## Conclusion and Next Steps

**Decision: Hold** (all 10 predictions at current evidence stage)

**Rationale:**
The top-ranked TxGNN prediction (Prinzmetal Angina) is mechanistically contraindicated — Digoxin's vascular Na⁺/K⁺-ATPase inhibition raises coronary smooth muscle calcium and may worsen vasospasm. Ranks 2–8 lack any meaningful supporting evidence. The one indication with substantive evidence — **Stroke Disorder** (rank 10) — reflects Digoxin's indirect role in AF rate control rather than a direct anti-stroke mechanism, and all associated clinical trials are observational or in the AF background, not stroke-specific interventions.

**To proceed, the following is needed:**

- **Obtain mechanism of action data** from DrugBank API (Data Gap DG002) to enable rigorous mechanistic plausibility scoring across all 10 predicted indications
- **Retrieve Singapore HSA / Taiwan TFDA package insert** for full safety warnings, contraindications, and drug interactions (Data Gap DG001) — particularly important given Digoxin's narrow therapeutic index
- **Conduct a separate focused evidence synthesis for Stroke Disorder (rank 10)**: specifically examine whether Digoxin's role in AF rate control confers measurable stroke risk reduction compared to beta-blockers or calcium channel blockers, using the Phase 4 RCT data (NCT02391337, NCT05130268) and retrospective cohort evidence (PMID 35420260)
- **Flag Prinzmetal Angina as a potential contraindicated prediction** in the knowledge graph model, to improve future prediction calibration for vasospastic conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

