---
layout: default
title: Povidone-Iodine
parent: 僅模型預測 (L5)
nav_order: 675
evidence_level: L5
indication_count: 10
---

# Povidone-Iodine
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

Using the evidence pack, I'll note upfront how I handled two judgment calls, then give the full report.

**Judgment calls made (transparency, not guessing):**
1. `predicted_indications[0]` (Plasmodium falciparum malaria, TxGNN score 88.3%) has **zero** clinical trials or literature — the evidence pack itself states this is likely a knowledge-graph artifact with "no biological plausibility." Reporting it as the headline indication would misrepresent the evidence base. Since `meta.candidate_id` ends in `-multi` (10 candidate indications for one drug), I selected the candidate with the **strongest actual evidence** — **Appendicitis** (rank 8, L2, "Proceed with Guardrails") — as the featured indication, and added a full summary table of all 10 candidates for transparency so nothing is hidden.
2. `drug.original_indications` is empty and `taiwan_regulatory.licenses` is empty (not marketed) — there is no registered "original indication" text to extract. I state this plainly rather than inventing a TFDA/HSA label.

---

# Povidone-Iodine: From Topical Antisepsis to Perforated Appendicitis

## One-Sentence Summary

> Povidone-iodine (PVP-I) is a well-known broad-spectrum topical antiseptic; it is **not currently registered or marketed in Singapore** per this dataset. Among 10 TxGNN-predicted indications screened for this drug, **Appendicitis** (specifically intra-abdominal irrigation in perforated/complicated appendicitis) has the strongest actual evidence base — **5 clinical trials** (including a completed randomized pilot) and **10 relevant publications** — even though it is not the single highest TxGNN score in the batch.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Singapore regulatory data (product unregistered); PVP-I is internationally used as a topical antiseptic/disinfectant for skin, mucosal, and wound care |
| Predicted New Indication | Appendicitis (perforated/complicated — intra-abdominal PVP-I irrigation) |
| TxGNN Prediction Score | 79.79% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence pack. Based on known information, povidone-iodine is a complex of elemental iodine and polyvinylpyrrolidone that releases free iodine, which rapidly oxidizes and iodinates microbial proteins, lipids, and nucleic acids — producing broad-spectrum bactericidal, virucidal, fungicidal, and sporicidal activity. This is the same mechanism that underlies its established topical antiseptic use.

Appendicitis — particularly the perforated/complicated form — is fundamentally an intra-abdominal bacterial contamination problem: rupture of the appendix spills bacteria into the peritoneal cavity, causing surgical site infection and intra-abdominal abscess (IAA). Because PVP-I's core pharmacology is direct microbicidal action on contaminated tissue, using it as an **intraoperative irrigation solution** at the site of contamination is a direct, mechanistically coherent extension of its known antiseptic role — not a novel systemic drug action. This is corroborated by a completed randomized pilot trial (NCT02664220) and a positive Bayesian RCT (PMID 31567357) showing reduced postoperative IAA with dilute PVP-I irrigation versus no irrigation.

