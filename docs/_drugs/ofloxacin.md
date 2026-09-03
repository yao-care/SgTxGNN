---
layout: default
title: Ofloxacin
parent: 僅模型預測 (L5)
nav_order: 725
evidence_level: L5
indication_count: 10
---

# Ofloxacin
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

# Ofloxacin: From Bacterial Infections to Septicemic Plague

## One-Sentence Summary

Ofloxacin is a broad-spectrum fluoroquinolone antibiotic. Among the 10 candidate indications TxGNN generated for this drug, most (ranks 1–5, 9) are unsupported high-score statistical artifacts with no mechanistic or literature basis, but **septicemic plague** stands out with a coherent class-effect mechanism and **20 supporting publications**, making it the only candidate in this evidence pack that reaches an actionable "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (fluoroquinolone antibiotic class) — no Singapore license/indication text available in this evidence pack |
| Predicted New Indication | Septicemic Plague |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ofloxacin is not available in this evidence pack (marked as Data Gap). Based on known pharmacology, ofloxacin is a fluoroquinolone antibiotic that inhibits bacterial DNA gyrase and topoisomerase IV, blocking DNA replication in susceptible organisms. This class-level mechanism is directly applicable to *Yersinia pestis*, the causative agent of plague.

The evidence pack's own rationale for this candidate notes that same-class fluoroquinolones — ciprofloxacin and levofloxacin — have already been approved by the US FDA for treatment and post-exposure prophylaxis of plague via the Animal Rule pathway (since human efficacy trials are not ethically feasible for this disease). Ofloxacin sharing the same target and spectrum makes this less a novel mechanistic hypothesis and more a **class-extension repurposing case**: if other fluoroquinolones are proven effective against *Y. pestis*, ofloxacin's activity against the same organism (in vitro susceptibility is directly documented in the literature below) is biologically plausible.

Of the remaining 9 predicted indications in this pack, none carry a comparable rationale — most are flagged internally as having "no identifiable mechanistic link" (L5, Hold), and one (peripheral neuropathy-associated hematological disease) actually runs counter to a known fluoroquinolone class safety signal rather than supporting a therapeutic use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Human RCTs are not feasible for plague given its rarity and outbreak-driven epidemiology; supporting evidence below is preclinical/animal-model based, consistent with the FDA Animal Rule pathway used for this drug class.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16127904](https://pubmed.ncbi.nlm.nih.gov/16127904/) | 2002 | Preclinical (murine) | Antibiotiki i khimioterapiia | Ofloxacin MIC 0.08 mg/L against *Y. pestis*; superior to pefloxacin and nalidixic acid in prophylaxis/treatment of experimental plague |
| [8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/) | 1994 | Preclinical (murine) | Antimicrob Agents Chemother | Ofloxacin active in vitro against virulent *Y. pestis* strain, comparable to reference drug streptomycin in systemic infection model |
| [32435805](https://pubmed.ncbi.nlm.nih.gov/32435805/) | 2020 | Preclinical (NHP/AGM) | Clin Infect Dis | Ciprofloxacin/levofloxacin ≥90% effective for pneumonic plague in African green monkeys when dosed within 2–6 hours of fever onset |
| [21347450](https://pubmed.ncbi.nlm.nih.gov/21347450/) | 2011 | Preclinical (NHP) | PLoS Negl Trop Dis | Levofloxacin cures experimental pneumonic plague in African green monkeys; basis for FDA approval of the fluoroquinolone class for this indication |
| [20052916](https://pubmed.ncbi.nlm.nih.gov/20052916/) | 2009 | Preclinical (murine) | Antibiotiki i khimioterapiia | Levofloxacin, lomefloxacin, and moxifloxacin highly active against F1+/F1- *Y. pestis* strains in mice |
| [32435803](https://pubmed.ncbi.nlm.nih.gov/32435803/) | 2020 | Review | Clin Infect Dis | Describes the AGM pneumonic plague model used as the basis for FDA antimicrobial approvals under the Animal Rule |
| [17517837](https://pubmed.ncbi.nlm.nih.gov/17517837/) | 2007 | Preclinical (PK/PD model) | Antimicrob Agents Chemother | In vitro PK/PD comparison of streptomycin vs. levofloxacin for plague therapy, including resistance-emergence risk |
| [21127743](https://pubmed.ncbi.nlm.nih.gov/21127743/) | 2010 | Review | Open Microbiol J | Reviews fluoroquinolone protection (ciprofloxacin, levofloxacin) in animal models of anthrax, plague, and tularemia respiratory infection |
| [9517950](https://pubmed.ncbi.nlm.nih.gov/9517950/) | 1998 | Preclinical (murine) | Antimicrob Agents Chemother | Establishes mouse model for evaluating antibiotic treatment of pneumonic plague, benchmarking against streptomycin |
| [10987101](https://pubmed.ncbi.nlm.nih.gov/10987101/) | 2000 | Preclinical (murine) | Antibiotiki i khimioterapiia | Notes ofloxacin (with ciprofloxacin, pefloxacin) can interfere with post-vaccination immunity development against plague — a relevant safety/interaction caveat if co-administered with live attenuated plague vaccine |

---

## Singapore Market Information

No registration records are available — ofloxacin currently has **0 licenses** and a "Not Marketed" status in the Singapore regulatory dataset used for this evidence pack.

---

## Safety Considerations

Detailed safety data (key warnings, contraindications, drug interactions) is not available in this evidence pack, and no DDI records were found for this drug.

One class-level caution surfaced during evidence review for a different candidate indication in this pack: fluoroquinolones, including ofloxacin, carry a known risk of peripheral neuropathy — relevant to monitor if this repurposing path proceeds. Additionally, literature evidence above (PMID 10987101) notes ofloxacin may interfere with immune response development when co-administered with live plague vaccine.

Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Septicemic plague repurposing is supported by a coherent class mechanism (fluoroquinolone inhibition of *Y. pestis* DNA gyrase/topoisomerase IV) and multiple preclinical/animal studies, paralleling the FDA Animal Rule approval already granted to same-class drugs (ciprofloxacin, levofloxacin). However, evidence is entirely preclinical/animal-derived (no human trials exist or are feasible), and Singapore-specific regulatory and safety data are completely absent.

**To proceed, the following is needed:**
- HSA/package-insert warnings, contraindications, and DDI data (currently a Blocking data gap, DG001)
- Confirmed mechanism-of-action documentation from DrugBank (High-severity data gap, DG002)
- Singapore-specific regulatory pathway assessment given current "Not Marketed" status and zero registrations
- Formal risk assessment of fluoroquinolone class safety signals (peripheral neuropathy, tendon rupture, QT prolongation) specific to a biodefense/outbreak-use context
- The remaining 9 predicted indications in this pack (hyperamylasemia, monoclonal gammopathy, etc.) should remain at **Hold** — they lack mechanistic rationale and are supported only by raw TxGNN scores, not curated evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

