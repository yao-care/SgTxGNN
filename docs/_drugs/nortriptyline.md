---
layout: default
title: Nortriptyline
parent: 僅模型預測 (L5)
nav_order: 717
evidence_level: L5
indication_count: 10
---

# Nortriptyline
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

Using the drug-repurposing report prompt directly (no additional skill applies — this is straight report generation from a supplied Evidence Pack).

Note: `predicted_indications[0]` = ADHD (rank 1, highest score + best evidence level), so the report is built around that indication per the extraction rules.

---

# Nortriptyline: From Depression to Attention-Deficit/Hyperactivity Disorder (ADHD)

## One-Sentence Summary

Nortriptyline is a tricyclic antidepressant (TCA); structured original-indication and MOA fields are not populated in this evidence pack, but literature in this pack consistently identifies it as a norepinephrine-reuptake-inhibiting antidepressant used for major depression. The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**, with **1 controlled clinical trial**, **1 Cochrane systematic review**, and **20 supporting publications** currently identified — but the drug is **not marketed in Singapore** and a blocking safety-label data gap remains.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in structured registry data; literature in this pack identifies Nortriptyline as a TCA used for depression |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in DrugBank fields (`original_moa: [Data Gap]`). Based on known information from the accompanying literature and repurposing rationale, Nortriptyline is a secondary-amine tricyclic antidepressant whose principal activity is norepinephrine (NE) reuptake inhibition, with comparatively weak serotonergic activity. This noradrenergic profile overlaps mechanistically with atomoxetine, an already-approved non-stimulant ADHD medication, which supports the biological plausibility of the TxGNN prediction.

Depression and ADHD are distinct diagnoses, but both have long-documented links to noradrenergic/dopaminergic circuit dysregulation affecting attention, arousal, and impulse control. Clinically, TCAs such as nortriptyline and desipramine have decades of off-label use as second-line, non-stimulant options for ADHD — particularly in patients where stimulants are undesirable, such as those with comorbid tic disorders or Tourette syndrome (stimulants can exacerbate tics).

The main caveat is that this class carries a narrower therapeutic index and cardiovascular toxicity risk than modern non-stimulants, which historically limited adoption despite mechanistic plausibility and positive early trial data — this tension is reflected directly in the literature evidence below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25238582](https://pubmed.ncbi.nlm.nih.gov/25238582/) | 2014 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Reviews TCAs, including nortriptyline, as second-line treatment for ADHD symptom reduction in children/adolescents |
| [11052409](https://pubmed.ncbi.nlm.nih.gov/11052409/) | 2000 | RCT | J Child Adolesc Psychopharmacol | Controlled study of nortriptyline efficacy and tolerability in pediatric ADHD |
| [22700161](https://pubmed.ncbi.nlm.nih.gov/22700161/) | 2012 | RCT | Pediatric Nephrology | Randomized double-blind trial of nortriptyline for enuresis in children with ADHD |
| [8428873](https://pubmed.ncbi.nlm.nih.gov/8428873/) | 1993 | Cohort/Open-label | J Am Acad Child Adolesc Psychiatry | Nortriptyline used for ADHD in children with comorbid tic disorder or Tourette's syndrome |
| [15064003](https://pubmed.ncbi.nlm.nih.gov/15064003/) | 2004 | Review | Psychiatric Clinics of North America | Reviews nonstimulant ADHD treatments; notes nortriptyline's noradrenergic activity but flags narrow therapeutic index and cardiovascular toxicity as limiting factors |
| [15794722](https://pubmed.ncbi.nlm.nih.gov/15794722/) | 2005 | Review | Expert Opinion on Drug Safety | Safety review of non-stimulant ADHD agents, including tricyclic antidepressants |
| [17915180](https://pubmed.ncbi.nlm.nih.gov/17915180/) | 2007 | Review | Neuropsychiatrie | Pharmacotherapy algorithms for ADHD and comorbid disorders, including TCA options |
| [22303520](https://pubmed.ncbi.nlm.nih.gov/22303520/) | 2012 | Guideline/Review | Annals of Clinical Psychiatry | CANMAT task force recommendations for managing mood disorders with comorbid ADHD |
| [4075308](https://pubmed.ncbi.nlm.nih.gov/4075308/) | 1985 | Case series | Clinical Neuropharmacology | Early case series reporting nortriptyline use in attention deficit disorder |
| [8428875](https://pubmed.ncbi.nlm.nih.gov/8428875/) | 1993 | Case series | J Am Acad Child Adolesc Psychiatry | Comparator safety signal: bupropion (not nortriptyline) exacerbates tics in ADHD+Tourette patients, relevant context for positioning TCAs as an alternative |

---

## Singapore Market Information

Nortriptyline currently holds no marketing authorization in Singapore in this evidence pack — market status is **未上市 (Not Marketed)** with **0 registered licenses**. No product/dosage-form data is available to tabulate.

---

## Safety Considerations

Structured safety fields (key warnings, contraindications, DDI) are all marked as data gaps or "not found" in this evidence pack (DG001, severity: Blocking — impact: cannot proceed to S1 safety pre-screening). Please refer to the package insert for safety information.

**Literature-derived signal (not from structured fields):** Multiple publications in this pack (e.g., PMID 15064003, PMID 8444754) flag TCA-class cardiovascular toxicity and a narrow therapeutic index, including ECG effects reported specifically in pediatric nortriptyline use — this should be treated as a priority item once formal safety data is obtained, not as a substitute for it.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap on TFDA/HSA-equivalent label warnings and contraindications (DG001) prevents even a first-pass safety screen (S1), and the drug is not currently marketed in Singapore (0 registrations). While the evidence base for ADHD (1 RCT + 1 Cochrane systematic review, evidence level L2, current pipeline stage "Research Question") is more substantive than typical model-only predictions, TCA-class cardiotoxicity concerns mean this cannot advance past Hold without full safety data.

**To proceed, the following is needed:**
- Local safety/label data: TFDA/HSA package insert warnings and contraindications (DG001, blocking)
- Confirmed mechanism of action data from DrugBank (DG002)
- Independent replication of the single pediatric ADHD RCT (PMID 11052409), given its limited size
- A cardiac safety monitoring plan (baseline/serial ECG) given documented TCA cardiotoxicity risk in children
- A formal drug-drug interaction screen (current DDI query returned "not_found")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

