---
layout: default
title: Flurbiprofen
parent: 僅模型預測 (L5)
nav_order: 441
evidence_level: L5
indication_count: 10
---

# Flurbiprofen
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

# Flurbiprofen: From Rheumatoid Arthritis to Ankylosing Spondylitis

## One-Sentence Summary

Flurbiprofen is a propionic acid-class NSAID established for the treatment of rheumatoid arthritis, osteoarthritis, and musculoskeletal pain — however, it is not currently registered in Singapore.

The TxGNN model's top-ranked prediction (rank 1) is a rare skeletal genetic disorder with zero clinical evidence. Scanning down the ranked list, **Ankylosing Spondylitis** (rank 8, score 99.97%) emerges as the first clinically actionable prediction, supported by **0 registered clinical trials** but **20 published studies including 6 head-to-head RCTs** dating from 1974–1986 directly evaluating flurbiprofen in AS patients.

> **Note on prediction ranking**: Ranks 1–7 are all ultra-rare congenital skeletal dysplasias (e.g., acromesomelic dysplasia, brachydactyly-syndactyly syndrome) for which NSAID treatment has no mechanistic basis or any clinical evidence — all scored "Hold / L5." This report focuses on ankylosing spondylitis (rank 8) as the first prediction with substantive clinical evidence and a coherent mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; established global uses include rheumatoid arthritis and osteoarthritis |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.97% (rank 838 in full disease universe) |
| Evidence Level | L2 (multiple comparative RCTs; pooled Phase III safety data across 1,677 patients suggests potential L1) |
| Singapore Market Status | ✗ Not marketed |
| Number of Singapore Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Flurbiprofen is a phenylalkanoic acid-class NSAID that inhibits both COX-1 and COX-2 cyclooxygenase enzymes, thereby reducing the synthesis of prostaglandins (PGE₂, PGI₂). These prostaglandins are central mediators of inflammation, pain, and fever. While detailed MOA data from the current data pipeline is unavailable, the drug's pharmacological class and mechanism are well-characterised in the retrieved literature going back to the 1970s.

Ankylosing spondylitis (AS) is a chronic HLA-B27-associated inflammatory arthritis predominantly affecting the axial skeleton. Its hallmark features — spinal inflammation, morning stiffness, progressive ankylosis, and new bone formation — are all mediated in part through COX-dependent prostaglandin pathways. PGE₂ plays a direct role in activating osteoclasts and driving spinal entheseal inflammation. By suppressing prostaglandin synthesis, NSAIDs are the pharmacological cornerstone of AS management and have remained first-line therapy across all major clinical guidelines (ASAS, ACR, EULAR) for decades.

