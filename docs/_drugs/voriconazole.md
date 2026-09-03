---
layout: default
title: Voriconazole
parent: 僅模型預測 (L5)
nav_order: 1066
evidence_level: L5
indication_count: 10
---

# Voriconazole
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

# Voriconazole: From Invasive Fungal Infection to Multidrug-Resistant Tuberculosis

## One-Sentence Summary

> Voriconazole is a triazole antifungal typically used for serious invasive fungal infections; detailed original-indication and mechanism-of-action data were not provided in this evidence pack.
> The TxGNN model predicts it may be effective for **Multidrug-Resistant Tuberculosis (MDR-TB)**,
> but this direction is currently supported only by **0 clinical trials** and **3 tangentially related publications** (case reports of fungal/TB co-infection, not evidence of anti-TB efficacy).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (voriconazole is a triazole antifungal, generally indicated for invasive fungal infections) |
| Predicted New Indication | Multidrug-Resistant Tuberculosis |
| TxGNN Prediction Score | 98.67% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on general pharmacological knowledge, voriconazole is a second-generation triazole antifungal that inhibits fungal cytochrome P450-dependent 14α-lanosterol demethylase, disrupting ergosterol synthesis in fungal cell membranes. It is not known to have activity against *Mycobacterium tuberculosis*, which has a fundamentally different cell wall (mycolic acid-based) and metabolic machinery than fungi.

There is no obvious mechanistic overlap between antifungal azole activity and anti-mycobacterial activity, and no original indication data was provided to establish a pharmacological bridge to MDR-TB. The three literature items retrieved for this candidate are case reports and in vitro studies describing **fungal infections (aspergillosis, chromoblastomycosis) that happen to co-occur with or mimic tuberculosis**, not studies demonstrating voriconazole efficacy against *M. tuberculosis* itself. This pattern — high TxGNN score paired with only incidental co-occurrence literature — is consistent with a knowledge-graph embedding artifact rather than a genuine repurposing signal, similar to other low-plausibility candidates in this drug's prediction list (e.g., Ambras-type hypertrichosis, Dandy-Walker malformation syndrome), which show no mechanistic or evidentiary link either.

Given the absence of confirmed MOA data, original indication data, and any direct supporting study, this candidate should be treated as a low-confidence model output requiring further validation before any further action.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18992166](https://pubmed.ncbi.nlm.nih.gov/18992166/) | 2008 | Case report | Cases Journal | Describes a diabetic patient with MDR-TB co-existing with aspergilloma/invasive aspergillosis — does not evaluate voriconazole for TB treatment, only for the concurrent fungal infection |
| [37145297](https://pubmed.ncbi.nlm.nih.gov/37145297/) | 2023 | In vitro study | Braz J Microbiol | Evaluates photodynamic therapy (not voriconazole) against multidrug-resistant fungal chromoblastomycosis; unrelated to TB treatment |
| [39359062](https://pubmed.ncbi.nlm.nih.gov/39359062/) | 2024 | Observational/genetic study | Virulence | Characterizes azole-resistant *Candida krusei* isolates; no TB or voriconazole-TB efficacy data |

**Note:** None of the retrieved literature directly evaluates voriconazole's efficacy against *M. tuberculosis* or MDR-TB.

---

## Singapore Market Information

Voriconazole currently has no registered licenses in Singapore (`total_licenses: 0`); no market authorization records were found in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The MDR-TB prediction lacks any direct supporting clinical trial or literature evidence — the three retrieved publications describe incidental fungal/TB co-infection scenarios rather than anti-tuberculosis efficacy of voriconazole, and there is no established mechanistic basis (azole antifungal vs. anti-mycobacterial activity) to support this repurposing signal. Additionally, voriconazole is not currently marketed in Singapore.

**To proceed, the following is needed:**
- Confirmed original indication and mechanism-of-action data (DrugBank/TFDA source)
- TFDA package insert (warnings, contraindications) — currently a blocking data gap (DG001)
- A mechanistic or preclinical rationale specifically linking triazole antifungal activity to anti-mycobacterial effect, if such exists
- Re-screening of literature/clinical trial databases specifically for "voriconazole AND tuberculosis" (direct efficacy studies), rather than co-occurrence hits
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

