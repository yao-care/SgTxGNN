---
layout: default
title: Solifenacin
parent: 僅模型預測 (L5)
nav_order: 916
evidence_level: L5
indication_count: 10
---

# Solifenacin
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

# Solifenacin: From Overactive Bladder to Low Compliance Bladder (Neurogenic Detrusor Overactivity)

## One-Sentence Summary

> Solifenacin is a selective M3 muscarinic receptor antagonist with established use in overactive bladder (OAB) and neurogenic detrusor overactivity.
> Across 10 TxGNN-predicted indications, the highest-scoring candidate (Polycystic Kidney Disease 3, 97.1%) shows **no mechanistic or clinical support** and is flagged for **Hold**.
> The most evidence-backed candidate is **Low Compliance Bladder**, supported by **2 clinical trials** and **10 relevant publications**, including RCTs and Phase 3 open-label data in neurogenic bladder populations.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in structured data (original_indications empty); literature confirms established clinical use in Overactive Bladder (OAB) / Neurogenic Detrusor Overactivity |
| Predicted New Indication | Low Compliance Bladder |
| TxGNN Prediction Score | 95.37% (rank 25,806) |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on the top TxGNN-ranked candidate:** Polycystic Kidney Disease 3 (score 97.1%) ranked highest by raw model score, but the accompanying evidence review found the 20 supporting publications are all background reviews on PKD/PLD pathophysiology, genetics, and transplantation — none involve solifenacin or anticholinergic therapy. This is assessed as a graph-embedding artifact from kidney–liver node proximity, not a genuine mechanistic signal, and is recommended **Hold**. This report therefore focuses on the highest-quality candidate, Low Compliance Bladder (rank 7), which is the only prediction reaching evidence level L2.

---

## Why is This Prediction Reasonable?

Currently, the structured `original_moa` field is a data gap. Based on the pharmacological information embedded in the evidence review, solifenacin is a **selective M3 muscarinic receptor antagonist** acting primarily on the detrusor muscle of the bladder, and is approved for overactive bladder and neurogenic detrusor overactivity.

Low compliance bladder is a urodynamic finding commonly seen in neurogenic bladder dysfunction, where detrusor overactivity and/or fibrosis cause abnormally elevated storage pressure. Because solifenacin already targets the same detrusor M3 receptor pathway responsible for both OAB and neurogenic detrusor overactivity, this predicted indication represents a **label-adjacent extension of an existing, validated mechanism** rather than a novel mechanistic hypothesis. Supporting this, one identified study specifically evaluated anticholinergic therapy in patients with low compliance bladder (<10 mL/cmH₂O) refractory to first-line treatment, and a separate Phase 3 open-label program demonstrated long-term efficacy and safety of solifenacin in neurogenic detrusor overactivity in patients aged 6 months–18 years.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04477265](https://clinicaltrials.gov/study/NCT04477265) | N/A | Completed | 140 | Compared pelvic floor muscle training with biofeedback vs. medication (including anticholinergics) in women with overactive bladder; medication arm relevant to solifenacin use in bladder storage disorders |
| [NCT04819360](https://clinicaltrials.gov/study/NCT04819360) | Phase 4 | Terminated | 1 | Compared botulinum toxin A vs. anticholinergic first-line therapy for neurogenic detrusor overactivity in multiple sclerosis; terminated early with insufficient enrollment to draw conclusions |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32007426](https://pubmed.ncbi.nlm.nih.gov/32007426/) | 2020 | Phase 3 Open-label | J Pediatr Urol | Long-term efficacy and safety of solifenacin in pediatric neurogenic detrusor overactivity (6 months–18 years), across two prospective Phase 3 studies |
| [25170796](https://pubmed.ncbi.nlm.nih.gov/25170796/) | 2014 | RCT | Urologia Internationalis | Combined low/standard-dose trospium and solifenacin effective for moderate OAB symptoms in elderly patients |
| [25435915](https://pubmed.ncbi.nlm.nih.gov/25435915/) | 2014 | RCT | Therapeutic Advances in Urology | Cyclic vs. continuous trospium + solifenacin combination improves compliance in severe OAB in elderly patients |
| [27928426](https://pubmed.ncbi.nlm.nih.gov/27928426/) | 2016 | RCT | Therapeutic Advances in Urology | Factors affecting treatment persistence with high-dose antimuscarinic therapy in working patients |
| [15716204](https://pubmed.ncbi.nlm.nih.gov/15716204/) | 2005 | Cohort | European Urology | Long-term open-label solifenacin associated with high treatment persistence in OAB over 1 year |
| [25503446](https://pubmed.ncbi.nlm.nih.gov/25503446/) | 2015 | Cohort | International Urology and Nephrology | Prospective study on dry mouth association with solifenacin treatment and its impact on efficacy |
| [38256949](https://pubmed.ncbi.nlm.nih.gov/38256949/) | 2024 | Real-world/Observational | Pharmaceuticals (Basel) | Analysis of adherence and reasons for discontinuation of solifenacin in urologist-managed OAB patients |
| [25656013](https://pubmed.ncbi.nlm.nih.gov/25656013/) | 2015 | Case Series | Hinyokika Kiyo | Videourodynamic evaluation of mirabegron add-on therapy in anticholinergic-resistant neurogenic bladder patients, including those with low compliance bladder (<10 mL/cmH₂O) |
| [16465186](https://pubmed.ncbi.nlm.nih.gov/16465186/) | 2006 | Review | British Journal of Pharmacology | Mechanistic review of muscarinic (M2/M3) receptors in bladder and their role in antimuscarinic OAB therapy |
| [17594185](https://pubmed.ncbi.nlm.nih.gov/17594185/) | 2007 | Review | Expert Opinion on Investigational Drugs | Review of OAB treatments in early-phase clinical development |

---

## Singapore Market Information

Solifenacin currently has **no marketing authorization records in Singapore** (0 registered licenses; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Low Compliance Bladder is a mechanistically coherent, label-adjacent extension of solifenacin's approved use in OAB and neurogenic detrusor overactivity, supported by RCT and Phase 3 open-label evidence (L2). By contrast, the model's top-ranked prediction (Polycystic Kidney Disease 3) and 7 of the remaining 8 candidates show no mechanistic plausibility and zero or purely background literature support, and are recommended **Hold**.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official package insert warnings/contraindications to complete the S1 safety assessment
- Resolve DG002 (High): confirm mechanism of action via DrugBank API query
- Clarify Singapore regulatory pathway, since the drug currently holds no local marketing authorization
- Seek a dedicated clinical trial or urodynamic study directly evaluating solifenacin in low compliance bladder, as current evidence is derived from adjacent neurogenic bladder populations rather than a low-compliance-bladder-specific trial
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

