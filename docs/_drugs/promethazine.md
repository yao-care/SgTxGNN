---
layout: default
title: Promethazine
parent: 僅模型預測 (L5)
nav_order: 823
evidence_level: L5
indication_count: 10
---

# Promethazine
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

# Promethazine: From Antihistamine/Antiemetic Use to Allergic Urticaria and Allergic Rhinitis

## One-Sentence Summary

Promethazine is a first-generation phenothiazine H1-antihistamine long used internationally for allergic reactions, motion sickness, and sedation, though it is **not currently registered in Singapore**. Among the 10 indications TxGNN predicted, only **Allergic Urticaria** and **Allergic Rhinitis** are backed by any real-world evidence — a handful of promethazine-specific pharmacology studies and case series — while the other 8 candidates (mostly conjunctivitis subtypes and a rare syndrome) have **zero clinical trials or literature** and rest on model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore; internationally marketed as a first-generation H1-antihistamine used for allergy, motion sickness/nausea, and pre-operative sedation |
| Predicted New Indications | **Allergic Urticaria** (primary) and **Allergic Rhinitis** (secondary) — the only two of 10 predictions with supporting evidence |
| TxGNN Prediction Score | Allergic Urticaria: 98.13% · Allergic Rhinitis: 94.16% |
| Evidence Level | L3 (both — literature-level evidence, no promethazine-specific registered RCTs) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails (Urticaria/Rhinitis only) — **Hold** on the remaining 8 predicted indications |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank query pending — see Data Gaps). Based on known pharmacology, Promethazine is a phenothiazine-class first-generation H1-antihistamine with antihistaminic, anticholinergic, and mast-cell-stabilizing activity, and this class effect is well established across decades of clinical use.

**Allergic Urticaria** and **Allergic Rhinitis** are both classic histamine-mediated conditions (mast cell degranulation → H1 receptor activation → vasodilation, pruritus, wheal formation, and mucosal hypersecretion). H1-receptor blockade is the guideline-standard mechanism for both, so a mechanistic link for promethazine is strong and unsurprising — it is essentially confirming an already-known class effect rather than revealing something novel.

By contrast, the other 8 TxGNN predictions (rosacea conjunctivitis, recalcitrant atopic dermatitis, Angelucci syndrome, acute hemorrhagic conjunctivitis, parasitic conjunctivitis, chronic follicular conjunctivitis, serous conjunctivitis, cold urticaria) involve pathophysiology that is predominantly infectious, vascular/inflammatory, or Th2/barrier-driven rather than simple histamine-mediated allergy. TxGNN assigned these all similarly high scores (>0.92), but score alone does not track with mechanistic plausibility or evidence — none of these 8 have any supporting trial or publication.

---

## Clinical Trial Evidence

