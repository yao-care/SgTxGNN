---
layout: default
title: Mefenamic Acid
parent: 僅模型預測 (L5)
nav_order: 635
evidence_level: L5
indication_count: 10
---

# Mefenamic Acid
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

# Mefenamic Acid: From Analgesic/Anti-Inflammatory Use to Rheumatoid Arthritis

## One-Sentence Summary

Mefenamic acid is a fenamate-class NSAID historically used for pain, primary dysmenorrhea, and inflammatory joint conditions, but it is **not currently registered or marketed in Singapore**. The TxGNN model's top prediction identifies **Rheumatoid Arthritis** as its leading candidate indication, with a **99.73% prediction score**, supported by **20 publications** (including several controlled trials from the 1960s–1980s) but **no currently registered clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in local regulatory data (drug not marketed in Singapore); internationally, mefenamic acid is a classic NSAID historically indicated for mild-to-moderate pain, primary dysmenorrhea, and inflammatory joint disease |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced mechanism of action data is not currently available for this candidate (flagged as a High-severity data gap, DG002). Based on the literature synthesized in this evidence pack, mefenamic acid is a fenamate (anthranilic acid derivative) NSAID that inhibits cyclo-oxygenase (COX), reducing prostaglandin-mediated inflammation and pain — the same mechanism shared by ibuprofen, diclofenac, and indomethacin, drugs it is directly compared against in the trial literature below.

This mechanism is directly relevant to rheumatoid arthritis (RA), a chronic autoimmune joint disease driven substantially by prostaglandin-mediated inflammation. COX inhibition provides symptomatic relief of joint pain, swelling, and morning stiffness, which is why NSAIDs including mefenamic acid have long been used as adjunctive/symptomatic therapy in RA.

It is worth noting transparently that this is not a *novel* mechanistic hypothesis: the literature evidence includes multiple double-blind RCTs from 1966–1979 directly testing mefenamic acid in RA populations, so the model is substantially re-identifying an already well-documented historical use rather than proposing an unprecedented repurposing. Importantly, as an NSAID, mefenamic acid provides **symptomatic relief only** and has **no disease-modifying (DMARD) activity** — a distinction critical to interpreting its relevance against modern RA standard-of-care.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [373989](https://pubmed.ncbi.nlm.nih.gov/373989/) | 1979 | RCT (double-blind crossover) | Current Medical Research and Opinion | In 24 RA patients, mefenamic acid, sulindac, and flurbiprofen were all significantly superior to placebo on pain score, patient assessment, joint tenderness, and morning stiffness |
| [330287](https://pubmed.ncbi.nlm.nih.gov/330287/) | 1977 | RCT | Journal of International Medical Research | Randomized double-blind within-patient study (n=40) found mefenamic acid and ibuprofen had comparable analgesic/anti-inflammatory effect and similar (mostly mild) side effects |
| [796645](https://pubmed.ncbi.nlm.nih.gov/796645/) | 1976 | RCT (double-blind crossover) | The Medical Journal of Australia | Mefenamic acid (1500 mg/day) compared favourably with ibuprofen (1200 mg/day) in RA patients on background salicylate therapy; side effects mild and mostly gastrointestinal |
| [4294443](https://pubmed.ncbi.nlm.nih.gov/4294443/) | 1967 | Clinical Trial | Annals of the Rheumatic Diseases | Early clinical trial establishing efficacy of mefenamic acid in rheumatoid arthritis (abstract not available in source) |
| [5920657](https://pubmed.ncbi.nlm.nih.gov/5920657/) | 1966 | RCT (comparative) | British Medical Journal | Comparative trial of mefenamic acid and flufenamic acid against aspirin and phenylbutazone in RA (abstract not available in source) |
| [6039589](https://pubmed.ncbi.nlm.nih.gov/6039589/) | 1967 | Comparative trial | Annals of the Rheumatic Diseases | Methodological evaluation comparing mefenamic and flufenamic acids with phenylbutazone and aspirin in RA outpatients (abstract not available in source) |
| [10439](https://pubmed.ncbi.nlm.nih.gov/10439/) | 1976 | Comparative study | The Journal of Rheumatology | Single-blind, non-crossover comparison of 10 antirheumatic drugs in 684 RA patients using a daily pain-chart methodology |
| [306128](https://pubmed.ncbi.nlm.nih.gov/306128/) | 1978 | Review | Scottish Medical Journal | Reviews the therapeutic place of mefenamic acid specifically within RA management (abstract not available in source) |
| [29548675](https://pubmed.ncbi.nlm.nih.gov/29548675/) | 2018 | Observational (case-crossover) | The American Journal of Cardiology | Case-crossover study of 5,921 stroke/AMI patients with RA comorbidity evaluating transient cardiovascular risk of selective vs. non-selective NSAIDs |
| [4890710](https://pubmed.ncbi.nlm.nih.gov/4890710/) | 1967 | RCT (double-blind) | Reumatismo | Italian double-blind clinical and biohumoral study of mefenamic acid in RA therapy (preliminary observations; abstract not available in source) |

---

## Singapore Market Information

Mefenamic acid currently has no registered product authorizations in Singapore (0 licenses on file; market status: not marketed).

---

## Safety Considerations

Structured safety data (key warnings, contraindications, and drug-drug interaction database) is not currently available for this candidate — please refer to the package insert for safety information.

**Supplementary note (from literature review):** although not part of the structured safety dataset, the literature evidence collected for this candidate independently documents several class-related adverse effect signals for mefenamic acid, including nephropathy (PMID [3561624](https://pubmed.ncbi.nlm.nih.gov/3561624/)), enteropathy/villous atrophy (PMID [3680546](https://pubmed.ncbi.nlm.nih.gov/3680546/), [29095288](https://pubmed.ncbi.nlm.nih.gov/29095288/)), autoimmune hemolytic anemia (PMID [5676955](https://pubmed.ncbi.nlm.nih.gov/5676955/)), and GI bleeding (PMID [949194](https://pubmed.ncbi.nlm.nih.gov/949194/)). These should be formally verified against an official package insert before any clinical use is considered.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple tier-1 double-blind RCTs from the 1960s–1980s support the historical efficacy of mefenamic acid in rheumatoid arthritis, comparable to ibuprofen and other reference NSAIDs, giving this pairing a reasonably strong evidence base (L1). However, the drug is not currently marketed in Singapore, provides symptomatic relief only (no disease-modifying activity relevant to modern RA standard of care), and a Blocking-severity data gap (DG001: local regulatory warnings/contraindications) currently prevents a full safety evaluation.

**To proceed, the following is needed:**
- Official package insert / regulatory warnings and contraindications data (DG001 — Blocking; required before any Stage 1 safety review)
- Confirmed mechanism of action from DrugBank API (DG002)
- Confirmation of Singapore registration/market-entry pathway, given current "not marketed" status
- Formal DDI database query (current query returned "not found")
- Clinical positioning assessment against modern RA standard-of-care (DMARDs/biologics), since mefenamic acid would at most serve as adjunctive symptomatic therapy, not primary treatment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

