---
layout: default
title: Benzylpenicillin
parent: 僅模型預測 (L5)
nav_order: 150
evidence_level: L5
indication_count: 10
---

# Benzylpenicillin
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

# Benzylpenicillin: From Bacterial Infections to Pericoronitis

## One-Sentence Summary

Benzylpenicillin (Penicillin G) is one of the original beta-lactam antibiotics, historically the first-line treatment for a broad range of gram-positive and anaerobic bacterial infections.
The TxGNN model predicts it may be effective for **Pericoronitis**, with **0 clinical trials** and **20 publications** currently supporting this direction.
Benzylpenicillin is not currently registered in Singapore, and formal safety data from the Singapore regulatory database are unavailable.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from Singapore registry (drug not registered) |
| Predicted New Indication | Pericoronitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Benzylpenicillin (Penicillin G) belongs to the beta-lactam class of antibiotics. Although detailed MOA data could not be retrieved from DrugBank in this evaluation run, the mechanism is well-established: beta-lactams bind irreversibly to penicillin-binding proteins (PBPs) on the bacterial cell membrane, inhibiting peptidoglycan cross-linking and causing cell lysis. Benzylpenicillin has a narrow spectrum, with greatest potency against gram-positive cocci, gram-negative cocci, and many anaerobes — precisely the organisms implicated in pericoronitis.

Pericoronitis is an acute infection of the pericoronal soft tissues surrounding a partially erupted tooth, most commonly the mandibular third molar. The infection is polymicrobial, dominated by the Streptococcus milleri group, viridans streptococci, and obligate oral anaerobes (Peptostreptococcus, Bacteroides, Fusobacterium nucleatum, and spirochetes). This flora profile falls within benzylpenicillin's classical antibacterial coverage. Expert survey data (PMID 1873287) and systematic antibiotic prescribing guidance (PMID 35959239) both confirm beta-lactams as a legitimate first-line choice when systemic antibiotic therapy is indicated.

The key reservation is the rising prevalence of beta-lactamase-producing strains in pericoronitis flora: a dedicated microbiological study (PMID 12789143, 2003) identified significant beta-lactamase-producing bacteria in third molar pericoronitis, which would render benzylpenicillin ineffective without a beta-lactamase inhibitor. Current Japanese antimicrobial susceptibility surveillance (PMID 40381916, 2025) further underscores that resistance profiles must be verified before selecting a narrow-spectrum agent. Modern dental practice increasingly favours amoxicillin ± clavulanic acid or metronidazole over benzylpenicillin for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39068391](https://pubmed.ncbi.nlm.nih.gov/39068391/) | 2024 | RCT | BMC Oral Health | Assessed a combined mouthwash (chlorhexidine, benzydamine, nanosilver, amoxicillin, metronidazole) for pain reduction and improved mouth opening in acute pericoronitis; supports local antimicrobial therapy concept |
| [35959239](https://pubmed.ncbi.nlm.nih.gov/35959239/) | 2022 | Systematic Review | JAC-Antimicrobial Resistance | Reviewed indications for metronidazole in non-periodontal dental infections; recommends restricting systemic antibiotics to cases with clear systemic involvement, with beta-lactam monotherapy as first-line |
| [40381916](https://pubmed.ncbi.nlm.nih.gov/40381916/) | 2025 | Surveillance Study | J Infect Chemother | Second Japanese susceptibility surveillance of odontogenic infection isolates including pericoronitis samples; provides current resistance data relevant to penicillin-class selection |
| [32591324](https://pubmed.ncbi.nlm.nih.gov/32591324/) | 2020 | Surveillance Study | J Infect Chemother | First Japanese susceptibility surveillance; 6 pericoronitis samples from 246 odontogenic infection specimens; establishes baseline penicillin-class resistance rates |
| [12789143](https://pubmed.ncbi.nlm.nih.gov/12789143/) | 2003 | Microbiological Study | Oral Surg Oral Med Oral Pathol | Characterised predominant flora in third molar pericoronitis and identified a significant proportion of beta-lactamase-producing strains — key safety signal for benzylpenicillin monotherapy |
| [16388299](https://pubmed.ncbi.nlm.nih.gov/16388299/) | 2006 | Observational Study | Med Oral Patol Oral Cir Bucal | Evaluated antibiotic susceptibility profiles of bacteria from pericoronitis of the lower third molar alongside periapical infections; aimed at optimising antibiotherapy selection |
| [26067725](https://pubmed.ncbi.nlm.nih.gov/26067725/) | 2015 | Retrospective Study | J Contemp Dent Pract | Analysed prevalence, demographics, and management of odontogenic infections (including pericoronitis) in a university dental emergency service over one year |
| [1873287](https://pubmed.ncbi.nlm.nih.gov/1873287/) | 1991 | Survey / Expert Opinion | Br J Oral Maxillofac Surg | British oral and maxillofacial surgeons' consensus on pericoronitis aetiology and management; identifies anaerobic flora dominance and confirms penicillins and metronidazole as effective antimicrobials |
| [29693642](https://pubmed.ncbi.nlm.nih.gov/29693642/) | 2018 | Narrative Review | Antibiotics (Basel) | Reviews antibiotic prescribing patterns for oro-facial infections in paediatric outpatients; highlights growing resistance concerns and appropriate selection principles |
| [21027620](https://pubmed.ncbi.nlm.nih.gov/21027620/) | 1946 | Case Report (Historical) | Am J Orthodontics Oral Surg | Earliest direct evidence: submaxillary abscess secondary to acute pericoronitis treated by aspiration and local penicillin instillation with clinical success |

---

## Singapore Market Information

Benzylpenicillin is not currently registered in Singapore. No marketing authorisations are on record in the Singapore regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Benzylpenicillin has a mechanistically sound rationale for pericoronitis — the causative oral streptococci and anaerobes fall within its classical antibacterial spectrum, expert opinion confirms penicillins as an appropriate first-line antibiotic class for this indication, and historical clinical use (including a 1946 direct-use case) provides foundational support. However, the absence of modern controlled trials, the documented rise of beta-lactamase-producing organisms in pericoronitis flora, and the drug's non-registration in Singapore mean further validation steps are required before clinical deployment.

**To proceed, the following is needed:**
- Retrieve detailed MOA and safety data from the DrugBank API (DG001, DG002 data gaps)
- Obtain Singapore (HSA) or equivalent package insert to complete warnings, contraindications, and drug interaction assessment
- Commission a contemporary susceptibility study of pericoronitis isolates against benzylpenicillin to quantify local resistance rates
- Define the intended route of administration (intravenous vs. oral benzylpenicillin vs. topical/local instillation) and confirm clinical feasibility in the outpatient dental setting
- Conduct a head-to-head comparative effectiveness study versus current standard of care (amoxicillin ± clavulanate or metronidazole) before any clinical implementation
- Evaluate the regulatory pathway for Singapore — either market registration or a defined off-label use framework with appropriate clinical governance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

