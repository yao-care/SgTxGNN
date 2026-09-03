---
layout: default
title: Posaconazole
parent: 僅模型預測 (L5)
nav_order: 800
evidence_level: L5
indication_count: 10
---

# Posaconazole
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

Using the provided Evidence Pack, here is the evaluation report.

---

# Posaconazole: From Invasive Fungal Infection to Pneumocystosis

## One-Sentence Summary

Posaconazole is a broad-spectrum triazole antifungal, globally used for the prophylaxis and treatment of invasive fungal infections in high-risk and immunocompromised patients (Singapore market registration data is not available for this drug).
The TxGNN model's top-ranked prediction proposes **Pneumocystosis** as a new indication, but this candidate is currently supported only by **2 loosely-related clinical trials** and **no dedicated literature**, and a critical review of the underlying mechanism found the biological rationale does not hold up.
Overall evidentiary support for this specific prediction is weak; a lower-ranked candidate (vulvovaginal candidiasis, see note in Conclusion) shows a more credible mechanistic basis and is worth tracking separately.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Singapore registry data; per global labeling, posaconazole is indicated for prophylaxis/treatment of invasive fungal infections (e.g. invasive aspergillosis, candidiasis) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for posaconazole is not available from the evidence pack (DrugBank MOA field is a data gap). Based on generally known pharmacology, posaconazole is a second-generation triazole antifungal that inhibits fungal CYP51 (lanosterol 14α-demethylase), blocking ergosterol biosynthesis in the fungal cell membrane — the mechanism underlying its efficacy against *Aspergillus*, *Candida*, and other invasive mould/yeast infections in immunocompromised hosts (e.g. hematologic malignancy, stem cell/organ transplant patients).

On the surface, pneumocystosis (caused by *Pneumocystis jirovecii*) might appear mechanistically adjacent, since it is also an opportunistic infection common in the same immunocompromised transplant population where posaconazole is frequently co-prescribed as antifungal prophylaxis. This population overlap is likely what drove the TxGNN model's high prediction score (99.77%, rank 3786).

However, a closer mechanistic review indicates the prediction is **not biologically well-founded**: *Pneumocystis jirovecii* lacks the classic ergosterol-containing membrane structure that azole antifungals target, and its CYP51/lanosterol demethylase pathway is not considered a sensitive target for triazoles. Published literature confirms azole antifungals are not effective against *Pneumocystis*. The two clinical trials identified (below) both involve posaconazole only as a background prophylactic agent in transplant/GVHD settings, not as a direct intervention against pneumocystosis — with the actual anti-*Pneumocystis* coverage in one trial provided by TMP-SMX, not posaconazole. This pattern is consistent with a **co-occurrence confound** in the knowledge graph (posaconazole and PCP-prophylaxis drugs are frequently used together in transplant patients) rather than a genuine causal treatment signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial comparing GVHD prophylaxis regimens after mismatched unrelated donor stem cell transplant; posaconazole, if used, appears only as background antifungal prophylaxis, not as the studied intervention for pneumocystosis. |
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Active, not recruiting | 602 | Rezafungin vs. standard antimicrobial regimen (fluconazole + posaconazole + TMP-SMX) for invasive fungal disease prevention post-transplant; anti-*Pneumocystis* coverage in the comparator arm is provided by TMP-SMX, not posaconazole. |

Both trials are graded **low direct relevance (Grade C)** — posaconazole appears only as a co-administered background agent, not as a tested treatment for pneumocystosis.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Posaconazole currently has no license records in the Singapore regulatory dataset (market status: Not Marketed; 0 registrations).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data for posaconazole are not available in the current evidence pack; a product label/DDI lookup should be completed before proceeding — see Next Steps.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (pneumocystosis) is not supported by a credible mechanistic link, and the only available clinical trial evidence shows posaconazole appearing merely as a co-administered background agent rather than as a direct treatment for pneumocystosis — consistent with a knowledge-graph co-occurrence artifact rather than a true drug-disease signal. No dedicated literature exists for this candidate, and the drug currently has no Singapore market presence to support access.

**Note on other candidates in this evidence pack:** Among the 10 predictions reviewed, rank 2 — **vulvovaginal candidiasis** (TxGNN score 98.9%, Evidence Level L3, decision stage S2, "Research Question") — has a substantially stronger mechanistic rationale (direct CYP51/ergosterol inhibition against *Candida* species, including azole-resistant strains) and 20 supporting *in vitro*/clinical publications. This may be a more productive candidate for further evaluation than the top-ranked pneumocystosis prediction. Ranks 3–10 (leprosy, multibacillary/paucibacillary leprosy, and several congenital/genetic syndromes) show no plausible mechanistic link to an antifungal agent and are assessed as model noise (Evidence Level L5) — no further action recommended for these.

**To proceed, the following is needed:**
- Product label / package insert data (TFDA/HSA equivalent) for posaconazole — currently a **Blocking** data gap that prevents any safety pre-assessment (DG001)
- Confirmed mechanism of action data via DrugBank API — currently a **High** severity data gap affecting mechanistic-relevance analysis (DG002)
- If pursuing the pneumocystosis lead further: a dedicated PubMed/trial search specifically testing posaconazole (not as background prophylaxis) against *Pneumocystis jirovecii*, to confirm whether any direct evidence exists beyond the confounded trials identified here
- Consider re-scoping this evaluation toward the vulvovaginal candidiasis candidate (rank 2), which currently has stronger mechanistic and literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

