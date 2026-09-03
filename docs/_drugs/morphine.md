---
layout: default
title: Morphine
parent: 僅模型預測 (L5)
nav_order: 681
evidence_level: L5
indication_count: 10
---

# Morphine
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

# Morphine: From Moderate-to-Severe Pain to Myofascial Pain Syndrome

## One-Sentence Summary

> Morphine is a potent opioid analgesic (μ-opioid receptor agonist), originally used for the management of moderate to severe pain.
> The TxGNN model predicts it may also be effective for **Myofascial Pain Syndrome**,
> with **33 clinical trials** and **17 publications** currently supporting this direction, including a 2026 randomized controlled trial directly testing morphine for myofascial infiltration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate to severe acute and chronic pain (opioid analgesic) — no Singapore-specific approved indication text is available because the drug is not locally registered |
| Predicted New Indication | Myofascial Pain Syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available in this evidence pack. Based on well-established pharmacology, Morphine is the prototypical opioid analgesic — a full μ-opioid receptor agonist that suppresses nociceptive transmission at both spinal and supraspinal levels. Its efficacy in moderate-to-severe pain is long established, and mechanistically this analgesic action is not disease-specific, so extension to other pain-driven conditions is biologically plausible.

Myofascial Pain Syndrome (MPS) is characterized by localized and referred pain arising from muscle trigger points. Because morphine's core pharmacology acts on the same central and peripheral nociceptive pathways implicated in MPS, its use here represents an extension of existing analgesic pharmacology rather than a novel mechanism. Importantly, this is not a purely theoretical extrapolation: a 2026 double-blind randomized controlled trial (PMID 41664327) directly compared morphine (combined with dexmedetomidine) against plain local anesthetic for myofascial infiltration in spinal fusion surgery, providing direct clinical evidence rather than only mechanistic inference.

