---
layout: default
title: Prilocaine
parent: 僅模型預測 (L5)
nav_order: 816
evidence_level: L5
indication_count: 10
---

# Prilocaine
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

# Prilocaine: From Local Anesthesia to Postherpetic Neuralgia

## One-Sentence Summary

Prilocaine is an amide-type local anesthetic, best known as one of the two active ingredients (with lidocaine) in EMLA cream, used to numb skin and mucosa before minor procedures. The TxGNN model screened 10 potential new indications for this drug; most (including its top-ranked hit, papillary conjunctivitis) show no mechanistic or clinical support and are flagged in the evidence pack itself as likely knowledge-graph noise. **Neuralgia** — specifically postherpetic neuralgia (PHN) — is the one candidate backed by real evidence: **12 clinical trials** and **20 publications**, including completed RCTs testing lidocaine/prilocaine cream directly in PHN patients.

> **Note on indication selection:** This report focuses on Neuralgia rather than the TxGNN top-ranked prediction (papillary conjunctivitis, score 99.78%), because the evidence pack explicitly scores that and three other top-10 predictions (bipolar disorder, bronchitis, rosacea conjunctivitis) as `L5 / Hold` with "no known mechanistic link — likely graph artifact." Neuralgia is the only candidate reaching `L2` evidence with a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Singapore registry data (drug not independently marketed). Known clinical use per literature: topical/infiltration local anesthesia (e.g., EMLA cream) |
| Predicted New Indication | Neuralgia (postherpetic neuralgia) |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data is not available in the evidence pack (flagged as a Blocking/High-severity data gap). Based on information consistently referenced across the supporting evidence, Prilocaine is an **amide-type local anesthetic** that blocks voltage-gated Na⁺ channels in peripheral sensory neurons, interrupting pain signal transduction at the nerve fiber level. Its principal clinical form is **EMLA cream** (Eutectic Mixture of Local Anesthetics), a 1:1 combination of 2.5% lidocaine and 2.5% prilocaine.

