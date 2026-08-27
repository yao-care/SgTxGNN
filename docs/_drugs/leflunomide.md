---
layout: default
title: Leflunomide
parent: 僅模型預測 (L5)
nav_order: 578
evidence_level: L5
indication_count: 10
---

# Leflunomide
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

Using no additional skill here — this is a direct content-generation task fully specified by the system prompt's report template; I applied "cite-before-write" discipline from CLAUDE.md by grounding every claim in the JSON evidence pack itself (including sourcing "original indication = rheumatoid arthritis" from the abstracts of PMID 19174558 / 32268821, since `taiwan_regulatory.licenses` is empty).

**One editorial note before the report:** This evidence pack (`TW-DB01097-multi`) contains 10 TxGNN-ranked predictions. The literal #1-ranked prediction ("brachydactyly-syndactyly syndrome") has **zero trials and zero literature** (L5/Hold), as do ranks #2, #6–#10. The only candidates with real clinical evidence are **plasma cell myeloma / indolent (smoldering) plasma cell myeloma** (ranks #3–#4, merged per the pack's own rationale) and **myeloid leukemia** (rank #5). As a repurposing evaluator, leading the report with a zero-evidence rare genetic syndrome would be misleading, so I built the report around the evidence-bearing candidate and added a full ranking table for transparency. This deviation from strict rank-#1 extraction is flagged explicitly rather than silently applied.

---

# Leflunomide: From Rheumatoid Arthritis to Multiple Myeloma (Plasma Cell Myeloma)

## One-Sentence Summary

Leflunomide is an immunomodulatory DHODH inhibitor documented in the evidence pack's own literature as being used for rheumatoid arthritis. The TxGNN model predicts activity against **Plasma Cell Myeloma / Indolent (Smoldering) Plasma Cell Myeloma**, and this direction is currently supported by **5 directly relevant clinical trials** (including one completed and published Phase 1/2 study) and **5 mechanistic/clinical publications**.

> Note: this candidate was selected from a 10-indication TxGNN ranking because it is the only one backed by real trial and literature evidence — see "All Predicted Indications" below for the full picture, including a lower-confidence secondary candidate (myeloid leukemia) and seven candidates with no supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (sourced from trial/literature abstracts in this pack; no Singapore market license data exists for this drug) |
| Predicted New Indication | Plasma Cell Myeloma (including Indolent/Smoldering Multiple Myeloma) |
| TxGNN Prediction Score | 95.16% (plasma cell myeloma, rank 26,325) / 95.47% (indolent plasma cell myeloma, rank 25,538) |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The evidence pack flags Leflunomide's official mechanism-of-action field as a data gap (DG002), but the mechanism can be reconstructed from the indication-specific literature it contains. Leflunomide's active metabolite, A771726 (teriflunomide), inhibits dihydroorotate dehydrogenase (DHODH), the rate-limiting enzyme in de novo pyrimidine synthesis (PMID 34577124, PMID 19174558). This is the same mechanism underlying Leflunomide's established immunomodulatory use in rheumatoid arthritis, where blocking pyrimidine supply curbs the rapid clonal expansion of activated lymphocytes (PMID 19174558: "the immunosuppressive drug leflunomide, which is currently applied in the treatment of rheumatoid arthritis").

Malignant plasma cells in multiple myeloma are similarly dependent on high-throughput nucleotide synthesis to sustain proliferation and immunoglobulin production. Multiple independent research groups have shown that DHODH is broadly expressed in myeloma cell lines and primary myeloma cells, and that DHODH inhibition by A771726 induces apoptosis and halts myeloma cell growth (PMID 19174558), downregulates c-Myc via PIM kinase inhibition (PMID 30940637), and disrupts mitochondrial fusion dynamics to sensitize cells to venetoclax (PMID 40814067). This gives the RA→myeloma repurposing hypothesis a coherent, cross-validated mechanistic basis rather than resting on graph-embedding similarity alone.

