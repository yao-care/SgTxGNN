---
layout: default
title: Fluticasone Propionate
parent: 僅模型預測 (L5)
nav_order: 443
evidence_level: L5
indication_count: 10
---

# Fluticasone Propionate
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

Using the report as specified — this evidence pack (`TW-DB00588-multi`) contains **10 ranked TxGNN predictions** for fluticasone propionate, but only one (`atopic dermatitis`, rank 7) has real supporting clinical trial/literature evidence and reached decision stage S3. I've built the report around that candidate rather than the raw rank-1 score (which has zero supporting evidence, L5/Hold), since that is the only signal in this pack that is actually actionable — I flag this scoping choice and summarize the other 9 candidates in the summary/conclusion so nothing is silently dropped.

---

# Fluticasone Propionate: From Allergic & Inflammatory Airway/Skin Disease to Atopic Dermatitis

## One-Sentence Summary

> Fluticasone propionate is a synthetic corticosteroid whose established uses span allergic rhinitis, asthma, and inflammatory dermatoses, delivered via nasal, inhaled, and topical formulations.
> Of the **10 candidate indications** screened by TxGNN for this drug, the only one with substantive supporting evidence is **Atopic Dermatitis**, backed by **11 clinical trials** and **19 publications** — however, this largely **reconfirms an already-established topical use** rather than representing a genuinely novel repurposing.
> One additional candidate, **Polyp of Middle Ear**, has partial supporting evidence (4 trials, 5 publications, all for the anatomically related condition of nasal polyps) and is flagged only as a research question; the remaining 8 candidates (e.g. alopecia areata, alopecia mucinosa, folliculitis decalvans) have TxGNN scores only, with no clinical or literature support (Evidence Level L4–L5).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Singapore registration data (drug is not marketed locally). Based on general pharmacological knowledge, fluticasone propionate's established uses are allergic rhinitis, asthma, and inflammatory skin conditions (topical/inhaled/intranasal corticosteroid). |
| Predicted New Indication | Atopic Dermatitis *(reconfirmation of an existing use — see caveat below)* |
| TxGNN Prediction Score | 95.32% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails *(contingent — see Blocking data gap below)* |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for this specific record is not available (DrugBank MOA field: Data Gap). Based on the supporting literature in this evidence pack, fluticasone propionate is a carbothioate-class topical/inhaled glucocorticoid with high glucocorticoid-receptor binding affinity, high lipophilicity, and rapid hepatic biotransformation — properties associated with a favourable local anti-inflammatory effect relative to systemic exposure (PMID 21977914, PMID 15608497). Its anti-inflammatory action works through suppression of Th2-driven cytokine pathways (IL-4/IL-13 axis) implicated in atopic dermatitis pathophysiology.

Atopic dermatitis is a chronic, relapsing inflammatory skin disease for which topical corticosteroids — including fluticasone propionate specifically (marketed as Cutivate) — are already a standard, guideline-recognized therapy. The TxGNN signal here is therefore best read as a **validation of a known pharmacological relationship** rather than a novel repurposing hypothesis: the mechanism-to-indication link is direct and well-established, and the "prediction" essentially recovers an already-approved use pattern of this molecule in other jurisdictions.

