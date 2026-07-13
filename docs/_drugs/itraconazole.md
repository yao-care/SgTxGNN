---
layout: default
title: Itraconazole
parent: 僅模型預測 (L5)
nav_order: 541
evidence_level: L5
indication_count: 10
---

# Itraconazole
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

# Itraconazole: From Fungal Infections to Pneumocystosis

## One-Sentence Summary

Itraconazole is a broad-spectrum triazole antifungal agent, widely used to treat systemic and superficial fungal infections including aspergillosis, histoplasmosis, and onychomycosis.
The TxGNN model predicts it may be effective for **Pneumocystosis** (Pneumocystis jirovecii pneumonia, PCP),
with **0 clinical trials** and **20 publications** currently identified — however, the mechanistic basis for this prediction is critically weak and the evidence does not support clinical use in PCP.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Systemic and superficial fungal infections (not registered in Singapore; no local indication data available) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Itraconazole is a triazole antifungal that works by inhibiting the fungal enzyme CYP51 (Erg11), which is a key enzyme in the ergosterol biosynthesis pathway. Ergosterol is the primary sterol component of most fungal cell membranes, and blocking its production disrupts membrane integrity, ultimately killing susceptible fungi. This mechanism is well-validated across a wide range of clinically important fungi, including *Aspergillus*, *Histoplasma*, *Cryptococcus neoformans*, *Talaromyces marneffei*, and dermatophytes.

The problem is that *Pneumocystis jirovecii* — the causative agent of PCP — is fundamentally different from other fungi in its sterol biology. Unlike typical fungi, *P. jirovecii* contains very little ergosterol in its cell membrane and instead relies on a unique *Pneumocystis*-specific sterol pathway. This makes CYP51/Erg11 inhibition essentially irrelevant to its survival. A 2003 molecular study (PMID 12606318) directly characterised the *P. carinii* PCERG11 gene and found that two key structural positions identical to those conferring azole resistance in other organisms are present, providing a molecular explanation for why azoles do not work against *Pneumocystis*.

