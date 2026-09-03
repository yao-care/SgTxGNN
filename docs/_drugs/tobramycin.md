---
layout: default
title: Tobramycin
parent: 僅模型預測 (L5)
nav_order: 989
evidence_level: L5
indication_count: 10
---

# Tobramycin
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

# Tobramycin: From Gram-Negative Bacterial Infections to Exposure Keratitis

## One-Sentence Summary

> Tobramycin is an aminoglycoside antibiotic established for treating gram-negative bacterial infections (e.g., *Pseudomonas aeruginosa*), most notably in cystic fibrosis pulmonary infection, otitis externa, and ocular/topical infections.
> The TxGNN model's top-ranked prediction is **Exposure Keratitis**, supported by **2 clinical trials** and **7 publications** — however, the underlying rationale flags this as a mechanistically indirect match, since exposure keratitis is a non-infectious, mechanical/neurotrophic corneal condition rather than a primary bacterial disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack — Tobramycin is not currently licensed in Singapore, so no approved indication text exists on file. (Context from evidence: aminoglycoside antibiotic active against gram-negative organisms, particularly *Pseudomonas aeruginosa*.) |
| Predicted New Indication | Exposure Keratitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for Tobramycin is not available (flagged as a High-severity data gap). Based on information contained in the evidence pack, Tobramycin is an aminoglycoside broad-spectrum antibiotic with strong bactericidal activity against gram-negative organisms, particularly *Pseudomonas aeruginosa*. Across the wider prediction set for this drug, this antimicrobial spectrum underlies several plausible repurposing candidates involving gram-negative infection at different anatomical sites — pulmonary (cystic fibrosis), aural (otitis externa), and ocular (bacterial keratitis).

For the top-ranked candidate, exposure keratitis, the connection is topical: tobramycin eye drops are commonly used to prevent secondary bacterial infection in corneas that cannot close properly (e.g., in sedated or comatose patients), which is the same setting reflected in the supporting literature (e.g., a case of bacterial keratitis in a vegetative-state patient unable to close his eyes).

However, the evidence pack's own mechanistic assessment explicitly cautions that exposure keratitis itself is a **mechanical/neurotrophic** corneal disorder, not an infectious disease. Tobramycin can only act as **infection-prophylaxis** for a secondary complication of exposure keratitis — it does not address the underlying corneal exposure pathology. This distinguishes it from indications like otitis externa or CF-associated Pseudomonas pulmonary infection (found lower in the ranked list), where tobramycin's antibacterial mechanism directly targets the disease driver.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06200727](https://clinicaltrials.gov/study/NCT06200727) | N/A | Unknown | 170 | Platelet-rich fibrin (PRF) membrane trial across four ophthalmic conditions (macular hole, pterygium, corneal ulcer, trabeculectomy patients); tobramycin not the study intervention — indirect relevance only (Grade C). |
| [NCT05313828](https://clinicaltrials.gov/study/NCT05313828) | N/A | Unknown | 40 | Compares treatment modalities for dendritic (herpes simplex viral) corneal ulcer; viral, not bacterial, aetiology — mechanism does not match tobramycin's antibacterial action (Grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34987857](https://pubmed.ncbi.nlm.nih.gov/34987857/) | 2021 | Case report | Oxford Medical Case Reports | Bacterial keratitis from multi-drug-resistant *Shewanella algae* in a bedridden patient unable to close his eyes (classic exposure-keratitis-with-secondary-infection scenario). |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case report | Ophthalmology | *Bacillus cereus* keratitis associated with contact lens wear; first genetic identification of the causative organism from cornea and lens case. |
| [2707046](https://pubmed.ncbi.nlm.nih.gov/2707046/) | 1989 | In vitro | Current Eye Research | In vitro corneal epithelial cytotoxicity comparison of four aminoglycosides (including tobramycin) using a rabbit corneal cell model. |
| [12861116](https://pubmed.ncbi.nlm.nih.gov/12861116/) | 2003 | Case report | Eye & Contact Lens | Bilateral MRSA keratitis following photorefractive keratectomy (PRK). |
| [17228760](https://pubmed.ncbi.nlm.nih.gov/17228760/) | 2006 | Pending classification | Nippon Ganka Gakkai Zasshi | MIC and post-antibiotic effect comparison of antibiotic eye drops against isolates from Japan's National Surveillance of Infectious Keratitis. |
| [33847093](https://pubmed.ncbi.nlm.nih.gov/33847093/) | 2021 | Pending classification | Polish Journal of Veterinary Sciences | Feline ocular toxoplasmosis case series (60 cats) — veterinary, not directly relevant to human exposure keratitis. |
| [14574976](https://pubmed.ncbi.nlm.nih.gov/14574976/) | 2003 | Case report | Yan Ke Xue Bao (Eye Science) | Paracentral corneal dellen as a rare sign of Graves ophthalmopathy — mechanical/inflammatory, not infectious. |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data were not available in the evidence pack — flagged as a **Blocking** data gap that must be resolved before any S1 safety evaluation.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (exposure keratitis) rests on L4 evidence with only Grade C (indirectly relevant) clinical trials and mostly case-report/in-vitro literature. Critically, the evidence pack's own mechanistic analysis states tobramycin cannot treat the primary (non-infectious) pathology of exposure keratitis — it can only serve a prophylactic role against secondary bacterial infection. This is insufficient to proceed.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent product label (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action (MOA) data from DrugBank
- A refined disease-target definition distinguishing "prevention of secondary infection in exposure keratitis" from "treatment of exposure keratitis," since these require different clinical trial designs
- Consideration of re-prioritizing evaluation toward the two stronger candidates identified elsewhere in this same evidence pack: **post-bacterial disease** (rank 5, L1 evidence, multiple completed Phase 3 RCTs in CF-associated *Pseudomonas* pulmonary infection, "Proceed with Guardrails") and **otitis externa** (rank 3, L3 evidence, established clinical use in malignant/necrotizing otitis externa, "Proceed with Guardrails") — both show substantially stronger mechanistic and evidentiary alignment with tobramycin's known antibacterial action than exposure keratitis does.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

