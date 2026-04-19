# Dacomitinib: From Non-Small Cell Lung Cancer to Pulmonary Hypertension

## One-Sentence Summary

Dacomitinib (Vizimpro®) is a second-generation, irreversible pan-ErbB tyrosine kinase inhibitor originally approved for EGFR-mutant non-small cell lung cancer (NSCLC).
The TxGNN model's highest-scored prediction is **rheumatoid arthritis** (97.79%), but **pulmonary hypertension** (rank #4, 96.51%) carries the strongest translational evidence across all 10 candidates.
Currently **1 direct preclinical study** (PMID 30753867) and **1 related clinical trial** (NCT01121575) support this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | EGFR-mutant non-small cell lung cancer (NSCLC) |
| Predicted New Indication (Best Evidence) | Pulmonary Hypertension (Rank #4 of 10; Top TxGNN prediction: Rheumatoid Arthritis) |
| TxGNN Prediction Score | 96.51% (Pulmonary Hypertension) / 97.79% (Top-ranked: Rheumatoid Arthritis) |
| Evidence Level | L3 — 1 preclinical animal study + 1 indirect clinical trial |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available from the regulatory dataset. Based on published pharmacology, Dacomitinib is a second-generation, irreversible pan-ErbB (EGFR/HER1, HER2, HER4) tyrosine kinase inhibitor. Unlike first-generation reversible EGFR inhibitors (erlotinib, gefitinib), Dacomitinib covalently binds to the ATP-binding pocket of all catalytically active ErbB family members, resulting in broader and more sustained pathway suppression. Its original clinical indication — EGFR-mutant NSCLC — established robust human safety and pharmacokinetic data at clinically tolerable doses.

In pulmonary arterial hypertension (PAH), EGFR/ErbB signalling drives abnormal proliferation and apoptosis resistance of pulmonary artery smooth muscle cells (PASMCs), a central mechanism in pulmonary vascular remodelling. EGFR ligands such as EGF and TGF-α are overexpressed in the lung tissue of PAH patients, creating a self-sustaining autocrine/paracrine loop that thickens vascular walls and progressively raises pulmonary vascular resistance (PVR). This mechanistic link was directly tested in a dedicated animal study: PMID 30753867 (Yu et al., 2019, *European Journal of Pharmacology*) demonstrated that Dacomitinib attenuated hypoxia- and monocrotaline-induced right ventricular hypertension and vascular remodelling in rats — providing the first direct preclinical proof-of-concept for this repurposing hypothesis.

One critical caveat warrants emphasis: earlier first-generation EGFR inhibitors (gefitinib, erlotinib, lapatinib) were explored for PAH and failed to produce meaningful clinical benefit. Dacomitinib's pan-ErbB irreversible binding profile may confer mechanistic advantages, but this remains entirely unestablished in human PAH cohorts. The evidence base is preclinical only, and translation to human disease requires a formally designed validation programme.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01121575](https://clinicaltrials.gov/study/NCT01121575) | Phase 1 | Completed | 70 | Dose-escalation safety, PK, and PD study of combined crizotinib (c-MET/ALK) + dacomitinib (pan-HER) in advanced NSCLC patients who developed acquired resistance to first-generation EGFR inhibitors. Not designed for pulmonary hypertension — no PH-specific endpoints (6MWD, PVR, NT-proBNP). Provides human tolerability and pharmacokinetic baseline data informing dose selection for future PAH-specific trial design. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [30753867](https://pubmed.ncbi.nlm.nih.gov/30753867/) | 2019 | Preclinical (in vitro + rodent model) | European Journal of Pharmacology | Dacomitinib significantly attenuated pulmonary vascular remodelling and right ventricular systolic pressure in both hypoxia-induced and monocrotaline-induced PAH rat models. Results indicate pan-EGFR inhibition via Dacomitinib suppresses PASMC proliferation and promotes apoptosis, representing the only direct preclinical study of this drug in PAH to date. |

---

## Singapore Market Information

Dacomitinib is **not registered** with the Health Sciences Authority (HSA) of Singapore. No product licences, authorisation numbers, or approved indications are currently on record. Any clinical use in Singapore would require special access pathways (e.g., Compassionate Use, Clinical Trial Authorisation, or Therapeutic Products import permit).

---

## Cytotoxicity

Dacomitinib is an antineoplastic targeted therapy (EGFR-mutant NSCLC indication). The following cytotoxicity profile applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — 2nd-generation irreversible pan-ErbB (EGFR/HER2/HER4) tyrosine kinase inhibitor; not a conventional cytotoxic agent |
| Myelosuppression Risk | Low — TKI class does not directly target haematopoietic progenitor cells; clinically reported myelosuppression is uncommon |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function (ALT, AST, total bilirubin); CBC with differential; renal function; pulmonary function / HRCT for interstitial lung disease (ILD); dermatologic assessment (acneiform rash, paronychia, dry skin); stomatitis; diarrhoea severity grading |
| Handling Protection | Standard oral antineoplastic handling precautions apply; closed-system transfer recommended during dose preparation; cytotoxic waste disposal per local regulations |

---

## Safety Considerations

Singapore-specific regulatory safety data (HSA-approved package insert, local warnings, and contraindications) is currently unavailable as Dacomitinib is not registered with HSA. Please refer to the **FDA-approved Vizimpro® prescribing information** or **EMA SmPC** for complete safety data, including class-specific warnings for ILD/pneumonitis, dermatologic toxicity, embryo-foetal toxicity, and QTc prolongation risk.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The EGFR/ErbB → PASMC proliferation axis provides a biologically coherent mechanistic link between Dacomitinib and pulmonary arterial hypertension, and the preclinical animal data (PMID 30753867) offers direct proof-of-concept. However, with only one rodent study, no human PAH trial, and a track record of failed earlier-generation EGFR inhibitors in PAH, the evidence base is insufficient to justify clinical translation without a structured validation programme.

**To proceed, the following is needed:**

- **Preclinical package expansion**: Confirmatory studies across additional PAH models (SuHx rat, large-animal models), dose-response characterisation, right ventricular function as an independent endpoint, and chronic toxicity profiling at PAH-relevant doses
- **Pharmacokinetic modelling**: Assessment of lung tissue Dacomitinib exposure at clinically tolerable doses relative to EGFR IC₅₀ in PAH-relevant cell types
- **Mechanism of action data**: Formal retrieval from DrugBank API to support mechanistic rationale documentation (Data Gap DG002)
- **Singapore safety data**: HSA package insert / TFDA product monograph retrieval to enable S1 safety screening and identify contraindications relevant to PAH patient population (Data Gap DG001 — currently Blocking)
- **Regulatory pathway scoping**: Evaluate orphan drug designation eligibility (PAH is a rare disease), IND/CTA requirements, and HSA therapeutic product import permit pathway for investigator-initiated trial use
- **Phase 1b/2a trial design**: If the preclinical package is supportive, design a proof-of-concept study in WHO Group 1 PAH patients (add-on to background therapy), with primary endpoints of PVR and 6-minute walk distance at 12–16 weeks