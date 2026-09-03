---
layout: default
title: Ticlopidine
parent: 僅模型預測 (L5)
nav_order: 979
evidence_level: L5
indication_count: 10
---

# Ticlopidine
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

# Ticlopidine: From Antiplatelet Therapy to Rheumatoid Arthritis

## One-Sentence Summary

> Ticlopidine is a thienopyridine-class antiplatelet agent (irreversible P2Y12/ADP receptor antagonist), historically used to prevent thrombotic/ischemic events (e.g., post-stent, stroke prophylaxis) before being largely superseded by clopidogrel.
> The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**,
> with **0 clinical trials** and **9 publications** currently supporting this direction — evidence is mechanistically peripheral rather than direct, and the drug is not currently marketed in Singapore.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — Ticlopidine is not marketed in Singapore, so no HSA-approved indication text exists in the evidence pack (antiplatelet/thromboprophylaxis use is inferred from embedded literature context, not from a local label) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 98.91% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed structured MOA data is marked as a data gap in this evidence pack. However, the review notes embedded in the evidence describe Ticlopidine as a thienopyridine-class drug that irreversibly antagonizes the P2Y12/ADP receptor on platelets — the same drug class as clopidogrel (PMID 11570785 confirms clopidogrel "replaced ticlopidine... worldwide" for antiplatelet indications such as post-angioplasty/stent placement).

The proposed link to rheumatoid arthritis (RA) is that RA patients carry elevated cardiovascular and microvascular ischemic risk (via chronic inflammation-driven endothelial dysfunction and hypercoagulability), and antiplatelet therapy could theoretically mitigate RA-associated vascular complications. Two small historical trials (PMID 2790405, PMID 3000794) even tested ticlopidine directly in RA patients and reported improvements in blood filterability, ESR, and joint counts — suggesting a possible independent "antirheumatic" effect beyond pure antiplatelet activity.

That said, RA's core pathology is autoimmune synovitis driven by cytokines (TNF-α, IL-6, etc.), not thrombosis. The antiplatelet mechanism addresses a downstream vascular complication rather than the primary disease process, so this is best characterized as a peripheral, supportive mechanistic link rather than a core therapeutic rationale — consistent with the L4 evidence level and "Hold" recommendation assigned in this evidence pack.

**Note:** Two other TxGNN candidates for this drug — female breast carcinoma and chronic HIV-associated platelet activation (both L2, "Research Question") — carry substantially stronger evidence, including a completed Phase 2 RCT (PMID 24267729, NCT02578706) on antiplatelet inhibition of circulating tumor cells and platelet reactivity. These may warrant separate evaluation despite ranking below RA on raw TxGNN score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2790405](https://pubmed.ncbi.nlm.nih.gov/2790405/) | 1989 | Small double-blind study | Br J Rheumatol | Oral ticlopidine vs placebo (n=40 RA patients on NSAID) significantly improved ESR (-28%) and whole blood filterability |
| [3000794](https://pubmed.ncbi.nlm.nih.gov/3000794/) | 1985 | Small open-label clinical study (biomarker endpoint) | Eur J Clin Pharmacol | 18-month low-dose ticlopidine (250 mg/day, n=22) reduced involved joint counts, Tc-index and ESR; increased serum sulfhydryl levels |
| [27188755](https://pubmed.ncbi.nlm.nih.gov/27188755/) | 2016 | Cohort (clopidogrel, class-effect proxy) | BMC Musculoskelet Disord | Compared ADP-dependent platelet activation across systemic sclerosis, RA, and healthy controls; clopidogrel suppression assessed as class-effect reference |
| [25446727](https://pubmed.ncbi.nlm.nih.gov/25446727/) | 2015 | Review | Nat Rev Gastroenterol Hepatol | Cites RA as a reference model for chronic inflammatory disease-associated cardiovascular risk |
| [19765672](https://pubmed.ncbi.nlm.nih.gov/19765672/) | 2010 | Review | Clin Gastroenterol Hepatol | Reviews diseases/drugs, including RA, associated with acute large bowel ischemia risk |
| [26939212](https://pubmed.ncbi.nlm.nih.gov/26939212/) | 2015 | Review/case series | Rom J Intern Med | Describes an RA patient on antiplatelet/antithrombotic therapy presenting with atherothrombotic disease and bleeding |
| [16729012](https://pubmed.ncbi.nlm.nih.gov/16729012/) | 2006 | Case report | Nat Clin Pract Cardiovasc Med | RA patient with lupus anticoagulant and ischemic myocardial microangiopathy |
| [7893538](https://pubmed.ncbi.nlm.nih.gov/7893538/) | 1994 | Case report | No To Shinkei | RA patient with hemiparesis and renal failure |
| [41689871](https://pubmed.ncbi.nlm.nih.gov/41689871/) | 2026 | Pending classification | Drug Metab Dispos | Herbal compound (bicuculline) CYP2C19 interaction study; background notes use of related compound for RA symptom relief |

---

## Singapore Market Information

No HSA license records found. Ticlopidine is not currently marketed in Singapore (0 registrations).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rheumatoid arthritis signal rests on two small, decades-old trials (1985, 1989) with a mechanistically indirect link (antiplatelet effect on vascular complications, not core autoimmune pathology), and no clinical trials currently target this indication. Combined with the absence of Singapore market presence and a blocking data gap on product labeling, evidence does not support progression beyond hypothesis-generation at this time.

**To proceed, the following is needed:**
- TFDA/HSA product label (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Confirmed DrugBank mechanism of action record (DG001/DG002 remediation)
- A modern-era trial (post-2000) re-testing ticlopidine or a class analog specifically in RA populations, given known thienopyridine-class hematologic risks (e.g., neutropenia, TTP) that may limit chronic RA use
- Separate evaluation of the breast carcinoma and HIV-associated platelet activation candidates, which carry stronger (L2) evidence including a completed Phase 2 RCT
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

