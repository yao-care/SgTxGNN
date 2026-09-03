---
layout: default
title: Rupatadine
parent: 僅模型預測 (L5)
nav_order: 879
evidence_level: L5
indication_count: 10
---

# Rupatadine
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

# Rupatadine: From Allergic Rhinitis/Chronic Urticaria to Cold Urticaria

## One-Sentence Summary

Rupatadine is a second-generation antihistamine with dual H1-receptor and platelet-activating factor (PAF) antagonist activity, historically used for allergic rhinitis and chronic urticaria (based on literature, as no structured original-indication data was available for this dataset). The TxGNN model predicts it may also be effective for **Cold Urticaria** (cold contact urticaria), a physical/inducible urticaria subtype, with **1 completed Phase 2 RCT** and **8 supporting publications**, including a dedicated randomized controlled trial.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Singapore regulatory data (drug not locally registered); literature indicates allergic rhinitis and chronic urticaria as established global uses |
| Predicted New Indication | Cold Urticaria (Cold Contact Urticaria) |
| TxGNN Prediction Score | 96.97% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data (`original_moa`) is currently a data gap for this drug. However, the supporting literature consistently describes rupatadine as a second-generation, non-sedating H1-antihistamine that also has clinically relevant antagonist activity against platelet-activating factor (PAF) — a dual mechanism distinguishing it from most other antihistamines (PMID 23806068, 25491409).

Cold urticaria (cold contact urticaria) is a mast-cell-mediated physical urticaria in which cold exposure triggers local release of histamine and PAF, producing wheals and pruritus. Since rupatadine's core pharmacology directly targets both of these mediators, the mechanistic rationale for efficacy in cold urticaria is stronger than for a typical "off-target" repurposing candidate — it extends the drug's known antihistamine/anti-PAF activity to a related, mechanistically congruent urticaria subtype rather than an unrelated disease area.

This is reinforced by a dedicated Phase 2 randomized, double-blind, three-way crossover, placebo-controlled trial (NCT01605487) specifically designed to test rupatadine 20 mg and 40 mg in cold contact urticaria using a standardized cold-provocation device (TempTest®), along with a separate published RCT (PMID 26038847) replicating the up-dosing efficacy signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01605487](https://clinicaltrials.gov/study/NCT01605487) | Phase 2 | Completed | 24 | Double-blind, three-way crossover, placebo-controlled trial evaluating rupatadine 20 mg and 40 mg for cold contact urticaria using a standardized Peltier-based cold-provocation device (TempTest®) to determine symptom and temperature/stimulation-time thresholds |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26038847](https://pubmed.ncbi.nlm.nih.gov/26038847/) | 2016 | RCT | Acta Dermato-Venereologica | Two-centre, randomized, double-blind, 3-way crossover, placebo-controlled study confirming rupatadine 20 mg and 40 mg are effective in reducing symptoms of chronic cold urticaria |
| [20143651](https://pubmed.ncbi.nlm.nih.gov/20143651/) | 2010 | Clinical Trial | Ann Allergy Asthma Immunol | Rupatadine improved symptom control, stimulation time, and temperature thresholds in patients with acquired cold urticaria |
| [30708143](https://pubmed.ncbi.nlm.nih.gov/30708143/) | 2019 | Cohort/Mechanistic Study | J Allergy Clin Immunol Pract | Examined H1-antihistamine inhibition of histamine/codeine-induced wheals and its (lack of) predictive value for treatment response in chronic cold urticaria |
| [24977664](https://pubmed.ncbi.nlm.nih.gov/24977664/) | 2015 | Prospective Cohort | Acta Dermato-Venereologica | One-year prospective study defining temperature thresholds as a tool to assess clinical course of acquired cold contact urticaria |
| [23806068](https://pubmed.ncbi.nlm.nih.gov/23806068/) | 2013 | Review | Expert Opin Pharmacother | Overview of rupatadine's dual H1/PAF antagonist activity, rapid onset, and long-lasting effect in urticaria treatment |
| [25491409](https://pubmed.ncbi.nlm.nih.gov/25491409/) | 2015 | Review | Allergy | Update on rupatadine's broadened mechanism of action involving PAF beyond classic H1-antihistamine effects |
| [41424665](https://pubmed.ncbi.nlm.nih.gov/41424665/) | 2025 | Review | Drugs in Context | Case series review of off-label rupatadine use across allergic and skin disorders, leveraging its antihistamine and anti-PAF effects |
| [19392988](https://pubmed.ncbi.nlm.nih.gov/19392988/) | 2009 | Case Series | Allergy | Early case series reporting treatment of acquired cold urticaria with rupatadine |

---

## Singapore Market Information

Rupatadine is **not currently registered or marketed in Singapore** — the regulatory data pack shows 0 licenses on file. As a result, no product listings, dosage forms, or approved indication text are available for the Singapore market at this time.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are not currently available in the structured dataset for this drug — flagged as a blocking data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A dedicated completed Phase 2 RCT plus a corroborating published RCT and mechanistic cohort studies support rupatadine's efficacy in cold urticaria, and the dual H1/PAF antagonist mechanism is pharmacologically coherent with this disease's pathophysiology. However, the pivotal trial had a small sample size (n=24), and the drug is not currently registered in Singapore, warranting a guarded, phased approach rather than immediate full endorsement.

**To proceed, the following is needed:**
- TFDA/HSA package insert data — warnings and contraindications (data gap DG001, blocking; required before any S1 safety assessment can proceed)
- Confirmed detailed mechanism-of-action data from DrugBank (data gap DG002)
- A Singapore market-entry/registration pathway assessment, since the drug currently has zero local licenses
- Larger confirmatory trials in the cold urticaria population to strengthen the evidence base beyond the existing n=24 study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

