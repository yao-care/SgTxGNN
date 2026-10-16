---
layout: default
title: Taurine
parent: Low Evidence (L5)
nav_order: 956
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Taurine: predicted new indication Alcohol withdrawal delirium (evidence level L5). Approved use: Not stated in the Singapore licence records"
monitor_inn: "Taurine"
predicted_indications: ["alcohol withdrawal delirium", "antidepressant type abuse", "barbiturate abuse", "hallucinogen abuse", "cauda equina syndrome", "migraine disorder", "migraine with brainstem aura", "restless legs syndrome", "obsolete neurogenic bladder (disease)", "phencyclidine abuse"]
---

# Taurine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Taurine: From Parenteral Nutrition Amino Acid Component to Alcohol Withdrawal Delirium

## One-Sentence Summary

Taurine is an amino acid that is a component of parenteral nutrition (amino acid infusion) products marketed in Singapore.
The TxGNN model predicts it may be effective for **alcohol withdrawal delirium** (top-ranked prediction), but **no clinical trials and no publications** currently support this specific prediction.
Among the other ten predicted indications, **migraine disorder** has the most supporting material (8 publications, mostly observational), so it may be the more practical research direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records (all 10 licences have blank indication text); the products are amino acid infusion and parenteral nutrition formulations |
| Predicted New Indication | Alcohol withdrawal delirium |
| TxGNN Prediction Score | 93.07% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, taurine is an amino acid present in infusion and parenteral nutrition products, where it serves as a nutritional component. Its original-indication details are not recorded in the Singapore licence data, so a formal link between the original and new indications cannot be established.

Taurine acts as an inhibitory neuromodulator. It is reported to act at GABA-A and glycine receptors and to modulate glutamatergic excitability and calcium homeostasis. This is plausibly relevant to the neuronal hyperexcitability seen in alcohol withdrawal. However, this reasoning rests on the TxGNN prediction alone, because no trials or literature were found for this indication.

For reference, the other predictions in the list fall into three groups:
- **Substance-related conditions** (antidepressant type abuse, barbiturate abuse, hallucinogen abuse, phencyclidine abuse): the available papers are animal neurochemistry or metabolite-measurement studies. They do not show a therapeutic effect of taurine.
- **Migraine disorder**: the best-supported of the list, with clinical observational data showing altered taurine levels in patients (see below).
- **Others** (cauda equina syndrome, migraine with brainstem aura, restless legs syndrome, obsolete neurogenic bladder): no evidence was provided. The neurogenic bladder term is obsolete in the ontology and should be mapped to a current term before further evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered for alcohol withdrawal delirium. No registered trials were identified for any of the other predicted indications either.

## Literature Evidence

Currently no related literature available for alcohol withdrawal delirium.

For reference, the most informative literature among the other predictions concerns **migraine disorder** (rank 6, evidence level L4):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8349475](https://pubmed.ncbi.nlm.nih.gov/8349475/) | 1993 | Case-control | Headache | Plasma and CSF taurine were significantly higher in migraine patients during attacks than in controls |
| [8706112](https://pubmed.ncbi.nlm.nih.gov/8706112/) | 1995 | Case-control | Cephalalgia | CSF taurine, glycine and glutamine were significantly higher in 38 migraine patients than in 10 headache-free controls |
| [7107244](https://pubmed.ncbi.nlm.nih.gov/7107244/) | 1982 | Case-control | Headache | Changes in platelet taurine in migraine |
| [3372239](https://pubmed.ncbi.nlm.nih.gov/3372239/) | 1988 | Observational | Headache | Urinary taurine excretion in migraine |
| [8961243](https://pubmed.ncbi.nlm.nih.gov/8961243/) | 1996 | Hypothesis/clinical | Medical Hypotheses | Proposes magnesium taurate plus fish oil for migraine prevention; a combination product, so taurine's own effect cannot be isolated |
| [1978346](https://pubmed.ncbi.nlm.nih.gov/1978346/) | 1990 | Review/Hypothesis | Prog Clin Biol Res | Glutamate and taurine redistribution in migraine and epilepsy |
| [28921630](https://pubmed.ncbi.nlm.nih.gov/28921630/) | 2018 | Preclinical | Magn Reson Med | High-field MRS metabolic profiling of a rat migraine model, including taurine |

These studies show an association between taurine and migraine, but none shows that giving taurine treats migraine.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11682P | Aminoven Solution for Infusion 5% | Injection | Not stated in the records |
| SIN11829P | Aminoven Solution for Infusion 10% | Injection | Not stated in the records |
| SIN16337P | Aminoven Solution for Infusion 15% | Infusion, solution | Not stated in the records |
| SIN07846P | Trophamine Injection 10% | Injection | Not stated in the records |
| SIN07428P | Vaminolact Intravenous Solution | Injection | Not stated in the records |

Five more licences (all single-ingredient, valid) are held for SmofKabiven products, all injectable emulsions. All 10 registrations are injectable forms.

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found for taurine, and no disease contraindications were identified in the knowledge graph.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, alcohol withdrawal delirium, is supported only by the TxGNN score (93.07%), with no trials or publications, so it remains at evidence level L5. Taurine is already marketed in Singapore, but only as an injectable nutrition component, and its safety documentation is incomplete.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (currently missing, and a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature search focused on alcohol withdrawal and taurine, including animal and human studies
- Confirmation of the route of administration needed (oral versus the injectable forms registered), since route compatibility has not been assessed
- If a lead is wanted, consider migraine disorder as a research question, which would need a well-designed controlled trial of taurine alone
- Mapping of the obsolete neurogenic bladder term to a current disease term
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

