---
layout: default
title: Sulfasalazine
parent: 僅模型預測 (L5)
nav_order: 931
evidence_level: L5
indication_count: 10
---

# Sulfasalazine
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

# Sulfasalazine: From Rheumatoid Arthritis to Spondyloarthropathy Susceptibility

## One-Sentence Summary

Sulfasalazine is a classic DMARD (sulfapyridine + 5-aminosalicylic acid), long established for rheumatoid arthritis and inflammatory bowel disease. The TxGNN model highlights **spondyloarthropathy susceptibility** — particularly peripheral spondyloarthritis — as the strongest-supported repurposing signal among the top 10 predictions, backed by **13 publications** including a genetic-association cohort study, though no dedicated clinical trials for this exact indication were identified.

*Note: Among the 10 TxGNN candidates in this evidence pack, several (e.g., brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia) are flagged in the source data itself as likely embedding noise with no biological plausibility. This report focuses on the candidate with the highest actual evidence level (L2) and decision stage (S3).*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis / Ulcerative colitis (based on established clinical knowledge — not derived from Singapore registration data, since the drug is not currently registered locally) |
| Predicted New Indication | Spondyloarthropathy, susceptibility to |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (flagged as a High-severity data gap). Based on known information, sulfasalazine is a combination molecule (sulfapyridine + 5-aminosalicylic acid) whose anti-inflammatory activity — inhibition of NF-κB signalling and modulation of gut microbiota-driven immune activation — has been proven effective in rheumatoid arthritis and inflammatory bowel disease.

Spondyloarthropathies (reactive arthritis, psoriatic arthritis, IBD-associated arthritis, peripheral ankylosing spondylitis) share substantial inflammatory and gut-immune overlap with sulfasalazine's established indications, and sulfasalazine is already a guideline-recognized DMARD for **peripheral** spondyloarthritis. The TxGNN signal here should be read specifically as *susceptibility* — i.e., genetic/metabolic risk association — rather than a de novo therapeutic indication. This is reinforced by a Han Chinese cohort study (PMID 25413361) linking NAT (arylamine N-acetyltransferase) polymorphisms to both ankylosing spondylitis susceptibility and sulfasalazine-related adverse drug reactions, suggesting a pharmacogenomic link between drug metabolism and disease risk profile.

Importantly, the mechanistic link is weaker for **axial-only** disease — several RCTs cited in the underlying rationale report no benefit of sulfasalazine on axial symptoms of ankylosing spondylitis. Any repurposing pathway should therefore be scoped to peripheral spondyloarthritis phenotypes rather than the broader "spondyloarthropathy susceptibility" label predicted by the model.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25413361](https://pubmed.ncbi.nlm.nih.gov/25413361/) | 2014 | Genetic Association/Cohort | BMC Pharmacol Toxicol | NAT polymorphisms in Han Chinese AS patients linked to sulfasalazine-induced adverse drug reactions |
| [20436080](https://pubmed.ncbi.nlm.nih.gov/20436080/) | 2010 | Cohort (longitudinal) | J Rheumatol | Long-term follow-up of undifferentiated spondyloarthritis patients |
| [18166219](https://pubmed.ncbi.nlm.nih.gov/18166219/) | 2008 | Review | Semin Arthritis Rheum | Bench-to-clinic review of spondyloarthritis pathology and treatment |
| [15922688](https://pubmed.ncbi.nlm.nih.gov/15922688/) | 2005 | Review | Am J Med | Update on spondyloarthritis pathogenesis and management |
| [19938189](https://pubmed.ncbi.nlm.nih.gov/19938189/) | 2009 | Review | World J Gastroenterol | Rheumatic manifestations of IBD, including peripheral arthritis pathways |
| [10910178](https://pubmed.ncbi.nlm.nih.gov/10910178/) | 2000 | Review | Curr Opin Rheumatol | Review of juvenile spondyloarthropathies including reactive arthritis |
| [34599048](https://pubmed.ncbi.nlm.nih.gov/34599048/) | 2022 | Review | J Rheumatol | Interplay between COVID-19 and spondyloarthritis/its treatment |
| [8105815](https://pubmed.ncbi.nlm.nih.gov/8105815/) | 1993 | Review | APMIS | Discussion of antibiotic use in reactive arthritis |
| [1419506](https://pubmed.ncbi.nlm.nih.gov/1419506/) | 1992 | Review | Curr Opin Rheumatol | Immunogenetics of juvenile chronic arthritis and spondyloarthropathies |
| [12105678](https://pubmed.ncbi.nlm.nih.gov/12105678/) | 2002 | Review | Reumatismo | Advances in diagnosis and treatment of reactive arthritis |

---

## Singapore Market Information

Sulfasalazine currently has no marketing authorization registered in Singapore (market status: **Not Marketed**, 0 registrations).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Sulfasalazine already has an established therapeutic role in peripheral spondyloarthritis, and a genetic-association study directly links drug metabolism (NAT polymorphisms) to spondyloarthritis susceptibility and ADR risk — giving this candidate the highest evidence level (L2) and decision stage (S3) among the 10 TxGNN predictions reviewed. However, no dedicated clinical trials exist for the specific "susceptibility" framing, and axial disease is unlikely to respond.

**To proceed, the following is needed:**
- HSA-approved label warnings and contraindications (currently a Blocking data gap — required before any S1 safety review)
- Confirmed mechanism of action data from DrugBank (currently a High-severity data gap)
- Clarification of the intended clinical scope: peripheral vs. axial spondyloarthritis
- Singapore market registration pathway assessment, given the drug is not currently marketed locally
- Consideration of NAT-polymorphism pharmacogenomic screening in future protocol design, given the ADR association identified in the literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