### Allergic Urticaria

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04660799](https://clinicaltrials.gov/study/NCT04660799) | Phase 2 | Completed | 50 | Rituximab SC vs IV in DLBCL — **not a promethazine trial**, low relevance (Grade C) |
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | IV cetirizine vs IV diphenhydramine for acute urticaria — antihistamine class comparator, but not promethazine (Grade C) |
| [NCT05354466](https://clinicaltrials.gov/study/NCT05354466) | Phase 4 | Completed | 174 | Sugammadex vs neostigmine for perioperative respiratory events in pediatric tonsillectomy — unrelated mechanism (Grade C) |

*None of the identified trials studied promethazine directly; all are Grade C relevance.*

### Allergic Rhinitis

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00648973](https://clinicaltrials.gov/study/NCT00648973) | Phase 4 | Completed | 1021 | Diphenhydramine 25mg/50mg vs placebo/pseudoephedrine for nasal congestion in seasonal allergic rhinitis — antihistamine class, not promethazine (Grade C) |
| [NCT00599872](https://clinicaltrials.gov/study/NCT00599872) | Phase 3 | Completed | 430 | Sublingual immunotherapy for ragweed allergic rhinoconjunctivitis — different mechanism (Grade C) |
| [NCT05586477](https://clinicaltrials.gov/study/NCT05586477) | Phase 4 | Completed | 20 | Diphenhydramine effect on thermoregulation during exercise — not promethazine (Grade C) |
| [NCT00762749](https://clinicaltrials.gov/study/NCT00762749) | Phase 1 | Completed | 36 | Diphenhydramine pharmacokinetics in children/adolescents — not promethazine (Grade C) |
| [NCT06217367](https://clinicaltrials.gov/study/NCT06217367) | Phase 4 | Unknown | 16 | OTC antihistamines and thermoregulation during heat stress — drug not confirmed as promethazine, status unknown (Grade C) |
| [NCT01177852](https://clinicaltrials.gov/study/NCT01177852) | Phase 3 | Withdrawn | 0 | Diphenhydramine combination for cough/rhinitis in children — withdrawn, no data (Grade C) |
| [NCT01199497](https://clinicaltrials.gov/study/NCT01199497) | Phase 3 | Withdrawn | 0 | Diphenhydramine combination for cough/rhinitis (≥12y) — withdrawn, no data (Grade C) |

*All identified trials studied other antihistamines (diphenhydramine, cetirizine) or unrelated mechanisms; no registered trial evaluated promethazine specifically for rhinitis.*

### Other 8 Predicted Indications

Currently no related clinical trials registered for rosacea conjunctivitis, recalcitrant atopic dermatitis, Angelucci syndrome, acute hemorrhagic conjunctivitis, parasitic conjunctivitis, chronic follicular conjunctivitis, or serous conjunctivitis (except viral).

---

## Literature Evidence

### Allergic Urticaria

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22130869](https://pubmed.ncbi.nlm.nih.gov/22130869/) | 2012 | RCT | Arch Dermatol Res | Single-dose promethazine vs fexofenadine/olopatadine: compares antihistaminic efficacy and psychomotor impairment via histamine wheal-and-flare model |
| [26844217](https://pubmed.ncbi.nlm.nih.gov/26844217/) | 2016 | Cohort/Audit | Asia Pacific Allergy | ED anaphylaxis management audit vs best practice (antihistamines incl. promethazine as adjunct) |
| [15861](https://pubmed.ncbi.nlm.nih.gov/15861/) | 1977 | Review | Farmakologiia i Toksikologiia | Compares phencarol to diphenhydramine and promethazine (diprazine) for urticaria/angioedema; notes promethazine's CNS depressant effect |
| [4402272](https://pubmed.ncbi.nlm.nih.gov/4402272/) | 1972 | Review | Oto-rino-laringologie | Antihistamine use in allergic rhinopathies |
| [736582](https://pubmed.ncbi.nlm.nih.gov/736582/) | 1978 | Case report | Arch Dermatol | Photoallergic/solar urticaria mechanism study |
| [1453998](https://pubmed.ncbi.nlm.nih.gov/1453998/) | 1992 | Case series | Med J Aust | Scombroid (histamine) poisoning presenting with urticaria-like symptoms |
| [12368120](https://pubmed.ncbi.nlm.nih.gov/12368120/) | 2002 | Case report | Toxicon | Generalized urticarial reaction following spider contact |
| [27725018](https://pubmed.ncbi.nlm.nih.gov/27725018/) | 2016 | Case report | S Afr Med J | Angio-oedema associated with colistin |
| [19797416](https://pubmed.ncbi.nlm.nih.gov/19797416/) | 2010 | Case report | Jpn J Clin Oncol | Desensitization protocol for sunitinib-induced hypersensitivity |

### Allergic Rhinitis

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24791618](https://pubmed.ncbi.nlm.nih.gov/24791618/) | 2014 | RCT | Clin Neurophysiol | Consecutive daily dosing of promethazine vs loratadine: drowsiness and motor response comparison |
| [22130869](https://pubmed.ncbi.nlm.nih.gov/22130869/) | 2012 | RCT | Arch Dermatol Res | Promethazine vs fexofenadine/olopatadine: psychomotor function and histamine-wheal suppression |
| [12113215](https://pubmed.ncbi.nlm.nih.gov/12113215/) | 2002 | Review | Clin Allergy Immunol | Antiallergic/anti-inflammatory effects of H1-antihistamines including promethazine, independent of H1 blockade |
| [17089107](https://pubmed.ncbi.nlm.nih.gov/17089107/) | 2006 | Cohort | Eur J Clin Pharmacol | CYP2D6*10 genotype impact on H1-antihistamine-induced hypersomnia |
| [38746603](https://pubmed.ncbi.nlm.nih.gov/38746603/) | 2023 | Review | Acta Clin Croat | Airway/premedication considerations in obstetric anesthesia |
| [568438](https://pubmed.ncbi.nlm.nih.gov/568438/) | 1978 | Case series | Ann Allergy | Long-term (6–48 month) promethazine use in chronic rhinitis of preschool children |
| [13593960](https://pubmed.ncbi.nlm.nih.gov/13593960/) | 1958 | Case series | AMA Arch Otolaryngol | 66 patients with secretory otitis media/nasal allergy treated with promethazine |
| [14175878](https://pubmed.ncbi.nlm.nih.gov/14175878/) | 1964 | Review | Can Med Assoc J | General treatment approach to allergic rhinitis |
| [2896668](https://pubmed.ncbi.nlm.nih.gov/2896668/) | 1987 | Survey | J Clin Pharm Ther | 12-month community pharmacy prescribing pattern of H1-antihistamines |
| [38967232](https://pubmed.ncbi.nlm.nih.gov/38967232/) | 2024 | Basic/histology | Dent Med Probl | Antihistamine effects on iNOS/caspase-3/α-SMA expression in rat parotid gland |

### Cold Urticaria (Rank 3 — for reference, insufficient evidence)

Only one literature record exists: [PMID 4396149](https://pubmed.ncbi.nlm.nih.gov/4396149/) (1970, case report on physical allergies) — a single 55-year-old publication with no clinical trials. This does not meet the bar for further action at this time.

### Remaining 6 Predicted Indications

Currently no related literature available for rosacea conjunctivitis, recalcitrant atopic dermatitis, Angelucci syndrome, acute hemorrhagic conjunctivitis, parasitic conjunctivitis, chronic follicular conjunctivitis, or serous conjunctivitis (except viral).

---

## Singapore Market Information

Promethazine currently holds **no marketing authorization in Singapore** (0 registered licenses on record). No dosage forms, brand names, or approved indication text are available from local regulatory sources for this product.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured key warnings, contraindications, or drug–drug interaction data were retrievable at this time (TFDA-equivalent label data is flagged as a **Blocking** data gap — see Conclusion below).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (Allergic Urticaria and Allergic Rhinitis only) — **Hold** on the other 8 predicted indications.

**Rationale:**
- Allergic Urticaria and Allergic Rhinitis are mechanistically well-supported (classic H1-antihistamine indications) and have multiple promethazine-specific pharmacology studies and case series (L3), even though no registered RCT targets these indications directly with promethazine.
- The remaining 8 indications (rosacea conjunctivitis, atopic dermatitis, Angelucci syndrome, and four conjunctivitis subtypes) have **no clinical trials or literature** (L5) and involve pathophysiology not primarily histamine-driven — these should not proceed past model prediction stage.

**To proceed, the following is needed:**
- **Blocking gap:** Obtain official product label warnings/contraindications (TFDA or equivalent) before any S1 safety review can begin — this is currently missing entirely.
- Obtain verified mechanism of action data from DrugBank API (currently unavailable).
- Since promethazine is unregistered in Singapore, determine the regulatory pathway (new registration vs. named-patient/compassionate use) required before any repurposing indication could be pursued locally.
- Seek promethazine-specific controlled trials in urticaria/rhinitis populations, since current evidence relies on pharmacodynamic comparator studies and decades-old case series rather than modern RCTs.
- Do not advance cold urticaria or the remaining conjunctivitis/dermatologic predictions without new primary evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

