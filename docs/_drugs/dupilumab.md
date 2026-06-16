---
layout: default
title: Dupilumab
parent: 僅模型預測 (L5)
nav_order: 355
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# Dupilumab: From Atopic Dermatitis to Bronchitis

## One-Sentence Summary

Dupilumab is a fully human monoclonal antibody targeting the IL-4 receptor α subunit (IL-4Rα), globally approved for atopic dermatitis, moderate-to-severe asthma, and chronic rhinosinusitis with nasal polyps — but not yet registered in Singapore.
The TxGNN model predicts it may be effective for **Bronchitis**, with **1 clinical trial** and **6 publications** currently supporting this direction.
The broader Dupilumab pipeline also yields a high-confidence prediction for **Atopic Dermatitis** (Rank 2, L1 evidence, "Proceed with Guardrails") — an indication already globally approved but absent from the Singapore market.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Globally approved for atopic dermatitis, moderate-to-severe asthma, and CRS with nasal polyps (not registered in Singapore) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (Research Phase) |

---

## Why is This Prediction Reasonable?

Dupilumab is a fully human IgG4 monoclonal antibody that blocks the shared IL-4Rα subunit of the IL-4 and IL-13 receptors, thereby suppressing downstream JAK1/TYK2–STAT6 signalling — the central axis of type 2 (Th2) inflammatory diseases. Although detailed mechanism of action data was not available in this evidence pack, this target biology is well-established across multiple regulatory-approved indications. Dupilumab's efficacy in atopic dermatitis and asthma has been confirmed in landmark Phase 3 trials (LIBERTY AD, QUEST), validating IL-4/IL-13 blockade as a clinically meaningful approach to Th2-driven diseases.

The mechanistic link to bronchitis is grounded in the "united airway disease" concept. IL-4 and IL-13 drive goblet cell hyperplasia, excessive mucus secretion, subepithelial fibrosis, and eosinophilic airway infiltration — all hallmark pathological features of chronic and eosinophilic bronchitis. Dupilumab's blockade of IL-4Rα can theoretically attenuate these processes by reducing airway hyperresponsiveness, mucus hypersecretion, and eosinophil-mediated tissue remodelling. This shared inflammatory architecture with asthma (already an approved indication) makes biological plausibility for bronchitis strong.

However, bronchitis is a heterogeneous clinical entity: infectious bronchitis (viral or bacterial) and smoking-induced chronic bronchitis involve predominantly non-Th2 pathways, and dupilumab would offer limited benefit in these subgroups. The actionable target population is **eosinophilic or Th2-dominant bronchitis**, where biomarker stratification (blood eosinophil count, FeNO, serum IgE) would be essential to identify likely responders. Indirect clinical support comes from the Phase 3 asthma RCT programme and the COPD eosinophilic phenotype literature; no dedicated bronchitis RCT currently exists.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | Completed | 33 | Dupilumab in chronic rhinosinusitis without nasal polyps (CRSsNP). Shares Th2-driven upper/lower airway inflammation mechanism with bronchitis (united airway disease concept), but anatomically distinct from bronchitis. Small sample (n=33); findings cannot be directly extrapolated to bronchitis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | Phase 3 RCT Extension (open-label) | The Lancet. Respiratory Medicine | TRAVERSE study: long-term (>1 year) safety and sustained efficacy of dupilumab in moderate-to-severe asthma. Confirms durable suppression of Th2 airway inflammation — the mechanistic basis shared with eosinophilic bronchitis. |
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Meta-analysis | The Journal of Asthma | Meta-analysis of multiple RCTs: dupilumab significantly reduced exacerbation rates and improved FEV1 in uncontrolled asthma. Provides pooled evidence for IL-4/IL-13 pathway suppression across airway disease. |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Comprehensive Review | Tuberculosis and Respiratory Diseases | Reviews pharmacologic strategies for COPD exacerbation prevention including novel biologics; contextualises dupilumab's emerging role in eosinophilic airway disease and highlights evidence gaps in chronic bronchitis. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Narrative Review | Expert Opinion on Pharmacotherapy | Examines management of asthma with smoking-induced airway diseases including chronic bronchitis and asthma-COPD overlap (ACO); highlights exclusion of these patients from most trials and the resulting evidence gap for biologics. |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Case Series / Review | Pediatric Pulmonology | Novel therapies for eosinophilic plastic bronchitis in paediatric patients; documents emerging use of dupilumab and other Th2-targeting biologics as treatment options, offering preliminary real-world support. |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Prospective Observational / Mechanistic | Chest | MRI lung ventilation study in severe prednisone-dependent asthma treated with anti-T2 biologics; demonstrates that eosinophil-driven airway obstruction is reversible with IL-4/IL-13 blockade, providing direct mechanistic support for extension to bronchitis. |

---

## Singapore Market Information

Dupilumab (Dupixent®) currently has **no Singapore Health Sciences Authority (HSA) registrations**. It is not listed as a marketed product in Singapore. The drug holds regulatory approval in the United States (FDA, 2017), European Union (EMA, 2017), Japan, and multiple other jurisdictions for atopic dermatitis, asthma, CRS with nasal polyps, prurigo nodularis, and eosinophilic oesophagitis — none of which have been translated into Singapore market authorisation.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for Singapore market entry:** The absence of HSA registration means that Singapore-specific package insert data, local pharmacovigilance data, and TFDA (Taiwan FDA) label warnings are not currently available in this evidence pack. Before any regulatory submission or clinical use, the following safety documentation should be obtained: (1) full prescribing information from FDA/EMA, (2) post-marketing pharmacovigilance reports, and (3) any Asian population-specific safety signals from Japan PMDA or Korean MFDS approvals.

---

## Conclusion and Next Steps

**Decision: Hold (Research Phase)**

**Rationale:**
The mechanistic case for dupilumab in eosinophilic/Th2-dominant bronchitis is biologically sound, but current evidence is indirect — comprising one small Phase 2 trial in upper airway disease and mechanistic extrapolation from asthma studies. No dedicated bronchitis RCT exists, placing this firmly at Evidence Level L3 and warranting a research-phase designation rather than immediate development. Additionally, Dupilumab has no Singapore regulatory foothold, making a bronchitis indication a distant secondary priority compared to establishing baseline atopic dermatitis registration.

**To proceed, the following is needed:**

- **Priority 1 — Singapore market baseline:** Initiate HSA registration for the primary indication (atopic dermatitis, L1 evidence, globally approved), which would establish a Singapore regulatory presence as the prerequisite for further indication expansion
- **Priority 2 — Indication-specific trial:** A Phase 2 RCT in clearly defined eosinophilic bronchitis (biomarker-stratified: blood eosinophils ≥300/µL or FeNO ≥25 ppb) is needed to generate direct clinical evidence
- **Biomarker strategy:** Identify and validate patient selection criteria distinguishing Th2-dominant bronchitis from infectious or smoking-induced subtypes, to avoid diluting trial results with non-responsive populations
- **MOA documentation:** Obtain complete Dupilumab mechanism of action data from DrugBank API and package insert to support the mechanistic rationale section for regulatory submissions
- **Safety package:** Download and parse the FDA/EMA full prescribing information (package insert) to complete the safety assessment, including key warnings, contraindications, and known drug interactions relevant to Singapore prescribing practice
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

