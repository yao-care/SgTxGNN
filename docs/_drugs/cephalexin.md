---
layout: default
title: Cephalexin
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
---

# Cephalexin
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

# Cephalexin: From Bacterial Infections to Chronic Otitis Media

## One-Sentence Summary

Cephalexin is a first-generation oral cephalosporin antibiotic, widely used for treating susceptible bacterial infections including skin and soft tissue infections, urinary tract infections, and upper respiratory tract infections.
The TxGNN model predicts it may be effective for **Chronic Otitis Media**, with **0 registered clinical trials** and **20 publications** currently identified in support of this direction.
However, critical limitations in its antimicrobial spectrum — particularly gaps against *Pseudomonas aeruginosa* and anaerobic bacteria — raise concerns about its adequacy as a standalone therapy for this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not specified (no Singapore HSA registration on record) |
| Predicted New Indication | Chronic Otitis Media |
| TxGNN Prediction Score | 98.55% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known pharmacology, Cephalexin is a first-generation cephalosporin that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs), disrupting peptidoglycan cross-linking and causing cell lysis. It has reliable activity against Gram-positive organisms — particularly *Staphylococcus aureus* (methicillin-susceptible) and *Streptococcus* species — with limited coverage of Gram-negative organisms and virtually no activity against *Pseudomonas aeruginosa* or anaerobic bacteria.

Chronic otitis media (COM), especially chronic suppurative otitis media (CSOM), is a persistent middle ear infection characterised by tympanic membrane perforation and ongoing otorrhea. The microbiology of CSOM is polymicrobial: *Pseudomonas aeruginosa* and *Staphylococcus aureus* are the dominant aerobic pathogens, with anaerobic bacteria (e.g., *Bacteroides*, *Peptostreptococcus*) co-isolated in over 50% of cases (Brook I, 1994, PMID 8177625). Cephalexin's activity against *S. aureus* and *Streptococcus* provides a partial mechanistic rationale for use in early or less severe cases.

The critical limitation is that cephalexin's spectrum does not cover the full polymicrobial burden of CSOM. The 1994 Brook study (PMID 8177625) directly compared outcomes in 69 children with CSOM and found that therapies active against anaerobic bacteria produced faster resolution than cephalexin-class regimens. An older RCT from 1983 (PMID 6361325) did use cephalexin as an active comparator in acute suppurative otitis media and demonstrated comparable efficacy to cefroxadine — suggesting historical clinical use — but modern ENT guidelines no longer list first-generation cephalosporins as preferred agents. The TxGNN prediction likely reflects the proximity of cephalosporins to otitis media nodes in the pharmacological knowledge graph, rather than a direct and compelling mechanistic advantage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cephalexin in Chronic Otitis Media.

---

## Literature Evidence

