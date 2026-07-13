---
layout: default
title: Fluticasone Furoate
parent: 僅模型預測 (L5)
nav_order: 442
evidence_level: L5
indication_count: 10
---

# Fluticasone Furoate
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

# Fluticasone Furoate: From COPD and Asthma to Atopic Eczema

## One-Sentence Summary

Fluticasone furoate (FF) is a next-generation inhaled corticosteroid with exceptionally high glucocorticoid receptor affinity, globally approved as the core component of Trelegy Ellipta (FF/UMEC/VI) and Relvar Ellipta (FF/VI) for COPD and asthma — though it holds no current registration in Singapore.
The TxGNN model predicts it may be effective for **Atopic Eczema**, with **11 clinical trials** and **2 publications** currently supporting this direction.
Critically, all existing trial evidence derives from the closely related compound fluticasone propionate (FP) rather than fluticasone furoate itself, and no topical skin formulation of FF currently exists — making this a compelling but formulation-constrained repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; globally approved for COPD and asthma (as Trelegy Ellipta / Relvar Ellipta) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacology, fluticasone furoate belongs to the fluorinated corticosteroid class and is a highly potent glucocorticoid receptor (GR) agonist with a receptor relative affinity (RRA) of approximately 2,989 — roughly 29 times that of dexamethasone. Its clinical efficacy in COPD and asthma has been established through landmark Phase 3 trials including IMPACT and FULFIL, where FF-containing regimens significantly reduced exacerbation rates, improved FEV₁, and demonstrated a reduction in all-cause mortality. This positions FF as a high-potency, long-residence ICS with proven systemic anti-inflammatory credibility.

Atopic eczema is driven by a Th2-dominant inflammatory cascade involving cytokines such as IL-4, IL-5, IL-13, TSLP, and IL-33, with downstream mast cell activation and impaired skin barrier function. Glucocorticoid receptor agonism — FF's primary mechanism — can suppress these cytokine pathways at the transcriptional level, theoretically interrupting the self-reinforcing inflammation cycle seen in chronic atopic dermatitis. This mechanistic overlap is precisely why topical corticosteroids are the first-line treatment for eczema flares.

