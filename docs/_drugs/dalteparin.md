---
layout: default
title: Dalteparin
parent: 僅模型預測 (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
---

# Dalteparin
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

# Dalteparin: From VTE Prevention to Thrombophilia Due to Protein C Deficiency

## One-Sentence Summary

Dalteparin (Fragmin®) is a Low Molecular Weight Heparin (LMWH) anticoagulant, internationally established for the prevention and treatment of venous thromboembolism (VTE) and thromboembolic complications in cancer patients, though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **thrombophilia due to protein C deficiency, autosomal recessive** (prediction score: 99.88%), supported by a strong mechanistic rationale — Dalteparin's antithrombin III-mediated anticoagulation can compensate for the protein C-deficiency-induced hypercoagulable state.
However, this candidate currently has **no dedicated clinical trials or publications** directly addressing this specific indication, placing evidence at **Level L4 (mechanistic rationale only)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; internationally approved for VTE prevention and treatment |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why Is This Prediction Reasonable?

Protein C deficiency (autosomal recessive) eliminates a pivotal natural anticoagulation checkpoint: activated Protein C (aPC) normally degrades Factors Va and VIIIa to suppress thrombin generation. When Protein C is absent or severely reduced, this braking mechanism fails, producing a severe hypercoagulable state that manifests as recurrent, often life-threatening thromboembolism — frequently presenting in neonates with purpura fulminans.

Dalteparin, as an LMWH, exerts its anticoagulant effect primarily through potentiation of Antithrombin III (ATIII), which rapidly inhibits Factor Xa and thrombin. This mechanism operates entirely independently of the Protein C pathway, offering a compensatory anticoagulation route that is theoretically well-suited to Protein C deficiency. While no Dalteparin-specific clinical trials exist for this rare condition, anticoagulants as a drug class — including LMWH, warfarin, and direct oral anticoagulants — are already the established standard of care for Protein C deficiency-associated thrombophilia. This represents a strong "class effect" rationale, and the TxGNN model's high score of 99.88% likely captures this deep mechanistic alignment within the knowledge graph.

Detailed mechanism of action data for Dalteparin is not available in this evidence pack. Based on established pharmacology, Dalteparin is an LMWH whose efficacy in VTE prevention and treatment is well-proven globally; its mechanism is mechanistically applicable to the hypercoagulable state caused by Protein C deficiency. The main evidence gap is the absence of Dalteparin-specific trials — the indication is supported by class-level, not drug-specific, evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for thrombophilia due to protein C deficiency, autosomal recessive.

---

## Literature Evidence

Currently no related literature available for thrombophilia due to protein C deficiency, autosomal recessive.

---

## Singapore Market Information

Dalteparin is **not registered** in Singapore. There are currently **0 product authorizations** in the Singapore regulatory database.

For reference: Dalteparin is marketed internationally as Fragmin® (Pfizer) and is approved in multiple jurisdictions (EU, USA, Japan, Taiwan, etc.) for VTE prevention in surgical patients, treatment of DVT/PE, unstable angina/NSTEMI, and extended VTE prevention in cancer patients.

---

## Safety Considerations

Please refer to the package insert for safety information.

> As Dalteparin is not registered in Singapore and no safety data were available in this evidence pack, clinicians should consult the international Fragmin® prescribing information. Key safety considerations for the LMWH class include: major/minor bleeding risk, heparin-induced thrombocytopenia (HIT/HITT), hyperkalaemia (via aldosterone suppression), and special dose adjustments in renal impairment.

---

## All Predicted Indications — Multi-Candidate Overview

This evidence pack covers 10 TxGNN predictions (candidate ID: TW-DB06779-multi). Summary of all indications:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Key Rationale |
|------|---------|-------------|----------------|----------------|---------------|
| 1 | Thrombophilia (Protein C deficiency, AR) | 99.88% | L4 | Research Question | Strong mechanistic fit; ATIII pathway compensates for protein C deficiency |
| 2 | Primary release disorder of platelets | 99.67% | L5 | **Hold** | Bleeding disorder — anticoagulant would worsen haemorrhagic risk |
| 3 | Pseudo-von Willebrand disease | 99.52% | L5 | **Hold** | Bleeding disorder — GPIb mutation; anticoagulant contraindicated |
| 4 | Atypical HUS (thrombomodulin anomaly) | 99.34% | L5 | Research Question | Potential anti-Xa + anti-complement activity; exploratory only |
| 5 | Neuropathy, painful | 99.19% | **L3** | Research Question | **3 clinical trials identified; strongest evidence in this pack** |
| 6 | Thrombotic thrombocytopenic purpura | 98.09% | L5 | **Hold** | Microangiopathic thrombosis; plasmapheresis is standard; bleeding risk |
| 7 | Retinal telangiectasia | 95.54% | L4 | Research Question | 1 case report; secondary vascular occlusion prevention rationale |
| 8 | Retinal microaneurysm | 95.19% | L5 | **Hold** | Non-thrombotic pathology; no mechanistic basis for anticoagulation |
| 9 | Arteriosclerotic retinopathy | 95.19% | L5 | **Hold** | Atherosclerotic process; LMWH lacks direct mechanistic support |
| 10 | Vertebral artery occlusion | 94.96% | L4 | Research Question | 1 preclinical Dalteparin study; dissection/thrombosis anticoagulation rationale |

---

### Spotlight: Rank 5 — Neuropathy, Painful (L3 — Highest Evidence in This Pack)

Of all 10 predicted indications, **painful neuropathy** (score 99.19%) carries the highest level of supporting evidence, with three clinical trials directly or closely involving Dalteparin in neuropathic/neuro-ischaemic settings:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00445328](https://clinicaltrials.gov/study/NCT00445328) | Phase 4 | Terminated | 84 | Randomised head-to-head: Dalteparin vs. unfractionated heparin for VTE prevention in acutely ill medical patients — only trial directly naming Dalteparin; terminated early (reason unknown, warrants investigation) |
| [NCT00662831](https://clinicaltrials.gov/study/NCT00662831) | Phase 2/3 | Completed | 276 | Double-blind placebo-controlled RCT of Fragmin® (Dalteparin) for chronic neuro-ischaemic foot ulcers in diabetic patients with peripheral neuropathy — primary endpoint ≥50% ulcer surface reduction; 276-patient scale provides meaningful power |
| [NCT00765063](https://clinicaltrials.gov/study/NCT00765063) | Phase 2/3 | Completed | 62 | 6-month open-label extension of NCT00662831 — long-term safety and tolerability of Dalteparin in diabetic neuro-ischaemic foot ulcer patients with peripheral arterial occlusive disease |

**Mechanistic rationale**: Painful neuropathy (particularly diabetic neuropathic pain) involves endoneurial microvascular ischaemia and neuroinflammation. LMWH may act via: (1) improving endoneurial microcirculation through anti-Xa-mediated local anticoagulation, (2) inhibiting heparanase to reduce basement membrane degradation, and (3) anti-inflammatory effects through NF-κB suppression and complement inhibition. The two completed Dalteparin trials in diabetic neuro-ischaemic foot ulcers provide the most directly translatable clinical evidence in this entire pack.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
For the top-ranked indication (Protein C deficiency thrombophilia, rank 1), the mechanistic justification is compelling — LMWH anticoagulants are already the standard of care for this condition as a drug class — but no Dalteparin-specific clinical evidence exists, and the drug is not registered in Singapore. Five of the ten predictions (ranks 2, 3, 6, 8, 9) should be held, as anticoagulant use in these bleeding-prone or mechanistically mismatched conditions would be inappropriate or potentially harmful.

**To proceed with Rank 1 (Protein C deficiency), the following is needed:**
- Mechanism of action data (DrugBank API query for Dalteparin DB06779)
- Singapore/international package insert: key warnings and contraindications
- Systematic review of LMWH class evidence in hereditary Protein C deficiency (rare disease registries: EUCLID, ProC-Registry)
- Singapore regulatory pathway assessment for an unregistered drug
- Consideration of alternative LMWH agents already registered in Singapore (e.g., enoxaparin)

**To proceed with Rank 5 (Painful Neuropathy) — recommended priority:**
- Retrieve full results from NCT00662831 (276-patient completed RCT) and NCT00765063
- Investigate reason for early termination of NCT00445328
- Expand PubMed search with broader terms: "Dalteparin + diabetic neuropathy", "Fragmin + peripheral neuropathy"
- Dose-response data and biomarker endpoints (anti-Xa levels, endoneurial blood flow)
- Safety monitoring plan tailored to diabetic patients (renal function, bleeding risk)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

