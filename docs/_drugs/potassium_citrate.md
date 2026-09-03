---
layout: default
title: Potassium Citrate
parent: 僅模型預測 (L5)
nav_order: 804
evidence_level: L5
indication_count: 10
---

# Potassium Citrate
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

Using the Evidence Pack, I selected **nephrolithiasis** (predicted_indications rank 4) as the report's focal indication rather than the raw #1-by-score entry ("familial visceral myopathy"), because the top three TxGNN-scored predictions (ranks 1–3, plus 6, 8, 10) have **zero clinical trials, zero literature, evidence level L5, and are explicitly flagged in their own `repurposing_rationale` as likely false-positive knowledge-graph artifacts**. Nephrolithiasis is the only candidate with substantive clinical trial (35) and literature (19) support, an L2 evidence level, and a "Proceed with Guardrails" recommendation — this is the only prediction that meaningfully supports a repurposing decision. This substitution is noted explicitly in the report below for transparency.

---

# Potassium Citrate: Toward Nephrolithiasis (Kidney Stone Prevention)

## One-Sentence Summary

> Potassium citrate currently has no recorded original indication in this jurisdiction's regulatory data, as the drug is **not marketed** locally.
> Among the TxGNN model's predicted indications, **Nephrolithiasis** stands out as the only candidate backed by substantive real-world evidence,
> with **35 clinical trials** and **19 publications** identified, including a Phase 3 RCT (n=300) and a published systematic review/meta-analysis of potassium citrate for stone recurrence prevention.

*Note: Several other TxGNN predictions scored higher (e.g., familial visceral myopathy, mitochondrial disorder, Pendred syndrome) but had zero supporting trials or literature and were explicitly assessed in the evidence pack as low-confidence, possible false-positive knowledge-graph associations. This report focuses on nephrolithiasis as the only evidence-supported candidate.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is not currently marketed in this jurisdiction (regulatory data gap) |
| Predicted New Indication | Nephrolithiasis (kidney stone disease) |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data from DrugBank is currently unavailable (data gap). However, based on the pharmacological rationale documented alongside this prediction, potassium citrate acts through two well-characterized mechanisms relevant to kidney stone disease: it raises urinary citrate concentration, which chelates calcium ions and inhibits calcium oxalate/calcium phosphate crystal aggregation, and it alkalinizes the urine, which promotes dissolution of uric acid stones. Low urinary citrate (hypocitraturia) is itself a well-established, independent risk factor for calcium-containing kidney stones.

Because no original indication is recorded for this drug in the local regulatory dataset (it is not currently marketed here), a direct "original indication → new indication" comparison cannot be made from this Evidence Pack alone. That said, the supporting literature (e.g., the 1987 foundational paper by Pak CY, PMID 3306318) shows potassium citrate has long been used internationally for renal tubular acidosis-associated stones, hypocitraturic calcium oxalate nephrolithiasis, and uric acid lithiasis — indicating this is less a mechanistically novel repurposing signal and more a matter of confirming an already well-established therapeutic use that has not yet been formally registered in this market.