The link between "local anesthesia" and "neuralgia" is not a novel hypothesis — it is a natural extension of existing peripheral-analgesic use. EMLA cream is already used clinically as a topical desensitizing agent prior to painful dermatologic and neurologic procedures, and multiple published studies test it directly for PHN pain relief and as a pretreatment before capsaicin 8% patch application (a standard PHN therapy) to improve procedural tolerability. In this sense, the TxGNN prediction is best understood as identifying an **established off-label/adjunct use** rather than an unexplored mechanistic hypothesis, which is consistent with the L2 evidence grade.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00916942](https://clinicaltrials.gov/study/NCT00916942) | Phase 2 | Completed | 20 | Open-label study of topical lidocaine (2.5%)/prilocaine (2.5%) cream as pre-treatment before NGX-4010 capsaicin patch in postherpetic neuralgia patients — direct evidence of prilocaine's tolerability role in PHN management |
| [NCT01540877](https://clinicaltrials.gov/study/NCT01540877) | N/A | Completed | 28 | Human experimental model combining capsaicin sensitization with local anesthetic C-fiber block to characterize neuropathic pain mechanisms |
| [NCT03220113](https://clinicaltrials.gov/study/NCT03220113) | Phase 1/2 | Unknown | 100 | De-Novo algorithm combining dexamethasone, lidocaine, and thiamine injected into trigeminal/occipital nerve branches for chronic craniofacial neuralgia |
| [NCT06247592](https://clinicaltrials.gov/study/NCT06247592) | N/A | Unknown | 70 | Explicitly uses 2% prilocaine for greater occipital nerve blockade, compared against pulse radiofrequency, in chronic migraine/neuralgia-adjacent pain |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2493878](https://pubmed.ncbi.nlm.nih.gov/2493878/) | 1989 | RCT | BMJ | Lignocaine-prilocaine cream evaluated for postherpetic neuralgia pain relief |
| [2616182](https://pubmed.ncbi.nlm.nih.gov/2616182/) | 1989 | RCT | Pain | EMLA cream (5-10g, 24h application) significantly improved pain intensity scores at 6h in 12 PHN patients, including facial PHN subgroup |
| [22182397](https://pubmed.ncbi.nlm.nih.gov/22182397/) | 2011 | RCT | BMC Anesthesiology | Lidocaine 2.5%/prilocaine 2.5% cream pretreatment improved tolerability of capsaicin 8% dermal patch (NGX-4010) in PHN patients |
| [1430539](https://pubmed.ncbi.nlm.nih.gov/1430539/) | 1992 | Review | J Dermatol Surg Oncol | Reviews EMLA (2.5% lidocaine/2.5% prilocaine) as safe, effective topical analgesic, with postherpetic neuralgia cited as an indication |
| [23314014](https://pubmed.ncbi.nlm.nih.gov/23314014/) | 2013 | Review | Curr Opin Support Palliat Care | Evidence-based review of persistent wound-related pain management, including topical anesthetic approaches |
| [10353509](https://pubmed.ncbi.nlm.nih.gov/10353509/) | 1999 | Cohort | Pain | Single and repeated EMLA applications reduced spontaneous and evoked pain in 11 PHN patients |
| [12378018](https://pubmed.ncbi.nlm.nih.gov/12378018/) | 2002 | Cohort | J Korean Med Sci | Identifies prognostic factors for PHN development and discusses treatment options including topical anesthetics |
| [8695081](https://pubmed.ncbi.nlm.nih.gov/8695081/) | 1996 | Case Report | J Clin Anesth | EMLA cream successfully treated PHN resistant to other therapies |
| [2046584](https://pubmed.ncbi.nlm.nih.gov/2046584/) | 1991 | Case Report | Med J Aust | EMLA cream application in herpetic neuralgia |
| [1875823](https://pubmed.ncbi.nlm.nih.gov/1875823/) | 1991 | Case Report | Med J Aust | EMLA cream in herpetic neuralgia (correspondence) |

---

## Singapore Market Information

Prilocaine has **0 registered products** in the Singapore regulatory dataset used for this evaluation (`market_status: 未上市`). No authorization records, product names, or approved-indication text are available. If this candidate advances, formal HSA registration status and label text must be independently confirmed before further evaluation.

---

## Safety Considerations

Please refer to the package insert for safety information — no `key_warnings`, `contraindications`, or `DDI` data are currently available in the evidence pack (all fields flagged `[Data Gap]`, DDI query returned `not_found`).

**Note for decision-makers:** although not part of the structured safety data, the literature evidence for a related candidate (atopic eczema, rank 7) surfaced notable safety signals for this drug class worth flagging for the S1 safety review — including case reports of **methemoglobinemia and seizures** after topical lidocaine/prilocaine application in a child with barrier-compromised skin, and **contact allergy/purpura** reactions. These should be explicitly addressed once TFDA-equivalent label data (DG001) is obtained.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Neuralgia (postherpetic neuralgia) is supported by a completed Phase 2 trial (NCT00916942) and multiple published RCTs/cohort studies showing lidocaine/prilocaine cream provides measurable pain relief in PHN, and the mechanistic link (peripheral Na⁺ channel blockade) is well established and consistent with prilocaine's existing use. However, all supporting evidence pairs prilocaine with lidocaine (as EMLA), not prilocaine alone, so single-agent efficacy is not directly demonstrated.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official label warnings/contraindications before any S1 safety sign-off
- Resolve DG002 (High): confirm formal MOA documentation via DrugBank API
- Clarify whether the therapeutic signal applies to prilocaine as monotherapy or only in fixed combination with lidocaine
- Confirm Singapore registration pathway status, since the drug currently has zero local market presence
- Independently verify known class-level safety signals (methemoglobinemia, seizure risk in barrier-compromised skin, contact allergy) noted in adjacent literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

