---
layout: default
title: Sultamicillin
parent: Medium Evidence (L3-L4)
nav_order: 944
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Sultamicillin: predicted new indication Bronchitis (evidence level L3). Approved use: Not recorded in the licence data (the approved indication text is emp…"
monitor_inn: "Sultamicillin"
predicted_indications: ["bronchitis", "thrombotic disease", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "rheumatoid arthritis", "antithrombin deficiency type 2", "laryngotracheitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "thrombophilia", "myositis fibrosa"]
---

# Sultamicillin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Sultamicillin: From Bacterial Infections (Indication Text Not Recorded) to Bronchitis

## One-Sentence Summary

Sultamicillin is an oral antibiotic that combines ampicillin and sulbactam (a beta-lactamase inhibitor) in a single molecule. The registered indication text for the Singapore licence is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **bronchitis**. Currently **0 registered clinical trials** and **13 publications** (mostly small, open-label or non-comparative studies from 1984 to 1993) support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the licence data (the approved indication text is empty) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 96.2% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, sultamicillin is a mutual prodrug of ampicillin and sulbactam. Ampicillin is a broad-spectrum beta-lactam antibiotic, and sulbactam inhibits beta-lactamase enzymes that would otherwise destroy it. Together they cover common respiratory pathogens, including beta-lactamase-producing strains.

Bacterial bronchitis and acute exacerbations of chronic bronchitis are therefore consistent with the drug's antibacterial activity. This is an extension within the anti-infective class rather than a true mechanistic repurposing. Because the original indication field is empty, we could not confirm whether bronchitis or other respiratory infections already appear on the Singapore label.

Other predicted indications were reviewed and are not supported. Thrombotic and coagulation disorders (thrombotic disease, thrombophilia, heparin cofactor 2 deficiency, antithrombin deficiency type 2, factor 5 excess), rheumatoid arthritis, colobomatous microphthalmia-rhizomelic dysplasia syndrome and myositis fibrosa have no plausible mechanism and no relevant evidence. Their high scores are likely artifacts of knowledge-graph proximity. Laryngotracheitis is plausible only for rare bacterial cases, because most croup is viral.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6323377](https://pubmed.ncbi.nlm.nih.gov/6323377/) | 1984 | Open-label trial | J Antimicrob Chemother | 30 hospitalised patients with acute exacerbations of chronic bronchitis took 750 or 1000 mg twice daily for 10 days. Clinical cure was 73% at end of treatment and 60% one week later. |
| [8008659](https://pubmed.ncbi.nlm.nih.gov/8008659/) | 1993 | Clinical comparison | Pol Tyg Lek | Sultamicillin compared with cefuroxime axetil in outpatients with exacerbated chronic bronchitis (no abstract available). |
| [2041156](https://pubmed.ncbi.nlm.nih.gov/2041156/) | 1991 | Multicentre clinical evaluation | Jpn J Antibiot | 132 patients with lower respiratory tract infections across 19 institutions. Efficacy was 78.5% (73/93) for bronchitis and 80.0% (28/35) for pneumonia. |
| [1451929](https://pubmed.ncbi.nlm.nih.gov/1451929/) | 1992 | Clinical study | J Int Med Res | 30 adults with lower respiratory tract infections taking 375 mg tablets. 76.6% were cured and the rest improved. |
| [1458803](https://pubmed.ncbi.nlm.nih.gov/1458803/) | 1992 | Open non-comparative study | Clin Ter | 48 children with respiratory infections (18 with bronchitis) were treated at 50 mg/kg/day. 96% showed a good clinical response. |
| [3249369](https://pubmed.ncbi.nlm.nih.gov/3249369/) | 1988 | Paediatric clinical study | Jpn J Antibiot | 15 children with acute bacterial infections, including 2 with acute bronchitis. All responded well to excellent. |
| [3249367](https://pubmed.ncbi.nlm.nih.gov/3249367/) | 1988 | Paediatric clinical study | Jpn J Antibiot | 18 children, mostly with tonsillitis. The overall efficacy rate was 94.4%, and the single bronchitis case responded well. |
| [3249370](https://pubmed.ncbi.nlm.nih.gov/3249370/) | 1988 | Paediatric clinical study | Jpn J Antibiot | 17 children, including 2 with bronchitis, assessed for pharmacokinetics, safety and efficacy. |
| [3249372](https://pubmed.ncbi.nlm.nih.gov/3249372/) | 1988 | Paediatric PK and clinical study | Jpn J Antibiot | Pharmacokinetic and clinical study of the granule formulation in children. |
| [3249373](https://pubmed.ncbi.nlm.nih.gov/3249373/) | 1988 | Paediatric PK and clinical study | Jpn J Antibiot | Pharmacokinetic and clinical study of 10% fine granules in children with various infections. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN04892P | UNASYN ORAL TABLET 375 mg | Film-coated tablet | Not recorded |

---

## Safety Considerations

Please refer to the package insert for safety information. Warning and contraindication text was not available in the data compiled for this report, and no drug-interaction records were found.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The use of sultamicillin in bronchitis is consistent with its antibacterial mechanism, and several small clinical studies report clinical response rates of roughly 60–96%. However, the evidence consists of older, mostly uncontrolled studies with no registered trials, so it is classed as L3. Because the safety data and the labelled indications are missing, this should proceed only with conditions.

**To proceed, the following is needed:**
- Download and review the HSA package insert to confirm the labelled indications, warnings and contraindications. This blocks safety screening.
- Obtain detailed mechanism of action data (for example from DrugBank).
- Confirm whether bronchitis or respiratory tract infection is already on the Singapore label.
- Check current local resistance patterns of respiratory pathogens.
- Look for more recent controlled studies, since the available data date from 1984 to 1993.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