By contrast, the model's literal top-ranked candidates (e.g. "2-hydroxyethyl methacrylate sensitization," "vulvar inverted follicular keratosis," "telogen effluvium") carry no clinical or literature support in this pack, and several are noted in the underlying rationale as having pathophysiology (genetic, non-inflammatory, or structural) that does not plausibly respond to a corticosteroid's anti-inflammatory mechanism. These are appropriately scored L4–L5 and held.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00119158](https://clinicaltrials.gov/study/NCT00119158) | Phase 4 | Completed | 90 | Exploratory RCT of pimecrolimus + fluticasone (Cutivate) combination vs. vehicle in severe AD lesions. |
| [NCT01772056](https://clinicaltrials.gov/study/NCT01772056) | Phase 3 | Terminated | 54 | Double-blind RCT of twice-weekly fluticasone maintenance therapy to reduce relapse risk in children with mild-moderate AD. |
| [NCT00690105](https://clinicaltrials.gov/study/NCT00690105) | Phase 4 | Completed | 577 | Large multicentre RCT comparing tacrolimus 0.1% vs. fluticasone 0.005% ointment for facial ("red face") AD in adults. |
| [NCT00546000](https://clinicaltrials.gov/study/NCT00546000) | Phase 4 | Completed | 56 | Open-label study of fluticasone (Cutivate) lotion's effect on the HPA axis in paediatric AD patients. |
| [NCT01915914](https://clinicaltrials.gov/study/NCT01915914) | Phase 4 | Completed | 107 | Randomized comparative study of intermittent (twice-weekly) fluticasone dosing to reduce relapse risk in stabilized paediatric AD. |
| [NCT00689832](https://clinicaltrials.gov/study/NCT00689832) | Phase 4 | Completed | 487 | Large multicentre RCT comparing tacrolimus 0.03% vs. fluticasone 0.005% ointment in children ≥2 years with moderate-severe AD. |
| [NCT00616538](https://clinicaltrials.gov/study/NCT00616538) | Phase 4 | Completed | 121 | Pilot RCT comparing a non-steroidal barrier cream (Epiceram) vs. mid-strength fluticasone 0.05% as standard-of-care in paediatric AD. |
| [NCT03742414](https://clinicaltrials.gov/study/NCT03742414) | Phase 2 | Active, not recruiting | 398 | RCT testing proactive skin-barrier care plus fluticasone vs. reactive therapy to prevent AD progression and food allergy in infants. |
| [NCT04706559](https://clinicaltrials.gov/study/NCT04706559) | N/A | Completed | 98 | Probiotic supplementation trial in children with AD; fluticasone not the study drug (contextual relevance only). |
| [NCT03594565](https://clinicaltrials.gov/study/NCT03594565) | Early Phase 1 | Completed | 13 | Small case series of topical nasal steroids for skin reactions from continuous glucose monitors; limited relevance to classic AD. |

*Note: one additional trial (NCT00426283, swallowed fluticasone for eosinophilic esophagitis) was excluded as it targets a different route and organ system and appears to be a data-classification outlier.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29373242](https://pubmed.ncbi.nlm.nih.gov/29373242/) | 2018 | RCT | Allergologia et Immunopathologia | Intermittent fluticasone 0.05% cream reduces relapse risk vs. vehicle in children with stabilized AD. |
| [12207596](https://pubmed.ncbi.nlm.nih.gov/12207596/) | 2002 | Clinical Trial | British Journal of Dermatology | Intermittent dosing of fluticasone cream reduces relapse risk in AD patients; addresses long-term management gap. |
| [14522623](https://pubmed.ncbi.nlm.nih.gov/14522623/) | 2003 | RCT | Journal of Dermatological Treatment | Two multicentre, randomised, double-blind studies of fluticasone 0.05% cream for acute and maintenance AD treatment in children. |
| [11862174](https://pubmed.ncbi.nlm.nih.gov/11862174/) | 2002 | Clinical Safety Study | Journal of the American Academy of Dermatology | Establishes safety of fluticasone 0.05% cream in severe/extensive AD in children as young as 3 months. |
| [33150035](https://pubmed.ncbi.nlm.nih.gov/33150035/) | 2020 | Open-label Prospective | Dermatology Practical & Conceptual | Compares efficacy/safety of topical fluticasone vs. tacrolimus in proactive AD treatment. |
| [27543211](https://pubmed.ncbi.nlm.nih.gov/27543211/) | 2016 | Cohort Study | Journal of the American Academy of Dermatology | Evaluates cutaneous microbiome effects of fluticasone cream plus bleach baths in childhood AD. |
| [21977914](https://pubmed.ncbi.nlm.nih.gov/21977914/) | 2012 | Review | JEADV | Reviews fluticasone's high therapeutic index and its role as a standard intervention/maintenance option for AD. |
| [15608497](https://pubmed.ncbi.nlm.nih.gov/15608497/) | 2005 | Review | Skin Pharmacology and Physiology | Reviews fluticasone's pharmacology, receptor binding, and safety/efficacy across dermatological uses including AD. |
| [17225720](https://pubmed.ncbi.nlm.nih.gov/17225720/) | 2007 | Comparative Study | Annals of Allergy, Asthma & Immunology | Compares S. aureus colonization in AD treated with fluticasone vs. tacrolimus, with/without antibiotics. |
| [16394380](https://pubmed.ncbi.nlm.nih.gov/16394380/) | 2005 | Open-label Study | Indian J Dermatology, Venereology & Leprology | Evaluates fluticasone + mupirocin combination ointment for AD with suspected secondary bacterial infection. |

---

## Singapore Market Information

Fluticasone propionate currently has **no marketing authorization on record in Singapore** (0 registrations; market status: 未上市 / Not marketed). No product listing is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. *(Key warnings, contraindications, and drug-interaction data are all marked as data gaps in this evidence pack — DDI query returned no result.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(efficacy-only; execution is currently blocked — see below)*

**Rationale:**
- The atopic dermatitis signal is supported by 11 clinical trials (including multiple completed Phase 3/4 RCTs with large enrollment, e.g. n=577 and n=487) and 19 publications, meeting Evidence Level L1 and decision stage S3. However, it substantially reconfirms fluticasone propionate's already-established topical use rather than identifying a novel indication, so the practical "repurposing" value is limited.
- A **Blocking** data gap (DG001: TFDA/HSA label warnings and contraindications) means this candidate **cannot yet enter the S1 safety pre-assessment**, regardless of efficacy evidence strength. This must be resolved before any Go decision.
- Among the other 9 screened candidates, only "Polyp of Middle Ear" (L4, S1, Research Question) has partial supporting evidence — and that evidence is drawn from nasal polyp studies (different anatomical site), so it should be treated as a hypothesis-generating research question, not an evidence-backed candidate.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain HSA/product-label warnings, precautions, and contraindications for fluticasone propionate.
- Resolve DG002 (High): obtain a confirmed mechanism-of-action record from DrugBank to formally support the mechanistic rationale.
- Confirm whether local product registration is planned/expected, since Singapore market status is currently "not marketed" with 0 licenses.
- If pursuing the middle-ear polyp research question, commission a literature/trial search specific to middle-ear (not nasal) polyp pathology before elevating its evidence level.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