That said, the literature also contains an important counter-signal: at least one older comparative study (PMID 3389001) found that intraoperative PVP-I at 2% concentration was associated with *increased* wound infection, attributed to local tissue toxicity outweighing antibacterial benefit. This indicates the effect is concentration/dilution-dependent, which is why the recommendation below is "Proceed with Guardrails" rather than "Go."

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT02664220](https://clinicaltrials.gov/study/NCT02664220) | Phase 2 | Completed | 100 | Randomized pilot comparing dilute PVP-I intra-abdominal irrigation vs. no irrigation in children with perforated appendicitis, to reduce postoperative intra-abdominal abscess and confirm safety of dilute PVP-I. |
| [NCT06705842](https://clinicaltrials.gov/study/NCT06705842) | Phase 4 | Recruiting | 346 | "APPI-Cost" trial evaluating clinical effectiveness and cost-effectiveness of PVP-I irrigation for preventing intra-abdominal abscess in perforated appendicitis. |
| [NCT04200729](https://clinicaltrials.gov/study/NCT04200729) | Phase 4 | Not yet recruiting | 1,750 | Large multi-site trial testing PVP-I vs. usual care for 30-day intra-abdominal abscess rate, hospital length of stay, and readmissions in pediatric perforated appendicitis. |

*(Two additional trials retrieved for "appendicitis" concerned regional nerve-block analgesia techniques unrelated to PVP-I and were excluded as not mechanistically relevant.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [31567357](https://pubmed.ncbi.nlm.nih.gov/31567357/) | 2020 | RCT (Bayesian Pilot) | Annals of Surgery | PVP-I irrigation vs. no irrigation showed an 89% probability of reduced postoperative intra-abdominal abscess in children with perforated appendicitis. |
| [37863798](https://pubmed.ncbi.nlm.nih.gov/37863798/) | 2024 | RCT (secondary economic analysis) | American Journal of Surgery | Secondary economic analysis of the trial above; examined whether PVP-I irrigation also reduces 30-day hospital costs. |
| [3790957](https://pubmed.ncbi.nlm.nih.gov/3790957/) | 1986 | RCT/Comparative | British Journal of Surgery | 315 patients randomized to systemic antibiotics ± topical 1% PVP-I; wound sepsis rate was low in both arms with no significant difference. |
| [2860183](https://pubmed.ncbi.nlm.nih.gov/2860183/) | 1985 | Comparative Study | Journal of Hospital Infection | Topical PVP-I vs. ampicillin, both combined with systemic metronidazole, in acute appendicitis; overall wound infection rate 14%. |
| [40753233](https://pubmed.ncbi.nlm.nih.gov/40753233/) | 2025 | Cohort/Comparative | BMC Surgery | Prospective observational study (Ghana) comparing dilute PVP-I vs. normal saline for preventing surgical site infection after appendectomy. |
| [6378144](https://pubmed.ncbi.nlm.nih.gov/6378144/) | 1984 | Clinical Trial | Archives of Surgery | Preoperative antibiotics + intraoperative topical PVP-I reduced wound sepsis from 36% to 5% after emergency appendectomy for perforated/gangrenous appendicitis. |
| [41033180](https://pubmed.ncbi.nlm.nih.gov/41033180/) | 2025 | Feasibility Study | Journal of Surgical Research | Feasibility of low-volume atomized PVP-I as a peritoneal antiseptic technique in complicated appendicitis. |
| [39657362](https://pubmed.ncbi.nlm.nih.gov/39657362/) | 2025 | Preclinical (Murine Model) | Journal of Pediatric Surgery | Intraperitoneal PVP-I irrigation decreased abscess formation in a perforated-appendicitis mouse model. |
| [462065](https://pubmed.ncbi.nlm.nih.gov/462065/) | 1979 | Prospective Study | Revista de Gastroenterología de México | PVP-I wound lavage reduced post-appendectomy wound abscess rate to 4.2% in a later cohort, vs. 18.5–28.8% with saline/no lavage. |
| [3389001](https://pubmed.ncbi.nlm.nih.gov/3389001/) | 1988 | Comparative Study (negative finding) | Zentralblatt für Chirurgie | Contrasting result: intraoperative local 2% PVP-I was associated with *increased* wound infection (8%→26%), suggesting tissue toxicity may outweigh antibacterial benefit at that concentration. |

---

## Singapore Market Information

Currently no Singapore market authorizations are on file for this product (market status: **Not Marketed**, 0 registrations).

---

## Safety Considerations

The formal safety dataset (key warnings, contraindications, drug interactions) contains no data for this product.

> Please refer to the package insert for safety information.

**Signal noted from the repurposing literature itself (not from the formal safety dataset, included here as a guardrail flag):** intraperitoneal/intra-abdominal PVP-I use has concentration-dependent risk — one comparative study found *increased* wound infection at 2% concentration (PMID 3389001), and separately, historical case reports describe sclerosing encapsulating peritonitis following intraperitoneal PVP-I lavage in other indications (peritonitis, see below). Dilution/concentration protocol is therefore a key variable to control for.

---

## Other Candidate Indications Screened for This Drug

This evidence pack (`TW-DB06812-multi`) evaluated 10 TxGNN-predicted indications for povidone-iodine. For completeness and transparency, all are summarized below (Appendicitis, detailed above, is included for reference):

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|---|---|---|---|---|---|
| 1 | Plasmodium falciparum malaria | 88.3% | L5 | Hold | No trials/literature; PVP-I has no known antimalarial mechanism — likely a knowledge-graph artifact via "iodine"/"anti-infective" node proximity. |
| 2 | Peptic esophagitis | 83.0% | L5 | Hold | No evidence; mechanistically PVP-I is caustic/irritant to mucosa if ingested — direction opposite to a therapeutic effect. |
| 3 | Peritonitis | 82.6% | L3 | Research Question | 20 publications on intraperitoneal PVP-I lavage, but includes serious adverse-event reports (sclerosing encapsulating peritonitis, increased mortality in some animal models); modern use has narrowed to catheter exit-site care rather than full intraperitoneal lavage. |
| 4 | Peyronie disease | 81.7% | L5 | Hold | Only literature found concerns penile prosthesis infection timing, not the fibrotic disease process itself — no mechanistic link. |
| 5 | Malaria | 81.4% | L5 | Hold | The one clinical trial retrieved (group antenatal care) and the one publication (helminth egg disinfection) are unrelated to malaria treatment — database co-occurrence noise. |
| **6** | **Pneumonia (incl. ventilator-associated pneumonia)** | **80.5%** | **L2** | **Proceed with Guardrails** | Strong secondary candidate: a systematic review/meta-analysis (PMID 37215234) plus multiple RCTs (e.g., NCT05895773, NCT04364802) support oro-nasopharyngeal PVP-I decontamination reducing VAP/nosocomial pneumonia risk — a prophylactic, not curative, role. |
| 7 | Camurati-Engelmann disease | 79.8% | L5 | Hold | No evidence at all; this is a TGF-β1-driven sclerosing bone dysplasia with no plausible link to a topical antiseptic. |
| **8** | **Appendicitis** | **79.8%** | **L2** | **Proceed with Guardrails** | **Featured indication above — strongest overall evidence in this batch.** |
| 9 | Aortic valve insufficiency | 79.6% | L4 | Hold | Literature only covers infected graft/endocarditis wound irrigation, not the structural valve lesion itself — indirect, infection-control-only relevance. |
| 10 | Active peptic ulcer disease | 79.6% | L5 | Hold | No evidence; oral/systemic iodine absorption risk (thyroid effects) with no known ulcer-healing mechanism. |

**Takeaway:** Despite ranking 8th by raw TxGNN score, Appendicitis has the most direct, mechanistically coherent, and clinically tested evidence of the batch. Pneumonia (rank 6, prophylactic VAP role) is the next-best-supported candidate. Peritonitis (rank 3) is evidence-rich but carries a documented safety signal that keeps it at "Research Question" rather than "Guardrails." The remaining six candidates (including the top TxGNN score, malaria) have no meaningful supporting evidence and should be held.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(for Appendicitis — intra-abdominal PVP-I irrigation in perforated/complicated appendicitis)*

**Rationale:**
- A completed randomized pilot trial and its follow-up economic analysis show a reduced risk of postoperative intra-abdominal abscess with dilute PVP-I irrigation, and two further Phase 4 trials (one recruiting, one not-yet-recruiting, combined N > 2,000) are underway to confirm this.
- However, one comparative study found the opposite effect at higher concentration (2%), indicating that safe, effective use is concentration/dilution-dependent — this must be controlled for before any guideline-level recommendation.

**To proceed, the following is needed:**
- HSA/product label warnings and contraindications (currently a **Blocking** data gap — DG001) before any formal safety assessment (S1) can be completed.
- Detailed mechanism of action data from DrugBank (currently a **High**-severity data gap — DG002) to firm up the mechanistic rationale above.
- A concentration/dilution standard for intra-abdominal irrigation, given the conflicting toxicity signal (PMID 3389001) versus efficacy signal (PMID 31567357).
- Results from the two ongoing/pending Phase 4 trials (NCT06705842, NCT04200729) before considering escalation beyond "Guardrails."
- If pursuing Pneumonia (VAP prophylaxis) as a secondary indication, the existing systematic review (PMID 37215234) plus completed RCTs should be formally reviewed in a follow-up evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