The class-effect support is substantial: the structurally related compound fluticasone propionate (FP), marketed as Cutivate, has been tested in multiple Phase 4 RCTs enrolling hundreds of patients with atopic dermatitis, and consistently serves as the active comparator benchmark against newer agents such as tacrolimus and pimecrolimus. However, a critical limitation distinguishes FF from FP: fluticasone furoate currently exists only in inhaled formulations (Ellipta dry powder inhaler). No approved or investigational topical skin preparation of FF exists, meaning any direct repurposing to atopic eczema would require developing an entirely new dosage form — a substantial pharmaceutical and regulatory hurdle.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|------------|------|--------|-----------|------------|
| [NCT00689832](https://clinicaltrials.gov/study/NCT00689832) | Phase 4 | Completed | 487 | Large multicentre double-blind RCT in children ≥2 years with moderate-to-severe AD; tacrolimus 0.03% vs fluticasone propionate 0.005% ointment — FP serves as the efficacy benchmark establishing class standard of care |
| [NCT00690105](https://clinicaltrials.gov/study/NCT00690105) | Phase 4 | Completed | 577 | Large multicentre double-blind RCT in adults with facial AD ("red face" lesions); tacrolimus 0.1% vs fluticasone propionate ointment for 3–6 weeks — establishes FP's efficacy in moderate-to-severe facial AD |
| [NCT00616538](https://clinicaltrials.gov/study/NCT00616538) | Phase 4 | Completed | 121 | Randomized investigator-blind controlled pilot study in paediatric subjects; EpiCream barrier cream vs fluticasone propionate 0.05% as mid-strength steroid standard of care |
| [NCT01915914](https://clinicaltrials.gov/study/NCT01915914) | Phase 4 | Completed | 107 | Randomized open-label study evaluating FP 0.05% cream administered twice weekly (intermittent regimen) combined with daily moisturisation to reduce relapse risk in paediatric patients with stabilised AD |
| [NCT00119158](https://clinicaltrials.gov/study/NCT00119158) | Phase 4 | Completed | 90 | Exploratory double-blind vehicle-controlled paired study evaluating concomitant use of pimecrolimus cream 1% and Cutivate cream 0.05% in patients with severe AD lesions |
| [NCT00546000](https://clinicaltrials.gov/study/NCT00546000) | Phase 4 | Completed | 56 | Multi-centre open-label study of Cutivate (FP) lotion 0.05% assessing HPA axis effects when used to treat atopic dermatitis in infants |
| [NCT01772056](https://clinicaltrials.gov/study/NCT01772056) | Phase 3 | Terminated | 54 | Double-blind RCT of twice-weekly FP 0.05% cream for 16-week maintenance treatment to reduce relapse in mild-to-moderate AD in children; terminated prior to completion |
| [NCT03742414](https://clinicaltrials.gov/study/NCT03742414) | Phase 2 | Active, not recruiting | 398 | SEAL (Stopping Eczema and ALlergy) study: proactive sequential skin care (EpiCream + FP cream) vs reactive AD therapy in infants with early-onset AD to prevent the allergic march and food allergy |
| [NCT04706559](https://clinicaltrials.gov/study/NCT04706559) | N/A | Completed | 98 | Probiotic supplementation in children with AD assessed by SCORAD index; fluticasone used as background standard-of-care comparator rather than primary intervention |
| [NCT03594565](https://clinicaltrials.gov/study/NCT03594565) | Early Phase 1 | Completed | 13 | Small exploratory case series of topical nasal steroids for CGM sensor-related skin reactions in children with type 1 diabetes; extremely small scale and non-standard AD trial design |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|-----|--------|------------|
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Reviews systemic effects of intranasal corticosteroids on the HPA axis; discusses cumulative corticosteroid burden in patients using ICS for allergic rhinitis, asthma, and atopic dermatitis concurrently — relevant to the safety assessment of FF class effects |
| [40066386](https://pubmed.ncbi.nlm.nih.gov/40066386/) | 2025 | Case Report | Indian Journal of Otolaryngology and Head and Neck Surgery | Case study of allergen immunotherapy (AIT) in autoimmune settings; contextualises AIT use in atopic dermatitis and interactions with corticosteroid therapy |

---

## Singapore Market Information

Fluticasone furoate holds no product registrations with the Health Sciences Authority (HSA) of Singapore. The drug is not currently marketed in Singapore in any dosage form.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
While the TxGNN model assigns a very high prediction score (99.98%) and class-effect evidence from fluticasone propionate is well-established in atopic dermatitis, fluticasone furoate itself has no topical skin formulation, no direct clinical trials in atopic eczema, and no Singapore regulatory registration. The evidence level of L3 reflects indirect, class-effect support rather than FF-specific data, making this a scientifically plausible but pre-translational hypothesis requiring substantial development work before clinical evaluation is feasible.

**To proceed, the following is needed:**

- **Topical formulation development**: A dermal formulation of fluticasone furoate must be developed from scratch — no such product currently exists in any market
- **FF-specific preclinical skin data**: Direct evidence of FF's pharmacokinetics and efficacy in skin tissue models to confirm transdermal delivery and local GR activation
- **Mechanism of action confirmation**: Full MOA data from DrugBank/literature to formally document GR-binding in skin relative to Th2 pathway suppression
- **HPA axis risk assessment**: Given FF's exceptional GR potency (RRA ~2,989), any topical formulation will need rigorous systemic absorption and adrenal suppression studies
- **Head-to-head design against FP**: Any future trial must justify FF over the already-established fluticasone propionate (Cutivate) in terms of potency, safety profile, or patient benefit
- **Singapore regulatory pathway**: HSA registration of fluticasone furoate in at least one formulation would be a prerequisite for local development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

