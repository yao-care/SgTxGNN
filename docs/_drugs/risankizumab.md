---
layout: default
title: Risankizumab
parent: 僅模型預測 (L5)
nav_order: 864
evidence_level: L5
indication_count: 10
---

# Risankizumab
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

# Risankizumab: From Plaque Psoriasis to Dermatitis

## One-Sentence Summary

Risankizumab is an IL-23p19-targeting monoclonal antibody globally approved for plaque psoriasis, psoriatic arthritis, generalized pustular psoriasis, erythrodermic psoriasis and Crohn's disease, but it is **not currently registered in Singapore**. The TxGNN model predicts effectiveness for the broad category **"Dermatitis"** (score 99.98%), supported by **7 clinical trials** and **16 publications**; however, this bucket mixes an already-approved label (psoriasis) with a hypothesis that **failed** its pivotal Phase 2 trial (atopic dermatitis), so the two must be evaluated separately.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore (0 licenses); globally approved for Plaque Psoriasis, Psoriatic Arthritis, Generalized Pustular/Erythrodermic Psoriasis, Crohn's Disease (per PMID 31098898) |
| Predicted New Indication | Dermatitis (spans psoriasis-spectrum disease + atopic dermatitis — see below) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available in this evidence pack (data gap DG002). Based on published literature (PMID 31098898), Risankizumab is a humanised IgG monoclonal antibody targeting the p19 subunit of interleukin-23 (IL-23), first globally approved in Japan (2019) for psoriasis vulgaris, psoriatic arthritis, generalised pustular psoriasis and erythrodermic psoriasis, and subsequently approved elsewhere (including Crohn's disease) — but it has no Singapore licence to date.

The TxGNN model groups the predicted indication under the broad label **"dermatitis,"** which in fact spans two clinically distinct entities that require separate evaluation:

1. **Plaque psoriasis and its variants (genital, scalp, erythrodermic)** — IL-23/Th17-axis-driven inflammatory skin disease that matches Risankizumab's core mechanism directly. This is already the drug's approved global indication, so the "new indication" signal here mainly reflects an evidence-completion opportunity for the Singapore market rather than a genuinely novel repurposing hypothesis (Phase 4 head-to-head and RCT evidence: NCT04908475, NCT05969223).
2. **Atopic dermatitis (AD)** — primarily Th2-driven. A mechanistic crossover hypothesis (IL-23→Th17/Th22) motivated testing, but the completed Phase 2 RCT (NCT03706040 / PMID 36588137) **did not demonstrate significant benefit over placebo**. This sub-indication should be treated as a **falsified hypothesis**, not supportive evidence.

Because "dermatitis" bundles a de-facto label-expansion candidate (psoriasis) with a disproven hypothesis (AD), guardrail design must explicitly disaggregate the two.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04908475](https://clinicaltrials.gov/study/NCT04908475) | Phase 4 | Completed | 352 | Head-to-head vs apremilast in moderate plaque psoriasis; directly supports existing psoriasis label (Grade A) |
| [NCT05969223](https://clinicaltrials.gov/study/NCT05969223) | Phase 4 | Completed | 214 | Randomized double-blind trial in moderate-to-severe genital/scalp psoriasis (Grade A) |
| [NCT04818385](https://clinicaltrials.gov/study/NCT04818385) | N/A | Completed | 240 | Taiwan real-world observational cohort; PASI90 durability vs other biologics (Grade B, real-world evidence) |
| [NCT03706040](https://clinicaltrials.gov/study/NCT03706040) | Phase 2 | Completed | 172 | Randomized placebo-controlled trial in moderate-to-severe atopic dermatitis — **did not meet efficacy endpoint** (Grade B, negative result) |
| [NCT07021495](https://clinicaltrials.gov/study/NCT07021495) | N/A | Recruiting | 840 | Observational biomarker profiling across 6 immune-mediated inflammatory skin diseases incl. AD/psoriasis (Grade C, mechanistic) |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A | Completed | 1000 | Pharmacogenetic study of biologic drug survival in cutaneous psoriasis (Grade C, indirect) |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | Not yet recruiting | 10 | Microdevice drug-delivery testing platform for AD/psoriasis; not an efficacy trial (Grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36588137](https://pubmed.ncbi.nlm.nih.gov/36588137/) | 2023 | RCT | Dermatology and Therapy | Phase 2 RCT in moderate-to-severe atopic dermatitis — **negative result**, no significant benefit over placebo |
| [31098898](https://pubmed.ncbi.nlm.nih.gov/31098898/) | 2019 | Review | Drugs | "First Global Approval" review — defines MOA (IL-23p19 mAb) and approved indications (psoriasis, PsA, GPP, EP) |
| [40794374](https://pubmed.ncbi.nlm.nih.gov/40794374/) | 2025 | Systematic Review | Inflammopharmacology | Role of IL inhibitors in lichen planus, including therapeutic and paradoxical effects |
| [39201826](https://pubmed.ncbi.nlm.nih.gov/39201826/) | 2024 | Review | Children (Basel) | Narrative review of biologics for pediatric alopecia areata, psoriasis, AD, HS |
| [33078990](https://pubmed.ncbi.nlm.nih.gov/33078990/) | 2020 | Review | Expert Opin Biol Ther | Current/emerging biologics for pediatric atopic dermatitis |
| [40856907](https://pubmed.ncbi.nlm.nih.gov/40856907/) | 2025 | Systematic Review | Am J Clin Dermatol | Management of erythrodermic psoriasis with systemic therapies |
| [39668419](https://pubmed.ncbi.nlm.nih.gov/39668419/) | 2025 | Cohort | Int J Dermatol | Combined dupilumab + risankizumab in patients with concomitant AD and psoriasis |
| [40071317](https://pubmed.ncbi.nlm.nih.gov/40071317/) | 2025 | Cohort | Experimental Dermatology | Clinical experience of risankizumab in patients with history of erythrodermic psoriasis |
| [37381703](https://pubmed.ncbi.nlm.nih.gov/37381703/) | 2023 | Case Report | J Dermatolog Treat | Acrodermatitis continua of Hallopeau successfully treated with risankizumab |
| [33368238](https://pubmed.ncbi.nlm.nih.gov/33368238/) | 2021 | Case Report | Int J Dermatol | Acrodermatitis continua Hallopeau successfully treated by risankizumab |

---

## Singapore Market Information

Risankizumab currently holds **no licence in Singapore** (0 registrations, market status: Not Marketed). No local authorization number, product name, or approved indication text is available for extraction.

---

## Safety Considerations

Formal local safety data (structured warnings, contraindications, drug interactions) is not yet available for Risankizumab in this evidence pack (data gap DG001, classified **Blocking** — must be resolved before S1 safety screening). Please refer to the manufacturer's package insert once available.

**Literature-Reported Safety Signal**: Multiple case reports (PMID 41645692, 36939506, 33185530, 37014149, 33185535, 38607726) describe **paradoxical eczematous eruptions** occurring during treatment with Risankizumab and other IL-23 inhibitors in psoriasis patients, with an estimated incidence of 1–3%. This signal is particularly relevant given that the predicted indication under evaluation is itself "dermatitis," and should be weighed in any risk-benefit assessment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The **psoriasis-spectrum** portion of the "dermatitis" prediction is well-supported by completed Phase 4 RCTs (NCT04908475, NCT05969223) and real-world cohort data (NCT04818385), and essentially reflects Risankizumab's existing global label rather than a novel hypothesis — justifying a guardrailed proceed for Singapore registration/label-expansion purposes.
- The **atopic dermatitis** sub-indication should be explicitly excluded from this pathway: its pivotal Phase 2 RCT (NCT03706040 / PMID 36588137) was negative, and no further clinical development should be assumed without new evidence.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001 — obtain TFDA/local-equivalent package insert warnings and contraindications before any S1 safety evaluation
- Complete structured MOA data (DG002) from DrugBank API
- Confirm Singapore registration pathway, since the drug currently has zero local licences
- Disaggregate the TxGNN "dermatitis" bucket into psoriasis-spectrum (proceed) vs. atopic dermatitis (hold/exclude) in any downstream indication-specific dossier
- Note: ranks 2–10 in this evidence pack (e.g., neonatal dermatomyositis, amyopathic dermatomyositis, acrodermatitis chronica atrophicans, etc.) are all Evidence Level L5 with no clinical trial or literature support — model-prediction only — and are recommended **Hold** with no further action at this stage.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

