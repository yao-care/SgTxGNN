---
layout: default
title: Nitroglycerin
parent: 僅模型預測 (L5)
nav_order: 710
evidence_level: L5
indication_count: 10
---

# Nitroglycerin
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

# Nitroglycerin: From Angina Pectoris to Pulmonary Hypertension

## One-Sentence Summary

Nitroglycerin (DB00727) is a classic organic nitrate vasodilator, long established in the treatment of angina pectoris and acute coronary vasospasm. The TxGNN model predicts it may also be effective for **Pulmonary Hypertension**, with **13 clinical trials** and **20 publications** currently supporting this direction, including several trials that directly test nebulized/inhaled nitroglycerin as a pulmonary vasodilator.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Angina Pectoris / coronary vasospasm (organic nitrate vasodilator; not currently HSA-registered in Singapore per this dataset) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is currently a data gap. Based on well-established pharmacological knowledge, nitroglycerin is a nitric oxide (NO) donor: it is metabolized to release NO, which activates soluble guanylate cyclase and raises intracellular cGMP in vascular smooth muscle, producing relaxation and vasodilation. This mechanism is the basis of its decades-long use in angina pectoris, where it dilates coronary vessels and reduces cardiac preload/afterload.

Pulmonary hypertension is likewise a disease of excessive pulmonary vascular smooth muscle tone and vasoconstriction. Because the NO–cGMP pathway is a central, well-validated target in PH therapeutics (shared with drugs such as sildenafil and inhaled nitric oxide), nitroglycerin's core mechanism is directly transferable from the coronary to the pulmonary vascular bed. In practice, nebulized/inhaled nitroglycerin already has real-world clinical use as an acute pulmonary vasodilator and as a vaso-reactivity testing agent in pulmonary arterial hypertension (PAH), which supports the biological plausibility of the TxGNN prediction — although this dataset lacks a large, contemporary Phase 3 RCT specific to nitroglycerin in PH.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07214129](https://clinicaltrials.gov/study/NCT07214129) | N/A | Completed | 20 | Nebulized nitroglycerin evaluated as a vaso-reactivity testing agent in pre-capillary pulmonary hypertension. |
| [NCT04594629](https://clinicaltrials.gov/study/NCT04594629) | Phase 1 | Unknown | 120 | Nebulized nitroglycerin vs. nebulized PGI2 (epoprostenol) for pulmonary hypertension after valve replacement surgery. |
| [NCT05741229](https://clinicaltrials.gov/study/NCT05741229) | N/A | Completed | 80 | Nebulized nitroglycerin as adjuvant therapy for persistent pulmonary hypertension of the newborn (PPHN); echocardiographic and clinical endpoints. |
| [NCT01120964](https://clinicaltrials.gov/study/NCT01120964) | Phase 1/2 | Completed | 22 | IV L-citrulline (NO pathway precursor) vs. placebo in children undergoing cardiopulmonary bypass, targeting pulmonary pressure control. |
| [NCT03259165](https://clinicaltrials.gov/study/NCT03259165) | Phase 2 | Terminated | 52 | Nitroglycerin vs. furosemide guided by lung ultrasound in acute heart failure/pulmonary congestion. |
| [NCT06107465](https://clinicaltrials.gov/study/NCT06107465) | Phase 2/3 | Unknown | 60 | High-dose vs. low-dose nitroglycerin in sympathetic crashing acute pulmonary edema. |
| [NCT00449059](https://clinicaltrials.gov/study/NCT00449059) | Phase 4 | Completed | 20 | Acute effect of nitroglycerin infusion on cyclosporine-induced hypertension after cardiac transplantation. |
| [NCT05373108](https://clinicaltrials.gov/study/NCT05373108) | Phase 4 | Completed | 19 | Endothelin-1 and vasomotor function in cardiac allograft vasculopathy after heart transplant. |
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Phase 1 | Recruiting | 420 | Vascular endothelial/vasomotor function and blood pressure regulation across health and disease states. |
| [NCT03014791](https://clinicaltrials.gov/study/NCT03014791) | N/A | Unknown | 500 | Influence of age, weight, and ethnicity on blood pressure regulation (AWE study). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34082850](https://pubmed.ncbi.nlm.nih.gov/34082850/) | 2021 | Cohort | Cardiology in the Young | Review of nitroglycerin inhalation for acute treatment of pulmonary arterial hypertension in children with congenital heart disease. |
| [40888971](https://pubmed.ncbi.nlm.nih.gov/40888971/) | 2025 | RCT | European Journal of Pediatrics | Randomized controlled trial: nebulized nitroglycerin as adjuvant therapy in persistent pulmonary hypertension of newborns (80 patients). |
| [29880427](https://pubmed.ncbi.nlm.nih.gov/29880427/) | 2018 | RCT/Cohort | J Cardiothorac Vasc Anesth | Dobutamine + nitroglycerin vs. milrinone for perioperative pulmonary hypertension management in mitral valve surgery. |
| [39549131](https://pubmed.ncbi.nlm.nih.gov/39549131/) | 2024 | Network Meta-Analysis | Clinical Drug Investigation | Network meta-analysis of pulmonary vasodilators (including nitroglycerin) in PH patients undergoing mitral valve replacement. |
| [6423015](https://pubmed.ncbi.nlm.nih.gov/6423015/) | 1984 | Cohort | Bull Eur Physiopathol Respir | Nitroglycerin and isosorbide dinitrate reduced pulmonary vascular resistance in COPD-related pulmonary hypertension. |
| [6407380](https://pubmed.ncbi.nlm.nih.gov/6407380/) | 1983 | Cohort | Annals of Internal Medicine | Nitroglycerin increased cardiac index and decreased pulmonary vascular resistance and mean pulmonary artery pressure in chronic PH patients. |
| [29096811](https://pubmed.ncbi.nlm.nih.gov/29096811/) | 2017 | Review | J Am Coll Cardiol | Comprehensive review of nitroglycerin/nitrogen oxide biology and cardiovascular therapeutic applications. |
| [16707530](https://pubmed.ncbi.nlm.nih.gov/16707530/) | 2006 | Clinical study | British Journal of Anaesthesia | Inhaled nitroglycerin reduced pulmonary and systemic hemodynamics in children with PAH from congenital heart disease. |
| [14508317](https://pubmed.ncbi.nlm.nih.gov/14508317/) | 2003 | Clinical study | Anesthesiology | Nitroglycerin inhalation improved postoperative hemodynamics in PH patients after mitral valve replacement. |
| [8689279](https://pubmed.ncbi.nlm.nih.gov/8689279/) | 1996 | Review | New Horizons | Review of calcium-channel and vasodilator mechanisms, including nitrates, in pulmonary hypertension and hypoxic vasoconstriction. |

## Singapore Market Information

Nitroglycerin currently has **no HSA registration records** in this dataset (0 licenses, market status: Not Marketed). No product-level authorization details are available to tabulate.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are currently marked as data gaps in this evidence pack; a DDI query returned no results.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed trials and two decades of published clinical experience support nitroglycerin's acute pulmonary vasodilator effect (nebulized/inhaled route) in pulmonary hypertension, and the NO–cGMP mechanism is well validated in this disease. However, no Phase 3 RCT specific to chronic PH management exists in this dataset, and the drug is not currently registered in Singapore.

**To proceed, the following is needed:**
- HSA product label / package insert (warnings, contraindications) — currently a **blocking** data gap (DG001) preventing safety pre-assessment
- DrugBank mechanism-of-action confirmation — currently a **high-severity** data gap (DG002)
- A defined administration route (nebulized/inhaled vs. IV) and dosing protocol specific to PH, since original formulations are approved for angina, not inhalation
- Confirmation of local regulatory pathway, since the drug currently has zero Singapore registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

