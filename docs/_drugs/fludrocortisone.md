---
layout: default
title: Fludrocortisone
parent: 僅模型預測 (L5)
nav_order: 433
evidence_level: L5
indication_count: 10
---

# Fludrocortisone
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

# Fludrocortisone: From Adrenal Insufficiency to Eye Disease

## One-Sentence Summary

> Fludrocortisone is a potent synthetic mineralocorticoid, established for treating adrenal insufficiency (Addison's disease) and salt-wasting adrenogenital syndrome.
> The TxGNN model's highest-scoring prediction is primary cutaneous T-cell lymphoma (99.58%), but this lacks clinical evidence (L5, Hold); the most evidence-supported new indication is **Eye Disease** — specifically geographic atrophy secondary to age-related macular degeneration —
> with **1 Phase 1B study identified in the literature** and **20 publications** supporting this direction (L3, Proceed with Guardrails).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Adrenal insufficiency (Addison's disease); salt-wasting adrenogenital syndrome |
| Predicted New Indication | Eye Disease (geographic atrophy / age-related macular degeneration) |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Fludrocortisone is a synthetic adrenocorticosteroid with markedly potent mineralocorticoid activity (approximately 125 times stronger than cortisol) and moderate glucocorticoid activity. While it is primarily used to replace aldosterone in adrenal insufficiency, the mineralocorticoid receptor (MR) is constitutively expressed throughout the eye — in retinal Müller cells, retinal pigment epithelium (RPE) cells, and ganglion cells. Activation of these receptors can modulate oxidative stress responses, suppress pro-inflammatory cytokines implicated in geographic atrophy pathogenesis (such as IL-1β and complement cascade components), and promote cell survival signaling pathways. The current lack of MOA documentation in the Evidence Pack is a recognized data gap, but this mechanistic rationale is well-established in the experimental literature.

A 2021 preclinical study (PMID 34509498) directly demonstrated that fludrocortisone exerts anti-inflammatory and neuroprotective effects in retinal degeneration models, specifically suppressing Müller cell-mediated cytokine expression under inflammatory challenge — the core pathogenic mechanism of geographic atrophy. This preclinical rationale led to a Phase 1B clinical trial (PMID 36161841, 2022) testing intravitreal fludrocortisone acetate (IVT-FCA) at 1 mg/0.1 mL and 2 mg/0.1 mL in geographic atrophy patients, validating the repurposing hypothesis at an early clinical stage. Separately, some glaucoma clinicians already use fludrocortisone (combined with salt intake) to stabilize nocturnal blood pressure dips in normal-tension glaucoma, leveraging its mineralocorticoid activity to maintain optic nerve perfusion pressure (PMID 17998043; PMID 23430676).

⚠️ A critical counter-signal must be noted: systemic corticosteroids — including mineralocorticoids — can elevate intraocular pressure (IOP), and fludrocortisone's effects on aqueous humor outflow resistance have been documented since 1964 (PMID 14211917). Furthermore, systemic fludrocortisone can cause sodium and fluid retention sufficient to raise intracranial pressure, with optic papillitis documented as a direct iatrogenic complication (PMID 3263626). These risks make intravitreal delivery — as explored in the Phase 1B trial — the strongly preferred route over systemic administration for any ophthalmic indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

> **Important note**: A Phase 1B study (PMID 36161841, 2022) evaluating single-dose intravitreal fludrocortisone acetate in geographic atrophy patients was identified through the literature search but was not captured in the ClinicalTrials.gov registry query. This trial represents the primary source of early clinical safety evidence and should be tracked as a priority.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36161841](https://pubmed.ncbi.nlm.nih.gov/36161841/) | 2022 | Phase 1B Clinical Trial | BMJ Open Ophthalmology | Safety and tolerability of single-dose intravitreal fludrocortisone acetate at 1 mg and 2 mg/0.1 mL in geographic atrophy secondary to AMD — primary safety evaluation |
| [34509498](https://pubmed.ncbi.nlm.nih.gov/34509498/) | 2021 | Preclinical Study | Experimental Eye Research | Fludrocortisone demonstrates anti-inflammatory and neuroprotective properties in retinal degeneration; suppresses Müller cell-mediated cytokine expression under inflammatory challenge |
| [17998043](https://pubmed.ncbi.nlm.nih.gov/17998043/) | 2007 | Review | Survey of Ophthalmology | Fludrocortisone (with salt intake) cited among emerging glaucoma therapies beyond IOP reduction; used to prevent nocturnal blood pressure dips that may drive progressive optic nerve damage |
| [23430676](https://pubmed.ncbi.nlm.nih.gov/23430676/) | 2013 | Review | Klin Monatsbl Augenheilkunde | Confirms fludrocortisone use in vascular-dysregulation glaucoma to stabilize nocturnal ocular perfusion pressure; provides mechanistic framework for MR-targeted ophthalmic therapy |
| [14211917](https://pubmed.ncbi.nlm.nih.gov/14211917/) | 1964 | Experimental Study | Experimental Eye Research | Foundational study on fludrocortisone's effects on IOP and aqueous humor outflow resistance — key safety pharmacodynamics data for ocular use |
| [12770979](https://pubmed.ncbi.nlm.nih.gov/12770979/) | 2003 | Observational Study | British Journal of Ophthalmology | Impact of smoking on thyroid-associated ophthalmopathy treatment — illustrates corticosteroid sensitivity in ocular inflammatory disease relevant to this drug class |
| [17191197](https://pubmed.ncbi.nlm.nih.gov/17191197/) | 2006 | Case report | European Journal of Ophthalmology | Limbal stem cell deficiency in autoimmune polyendocrinopathy — ocular surface complications in patients on long-term mineralocorticoid replacement therapy |

---

## Singapore Market Information

Fludrocortisone is currently **not registered or marketed in Singapore**. No HSA-approved product records are available (0 licenses). A de novo regulatory submission pathway would be required.

---

## Safety Considerations

Formal package insert warnings and contraindications were not available in this Evidence Pack (data gap). Based on pharmacological evidence identified in the literature:

- **⚠️ Intraocular Pressure Elevation**: Corticosteroids, including mineralocorticoids, can increase IOP and precipitate steroid-induced glaucoma. Fludrocortisone's effects on aqueous humor outflow resistance are documented (PMID 14211917). Mandatory IOP monitoring is required for any ophthalmic use; the glaucoma signal makes this drug unsuitable as a systemic agent for eye disease.
- **⚠️ Adverse Effect Signal — Optic Papillitis**: Systemic fludrocortisone causes sodium and fluid retention that can elevate intracranial pressure. A 1988 case report (PMID 3263626) documents recurrent iatrogenic benign intracranial hypertension — with optic papillitis as a direct complication — in a pediatric patient receiving fludrocortisone for congenital adrenogenital syndrome. This adverse effect signal strongly argues for intravitreal over systemic delivery in ophthalmic indications and represents a contraindication signal for neurological/intracranial pressure applications.
- **Sodium/Fluid Retention (Systemic)**: Potent mineralocorticoid activity drives sodium retention, potentially causing hypertension, dependent edema, and hypokalemia. These systemic risks are substantially mitigated by intravitreal delivery.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Fludrocortisone's repurposing for eye disease — specifically geographic atrophy secondary to AMD — is supported by an established mechanistic rationale (MR expression in retinal cells), preclinical neuroprotective evidence (2021), and a completed Phase 1B clinical trial (2022). Intravitreal delivery mitigates systemic mineralocorticoid risks, though IOP monitoring remains mandatory. The drug is unregistered in Singapore and requires a full regulatory pathway.

**To proceed, the following is needed:**
- Obtain full Phase 1B trial results (PMID 36161841) to confirm safety and tolerability outcomes in geographic atrophy patients
- Complete MOA documentation via DrugBank API (DG002) to enable formal mechanism-of-action analysis
- Identify any ClinicalTrials.gov registration number for the Phase 1B study
- Design Phase 2 efficacy trial with primary endpoints (geographic atrophy lesion growth rate, best-corrected visual acuity)
- Establish a mandatory IOP monitoring and management protocol for all ophthalmic studies
- Assess Singapore HSA regulatory pathway requirements for this unregistered compound
- All other top-10 TxGNN predictions (primary cutaneous T-cell lymphoma, dermoid cysts, orbital region disease, exostosis, granulomatous slack skin disease) are rated **Hold** — clinical or mechanistic evidence is absent, and several high TxGNN scores likely reflect non-specific graph traversal artifacts rather than true pharmacological relevance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

