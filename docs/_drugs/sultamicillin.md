---
layout: default
title: Sultamicillin
parent: 僅模型預測 (L5)
nav_order: 934
evidence_level: L5
indication_count: 10
---

# Sultamicillin
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

# Sultamicillin: From Bacterial Infections to Bronchitis

## One-Sentence Summary

Sultamicillin is an oral mutual prodrug of ampicillin and sulbactam, a β-lactam/β-lactamase inhibitor combination antibiotic used to treat bacterial infections. The TxGNN model predicts it may be effective for **Bronchitis** (including acute exacerbations of chronic bronchitis), with **0 registered clinical trials** but **16 supporting publications**, mostly historical open-label and cohort studies from the 1980s–1990s. This is best understood as confirmation of an already-known antibacterial indication rather than a novel mechanistic repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in registry data (Sultamicillin is a β-lactam/β-lactamase inhibitor combination antibiotic used for bacterial infections) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 96.20% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Sultamicillin is a mutual prodrug of ampicillin and sulbactam, belonging to the β-lactam/β-lactamase inhibitor combination antibiotic class; its efficacy against bacterial infections has been well established, and mechanistically it is expected to be applicable to bronchitis.

Bronchitis — particularly acute exacerbations of chronic bronchitis and lower respiratory tract infections — is commonly caused by bacterial pathogens (e.g. *Haemophilus influenzae*, *Streptococcus pneumoniae*, *Branhamella catarrhalis*) that fall within Sultamicillin's known antibacterial spectrum. This is therefore not a mechanistic "repurposing" in the traditional sense, but rather a confirmation/extension of the drug's core antibacterial indication to a specific respiratory infection subtype. Because the input `original_indications` field was empty, the candidate was still carried through the full evaluation pipeline for completeness.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6323377](https://pubmed.ncbi.nlm.nih.gov/6323377/) | 1984 | Open-label trial | J Antimicrob Chemother | 30 hospitalised patients with acute purulent exacerbations of chronic bronchitis treated with sultamicillin 750–1000 mg BID x10 days; clinical cure rates 73% at end-of-treatment, 60% at 1-week follow-up |
| [2041156](https://pubmed.ncbi.nlm.nih.gov/2041156/) | 1991 | Open-label clinical evaluation | Jpn J Antibiot | Multicenter trial (132 patients) in lower respiratory tract infections; efficacy rate 78.5% (73/93) for bronchitis and 80.0% for pneumonia |
| [1451929](https://pubmed.ncbi.nlm.nih.gov/1451929/) | 1992 | Open-label trial | J Int Med Res | 30 adults with lower respiratory tract infections treated with 375 mg sultamicillin q8–12h; cure in 76.6%, improvement in 23.3% |
| [1458803](https://pubmed.ncbi.nlm.nih.gov/1458803/) | 1992 | Open non-comparative trial | La Clinica Terapeutica | 48 children with respiratory infections (18 bronchitis, 4 asthmatic bronchitis) treated at 50 mg/kg/day; 96% good clinical response |
| [8008659](https://pubmed.ncbi.nlm.nih.gov/8008659/) | 1993 | Comparative trial (vs cefuroxime axetil) | Pol Tyg Lek | Ambulatory treatment comparison in exacerbated chronic bronchitis |
| [3249371](https://pubmed.ncbi.nlm.nih.gov/3249371/) | 1988 | Cohort/PK study (pediatric) | Jpn J Antibiot | Pharmacokinetics and therapeutic effectiveness of sultamicillin fine granules in children |
| [3249372](https://pubmed.ncbi.nlm.nih.gov/3249372/) | 1988 | Cohort/PK study (pediatric) | Jpn J Antibiot | Plasma and urinary concentration study of sultamicillin granules in pediatric patients |
| [3249362](https://pubmed.ncbi.nlm.nih.gov/3249362/) | 1988 | Cohort/PK/bacteriological study (pediatric) | Jpn J Antibiot | Antibacterial activity against key respiratory pathogens (H. influenzae, S. pneumoniae, B. catarrhalis) compared with ampicillin |
| [3249365](https://pubmed.ncbi.nlm.nih.gov/3249365/) | 1988 | Cohort/clinical study (pediatric) | Jpn J Antibiot | Serum level and clinical response study including bronchitis cases |
| [3249373](https://pubmed.ncbi.nlm.nih.gov/3249373/) | 1988 | Cohort/PK study (pediatric) | Jpn J Antibiot | Pharmacokinetic and clinical study of sultamicillin fine granules in a variety of pediatric infections |

---

## Singapore Market Information

Sultamicillin is not currently registered in Singapore (0 licenses on file, market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bronchitis is supported by a consistent, decades-spanning body of open-label and cohort literature (1984–1993) showing efficacy in acute bronchitis and exacerbations of chronic bronchitis, aligned with Sultamicillin's known antibacterial spectrum. However, evidence is limited to older non-RCT studies, no trials are registered, and the drug is not currently marketed in Singapore — hence guardrails rather than an unconditional "Go."

**To proceed, the following is needed:**
- Local (HSA) safety labeling — warnings and contraindications data are currently a blocking gap (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- A market entry/registration assessment for Singapore, since the drug has zero existing local licenses
- Note: Ranks 2–10 in this evidence pack (thrombotic disease, heparin cofactor 2 deficiency, rheumatoid arthritis, etc.) are largely unsupported KG artifacts (L4–L5, mostly "Hold") and are not recommended for further action at this time.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

