---
layout: default
title: Mometasone Furoate
parent: 僅模型預測 (L5)
nav_order: 667
evidence_level: L5
indication_count: 10
---

# Mometasone Furoate
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

# Mometasone Furoate: From Corticosteroid Therapy to Nasal/Sinus Polyp Disease (Frontal Sinus Polyp)

## One-Sentence Summary

Mometasone furoate is a topical corticosteroid; this evidence pack does not record an original approved indication for the product, and it currently holds **no market registration in Singapore**. Among 10 TxGNN-predicted candidate indications, the model's single **top-scoring** hit (98.62%, "2-hydroxyethyl methacrylate sensitization") has **zero** supporting trials or literature and is not clinically actionable. The most credible repurposing signal instead comes from **Polyp of the Frontal Sinus** (rank 4, **97.55%**), supported by **16 clinical trials** — including a trial that places a mometasone-furoate-eluting sinus implant directly in the frontal sinus — consistent with mometasone's known anti-inflammatory mechanism in nasal/sinus polyp disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack — mometasone furoate is a topical corticosteroid, but no approved-indication text or Singapore license record exists for this product |
| Predicted New Indication | Polyp of the Frontal Sinus (an anatomic subtype of chronic rhinosinusitis with nasal polyps) |
| TxGNN Prediction Score | 97.55% (rank 4 of 10 screened candidates) |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

> **Note:** Per the standard extraction rule this table would default to the model's #1-ranked candidate. That candidate ("2-hydroxyethyl methacrylate sensitization," 98.62%) has no clinical trials, no literature, and no plausible mechanistic link beyond a generic "topical steroids treat contact dermatitis" argument — it is not a usable repurposing signal. This report instead focuses on the highest-evidence candidate in the pack (rank 4). All 10 candidates are listed for completeness in **Other Candidates Considered** below.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned for this product in the current evidence pack (flagged as data gap DG002). Based on general pharmacological knowledge, mometasone furoate is a synthetic corticosteroid administered topically (nasal spray or sinus-implant device) that suppresses inflammatory mediator release, reduces mucosal edema, and inhibits the chronic inflammatory/hyperplastic tissue response that drives polyp formation. This mechanism is already the basis of an FDA-cleared, commercially available product — a mometasone-furoate-eluting sinus implant (marketed elsewhere as Sinuva/Propel/Propel Contour) — used specifically to prevent polyp recurrence after endoscopic sinus surgery.

Frontal sinus polyps are not a distinct disease but an anatomic subtype of chronic rhinosinusitis with nasal polyps (CRSwNP), the same disease category in which mometasone furoate nasal spray/implants are already established. The rationale supplied with this prediction explicitly notes that the drug-eluting implant technology has been trialed with placement directly in the frontal sinus ostium (NCT04858802, "PROPEL Contour"), giving this candidate a direct product-level precedent rather than a purely inferential mechanistic argument.

The broader evidentiary context strengthens this: 16 clinical trials were retrieved for this indication, and while most involve different drugs (dupilumab, omalizumab, tezepelumab, benralizumab, itepekimab), they confirm CRSwNP/frontal sinus polyp disease is an active, well-studied Phase 3 therapeutic area with mature trial infrastructure and validated endpoints (Nasal Polyp Score, endoscopic scoring). This supports feasibility of further mometasone-specific study, even though most of the individual trials are class-level rather than drug-specific evidence.

---

## Clinical Trial Evidence

