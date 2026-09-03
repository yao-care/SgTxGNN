---
layout: default
title: Spironolactone
parent: 僅模型預測 (L5)
nav_order: 925
evidence_level: L5
indication_count: 10
---

# Spironolactone
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

# Spironolactone: From Hypertension/Oedema to Alopecia (Androgenetic Hair Loss)

## One-Sentence Summary

Spironolactone is a mineralocorticoid receptor antagonist traditionally used for hypertension, oedema, and heart failure. The TxGNN model predicts it may be effective for **Alopecia**, with **2 clinical trials** and **20 publications** — including multiple systematic reviews and a comparative RCT — currently supporting this off-label dermatological use.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in Singapore (HSA) registration data — drug currently not marketed locally; internationally established for hypertension, oedema, and heart failure |
| Predicted New Indication | Alopecia (Androgenetic Alopecia / Female Pattern Hair Loss) |
| TxGNN Prediction Score | 97.83% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap, DrugBank query pending). Based on generally established pharmacology, spironolactone is a synthetic aldosterone-receptor antagonist that also exhibits anti-androgenic activity — it blocks androgen receptors and lowers circulating testosterone/DHT. Its efficacy in hypertension, oedema, and heart failure relies on the aldosterone-antagonist arm of this dual mechanism.

Androgenetic alopecia (AGA), particularly in women, is a hormonally driven condition in which excessive follicular sensitivity to androgens converts terminal scalp hair to fine vellus hair. This is mechanistically distinct from the drug's cardiovascular indications, but is directly addressed by spironolactone's *anti-androgenic* arm rather than its aldosterone-antagonist arm — making the TxGNN prediction mechanistically coherent rather than a graph-similarity artifact.

This is reinforced by real-world practice: spironolactone is already widely used off-label by dermatologists for AGA and hirsutism, and a completed Phase 2 RCT directly compared it against topical minoxidil in female pattern hair loss. Multiple systematic reviews (2022–2024) independently confirm this established off-label use, giving the prediction substantially stronger support than a pure model-score inference.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00175617](https://clinicaltrials.gov/study/NCT00175617) | Phase 2 | Completed | 40 | Direct comparison of oral spironolactone (anti-androgen) vs. topical minoxidil in female pattern hair loss |
| [NCT02483195](https://clinicaltrials.gov/study/NCT02483195) | Phase 4 | Withdrawn (enrollment 0) | 0 | Planned head-to-head of finasteride vs. spironolactone+minoxidil in postmenopausal AGA; no data generated |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36923692](https://pubmed.ncbi.nlm.nih.gov/36923692/) | 2023 | Systematic Review | Clin Cosmet Investig Dermatol | Oral and topical spironolactone widely used off-label to stimulate hair growth in AGA |
| [34352345](https://pubmed.ncbi.nlm.nih.gov/34352345/) | 2022 | Systematic Review | J Am Acad Dermatol | Confirms efficacy and safety profile of oral spironolactone for androgenic alopecia |
| [37650533](https://pubmed.ncbi.nlm.nih.gov/37650533/) | 2024 | Blinded RCT | J Cosmet Dermatol | Topical minoxidil + oral spironolactone shows comparable efficacy to minoxidil + finasteride in women with AGA |
| [38852607](https://pubmed.ncbi.nlm.nih.gov/38852607/) | 2024 | Systematic Review (PRISMA) | J Cosmet Laser Ther | 141-study review; spironolactone identified among effective prescription options for AGA |
| [36039391](https://pubmed.ncbi.nlm.nih.gov/36039391/) | 2022 | Comparative Study | J Cosmet Dermatol | Dermoscopy shows combined topical spironolactone 5% + minoxidil 5% outperforms monotherapy in AGA |
| [39133327](https://pubmed.ncbi.nlm.nih.gov/39133327/) | 2024 | Retrospective Cohort | Arch Dermatol Res | Spironolactone reduces minoxidil-induced hypertrichosis in alopecia combination therapy |
| [27225981](https://pubmed.ncbi.nlm.nih.gov/27225981/) | 2016 | Cochrane Systematic Review | Cochrane Database Syst Rev | Reviews interventions for female pattern hair loss, including anti-androgens such as spironolactone |
| [35038224](https://pubmed.ncbi.nlm.nih.gov/35038224/) | 2022 | Review | Dermatol Ther | Reviews spironolactone's anti-androgenic dermatological applications, including AGA |
| [37284568](https://pubmed.ncbi.nlm.nih.gov/37284568/) | 2023 | Review | Clin Cosmet Investig Dermatol | Current treatment guidance for AGA lists spironolactone among evidence-based options |
| [38540126](https://pubmed.ncbi.nlm.nih.gov/38540126/) | 2024 | Review | Biomedicines | Reviews hormonal (androgen) basis of non-scarring alopecias and treatment options |

---

## Singapore Market Information

Currently not marketed in Singapore — no HSA registration records are available for this candidate (0 registrations found in the Evidence Pack).

---

## Safety Considerations

Please refer to the package insert for safety information. Detailed TFDA/HSA-approved warnings, contraindications, and drug-drug interaction data were not available at the time of this report (flagged as a **Blocking** data gap — DG001).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is backed by L2 evidence — a completed Phase 2 RCT plus multiple independent systematic reviews (2022–2024) — and aligns with spironolactone's already-established off-label dermatological use for androgenetic alopecia. However, the drug is not currently registered in Singapore, and formal safety labelling data is missing, so it cannot yet proceed without guardrails.

**To proceed, the following is needed:**
- Official package insert / HSA-approved warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action from DrugBank (DG002, High)
- HSA registration or import pathway assessment, given current "Not Marketed" status
- A monitoring plan for hyperkalaemia and renal function, given spironolactone's mineralocorticoid receptor antagonist class effects, especially if co-prescribed with other RAAS-active agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

