---
layout: default
title: Gemeprost
parent: 僅模型預測 (L5)
nav_order: 316
evidence_level: L5
indication_count: 10
---

# Gemeprost
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

# Gemeprost: From Pregnancy Termination to Atypical Coarctation of Aorta

## One-Sentence Summary

Gemeprost is a synthetic prostaglandin E1 (PGE1) analogue, administered as a vaginal pessary for cervical ripening and medical termination of pregnancy in combination with mifepristone.
The TxGNN model predicts it may be relevant to **Atypical Coarctation of Aorta** (top-ranked prediction, score 99.53%), though across this multi-target evaluation all 10 predicted indications currently carry a **Hold** recommendation, as no supporting clinical trials exist and mechanistic analysis reveals the drug's vasoconstrictive properties are counterproductive or actively harmful for the majority of predicted cardiovascular and structural indications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cervical ripening; medical termination of early pregnancy (in combination with mifepristone) |
| Predicted New Indication | Atypical Coarctation of Aorta |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available from DrugBank. Based on established pharmacology, Gemeprost acts primarily as an agonist at EP1 and EP3 prostanoid receptors, producing uterine contractions, cervical softening, and—critically—**vasoconstriction** in arterial smooth muscle. These actions underpin its clinical application in pregnancy termination. However, this vasoconstrictive EP3 profile is directly at odds with virtually all of the cardiovascular and structural indications predicted by TxGNN.

For the top-ranked prediction—atypical coarctation of aorta—the mechanistic case is unfavorable. Aortic coarctation is a structural obstructive lesion managed by relieving the obstruction, not by pharmacological intervention. Gemeprost's EP3 agonism would theoretically increase vasomotor tone and worsen the haemodynamic burden distal to the coarctation. Published case series directly document severe cardiovascular events attributable to Gemeprost, including cardiogenic shock, myocardial infarction, and coronary vasospasm (PMID 10904996, 18185889). The high TxGNN score likely reflects non-specific connectivity between PGE1-pathway nodes and cardiovascular disease nodes in the knowledge graph, rather than a true therapeutic opportunity.

The same pattern applies across all 10 predicted indications. Where indirect mechanistic links exist—such as pulmonary hypertension or peripheral arterial disease, where other PGE1 prostanoids (epoprostenol, alprostadil) are approved—the critical distinction is receptor subtype selectivity: those drugs act via vasodilatory EP2/EP4 receptors, whereas Gemeprost's EP1/EP3 activity produces the opposite hemodynamic effect (PMID 7834185). This represents a class divergence phenomenon that cannot be bridged by analogy alone.

### All Predicted Indications Overview

| Rank | Indication | TxGNN Score | Evidence Level | Key Mechanistic Issue | Decision |
|------|-----------|------------|----------------|----------------------|---------|
| 1 | Atypical Coarctation of Aorta | 99.53% | L5 | EP3 vasoconstriction worsens obstructive haemodynamics; severe CVS AE reports | Hold |
| 2 | Amenorrhea (disease) | 99.36% | L4 | 8 publications use "amenorrhoea" as gestational age unit, not as a treated condition | Hold |
| 3 | Non-syndromic Esophageal Malformation | 99.27% | L5 | Structural congenital defect; no PGE1 pathway relevance | Hold |
| 4 | Aortic Malformation | 99.22% | L5 | Structural congenital defect; EP3 vasoconstriction harmful | Hold |
| 5 | Pulmonary Hypertension | 99.15% | L4 | Class divergence: Gemeprost EP3 contracts pulmonary artery (PMID 7834185), opposite to needed vasodilation | Hold |
| 6 | Kyphoscoliotic Heart Disease | 98.88% | L5 | Restrictive cardiopulmonary disease secondary to thoracic deformity; no PGE1 relevance | Hold |
| 7 | Esophageal Disease | 98.86% | L5 | EP1/EP3 profile lacks mucosal-protective EP2/EP4 activity; no supporting evidence | Hold |
| 8 | Peripheral Arterial Disease | 98.78% | L4 | Class divergence from alprostadil; EP3-mediated vasoconstriction counterproductive; severe CVS AE safety signal | Hold |
| 9 | HER2+ Breast Carcinoma | 98.47% | L5 | PGE2 pathways are pro-tumour, not anti-tumour; no preclinical or clinical data | Hold |
| 10 | Vascular Disease | 98.12% | L4 | Retrieved literature constitutes adverse event reports (MI, vasospasm, shock), not therapeutic evidence | Hold |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for atypical coarctation of aorta or any of the 10 predicted indications.

---

## Literature Evidence

