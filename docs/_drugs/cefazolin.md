---
layout: default
title: Cefazolin
parent: 僅模型預測 (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
---

# Cefazolin
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

# Cefazolin: From Bacterial Infection Prophylaxis to Infectious Otitis Media

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic established in clinical practice for surgical site infection prophylaxis and treatment of susceptible gram-positive bacterial infections.
The TxGNN model predicts it may be effective for **Infectious Otitis Media**,
with **1 clinical trial** and **3 publications** currently supporting this direction.
However, critical antibacterial spectrum gaps against key otitis media pathogens limit the strength of this prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no Singapore regulatory registration on record) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available from DrugBank records. Based on established pharmacology, Cefazolin is a first-generation cephalosporin antibiotic that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs). It demonstrates strong activity against gram-positive organisms — particularly methicillin-susceptible *Staphylococcus aureus* (MSSA), *Streptococcus pyogenes*, and *Streptococcus pneumoniae* — but has limited activity against gram-negative organisms such as *Haemophilus influenzae* and *Moraxella catarrhalis*.

Infectious otitis media (acute otitis media, AOM) is caused primarily by three pathogens: *S. pneumoniae*, *H. influenzae*, and *M. catarrhalis*. Cefazolin can plausibly cover the *S. pneumoniae* component, which accounts for approximately 25–30% of bacterial AOM cases. However, it lacks meaningful activity against *H. influenzae* and *M. catarrhalis*, which together account for over 50% of bacterial AOM. This represents a critical antibacterial spectrum gap for empiric otitis media treatment. In the specific scenario where AOM is confirmed to involve gram-positive organisms only (e.g., *S. pyogenes*), the mechanistic rationale is considerably stronger.

The TxGNN prediction likely arises from Cefazolin's established role in treating gram-positive ear and upper respiratory tract infections, and its structural and pharmacological similarity to later-generation cephalosporins that do hold formal otitis media indications (e.g., cefuroxime, cefdinir). In practice, however, Cefazolin's IV-only formulation and incomplete pathogen coverage make it a suboptimal empiric choice for routine AOM treatment compared to oral alternatives with broader spectrum.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2b | Terminated | 520 | Multicenter double-blind RCT comparing 5-day vs 10-day antibiotic courses in children aged 6–23 months with AOM. The trial was terminated before completion; no efficacy conclusions are available. The reason for early termination has not been disclosed and requires investigation to rule out safety signals. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case Report | Ann Otol Rhinol Laryngol | Describes ceftazidime–cefazolin empiric combination therapy for pediatric Gradenigo Syndrome — a rare complication of petrous apicitis secondary to acute otitis media. Cefazolin contributed gram-positive coverage; authors proposed this combination as an empiric alternative where standard monotherapy is inadequate. |
| [877649](https://pubmed.ncbi.nlm.nih.gov/877649/) | 1977 | General Review | South Med J | Broad review of cephalosporin use in pediatric infections. Notes the inhibitory efficacy of first-generation cephalosporins against some organisms relevant to pediatric ear infections, but predates modern AOM pathogen characterisation. Historical reference value only. |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Clinical Review | Clin Pharmacy | Case report and literature review of Stevens-Johnson syndrome in a child with concurrent otitis media. Cefazolin appears as part of a complex treatment course, not as a targeted otitis media therapy. Limited direct relevance to the predicted indication. |

---

## Singapore Market Information

Cefazolin is currently **not registered** in Singapore. No active product licences or marketing authorisations are on record with the Health Sciences Authority (HSA).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole clinical trial for infectious otitis media was terminated before completion, yielding no efficacy conclusions, and all three supporting publications are case-level or historical reviews with minimal direct relevance. More fundamentally, Cefazolin lacks antibacterial activity against *H. influenzae* and *M. catarrhalis* — the two most prevalent AOM pathogens after *S. pneumoniae* — creating a mechanistic basis too narrow for empiric use in an unselected otitis media population.

**To proceed, the following is needed:**

- **Termination reason for NCT01511107**: Determine whether early stopping reflected a safety signal, futility finding, or administrative cause before any further clinical development is considered
- **MOA and DrugBank data**: Formal confirmation of spectrum and pharmacodynamics from DrugBank to support mechanistic analysis
- **Pathogen-stratified strategy**: Cefazolin may be appropriate in scenarios confirmed to involve gram-positive pathogens only (e.g., post-culture *S. pyogenes* AOM); prospective data in this subgroup would be required
- **Singapore registration pathway**: Cefazolin is not registered locally; regulatory filing with HSA would be a prerequisite to any clinical use
- **Package insert and safety data**: TFDA prescribing information should be obtained to complete safety assessment (warnings, contraindications, DDI)
- **Consider adjacent indications with stronger evidence**: Middle ear disease in the surgical prophylaxis context (L2, "Proceed with Guardrails") and urinary tract infection (L3, "Proceed with Guardrails") both present more mechanistically coherent and better-evidenced opportunities within this Evidence Pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

