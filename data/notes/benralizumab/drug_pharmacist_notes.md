# Benralizumab: From Severe Eosinophilic Asthma to Dermatitis

## One-Sentence Summary

Benralizumab (Fasenra®) is an anti-IL-5Rα monoclonal antibody approved globally for severe eosinophilic asthma, which depletes eosinophils and basophils via antibody-dependent cell-mediated cytotoxicity (ADCC).
The TxGNN model predicts it may be effective for **Dermatitis** (primarily atopic dermatitis),
with **3 directly relevant clinical trials** and **20 publications** supporting this direction — however, the pivotal Phase 2 RCT (HILLIER study) was **terminated early and reported negative results**, substantially weakening the clinical case for general atopic dermatitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe eosinophilic asthma (add-on maintenance treatment in adults) |
| Predicted New Indication | Dermatitis (Atopic Dermatitis) |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Benralizumab binds with high affinity to IL-5Rα (the alpha subunit of the IL-5 receptor), blocking IL-5 signalling and inducing near-complete, rapid depletion of circulating and tissue eosinophils and basophils via ADCC. Its proven benefit in severe eosinophilic asthma rests precisely on this eosinophil-depleting mechanism — making any eosinophil-driven disease a plausible repurposing target. Currently, detailed MOA data from the DrugBank source is not available in this evidence pack (Data Gap DG002); the above summary is drawn from published literature referenced in the collected trials and publications.

Atopic dermatitis (AD) and eosinophilic asthma share the same upstream inflammatory architecture: ILC2 activation and Th2 skewing drive both conditions, and eosinophils are histologically prominent in AD skin lesions. The IL-5/IL-5Rα axis actively recruits eosinophils to skin, and a 2025 translational study (PMID 40781582) confirmed that Benralizumab does deplete IL-5Rα-bearing cells within AD skin lesions — validating that the drug's mechanism of action physically reaches the target tissue. This mechanistic plausibility is why TxGNN assigned a high prediction score and why two Phase 2 trials were conducted.

