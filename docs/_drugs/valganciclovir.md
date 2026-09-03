---
layout: default
title: Valganciclovir
parent: 僅模型預測 (L5)
nav_order: 1041
evidence_level: L5
indication_count: 10
---

# Valganciclovir
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

# Valganciclovir: From Cytomegalovirus Infection to Rheumatoid Arthritis

## One-Sentence Summary

Valganciclovir is a prodrug of ganciclovir, established for the treatment of cytomegalovirus (CMV) infections such as CMV retinitis. The TxGNN model predicts a possible association with **Rheumatoid Arthritis**, but the supporting evidence consists entirely of case reports describing CMV reactivation *in* RA patients on immunosuppressive therapy — not evidence that valganciclovir treats RA itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cytomegalovirus (CMV) infection (e.g., CMV retinitis) — inferred from literature context; no structured original-indication data available |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 98.97% |
| Evidence Level | L4 (mechanism/case-level only, no controlled studies) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for valganciclovir is not available in the structured drug profile (flagged as a data gap). Based on the literature collected in this evidence pack, valganciclovir is a prodrug that is rapidly hydrolyzed to ganciclovir, which inhibits CMV DNA polymerase. It is a pure antiviral agent with no known immunomodulatory activity on the pathways implicated in rheumatoid arthritis (TNF-α, IL-6, JAK-STAT).

The predicted RA association appears to be driven by a confounding pattern rather than a genuine pharmacological signal. Nearly all of the retrieved literature describes CMV reactivation or infection **occurring in** RA patients who were already immunosuppressed by other therapies — methotrexate, TNF inhibitors, tofacitinib, or upadacitinib. In these cases, RA is the background condition that predisposes patients to CMV disease requiring valganciclovir treatment; it is not a target that valganciclovir treats. This is best understood as a reverse-indexing artifact in the knowledge graph (RA and valganciclovir co-occur in the literature because of shared patients, not shared pharmacology).

Notably, a secondary prediction in this evidence pack (rank 2, "bronchitis," evidence level L3) points to a more biologically coherent — though still indirect — signal: valganciclovir prophylaxis reduces CMV reactivation after lung transplantation, which in turn lowers rates of bronchiolitis obliterans syndrome (BOS), a chronic rejection phenotype. That mechanism (prevent CMV → prevent a CMV-driven complication) is pharmacologically sound, unlike the RA signal, though it does not match "bronchitis" as a disease label and would need separate evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15155152](https://pubmed.ncbi.nlm.nih.gov/15155152/) | 2004 | Review | Expert Opin Drug Saf | General review of drug-induced retinal toxicity; RA-related drugs (e.g., hydroxychloroquine) discussed in a different context, not valganciclovir efficacy in RA |
| [18068874](https://pubmed.ncbi.nlm.nih.gov/18068874/) | 2008 | Review | La Revue de médecine interne | Notes absence of guidelines for antiviral management of CMV infection in patients on immunosuppressants for RA/SLE — a safety review, not an efficacy claim |
| [26150269](https://pubmed.ncbi.nlm.nih.gov/26150269/) | 2015 | Case Report | Reumatismo | CMV ileocolitis in an RA patient on immunosuppressive therapy |
| [28389165](https://pubmed.ncbi.nlm.nih.gov/28389165/) | 2017 | Case Report | J Infect Chemother | CMV retinitis with immune recovery uveitis in an elderly RA patient on methotrexate + tofacitinib |
| [25697299](https://pubmed.ncbi.nlm.nih.gov/25697299/) | 2015 | Case Report | BMJ Case Rep | Frail RA patient with pericardial effusion and concurrent CMV bowel involvement |
| [41779881](https://pubmed.ncbi.nlm.nih.gov/41779881/) | 2025 | Case Report | Retinal Cases Brief Rep | CMV retinitis in non-HIV RA patients on tofacitinib |
| [15494900](https://pubmed.ncbi.nlm.nih.gov/15494900/) | 2004 | Case Report | Clin Infect Dis | CMV retinitis in an RA patient treated with anti-TNF-α antibody therapy |
| [23904414](https://pubmed.ncbi.nlm.nih.gov/23904414/) | 2013 | Case Report | BMJ Case Rep | RA patient on methotrexate with CMV gastritis and concurrent H. pylori infection |
| [20711100](https://pubmed.ncbi.nlm.nih.gov/20711100/) | 2010 | Case Report | Acta Reumatol Port | Adult-onset Still's disease with CMV hepatitis, treated with valganciclovir |
| [23247975](https://pubmed.ncbi.nlm.nih.gov/23247975/) | 2013 | Case Report | Jpn J Ophthalmol | CMV and HHV-6 co-detected in a case of corneal endotheliitis (no RA link reported) |

---

## Singapore Market Information

Valganciclovir currently has no registration records in Singapore (market status: Not Marketed; 0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not currently available in this evidence pack — flagged as a blocking data gap requiring label retrieval before any safety evaluation.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (rheumatoid arthritis) is supported only by case reports describing CMV infection occurring *in* RA patients due to their immunosuppressive treatment — not evidence of valganciclovir efficacy against RA itself. This is a likely reverse-causality artifact, evidence level is L4, no clinical trials exist, and the drug is not currently marketed in Singapore.

**To proceed, the following is needed:**
- Resolve the blocking data gap: obtain the approved product label (warnings, contraindications, DDI) before any safety screening can begin
- Obtain confirmed mechanism-of-action data from DrugBank
- Independently verify whether TxGNN's disease node is capturing a genuine RA-treatment signal or a co-occurrence artifact, ideally with the model developer
- If further repurposing is pursued, consider re-scoping toward the more mechanistically coherent rank-2 signal (CMV prophylaxis to reduce bronchiolitis obliterans syndrome after lung transplantation) rather than the RA prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