No published literature was identified for the top-ranked prediction (atypical coarctation of aorta).

For the amenorrhea prediction (Rank 2), 8 publications were retrieved but all use "amenorrhoea" as a unit to measure gestational age (≤56 days since last menstrual period), not as a disease being treated. They describe Gemeprost's established use in pregnancy termination and are not relevant to repurposing for amenorrhea as a clinical condition.

For the vascular disease prediction (Rank 10), 12 publications were retrieved. The table below presents the most clinically significant ones—the body of evidence constitutes a safety signal, not a repurposing rationale:

| PMID | Year | Type | Journal | Key Finding |
|------|------|------|---------|------------|
| [10904996](https://pubmed.ncbi.nlm.nih.gov/10904996/) | 2000 | Case Series | Zentralblatt fur Gynakologie | Two cases of severe cardiovascular reactions after gemeprost pessary: cardiogenic shock from vasospasm; cerebral stroke |
| [18185889](https://pubmed.ncbi.nlm.nih.gov/18185889/) | 2007 | Case Report | Annals of the Academy of Medicine, Singapore | Acute myocardial infarction in a middle-aged woman following gemeprost vaginal pessary insertion |
| [7834185](https://pubmed.ncbi.nlm.nih.gov/7834185/) | 1994 | Basic Pharmacology | British Journal of Pharmacology | EP3-receptor agonists produce potent contraction of human isolated pulmonary artery at nanomolar concentrations—key mechanistic basis for cardiovascular risk |
| [20224253](https://pubmed.ncbi.nlm.nih.gov/20224253/) | 2010 | Case Report | Fetal Diagnosis and Therapy | Acute coronary artery vasospasm associated with PGE1 analogue use for pregnancy termination; notes class-level cardiovascular risk |
| [11187221](https://pubmed.ncbi.nlm.nih.gov/11187221/) | 2000 | Case Report | Ugeskrift for Laeger | Vasospastic angina with loss of consciousness, bradycardia and seizures after mifepristone + gemeprost; prior history of vasospastic disorder identified as risk factor |
| [10826591](https://pubmed.ncbi.nlm.nih.gov/10826591/) | 2000 | Case Report | BJOG | Life-threatening myocardial ischaemia associated with prostaglandin E1 use for abortion induction |
| [1432596](https://pubmed.ncbi.nlm.nih.gov/1432596/) | 1992 | Review | Yakugaku Zasshi | Historical overview of prostaglandin drug development including gemeprost; confirms PGE1 analogue class profile |

---

## Singapore Market Information

Gemeprost is not registered in Singapore. No product authorizations exist.

---

## Safety Considerations

**Key cardiovascular safety signals (from retrieved literature):**

Gemeprost has been associated with life-threatening cardiovascular adverse events in published case reports and case series:

- **Acute myocardial infarction** following vaginal pessary administration (PMID 18185889)
- **Cardiogenic shock and cerebral stroke** from severe vasospasm (PMID 10904996)
- **Coronary artery vasospasm** (PMID 20224253, 11187221, 10826591)

These events are mechanistically consistent with EP3 receptor-mediated arterial smooth muscle contraction and are most likely in patients with a history of smoking, migraine, vasospastic disorders, or prior cardiovascular disease.

For complete prescribing warnings and contraindications, please refer to the originator package insert.

---

## Conclusion and Next Steps

**Decision: Hold (All 10 Predicted Indications)**

**Rationale:**
All 10 TxGNN-predicted indications lack supporting clinical trial evidence, and mechanistic analysis reveals that Gemeprost's EP1/EP3 vasoconstrictive profile is counterproductive for the dominant cluster of cardiovascular and structural disease predictions. Where indirect analogy to other PGE1 drugs might suggest a hypothesis (pulmonary hypertension, peripheral arterial disease), the critical EP receptor subtype divergence disqualifies direct extrapolation, and safety literature documents severe cardiovascular harm in general populations at standard doses.

**To proceed with any further evaluation, the following is needed:**

- Complete MOA documentation from DrugBank or primary literature confirming EP receptor selectivity profile and any tissue-specific effects
- TFDA package insert download and review to fill the blocking safety data gap (DG001)
- Structured cardiovascular risk assessment before evaluating any vascular indication
- Identification of whether any uterotonic or cervical-specific mechanism could be leveraged for a gynaecological repurposing hypothesis outside the predicted top 10
- Drug-drug interaction review (currently no DDI data available)
- If the amenorrhea hypothesis is to be explored, dedicated literature search specifically for primary/secondary amenorrhea as a treated condition—entirely separate from the retrieved gestational-age literature

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