The mechanistic plausibility is reinforced by the breadth of ongoing and completed trials: studies testing potassium citrate directly against placebo/alternative agents (sodium bicarbonate, potassium phosphate, chlorthalidone combinations) for stone prevention, recurrence reduction, and urinary pH/citrate correction. This consistency across trial designs and multiple decades of literature supports the TxGNN association, distinguishing it clearly from the model's other high-scoring but evidence-free predictions for this drug.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00004284](https://clinicaltrials.gov/study/NCT00004284) | Phase 3 | Completed | 300 | Randomized double-blind comparison of potassium phosphate vs. potassium citrate for correcting absorptive hypercalciuria and preventing recurrent stone formation |
| [NCT06966635](https://clinicaltrials.gov/study/NCT06966635) | Phase 4 | Recruiting | 312 | Ongoing RCT comparing potassium citrate vs. sodium bicarbonate alkalization vs. control for lowering uric acid and reducing gout flares/urinary calculi |
| [NCT01217372](https://clinicaltrials.gov/study/NCT01217372) | Phase 2 | Completed | 203 | LIMONE study: randomized trial of citrate/lemon-juice supplementation to prevent recurrence in calcium oxalate nephrolithiasis |
| [NCT01329042](https://clinicaltrials.gov/study/NCT01329042) | Phase 4 | Completed | 80 | Evaluated preventive effect of potassium sodium citrate on stone recurrence/growth after shockwave lithotripsy or PCNL in calcium oxalate urolithiasis |
| [NCT05365477](https://clinicaltrials.gov/study/NCT05365477) | Phase 4 | Completed | 56 | Randomized comparison of empiric vs. metabolic-testing-guided diet plus pharmacologic (citrate-based) therapy in high-risk stone formers |
| [NCT07162974](https://clinicaltrials.gov/study/NCT07162974) | N/A | Completed | 49 | Prospective cohort assessing efficacy/safety of citrate-mixture litholytic therapy for coralloid uric acid nephrolithiasis |
| [NCT06819553](https://clinicaltrials.gov/study/NCT06819553) | Phase 2/3 | Active, not recruiting | 48 | RCT evaluating oral potassium citrate for reducing ureteral stent encrustation after ureteroscopy for uric acid stones |
| [NCT01754779](https://clinicaltrials.gov/study/NCT01754779) | Phase 2 | Completed | 13 | Examined whether citric acid or potassium citrate reduces calcium phosphate saturation in urine of calcium phosphate stone formers |
| [NCT03984409](https://clinicaltrials.gov/study/NCT03984409) | N/A | Completed | 22 | Compared dietary orange juice vs. standard potassium citrate for resolving hypocitraturia/aciduria in nephrolithiasis patients |
| [NCT01980004](https://clinicaltrials.gov/study/NCT01980004) | Phase 2 | Withdrawn | 0 | Planned comparison of potassium citrate + dietary education vs. education alone for calcium phosphate stone formers; withdrawn before enrollment, no efficacy data generated |

*25 additional trials were identified but are not shown here (up to 10 most relevant listed per reporting rules).*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27915395](https://pubmed.ncbi.nlm.nih.gov/27915395/) | 2017 | Systematic Review / Meta-analysis | Urolithiasis | Meta-analysis of trials showing potassium citrate supplementation reduces stone recurrence before/after shockwave lithotripsy |
| [40583613](https://pubmed.ncbi.nlm.nih.gov/40583613/) | 2025 | Guideline/Review (Tier 1) | Arch Ital Urol Androl | Expert consensus (ESD 2025) on management of urinary stones, including pharmacologic prevention with citrate therapy |
| [40978115](https://pubmed.ncbi.nlm.nih.gov/40978115/) | 2025 | Review (Tier 2) | Clinical Kidney Journal | Updated review of citrate biology, renal handling, and clinical use of potassium citrate for hypocitraturic calcium stone disease |
| [39206631](https://pubmed.ncbi.nlm.nih.gov/39206631/) | 2024 | Cohort/Pilot (Phase II) | Urologia | Phase II study: potassium citrate + magnesium + probiotics reduced crystalluria in stone formers |
| [38583757](https://pubmed.ncbi.nlm.nih.gov/38583757/) | 2024 | Cohort | Am J Kidney Diseases | Large cohort study quantifying associations between 24-hour urine chemistries (including citrate) and kidney stone risk |
| [30531474](https://pubmed.ncbi.nlm.nih.gov/30531474/) | 2019 | Review | Curr Opin Nephrol Hypertens | Review of citrate therapy specifically for calcium phosphate stone prevention; notes mixed efficacy of citrate-raising strategies |
| [3306318](https://pubmed.ncbi.nlm.nih.gov/3306318/) | 1987 | Foundational Review | Miner Electrolyte Metab | Seminal paper (Pak CY) establishing potassium citrate's role in RTA-associated stones, hypocitraturic calcium oxalate nephrolithiasis, and uric acid lithiasis |
| [33417997](https://pubmed.ncbi.nlm.nih.gov/33417997/) | 2021 | Preclinical | Kidney International | Animal model: chlorthalidone + potassium citrate combination reduced calcium oxalate stones and improved bone quality vs. either agent alone |
| [28762682](https://pubmed.ncbi.nlm.nih.gov/28762682/) | 2017 | Review | G Ital Nefrol | Review on clinical use of citrate salts in nephrolithiasis patients |
| [16443041](https://pubmed.ncbi.nlm.nih.gov/16443041/) | 2006 | Review | Lancet | General review of kidney stone pathophysiology and medical management, including citrate-based therapy |

*9 additional publications were identified but are not shown here (up to 10 most relevant listed per reporting rules).*

---

## Singapore Market Information

Potassium citrate currently has **no marketing authorization records** in this jurisdiction (market status: Not Marketed; 0 registrations). No product listing, dosage form, or approved indication text is available to report.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug-drug interaction data were found in the sources queried for this Evidence Pack (DDI database query status: not found). This absence of local safety data is flagged as a **Blocking** data gap (TFDA/HSA label warnings and contraindications) that must be resolved before any clinical or regulatory decision is finalized.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Nephrolithiasis is supported by a substantial and consistent evidence base — including a completed Phase 3 RCT (n=300) and a published systematic review/meta-analysis — that aligns with potassium citrate's established, decades-long clinical use for calcium and uric acid stone prevention. However, this drug is not currently marketed in this jurisdiction, has no local safety labeling on file, and formal mechanism-of-action data is missing, so guardrails are required before advancing further.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent package insert warnings and contraindications (Blocking data gap DG001)
- Confirmed DrugBank mechanism-of-action documentation (High-priority data gap DG002)
- A local regulatory pathway assessment, given zero current registrations in this jurisdiction
- A dedicated drug-drug interaction review, since the queried DDI database returned no results
- Clarification of which specific stone subtype(s) (calcium oxalate, calcium phosphate, uric acid) the intended indication would target, to align with product labeling

---

**Note on excluded predictions:** The remaining TxGNN-predicted indications for this drug (familial visceral myopathy, mitochondrial oxidative phosphorylation disorder, Pendred syndrome, hypermanganesemia with dystonia, autosomal recessive nonsyndromic deafness, leukocyte adhesion deficiency) had TxGNN scores in a similar range but **zero supporting clinical trials or literature** and evidence level L5. Their own repurposing rationales describe them as likely artifacts of gene-family or knowledge-graph structural similarity rather than genuine pharmacological connections, and are recommended **Hold**. Two additional predictions — cystinosis and exocrine pancreatic insufficiency — had limited case-report-level evidence (L4, "Research Question" stage) for treating secondary complications (Fanconi syndrome, oxalate nephropathy) rather than the diseases themselves, and may warrant future monitoring but do not currently support a repurposing decision.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

