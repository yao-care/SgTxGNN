---
layout: default
title: Zidovudine
parent: 僅模型預測 (L5)
nav_order: 1073
evidence_level: L5
indication_count: 10
---

# Zidovudine
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

# Zidovudine: From HIV/AIDS Treatment to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Zidovudine (AZT) is the first nucleoside reverse transcriptase inhibitor (NRTI) developed for HIV/AIDS treatment in humans.
> The TxGNN model's top-ranked prediction for this drug is **Feline Acquired Immunodeficiency Syndrome** — a veterinary (cat) disease, not a human indication —
> supported by **0 clinical trials** and **20 publications**, all of which are animal-model studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore (drug not marketed there); internationally established as first-in-class NRTI for HIV/AIDS |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (veterinary) |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Zidovudine is a nucleoside reverse transcriptase inhibitor (NRTI) that was originally developed and approved for treating human immunodeficiency virus (HIV) infection; its efficacy comes from inhibiting the viral reverse transcriptase enzyme required for retroviral replication.

Feline immunodeficiency virus (FIV), which causes Feline Acquired Immunodeficiency Syndrome, is a lentivirus closely related to HIV and produces a clinically similar immunodeficiency syndrome in cats. Because both viruses share the same reverse-transcriptase-dependent replication mechanism, it is biologically plausible that a reverse transcriptase inhibitor effective against HIV would also show activity against FIV — and this is exactly what decades of veterinary research (summarized below) have shown in vitro and in experimentally infected cats.

However, this is a **veterinary, not human, indication**. There is no evidence in this pack of any human clinical relevance for this specific disease term, and none of the supporting literature involves human subjects or clinical trials. The mechanistic plausibility is real, but it does not translate into an actionable human drug-repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2475068](https://pubmed.ncbi.nlm.nih.gov/2475068/) | 1989 | Animal Model Study | Antimicrob Agents Chemother | Established FIV reverse transcriptase as sufficiently similar to HIV-1 RT to support use as a chemotherapy model |
| [2163339](https://pubmed.ncbi.nlm.nih.gov/2163339/) | 1990 | Animal Toxicity Study | Fundam Appl Toxicol | Evaluated zidovudine toxicity in FeLV-infected cats across five dosage groups |
| [2178336](https://pubmed.ncbi.nlm.nih.gov/2178336/) | 1990 | Animal Trial | Antimicrob Agents Chemother | AZT alone had no effect on FeLV viral load; AZT + IFN-alpha showed therapeutic benefit in presymptomatic FeLV-FAIDS |
| [2164083](https://pubmed.ncbi.nlm.nih.gov/2164083/) | 1990 | Animal Trial | J Acquir Immune Defic Syndr | AZT + interferon-alpha + IL-2 evaluated as prophylaxis for FeLV-induced immunodeficiency syndrome |
| [7688949](https://pubmed.ncbi.nlm.nih.gov/7688949/) | 1993 | Animal Cohort | Arch Virol | Zidovudine lowered plasma FIV titers at 2 weeks post-infection but did not prevent establishment of infection |
| [8381867](https://pubmed.ncbi.nlm.nih.gov/8381867/) | 1993 | Animal Study | J Acquir Immune Defic Syndr | Prophylactic ZDV prevented early viremia and lymphocyte decline but not primary FIV infection |
| [11943320](https://pubmed.ncbi.nlm.nih.gov/11943320/) | 2002 | pending | Vet Immunol Immunopathol | AZT/3TC combination showed additive-to-synergistic anti-FIV activity in vitro, but efficacy against pathogenesis was limited |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | pending | Antiviral Res | Combined zidovudine + lamivudine + abacavir suppressed FIV replication in vitro, informing HIV drug-interaction research |
| [22816034](https://pubmed.ncbi.nlm.nih.gov/22816034/) | 2012 | pending | Viruses | Single-agent antiretroviral therapy during acute FIV infection did not alter the course of chronic infection |
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | pending | J Feline Med Surg | Long-term (5-6 year) follow-up of FIV-infected cats treated with zidovudine (AZT) as part of antiretroviral therapy |

*10 additional publications on FIV/SIV/FeLV models are available in the underlying evidence pack but are omitted here for brevity.*

---

## Singapore Market Information

Zidovudine is not currently registered or marketed in Singapore (0 licenses on record); no product information is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Detailed TFDA/HSA label warnings and contraindications for this drug are flagged as a blocking data gap (DG001) and mechanism-of-action data as a high-priority gap (DG002); both should be resolved before any further safety evaluation.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Feline Acquired Immunodeficiency Syndrome) is a veterinary, not human, disease target. All supporting evidence (20 publications) consists of animal-model, toxicity, and in vitro studies in cats; there are no human clinical trials and no human safety data for this indication. This candidate is not clinically actionable for human drug repurposing.

**To proceed, the following is needed:**
- Reframe the evaluation around human-relevant indications: the same evidence pack shows **"AIDS related complex"** (rank 6) with L1 evidence and a historical FDA approval basis (Zidovudine's original approved use), which is a substantially stronger candidate and merits its own evaluation report.
- Resolve blocking data gap DG001 (TFDA/HSA warnings and contraindications) before any S1 safety review can proceed for this drug in Singapore.
- Resolve high-priority data gap DG002 (mechanism of action) via DrugBank API query.
- If veterinary repurposing is genuinely in scope for this program, obtain veterinary regulatory and pharmacokinetic data, which are entirely absent from this evidence pack.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

