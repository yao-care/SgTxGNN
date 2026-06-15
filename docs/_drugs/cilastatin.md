---
layout: default
title: Cilastatin
parent: 僅模型預測 (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
---

# Cilastatin
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

# Cilastatin: From Imipenem/Cilastatin Combination Component to Staphylococcus Aureus Infection

## One-Sentence Summary

Cilastatin is a renal dehydropeptidase-I (DHP-I) inhibitor with no standalone antibacterial activity, used exclusively as a fixed-dose combination partner with Imipenem to prevent its renal degradation and protect against nephrotoxicity.
The TxGNN model predicts it may be effective for **Staphylococcus aureus infection** (encompassing both MSSA and MRSA),
with **3 clinical trials** and **20 publications** currently indexed — though most evidence reflects the Imipenem/Cilastatin combination as a whole, rather than Cilastatin's independent contribution.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No independent registered indication; used exclusively as part of the Imipenem/Cilastatin fixed-dose combination for broad-spectrum bacterial infections |
| Predicted New Indication | Staphylococcus aureus infection |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Cilastatin is not available from the Evidence Pack. Based on known pharmacological information, Cilastatin is the indispensable companion component of the Imipenem/Cilastatin fixed-dose combination (brand name: Tienam®). Its sole function is to competitively and reversibly inhibit the renal brush-border enzyme dehydropeptidase-I (DHP-I), which would otherwise rapidly metabolize and inactivate Imipenem in the proximal renal tubule. By protecting Imipenem from this degradation, Cilastatin enables the antibiotic to sustain effective concentrations in blood and tissues, while simultaneously reducing Imipenem-associated nephrotoxicity.

The mechanistic rationale linking this combination to Staphylococcus aureus infection rests on Imipenem's β-lactam activity: Imipenem binds with high affinity to penicillin-binding proteins (PBPs) and disrupts bacterial cell wall synthesis, conferring broad-spectrum bactericidal activity that includes methicillin-susceptible S. aureus (MSSA). Cilastatin's pharmacokinetic "enabling" role allows Imipenem to reach adequate tissue concentrations needed to sustain time-dependent killing (T>MIC). However, a critical biological caveat limits this prediction: methicillin-resistant S. aureus (MRSA) carries the mecA gene encoding PBP2a, a low-affinity PBP that confers intrinsic resistance to all β-lactams including carbapenems. For MRSA, Imipenem/Cilastatin is ineffective as monotherapy, and any clinical utility requires synergistic combinations (e.g., with Arbekacin, Fosfomycin, or Cefotiam, as described in several case reports and in vitro studies).

The TxGNN model's high prediction score (99.94%, global rank #1,315) likely reflects the Imipenem/Cilastatin combination's well-documented activity across diverse bacterial pathogens captured as co-occurring nodes in the underlying knowledge graph, rather than a truly novel repurposing signal for Cilastatin specifically against S. aureus. The repurposing hypothesis requires further mechanistic disambiguation: MSSA infections represent an established (not novel) use of the combination, while MRSA represents an experimental niche requiring combination strategies.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Phase 3 | Completed | 274 | IMI/Cilastatin/Relebactam vs. Piperacillin/Tazobactam for hospital-acquired bacterial pneumonia (HABP) and ventilator-associated bacterial pneumonia (VABP); non-inferiority design with Imipenem/Cilastatin as the carbapenem backbone — not S. aureus-specific |
| [NCT00707239](https://clinicaltrials.gov/study/NCT00707239) | Phase 2 | Terminated | 108 | Two doses of Tigecycline vs. Imipenem/Cilastatin for hospital-acquired pneumonia (≥70% VAP); Imipenem/Cilastatin served as the active comparator arm; early termination limits conclusions, and S. aureus was not the primary target organism |
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Phase 4 | Unknown | 60 | Linezolid alone or combined with Carbapenem (including Imipenem/Cilastatin) against MRSA in ventilator-associated pneumonia patients; small scale and unknown status substantially limit evidence quality; investigates synergy relevant to the MRSA repurposing hypothesis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | Comparative Clinical Study | Antimicrobial Agents and Chemotherapy | Imipenem-cilastatin evaluated in 23 patients (11 MRSA, 12 MSSA) with soft tissue, endovascular, and skeletal infections; demonstrated efficacy for MSSA; limited activity against MRSA confirmed in vitro (MIC90 6.25 mg/L) |
| [8072190](https://pubmed.ncbi.nlm.nih.gov/8072190/) | 1994 | Clinical Trial | The Japanese Journal of Antibiotics | Arbekacin (ABK) + Imipenem/Cilastatin combination showed synergistic MIC reductions against MRSA clinical isolates; combination superior to either agent alone, supporting a salvage combination strategy |
| [3378959](https://pubmed.ncbi.nlm.nih.gov/3378959/) | 1988 | Animal Model | Journal of Antimicrobial Chemotherapy | Rabbit model of MRSA aortic valve endocarditis: Imipenem bacteriostatic in vitro (MIC90/MBC90: 8/32 mg/L) vs vancomycin bactericidal; Imipenem-cilastatin showed comparable or superior efficacy to vancomycin by several in vivo criteria |
| [10588305](https://pubmed.ncbi.nlm.nih.gov/10588305/) | 1999 | In Vitro / In Vivo Study | Journal of Antimicrobial Chemotherapy | Vancomycin + Imipenem demonstrated synergistic or additive effects in 36 of 36 MRSA clinical isolates in vitro, with confirmation in a neutropenic mouse thigh infection model |
| [8514648](https://pubmed.ncbi.nlm.nih.gov/8514648/) | 1993 | Animal Model | Journal of Antimicrobial Chemotherapy | Imipenem/Cilastatin + Cefotiam synergistic against MRSA in mouse bacteremia model, effective against both β-lactamase-producing and non-producing MRSA strains at ratios of 1:5 to 1:160 |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | Case Commentary | Antimicrobial Agents and Chemotherapy | Commentary on use of Imipenem/Cilastatin + Fosfomycin for refractory MRSA bacteremia; argues that individualized combination selection is essential given the near-impossibility of conducting RCTs in this patient population |
| [22196394](https://pubmed.ncbi.nlm.nih.gov/22196394/) | 2012 | Narrative Review | International Journal of Antimicrobial Agents | Comprehensive review of MRSA pathogenesis and treatment; discusses carbapenems in the context of combination regimens for serious healthcare-associated MRSA infections |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Narrative Review | International Journal of Antimicrobial Agents | Off-label antibiotic use for multidrug-resistant bacteria; includes discussion of carbapenem combinations for resistant Gram-positive pathogens, contextualizing the role of Imipenem/Cilastatin in MDR scenarios |
| [12878512](https://pubmed.ncbi.nlm.nih.gov/12878512/) | 2003 | In Vivo Preclinical Study | Antimicrobial Agents and Chemotherapy | Comparative in vivo study: Imipenem-cilastatin less active against MRSA (ED50 >100 mg/kg) compared to vancomycin and the experimental cephalosporin S-3578; reinforces carbapenem limitations as MRSA monotherapy |
| [18649613](https://pubmed.ncbi.nlm.nih.gov/18649613/) | 2008 | Clinical Review | American Family Physician | Diabetic foot infection review: S. aureus and β-hemolytic streptococci predominate in mild-to-moderate infections; severe or polymicrobial diabetic foot infections may require broad-spectrum coverage including carbapenems as second-line agents |

---

## Singapore Market Information

Cilastatin currently has **no registered products** in Singapore. It is not available as a standalone agent; it is always co-formulated with Imipenem. There are no Health Sciences Authority (HSA) product authorizations on record for this compound.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The clinical trials and literature in this Evidence Pack address the Imipenem/Cilastatin combination against broad nosocomial infections — none is specifically designed to evaluate Cilastatin's contribution to S. aureus outcomes. More critically, Cilastatin carries no independent antibacterial activity; it is a pharmacokinetic enhancer. For MSSA, Imipenem/Cilastatin is already an established treatment option (not a repurposing opportunity), while MRSA is intrinsically carbapenem-resistant, making straightforward repurposing biologically untenable without a defined combination strategy and specific patient population.

**To proceed, the following is needed:**
- **Clarify the repurposing hypothesis**: Is the target MSSA (established use, low novelty) or MRSA in a defined combination regimen (experimental, requires dedicated study design)?
- **Fill the MOA data gap**: Query the DrugBank API (DB01597) to retrieve full pharmacological data and support mechanistic analysis
- **Resolve the safety data gap**: Download and parse the TFDA/FDA package insert PDF to complete safety and contraindication assessment before any regulatory pathway can be evaluated
- **Define a specific clinical niche**: A narrowly scoped question — such as "Imipenem/Cilastatin + Fosfomycin for MRSA bacteremia in patients failing vancomycin" — is more tractable than the broad indication "S. aureus infection"
- **Clarify whether Cilastatin is the true repurposing candidate**: If the clinical signal belongs to the Imipenem/Cilastatin combination, the repurposing unit of analysis should be the combination drug (DB00691 + DB01597), not Cilastatin alone
- **Note on a higher-evidence opportunity**: The pneumonia indication (TxGNN rank #6 in this pack) carries **L1 evidence** supported by multiple completed Phase 3 RCTs — if the goal is to identify the most actionable repurposing candidate for this drug, pneumonia warrants prioritized evaluation over S. aureus infection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

