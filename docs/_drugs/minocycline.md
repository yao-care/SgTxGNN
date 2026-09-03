---
layout: default
title: Minocycline
parent: 僅模型預測 (L5)
nav_order: 670
evidence_level: L5
indication_count: 10
---

# Minocycline
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

# Minocycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Minocycline is a broad-spectrum, semisynthetic tetracycline-class antibiotic classically used to treat bacterial infections (e.g., acne, respiratory and periodontal infections); it is **not currently marketed in Taiwan**. The TxGNN model's top-ranked prediction is **Punctate Epithelial Keratoconjunctivitis** (score **99.63%**), but this is a pure knowledge-graph prediction with **no clinical trials and no literature** currently identified for it — evidence level **L5**. This Evidence Pack screened 10 candidate indications in total; three of them (post-bacterial disorder, otitis externa, post-infectious syndrome) have real supporting trial/literature evidence and are summarized separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (tetracycline-class antibiotic) — no Taiwan-approved indication text on file; drug is not marketed in Taiwan |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for Minocycline is not available in this Evidence Pack (marked as a High-severity data gap). Based on generally known pharmacology, Minocycline belongs to the tetracycline class and, beyond its antibacterial action, is known for anti-inflammatory and matrix metalloproteinase-9 (MMP-9) inhibitory effects — a class effect it shares with doxycycline, which is already used clinically for ocular-surface inflammatory conditions.

For **Punctate Epithelial Keratoconjunctivitis** specifically, the rationale supplied with this candidate states that the link is a *class-effect extrapolation*: because tetracyclines such as doxycycline are used for ocular surface inflammation via MMP-9 inhibition and anti-inflammatory activity, Minocycline is assumed to behave similarly. However, **no clinical trial or publication was found that studies Minocycline itself in this indication**, and the fact that Minocycline is not marketed in Taiwan further limits near-term feasibility of developing an ophthalmic formulation. This prediction should therefore be treated as a hypothesis generated purely from the knowledge graph, not as an evidence-backed direction.

Because the headline (rank 1) prediction is evidence-thin, this Evidence Pack also evaluated nine other candidate indications for Minocycline. Three of them — post-bacterial disorder, otitis externa, and post-infectious syndrome — have real clinical-trial and/or literature support and are more promising near-term research directions (see "Other TxGNN-Predicted Indications" below).

---

## Clinical Trial Evidence
*(for the headline prediction: Punctate Epithelial Keratoconjunctivitis)*

Currently no related clinical trials registered.

---

## Literature Evidence
*(for the headline prediction: Punctate Epithelial Keratoconjunctivitis)*

Currently no related literature available.

---

## Other TxGNN-Predicted Indications (Full Candidate List)

This Evidence Pack scored 10 candidate indications for Minocycline. Only 3 currently have supporting evidence; the rest are model-prediction-only (L5) and are held pending further data.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Note |
|------|----------------------|-------------|-----------------|-----------------|------|
| 1 | Punctate epithelial keratoconjunctivitis | 99.63% | L5 | Hold | Class-effect theory only; no direct evidence |
| 2 | Exposure keratitis | 99.20% | L5 | Hold | Same class-effect theory only |
| 3 | Neurotrophic keratopathy | 98.98% | L5 | Hold | Cross-system (CNS → cornea) analogy only |
| 4 | Postinfectious vasculitis | 98.76% | L5 | Hold | ⚠️ Safety flag — see below |
| 5 | Post-bacterial disorder | 98.74% | L3 | Research Question | 16 trials found; see detail table below |
| 6 | Otitis externa | 98.70% | L4 | Research Question | 5 literature items found; see detail table below |
| 7 | Post-infectious syndrome | 98.68% | L3 | Research Question | 8 trials found; see detail table below |
| 8 | Chronic ethmoidal sinusitis | 98.67% | L5 | Hold | No trials or literature |
| 9 | Chronic rhinosinusitis | 98.63% | L5 | Hold | 1 background review only, not drug-specific |
| 10 | Paranasal sinus neoplasm | 98.61% | L5 | Hold | No trials or literature; oncology indication requires separate pathway |

