---
layout: default
title: Cetirizine
parent: 僅模型預測 (L5)
nav_order: 230
evidence_level: L5
indication_count: 10
---

# Cetirizine
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

# Cetirizine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Cetirizine is a second-generation, non-sedating H1 antihistamine widely used internationally for allergic rhinitis and related allergic conditions, though it currently holds no registration in Singapore.
The TxGNN model predicts it may be effective for **Allergic Urticaria**,
with **3 clinical trials** and **18 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis, hay fever (established global use; no Singapore registration on record) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cetirizine is a selective, potent histamine H1-receptor antagonist and the carboxylated metabolite of hydroxyzine. It binds peripheral H1 receptors with high affinity while showing minimal central nervous system penetration at standard doses (10 mg daily), which explains its low-sedation profile compared to first-generation antihistamines. Crucially, cetirizine exerts anti-inflammatory effects beyond pure receptor blockade: it inhibits eosinophil chemotaxis and suppresses mast cell degranulation during the late-phase allergic response, giving it a dual mechanism of action particularly relevant to urticaria.

Allergic urticaria is characterised by IgE-mediated mast cell activation triggered by allergen exposure, releasing histamine that binds H1 receptors on dermal blood vessels and nerve endings to produce the hallmark wheal-and-flare reaction. Cetirizine directly targets this core pathophysiology — blocking the immediate H1-mediated vascular response while also attenuating the secondary inflammatory cascade involving eosinophil recruitment and further mediator release. This mechanistic alignment is exceptionally strong.

Globally, cetirizine has been a cornerstone first-line treatment for chronic spontaneous urticaria (CSU) for over three decades, endorsed in EAACI/GA²LEN/EDF international guidelines. In 2019, the US FDA approved an intravenous cetirizine formulation specifically for acute urticaria, further cementing its role in this indication. The TxGNN prediction score of 99.99% accurately reflects this well-validated mechanistic and clinical fit. The primary opportunity in Singapore is to establish formal HSA registration to enable structured prescribing within the local healthcare system.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Multicenter, double-blind pilot Phase 3 study comparing IV cetirizine injection (10 mg) vs. IV diphenhydramine (50 mg) in acute urticaria patients presenting to emergency departments, urgent care centres, and allergy clinics |
| [NCT03296358](https://clinicaltrials.gov/study/NCT03296358) | N/A | Completed | 75 | Randomised, double-blind trial evaluating whether adding a short burst of corticosteroid to conventional H1 antihistamine treatment improves outcomes in urticaria; cetirizine represents the standard background therapy tested |
| [NCT01008592](https://clinicaltrials.gov/study/NCT01008592) | N/A | Terminated | 11 | Levocetirizine (the active R-enantiomer of cetirizine) in symptomatic dermatographism and chronic idiopathic urticaria; assessed skin levels of histamine, prostaglandin E2, leukotriene B4, and cathepsins — terminated early due to insufficient enrolment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7645679](https://pubmed.ncbi.nlm.nih.gov/7645679/) | 1995 | Clinical Study (RCT/Controlled) | Allergy | Direct clinical trials of cetirizine in allergic rhinitis and chronic urticaria, establishing its efficacy profile across allergic indications |
| [33030434](https://pubmed.ncbi.nlm.nih.gov/33030434/) | 2021 | Systematic Review | J Investig Allergol Clin Immunol | Critical review of up-dosing second-generation antihistamines (including cetirizine, up to 4× licensed dose) in chronic spontaneous urticaria; confirms first-line guideline status |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Comprehensive Review | Drugs | Foundational pharmacological review of cetirizine; confirms controlled trial efficacy in urticaria with documentation of anti-inflammatory effects including histamine release inhibition and eosinophil chemotaxis suppression |
| [7510611](https://pubmed.ncbi.nlm.nih.gov/7510611/) | 1993 | Review | Drugs | Reappraisal of cetirizine's pharmacological properties; confirms efficacy and tolerability in chronic idiopathic urticaria in adults and children at 10 mg/day |
| [8477125](https://pubmed.ncbi.nlm.nih.gov/8477125/) | 1993 | Review | Ann Pharmacother | Introduction of cetirizine as a non-sedating antihistamine; reviews mechanism, chemistry, and clinical/comparative trials demonstrating urticaria efficacy |
| [9951950](https://pubmed.ncbi.nlm.nih.gov/9951950/) | 1999 | Comparative Review | Drugs | Comparative review of second-generation antihistamines including cetirizine; evaluates sedation, anticholinergic profiles, and clinical efficacy across urticaria and rhinitis |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Review of first- and newer-generation antihistamine efficacy and safety for chronic idiopathic urticaria, with emphasis on pharmacy practice management |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Review | Drugs | Urticaria recognition, causes, and treatment overview; identifies non-sedating antihistamines including cetirizine as the mainstay of chronic idiopathic urticaria management |
| [41602253](https://pubmed.ncbi.nlm.nih.gov/41602253/) | 2025 | Case Report | Cureus | Reports rebound pruritus and urticaria following discontinuation of long-term cetirizine use in a Chinese patient in Singapore — directly relevant to Singapore practice and highlights long-term use and withdrawal considerations in Asian populations |
| [27110120](https://pubmed.ncbi.nlm.nih.gov/27110120/) | 2016 | Review | Ther Clin Risk Manag | Review of antihistamine treatment for allergic rhinitis and urticaria in Asia-Pacific populations; cetirizine serves as the benchmark comparator, providing regional treatment landscape context |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cetirizine has an exceptionally well-established safety and efficacy profile for allergic urticaria, backed by decades of global clinical use, a completed Phase 3 study of IV cetirizine for acute urticaria, and first-line status in international allergy guidelines; the TxGNN prediction score of 99.99% accurately reflects this strong evidence base. The primary gap is formal Singapore HSA registration rather than any clinical uncertainty about efficacy or safety.

**To proceed, the following is needed:**
- Singapore HSA Product Licence application with a complete product dossier conforming to ASEAN Common Technical Dossier (ACTD) format
- HSA-compliant package insert incorporating key warnings, contraindications, and drug interaction data (currently absent from Evidence Pack — data gaps DG001 and DG002)
- Formal mechanism of action documentation sourced from DrugBank API to support labelling accuracy
- Singapore-specific pharmacovigilance plan and post-marketing surveillance framework
- Evaluation of appropriate dosage forms for the local market (oral tablet, oral solution) and assessment of OTC vs. prescription classification
- Paediatric dosing and safety review, as allergic urticaria affects children as well as adults in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

