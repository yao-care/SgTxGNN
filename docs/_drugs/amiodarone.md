---
layout: default
title: Amiodarone
parent: 僅模型預測 (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
---

# Amiodarone
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

# Amiodarone: From Ventricular Arrhythmias to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Amiodarone is a well-established broad-spectrum antiarrhythmic agent used globally for life-threatening ventricular arrhythmias and atrial fibrillation, though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)**, a rare inherited cardiac channelopathy,
with **no registered clinical trials** and **10 publications** currently available to support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; globally indicated for ventricular fibrillation and life-threatening ventricular arrhythmias |
| Predicted New Indication | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Amiodarone is a Class III antiarrhythmic drug with uniquely broad multi-channel blocking properties. It inhibits delayed rectifier potassium channels (IKr/IKs) to prolong the cardiac action potential duration and effective refractory period, while simultaneously exerting sodium channel blockade (Class I), beta-adrenergic receptor antagonism (Class II), and L-type calcium channel inhibition (Class IV). This multi-class profile makes it a drug of last resort for arrhythmias refractory to conventional agents.

CPVT is caused by gain-of-function mutations in the RYR2 (ryanodine receptor 2) gene or loss-of-function mutations in CASQ2 (calsequestrin-2). Under catecholamine stimulation — exercise or emotional stress — these mutations cause pathological calcium leakage from the sarcoplasmic reticulum, producing delayed afterdepolarizations (DADs) that trigger polymorphic ventricular tachycardia and potentially fatal cardiac arrest. The mechanistic link between Amiodarone and CPVT is therefore indirect at best: although Amiodarone possesses calcium channel blocking activity, it does not directly modulate RyR2-mediated sarcoplasmic reticulum calcium release, which is the core dysfunction in CPVT.

By contrast, Flecainide has demonstrated direct RyR2 channel blockade independent of its sodium channel effects and has emerged as a more mechanistically targeted treatment for CPVT. Amiodarone's documented role in CPVT is largely limited to adjunctive rescue therapy during acute electrical storms, as reflected in the available case literature. The high TxGNN prediction score likely reflects knowledge graph associations derived from Amiodarone's broad antiarrhythmic utility rather than a specific CPVT mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Amiodarone in catecholaminergic polymorphic ventricular tachycardia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opinion on Pharmacotherapy | Reviews pharmacological management of ventricular arrhythmias; antiarrhythmic drugs including amiodarone remain important despite advances in non-pharmacologic therapy |
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Cohort | Life (Basel) | Systematic review of CPVT clinical characteristics, genetic findings, and arrhythmic outcomes in Chinese patients; highlights phenotypic differences from Western cohorts |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Cohort | Reviews in Cardiovascular Medicine | Retrospective cohort examining CPVT clinical characteristics, genetic basis, healthcare utilisation, and costs in a Chinese city |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case Series | Pacing and Clinical Electrophysiology | Flecainide (not amiodarone) suppresses ICD-induced arrhythmic storm in a 14-year-old with CPVT due to CASQ2 mutation; underscores RyR2-targeted therapy advantage |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Case Report | BMJ Case Reports | Pediatric out-of-hospital cardiac arrest; amiodarone used as part of multimodal resuscitation including 40 defibrillation shocks for refractory pulseless VT/VF |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Case Report | Anesthesia and Analgesia | Neonate with compound long QT mutation requiring multimodal therapy with amiodarone, esmolol, and lidocaine for refractory ventricular tachycardia |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case Report | Medicine | Delayed CPVT diagnosis (RYR2 c.7580T>G mutation) in a 9-year-old child; illustrates diagnostic challenges and the consequences of delayed recognition |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case Report | Turk Pediatri Arsivi | 2-year-old presenting with sudden cardiac arrest caused by CPVT; genetic arrhythmia in the absence of structural heart disease |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case Report | Frontiers in Cardiovascular Medicine | Successful resolution of refractory CPVT in a teenager via bilateral cardiac sympathetic denervation after failure of medical therapy |
| [17125720](https://pubmed.ncbi.nlm.nih.gov/17125720/) | 2006 | Case Report | Revista Española de Cardiología | Arrhythmic storm triggered by ICD discharges in a CPVT patient; demonstrates complexity of device-therapy interactions in catecholamine-driven arrhythmias |

---

## Singapore Market Information

Amiodarone (DrugBank ID: DB01118) is **not registered** in Singapore. No Health Sciences Authority (HSA) authorisation records are available. The drug is therefore not legally marketed through standard channels in Singapore, and any clinical use would require special access pathways (e.g., Special Access Route or institutional compassionate use).

---

## Safety Considerations

Please refer to the package insert for safety information. Formal warnings and contraindications specific to the Singapore/HSA label are not available, as the drug is not registered locally. Clinicians should consult established international references (e.g., FDA label, EMA SmPC) for Amiodarone's well-documented toxicity profile, which includes pulmonary toxicity, thyroid dysfunction, hepatotoxicity, and QT prolongation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.78%), the mechanistic link between Amiodarone and CPVT is weak — Amiodarone does not directly target the RyR2/CASQ2 calcium dysregulation that drives CPVT pathophysiology, no clinical trials have been conducted in this specific indication, and available literature supports only adjunctive or rescue use in acute arrhythmic emergencies rather than disease-specific CPVT therapy.

**To proceed, the following is needed:**

- **Mechanistic evidence**: Pre-clinical or translational data demonstrating whether Amiodarone exerts any meaningful effect on RyR2-mediated calcium release in CPVT models
- **Safety data**: Full review of the Amiodarone package insert (Singapore or international) for warnings, contraindications, and drug–drug interactions, particularly relevant given the drug's broad toxicity profile
- **Comparative positioning**: Clarify Amiodarone's role relative to established CPVT therapies (nadolol, flecainide, cardiac sympathetic denervation) — current evidence suggests it offers no advantage as a primary agent
- **Registry or case series data**: A prospective registry documenting Amiodarone outcomes specifically in CPVT patients who are refractory to beta-blockers and flecainide would be required before any formal repurposing evaluation can proceed
- **Regulatory pathway assessment**: Given zero Singapore registrations, any development programme would need to account for HSA registration requirements from the outset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