> ⚠️ **Safety flag — Postinfectious Vasculitis (Rank 4):** The evidence pack explicitly warns that Minocycline is a **known cause** of drug-induced ANCA-associated vasculitis / lupus-like vasculitis. The TxGNN co-occurrence signal here may reflect this adverse-event relationship rather than a genuine treatment effect (possible reversed causality). This candidate should **not** be advanced without ruling out this confound.

### Post-bacterial disorder (Rank 5) — Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06307288](https://clinicaltrials.gov/study/NCT06307288) | Phase 4 | Enrolling by Invitation | 45 | Tranilast + Minocycline vs. Minocycline alone for rosacea (mast-cell stabilization mechanism) |
| [NCT00662532](https://clinicaltrials.gov/study/NCT00662532) | Phase 3 | Completed | 44 | Minocycline HCl 1mg microspheres for peri-implantitis (dental-implant infection) |
| [NCT03964935](https://clinicaltrials.gov/study/NCT03964935) | Phase 2 | Unknown | 30 | Minocycline microspheres vs. lycopene gel as periodontal adjunct; measured MMP-9/TGF-β1/IL-8 |
| [NCT02099240](https://clinicaltrials.gov/study/NCT02099240) | Early Phase 1 | Terminated | 11 | IV antibiotics (incl. minocycline) with/without early oral switch, for osteomyelitis |
| [NCT05575427](https://clinicaltrials.gov/study/NCT05575427) | Phase 4 | Unknown | 112 | Minocycline combination therapy for *Stenotrophomonas maltophilia* infection |
| [NCT03369951](https://clinicaltrials.gov/study/NCT03369951) | Phase 4 | Completed | 58 | PK/PD of single-dose IV Minocin in critically ill ICU patients with Gram-negative infection |
| [NCT02802631](https://clinicaltrials.gov/study/NCT02802631) | Phase 1 | Completed | 69 | Safety, tolerability and PK of IV Minocin in healthy adults (ascending dose) |
| [NCT00668746](https://clinicaltrials.gov/study/NCT00668746) | Phase 4 | Completed | 35 | Long-term safety/resistance evaluation of minocycline microspheres in chronic periodontitis |
| [NCT05530252](https://clinicaltrials.gov/study/NCT05530252) | Phase 4 | Completed | 51 | Antimicrobial peptides after non-surgical periodontal therapy (minocycline as reference) |
| [NCT06075979](https://clinicaltrials.gov/study/NCT06075979) | N/A | Recruiting | 200 | Investigating low-toxicity bacterial infection in lumbar degenerative disc disease |

*Note: "post-bacterial disorder" is a broad/ambiguous disease-node label in the knowledge graph. Actual trials above concern periodontal disease, rosacea, osteomyelitis, and Gram-negative infections — the exact clinical scope this node represents should be clarified before further action.*

### Otitis externa (Rank 6) — Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12542200](https://pubmed.ncbi.nlm.nih.gov/12542200/) | 2002 | Cohort | Acta Oto-Laryngologica | Community-acquired MRSA prevalence in discharging ears (otorrhoea) |
| [12437801](https://pubmed.ncbi.nlm.nih.gov/12437801/) | 2002 | Cohort | J Laryngol Otol | Bacteriology of 161 discharging-ear patients in Taiwan; S. aureus and Pseudomonas most common pathogens |
| [4405139](https://pubmed.ncbi.nlm.nih.gov/4405139/) | 1972 | Case series | Jpn J Antibiot | Early clinical use of minocycline dry syrup for ENT infections |
| [37026784](https://pubmed.ncbi.nlm.nih.gov/37026784/) | 2023 | In vitro | Otology & Neurotology | Tetracyclines are less cytotoxic than quinolones to tympanic membrane fibroblasts |
| [34009720](https://pubmed.ncbi.nlm.nih.gov/34009720/) | 2021 | Cohort/ecological | Veterinary Dermatology | AMR patterns in *S. pseudintermedius* (veterinary; antimicrobial-stewardship context) |

### Post-infectious syndrome (Rank 7) — Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00855062](https://clinicaltrials.gov/study/NCT00855062) | Phase 1/2 | Terminated | 73 | Minocycline for HIV-associated cognitive impairment (Uganda), 24-week RCT — direct drug/indication match, but terminated |
| [NCT07280572](https://clinicaltrials.gov/study/NCT07280572) | Phase 3 | Enrolling by Invitation | 1250 | RECLAIM adaptive platform trial for Long COVID (PASC); a minocycline treatment domain is planned from Jan 2026 (not yet confirmed active) |
| [NCT01053156](https://clinicaltrials.gov/study/NCT01053156) | N/A | Completed | 66 | Minocycline crossover trial in children with Fragile X Syndrome (lowers MMP-9); genetic, not post-infectious |
| [NCT04130451](https://clinicaltrials.gov/study/NCT04130451) | Phase 1/2 | Unknown | 104 | Talc/povidone-iodine pleurodesis for pneumothorax; minocycline mentioned as an alternative pleurodesis agent |
| [NCT00378781](https://clinicaltrials.gov/study/NCT00378781) | N/A | Withdrawn | 0 | Heparin vs. Minocycline-EDTA catheter flush for infection/occlusion prevention — withdrawn, 0 enrolled |
| [NCT00114530](https://clinicaltrials.gov/study/NCT00114530) | Phase 2/3 | Completed | 75 | Stem-cell transplant vs. cyclophosphamide for severe systemic sclerosis — no minocycline arm |
| [NCT03975790](https://clinicaltrials.gov/study/NCT03975790) | N/A | Completed | 479 | Claims-database study of tofacitinib+MTX in RA — no minocycline |
| [NCT06693362](https://clinicaltrials.gov/study/NCT06693362) | Phase 1 | Recruiting | 60 | Mesenchymal stem cell injection for severe viral pneumonia — minocycline involvement unconfirmed |

*Note: only the first two trials directly match both drug and disease concept; the remainder are largely knowledge-graph co-occurrence noise.*

---

## Safety Considerations

Please refer to the package insert for safety information — no drug-drug interaction, warning, or contraindication data was retrievable in this Evidence Pack (DDI query returned "not found"; TFDA label warnings/contraindications are marked as a **Blocking** data gap, meaning this candidate cannot yet proceed to an S1 safety pre-assessment).

Additionally note the specific signal identified during indication screening: Minocycline has a recognized association with **drug-induced ANCA-associated / lupus-like vasculitis**, which is directly relevant to candidate indication #4 (postinfectious vasculitis) and should be considered a contraindication-adjacent signal regardless of which indication is pursued.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The headline TxGNN prediction (punctate epithelial keratoconjunctivitis) is supported only by class-effect theory with no drug-specific clinical or literature evidence (L5), and a Blocking data gap (missing TFDA/label safety data) prevents this candidate from entering safety pre-assessment (S1) for any indication. Three secondary candidates (post-bacterial disorder, otitis externa, post-infectious syndrome) have real supporting evidence and are already at decision stage S1 ("Research Question"), but require disease-node clarification before they can be prioritized over the headline prediction.

**To proceed, the following is needed:**
- TFDA label data (warnings, contraindications, precautions) — currently Blocking (DG001)
- Drug-specific mechanism of action (MOA) data from DrugBank — currently High priority (DG002)
- Clarification of the exact clinical scope of the "post-bacterial disorder" knowledge-graph node, to determine whether the associated trials (periodontitis, rosacea, osteomyelitis) genuinely represent this indication
- Confirmation of whether Minocycline is included as an active arm in the ongoing RECLAIM (Long COVID) platform trial (NCT07280572)
- A dedicated pharmacovigilance review of Minocycline-induced vasculitis before any further consideration of candidate #4
- If any candidate advances, a feasibility assessment for introducing Minocycline to the Taiwan market, since it currently holds no local registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

