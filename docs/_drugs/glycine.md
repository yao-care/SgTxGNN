---
layout: default
title: Glycine
parent: 僅模型預測 (L5)
nav_order: 433
evidence_level: L5
indication_count: 10
---

# Glycine
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

# Glycine: From Nutritional Supplement to Nasal Cavity Disease

## One-Sentence Summary

Glycine (DB00145) is a non-essential amino acid used primarily as a nutritional supplement and irrigating solution, with no formally approved therapeutic indications in the Singapore market.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease** with a prediction score of **99.85%**,
however, current supporting evidence is limited to **1 clinical trial** and **2 publications**, neither of which directly evaluates glycine as a treatment for this condition.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved therapeutic indications found in the Singapore regulatory database |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 (model prediction only; no directly relevant clinical studies identified) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Glycine is the simplest proteinogenic amino acid with several biologically plausible mechanisms that could relate to upper airway disease. It serves as an inhibitory neurotransmitter in the central and peripheral nervous system through glycine-gated chloride channels (GlyR), and also functions as a co-agonist at NMDA glutamate receptors. Beyond neurotransmission, glycine has well-documented anti-inflammatory properties: it activates GlyR expressed on macrophages, neutrophils, and mast cells, thereby suppressing pro-inflammatory cytokine release (TNF-α, IL-1β, IL-6) and reducing oxidative stress. These immunomodulatory effects have been studied in models of ischaemia-reperfusion injury, sepsis, and mucosal inflammation.

The nasal cavity mucosa is a key immunological barrier continuously exposed to allergens, pathogens, and irritants. Conditions such as allergic rhinitis, chronic rhinosinusitis, and nasal polyposis are driven largely by mucosal inflammation and dysregulated immune responses — precisely the pathways in which glycine's anti-inflammatory mechanism is active. Furthermore, glycine's established use as an irrigating solution in urological procedures demonstrates precedent for its local mucosal application, which raises the possibility of intranasal or topical delivery formats. The TxGNN knowledge-graph prediction may reflect these shared molecular pathways between glycine's receptor targets and the inflammatory biology of nasal cavity disease.

However, detailed mechanism of action data was not available in this Evidence Pack, and no clinical studies directly testing glycine as a therapeutic agent for nasal cavity disease were identified. The retrieved evidence is only tangentially related to glycine's activity in nasal tissue. This prediction should therefore be treated as a hypothesis-generating signal requiring preclinical and mechanistic validation before any clinical development can be considered.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Phase 1–2 | Completed | 25 | PET/CT and PET/MRI imaging study using 18F-FPPRGD2 — an RGD (Arg-Gly-Asp) tripeptide-containing radiopharmaceutical — to assess αvβ3 integrin expression as a biomarker of angiogenesis in patients with glioblastoma, gynaecological cancers, and renal cell carcinoma receiving antiangiogenic therapy. Glycine is embedded in the RGD peptide backbone of the tracer; the trial does not evaluate glycine as a therapeutic agent for nasal cavity disease. Relevance is indirect. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Animal Study | Veterinary Pathology | Used lectin histochemistry to characterise glycoconjugate composition in normal and BHV1-infected bovine nasal mucosa; examined changes that may facilitate Pasteurella haemolytica adhesion in the nasal cavity. Investigates nasal mucosal glycobiology in the context of infection — glycine is not studied as a therapeutic agent. |
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | Experimental | Chemical & Pharmaceutical Bulletin | Evaluated D-octaarginine-linked polymers (incorporating the Arg-Gly-Asp motif) as intranasal mucosal adjuvants for influenza vaccination in mice; demonstrated full protection against homologous virus infection. Glycine is structurally incorporated into the RGD adjuvant sequence, but is not studied as an independent therapeutic agent for nasal cavity disease. |

---

## Singapore Market Information

No registered pharmaceutical products containing Glycine were identified in the Singapore regulatory database. Glycine is currently not approved or marketed as a stand-alone therapeutic product in Singapore.

---

## Safety Considerations

No drug interaction data, key warnings, or contraindication information were available in this Evidence Pack. Please refer to the relevant package inserts, the DrugBank entry for DB00145, and official prescribing guidelines for safety information before any clinical use is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score of 99.85%, neither the clinical trial nor the literature identified in this Evidence Pack provides direct evidence that glycine is effective for treating nasal cavity disease; both are only tangentially related through glycine-containing molecular scaffolds. With zero Singapore regulatory approvals, absent safety profile data, and no primary studies testing glycine in a nasal cavity disease context, this candidate cannot advance without foundational evidence.

**To proceed, the following is needed:**
- A targeted literature search specifically examining glycine supplementation or local glycine administration in upper respiratory and nasal mucosal conditions (allergic rhinitis, chronic rhinosinusitis, nasal polyposis)
- Mechanistic evidence documenting glycine receptor (GlyR) expression in nasal mucosal tissue and demonstration of anti-inflammatory activity in relevant preclinical models
- Determination of an appropriate route of administration (e.g., intranasal, oral, topical) and associated pharmacokinetic/pharmacodynamic data
- Full safety and toxicology profile retrieval from DrugBank and TFDA/HSA package insert sources to complete the safety evaluation
- Preclinical proof-of-concept study before any consideration of a Phase 1 or investigator-initiated trial
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

