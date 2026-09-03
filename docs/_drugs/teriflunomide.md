---
layout: default
title: Teriflunomide
parent: 僅模型預測 (L5)
nav_order: 958
evidence_level: L5
indication_count: 10
---

# Teriflunomide
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

# Teriflunomide: Original Indication Data Unavailable → Relapsing-Remitting Multiple Sclerosis (Confirmed Indication, Not Marketed in Singapore)

## One-Sentence Summary

> Teriflunomide's original indication and market history are not documented in this evidence pack (data gap), but the drug is internationally known and approved (as *Aubagio*) for relapsing-remitting multiple sclerosis (RRMS).
> The TxGNN model's top prediction for teriflunomide is also **Relapsing-Remitting Multiple Sclerosis**, supported by **30 clinical trials** (including two pivotal TEMSO Phase 3 RCTs) and **20 publications**.
> This is therefore best understood not as novel drug repurposing, but as a **Singapore market-entry candidate** for an indication already well-validated elsewhere.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current evidence pack (data gap) — internationally documented as relapsing-remitting multiple sclerosis (Aubagio) |
| Predicted New Indication | Relapsing-Remitting Multiple Sclerosis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not captured in the drug-level field of this evidence pack. However, the prediction rationale itself supplies mechanistic detail: teriflunomide is a **dihydroorotate dehydrogenase (DHODH) inhibitor**, blocking de novo pyrimidine synthesis and thereby selectively suppressing proliferation of rapidly dividing, activated T- and B-lymphocytes. This is a well-characterized immunomodulatory mechanism directly relevant to the autoimmune, inflammatory pathology of multiple sclerosis.

Importantly, the evidence pack itself flags that this "prediction" is **not a novel repurposing signal** — teriflunomide (marketed as Aubagio) already holds regulatory approval for RRMS in the US, EU, and other jurisdictions. TxGNN's high score here largely reflects the model correctly recovering a known, well-established drug–disease relationship rather than uncovering new therapeutic potential.

The practical significance for this evaluation is therefore different from a typical repurposing case: since teriflunomide is **not currently registered in the Singapore market**, the strategic question is not "does this mechanism plausibly work?" (it demonstrably does, per 30 trials and 20 publications) but "should this drug be brought to local registration/import for RRMS treatment?"

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Phase 3 | Completed | 1088 | Pivotal TEMSO trial — placebo-controlled RCT establishing teriflunomide's efficacy in reducing relapse frequency and disability accumulation in RRMS |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Phase 3 | Completed | 742 | TEMSO long-term extension — confirms durable safety/tolerability and long-term efficacy on disability, relapse rate, and MRI outcomes |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Phase 3 | Completed | 324 | Head-to-head RCT comparing teriflunomide vs. interferon beta-1a on effectiveness, relapse frequency, and tolerability |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Phase 4 | Active, not recruiting | 800 | DELIVER-MS — real-world comparison of early intensive vs. escalation treatment strategies including teriflunomide |
| [NCT06663189](https://clinicaltrials.gov/study/NCT06663189) | Phase 3 | Not yet recruiting | 200 | TWINS — evaluates safety of DMT (incl. teriflunomide) withdrawal in stable RRMS patients ≥55 years |
| [NCT06843382](https://clinicaltrials.gov/study/NCT06843382) | N/A | Not yet recruiting | 100 | ROOF-MS — real-world comparative study of teriflunomide vs. dimethyl fumarate on physical/cognitive fatigability |
| [NCT00273364](https://clinicaltrials.gov/study/NCT00273364) | Phase 2 | Completed | 110 | HSCT study in inflammatory MS failing prior therapy (teriflunomide not primary intervention) |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Phase 2 | Completed | 147 | Long-term extension assessing safety and efficacy of teriflunomide in MS with relapses |
| [NCT03464448](https://clinicaltrials.gov/study/NCT03464448) | N/A (Phase 4 mechanistic) | Completed | 30 | Mechanistic study — regulatory B-lymphocytes as mediators of teriflunomide's therapeutic effect |
| [NCT02490982](https://clinicaltrials.gov/study/NCT02490982) | N/A | Completed | 106 | Observational effectiveness study of teriflunomide in routine RRMS clinical practice |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | RCT | NEJM | Ofatumumab vs. teriflunomide — comparative efficacy in relapsing MS |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | RCT | NEJM | Ublituximab vs. teriflunomide in relapsing MS |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | RCT | NEJM | Tolebrutinib vs. teriflunomide — BTK inhibitor comparative trial |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Review (Network Meta-analysis) | Cochrane Database Syst Rev | Comparative benefit of immunomodulators/immunosuppressants (incl. teriflunomide) in RRMS |
| [26758290](https://pubmed.ncbi.nlm.nih.gov/26758290/) | 2016 | RCT-based review | CNS Drugs | EU SmPC review of teriflunomide — key clinical/safety outcomes |
| [33620411](https://pubmed.ncbi.nlm.nih.gov/33620411/) | 2021 | Review | JAMA | Diagnosis and treatment of MS — current evidence overview |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Review | Drugs | Teriflunomide: comprehensive review in RRMS |
| [31898276](https://pubmed.ncbi.nlm.nih.gov/31898276/) | 2020 | Review | CNS Drugs | Efficacy and safety of oral RRMS therapies including teriflunomide |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | RCT | JAMA Neurology | OPTIMUM — Ponesimod vs. teriflunomide, first head-to-head Phase 3 oral DMT trial |
| [37382446](https://pubmed.ncbi.nlm.nih.gov/37382446/) | 2023 | Review | Expert Rev Neurotherapeutics | Teriflunomide as first-line therapy in pediatric/adolescent RRMS |

---

## Singapore Market Information

Teriflunomide is currently **not registered/marketed in Singapore** (0 authorizations on file). No HSA license records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information — no structured warnings, contraindications, or drug interaction data were available in this evidence pack (key warnings, contraindications, and DDI query all returned no data).

**Note on a signal surfaced elsewhere in this evidence pack:** teriflunomide/its parent compound leflunomide carry known teratogenicity concerns (historically labeled Pregnancy Category X) and, per a case report reviewed for a separate candidate indication in this pack, leflunomide has been associated with a rare case of drug-induced thrombotic thrombocytopenic purpura ([PMID 34267852](https://pubmed.ncbi.nlm.nih.gov/34267852/)). These should be formally verified against the official package insert before any registration decision.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Efficacy of teriflunomide in RRMS is supported by extensive, high-quality evidence (two pivotal Phase 3 RCTs, multiple head-to-head Phase 3 trials against newer DMTs, and 20+ publications) — this is an L1-level, clinically confirmed indication internationally, not a speculative repurposing signal. The gap is regulatory, not scientific: the drug has zero registrations in Singapore.

**To proceed, the following is needed:**
- Confirm original indication/regulatory history and obtain the official package insert (teratogenicity, contraindications, DDI profile)
- Detailed mechanism-of-action documentation from DrugBank to close the current data gap
- Assessment of local regulatory pathway for market entry (new registration vs. parallel import) given the drug is unregistered in Singapore
- Safety monitoring plan addressing teratogenicity and hepatic/hematologic risk before clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

