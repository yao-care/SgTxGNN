---
layout: default
title: Eperisone
parent: 僅模型預測 (L5)
nav_order: 378
evidence_level: L5
indication_count: 10
---

# Eperisone
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

# Eperisone: From Muscle Spasm to Osteoarthritis

## One-Sentence Summary

Eperisone is a centrally acting muscle relaxant, widely used in Asia for the management of painful muscle spasm associated with cervical spondylosis, lumbar pain, and post-operative conditions.
The TxGNN model predicts it may be effective for **Osteoarthritis**, with **0 clinical trials** registered but **5 publications** currently supporting this direction.
The mechanistic rationale is biologically plausible, supported by two small RCTs, placing this at evidence level **L2**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Muscle spasm / Spasticity (cervical spondylosis, lumbar pain) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 94.35% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Eperisone is a centrally acting muscle relaxant that works through two complementary mechanisms: (1) blocking Na⁺ channels to inhibit monosynaptic spinal reflexes and reduce muscle tone, and (2) causing peripheral vasodilation to improve local blood flow and relieve muscle ischemia. These dual actions distinguish it from purely sedating muscle relaxants such as benzodiazepines.

In osteoarthritis (OA), particularly of the knee and hip, periarticular muscle spasm and protective muscle guarding are major contributors to functional limitation and pain amplification. This is mechanistically distinct from — and complementary to — the anti-inflammatory action of NSAIDs. The rationale is not that Eperisone treats the cartilage degeneration of OA directly, but that it addresses the secondary neuromuscular component that NSAIDs cannot. This forms a rational basis for combination therapy.

The evidence base bears this out: published RCTs have directly tested Eperisone as an add-on to NSAIDs in knee OA, and its use in post-total knee arthroplasty (TKA) recovery has also been evaluated. The TxGNN prediction is therefore grounded in clinical reality rather than being a spurious graph-topology artefact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered on ClinicalTrials.gov or ICTRP for Eperisone + Osteoarthritis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24194981](https://pubmed.ncbi.nlm.nih.gov/24194981/) | 2013 | RCT | Pain Research and Treatment | Prospective, randomised, open-label study (n=60); etodolac alone vs. etodolac + eperisone 50 mg TID for 8 weeks in knee OA. Assessed efficacy and tolerability. |
| [41063709](https://pubmed.ncbi.nlm.nih.gov/41063709/) | 2025 | RCT/Cohort | Journal of Drug Targeting | Examined glucosamine hydrochloride + eperisone combined with exercise therapy vs. controls in knee OA patients; measured inflammatory markers (e.g. IL-6, TNF-α) and knee joint function outcomes. |
| [23561916](https://pubmed.ncbi.nlm.nih.gov/23561916/) | 2013 | Cohort | The Journal of Arthroplasty | RCT (n=150, 1:1:1); muscle relaxants + celecoxib vs. muscle relaxants alone vs. placebo for 2 weeks post-TKA. Primary endpoint: VAS pain score; secondary: ROM, morphine consumption, blood loss. |
| [27989618](https://pubmed.ncbi.nlm.nih.gov/27989618/) | 2017 | PK Study | Clinical Therapeutics | Randomised crossover PK interaction study between pelubiprofen (a novel NSAID) and eperisone hydrochloride in healthy Korean men; supports the rationale for co-administration in musculoskeletal pain. |
| [35535532](https://pubmed.ncbi.nlm.nih.gov/35535532/) | 2022 | Observational | China Journal of Orthopaedics and Traumatology | Clinical observation of chiropractic manipulation in degenerative scoliosis; eperisone used as adjunct. Indirect relevance to degenerative musculoskeletal conditions. |

---

## Singapore Market Information

Eperisone (DB08992) currently has **no registered products** in Singapore. No authorisation records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Formal safety data (key warnings, contraindications, drug-drug interactions) was not retrievable from the queried sources at the time of this report. The DDI database query returned no interactions on record. Clinical teams should consult the originator SmPC/PIL and local pharmacovigilance resources before any clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two small RCTs have directly tested Eperisone in knee OA as adjunct to NSAID therapy, with a mechanistically sound rationale (neuromuscular spasm relief complementing NSAID anti-inflammation); however, the evidence base is limited in scale and methodological rigour, and the drug is not currently registered in Singapore.

**To proceed, the following is needed:**

- **Regulatory pathway**: File for HSA registration or seek Named Patient / Special Access route before any Singapore clinical use, as the drug is currently not marketed.
- **Full safety dossier**: Obtain and review the originator package insert (SmPC or equivalent) to document contraindications, key warnings, and known adverse effects — currently a blocking data gap.
- **Mechanism of action documentation**: Retrieve formal DrugBank MOA data (DB08992) to strengthen mechanistic justification for the regulatory dossier.
- **Larger RCT evidence**: Conduct or identify a powered, double-blind RCT specifically evaluating Eperisone vs. placebo as NSAID add-on in OA (existing studies are small, open-label, or short-duration).
- **Pharmacokinetic interaction review**: Clarify DDI profile with commonly co-prescribed OA medications (e.g. celecoxib, diclofenac, opioids) given the absence of interaction data in the current search.
- **Subgroup analysis**: Evaluate which OA subtype (knee, hip, hand) and severity stage benefits most, given that the current literature focuses exclusively on knee OA.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

