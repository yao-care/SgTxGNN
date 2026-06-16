---
layout: default
title: Erythromycin
parent: 僅模型預測 (L5)
nav_order: 394
evidence_level: L5
indication_count: 10
---

# Erythromycin
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

# Erythromycin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Erythromycin is a macrolide antibiotic with broad-spectrum activity, historically used to treat bacterial infections of the respiratory tract, skin, and sexually transmitted infections including chlamydial disease.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
with **0 clinical trials** and **2 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Singapore (HSA) registration — known use: broad-spectrum bacterial infections |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Erythromycin is a macrolide antibiotic that inhibits bacterial protein synthesis by binding reversibly to the 50S ribosomal subunit, blocking translocation of aminoacyl-tRNA and halting polypeptide chain elongation. This mechanism confers activity against gram-positive organisms (notably *Staphylococcus aureus*, *Streptococcus* spp.) and atypical intracellular pathogens including *Chlamydia trachomatis* — organisms frequently implicated in lid margin disease.

Punctate epithelial keratoconjunctivitis (PEK) is a non-specific corneal condition characterised by fine epithelial erosions and is often secondary to chronic blepharitis, meibomian gland dysfunction, or infectious conjunctivitis. Erythromycin ophthalmic ointment is an established standard-of-care agent for bacterial blepharitis and blepharokeratoconjunctivitis — conditions that share direct pathophysiological overlap with PEK. When lid margin staphylococcal colonisation or chlamydial infection is the root trigger, erythromycin's anti-staphylococcal and anti-chlamydial coverage provides a mechanistically plausible pathway to corneal epithelial improvement.

However, this remains a mechanism-based hypothesis. No study directly evaluates erythromycin as a therapy for PEK as a primary endpoint, and the TxGNN prediction likely reflects the drug–disease network proximity via the blepharitis–PEK pathophysiological bridge rather than direct clinical evidence. L4 evidence tier: the prediction is biologically rational but unverified in controlled trials.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11495307](https://pubmed.ncbi.nlm.nih.gov/11495307/) | 2001 | Review / Management Guideline | Journal of Pediatric Ophthalmology and Strabismus | Reviews history, symptoms, clinical signs, and treatment strategies for chronic blepharokeratoconjunctivitis in children — a condition mechanistically linked to punctate epithelial changes; erythromycin is among discussed antimicrobial options |
| [32826651](https://pubmed.ncbi.nlm.nih.gov/32826651/) | 2021 | Case Report | Cornea | Dual molecular diagnosis of microsporidia (*Encephalitozoon hellem*) keratoconjunctivitis in an immunocompetent adult via metagenomic sequencing — illustrates the breadth of infectious etiologies requiring targeted antimicrobial therapy in keratoconjunctivitis |

---

## Singapore Market Information

Erythromycin is not registered with the Health Sciences Authority (HSA) of Singapore. No product licences are on record in the HSA database.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Formal safety data (key warnings, contraindications, drug–drug interactions) were not available in this evidence pack. TFDA package insert review is identified as a blocking data gap (DG001) and must be completed before any clinical evaluation proceeds.

---

## Additional Noteworthy Predictions

While this report focuses on the top-ranked TxGNN prediction, two lower-ranked indications carry substantively stronger clinical evidence and may warrant prioritised investigation over Punctate Epithelial Keratoconjunctivitis:

**Lymphogranuloma Venereum (Rank 4 | L3 | "Proceed with Guardrails")**
LGV is caused by *Chlamydia trachomatis* serovars L1–L3. Erythromycin has a documented historical role as an alternative treatment (particularly in pregnancy, 21-day course) in WHO/CDC guidelines. One completed Phase 4 RCT (NCT03608774, n=177) confirms macrolide class efficacy; a 1955 clinical publication (PMID 13239093) directly records erythromycin use in early LGV. Evidence level L3 supports further evaluation pending local STI guideline alignment.

**Necrotising Ulcerative Gingivitis (Rank 5 | L3 | "Proceed with Guardrails")**
Vincent's angina is a mixed anaerobic infection (*Fusobacterium nucleatum* / *Treponema vincentii*). PMID 13221896 (1953) provides direct historical clinical evidence of erythromycin ("Ilotycin") for fusospirochetal oropharyngeal infection; PMID 6589179 (1984) identifies erythromycin as a second-line antibiotic of choice in dental infections for penicillin-allergic patients. Evidence is pre-RCT era but has direct drug–disease correspondence.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a very high prediction score (99.89%) reflecting strong network proximity, but the mechanistic link to Punctate Epithelial Keratoconjunctivitis is indirect — bridged via established blepharitis use rather than direct evidence. With zero registered clinical trials and only two tangentially related publications, the evidence does not meet the threshold for clinical deployment.

**To proceed, the following is needed:**
- Retrieve official MOA data from DrugBank (DG002) to formalise the mechanistic rationale
- Obtain TFDA package insert (DG001) for key warnings, contraindications, and drug interactions — this is a blocking prerequisite for any safety evaluation
- Commission a systematic literature search specifically combining erythromycin + PEK or erythromycin ophthalmic ointment + corneal epithelial disease
- Determine causative aetiology in target PEK patients (bacterial vs. viral vs. toxic/allergic) — antibiotic therapy is only appropriate for the bacterial subset
- Consider redirecting near-term clinical evaluation to Lymphogranuloma Venereum (Rank 4, L3) or Necrotising Ulcerative Gingivitis (Rank 5, L3), where evidence maturity is substantively higher
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