*(from predicted indication: Polyp of the Frontal Sinus, rank 4)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04858802](https://clinicaltrials.gov/study/NCT04858802) | NA (device) | Completed | 80 | **PROPEL Contour** mometasone-furoate-eluting sinus implant placed directly in the frontal sinus ostium after balloon dilation — the only trial in this set with a direct drug-and-anatomy match; single-arm device evaluation, not randomized. |
| [NCT03729310](https://clinicaltrials.gov/study/NCT03729310) | Early Phase 1 | Withdrawn (n=0) | 0 | Compared steroid-eluting implant (Propel, mometasone-based) vs. triamcinolone-soaked packing post-sinus surgery; withdrawn before enrollment, no usable data. |
| [NCT02912468](https://clinicaltrials.gov/study/NCT02912468) | Phase 3 | Completed | 276 | Dupilumab vs. placebo on a background of mometasone furoate nasal spray in bilateral nasal polyposis (includes frontal sinus disease); confirms mometasone as standard background therapy in this population. |
| [NCT02898454](https://clinicaltrials.gov/study/NCT02898454) | Phase 3 | Completed | 448 | Same design as above (dupilumab + mometasone background) in a larger cohort; mometasone furoate nasal spray again used as standard-of-care comparator arm. |
| [NCT04851964](https://clinicaltrials.gov/study/NCT04851964) | Phase 3 | Completed | 416 | Tezepelumab in severe CRSwNP (WAYPOINT trial); confirms disease severity spectrum relevant to frontal sinus involvement, different drug. |
| [NCT03401229](https://clinicaltrials.gov/study/NCT03401229) | Phase 3 | Completed | 413 | Benralizumab in severe nasal polyposis; same disease category, different drug class (anti-IL5). |
| [NCT06834347](https://clinicaltrials.gov/study/NCT06834347) | Phase 3 | Recruiting | 210 | Itepekimab as add-on to intranasal corticosteroids in CRSwNP; ongoing, background therapy consistent with mometasone class. |
| [NCT06834360](https://clinicaltrials.gov/study/NCT06834360) | Phase 3 | Recruiting | 210 | Parallel itepekimab Phase 3 study (identical design, different site cohort); same relevance as above. |
| [NCT05390255](https://clinicaltrials.gov/study/NCT05390255) | Phase 3 | Unknown | 87 | "Precise diagnosis and treatment system for refractory CRS"; omalizumab/oral glucocorticoid comparison, status unclear, drug not confirmed as mometasone. |
| [NCT05545072](https://clinicaltrials.gov/study/NCT05545072) | Phase 3 | Terminated (n=5) | 5 | Dupilumab post-surgery in allergic fungal rhinosinusitis on background intranasal corticosteroid; terminated early, minimal enrollment. |

---

## Literature Evidence

No literature was returned directly under "Polyp of the Frontal Sinus." However, the same evidence pack returned 8 relevant publications under a closely related (and likely mis-mapped) label, **"polyp of middle ear"** — the content of every one of these papers is actually about **sinonasal** polyps, not the middle ear, which the source rationale itself flags as a probable disease-ontology clustering error. Since these papers are the most direct mometasone-specific literature in the entire evidence pack, they are reported here for completeness, with that caveat:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29350840](https://pubmed.ncbi.nlm.nih.gov/29350840/) | 2018 | RCT | Int Forum Allergy Rhinol | Phase 3 trial of a mometasone furoate sinus implant (1350 mcg) for chronic sinusitis with recurrent nasal polyps — directly relevant drug and disease. |
| [27302143](https://pubmed.ncbi.nlm.nih.gov/27302143/) | 2016 | RCT | Am J Rhinol Allergy | Sodium hyaluronate added to topical corticosteroids in CRSwNP. |
| [27141307](https://pubmed.ncbi.nlm.nih.gov/27141307/) | 2016 | Review | Multidiscip Respir Med | Systematic review of mometasone furoate nasal spray across rhinosinusitis/nasal polyposis, explicitly including cases with middle-ear involvement (adenoidal hypertrophy with middle ear involvement) — likely source of the ontology overlap. |
| [19289710](https://pubmed.ncbi.nlm.nih.gov/19289710/) | 2009 | Cohort | Arch Otolaryngol Head Neck Surg | Mometasone furoate to prevent nasal polyp relapse after endoscopic sinus surgery. |
| [31117809](https://pubmed.ncbi.nlm.nih.gov/31117809/) | 2019 | Cohort (pooled analysis) | Am J Rhinol Allergy | In-office mometasone furoate sinus implants for recurrent nasal polyps, pooled analysis of 2 RCTs (400 adults). |
| [25256638](https://pubmed.ncbi.nlm.nih.gov/25256638/) | 2014 | Pharmacokinetic study | Int Forum Allergy Rhinol | Systemic safety/PK of a mometasone-furoate-releasing sinus implant. |
| [30645028](https://pubmed.ncbi.nlm.nih.gov/30645028/) | 2019 | Phase 1 | Int Forum Allergy Rhinol | Safety of a novel mometasone furoate delivery system (LYR-210) for chronic rhinosinusitis. |
| [33465455](https://pubmed.ncbi.nlm.nih.gov/33465455/) | 2021 | RCT (different drug: dupilumab) | Ann Allergy Asthma Immunol | Dupilumab in CRSwNP with comorbid asthma; background therapy context only. |

---

## Singapore Market Information

Mometasone furoate currently holds **no product registration in Singapore** (0 licenses on file; market status: Not Marketed). There is no local approved-indication text available to compare against the predicted new indication.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were returned for this product in the current evidence pack (this is logged as a **Blocking** data gap — DG001 — meaning formal safety review cannot proceed until label data is obtained from the manufacturer or a reference regulatory agency).

---

## Other Candidates Considered (Not Pursued)

Of the 10 TxGNN-predicted indications screened, 8 were screened out for lack of any supporting evidence, and one ("polyp of middle ear") is likely a disease-ontology mapping artifact rather than a distinct, novel signal:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Note |
|------|----------------------|-------------|-----------------|------|
| 1 | 2-hydroxyethyl methacrylate sensitization | 98.62% | L5 | No trials/literature; generic class-effect argument only |
| 2 | Polyp of vocal cord | 97.67% | L5 | No trials/literature |
| 3 | Polyp of middle ear | 97.65% | L3 | All retrieved evidence is actually about nasal/sinus polyps — likely ontology mismatch; do not treat as a distinct middle-ear indication without disease-label verification |
| 5 | Polyp of external auditory canal | 97.55% | L5 | No trials/literature; different pathophysiology (mechanical/cholesteatoma-related) |
| 6 | Fibroepithelial polyp | 97.55% | L5 | No trials/literature; not an inflammation-driven lesion |
| 7 | Polyp of vulva | 97.54% | L5 | No trials/literature |
| 8 | Polyp of ureter | 97.53% | L5 | No trials/literature; topical corticosteroid cannot reach this site |
| 9 | Epulis | 97.53% | L5 | No trials/literature; standard treatment is surgical, not steroid-based |
| 10 | Neoplastic polyp | 97.51% | L5 | No trials/literature; potential safety concern if it delays diagnosis of a neoplastic lesion |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The best-evidenced candidate (Polyp of the Frontal Sinus, L3) has genuine mechanistic and product-level plausibility — a mometasone-furoate-eluting implant already exists for this exact anatomic use elsewhere — but the supporting trial base is mostly indirect (other drugs, same disease class) and the drug itself has no Singapore registration and no available safety-label data in this evidence pack (Blocking gap DG001). Given the missing safety data, this cannot yet advance past a research/registration-feasibility question.

**To proceed, the following is needed:**
- Official mometasone furoate package insert / TFDA-equivalent label data (warnings, contraindications, DDI) to close the Blocking data gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank or a primary reference (DG002)
- Clarification of the "polyp of middle ear" vs. "polyp of frontal sinus" disease-ontology overlap before citing that literature set as supporting evidence
- If pursuing Singapore market entry: a regulatory pathway assessment, since the product currently holds zero local registrations
- A mometasone-furoate-specific trial or real-world evidence in frontal sinus/CRSwNP populations, since most current trial support comes from other drugs (dupilumab, tezepelumab, benralizumab, itepekimab) used only as active comparators alongside mometasone background therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

