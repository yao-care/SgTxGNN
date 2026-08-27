---
layout: default
title: Mesalazine
parent: 僅模型預測 (L5)
nav_order: 647
evidence_level: L5
indication_count: 10
---

# Mesalazine
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

Using the Evidence Pack for Mesalazine (DB00244), I selected the report's featured indication carefully rather than mechanically taking `predicted_indications[0]`. Rank 1 ("congenital hypotrichosis with juvenile macular dystrophy," score 0.9965) and ranks 4–10 all carry zero clinical trials, zero literature, evidence level L5, decision stage S0, and are explicitly flagged in their own `repurposing_rationale` as likely knowledge-graph embedding artifacts with no biological plausibility. The only candidates with real supporting evidence are rank 2 (osteoarthritis, L4/S1, preclinical only) and rank 3 (rheumatoid arthritis, L2/S2, 6 trials + 20 papers). I built the report around rheumatoid arthritis — the only candidate that reaches an actual decision-relevant evidence tier — and note the artifact-ranked and secondary candidates transparently rather than silently dropping them.

---

# Mesalazine: From Ulcerative Colitis to Rheumatoid Arthritis

## One-Sentence Summary

> Mesalazine (5-aminosalicylic acid, 5-ASA) is the active anti-inflammatory metabolite of sulfasalazine, a compound historically used for inflammatory bowel disease. The TxGNN model's top-ranked signal is a data artifact with no supporting evidence, so this evaluation instead focuses on the model's third-ranked, evidence-backed prediction: **Rheumatoid Arthritis**, supported by **6 clinical trials** and **20 publications** — though the literature itself disputes whether mesalazine, rather than its co-metabolite sulfapyridine, is the moiety actually responsible for the antirheumatic effect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in registry data (drug unregistered in Singapore); literature evidence indicates mesalazine is the active metabolite of sulfasalazine, used for inflammatory bowel disease (ulcerative colitis) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% (rank 5,829 of all drug–disease pairs) |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for mesalazine is not available in the source registry (DrugBank field flagged as a High-severity data gap). Based on the literature captured in this evidence pack, mesalazine (5-ASA) is one of the two active metabolites of sulfasalazine (the other being sulfapyridine), produced by colonic bacterial cleavage. Sulfasalazine itself has a well-documented history as a disease-modifying antirheumatic drug (DMARD), first used for rheumatic polyarthritis in the 1940s (PMID 7588084) before its use was extended to ulcerative colitis. Mechanistically, 5-ASA and sulfasalazine metabolites have been shown to suppress prostaglandin and leukotriene release from synovial tissue (PMID 1673814) and to reduce inflammatory cytokine and matrix metalloproteinase mRNA expression in rheumatoid synovial fibroblasts (PMID 10743803), providing a plausible anti-inflammatory rationale for activity in joint disease.

However, this is where the evidence becomes genuinely equivocal rather than simply supportive. Two independent clinical investigations (PMID 2860942, PMID 2877851) directly compared the two sulfasalazine moieties in RA patients and found that **sulfapyridine**, not 5-ASA/mesalazine, produced the pronounced second-line antirheumatic effect, while 5-ASA alone showed only a weak first-line effect. A subsequent review (PMID 8535642) confirms this consensus: the bulk of evidence favors sulfapyridine as the active moiety in RA. This means the strong historical evidence base for "sulfasalazine in RA" cannot be automatically attributed to mesalazine itself — the repurposing hypothesis rests on a mechanistically plausible but empirically contested claim.

