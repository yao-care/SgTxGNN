---
layout: default
title: Sultamicillin
parent: Medium Evidence (L3-L4)
nav_order: 934
evidence_level: L3
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Sultamicillin: From Antibacterial Use to Bronchitis

## One-Sentence Summary

Sultamicillin is an oral antibacterial prodrug of ampicillin and sulbactam (a beta-lactamase inhibitor). The TxGNN model predicts it may be effective for **bronchitis**, with **no registered clinical trials** but **16 publications** (open-label and non-comparative clinical studies, pediatric studies, and background microbiology) pointing in this direction. Because the drug is already marketed as an antibacterial, this may be an existing label use rather than true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Evidence Pack (antibacterial; label indication to be confirmed) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 96.2% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Sultamicillin is a mutual prodrug of ampicillin and sulbactam. Ampicillin is a beta-lactam antibacterial. Sulbactam inhibits the beta-lactamases that would otherwise inactivate it. Bacterial exacerbations of chronic bronchitis and lower respiratory tract infections fall within this antibacterial spectrum.

The high TxGNN score is consistent with this. However, the original-indication field is empty, which looks like a data gap, and the drug is already marketed. The label indication should be confirmed before this is treated as a repurposing finding.

The mechanism supports only **bacterial** bronchitis. Viral or non-bacterial bronchitis is not supported.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6323377](https://pubmed.ncbi.nlm.nih.gov/6323377/) | 1984 | Open-label trial | J Antimicrob Chemother | 30 hospitalised patients with acute exacerbations of chronic bronchitis took 750 or 1000 mg twice daily for 10 days. Clinical cure was 73% at end of treatment and 60% one week later. |
| [2041156](https://pubmed.ncbi.nlm.nih.gov/2041156/) | 1991 | Multicenter clinical evaluation | Jpn J Antibiot | 132 patients with lower respiratory tract infections. Efficacy was 78.5% (73/93) for bronchitis and 80.0% (28/35) for pneumonia. |
| [1451929](https://pubmed.ncbi.nlm.nih.gov/1451929/) | 1992 | Clinical study | J Int Med Res | 30 adults with lower respiratory tract infections took 375 mg tablets. 76.6% were cured and 23.3% improved. |
| [1458803](https://pubmed.ncbi.nlm.nih.gov/1458803/) | 1992 | Open non-comparative study | Clin Ter | 48 children with respiratory infections, including 18 with bronchitis. 96% showed a good clinical response. |
| [8008659](https://pubmed.ncbi.nlm.nih.gov/8008659/) | 1993 | Clinical study | Pol Tyg Lek | Compared with cefuroxime axetil in ambulatory exacerbated chronic bronchitis. Design unverified and no abstract available. |
| [3249367](https://pubmed.ncbi.nlm.nih.gov/3249367/) | 1988 | Pediatric clinical study | Jpn J Antibiot | 18 children with infections, 94.4% overall efficacy. Only 1 case of bronchitis (good response). |
| [3249369](https://pubmed.ncbi.nlm.nih.gov/3249369/) | 1988 | Pediatric clinical study | Jpn J Antibiot | 15 children with acute bacterial infections, including 2 with acute bronchitis. All had good to excellent responses. |
| [3249370](https://pubmed.ncbi.nlm.nih.gov/3249370/) | 1988 | Pediatric clinical study | Jpn J Antibiot | 17 children evaluated for PK, safety and efficacy. Bronchitis was only 2 of 14 treated cases. |
| [3249364](https://pubmed.ncbi.nlm.nih.gov/3249364/) | 1988 | Pediatric clinical study | Jpn J Antibiot | 31 pediatric patients with various bacterial infections, evaluated for efficacy and safety. |
| [3000026](https://pubmed.ncbi.nlm.nih.gov/3000026/) | 1985 | Clinical microbiology | Tohoku J Exp Med | Describes respiratory infections (including acute and chronic bronchitis) caused by beta-lactamase-producing *Branhamella catarrhalis*. This is background rationale for a beta-lactamase inhibitor combination. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN04892P | UNASYN ORAL TABLET 375 mg (Pfizer Global Supply Japan Inc) | Tablet, film coated | Not stated in the registry record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The antibacterial spectrum of ampicillin/sulbactam fits bacterial bronchitis. Several open-label and non-comparative studies report cure or response rates of roughly 73–96% in respiratory infections. However, the evidence is old, mostly uncontrolled, and has no confirmed Phase 3 RCT or registered trial. The indication may already be on the label.

**To proceed, the following is needed:**
- Confirm the approved label indication from the HSA package insert. This also supplies the missing warnings and contraindications.
- Obtain detailed mechanism of action data (for example from DrugBank).
- Review the full texts of key studies (especially the comparative trial vs cefuroxime axetil) and look for controlled trials.
- Restrict the scope to bacterial bronchitis, including acute exacerbations of chronic bronchitis.

**Other predictions (not recommended for pursuit):** Thrombosis-related and other predictions such as thrombotic disease, thrombophilia, rheumatoid arthritis and the rare genetic conditions have no plausible mechanism. Where literature exists, it concerns infections occurring alongside the condition, not treatment of the condition itself. All are on **Hold**. Laryngotracheitis (score 90.6%) is a research question only, plausible just for bacterial forms, with no trials or literature retrieved.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

