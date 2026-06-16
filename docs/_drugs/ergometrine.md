---
layout: default
title: Ergometrine
parent: 僅模型預測 (L5)
nav_order: 389
evidence_level: L5
indication_count: 10
---

# Ergometrine
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

# Ergometrine: From Postpartum Haemorrhage to Migraine Disorder

## One-Sentence Summary

Ergometrine is a natural ergot alkaloid used in obstetrics as an oxytocic agent for the prevention and treatment of postpartum haemorrhage and uterine atony.
The TxGNN model flags **Migraine Disorder** as the most clinically actionable repurposing target (TxGNN score 99.93%), supported by **20 publications** including direct clinical studies of ergometrine (ergonovine) and its active metabolite methylergonovine in migraine prophylaxis and acute treatment.
No registered clinical trials exist for this indication, placing the current evidence at **L3**, and formal safety documentation for Singapore was not retrieved in this pack.

> **Note on top TxGNN prediction**: The highest-scoring TxGNN prediction is hypertrichosis (99.96%), followed by several rare genetic or congenital conditions — all L5 with no supporting evidence and no mechanistic plausibility. This report focuses on **Migraine Disorder (rank 7)** as the highest-evidence, mechanistically coherent repurposing candidate. The top predictions are assessed in the Conclusion section.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Postpartum haemorrhage / uterine atony (obstetric oxytocic) |
| Highlighted Repurposing Target | Migraine Disorder |
| TxGNN Prediction Score | 99.93% (TxGNN rank 1,539) |
| Evidence Level | L3 (observational studies, clinical series, systematic reviews) |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ergometrine (also known as ergonovine) is a naturally occurring ergot alkaloid derived from the fungus *Claviceps purpurea*. Detailed mechanism of action data were not returned by DrugBank in this evidence pack. However, ergometrine is pharmacologically well characterised in the scientific literature: it acts as an **α-adrenergic agonist** and **serotonin 5-HT₂ receptor agonist/partial agonist**, producing potent smooth muscle contraction — including uterine contraction and systemic vasoconstriction. Its principal active metabolite, **methylergonovine**, shares an identical receptor profile and is pharmacologically interchangeable for many purposes.

The mechanistic case for migraine is direct and well-established. The 5-HT₂ agonism causes cranial vasoconstriction and suppresses neurogenic inflammation in the meningeal vessels — precisely the mechanism that underpins the classic ergot migraine drugs **ergotamine** (Cafergot) and **methysergide**. The literature review (PMID 9793694) explicitly describes methysergide as a "semisynthetic ergot alkaloid ergometrine derivative," confirming that ergometrine occupies the same pharmacological class and shares the same receptor targets as established migraine therapies. Ergotamine and dihydroergotamine (DHE) have been used in migraine for over 80 years. The α-adrenergic component additionally modulates meningeal vessel tone, reinforcing the dual rationale.

Most significantly, **ergometrine itself** — marketed historically under the brand name **Ergotrate** — appears directly in the migraine treatment literature (PMID 6773347), confirming historical clinical use for this indication. Prospective observational studies of oral methylergonovine (PMID 23432443) and a pilot emergency department study of intravenous methylergonovine (PMID 19895705) show positive signals for refractory migraine and cluster headache. A 40-patient clinical series studying ergonovine maleate specifically for menstrual migraine prophylaxis (PMID 2759844) further supports direct repurposing rather than only class-effect inference. The convergence of mechanistic rationale, class-effect evidence, and direct small-scale clinical data makes this the most coherent repurposing signal in the pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ergometrine in Migraine Disorder.

---

## Literature Evidence

