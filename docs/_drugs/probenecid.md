---
layout: default
title: Probenecid
parent: 僅模型預測 (L5)
nav_order: 817
evidence_level: L5
indication_count: 10
---

# Probenecid
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

Using no additional skill — this is a direct documentation/report-writing task governed entirely by the prompt's own template, so I'm applying it directly against the supplied Evidence Pack.

# Probenecid: From No Registered Indication to Renal Hypouricemia (Signal Flagged as Reversed)

## One-Sentence Summary

> No original indication is recorded for Probenecid in this evidence pack, and the drug is not currently marketed in Singapore.
> TxGNN's top-ranked prediction proposes **Renal Hypouricemia** with a **99.73%** score,
> but the mechanistic review flags this as a likely **reversed-causality artifact** — probenecid's own uricosuric action *causes* hypouricemia rather than treating it —
> and the supporting evidence is limited to **20 case-oriented publications** with **no clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license/indication data in evidence pack |
| Predicted New Indication | Renal Hypouricemia (hypouricemia, renal) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank (flagged as a High-severity data gap in this pack). Based on the mechanistic rationale attached to the top prediction, probenecid is known to inhibit renal tubular organic anion/urate transporters (URAT1, OAT1, OAT3), which reduces urate reabsorption and increases uricosuria — this is the same pharmacology used clinically to *lower* serum uric acid (e.g., in gout management).

This is precisely why the prediction should be treated with caution rather than as supportive evidence: renal hypouricemia is a condition of *already excessive* urate excretion (often due to URAT1 loss-of-function mutations). Administering a drug whose entire pharmacological purpose is to further promote urate excretion would not treat this condition — it would plausibly worsen it. TxGNN most likely picked up this candidate because probenecid and "hypouricemia" co-occur heavily in the literature (probenecid is the classic pharmacological *inducer* of hypouricemia used in diagnostic testing), not because of a genuine therapeutic relationship. This is a textbook example of a direction-reversed knowledge graph signal and should not be advanced without independent pharmacological review.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia etiology and classification for rheumatologists; does not address probenecid as treatment |
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Review/Case | Molecular Genetics and Metabolism | Hereditary renal hypouricemia is caused by loss-of-function mutations in SLC22A12 (URAT1) |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohort/Genetic | J Am Soc Nephrol | Clinical/molecular analysis of URAT1 mutations in 32 Japanese renal hypouricemia patients |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Case Report | Am J Kidney Dis | Renal hypouricemia complicated by exercise-induced acute renal failure; discusses prevention, not probenecid therapy |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Case Report | Am J Kidney Dis | Two brothers with hereditary renal hypouricemia and exercise-induced ARF |
| [3813739](https://pubmed.ncbi.nlm.nih.gov/3813739/) | 1987 | Case Report | Arch Intern Med | Diabetic patients with renal hypouricemia due to increased pyrazinamide-suppressible urate clearance |
| [1944743](https://pubmed.ncbi.nlm.nih.gov/1944743/) | 1991 | Case Report | Nephron | Type 1 diabetics show increased uric acid clearance and hypouricemia vs controls |
| [1656732](https://pubmed.ncbi.nlm.nih.gov/1656732/) | 1991 | Case Report | Am J Kidney Dis | Cholangiocarcinoma-associated severe renal hypouricemia, mechanistic workup |
| [8341392](https://pubmed.ncbi.nlm.nih.gov/8341392/) | 1993 | Case Report | Nephron | Novel renal hypouricemia subtype; notably **no urate response to probenecid** was observed in this patient |
| [7099326](https://pubmed.ncbi.nlm.nih.gov/7099326/) | 1982 | Case Report | Nephron | Familial renal hypouricemia case; urate excretion **paradoxically decreased** with probenecid |

**Note:** All 20 literature items concern the natural disease (genetics, case reports of hereditary/acquired renal hypouricemia) or use probenecid as a *diagnostic reagent* to probe tubular urate transport — none report probenecid as a therapeutic agent for hypouricemia. Several (e.g., PMID 8341392, 7099326) directly show blunted or paradoxical responses to probenecid in these patients, further undermining the repurposing signal.

---

## Singapore Market Information

Probenecid has no Singapore HSA registration on record (`total_licenses: 0`; market status: Not marketed). No product/license data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all unavailable in this evidence pack; TFDA/HSA package insert retrieval is flagged as a Blocking data gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (renal hypouricemia) is very likely a reversed-causality artifact — probenecid's uricosuric mechanism would plausibly worsen, not treat, this condition — and no clinical trial or RCT evidence exists to counter that concern. The remaining top-10 predictions (Lesch-Nyhan syndrome, HGPRT partial deficiency, cholelithiasis, and a cluster of hepatoportal/portal-hypertension disorders sharing an identical score of 0.9659) show either the same directional/safety concern (uricosuric therapy is contraindicated in overproduction-type hyperuricemia) or no mechanistic, literature, or trial support at all (L5, likely embedding-cluster artifacts). No candidate in this pack currently meets the bar to advance.

**To proceed, the following is needed:**
- HSA/manufacturer package insert — warnings, contraindications, DDI (Blocking gap, DG001)
- DrugBank mechanism-of-action detail (High-priority gap, DG002)
- A knowledge-graph review step to filter out drug-induced-phenotype vs. therapeutic-indication confusion (as seen here) before candidates reach S1 scoring
- If any candidate is pursued further, independent literature curation beyond case reports/case series, since none of the top 10 predictions currently have RCT or registered clinical trial support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