The mechanistic overlap between flurbiprofen and established AS treatments is complete: indomethacin, naproxen, and phenylbutazone — all COX inhibitors — are among the comparators in the head-to-head RCTs retrieved. In fact, six of these trials directly pit flurbiprofen against AS standard-of-care agents and demonstrate equivalent efficacy, validating that flurbiprofen's COX inhibition achieves the same therapeutic target. Some NSAID research also suggests a potential disease-modifying effect through inhibition of new bone formation (radiographic progression), adding further mechanistic interest beyond pure symptom relief.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for flurbiprofen in ankylosing spondylitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [4611579](https://pubmed.ncbi.nlm.nih.gov/4611579/) | 1974 | RCT (Double-blind crossover) | British Medical Journal | Flurbiprofen 150 mg/day vs phenylbutazone 300 mg/day in 35 AS patients over 4 weeks; flurbiprofen showed therapeutic efficacy approaching that of phenylbutazone with good tolerability |
| [4595274](https://pubmed.ncbi.nlm.nih.gov/4595274/) | 1974 | RCT (Double-blind crossover) | Annals of the Rheumatic Diseases | Three-arm crossover trial comparing indomethacin, flurbiprofen, and placebo in AS patients |
| [71969](https://pubmed.ncbi.nlm.nih.gov/71969/) | 1977 | RCT (Parallel, double-blind) | Current Medical Research and Opinion | Flurbiprofen 150–200 mg/day vs indomethacin 75–100 mg/day in 26 active AS patients over 6 weeks; both drugs equally effective in relieving pain and joint tenderness |
| [329422](https://pubmed.ncbi.nlm.nih.gov/329422/) | 1977 | RCT (Parallel, double-blind) | Southern Medical Journal | Confirmatory parallel-design RCT in 26 AS patients; flurbiprofen vs indomethacin showed equivalent efficacy, with no withdrawals for lack of efficacy in either arm |
| [324773](https://pubmed.ncbi.nlm.nih.gov/324773/) | 1977 | RCT (Parallel, double-blind) | European Journal of Clinical Pharmacology | Flurbiprofen 150–200 mg/day vs phenylbutazone 300–400 mg/day in 27 active AS patients over 6 weeks; both equally effective in pain and tenderness relief |
| [7003449](https://pubmed.ncbi.nlm.nih.gov/7003449/) | 1980 | RCT (Double-blind crossover) | New Zealand Medical Journal | Flurbiprofen 200 mg/day vs naproxen 750 mg/day in 30 AS patients over 4 weeks; both very effective for pain and stiffness with no significant difference in efficacy |
| [3963018](https://pubmed.ncbi.nlm.nih.gov/3963018/) | 1986 | RCT (Randomised, double-blind) | American Journal of Medicine | Flurbiprofen vs indomethacin in 57 AS patients over 26 weeks; flurbiprofen 200 mg/day (in divided doses) effectively controlled pain and AS symptoms, equivalent to indomethacin |
| [3963017](https://pubmed.ncbi.nlm.nih.gov/3963017/) | 1986 | RCT (Randomised, double-blind) | American Journal of Medicine | Flurbiprofen vs phenylbutazone in 90 AS patients over 26 weeks; flurbiprofen 200 mg/day (TID) equivalent to phenylbutazone 300 mg/day in symptom control; some patients responded at 150 mg/day |
| [3963024](https://pubmed.ncbi.nlm.nih.gov/3963024/) | 1986 | Safety study (Pooled Phase III) | American Journal of Medicine | Pooled analysis of 9 Phase III trials (1,677 patients: AS, OA, RA); no clinically significant changes in liver or kidney function across treatment groups |
| [391529](https://pubmed.ncbi.nlm.nih.gov/391529/) | 1979 | Systematic review | Drugs | Comprehensive pharmacological review; flurbiprofen 120–300 mg/day comparable to aspirin and indomethacin in RA and AS with generally fewer side effects; advocates use for AS and allied conditions |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data including key warnings, contraindications, and drug-drug interactions were not available in the current evidence pack. Given that flurbiprofen is an NSAID, clinicians should be aware of the class-wide safety profile relevant to all NSAIDs: gastrointestinal mucosal injury (gastropathy), renal function impairment with prolonged use, cardiovascular risks, and fluid retention. Concomitant use of proton pump inhibitors should be considered for at-risk patients per standard NSAID gastroprotection guidelines.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Six direct head-to-head RCTs conducted between 1974 and 1986 consistently demonstrate that flurbiprofen is equivalent in efficacy to indomethacin, naproxen, and phenylbutazone for active ankylosing spondylitis, and a pooled safety analysis across nine Phase III trials (1,677 patients) confirmed an acceptable liver and kidney safety profile. The mechanistic basis — COX-dependent prostaglandin suppression in a prostaglandin-driven inflammatory arthritis — is unambiguous and shared by the established first-line NSAID treatments for AS.

**To proceed, the following is needed:**

- **Singapore registration pathway**: Flurbiprofen is not currently registered in Singapore; a formal regulatory submission to HSA (Health Sciences Authority) would be required, including original NDA data and current international labelling
- **Formal MOA documentation**: Retrieve full DrugBank/TFDA package insert to complete the mechanistic analysis
- **Safety package completion**: Obtain current prescribing information (SmPC or FDA label) to document up-to-date contraindications, boxed warnings, and drug-drug interaction profile — particularly cardiovascular and GI risks mandated in modern NSAID labelling post-COX-2 era
- **Comparative positioning**: Clarify how flurbiprofen would be positioned versus currently available NSAIDs and biologics (anti-TNF, IL-17i) in Singapore's AS treatment landscape
- **Update evidence search**: The RCT evidence base is largely from 1974–1986; a contemporary systematic review search is recommended to confirm no disqualifying safety signals have emerged and to assess alignment with current ASAS/EULAR AS guidelines
- **Formulation strategy**: Identify an appropriate available dosage form (immediate-release oral tablet, sustained-release capsule) for the target Singapore patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

