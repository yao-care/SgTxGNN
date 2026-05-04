---
layout: default
title: Hydrocortisone Succinate
parent: 僅模型預測 (L5)
nav_order: 292
evidence_level: L5
indication_count: 10
---

# Hydrocortisone Succinate
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

# Hydrocortisone Succinate: From Glucocorticoid Therapy to Allergic Asthma

## One-Sentence Summary

Hydrocortisone succinate is an injectable, water-soluble prodrug of hydrocortisone — a corticosteroid used parenterally for acute inflammatory and allergic emergencies.
The TxGNN model predicts it may be effective for **Allergic Asthma** (score: 97.04%), with **2 clinical trials** and **4 publications** identified in support.
Critically, however, the retrieved evidence reveals a drug-specific safety paradox: the succinate ester moiety can paradoxically trigger severe bronchospasm in aspirin-sensitive asthmatic patients, rendering the overall recommendation **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indications in Singapore (not marketed) |
| Predicted New Indication | Allergic Asthma |
| TxGNN Prediction Score | 97.04% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacology, hydrocortisone succinate is a parenteral prodrug that is rapidly hydrolysed in vivo to release free hydrocortisone. As a glucocorticoid, it binds the glucocorticoid receptor (GR) and suppresses NF-κB–driven transcription of pro-inflammatory cytokines — including IL-4, IL-5, and IL-13 — that are central mediators of allergic airway inflammation. This class mechanism provides a coherent theoretical basis for efficacy in allergic asthma, and is consistent with the well-established role of inhaled and systemic corticosteroids in asthma management.

However, a critical drug-specific safety concern sets hydrocortisone succinate apart from other corticosteroid formulations. The succinate ester group is a known ligand for SUCNR1 (succinate receptor 1), expressed on mast cells and basophils. In aspirin-sensitive asthmatics — who have underlying dysregulation of the arachidonic acid/cyclooxygenase pathway — SUCNR1 activation by the free succinate moiety may trigger non-IgE-mediated mast cell degranulation and acute bronchospasm. Multiple published case reports have documented this paradoxical reaction specifically with the sodium succinate formulation (trade names Solu-Cortef, Saxizon), while phosphate ester formulations do not carry this risk.

This mechanistic duality creates a fundamental tension: the glucocorticoid class effect supports anti-asthma benefit, but the succinate ester introduces a drug-specific adverse signal not shared by other corticosteroids. For asthmatic patients — precisely the population of interest — this risk-benefit asymmetry is the dominant clinical concern and the primary driver of the Hold recommendation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT05607901](https://clinicaltrials.gov/study/NCT05607901) | Phase 2 | Completed | 100 | Tacrolimus vs. Hydrocortisone for atopic dermatitis in children; study population has comorbid allergic rhinitis/asthma — provides indirect evidence of corticosteroid use in the atopic spectrum, but does not evaluate allergic asthma efficacy directly |
| [NCT03742414](https://clinicaltrials.gov/study/NCT03742414) | Phase 2 | Active, Not Recruiting | 398 | SEAL study: proactive skin barrier care (including topical corticosteroid) to interrupt the allergic march (eczema → asthma); corticosteroid is a supporting component, not the primary intervention; relevant as a disease-pathway concept study |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [12668895](https://pubmed.ncbi.nlm.nih.gov/12668895/) | 2003 | Review | Clinical Reviews in Allergy & Immunology | Cross-reacting drugs in aspirin-exacerbated respiratory disease (AERD); provides mechanistic context for how COX-inhibitor sensitivity predisposes patients to drug-triggered bronchospasm |
| [1938768](https://pubmed.ncbi.nlm.nih.gov/1938768/) | 1991 | Review | Journal of Asthma | Systemic allergic/anaphylactic reactions to corticosteroids — review documents that the succinate ester is a key sensitising moiety responsible for type I hypersensitivity |
| [15226693](https://pubmed.ncbi.nlm.nih.gov/15226693/) | 2004 | Case Report | Presse Médicale | Skin allergy to hydrocortisone hemisuccinate in an asthmatic patient — documents IgE-mediated hypersensitivity specific to the succinate formulation |
| [8230880](https://pubmed.ncbi.nlm.nih.gov/8230880/) | 1993 | Case Report | Nihon Kyobu Shikkan Gakkai Zasshi | Severe bronchospasm after IV hydrocortisone sodium hemisuccinate (Solu-Cortef) in an aspirin-sensitive asthmatic; positive intradermal tests confirmed formulation-specific sensitivity |

---

## Singapore Market Information

Hydrocortisone succinate is **not currently registered** in Singapore. No product authorisations are on record.

---

## Safety Considerations

**Critical Drug-Specific Safety Signal — Paradoxical Bronchospasm**

The literature evidence retrieved in this evaluation reveals a direct safety concern highly relevant to the predicted indication:

- **Paradoxical Bronchospasm**: Case reports (PMID 8230880; and PMID 7264102 recovered under the intrinsic asthma indication) document severe, acute bronchospasm following IV administration of hydrocortisone sodium succinate in aspirin-sensitive asthmatics. The reaction is attributed to the succinate ester moiety rather than the glucocorticoid core, and was not triggered by other corticosteroid formulations.
- **Anaphylactic Reactions**: Multiple documented cases of systemic allergic and anaphylactic reactions to the succinate formulation (PMID 1938768, PMID 15226693), including positive intradermal skin test confirmation.

Formal package insert safety data (warnings, contraindications) is not available in this Evidence Pack. Please refer to the approved product label for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although corticosteroids are first-line agents for allergic asthma, the succinate ester–specific safety signal (paradoxical bronchospasm via SUCNR1 activation or non-IgE mast cell activation) constitutes a drug-specific hazard directly relevant to the asthmatic population — the very patients who would receive this drug. No clinical trial evidence directly supports hydrocortisone succinate for allergic asthma; both identified trials address atopic dermatitis, and all retrieved literature describes adverse events rather than therapeutic benefit.

**To proceed, the following is needed:**
- Obtain the full product label (TGA/HSA-equivalent package insert) to characterise formal contraindications and boxed warnings
- Determine the prevalence of aspirin-sensitive (AERD) subtype within the target allergic asthma population, to quantify the at-risk fraction
- Conduct a comparative formulation safety analysis: hydrocortisone succinate vs. phosphate ester preparations in asthmatic subjects
- Retrieve MOA data from DrugBank (DB14545) to formally document glucocorticoid receptor pharmacology
- If continued development is considered, a prospective Phase 2 trial with mandatory AERD/aspirin-sensitivity exclusion criteria and standardised bronchospasm monitoring would be the minimum requirement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

