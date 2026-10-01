---
layout: default
title: Probenecid
parent: Medium Evidence (L3-L4)
nav_order: 817
evidence_level: L4
indication_count: 10
---

# Probenecid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Probenecid: From Gout (Uricosuric) to Renal Hypouricemia

## One-Sentence Summary

Probenecid is an oral uricosuric tablet that is marketed in Singapore, although its registration record does not state an approved indication. The TxGNN model predicts it may be effective for **renal hypouricemia**, a condition of abnormally low blood uric acid. **No clinical trials** and **20 publications** (mostly case reports and reviews) are linked to this prediction. In those papers probenecid appears as a diagnostic probe, not as a treatment, and its known pharmacology would likely worsen the condition, so this prediction should not be pursued as a therapy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration record (probenecid is a uricosuric class drug, classically used for gout and hyperuricemia) |
| Predicted New Indication | Renal hypouricemia |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, probenecid inhibits renal urate transporters (URAT1) and organic anion transporters (OATs). This increases urinary urate excretion and lowers serum urate, which is why it is a uricosuric.

The high score most likely reflects the dense network of links between probenecid, urate transporters and the urate-handling genes and diseases in the knowledge graph. The mechanism points the wrong way for treatment. Renal hypouricemia is mostly caused by loss-of-function mutations in SLC22A12 (URAT1), which already leave patients with too much urate leaving through the kidney. A drug that further increases urate excretion would be expected to worsen the problem, not correct it.

The literature supports this reading. Probenecid is used as a **diagnostic probe**, and in several patients the urate response to probenecid was blunted or even paradoxical, which helps classify the type of transport defect. None of the papers reports probenecid as a treatment for the condition. This looks like a graph artifact of a disease-drug association rather than a true repurposing signal.

The other nine predictions (Lesch-Nyhan syndrome, partial HPRT deficiency, cholelithiasis, several rare hepatic and portal disorders, and a phenylalanine metabolism disorder) are no stronger. Seven have no clinical evidence at all. The remaining two have only indirect or tool-use literature, and several share identical scores that point to a common graph-neighborhood artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Review | Mol Genet Metab | Hereditary renal hypouricemia is mostly caused by loss-of-function mutations in SLC22A12 (URAT1), which impair urate reabsorption in the proximal tubule |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clin Rheumatol | Narrative update on hypouricemia (serum urate < 2 mg/dL), its causes and what rheumatologists should know |
| [476267](https://pubmed.ncbi.nlm.nih.gov/476267/) | 1979 | Review | Biomedicine | Review of eight families with inborn hypouricemia from an isolated renal tubular defect; hyperuricosuria is constant and urolithiasis is common |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Case series | J Am Soc Nephrol | 32 Japanese patients with renal hypouricemia were sequenced for SLC22A12 to link genetic and clinical features |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Case report + review | Am J Kidney Dis | Recurrent exercise-induced acute renal failure in a patient with renal hypouricemia, with discussion of prevention |
| [8341392](https://pubmed.ncbi.nlm.nih.gov/8341392/) | 1993 | Case report | Nephron | A novel subtype with no urate excretion response to pyrazinamide or probenecid |
| [7099326](https://pubmed.ncbi.nlm.nih.gov/7099326/) | 1982 | Case report | Nephron | Familial renal hypouricemia in which urate excretion was paradoxically decreased by probenecid |
| [854144](https://pubmed.ncbi.nlm.nih.gov/854144/) | 1977 | Case report | Nephron | Familial hypouricemia with only a slight uric acid clearance response to probenecid and pyrazinamide, suggesting a reabsorption defect |
| [2709741](https://pubmed.ncbi.nlm.nih.gov/2709741/) | 1989 | Case report | Klin Wochenschr | Acute renal failure from uric acid nephropathy in renal hypouricemia; urate fractional excretion was enhanced by probenecid |
| [8302413](https://pubmed.ncbi.nlm.nih.gov/8302413/) | 1993 | Case report | Nephron | Renal hypouricemia with urolithiasis; probenecid increased urate clearance, and the stones were treated by urine alkalization |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN07685P | PROBENECID TABLET 500 mg (Sunward Pharmaceutical Private Limited) | Tablet | Not stated in the registration record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials, and the literature uses probenecid as a diagnostic probe rather than a therapy. Its uricosuric action would be expected to aggravate renal hypouricemia, so the high TxGNN score is best explained as a graph artifact. The other predicted indications are also unsupported.

**To proceed, the following is needed:**
- The HSA package insert, including approved indication, warnings and contraindications
- Detailed mechanism of action data (MOA)
- A pharmacology and clinical expert review of the direction of effect, before any further investment
- Any evidence of probenecid benefit in a URAT1-deficient model or patient; without it, this candidate should be deprioritized

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

