---
layout: default
title: Epoprostenol
parent: Medium Evidence (L3-L4)
nav_order: 382
evidence_level: L4
indication_count: 10
---

# Epoprostenol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Epoprostenol: From Pulmonary Arterial Hypertension to Trigeminal Autonomic Cephalalgia

## One-Sentence Summary

Epoprostenol is a synthetic prostacyclin (PGI2), a potent vasodilator and platelet inhibitor, used as an infusion for pulmonary arterial hypertension (PAH).
The TxGNN model predicts it may be effective for **trigeminal autonomic cephalalgia** (for example, cluster headache) with a very high score. However, there are **0 clinical trials** and only **2 old publications**, and the available evidence suggests prostacyclin *provokes* headache rather than relieving it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (from general drug knowledge; the Singapore licence records provided contain no indication text) |
| Predicted New Indication | Trigeminal autonomic cephalalgia |
| TxGNN Prediction Score | 98.41% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on known pharmacology, epoprostenol is a prostacyclin that acts on IP receptors, raising cAMP, which causes vasodilation and inhibits platelet aggregation. Its efficacy in pulmonary arterial hypertension is established.

The high TxGNN score most likely reflects closeness in the knowledge graph: shared vasodilator and prostaglandin pathways link prostacyclin to headache biology. That closeness does not mean benefit.

The direction of effect points the wrong way. The retrieved papers link prostacyclin to headache mechanisms and attack provocation, not relief. Vasodilators and prostanoids tend to trigger attacks in headache disorders, so this prediction is unlikely to be therapeutic.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for trigeminal autonomic cephalalgia.

Trials registered for the broader "headache disorder" prediction are provocation studies (PGI2 induces headache), not treatment studies.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7026501](https://pubmed.ncbi.nlm.nih.gov/7026501/) | 1981 | Small interventional study | Headache | Effect of infused prostacyclin in migraine and cluster headache. No abstract available, so no outcome can be confirmed. |
| [3937967](https://pubmed.ncbi.nlm.nih.gov/3937967/) | 1985 | Narrative review | Neurologia i Neurochirurgia Polska | Pathomechanisms of cluster headache attacks. Nitroglycerin provoked attacks in 9 patients, and the study probed the role of the arachidonic acid cyclooxygenase pathway with indomethacin. It does not show a benefit of prostacyclin. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN02241P | Flolan for Infusion 0.5 mg/vial | Powder for solution for injection | Not stated in the record |
| SIN15405P | Veletri Powder for Solution for Infusion 0.5 mg/vial | Powder for solution for injection | Not stated in the record |
| SIN15406P | Veletri Powder for Solution for Infusion 1.5 mg/vial | Powder for solution for injection | Not stated in the record |

All three products are injectable only. No route suited to chronic headache prophylaxis is registered.

---

## Safety Considerations

Please refer to the package insert for safety information. The HSA warnings and contraindications were not retrieved, and no drug interaction data were found.

One signal from the literature is directly relevant here: intravenous epoprostenol triggered headache in healthy volunteers and migraine-like attacks in migraineurs in a randomized, double-blind crossover study (PMID 19614689). This argues against use in headache disorders.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high model score is not backed by any treatment evidence. There are no clinical trials, only two old, low-tier publications, and the broader literature shows prostacyclin provokes headache attacks. The evidence level is L4, and a therapeutic role is mechanistically unlikely.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- Any human data showing symptom relief (none found so far)

**Note on other predictions:** In this evidence pack, the most substantial signal is for **respiratory failure** (rank 9). Inhaled epoprostenol has a completed Phase 2 double-blind placebo-controlled trial in ventilated COVID-19 patients (NCT04452669, n=11, underpowered), Phase 4 studies and observational cohorts. It is graded L2 and flagged as a research question. It merits a separate evaluation, though outcome benefit (mortality, ventilator-free days) is not established.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