Supporting literature also documents opioid use in related myofascial and myofascial-adjacent conditions — temporomandibular joint (TMJ) myofascial pain, cervical myofascial pain, and myofascial pelvic pain — reinforcing that opioids, including morphine, are already used in clinical practice as adjuncts for regional/local myofascial pain management, even though this is not yet a formally labeled indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07413770](https://clinicaltrials.gov/study/NCT07413770) | NA | Recruiting | 60 | Evaluates classical massage vs. combined massage + physiotherapy for pain, muscle sensitivity, and function in myofascial pain syndrome |
| [NCT05478928](https://clinicaltrials.gov/study/NCT05478928) | NA | Unknown | 60 | Compares invasive techniques (percutaneous microelectrolysis vs. dry needling) for myofascial trigger points, using pressure pain threshold (algometry) |
| [NCT04640896](https://clinicaltrials.gov/study/NCT04640896) | Phase 4 | Recruiting | 60 | Trigger point injections vs. traditional therapy for post-surgical cervical myofascial pain after anterior cervical spine surgery |
| [NCT06955923](https://clinicaltrials.gov/study/NCT06955923) | Phase 2 | Completed | 11 | Trigger point injections vs. sham after total knee arthroplasty; notes high correlation between surgical soft-tissue manipulation and myofascial pain syndrome |
| [NCT03944889](https://clinicaltrials.gov/study/NCT03944889) | Early Phase 1 | Completed | 20 | Capsaicin-induced muscle sensitization model used to study central sensitization, a mechanism closely linked to myofascial pain syndrome |
| [NCT04831346](https://clinicaltrials.gov/study/NCT04831346) | NA | Recruiting | 100 | Low-level laser therapy vs. soft occlusive splints for pain and EMG activity in temporomandibular disorders (myofascial-related) |
| [NCT03813485](https://clinicaltrials.gov/study/NCT03813485) | NA | Unknown | 24 | EMG comparison of dry needling in latent myofascial trigger points of the trapezius |
| [NCT04684784](https://clinicaltrials.gov/study/NCT04684784) | NA | Completed | 46 | Effect of dry needling on surface EMG activity at latent trigger points of the upper trapezius |
| [NCT01878019](https://clinicaltrials.gov/study/NCT01878019) | N/A | Completed | 92 | Uses naloxone (an opioid antagonist related to morphine's mechanism) to probe brain pain-response differences in chronic pain patients |
| [NCT00456898](https://clinicaltrials.gov/study/NCT00456898) | Phase 1 | Completed | 40 | Crossover PK study on codeine-to-morphine biotransformation via CYP2D6; limited direct relevance, included for opioid pharmacology context |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41664327](https://pubmed.ncbi.nlm.nih.gov/41664327/) | 2026 | RCT | Asian Spine Journal | Double-blind RCT comparing dexmedetomidine+morphine vs. plain ropivacaine for myofascial infiltration in thoracolumbar spinal fusion |
| [20390305](https://pubmed.ncbi.nlm.nih.gov/20390305/) | 2010 | Cohort | Schmerz | Altered pain thresholds during/after opioid withdrawal in chronic low back pain patients under long-term opioid therapy |
| [35066974](https://pubmed.ncbi.nlm.nih.gov/35066974/) | 2022 | Retrospective Cohort | Pain Practice | Structured stretching exercise program improves myofascial pain resolution and reduces opioid usage in "legacy pain" patients |
| [22648287](https://pubmed.ncbi.nlm.nih.gov/22648287/) | 2012 | Study | Journal of Anesthesia | Cervical facet joint injections added to multimodal treatment for long-standing cervical myofascial pain syndrome |
| [39793344](https://pubmed.ncbi.nlm.nih.gov/39793344/) | 2025 | Study | Eur J Obstet Gynecol Reprod Biol | Pudendal nerve block combined with botulinum toxin injection for myofascial pelvic pain |
| [21419546](https://pubmed.ncbi.nlm.nih.gov/21419546/) | 2011 | Review | J Oral Maxillofac Surg | Reviews long-term opioid use for chronic temporomandibular joint (myofascial-related) pain |
| [16713811](https://pubmed.ncbi.nlm.nih.gov/16713811/) | 2006 | Study | J Oral Maxillofac Surg | TMJ arthrocentesis followed by intra-articular morphine infusion for refractory TMJ pain |
| [17870625](https://pubmed.ncbi.nlm.nih.gov/17870625/) | 2008 | RCT | European Journal of Pain | Compares epidural (morphine-based) analgesia vs. intercostal cryoanalgesia for post-thoracotomy pain control |
| [9214190](https://pubmed.ncbi.nlm.nih.gov/9214190/) | 1997 | Study | Zhurnal Nevrologii i Psikhiatrii | Combined analgesic (caffetin) shown effective for acute cervicalgia and lumbar ischialgia, with muscle relaxation effects |
| [6398047](https://pubmed.ncbi.nlm.nih.gov/6398047/) | 1984 | Study | Australian Dental Journal | Analgesic/antihistamine combination evaluated for TMJ pain-dysfunction syndrome |

---

## Singapore Market Information

Morphine currently holds **no marketing authorization in Singapore** under the regulatory data reviewed (0 registrations, market status: not marketed). No product license records are available to summarize in table form.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A directly relevant 2026 RCT plus a body of supportive literature and trials on opioids in TMJ/cervical/pelvic myofascial pain give this prediction real (L3) clinical grounding rather than pure model inference — but morphine's high dependence/abuse potential and the complete absence of structured safety data (warnings, contraindications, DDI) mean this candidate cannot yet move forward without guardrails.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (currently a Blocking data gap — required before any S1 safety screening)
- Structured mechanism-of-action data from DrugBank (High-priority gap affecting mechanistic-relevance analysis)
- Drug-drug interaction profile (DDI query currently returns no data)
- Clarification of Singapore/regional regulatory pathway, since morphine is not currently marketed locally
- A defined route-of-administration and dosing protocol specific to myofascial pain use (e.g., local/regional infiltration vs. systemic), given the opioid abuse/respiratory-depression risk profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