However, the clinical results decisively expose the limits of this rationale. AD's core pathological driver is the IL-4/IL-13 axis (not IL-5), which governs epithelial barrier breakdown and keratinocyte dysfunction. Depleting eosinophils without interrupting IL-4/IL-13 signalling is insufficient to resolve AD symptoms — a hypothesis now confirmed by the HILLIER trial's null result. One important exception is **DRESS** (Drug Reaction with Eosinophilia and Systemic Symptoms), a distinct dermatitis subtype where eosinophils are the central pathological mediators; a Phase 2 trial in DRESS (NCT06734884) is planned, representing a narrower but mechanistically better-justified opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04605094](https://clinicaltrials.gov/study/NCT04605094) | Phase 2 | Terminated | 194 | **HILLIER study** — multinational, randomised, double-blind, placebo-controlled RCT of Benralizumab vs placebo in moderate-to-severe atopic dermatitis. Terminated early; published results (PMID 37178404) confirm **no significant effect** on AD signs or symptoms. Strongest available evidence — and it is negative. |
| [NCT03563066](https://clinicaltrials.gov/study/NCT03563066) | Phase 2 | Completed | 20 | Proof-of-concept study in atopic dermatitis evaluating Benralizumab's effects on eosinophils, basophils, and ILC2s in skin. Very small sample (n=20); likely corresponds to the translational findings in PMID 40781582. Mechanistic insights only — cannot support efficacy claim. |
| [NCT06734884](https://clinicaltrials.gov/study/NCT06734884) | Phase 2 | Not Yet Recruiting | 96 | Benralizumab in **DRESS** (drug reaction with eosinophilia and systemic symptoms) — eosinophil-centric dermatitis subtype where IL-5Rα inhibition has stronger mechanistic rationale. Estimated completion September 2029; no results yet available. |
| [NCT04126499](https://clinicaltrials.gov/study/NCT04126499) | N/A (Observational) | Completed | 28 | Retrospective observational study of Benralizumab in severe eosinophilic asthma (Spain individualized access programme). No efficacy assessment; limited real-world safety data only. |
| [NCT04763447](https://clinicaltrials.gov/study/NCT04763447) | Phase 4 | Recruiting | 234 | Tests Omalizumab (anti-IgE) withdrawal in well-controlled severe allergic asthma — **different drug and different target**; no direct relevance to Benralizumab or dermatitis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37178404](https://pubmed.ncbi.nlm.nih.gov/37178404/) | 2023 | Phase 2 RCT Report | JEADV | **HILLIER trial primary publication**: Benralizumab shows **no significant effect** on signs and symptoms of moderate-to-severe atopic dermatitis. Primary endpoint not met. Key negative evidence for this indication. |
| [38695680](https://pubmed.ncbi.nlm.nih.gov/38695680/) | 2024 | Phase 2 RCT (Plain Language Summary) | Immunotherapy | Plain-language summary of the HILLIER study confirming the null result; reinforces and disseminates the negative conclusion from the pivotal trial. |
| [40781582](https://pubmed.ncbi.nlm.nih.gov/40781582/) | 2025 | Translational / Mechanistic Study | Clinical and Translational Allergy | Benralizumab depletes IL-5Rα-bearing cells in AD skin lesions — confirms biological target engagement in skin tissue, but clinical benefit (per HILLIER) remains unproven. |
| [39234416](https://pubmed.ncbi.nlm.nih.gov/39234416/) | 2024 | Mechanistic Study | J Allergy Clin Immunol Global | Effect of Benralizumab on skin inflammation after intradermal allergen challenge in AD — provides further mechanistic detail on eosinophil dynamics in the skin. |
| [36411004](https://pubmed.ncbi.nlm.nih.gov/36411004/) | 2023 | Review | Immunology and Allergy Clinics of North America | Reviews biologics (including Benralizumab) for atopic diseases during pregnancy and lactation; relevant for special population safety assessment. |
| [35987486](https://pubmed.ncbi.nlm.nih.gov/35987486/) | 2022 | Safety Review | J Allergy Clin Immunol In Practice | Safety of 7 FDA-approved biologics (including Benralizumab) during pregnancy; summarises maternal and foetal outcome data. |
| [31690400](https://pubmed.ncbi.nlm.nih.gov/31690400/) | 2019 | Review | Allergy and Asthma Proceedings | Reviews immunobiologics for severe asthma, AD, and urticaria; contextualises Benralizumab alongside other anti-IL-5 agents and dupilumab. |
| [36270814](https://pubmed.ncbi.nlm.nih.gov/36270814/) | 2023 | Case Report | Therapie | **Benralizumab-induced interstitial granulomatous dermatitis** — paradoxical adverse skin reaction reported during asthma treatment; safety signal directly relevant to dermatitis use. |
| [38035014](https://pubmed.ncbi.nlm.nih.gov/38035014/) | 2023 | Pharmacovigilance (FAERS) Study | Frontiers in Pharmacology | Disproportionality analysis identifies a **parasitic infection safety signal** for anti-type 2 immunity mAbs including Benralizumab — eosinophil depletion may impair helminth defence. |
| [38878020](https://pubmed.ncbi.nlm.nih.gov/38878020/) | 2024 | Observational Study | Journal of Allergy and Clinical Immunology | Patients on Benralizumab, dupilumab, or mepolizumab show **reduced post-vaccination SARS-CoV-2 immunity** — vaccine response attenuation signal relevant for immunocompromised risk assessment. |

---

## Singapore Market Information

Benralizumab is currently **not registered** in Singapore. No product authorisations were found in the Health Sciences Authority (HSA) database as of the data cutoff (10 April 2026).

> For reference, Benralizumab (Fasenra®) holds regulatory approval in the United States (FDA), European Union (EMA), Japan (PMDA), and multiple other markets for add-on maintenance treatment of severe eosinophilic asthma in adults. Any clinical use in Singapore would require HSA approval, a compassionate use application, or a clinical trial authorisation.

---

## Safety Considerations

Official Singapore/Taiwan package insert warnings and contraindications are not available for this report (Data Gap DG001 — Blocking severity). The following signals are drawn from collected literature only and do not substitute for a formal label review.

- **Parasitic infection risk**: FAERS pharmacovigilance analysis (PMID 38035014) identified a disproportionate signal for helminth and other parasitic infections across anti-type 2 immunity biologics including Benralizumab. Eosinophil depletion may impair innate anti-helminth defences; patients in endemic regions should be screened and treated for pre-existing helminth infections before initiation.
- **Vaccine response attenuation**: Patients on Benralizumab showed lower post-vaccination SARS-CoV-2 antibody titres compared to controls (PMID 38878020). Vaccination timing relative to biologic dosing should be considered.
- **Paradoxical skin reaction**: A case of Benralizumab-induced interstitial granulomatous dermatitis has been reported (PMID 36270814) — a particularly notable signal given the dermatitis indication being evaluated, and potentially relevant to DRESS trial monitoring.
- No drug-drug interactions were identified in the DDI database query (query status: not found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pivotal Phase 2 RCT (HILLIER study, NCT04605094, n=194) was terminated early, and its published results (PMID 37178404) explicitly confirm that Benralizumab produces **no significant improvement** in moderate-to-severe atopic dermatitis — this constitutes direct, high-quality negative evidence against the primary predicted indication. The underlying biology is now well understood: AD is driven by the IL-4/IL-13 axis, and eosinophil depletion alone is insufficient. The TxGNN model score of 99.16% reflects shared inflammatory pathway membership between asthma and AD at the knowledge-graph level, but does not account for the mechanistic insufficiency revealed by clinical trial data.

A narrow, mechanistically better-justified opportunity exists specifically for **DRESS** (eosinophil-centric dermatitis subtype), where a Phase 2 trial (NCT06734884, n=96) is planned — but completion is not expected until September 2029 and no interim data are available.

**To proceed (for DRESS subtype only), the following is needed:**
- Await primary results from NCT06734884 (Phase 2 DRESS trial; estimated September 2029)
- Obtain the official HSA/TFDA package insert to complete the safety assessment (Data Gap DG001 — Blocking)
- Retrieve DrugBank MOA data to complete mechanistic documentation (Data Gap DG002 — High)
- Confirm Singapore regulatory pathway for compassionate use or clinical trial authorisation, given no current HSA registration
- Conduct a focused literature review to identify any AD endotype (e.g., high eosinophil, low IgE) that retains eosinophil dependence and might respond selectively to IL-5Rα inhibition

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All website content should include a YMYL disclaimer.*