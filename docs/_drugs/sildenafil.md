---
layout: default
title: Sildenafil
parent: 僅模型預測 (L5)
nav_order: 902
evidence_level: L5
indication_count: 10
---

# Sildenafil
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

# Sildenafil: From PDE5 Inhibition to Genetic Alopecia (Hair Growth)

## One-Sentence Summary

> Sildenafil is a phosphodiesterase type 5 (PDE5) inhibitor; no approved indication is on record for this drug in the Singapore evidence pack, and it is not currently marketed here.
> Of **10 TxGNN-predicted indications**, only **genetic alopecia / hair growth** is supported by real evidence — **2 clinical trials** and **1 mechanistic publication**.
> The other 9 candidates (including the highest-scoring one) have **zero supporting trials or literature** and are flagged in the evidence pack itself as likely knowledge-graph artifacts.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record — no approved indication text found in Singapore regulatory data (drug not marketed) |
| Predicted New Indication | Genetic Alopecia (hair growth / androgenetic alopecia & alopecia areata) |
| TxGNN Prediction Score | 75.03% (rank 9 of 10 candidates; not the top-scoring prediction) |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available for Sildenafil in this evidence pack (DG002). Based on the evidence that is available, Sildenafil is a **PDE5 inhibitor** that increases intracellular cyclic GMP (cGMP), producing vasodilation. No original approved indication is recorded in the Singapore dataset, and the drug is not currently marketed here — so a direct "original indication → new indication" mechanistic bridge cannot be drawn from local regulatory data.

The genetic-alopecia hypothesis rests instead on general PDE5 pharmacology: cGMP-mediated vasodilation could theoretically increase perifollicular blood flow, a mechanism analogous to Minoxidil (another vasodilator already established for hair loss). This is not speculation — it is directly supported by a mechanistic study (PMID 30292404) showing Sildenafil affects human hair follicles in vitro, and the hypothesis has already progressed into early human trials (an Early Phase 1 RCT of a topical lipid-nanocarrier formulation, and a head-to-head trial vs. Minoxidil 5%).

It is important to note that **genetic alopecia was not TxGNN's top-ranked prediction**. The highest-scoring candidate (Ambras type hypertrichosis, 98.4%) and 7 other candidates have **no clinical trials, no literature, and no plausible mechanistic link** to PDE5 inhibition — the evidence pack itself characterizes these as probable knowledge-graph artifacts from disease-ontology similarity rather than genuine pharmacological signals. Genetic alopecia is therefore the only candidate in this set that merits further evaluation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06527729](https://clinicaltrials.gov/study/NCT06527729) | Early Phase 1 | Completed | 28 | Randomized study of Sildenafil-loaded lipid-based nanocarrier as a potential topical therapy for alopecia areata |
| [NCT05369481](https://clinicaltrials.gov/study/NCT05369481) | N/A | Unknown | 50 | Comparative trial of topical Sildenafil 2% vs. topical Minoxidil 5% for male androgenetic alopecia; status not updated since 2022 |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30292404](https://pubmed.ncbi.nlm.nih.gov/30292404/) | 2018 | Preclinical/Mechanistic | Biochem Biophys Res Commun | First report that Sildenafil, via cGMP-mediated vasodilation, has a direct effect on human hair follicles |

---

## Singapore Market Information

Sildenafil is currently **not marketed in Singapore** according to this evidence pack — no license records are available (total registrations: 0).

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not available in this evidence pack (flagged as a Blocking data gap, DG001).

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
Evidence for genetic alopecia is mechanistically plausible and has moved into early human testing, but is limited to one small completed Early Phase 1 trial (n=28) and one trial of unknown/stalled status (n=50) — no Phase 2/3 RCT data exists. Combined with the absence of local safety labeling data and the drug's current non-marketed status in Singapore, this does not yet meet the bar for a "Go" or "Proceed with Guardrails" decision. The other 9 TxGNN candidates lack any supporting evidence and should not be pursued.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent product label (warnings, contraindications) — currently blocking (DG001)
- Detailed DrugBank MOA data to formally support the mechanistic rationale (DG002)
- Published/completed results from NCT06527729 and a status update on NCT05369481
- If the signal holds, design of a Phase 2 RCT specifically for topical Sildenafil in alopecia
- Regulatory pathway assessment for Singapore market entry, given the drug is not currently registered here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