The following publications are ranked by direct relevance to cephalexin use in otitis media. Several papers in the full retrieved set primarily concern other cephalosporins (cefaclor, cefdinir, cefixime) and are noted accordingly.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [6361325](https://pubmed.ncbi.nlm.nih.gov/6361325/) | 1983 | RCT (active-controlled) | The Japanese Journal of Antibiotics | Double-blind RCT comparing cefroxadine (250 mg TID) vs **cephalexin** (250 mg QID) in acute suppurative otitis media and acute exacerbation of CSOM; both drugs produced comparable outcomes with no significant difference in efficacy assessments |
| [8177625](https://pubmed.ncbi.nlm.nih.gov/8177625/) | 1994 | Comparative Cohort | Pediatric Infectious Disease Journal | Retrospective study of 69 children with CSOM; 54% had mixed aerobic-anaerobic flora; anaerobic-active therapy produced the fastest resolution — explicitly outperforming cephalexin-class regimens; 58% of patients carried beta-lactamase-producing bacteria |
| [6798820](https://pubmed.ncbi.nlm.nih.gov/6798820/) | 1981 | Observational | Acta Oto-laryngologica | Divided COM patients into oral **cephalexin** vs cephalexin ear drops; the topical group showed higher incidence and greater magnitude of bacterial count reduction, suggesting local delivery is superior to systemic for COM |
| [22737435](https://pubmed.ncbi.nlm.nih.gov/22737435/) | 2011 | Cross-sectional Microbiological | Iranian Red Crescent Medical Journal | Investigated aerobic organisms in CSOM in Iran with current susceptibility patterns; confirms polymicrobial nature and identifies antibiotic resistance profiles relevant to cephalosporin selection |
| [11838568](https://pubmed.ncbi.nlm.nih.gov/11838568/) | 2001 | Review | Indian Journal of Pediatrics | Upper respiratory tract infections account for 20–40% of outpatient visits; otitis media comprises 87.5% of such infections; vast majority caused by viruses — antibiotics appropriate only for bacterial complications |
| [7200999](https://pubmed.ncbi.nlm.nih.gov/7200999/) | 1982 | Pharmacokinetic Study | Journal of Infectious Diseases | Studied penetration of amoxicillin, cefaclor, erythromycin-sulfisoxazole, and TMP-SMX into middle ear fluid of children with chronic serous otitis media; provides framework for evaluating whether oral cephalosporins achieve therapeutic concentrations in the middle ear |
| [1920724](https://pubmed.ncbi.nlm.nih.gov/1920724/) | 1991 | Bacteriological Survey | JAMA | Characterised bacteriology of acute otitis media in adults in the US; *Streptococcus pneumoniae* and *H. influenzae* predominant — the latter being relatively resistant to first-generation cephalosporins |
| [9519](https://pubmed.ncbi.nlm.nih.gov/9519/) | 1976 | Case Series / Bacteriological | Journal of Otolaryngology | 147 patients with acute suppurative otitis media treated with azidocillin, ampicillin, or **cephalexin**; assessed bacteriological response in aural discharge and nasopharynx; one of the earliest direct reports of cephalexin use in this condition |
| [240948](https://pubmed.ncbi.nlm.nih.gov/240948/) | 1975 | Case Series | JAMA | **Cephalexin** monohydrate suspension used in 97 children with otitis media; post-treatment cultures at 48 hours showed eradication of *Diplococcus pneumoniae* in most cases; provides early clinical context for cephalexin's activity |
| [29674370](https://pubmed.ncbi.nlm.nih.gov/29674370/) | 2018 | RCT | BMJ Open | Prospective RCT evaluating a single 2 g preoperative oral dose of **cephalexin** for surgical site infection prophylaxis in dermatological procedures on the nose and ear; relevant as evidence of cephalexin's perioperative role in ear-adjacent structures |

---

## Singapore Market Information

Cephalexin currently has no registered products with the Health Sciences Authority (HSA) of Singapore. No authorisation numbers, product names, or approved indications are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Formal safety data (key warnings, contraindications, and drug-drug interaction data) were not retrieved in this evidence pack. Before any clinical use, the full prescribing information should be reviewed. As a beta-lactam antibiotic, cephalexin carries a known risk of hypersensitivity reactions, including cross-reactivity in penicillin-allergic patients, and should be used with caution in patients with renal impairment (dose adjustment required).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While Cephalexin has documented historical use in acute otitis media and an older RCT (1983) demonstrates comparable efficacy to cefroxadine in suppurative otitis media, the evidence specifically for *chronic* otitis media is insufficient to support a repurposing recommendation. The mechanistic mismatch is significant: CSOM is characterised by polymicrobial infection (including *Pseudomonas aeruginosa* and anaerobes) that falls outside cephalexin's antimicrobial spectrum. A 1994 comparative cohort study explicitly demonstrated that broader-spectrum anaerobic-active therapies outperform cephalexin-class regimens in CSOM. No registered clinical trials currently exist for this specific indication, and modern ENT guidelines do not list first-generation cephalosporins as a recommended choice for CSOM.

**To proceed, the following is needed:**

- **Mechanism of action documentation**: Retrieve full DrugBank MOA data to formalise the pharmacological rationale
- **Singapore regulatory gap**: Cephalexin is not registered in Singapore — a market authorisation pathway must be considered before any clinical development
- **Updated microbiological susceptibility data**: Confirm whether contemporary local *S. aureus* strains in Singapore remain susceptible to cephalexin (MRSA prevalence is a key variable)
- **Spectrum gap analysis**: Evaluate whether a combination regimen (e.g., cephalexin + metronidazole) could address the anaerobic coverage gap, or whether a broader-spectrum cephalosporin would be more appropriate
- **TFDA/HSA package insert review**: Retrieve the full prescribing information (warnings, contraindications, DDI) to complete the safety assessment — currently classified as a Blocking data gap
- **Comparative effectiveness review**: Commission a systematic review or meta-analysis comparing first-generation cephalosporins against current guideline-recommended agents (quinolones, amoxicillin-clavulanate) specifically for CSOM in the context of modern resistance patterns
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