*(Source: predicted_indications rank 7 — migraine disorder; 10 most relevant of 20 retrieved publications)*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2759844](https://pubmed.ncbi.nlm.nih.gov/2759844/) | 1989 | Clinical Series | *Headache* | Ergonovine maleate (ergometrine) used as intermittent prophylaxis in 40 menstrual migraine patients over 6 months; vasoconstrictive mechanism cited; positive preliminary results |
| [23432443](https://pubmed.ncbi.nlm.nih.gov/23432443/) | 2013 | Prospective Observational | *Headache* | Oral methylergonovine maleate (direct active metabolite of ergometrine) evaluated for refractory migraine and cluster headache prevention; clinically significant response reported |
| [19895705](https://pubmed.ncbi.nlm.nih.gov/19895705/) | 2009 | Pilot Clinical Study | *Head & Face Medicine* | IV methylergonovine assessed in female migraine patients in the emergency department; open-label pilot study demonstrating feasibility and acute efficacy signal |
| [9793694](https://pubmed.ncbi.nlm.nih.gov/9793694/) | 1998 | Review | *Cephalalgia* | Methysergide — described as a "semisynthetic ergot alkaloid ergometrine derivative" — reviewed as a specific 5-HT receptor modulator for migraine prophylaxis; evidence of efficacy in resistant high-frequency migraine |
| [6773347](https://pubmed.ncbi.nlm.nih.gov/6773347/) | 1980 | Case Series | *AJR* | Pleural thickening documented with both Sansert (methysergide) and **Ergotrate (ergometrine brand)** during migraine treatment — confirms ergometrine itself was clinically used for migraine; identifies fibrosis as a chronic-use safety concern |
| [7216754](https://pubmed.ncbi.nlm.nih.gov/7216754/) | 1980 | Cohort | *Headache* | Long-term interval therapy of migraine with ergot-based prophylaxis; outcome data on sustained migraine prevention |
| [556819](https://pubmed.ncbi.nlm.nih.gov/556819/) | 1977 | Case Report / Review | *Neurology* | Carotidynia (recurrent vascular neck pain / migraine variant) in 8 women; drugs effective in migraine prophylaxis — including ergot preparations — shown to be effective |
| [5761912](https://pubmed.ncbi.nlm.nih.gov/5761912/) | 1969 | Clinical Study | *BMJ* | Prophylaxis of recurrent headache; ergot preparations including ergometrine-class drugs discussed in the context of sustained migraine prevention |
| [13306339](https://pubmed.ncbi.nlm.nih.gov/13306339/) | 1955 | Historical Review | *Int Arch Allergy* | Historical development of ergot therapy in migraine; places ergometrine in the context of the broader ergoline pharmacology that gave rise to modern migraine treatment |
| [23216317](https://pubmed.ncbi.nlm.nih.gov/23216317/) | 2013 | Review / Case Report | *Headache* | QT prolongation, Torsade de Pointes, and coronary vasospasm from headache medications; important safety framing for ergot use in migraine — serotonergic vasoconstrictors can narrow coronary arteries |

---

## Singapore Market Information

Ergometrine is **not registered with the Health Sciences Authority (HSA) in Singapore**. No product authorisation records were identified. The drug has established regulatory presence in other jurisdictions (UK, Australia, parts of Asia) for obstetric indications. Any clinical development or access programme in Singapore would require a full regulatory pathway assessment.

---

## Safety Considerations

Formal package insert warnings and contraindications for Singapore were not retrieved (data gap). The following clinically critical safety signals are directly derivable from the evidence literature in this pack:

- **Absolute Contraindication — Pulmonary Hypertension**: Multiple obstetric publications (PMID 22731893, PMID 26050249) classify ergometrine as contraindicated in patients with pulmonary hypertension. The α-adrenergic and 5-HT₂ agonism causes pulmonary vasoconstriction, directly worsening PAH pathophysiology. This is a firm pharmacological contraindication.

- **Contraindication — Migraine with Brainstem Aura**: Ergot alkaloids are historically contraindicated in basilar/brainstem aura migraine due to the risk of vertebrobasilar vasoconstriction causing brainstem ischaemia (PMID 10971665 documents postpartum cerebral angiopathy consistent with ergot-induced RCVS). TxGNN rank 8 — migraine with brainstem aura — is therefore a safety exclusion, not a treatment target.

- **Coronary Vasospasm Risk**: Ergometrine is actively used as a **diagnostic provocation agent** for variant (Prinzmetal's) angina (PMID 15293589, PMID 41185581). Use in patients with coronary artery disease or established variant angina is contraindicated.

- **Fibrotic Complications with Chronic Use**: Prolonged use of ergot preparations has been associated with retroperitoneal fibrosis, pleural thickening, and cardiac valvulopathy (PMID 6773347). This is a class-effect risk relevant to any migraine prophylaxis indication requiring long-term dosing.

Please refer to the full package insert for comprehensive prescribing information before any clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The repurposing rationale for Ergometrine in Migraine Disorder is mechanistically sound (5-HT₂/α-adrenergic vasoconstriction, shared with established ergot migraine drugs) and supported by direct positive clinical data for ergonovine/methylergonovine in migraine prophylaxis — however, all existing studies are small, non-randomised, or observational, and the drug carries meaningful safety contraindications that require active patient selection.

**Regarding other TxGNN predictions (ranks 1–6, 9–10):**
The high-scoring predictions for hypertrichosis, Ambras syndrome, genetic hair shaft abnormalities, and Dandy-Walker malformation (ranks 1–6) are assessed as **false positives** — they represent knowledge graph propagation artefacts with no mechanistic link to ergometrine's pharmacology. The periodontal disease literature (rank 4) consisted entirely of disease-general periodontology publications with no ergometrine-specific content (retrieval false positive). Leprosy (rank 9) has no antimicrobial rationale. Pulmonary hypertension (rank 10) is a **pharmacological contraindication** and should be flagged as a safety exclusion rather than a candidate indication.

**To proceed with migraine repurposing, the following is needed:**
- Retrieve full pharmacological MOA data from DrugBank (currently blocking data gap DG002)
- Obtain package insert warnings and contraindications from the regulatory authority (blocking data gap DG001) — mandatory before any S1 safety assessment
- Conduct a targeted systematic review of ergonovine / methylergonovine specifically in migraine, separate from the broader ergotamine/ergot class literature
- Assess whether oral or intranasal ergometrine formulations provide a route advantage over available ergotamine products
- Evaluate unmet clinical need: define the patient population where ergometrine would be used alongside or instead of modern triptans and CGRP antagonists
- Design a prospective pilot RCT for menstrual migraine prophylaxis as the most tractable initial indication, given the existing positive signal from PMID 2759844
- Establish a clear contraindication screening protocol (pulmonary hypertension, coronary artery disease, brainstem aura, peripheral vascular disease) for any future study enrolment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

