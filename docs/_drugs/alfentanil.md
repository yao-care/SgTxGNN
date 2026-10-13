---
layout: default
title: Alfentanil
parent: Low Evidence (L5)
nav_order: 60
evidence_level: L5
indication_count: 10
---

# Alfentanil
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

# Alfentanil: From Opioid Anaesthesia/Analgesia to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Alfentanil is a short-acting mu-opioid agonist given by injection, and it is marketed in Singapore. The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis**, which is the top-ranked prediction. However, **no clinical trials and no publications** support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records (alfentanil is a mu-opioid agonist used as an injectable analgesic/anaesthetic) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, alfentanil is a mu-opioid receptor agonist that modulates central pain pathways.

For the top prediction, no convincing mechanistic rationale is evident. Opioids can influence vasopressin release. Nephrogenic SIAD, however, is caused by gain-of-function mutations in the vasopressin V2 receptor gene (*AVPR2*). This is a defect in the kidney receptor itself, independent of vasopressin secretion. An opioid would therefore not be expected to correct it. The high model score is not backed by any trial or literature evidence.

Other predictions from the model are also weakly supported:
- **Migraine disorder** (99.76% rank list position 2, score 98.76%): only a 1988 preclinical review of spreading depression, plus a general paediatric pharmacokinetics study that is probably incidental. Opioids are generally not recommended for migraine because of medication-overuse headache, dependence and poor efficacy.
- **Headache disorder** (score 98.20%): a single case report of propofol plus alfentanil in episodic cluster headache. This is hypothesis-generating only, as it is one case and confounded by propofol.
- **Other predictions** (hypertrichosis, Dandy-Walker syndrome, hair shaft abnormalities, leprosy and others): no plausible mechanism and no evidence.

## Clinical Trial Evidence

For the top-ranked prediction (nephrogenic syndrome of inappropriate antidiuresis), currently no related clinical trials are registered.

The only trial linked to related predictions (migraine disorder and headache disorder) is shown below. It was graded as having low relevance.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3,520 | General paediatric pharmacokinetics study of understudied drugs given per standard of care. It was not designed to test migraine or headache efficacy, and the match is probably incidental. |

## Literature Evidence

For the top-ranked prediction, currently no related literature is available. The publications below are linked to the migraine and headache predictions only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24910816](https://pubmed.ncbi.nlm.nih.gov/24910816/) | 2014 | Case report | Anesthesiology and Pain Medicine | Propofol plus alfentanil used in a patient with episodic cluster headache. A single case confounded by propofol. |
| [2896809](https://pubmed.ncbi.nlm.nih.gov/2896809/) | 1988 | Review | Journal of Pharmacological Methods | Spreading depression (a proposed migraine aura mechanism) studied in alfentanil-anaesthetised rats. Preclinical and indirect, and does not show therapeutic efficacy. |
| [19181514](https://pubmed.ncbi.nlm.nih.gov/19181514/) | 2009 | Case series | International Journal of Obstetric Anesthesia | Spinal catheter anaesthesia for caesarean section in 34 women with complex cardiac disease. Not related to headache treatment. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN17055P | Alfentanil Kalceks Solution for Injection/Infusion 0.5 mg/ml | Injection, solution | Not stated in the licence record |
| SIN04326P | Rapifen Injection 0.5 mg/ml | Injection | Not stated in the licence record |

## Safety Considerations

- **Disease associations from the knowledge graph (not label text)**: the TxGNN knowledge graph records contraindication links between alfentanil and kidney disease, pyoureter, liver disease, gallbladder disease, hypotensive disorder, pseudotumor cerebri and intracranial hypertension. These links need confirmation against the package insert.
- **Drug Interactions**: 100 interactions were found in total. Examples of the major-level interactions among those listed are:
  - Aprepitant
  - Bupropion
  - Clarithromycin
  - Clotrimazole
  - Dexfenfluramine
  - Dolasetron
  - Fenfluramine
  - Granisetron
  - Lorcaserin

  Moderate-level examples include atropine, cimetidine, clidinium, dexamethasone, dicyclomine, dronabinol, eluxadoline, glycopyrronium, hyoscyamine and mazindol.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no trial or literature support and no plausible mechanism, since nephrogenic SIAD is a renal V2 receptor defect that an opioid would not be expected to fix. The only weak signal is a single confounded case report in headache disorder, which is at most a research question. Opioids also carry significant risks in headache conditions.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Singapore regulator (HSA), which are required before any safety screening
- Detailed mechanism of action data (for example, from DrugBank)
- Any direct mechanistic or clinical evidence linking alfentanil to the predicted indication
- If pursued at all, a focused review of opioid use in refractory headache, given the safety concerns
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

