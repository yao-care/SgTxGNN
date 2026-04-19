# Aminolevulinic Acid: From High-Grade Glioma Visualization to Pre-Malignant Neoplasm Treatment

## One-Sentence Summary

5-Aminolevulinic acid (5-ALA) is a naturally occurring amino acid and established photosensitizer precursor, globally approved for fluorescence-guided resection of high-grade gliomas (Gleolan®) and treatment of actinic keratosis (Levulan®), but currently holding no Singapore market authorization.
The TxGNN model predicts it may be effective for the broader indication of **Pre-Malignant Neoplasm** (TxGNN score 96.01%), supported by **1 completed Phase 3 RCT** directly targeting pre-malignant lesions and **20 publications** spanning mechanistic, systematic review, and clinical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; globally approved for actinic keratosis (Levulan®) and high-grade glioma fluorescence-guided surgery (Gleolan®) |
| Predicted New Indication | Pre-Malignant Neoplasm |
| TxGNN Prediction Score | 96.01% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established literature, 5-ALA is a naturally occurring intermediate in the haem biosynthetic pathway. When administered exogenously, it is selectively taken up by tumor and pre-malignant cells and metabolized to protoporphyrin IX (PpIX), a potent endogenous photosensitizer. The biochemical basis for this selectivity lies in two enzymatic imbalances characteristic of neoplastic cells: elevated porphobilinogen deaminase (PBGD) activity accelerates PpIX synthesis, while reduced ferrochelatase activity slows PpIX conversion to haem — causing selective PpIX accumulation. Upon illumination with appropriate light wavelengths (typically 630–635 nm red light), the accumulated PpIX generates singlet oxygen (¹O₂) and reactive oxygen species (ROS) that trigger targeted apoptosis and disrupt tumor neovasculature.

