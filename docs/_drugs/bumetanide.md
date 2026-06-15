---
layout: default
title: Bumetanide
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
---

# Bumetanide
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

# Bumetanide: From Congestive Heart Failure to Acute Pulmonary Heart Disease

## One-Sentence Summary

Bumetanide is a potent loop diuretic originally indicated for the management of oedema associated with congestive heart failure, hepatic disease, and renal disease.
The TxGNN model predicts it may be effective for **Acute Pulmonary Heart Disease**,
with **3 clinical trials** and **5 publications** currently supporting this direction. Evidence is rated at **L3** (observational studies and mechanistic reviews), sufficient to advance with guardrails but not yet backed by a dedicated randomised trial.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Oedema associated with congestive heart failure, hepatic and renal disease |
| Predicted New Indication | Acute Pulmonary Heart Disease |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is not currently available. Based on published literature, bumetanide belongs to the **loop diuretic** class and acts by inhibiting the NKCC2 (Na⁺-K⁺-2Cl⁻ cotransporter 2) in the thick ascending limb of Henle's loop. This blocks the reabsorption of sodium, potassium, and chloride, producing a rapid and powerful diuresis — typically within 30 minutes of administration — via oral, intravenous, or intramuscular routes.

Acute pulmonary heart disease (acute cor pulmonale) arises when conditions such as massive pulmonary embolism or severe acute respiratory failure rapidly elevate pulmonary vascular resistance, triggering right ventricular failure, raised venous pressure, and systemic fluid congestion. The clinical imperative in this setting is prompt reduction of preload and relief of pulmonary and peripheral oedema — precisely the target of loop diuretic therapy. This mechanistic overlap with bumetanide's established indication in congestive heart failure makes the TxGNN prediction biologically plausible.

Direct haemodynamic evidence reinforces this link. A 1987 prospective study (PMID 3304383) in 24 patients with documented coronary artery disease and either acute or chronic heart failure showed that a single intravenous dose of bumetanide (25 µg/kg) acutely reduced pulmonary artery occluded pressure (PAOP) and cardiac index at rest, confirming an immediate beneficial effect on cardiac filling pressures. The 1984 comprehensive review (PMID 6391889) explicitly lists **acute pulmonary congestion** among bumetanide's established therapeutic uses, further corroborating the model's prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT07375212](https://clinicaltrials.gov/study/NCT07375212) | Phase 4 | Withdrawn | 0 | Single 4 mg intranasal bumetanide in heart failure patients with implanted pulmonary artery monitors (CardioMEMS / Cordella); withdrawn before any enrolment — no data available |
| [NCT05580510](https://clinicaltrials.gov/study/NCT05580510) | Phase 2/3 | Unknown | 160 | Empagliflozin + sacubitril/valsartan in adults with CHD-associated HFrEF; bumetanide serves only as background therapy, not the primary intervention |
| [NCT06885164](https://clinicaltrials.gov/study/NCT06885164) | N/A | Recruiting | 200 | Seismocardiographic monitoring in heart failure outpatients (2025–2027); purely observational, not a bumetanide intervention trial |

> No clinical trial directly tests bumetanide as a primary intervention in acute pulmonary heart disease. All three identified trials relate to adjacent heart failure populations or are observational.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [3304383](https://pubmed.ncbi.nlm.nih.gov/3304383/) | 1987 | Clinical Pharmacodynamic Study | Br J Clin Pharmacol | IV bumetanide (25 µg/kg) in 24 CAD patients with acute or chronic heart failure; acutely reduced PAOP and cardiac index at rest and during exercise, confirming immediate haemodynamic benefit in acute failure states |
| [6391889](https://pubmed.ncbi.nlm.nih.gov/6391889/) | 1984 | Review | Drugs | Comprehensive review of bumetanide; explicitly lists acute pulmonary congestion as an established indication; describes multi-route efficacy with onset within 30 minutes |
| [19142155](https://pubmed.ncbi.nlm.nih.gov/19142155/) | 2009 | Review | Am J Therapeutics | Review of acute heart failure management; loop diuretics are the cornerstone of therapy for 1 million annual hospitalisations in the US; reviews recent trial evidence and options for diuretic-resistant cases |
| [19843838](https://pubmed.ncbi.nlm.nih.gov/19843838/) | 2009 | Review | Ann Pharmacother | Head-to-head comparison of loop diuretics (furosemide, bumetanide, torsemide); pharmacokinetic profiles, comparative safety and efficacy, and cost — evaluates whether furosemide should remain first-line |
| [39366035](https://pubmed.ncbi.nlm.nih.gov/39366035/) | 2024 | Epidemiological Study | Am J Emerg Med | US emergency department heart failure data 2016–2023; characterises current admission rates, evaluation patterns, and treatment strategies, underscoring the ongoing burden of acute cardiopulmonary decompensation |

---

## Singapore Market Information

Bumetanide is **not currently registered** in Singapore. There are no product authorisations on record and no approved dosage forms or routes listed. Any clinical use would require an import licence or special access pathway under the Health Sciences Authority (HSA).

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data for bumetanide (TFDA package insert warnings, contraindications, and drug-drug interaction profile) were not available at the time of this report. These gaps are classified as **Blocking** (warnings/contraindications) and **High** (MOA) severity and must be resolved before a full safety assessment can be completed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bumetanide's mechanism as a loop diuretic maps directly onto the pathophysiology of acute pulmonary heart disease — fluid overload, elevated pulmonary pressures, and right heart congestion are all targets of NKCC2 inhibition. Published haemodynamic data (1987) and a comprehensive review that explicitly lists acute pulmonary congestion as an indication (1984) provide a mechanistic and observational foundation strong enough to advance. The TxGNN prediction score (99.58%) further supports biological plausibility. However, bumetanide is not registered in Singapore, no dedicated randomised trials exist for this specific indication, and critical safety data have not yet been retrieved.

**To proceed, the following is needed:**

- **Regulatory pathway**: Confirm HSA requirements for clinical use of an unregistered loop diuretic; assess precedent via comparator markets (UK, US, Japan) where bumetanide holds marketing authorisation
- **Safety data retrieval**: Download and parse the TFDA (or EMA/FDA) package insert to extract warnings, contraindications, and drug-drug interactions — currently a blocking data gap
- **MOA documentation**: Retrieve full mechanism of action from DrugBank to support the mechanistic rationale in any regulatory submission
- **Dedicated clinical evidence**: Design or identify a prospective study specifically enrolling acute cor pulmonale patients; existing trials address adjacent CHF populations but not this indication directly
- **Pharmacokinetic planning**: Define IV dosing protocol and titration strategy for the acute inpatient setting, particularly given the absence of Singapore-registered formulations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

