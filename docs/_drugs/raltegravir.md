---
layout: default
title: Raltegravir
parent: 僅模型預測 (L5)
nav_order: 840
evidence_level: L5
indication_count: 10
---

# Raltegravir
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

# Raltegravir: From HIV-1 Infection to AIDS-Related Complex (Population Extension)

## One-Sentence Summary

Raltegravir is a first-in-class HIV-1 integrase strand transfer inhibitor, though the evidence pack does not document its original approved indication or mechanism of action in detail (data gap). TxGNN's highest-scoring predictions (ranks 1–3) turned out to be **knowledge-graph artifacts** — species-mismatched or biologically implausible — but two lower-ranked candidates, **AIDS Related Complex** and **congenital HIV infection**, are supported by **>30 clinical trials** and **~30 publications**, though these represent extensions of Raltegravir's already-known HIV use rather than a genuinely new indication.

---

## ⚠️ Important Note on TxGNN Ranking

The two highest-scoring TxGNN predictions in this pack are:
- **Rank 1** — *feline acquired immunodeficiency syndrome* (FIV, a cat disease)
- **Rank 2** — *simian immunodeficiency virus infection* (a nonhuman-primate research model)
- **Rank 3** — a rare pediatric neurodevelopmental disorder with no biological link to integrase inhibition

The pack's own rationale confirms these are **not valid human repurposing candidates**: they arise from embedding similarity to the word "immunodeficiency" (species mismatch) or have zero supporting evidence. Ranks 6–10 (hyperlipidemia, prostate fibroma, breast fibrocystic disease, reproductive neoplasms, Brenner tumor) are similarly unsupported (L5, no trials/literature).

The only candidates with real clinical evidence are **Rank 4 (AIDS related complex, L1)** and **Rank 5 (congenital HIV infection, L1)**. This report focuses on Rank 4 as the primary candidate, since both are essentially extensions of Raltegravir's known HIV indication into special populations (combination regimens, pediatric/pregnant patients) rather than novel disease targets.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap); Raltegravir is publicly known as an approved HIV-1 integrase inhibitor (Isentress®) |
| Predicted New Indication | AIDS Related Complex *(Rank 4 — the highest-scoring clinically credible candidate; Ranks 1–3 excluded as artifacts, see note above)* |
| TxGNN Prediction Score | 96.49% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on publicly available information, Raltegravir is an HIV-1 integrase strand transfer inhibitor (INSTI) — it blocks the enzyme HIV uses to integrate its DNA into the host genome, a mechanism well established in its approved use for HIV-1 infection.

"AIDS Related Complex" and "congenital human immunodeficiency virus" are not distinct diseases from Raltegravir's original use — they are part of the same HIV-1 disease spectrum (symptomatic pre-AIDS states, combination-regimen switching, and mother-to-child transmission/pediatric HIV). The clinical trial evidence therefore reflects population and regimen extensions (treatment-experienced adults, children, pregnant women, combination with other antiretrovirals) rather than a mechanistically novel repurposing hypothesis.

This distinction matters for decision-making: unlike a true repurposing signal (e.g., an antiviral shown effective in an unrelated disease), this candidate confirms known pharmacology in adjacent populations. It is lower-risk scientifically but does not represent a new commercial indication opportunity in the classic drug-repurposing sense.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00485264](https://clinicaltrials.gov/study/NCT00485264) | Phase 1/2 | Completed | 153 | IMPAACT study establishing raltegravir dosing, safety, tolerability, and PK in HIV-1 infected children and adolescents (4 weeks–18 years) |
| [NCT02383355](https://clinicaltrials.gov/study/NCT02383355) | Phase 4 | Completed | 40 | Switching virologically suppressed patients to a raltegravir-based regimen; assessed effects on platelet reactivity and cardiovascular inflammatory markers |
| [NCT01076179](https://clinicaltrials.gov/study/NCT01076179) | N/A | Completed | 502 | Observational study of Kaletra (lopinavir/ritonavir) combined with newer agents including integrase inhibitors such as raltegravir |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25394095](https://pubmed.ncbi.nlm.nih.gov/25394095/) | 2014 | Cohort | J Int AIDS Soc | Raltegravir shown to have a favorable drug-interaction profile, enabling safe co-administration with antineoplastic chemotherapy in HIV-infected cancer patients |
| [37568163](https://pubmed.ncbi.nlm.nih.gov/37568163/) | 2023 | Case Report | AIDS Res Ther | Raltegravir-based regimen used to minimize drug-drug interactions in an HIV-positive heart transplant recipient on immunosuppressive therapy |
| [33886444](https://pubmed.ncbi.nlm.nih.gov/33886444/) | 2022 | Case Report | Acta Clin Belg | Case of concurrent MAC/*Cryptococcus* opportunistic infection in an AIDS patient; illustrates the clinical complexity of the AIDS-related-complex population |
| [25691383](https://pubmed.ncbi.nlm.nih.gov/25691383/) | 2015 | In vitro mechanistic | J Leukoc Biol | Mechanistic study of HIV-1 integration in CD4+ T cells; background pharmacology relevant to integrase-inhibitor class effects |

---

## Singapore Market Information

Raltegravir currently has **no registered market authorizations in Singapore** (market status: 未上市 / Not Marketed; total registrations: 0). No license records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: the evidence pack flags the absence of local regulatory label warnings/contraindications as a **Blocking** data gap — DG001 — meaning this candidate cannot yet undergo initial safety screening (S1) until label data is obtained. No drug-drug interaction data was returned from the DDI query.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only clinically credible candidates (AIDS Related Complex, congenital HIV) are population extensions of Raltegravir's existing HIV-1 indication, not a novel repurposing opportunity — while TxGNN's top-ranked "new indication" predictions are confirmed artifacts (species mismatch, no biological plausibility). Combined with a Blocking safety data gap and zero market presence in Singapore, there is no actionable basis to advance this candidate at this time.

**To proceed, the following is needed:**
- Local regulatory label (warnings, contraindications, DDI) — currently a Blocking data gap
- Confirmed mechanism of action documentation from DrugBank
- Clarification on whether Singapore market entry is planned, since there are currently zero registrations
- If pursuing genuine repurposing (rather than population extension), TxGNN candidates should be re-screened excluding ranks 1–3, 6–10, which show no biological or evidentiary support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