For context, the TxGNN model's second-ranked, evidence-backed prediction — osteoarthritis (L4, preclinical only) — is supported by a distinct and more recent mechanistic line: a 2024 *Nature Communications* study proposing that 5-ASA suppresses osteoarthritis progression via the OSCAR-PPARγ axis (PMID 38310093). This is mentioned for completeness but is not the primary subject of this report, as it has zero clinical trial validation to date.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02930343](https://clinicaltrials.gov/study/NCT02930343) | Phase 3 | Terminated | 136 | The only trial in this set where both drug and indication match precisely: head-to-head RCT of sulfasalazine- vs. leflunomide-based combination DMARD therapy in RA patients failing methotrexate monotherapy. Terminated before completion; reason (safety vs. recruitment/funding) not documented in this evidence pack. |
| [NCT00637780](https://clinicaltrials.gov/study/NCT00637780) | Phase 4 | Terminated | 2 | Pharmacokinetics of sulfasalazine delayed-release tablets in pediatric Juvenile Idiopathic Arthritis, not adult RA; terminated with only 2 participants enrolled — low evidentiary value. |
| [NCT06201793](https://clinicaltrials.gov/study/NCT06201793) | Phase 2 | Completed | 46 | Evaluates minocycline (not mesalazine) added to mesalamine therapy in ulcerative colitis; drug/indication combination does not match RA. |
| [NCT05580861](https://clinicaltrials.gov/study/NCT05580861) | Phase 1/2 | Recruiting | 64 | Sulfasalazine combined with induction chemotherapy in older AML patients, exploiting its xCT/cystine-transporter inhibitory activity — an oncologic mechanism unrelated to RA. |
| [NCT00514982](https://clinicaltrials.gov/study/NCT00514982) | Phase 2 | Withdrawn | 0 | Observational study of step-up IBD therapy for Hermansky-Pudlak Syndrome-associated colitis; not RA-related and withdrawn with zero enrollment. |
| [NCT03591770](https://clinicaltrials.gov/study/NCT03591770) | Phase 4 | Terminated | 15 | Shingrix vaccine immunogenicity in ulcerative colitis patients on tofacitinib; unrelated to RA or mesalazine. |

**Note:** Only one of these six trials (NCT02930343) actually pairs the correct drug class with the correct indication, and it did not reach completion. There is currently no completed RCT isolating mesalazine's (as opposed to sulfasalazine's) effect in RA.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2860942](https://pubmed.ncbi.nlm.nih.gov/2860942/) | 1985 | Mechanistic/Clinical Investigation | BMJ | Sulfapyridine showed a pronounced second-line antirheumatic effect comparable to sulfasalazine; 5-aminosalicylic acid alone showed only a weak first-line effect — directly questions mesalazine's independent efficacy in RA. |
| [2877851](https://pubmed.ncbi.nlm.nih.gov/2877851/) | 1986 | Clinical Investigation | Drugs | 30 RA patients on 5-ASA or sulfapyridine alone; sulfasalazine-derived sulfapyridine improved disease activity, 5-ASA did not. |
| [7588084](https://pubmed.ncbi.nlm.nih.gov/7588084/) | 1995 | Review | Drugs | Comprehensive review establishing sulfasalazine as a DMARD since the 1940s; notes uncertainty over whether the parent molecule, sulfapyridine, or both is the active principle. |
| [8535642](https://pubmed.ncbi.nlm.nih.gov/8535642/) | 1995 | Review | British Journal of Rheumatology | Concludes the bulk of evidence favors sulfapyridine, not 5-ASA, as the active and toxicity-driving moiety in RA. |
| [2899645](https://pubmed.ncbi.nlm.nih.gov/2899645/) | 1988 | Cohort/Clinical | Journal of Rheumatology | 12 weeks of sulfasalazine treatment normalized elevated circulating activated lymphocytes in RA patients, suggesting an immunomodulatory mechanism. |
| [10743803](https://pubmed.ncbi.nlm.nih.gov/10743803/) | 2000 | Mechanistic | Journal of Rheumatology | Sulfasalazine and its metabolites (including 5-ASA) reduce mRNA levels of inflammatory cytokines and matrix metalloproteinases in rheumatoid synovial fibroblasts. |
| [7904547](https://pubmed.ncbi.nlm.nih.gov/7904547/) | 1993 | Review | Clinical Pharmacokinetics | Pharmacokinetic review of slow-acting antirheumatic drugs, including sulfasalazine; notes months-long delay to full clinical effect. |
| [1356747](https://pubmed.ncbi.nlm.nih.gov/1356747/) | 1992 | Review | Deutsche Medizinische Wochenschrift | Reviews aminosalicylates across chronic inflammatory bowel disease and rheumatoid arthritis. |
| [12235076](https://pubmed.ncbi.nlm.nih.gov/12235076/) | 2002 | Pharmacovigilance | Gut | Re-evaluation of serious adverse reaction reports for sulfasalazine and mesalazine submitted to the UK Committee on Safety of Medicines. |
| [17708602](https://pubmed.ncbi.nlm.nih.gov/17708602/) | 2007 | Cohort/Review | World Journal of Gastroenterology | Historical account: 5-ASA was originally designed to treat rheumatoid arthritis but was found more useful in ulcerative colitis instead — the reverse repurposing direction of the one proposed here. |

---

## Singapore Market Information

Mesalazine is currently **not registered or marketed** in Singapore under this Evidence Pack's regulatory data (0 licenses on file, market status: 未上市). No authorization records, product names, or approved indication text are available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information — no key warnings, contraindications, or drug-drug interaction data were returned from the structured safety query (DDI lookup status: not found, 0 interactions).

**Additional literature-reported signal (not part of the structured safety data):** A 2025 case report (PMID 41443863) describes mesalazine-induced colitis in a 76-year-old RA patient with no prior inflammatory bowel disease, following sulfasalazine and later mesalazine administration; a drug-induced lymphocyte stimulation test was positive for mesalazine. This is a single case report and not a systematic safety signal, but it is relevant to any future RA repurposing workup given the drug pair's shared metabolic origin.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The single drug/indication-matched trial (NCT02930343, Phase 3) was terminated before completion, and no completed RCT isolates mesalazine's own contribution to RA efficacy.
- Two independent clinical investigations (PMID 2860942, PMID 2877851) and a supporting review (PMID 8535642) indicate the antirheumatic activity of sulfasalazine is attributable mainly to its sulfapyridine metabolite, not mesalazine — undermining the mechanistic case for mesalazine specifically.
- A Blocking-severity data gap exists: no TFDA/regulatory warning or contraindication data is available, which per this evaluation's own scoring criteria prevents entry into the S1 safety pre-assessment stage.
- Mesalazine is not currently marketed in Singapore (0 registrations), so there is no local regulatory or supply pathway already in place.

**To proceed, the following is needed:**
- Official mechanism of action (MOA) data from DrugBank or an equivalent authoritative source (currently a High-severity data gap).
- Regulatory package insert / label data (warnings, contraindications) to clear the Blocking safety data gap before any S1 evaluation.
- A trial or pharmacokinetic study isolating mesalazine's antirheumatic activity independent of sulfapyridine, given the literature's direct challenge to the mechanistic premise.
- Clarification of NCT02930343's termination reason (safety signal vs. administrative/funding issue), as this is the only precisely matched trial in the evidence base.
- If interest continues, secondary monitoring of the osteoarthritis signal (rank 2, L4) is reasonable given its distinct and more recent mechanistic support (OSCAR-PPARγ axis), pending its own clinical validation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

