---
layout: default
title: Ropinirole
parent: 僅模型預測 (L5)
nav_order: 874
evidence_level: L5
indication_count: 10
---

# Ropinirole
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

Using the drug-repurposing-evaluation-report skill implicit in this task (structured template execution) — proceeding directly per the fixed v5 format, following the rule against guessing beyond what the evidence pack + its embedded literature actually state.

# Ropinirole: From Parkinson's Disease / Restless Legs Syndrome to Attention-Deficit/Hyperactivity Disorder

## One-Sentence Summary

> Ropinirole is a non-ergot dopamine D2/D3 receptor agonist established for Parkinson's Disease and Restless Legs Syndrome (RLS), as reflected in the drug's own supporting literature.
> The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**,
> with **no registered clinical trials** and **8 supporting publications** (mostly case report/review/mechanistic level) currently available.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's Disease / Restless Legs Syndrome (inferred from the drug's own literature evidence; not recorded in Singapore regulatory data as the product is not marketed) |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for ropinirole is not available in this evidence pack (data gap DG002). Based on the drug's own supporting literature, ropinirole is a non-ergot dopamine D2/D3 receptor agonist, with established efficacy in Parkinson's Disease and Restless Legs Syndrome (RLS). Several of the cited papers describe it explicitly as a "dopamine agonist" used alongside pramipexole in Parkinson's Disease management.

RLS and ADHD are known to frequently co-occur, and both have been linked to dysregulated dopaminergic signaling — a relationship reviewed in Cortese et al. (2005) and mechanistically explored via dopamine D4 receptor polymorphisms associated with ADHD (Casadó-Anguera et al., 2021). A pediatric case report (Konofal et al., 2005) directly describes ropinirole improving both RLS and comorbid ADHD symptoms in a child, offering a plausible mechanistic bridge between the drug's established indication and the TxGNN-predicted one.

However, this rationale currently rests on a single case report and narrative reviews rather than controlled clinical evidence. The shared dopaminergic hypothesis is biologically plausible but has not been tested in a dedicated ADHD trial for ropinirole.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15866437](https://pubmed.ncbi.nlm.nih.gov/15866437/) | 2005 | Case Report | Pediatric Neurology | Ropinirole improved both ADHD symptoms and sleep disruption (RLS/PLMS) in a 6-year-old with inadequate response to methylphenidate |
| [16218085](https://pubmed.ncbi.nlm.nih.gov/16218085/) | 2005 | Review | Sleep | Reviews the RLS–ADHD association and discusses shared dopaminergic treatment potential |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Mechanism Study | Pharmacological Research | Dopamine D4 receptor variant (D4.7) heteromerization with α2A adrenoceptor implicated in ADHD; relevant to dopaminergic drug rationale |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue Neurologique | General RLS review; supportive background on dopaminergic pathophysiology relevant to RLS-ADHD overlap |
| [24992083](https://pubmed.ncbi.nlm.nih.gov/24992083/) | 2014 | RCT | Clinical Neuropharmacology | RCT comparing piribedil vs. pramipexole/ropinirole for excessive daytime sleepiness in Parkinson Disease — supports ropinirole's established dopaminergic clinical use, not ADHD-specific |
| [17483695](https://pubmed.ncbi.nlm.nih.gov/17483695/) | 2007 | Animal Study | J Neuropathol Exp Neurol | Iron-deprived A11-lesioned mouse model of RLS involving dopamine/iron systems; mechanistic background only |
| [30950895](https://pubmed.ncbi.nlm.nih.gov/30950895/) | 2019 | Case Report | Cornea | Corneal edema associated with systemic dopaminergic agents; safety signal, not efficacy-related |
| [30460371](https://pubmed.ncbi.nlm.nih.gov/30460371/) | 2019 | Case Report | Acta Dermato-Venereologica | Treatment-induced delusions of infestation with increased brain dopamine levels; safety signal, not ADHD-related |

## Singapore Market Information

Ropinirole is currently **not marketed** in Singapore under this evidence pack (`total_licenses = 0`); no product authorization records are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are currently unavailable — flagged as a blocking data gap requiring TFDA/product label retrieval.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The ADHD prediction is mechanistically plausible (shared dopaminergic pathway, RLS-ADHD comorbidity) but is currently supported only by a single pediatric case report and narrative/mechanistic literature — no clinical trials exist for this indication. Combined with the drug's non-marketed status in Singapore and a blocking gap in core safety/label data, the evidence is insufficient to advance.

**To proceed, the following is needed:**
- Retrieve official product label (warnings, contraindications, DDI) — currently a blocking gap (DG001)
- Obtain confirmed mechanism of action data from DrugBank (DG002)
- Identify or commission a controlled trial (ideally in RLS-comorbid ADHD populations) rather than relying on a single case report
- Assess pediatric-population safety given the only direct supporting evidence is a pediatric case
- Clarify Singapore regulatory pathway status, since the product currently holds no local registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

