---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 867
evidence_level: L5
indication_count: 10
---

# Ritonavir
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

# Ritonavir: From HIV/AIDS to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Ritonavir is a HIV-1 protease inhibitor originally used as part of antiretroviral combination therapy (e.g., lopinavir/ritonavir, atazanavir/ritonavir) for HIV/AIDS.
> The TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) Infection**, a non-human primate disease used as a laboratory model for HIV research —
> supported only by **preclinical/animal literature (10 publications)**, with **no registered clinical trials**, reflecting a mechanistic rather than a clinically translatable signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV/AIDS antiretroviral therapy (per evidence-pack clinical context; not separately recorded in Singapore registry data) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, ritonavir is a HIV-1 protease inhibitor, most often used at sub-therapeutic doses as a pharmacokinetic "booster" (CYP3A4 inhibitor) to increase blood levels of co-administered protease inhibitors (e.g., lopinavir, atazanavir, darunavir) in combination antiretroviral therapy. Its efficacy in HIV/AIDS treatment is well established through decades of clinical use.

SIV protease shares structural homology with HIV-1 protease, and in vitro data (e.g., PMID 12709355) confirm that ritonavir can inhibit SIV replication at nanomolar concentrations, comparable to its activity against HIV-1. This provides a plausible biochemical basis for the TxGNN association.

However, SIV infection is a **non-human primate disease** — it is used exclusively as an animal model to study HIV pathogenesis and to test antiretroviral regimens before human trials, not as an actual human clinical indication. The high TxGNN score most likely reflects the close textual and biological similarity between "SIV" and "HIV" in the knowledge graph rather than a genuine new human therapeutic opportunity. As such, this mechanistic link **cannot be directly translated into a new human indication**, and the evidence pack's own rationale explicitly flags this limitation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro/Animal | Antimicrobial Agents and Chemotherapy | Ritonavir inhibited SIVmac239 in vitro with an EC50 of ~13 nM, comparable to its activity against HIV-1 |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal model | Journal of Virology | Quadruple antiretroviral therapy (including PI) produced rapid viral decay in SIV-infected macaques |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility | Antiviral Therapy | Evaluated susceptibility of HIV-2, SIV and SHIV strains to 16 approved anti-HIV-1 drugs, including ritonavir |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal model | PLoS Pathogens | Intensified multidrug ART induced long-term viral suppression in SIV-infected macaques (simian AIDS model) |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal model | PLoS One | Combination cART plus SAHA studied in SIV-infected Chinese rhesus macaques as a viral reservoir model |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Animal model | Microbes and Infection | Constructed a novel SHIV carrying HIV-1 protease gene as a tool for testing protease inhibitors in vivo |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal model | Journal of Virological Methods | Oral HAART including lopinavir/ritonavir evaluated in SHIV-infected monkeys, assessing CD8 subset impact |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Mechanistic/Animal | mBio | Lentiviral (HIV/SIV-family) brain reservoirs persist despite effective ART in multiple infection models |
| [9875393](https://pubmed.ncbi.nlm.nih.gov/9875393/) | 1998 | In vitro | Antiviral Chemistry & Chemotherapy | Fluoroquinolone derivative active against HIV-1, HIV-2 and SIV, including ritonavir-resistant strains |
| [12186895](https://pubmed.ncbi.nlm.nih.gov/12186895/) | 2002 | Mechanistic | Journal of Virology | Characterized viral protease-dependent processing of HIV-1 Vif protein, relevant to protease inhibitor biology |

---

## Singapore Market Information

Ritonavir currently has no registered product license in Singapore (market status: **Not Marketed**, 0 registrations on file). No authorization or approved-indication data is available from local registry sources.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (SIV infection) targets a non-human primate disease with no clinical trials and only preclinical/mechanistic literature; the evidence pack itself notes this cannot be translated into a human indication. This candidate does not warrant further clinical development at this time.

**To proceed, the following is needed:**
- Ritonavir mechanism-of-action (MOA) data from DrugBank to support proper mechanistic review
- TFDA/local package insert warnings and contraindications (currently a blocking data gap)
- Consideration of alternative, higher-quality candidates already present in this evidence pack — e.g., "AIDS related complex" and "congenital HIV" (both rank L1 evidence with completed Phase 3 trials, decision stage S3, "Proceed with Guardrails") — which represent genuine, clinically supported extensions of ritonavir's antiretroviral use rather than a cross-species artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