The mechanistic link between ALA's existing indications and the broader category of pre-malignant neoplasms is compelling. Actinic keratosis — one of ALA's already-approved indications — is itself a pre-malignant skin condition, meaning the drug has already demonstrated efficacy within this disease category. The same PpIX-accumulation mechanism applies across a spectrum of pre-malignant epithelial tissues including oral mucosa (leukoplakia, erythroplakia), esophageal epithelium (Barrett's esophagus), cervical epithelium, and colonic polyps. A 2016 mechanistic study (PMID 27150264) further identified eukaryotic translation elongation factor 1 alpha 1 (eEF1A1) as a molecular chaperone that actively binds and enriches PpIX within cancer cells, providing a molecular explanation for tumor selectivity across diverse tissue types.

Practical application of this mechanism extends across multiple anatomical sites through adaptable delivery routes: topical cream or gel for skin and oral mucosa, oral solution for systemic distribution and photodynamic diagnosis, intravesical instillation for bladder lesions, and endoscopic or intracavitary delivery for gastrointestinal pre-malignancies. This formulation versatility, combined with the mechanistically consistent PpIX accumulation across pre-malignant epithelial cells, renders the TxGNN prediction biologically robust and clinically translatable.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01497951](https://clinicaltrials.gov/study/NCT01497951) | Phase 3 | Completed | 28 | Randomized controlled trial of PDT vs placebo for premalignant mucosal oral lesions; most directly relevant evidence — ALA-PDT vs sham in oral pre-malignancy with long-term follow-up through 2017 |
| [NCT03638622](https://clinicaltrials.gov/study/NCT03638622) | Phase 1/2 | Completed | 30 | Low-cost image-guided ALA-PDT for oral pre-malignant lesions (India); evaluates feasibility of photodynamic screening and treatment in resource-limited settings — directly targets pre-malignant oral lesions |
| [NCT06507644](https://clinicaltrials.gov/study/NCT06507644) | N/A | Not Yet Recruiting | 144 | Double-blind RCT comparing MAL (ALA methyl ester prodrug) 8% vs 16% with 1 or 3 hour incubation for facial actinic keratoses; rigorous 4-arm design with 6-month follow-up in skin pre-malignancy |
| [NCT00241670](https://clinicaltrials.gov/study/NCT00241670) | Phase 3 | Completed | 415 | Landmark Phase 3 RCT of fluorescence-guided resection with 5-ALA vs conventional resection in malignant gliomas; established ALA as a tumor-selective photosensitizer in brain oncology |
| [NCT01167322](https://clinicaltrials.gov/study/NCT01167322) | Phase 3 | Completed | 45 | Assessment of NPC-07 (5-ALA HCl) positive predictive value, safety, and pharmacokinetics in malignant glioma (WHO Grade III/IV); 20 mg/kg oral dose 3 hours pre-surgery |
| [NCT06160492](https://clinicaltrials.gov/study/NCT06160492) | Phase 3 | Recruiting | 144 | Randomized multicenter Phase 3 trial of 5-ALA fluorescence-guided microsurgery vs white light microsurgical resection in WHO Grade 3/4 malignant gliomas |
| [NCT02191488](https://clinicaltrials.gov/study/NCT02191488) | Phase 1 | Active, Not Recruiting | 540 | Large-scale safety and pharmacodynamics study quantifying ALA-induced PpIX fluorescence during brain tumor resection; establishes the safety baseline for ALA fluorescence applications |
| [NCT06876038](https://clinicaltrials.gov/study/NCT06876038) | Phase 2 | Not Yet Recruiting | 65 | Comprehensive low-cost screening and image-guided PDT platform for pre-malignant and malignant oral lesions in low-resource settings; directly targets oral pre-malignancy |
| [NCT00285701](https://clinicaltrials.gov/study/NCT00285701) | Phase 1/2 | Completed | 38 | Dose-finding study of hexaminolevulinate (HAL, an ALA hexyl ester) for fluorescence endoscopy to detect pre-malignant and malignant colonic conditions; directly supports pre-malignant neoplasm detection |
| [NCT02050243](https://clinicaltrials.gov/study/NCT02050243) | Phase 1/2 | Unknown | 100 | ALA as intraoperative tumor marker for pediatric CNS tumors; demonstrates ALA-PpIX fluorescence applicability across pediatric tumor histologies |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [40614840](https://pubmed.ncbi.nlm.nih.gov/40614840/) | 2025 | RCT (10-yr follow-up) | Photodiagnosis Photodyn Ther | Long-term RCT comparing ALA-PDT, MAL-PDT, and surgery for BCC and pre-malignant lesions; confirms durable efficacy of ALA-based PDT over 10 years in skin pre-malignancy |
| [25315968](https://pubmed.ncbi.nlm.nih.gov/25315968/) | 2015 | Systematic Review | Photodiagnosis Photodyn Ther | Systematic review of PDT efficacy for oral premalignant lesions; highest-tier evidence directly supporting ALA-PDT for oral pre-malignancy management |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | Comprehensive review of combined PDT treatment strategies for non-melanoma skin cancer and pre-malignant lesions (actinic keratosis, Bowen's disease, BCC) |
| [18389144](https://pubmed.ncbi.nlm.nih.gov/18389144/) | 2008 | Review | Photochem Photobiol Sci | Bench-to-bedside review of ALA's clinical applications across dermatology, urology, neurosurgery, gynecology, and gastroenterology for both pre-malignant and malignant diseases |
| [27150264](https://pubmed.ncbi.nlm.nih.gov/27150264/) | 2016 | Mechanistic Study | Scientific Reports | Identifies eEF1A1 as the molecular mechanism that selectively binds and enriches PpIX within cancer cells; explains the tumor selectivity of ALA-PDT at the molecular level |
| [9744510](https://pubmed.ncbi.nlm.nih.gov/9744510/) | 1998 | Clinical-Mechanistic | Br J Cancer | Biochemical basis of ALA-induced PpIX accumulation in (pre)malignant esophageal lesions including Barrett's esophagus; directly measures PBGD and ferrochelatase activities explaining tumor selectivity |
| [39566196](https://pubmed.ncbi.nlm.nih.gov/39566196/) | 2024 | Review/Commentary | Photodiagnosis Photodyn Ther | Clinical review of PDT for early and recurrent oral cancers and pre-malignant lesions; highlights field cancerization treatment potential of ALA in high-prevalence populations |
| [16879035](https://pubmed.ncbi.nlm.nih.gov/16879035/) | 2006 | Clinical Pilot | Photochem Photobiol | In vivo dosimetry study of ALA-PDT for pre-malignant Barrett's esophagus; establishes PpIX fluorescence photobleaching kinetics critical for treatment dosing |
| [31364444](https://pubmed.ncbi.nlm.nih.gov/31364444/) | 2019 | Case Report | J Int Med Res | ALA-PDT successfully treats vulvar intraepithelial neoplasia (VIN) — a pre-malignant gynecological condition — demonstrating applicability in non-dermatological pre-malignancy |
| [22594985](https://pubmed.ncbi.nlm.nih.gov/22594985/) | 2012 | Comparative Clinical Study | Photodiagnosis Photodyn Ther | Direct comparison of ALA-PDT (n=48) vs cryotherapy (n=37) for oral leukoplakia, a pre-malignant lesion; ALA-PDT demonstrated comparable complete response rates with better tolerability |

---

## Singapore Market Information

Aminolevulinic acid (5-ALA) currently holds **no product registrations** with the Singapore Health Sciences Authority (HSA). The drug is not commercially available through authorized channels in Singapore, and there is no local prescribing information or regulatory labeling to reference.

For context, 5-ALA has received approvals in other major jurisdictions:

| Jurisdiction | Product Name | Form | Approved Indication |
|---------|------|------|-----------|
| USA (FDA) | Levulan® Kerastick | Topical solution 20% | Actinic keratosis (non-hyperkeratotic, face/scalp) in combination with BLU-U photodynamic illumination |
| USA (FDA) | Gleolan® | Oral solution powder, 30 mg/mL | Visualization of malignant tissue during fluorescence-guided surgery of high-grade glioma |
| EU (EMA) | Gliolan® | Oral solution powder, 30 mg/mL | Malignant glioma — adult patients with suspected malignant glioma undergoing surgery |
| EU (EMA) | Ameluz® | Gel 78 mg/g | Actinic keratosis (mild-to-moderate) and superficial/nodular basal cell carcinoma |

Any clinical use in Singapore would require either HSA special access authorization, compassionate use application, or importation under the Personal Importation Exemption framework.

---

## Cytotoxicity

5-ALA functions as a photodynamic therapy (PDT) agent used in the management of pre-malignant and malignant neoplasms. While not a conventional cytotoxic chemotherapy, it produces targeted cytotoxic effects in neoplastic tissue through photochemical mechanisms:

| Item | Content |
|------|------|
| Cytotoxicity Classification | Photosensitizer / Photodynamic Therapy (PDT) Agent — not a conventional cytotoxic; selectively generates reactive oxygen species (¹O₂, ROS) in PpIX-accumulating cells upon light activation |
| Myelosuppression Risk | Low — mechanism is photochemical and anatomically localized to illuminated tissue; systemic myelosuppression is not a reported concern |
| Emetogenicity Classification | Low — oral administration may produce mild transient nausea; primary adverse effects are photosensitivity reactions rather than emesis |
| Monitoring Items | Liver function tests (ALT, AST, bilirubin) prior to oral administration; skin photosensitivity status for 24–48 hours post-dose; ophthalmologic protection (UV-blocking glasses) required |
| Handling Protection | Standard photosensitizer precautions: protect prepared solution from light; instruct patients to avoid bright sunlight and strong indoor lighting for minimum 24 hours after oral administration; no specialized cytotoxic handling infrastructure required |

---

## Safety Considerations

All Singapore-specific safety data are unavailable as the drug is not registered locally. Based on international prescribing information (Gleolan®/Levulan®):

- **Photosensitivity**: Patients must avoid exposure to bright sunlight or intense indoor lighting for at least 24 hours post-administration; phototoxic skin reactions (erythema, burning, stinging) are the primary adverse effect
- **Hepatotoxicity**: Transient liver enzyme elevations have been reported; pre-existing hepatic impairment may increase systemic exposure — liver function monitoring is recommended before dosing
- **Cardiovascular**: Transient hypotension has been observed during or shortly after oral administration in some patients undergoing surgical procedures

Please refer to the full international package insert for Gleolan® or Levulan® for complete warnings, contraindications, and drug interaction information before any clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
5-ALA has a completed Phase 3 RCT directly in pre-malignant oral lesions (NCT01497951), systematic review evidence supporting oral pre-malignancy treatment, existing FDA/EMA approvals for related conditions (actinic keratosis, malignant glioma), and a well-characterized mechanistic basis for tumor-selective PpIX accumulation. The TxGNN prediction score of 96.01% reflects the drug's established biological plausibility across pre-malignant neoplasm categories. The primary barrier to clinical implementation in Singapore is the complete absence of local registration — not a lack of scientific evidence.

**To proceed, the following is needed:**

- **Regulatory pathway**: Apply to HSA for special access scheme (SAS) or compassionate use authorization for an appropriate 5-ALA formulation
- **Formulation selection**: Determine whether topical (oral/skin pre-malignant lesions) or oral solution (systemic photodynamic diagnosis/therapy) is appropriate for the intended clinical indication
- **Full safety review**: Obtain and formally review international package inserts for Gleolan® and/or Levulan®/Ameluz® covering contraindications, warnings, and drug interactions
- **MOA documentation**: Retrieve DrugBank API records (DB00855) to formally document mechanism of action for regulatory dossier
- **Light source assessment**: Confirm availability of appropriate photodynamic therapy light sources (630–635 nm red light or 417 nm blue light LED/laser system) in the target clinical facility
- **Clinical protocol development**: Define site-specific dosing protocol including ALA dose (typically 20 mg/kg oral or topical 20% concentration), incubation time (1–3 hours topical; 3 hours oral), light dose (typically 75–100 J/cm²), and follow-up schedule tailored to the target pre-malignant indication