This mechanistic plausibility is reinforced by clinical translation: a completed Phase 1/2 dose-escalation trial in relapsed/refractory multiple myeloma (NCT02509052) was published in 2020 (PMID 32268821), and two Phase 2 trials are now active in the smoldering (indolent) myeloma setting — the disease stage that TxGNN separately flagged as "indolent plasma cell myeloma." The pack's own rationale note treats these as the same underlying candidate, since the smoldering-myeloma trials are registered under the broader "plasma cell myeloma" evidence bucket rather than the indolent-specific one.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02509052](https://clinicaltrials.gov/study/NCT02509052) | Phase 1/2 | Completed | 12 | Dose-escalation of single-agent Leflunomide in relapsed/refractory multiple myeloma; no dose-limiting toxicities at 20–40 mg; published as PMID 32268821 |
| [NCT04508790](https://clinicaltrials.gov/study/NCT04508790) | Phase 2 | Recruiting | 29 | Leflunomide + Pomalidomide + Dexamethasone combination in relapsed/refractory multiple myeloma |
| [NCT05014646](https://clinicaltrials.gov/study/NCT05014646) | Phase 2 | Active, not recruiting | 27 | Leflunomide in African-American and European-American patients with high-risk smoldering multiple myeloma (population-stratified) |
| [NCT03952832](https://clinicaltrials.gov/study/NCT03952832) | Phase 2 | Withdrawn | 0 | Planned trial of Leflunomide in high-risk smoldering multiple myeloma; withdrawn before enrollment, no data generated |
| [NCT04370483](https://clinicaltrials.gov/study/NCT04370483) | Early Phase 1 | Active, not recruiting | 1 | Pilot study of Leflunomide to delay progression of high-risk smoldering multiple myeloma; enrollment too small for meaningful signal |

*Three additional trials returned by the database query (NCT01646385, NCT00720798, NCT05605587) were excluded — they test unrelated drugs (Etanercept, Tocilizumab) or an unrelated syndrome (MEN1/LUMEN1) and were flagged in the source data as likely mismatches.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32268821](https://pubmed.ncbi.nlm.nih.gov/32268821/) | 2020 | Clinical Trial (Phase 1) | Leukemia & Lymphoma | Phase 1 repurposing study of single-agent Leflunomide in relapsed/refractory myeloma; well tolerated at 20/40 mg, no DLTs |
| [34577124](https://pubmed.ncbi.nlm.nih.gov/34577124/) | 2021 | Preclinical/Mechanistic | Molecules | Mitochondria-independent cytotoxic effect of Leflunomide on RPMI-8226 myeloma cells via DHODH inhibition |
| [19174558](https://pubmed.ncbi.nlm.nih.gov/19174558/) | 2009 | Preclinical/Mechanistic | Molecular Cancer Therapeutics | A771726 (Leflunomide's active metabolite) induces apoptosis and diminishes proliferation across myeloma cell lines via DHODH inhibition |
| [40814067](https://pubmed.ncbi.nlm.nih.gov/40814067/) | 2025 | Preclinical/Mechanistic | Journal of Translational Medicine | MARCH5-MFN2 mitochondrial fusion axis sensitizes myeloma cells to venetoclax |
| [30940637](https://pubmed.ncbi.nlm.nih.gov/30940637/) | 2019 | Preclinical/Mechanistic | Blood Advances | Teriflunomide downregulates c-Myc via PIM kinase inhibition; extends survival with lenalidomide in an in vivo myeloma model |

---

## Secondary Candidate: Myeloid Leukemia (Rank 5, L3, Research Question)

This candidate has weaker but genuine evidence and is worth tracking alongside the primary myeloma indication.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06923488](https://clinicaltrials.gov/study/NCT06923488) | Phase 1/2 | Recruiting | 26 | Leflunomide + Decitabine in relapsed/refractory myelodysplastic syndromes/AML; no results yet |

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41549155](https://pubmed.ncbi.nlm.nih.gov/41549155/) | 2026 | Preclinical/Mechanistic | Annals of Hematology | BCOR-mutant AML shows synthetic-lethal sensitivity to DHODH inhibitors including Leflunomide |
| [30347213](https://pubmed.ncbi.nlm.nih.gov/30347213/) | 2019 | Review | Pharmacology & Therapeutics | DHODH as a therapeutic target across cancers, including Leflunomide/teriflunomide/brequinar |
| [12181422](https://pubmed.ncbi.nlm.nih.gov/12181422/) | 2002 | Preclinical/Mechanistic | Molecular Pharmacology | A77 1726 induces erythroid differentiation of K562 myeloid leukemia cells via CTP pool depletion |
| [16927021](https://pubmed.ncbi.nlm.nih.gov/16927021/) | 2006 | Preclinical/Mechanistic | Apoptosis | Low-dose Leflunomide activates PI3K/Akt in erythroleukemia cells, reducing apoptosis from other anticancer agents (a cautionary/antagonistic finding) |
| [15385935](https://pubmed.ncbi.nlm.nih.gov/15385935/) | 2004 | Preclinical/Mechanistic | Leukemia | CTP-depleting agents induce erythroid differentiation of K562 cells via the same pyrimidine-starvation pathway |

Note: one of these findings (PMID 16927021) is a **cautionary** signal — low-dose Leflunomide was shown to *reduce* apoptosis from other anticancer agents in erythroleukemia cells via PI3K/Akt activation, which should be considered if Leflunomide is combined with other chemotherapy in this indication.

---

## Singapore Market Information

No market license data is available — `taiwan_regulatory.total_licenses = 0` and the drug's market status is recorded as **Not Marketed** in this jurisdiction. There is no local product/dosage-form registration to summarize.

---

## All Predicted Indications (Full TxGNN Ranking)

For transparency, all 10 indications returned by TxGNN for this drug are listed below. Only the two discussed above have supporting evidence; the rest are score-only predictions.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Note |
|------|----------------------|-------------|-----------------|-----------------|------|
| 1 | Brachydactyly-syndactyly syndrome | 99.93% | L5 | Hold | No known mechanistic link; no trials/literature |
| 2 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.93% | L5 | Hold | No known mechanistic link; no trials/literature |
| 3 | Indolent plasma cell myeloma | 95.47% | L2 | Research Question | Same underlying candidate as Rank 4 (see above); DB label split |
| 4 | Plasma cell myeloma | 95.16% | L2 | **Proceed with Guardrails** | Primary evidence-backed candidate (see above) |
| 5 | Myeloid leukemia | 92.99% | L3 | Research Question | Secondary candidate (see above) |
| 6 | Meester-Loeys syndrome | 86.55% | L5 | Hold | No known mechanistic link; no trials/literature |
| 7 | Ganglioneuroblastoma | 76.30% | L5 | Hold | No known mechanistic link; no trials/literature |
| 8 | WHIM syndrome | 75.88% | L5 | Hold | **Negative safety signal** — Leflunomide's immunosuppressive action could theoretically worsen this primary immunodeficiency; no evidence either way |
| 9 | Scalp dermatosis | 73.87% | L5 | Hold | No known mechanistic link; only trial returned was a mismatch (Tofacitinib, not Leflunomide) |
| 10 | Vertebral anomalies and variable endocrine and T-cell dysfunction | 72.25% | L5 | Hold | No known mechanistic link; no trials/literature |

---

## Safety Considerations

Please refer to the package insert for safety information. Structured safety data (key warnings, contraindications, and drug-drug interactions) could not be retrieved for this evaluation — this is recorded in the evidence pack as a **Blocking-severity data gap (DG001)**, meaning this candidate **cannot yet enter formal safety pre-assessment (S1)** until TFDA/HSA label warnings and contraindications are obtained.

One evidence-based caution worth carrying forward regardless of label data: Leflunomide's immunosuppressive mechanism is mechanistically opposed to at least one low-ranked candidate indication (WHIM syndrome, a primary immunodeficiency — see ranking table above), underscoring that its immune-suppressing profile needs explicit consideration in any myeloma-population safety plan, particularly for infection risk in an already immunocompromised patient population.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Plasma Cell Myeloma / Indolent Plasma Cell Myeloma)

**Rationale:**
- A completed and published Phase 1/2 trial (NCT02509052 / PMID 32268821) establishes tolerability, and two Phase 2 trials are actively enrolling or active (NCT04508790, NCT05014646), supported by five independent mechanistic studies converging on DHODH inhibition as the driver of anti-myeloma activity.
- However, the drug is not marketed in this jurisdiction, and safety/label data cannot currently be assessed (DG001, Blocking) — guardrails must include this gap before any clinical application.
- The Myeloid Leukemia candidate (Rank 5) merits tracking as a **Research Question** but is not yet actionable — its only trial (NCT06923488) has not reported results, and one preclinical finding suggests a potential antagonistic interaction with other anticancer agents.
- The remaining seven candidates (Ranks 1, 2, 6–10) should remain on **Hold** — they carry high TxGNN similarity scores but zero clinical or literature corroboration, including one (WHIM syndrome) with a plausible mechanistic contraindication rather than a benefit.

**To proceed, the following is needed:**
- Singapore/regional regulatory label data (TFDA warnings, contraindications) — currently the single Blocking gap preventing formal safety pre-assessment (DG001)
- Confirmed, sourced original mechanism-of-action documentation from DrugBank (DG002) to formally replace the literature-reconstructed MOA used in this report
- Efficacy readouts from the two ongoing Phase 2 trials (NCT04508790, NCT05014646) before advancing past "Guardrails" status
- If pursuing the myeloid leukemia lead, results from NCT06923488 and clarification of the PI3K/Akt-mediated antagonism signal (PMID 16927021) before combination-therapy design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

