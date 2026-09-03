---
layout: default
title: Tocilizumab
parent: 僅模型預測 (L5)
nav_order: 990
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab: From Rheumatoid Arthritis to Ankylosing Spondylitis

## One-Sentence Summary

> Tocilizumab is an IL-6 receptor antagonist whose established uses (per literature in this evidence pack) include rheumatoid arthritis and juvenile idiopathic arthritis. The TxGNN model predicts it may also be effective for **Ankylosing Spondylitis**, with **8 clinical trials** and **20 publications** identified — but two of the most relevant Phase 3 RCTs were **terminated due to lack of efficacy**, making this a case where strong model confidence is contradicted by direct clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore (no local license data); literature in this pack cites rheumatoid arthritis and juvenile idiopathic arthritis as established uses |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on known information within the collected literature, tocilizumab is a humanized monoclonal antibody targeting the IL-6 receptor, and its efficacy has been established in rheumatoid arthritis, systemic and polyarticular juvenile idiopathic arthritis, and giant cell arteritis.

Mechanistically, the hypothesis linking tocilizumab to ankylosing spondylitis (AS) is plausible: IL-6 is one of several pro-inflammatory cytokines implicated in spondyloarthritis pathogenesis, alongside TNF-α and the IL-17/IL-23 axis, and cross-cytokine involvement across rheumatic diseases is well documented in this dataset (e.g., PMID 22452603, "Antagonizing IL-6 in ankylosing spondylitis").

However, this is a case where the mechanistic rationale does **not** hold up in direct clinical testing. Two purpose-built Phase 2/3 randomized, placebo-controlled trials specifically testing tocilizumab in AS (NCT01209689, NCT01209702) were **terminated early due to insufficient efficacy**, and this is corroborated by a published trial-results paper (PMID 23765873, BUILDER-1/BUILDER-2). The prevailing interpretation in the field is that TNF-α and IL-17/IL-23 — not IL-6 — are the dominant pathogenic axis in axial spondyloarthritis, which explains why IL-6 blockade underperformed relative to TNF inhibitors. This is a useful reminder that a high TxGNN similarity score reflects network-level relatedness, not confirmed clinical efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | Terminated | 113 | RCT of tocilizumab vs placebo in AS patients with inadequate response to prior TNF antagonists; terminated for lack of efficacy — key negative direct evidence |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | Terminated | 306 | Seamless RCT of tocilizumab vs placebo in TNF-naïve AS patients who failed NSAIDs; terminated for lack of efficacy — corroborates negative finding above |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Completed | 60 | Mechanistic study of tocilizumab's effect on T follicular helper cells in RA; exploratory, not an AS efficacy endpoint |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | Recruiting | 10,000 | Korean nationwide biologics safety registry covering RA, AS, and PsA patients; observational, not interventional |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | Recruiting | 2,500 | Multi-centre biomarker/cytokine profiling registry in systemic inflammatory diseases; not an AS-specific interventional trial |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Observational study of risk of developing additional immune-mediated inflammatory diseases in patients on biologics/immunosuppressants |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Completed | 1,431 | Real-world observational registry of Inflectra (infliximab) use; not tocilizumab-specific |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management study in rheumatology patients undergoing shoulder arthroplasty; not an AS efficacy trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT results (BUILDER-1/2) | Annals of the Rheumatic Diseases | Reports short-term symptomatic efficacy assessment of tocilizumab in AS from randomized, placebo-controlled trials — the primary source underlying the terminated Phase 3 program |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Systematic Review / Network Meta-analysis | Medicine | Bayesian network meta-analysis comparing effectiveness of all available biologic regimens in AS |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflammation & Allergy Drug Targets | Reviews the rationale and evidence for IL-6 antagonism in AS pathogenesis |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Meta-analysis (Cohort) | Clinical Rheumatology | Quantifies serious infection risk with biologics in AS and non-radiographic axial spondyloarthritis from RCT data |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Review | Seminars in Arthritis and Rheumatism | Italian expert board (ITABIO) review on second-line biologic therapy optimization in RA, PsA, and AS |
| [31852268](https://pubmed.ncbi.nlm.nih.gov/31852268/) | 2020 | Cohort | Expert Review of Clinical Immunology | Compares infection risk between non-biologic and biologic DMARDs (including IL-6 inhibitors) in inflammatory arthritis |
| [20851032](https://pubmed.ncbi.nlm.nih.gov/20851032/) | 2010 | Case Report | Joint Bone Spine | Case of tocilizumab use in a patient with AS and Crohn's disease refractory to TNF antagonists |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Case Report | Frontiers in Medicine | Two cases of AA amyloidosis secondary to AS successfully treated with tocilizumab |
| [32872025](https://pubmed.ncbi.nlm.nih.gov/32872025/) | 2020 | Case Report / Review | Medicine | Two case reports and literature review of AS complicating Turner syndrome |
| [20959960](https://pubmed.ncbi.nlm.nih.gov/20959960/) | 2011 | Review | Osteoporosis International | Reviews systemic bone effects of biologic therapies in RA and AS |

---

## Singapore Market Information

Tocilizumab is **not currently registered** in Singapore (`total_licenses = 0`). No local authorization records, brand names, or approved indication text are available in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are all currently unavailable in this evidence pack (flagged as Blocking data gap DG001 — TFDA/HSA label warnings and contraindications).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Although TxGNN assigns ankylosing spondylitis a very high confidence score (99.99%), the two most directly relevant Phase 2/3 RCTs (NCT01209689, NCT01209702) were **terminated due to lack of efficacy**, and this negative outcome is confirmed in the published literature (PMID 23765873). This is direct L1-grade evidence *against* pursuing this indication, not for it.
- The drug is not registered in Singapore, and both the mechanism of action and label safety data (warnings/contraindications) are missing (data gaps DG001–DG002), blocking any S1 safety pre-assessment.

**To proceed, the following is needed:**
- Retrieve tocilizumab's official label warnings/contraindications from HSA or the originator's regulatory filings (resolves DG001, currently Blocking)
- Confirm formal mechanism of action via DrugBank API query (resolves DG002)
- Given the negative AS signal, consider redirecting evaluation toward the pack's rank 7 and rank 10 candidates (polyarticular JIA and RF-positive polyarticular JIA), which reflect tocilizumab's already-approved indications and show consistent positive Phase 3 evidence — useful as a validation benchmark for this TxGNN pipeline rather than a "new" repurposing opportunity
- If AS is still of interest, monitor for newer trials/mechanisms (e.g., combination regimens) beyond the 2010–2011 terminated program, as no positive follow-up AS trials appear in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

