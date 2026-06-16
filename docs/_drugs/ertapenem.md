---
layout: default
title: Ertapenem
parent: 僅模型預測 (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
---

# Ertapenem
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

# Ertapenem: From Complicated Bacterial Infections to Staphylococcus aureus Infection (Persistent MSSA Bacteremia)

## One-Sentence Summary

Ertapenem (Invanz®) is a broad-spectrum 1β-methyl carbapenem antibiotic, globally established for complicated urinary tract infections, intra-abdominal infections, community-acquired pneumonia, and complicated skin/soft tissue infections — though formal Singapore HSA registration is not currently recorded in this dataset.
The TxGNN model predicts it may be effective for **Staphylococcus aureus Infection** — specifically as a novel salvage combination partner (cefazolin + ertapenem) for persistent MSSA bacteremia —
with **8 clinical trials** and **20 publications** supporting this direction, including a Phase 2 RCT currently recruiting.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Complicated urinary tract infections, intra-abdominal infections, CAP, skin/soft tissue infections (global approvals; Singapore HSA registration not recorded in current dataset) |
| Predicted New Indication | Staphylococcus aureus Infection (persistent MSSA bacteremia — cefazolin + ertapenem salvage combination) |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L3 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ertapenem is a Group 1 carbapenem that inhibits bacterial cell wall synthesis by binding preferentially to penicillin-binding proteins (PBP) 1a, 1b, 2, and 3. Unlike imipenem or meropenem, it has limited activity against *Pseudomonas aeruginosa* and *Enterococcus* species. Its pharmacokinetic profile — once-daily dosing, ~4-hour half-life, ~85–95% protein binding, and significant renal excretion — makes it particularly suited to outpatient parenteral antibiotic therapy (OPAT) and community-onset infections.

The novel repurposing concept centres on the **cefazolin + ertapenem (CEZ+ERT) combination** for persistent methicillin-susceptible *S. aureus* (MSSA) bacteremia — a condition where standard antistaphylococcal monotherapy can fail due to the inoculum effect. Under high bacterial load, β-lactamase enzymes produced by *S. aureus* can overwhelm and inactivate cefazolin. Ertapenem acts as a competitive β-lactamase "sponge," saturating the enzyme's active site and rescuing cefazolin's bactericidal activity through complementary PBP2/PBP3 binding. Beyond this pharmacological mechanism, in vitro evidence (PMID 34978891) demonstrates that ertapenem stimulates interleukin-1β release from peripheral blood monocytes, potentially augmenting the host innate immune response — which may explain why CEZ+ERT shows markedly greater in vivo potency than would be predicted from in vitro MIC data alone.

It is critical to emphasise that this is a **salvage strategy for confirmed persistent MSSA bacteremia only** — not a first-line treatment, and **strictly ineffective against MRSA** (ertapenem has no PBP2a binding activity). Clinical case series have documented rapid bacteremia clearance in refractory endocarditis, LVAD-related infections, and neonatal MSSA sepsis. The accumulating signal has now motivated a dedicated Phase 2 RCT (NCT04886284) and a large Phase 4 study (n=2,096, NCT07376889) — indicating the infectious disease community regards this combination as a credible therapeutic hypothesis deserving rigorous prospective testing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04886284](https://clinicaltrials.gov/study/NCT04886284) | Phase 2 | Recruiting | 60 | CERT trial: First dedicated RCT evaluating CEZ+ERT for persistent MSSA bacteremia; sub-study of the SNAP adaptive platform (NCT05137119); in vitro, animal, and human case series data support the hypothesis; expected completion July 2026 |
| [NCT07376889](https://clinicaltrials.gov/study/NCT07376889) | Phase 4 | Not Yet Recruiting | 2,096 | COMBAT-SAB: Large-scale RCT comparing combination vs single-agent antibiotic therapy for SAB; if ertapenem is included as the combination agent, this will be the most definitive validation to date; expected completion January 2029 |
| [NCT07148960](https://clinicaltrials.gov/study/NCT07148960) | Phase 4 | Enrolling by Invitation | 300 | SABEDTIO: Pragmatic open-label RCT evaluating early dual IV antibiotic therapy for SAB to reduce bacteremia duration (<6 days) and improve clinical outcomes; expected completion July 2027 |
| [NCT00366249](https://clinicaltrials.gov/study/NCT00366249) | Phase 3 | Completed | 1,061 | Tigecycline vs ertapenem for diabetic foot infections; co-primary efficacy endpoints not met; largest completed trial providing ertapenem safety and tolerability data in complicated infections including MSSA |
| [NCT06174649](https://clinicaltrials.gov/study/NCT06174649) | N/A | Completed | 900 | FAST trial: Multicenter RCT evaluating rapid phenotypic AST (Reveal™) for Gram-negative bacteremia; background context for antimicrobial stewardship decision-making around carbapenem use |
| [NCT06044272](https://clinicaltrials.gov/study/NCT06044272) | N/A | Completed | 10,000 | AMR surveillance across healthcare facilities in Meta State, Colombia (2018–2022); large-scale resistance profile data providing epidemiological context for ertapenem stewardship |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [38946294](https://pubmed.ncbi.nlm.nih.gov/38946294/) | 2024 | Retrospective Cohort | J Antimicrob Chemother | First comparative data for carbapenem combination (CEZ or OXA + carbapenem) vs standard of care in persistent MSSA bacteraemia; provides treatment-level evidence beyond case series |
| [40448546](https://pubmed.ncbi.nlm.nih.gov/40448546/) | 2025 | Retrospective Cohort | J Antimicrob Chemother | Hypoalbuminemia (albumin <2.5 g/dL) associated with suboptimal ertapenem exposures in MSSA combination therapy; critical PK/safety guidance for clinical implementation given ertapenem's high protein binding |
| [39230345](https://pubmed.ncbi.nlm.nih.gov/39230345/) | 2025 | Review | Am J Health-Syst Pharm | Comprehensive review of combination treatment options for persistent MSSA bacteremia, positioning CEZ+ERT within the current salvage treatment landscape alongside daptomycin and fosfomycin-based regimens |
| [31773134](https://pubmed.ncbi.nlm.nih.gov/31773134/) | 2020 | Case Series | Clin Infect Dis | CEZ+ERT salvage therapy successfully cleared 11 persistent MSSA bacteremia cases (including 6 endocarditis); immediate clearance (≤24 hours) in 8 cases; in vivo synergy confirmed in rat MSSA endocarditis model |
| [27572414](https://pubmed.ncbi.nlm.nih.gov/27572414/) | 2016 | Case Series | Antimicrob Agents Chemother | Original report describing CEZ+ERT clearing refractory MSSA bacteremia; in vitro and murine skin infection model confirmed synergy; foundational publication for this combination concept |
| [34978891](https://pubmed.ncbi.nlm.nih.gov/34978891/) | 2022 | Mechanistic Study | Antimicrob Agents Chemother | CEZ+ERT combination stimulates IL-1β release from peripheral blood monocytes in the presence and absence of S. aureus; ertapenem identified as the primary immune-activating driver; proposes immune augmentation as a novel mechanism explaining in vivo potency |
| [35493130](https://pubmed.ncbi.nlm.nih.gov/35493130/) | 2022 | In vitro / Biofilm | Open Forum Infect Dis | ERT+CEZ demonstrates potent activity within staphylococcal biofilms, beyond what antistaphylococcal β-lactams alone achieve; mechanistically relevant for endocarditis and device-related MSSA infections |
| [34599521](https://pubmed.ncbi.nlm.nih.gov/34599521/) | 2021 | Case Series | J Card Surg | CEZ+ERT used as salvage therapy for refractory LVAD-related MSSA infections prior to heart transplantation; supports applicability to device-related infections where source control is not feasible |
| [39777519](https://pubmed.ncbi.nlm.nih.gov/39777519/) | 2025 | In vitro | J Infect Dis | Carbapenems (ertapenem and meropenem) enhance ceftaroline- and vancomycin-mediated killing of MRSA; extends the carbapenem combination concept beyond MSSA to drug-resistant strains |
| [15164963](https://pubmed.ncbi.nlm.nih.gov/15164963/) | 2004 | RCT Subgroup Analysis | Int J Antimicrob Agents | Ertapenem vs piperacillin-tazobactam in complicated skin/soft tissue infections caused by MSSA (n=185 MSSA subgroup from Phase 3 RCT); demonstrates ertapenem's established clinical efficacy against MSSA in a randomised trial setting |

---

## Safety Considerations

Please refer to the package insert for safety information.

**Key pharmacokinetic safety note relevant to this indication:** Ertapenem is highly protein-bound (~85–95%). Retrospective data (PMID 40448546) advise against ertapenem use in patients with serum albumin <2.5 g/dL, where suboptimal drug exposures may compromise therapeutic effect. This is clinically critical when considering CEZ+ERT combination therapy in septic patients who frequently present with concurrent hypoalbuminemia or malnutrition.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The cefazolin + ertapenem combination has accumulated a credible and growing body of evidence — retrospective cohorts, multiple case series spanning endocarditis, LVAD infections, and neonatal sepsis, plus confirmed in vitro and animal model synergy — with a well-characterised mechanistic basis. A Phase 2 RCT is actively recruiting (NCT04886284), with results expected July 2026. This is a genuine drug repurposing signal with an actionable clinical niche as a salvage strategy, but adoption ahead of RCT results should be limited to refractory MSSA cases under specialist infectious disease guidance.

**To proceed, the following is needed:**
- Await Phase 2 RCT results from CERT (NCT04886284, n=60, estimated completion July 2026) as the first controlled evidence for CEZ+ERT in persistent MSSA bacteremia
- Confirm whether ertapenem is an active study arm in COMBAT-SAB (NCT07376889) and SABEDTIO (NCT07148960) protocols
- Verify Singapore HSA registration status — ertapenem may be accessible via Therapeutic Products (Unregistered Medicinal Products) authorisation for compassionate/named-patient use even without formal HSA registration
- Obtain complete safety package: Singapore/TFDA package insert with full warnings, contraindications, and drug interaction data (currently unavailable in this dataset)
- Implement albumin monitoring protocol prior to CEZ+ERT initiation; avoid or seek infectious disease specialist guidance when serum albumin <2.5 g/dL
- Define patient selection criteria for institutional salvage use: MSSA-confirmed (not MRSA) persistent bacteremia, failing standard antistaphylococcal therapy for ≥72 hours, appropriate source control measures undertaken
- Consider institutional ethics/stewardship review for any compassionate use protocol pending RCT results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