The high TxGNN score (99.34%) almost certainly reflects a non-specific knowledge graph connection between the "immunocompromised host" and "opportunistic fungal infection" nodes, rather than a genuine mechanistic prediction for PCP treatment. The 20 identified publications are predominantly indirect — they describe immunosuppressed patient cohorts (AIDS, bone marrow transplant, lung transplant) where PCP occurred alongside other fungal infections, but Itraconazole was used for those other fungal co-infections, not for PCP itself. The standard of care for PCP remains trimethoprim-sulfamethoxazole (TMP-SMX), with pentamidine as salvage therapy. Itraconazole has no established or investigational role in PCP treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Itraconazole in pneumocystosis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review (Guidelines) | BMJ Clinical Evidence | OI prophylaxis guidelines in HIV patients with CD4 < 250/mm³; PCP prophylaxis covered by TMP-SMX; Itraconazole not listed as a PCP treatment option |
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | RCT (Phase III) | HIV Medicine | Double-blind, placebo-controlled trial of Itraconazole prophylaxis to prevent deep fungal infections in HIV patients; not designed for PCP-specific endpoints; indirect evidence only |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Current Clinical Topics in Infectious Diseases | Comprehensive review of prophylaxis and treatment of infections in bone marrow transplant recipients; PCP discussed as a distinct entity requiring TMP-SMX, separate from fungal infection management |
| [12606318](https://pubmed.ncbi.nlm.nih.gov/12606318/) | 2003 | Mechanistic Study | Am J Respir Cell Mol Biol | Cloned and characterised the PCERG11 lanosterol 14α-demethylase from *P. carinii*; identified two structural sites identical to azole-resistance-conferring positions, providing direct molecular explanation for inherent azole resistance in *Pneumocystis* |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case Report | Frontiers in Immunology | *Talaromyces marneffei* + *P. jirovecii* coinfection in a child with STAT1 mutation; Itraconazole used to treat the Talaromyces component — the PCP was managed separately, illustrating that Itraconazole plays no role in PCP treatment even in coinfection settings |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Overview of therapy and prophylaxis for systemic protozoan infections including *Pneumocystis carinii*; standard PCP treatment summarised; antifungal azoles not mentioned as options |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Cohort Review | Seminars in Respiratory Infections | Infections after lung transplantation; PCP prevention protocols discussed as distinct from antifungal prophylaxis; Itraconazole use limited to fungal pathogens |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clinical Pharmacokinetics | Pulmonary epithelial lining fluid penetration of antifungal agents reviewed; Itraconazole ELF concentrations documented, but no data or discussion of activity against *Pneumocystis* |
| [30429396](https://pubmed.ncbi.nlm.nih.gov/30429396/) | 2018 | Observational Study | Indian Journal of Medical Microbiology | Profile of respiratory fungal pathogens in immunocompetent and immunocompromised hosts; PCP treated with TMP-SMX as standard; fungal pathogens and *Pneumocystis* treated as separate categories |
| [22273250](https://pubmed.ncbi.nlm.nih.gov/22273250/) | 2012 | Retrospective Cohort | Leukemia & Lymphoma | Non-bacterial infections in 182 Asian patients treated with alemtuzumab; both PCP and fungal infections documented, but managed by distinct drug classes; no evidence of Itraconazole utility for PCP |

---

## Singapore Market Information

Itraconazole is currently not registered for sale in Singapore. No HSA authorization records are available.

> **Note:** Itraconazole is approved and widely available in many other jurisdictions (e.g., FDA-approved in the United States for histoplasmosis, blastomycosis, aspergillosis, and onychomycosis; EMA-approved in Europe). Its absence from the Singapore registry warrants investigation into local registration pathways if any indication is pursued.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Prescriber note:** Itraconazole is a potent CYP3A4 inhibitor and is associated with clinically significant drug-drug interactions (e.g., with statins, benzodiazepines, anticoagulants, HIV antiretrovirals). Cardiac contraindications (negative inotropic effect) and potential QT prolongation are also established concerns. Formal DDI and contraindication data were not retrievable in this evidence pack; full package insert review is mandatory before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for using Itraconazole in pneumocystosis is fundamentally incompatible — *Pneumocystis jirovecii* is intrinsically resistant to azole antifungals due to its unique low-ergosterol cell membrane and structural alterations in its CYP51/PCERG11 enzyme, as confirmed at the molecular level (PMID 12606318). No clinical trials exist, and none of the 20 identified publications support direct PCP treatment with Itraconazole. The TxGNN score of 99.34% represents a knowledge graph generalisation artefact rather than a valid clinical prediction, and this indication should be deprioritised or removed from the candidate list.

**To proceed, the following is needed:**

- **Deprioritise this indication**: Pneumocystosis should be flagged as a TxGNN false positive and removed from the active repurposing candidate list for Itraconazole
- **Redirect evaluation resources**: The evidence pack contains two higher-quality repurposing candidates that warrant further review:
  - **Rank 2 — Cryptococcal Meningitis** (TxGNN 93.74%, Evidence Level L2, 3 completed clinical trials including Phase 2 RCTs, "Proceed with Guardrails"): Mechanism is sound; main limitation is low CSF penetration compared to Fluconazole
  - **Rank 5 — Penicilliosis / Talaromycosis** (TxGNN 89.01%, Evidence Level L2, Phase 3 trial in progress, WHO guideline-endorsed, "Proceed with Guardrails"): Itraconazole is already standard of care consolidation therapy in endemic regions
- **Address data gaps**: Obtain full Singapore/HSA registration status and package insert for complete safety and contraindication review (DG001); confirm MOA data from DrugBank (DG002)
- **Algorithm feedback**: Log this case as a confirmed false positive to improve future TxGNN prediction filtering for immune-mediated (non-infectious) and inherently-resistant pathogen indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

