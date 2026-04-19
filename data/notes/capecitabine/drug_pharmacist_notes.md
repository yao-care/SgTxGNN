# Capecitabine: From Colorectal Cancer to Gastric Tubular Adenocarcinoma

## One-Sentence Summary

Capecitabine is an oral fluoropyrimidine prodrug globally established as standard-of-care for colorectal cancer and breast cancer, achieving tumor-selective conversion to active 5-FU via Thymidine Phosphorylase (TP) overexpressed in epithelial tumor tissue.
The TxGNN model predicts it may be effective for **Gastric Tubular Adenocarcinoma** — the most prevalent gastric cancer histological subtype — supported by **20 publications** including multiple landmark Phase 3 RCTs demonstrating CAPOX as a standard chemotherapy backbone in gastric adenocarcinoma.
Notably, 9 of the top 10 TxGNN predictions for capecitabine are gastric cancer subtypes, reflecting a coherent biological signal across the gastric cancer disease network; the priority indication presented here (gastric tubular adenocarcinoma) carries L1 evidence and merits immediate clinical translation planning.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; globally approved for colorectal cancer and breast cancer |
| Predicted New Indication | Gastric Tubular Adenocarcinoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Capecitabine undergoes a three-step enzymatic cascade upon oral absorption. The critical final conversion from 5′-deoxy-5-fluorouridine (5′-DFUR) to active 5-fluorouracil (5-FU) is catalyzed by Thymidine Phosphorylase (TP), an enzyme characteristically overexpressed in tumor tissue relative to normal mucosa. The active 5-FU subsequently inhibits Thymidylate Synthase (TS), blocking de novo thymidylate (dTMP) synthesis, disrupting DNA replication, and triggering apoptosis in rapidly proliferating cancer cells. This tumor-targeted activation is the mechanistic basis for capecitabine's more favorable toxicity profile compared to systemic intravenous 5-FU. Formal mechanism of action data is currently flagged as a data gap in the Singapore regulatory record; however, this mechanism is comprehensively characterized in international pharmacological literature and underpins global regulatory approvals across multiple jurisdictions.

Gastric tubular adenocarcinoma (Lauren intestinal type, ~50–60% of all gastric cancers) is precisely the histological subtype most likely to benefit from capecitabine's prodrug mechanism. Intestinal-type gastric cancers characteristically overexpress TP in tumor cells, creating a pharmacologically selective environment for preferential intratumoral capecitabine activation. In contrast, diffuse-type gastric cancers (e.g., signet ring cell carcinoma) typically show lower TP expression and correspondingly lower fluoropyrimidine response rates — a histological distinction that directly supports capecitabine's specificity for the tubular subtype. The CLASSIC Phase 3 RCT (Bang YJ et al., Lancet 2012) established that adjuvant CAPOX (capecitabine + oxaliplatin) after D2 gastrectomy produced a significant improvement in disease-free survival (HR 0.56, p<0.0001) in stage II–IIIB gastric cancer, the majority of which were tubular adenocarcinomas, providing the most direct clinical validation.

From a systems biology perspective, the TxGNN knowledge graph assigns a 99.94% prediction score to this indication, reflecting strong multi-edge connectivity between capecitabine nodes and gastric adenocarcinoma disease nodes — connectivity driven by shared pathway biology with colorectal cancer (the original indication), common TS/TP biology, and overlapping clinical trial associations. This is not merely computational inference: the RESOLVE Phase 3 trial (2021, 2025 final OS update), and the contemporary immunotherapy combination trials (CheckMate 649, KEYNOTE-859, RATIONALE-305, GLOW, ORIENT-16) all incorporate capecitabine-based CAPOX as the standard chemotherapy backbone, collectively confirming capecitabine's central role in the modern gastric cancer treatment landscape.

---

## Clinical Trial Evidence

Currently no clinical trials have been registered specifically under the histological search term "gastric tubular adenocarcinoma." The evidence below draws from the broader gastric/gastroesophageal adenocarcinoma trial literature, where tubular adenocarcinoma constitutes the dominant histological subtype enrolled.

> No clinical trials registered specifically under "gastric tubular adenocarcinoma."

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22226517](https://pubmed.ncbi.nlm.nih.gov/22226517/) | 2012 | Phase 3 RCT | Lancet | **CLASSIC trial**: Adjuvant CAPOX vs. surgery alone after D2 gastrectomy in stage II–IIIB gastric cancer; DFS HR 0.56 (p<0.0001). Strongest direct evidence for capecitabine in predominantly tubular adenocarcinoma |
| [34252374](https://pubmed.ncbi.nlm.nih.gov/34252374/) | 2021 | Phase 3 RCT | Lancet Oncology | **RESOLVE trial** (initial report): Perioperative SOX vs. postoperative CapOx in locally advanced gastric/GEJ adenocarcinoma after D2 gastrectomy; CapOx confirmed as effective adjuvant standard (non-inferiority met) |
| [39952264](https://pubmed.ncbi.nlm.nih.gov/39952264/) | 2025 | Phase 3 RCT | Lancet Oncology | **RESOLVE trial** (final OS report): Mature overall survival data confirming long-term benefit of CapOx perioperative chemotherapy in gastric/GEJ adenocarcinoma |
| [34102137](https://pubmed.ncbi.nlm.nih.gov/34102137/) | 2021 | Phase 3 RCT | Lancet | **CheckMate 649**: Nivolumab + CAPOX or FOLFOX vs. chemotherapy alone in HER2-negative advanced gastric/GEJ adenocarcinoma; significant OS benefit, median OS improvement in PD-L1 CPS ≥5 population |
| [37524953](https://pubmed.ncbi.nlm.nih.gov/37524953/) | 2023 | Phase 3 RCT | Nature Medicine | **GLOW trial**: Zolbetuximab + CAPOX vs. placebo + CAPOX in CLDN18.2-positive, HER2-negative gastric/GEJ adenocarcinoma; improved PFS and OS confirming CAPOX as standard first-line backbone |
| [38806195](https://pubmed.ncbi.nlm.nih.gov/38806195/) | 2024 | Phase 3 RCT | BMJ | **RATIONALE-305**: Tislelizumab + chemotherapy (capecitabine-based) vs. placebo in advanced gastric/GEJ adenocarcinoma; significant OS improvement in overall and PD-L1-positive populations |
| [37875143](https://pubmed.ncbi.nlm.nih.gov/37875143/) | 2023 | Phase 3 RCT | Lancet Oncology | **KEYNOTE-859**: Pembrolizumab + fluoropyrimidine/platinum (including CAPOX) vs. placebo in HER2-negative advanced gastric/GEJ adenocarcinoma; OS benefit across PD-L1 CPS subgroups |
| [38051328](https://pubmed.ncbi.nlm.nih.gov/38051328/) | 2023 | Phase 3 RCT | JAMA | **ORIENT-16**: Sintilimab + chemotherapy (CAPOX or FOLFOX) vs. chemotherapy alone in unresectable gastric/GEJ cancer; improved OS and PFS, particularly in PD-L1-positive patients |
| [30982686](https://pubmed.ncbi.nlm.nih.gov/30982686/) | 2019 | Phase 3 RCT | Lancet | **FLOT4**: FLOT vs. ECF/ECX (epirubicin + cisplatin + capecitabine) as perioperative chemotherapy in locally advanced resectable gastric/GEJ adenocarcinoma; established superior perioperative standard |
| [20728210](https://pubmed.ncbi.nlm.nih.gov/20728210/) | 2010 | Phase 3 RCT | Lancet | **ToGA**: Trastuzumab + capecitabine or 5-FU + cisplatin vs. chemotherapy alone in HER2-positive advanced gastric/GEJ cancer; OS benefit (13.8 vs. 11.1 months), established HER2-directed standard |

---

## Singapore Market Information

Capecitabine is not registered with Singapore's Health Sciences Authority (HSA) and holds no active product licenses in Singapore.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No Singapore registrations on record |

> Capecitabine (Xeloda®, Roche) holds regulatory approvals in the United States (FDA), European Union (EMA), Japan (PMDA), South Korea (MFDS), and numerous other jurisdictions for colorectal cancer and breast cancer indications, with many markets additionally approving gastric cancer use. Singapore clinicians currently access capecitabine via the HSA Special Access Route (SAR) for unregistered medicines.

---

## Cytotoxicity

Capecitabine is a fluoropyrimidine antineoplastic agent with confirmed cytotoxic activity; this section is mandatory.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Fluoropyrimidine class (oral prodrug of 5-fluorouracil) |
| Myelosuppression Risk | Low to moderate (neutropenia and thrombocytopenia occur but are less frequent than with IV 5-FU; hand-foot syndrome (palmar-plantar erythrodysaesthesia) is the most characteristic dose-limiting toxicity) |
| Emetogenicity Classification | Low (oral administration; nausea/vomiting possible but high-grade emesis uncommon) |
| Monitoring Items | Complete blood count (CBC) with differential; renal function (serum creatinine and CrCl — dose reduction mandatory at CrCl 30–50 mL/min); liver function tests; DPD enzyme/DPYD genotype assessment prior to initiation |
| Handling Protection | Must follow cytotoxic drug handling regulations; oral chemotherapy-specific precautions apply to patients, caregivers, and pharmacy staff handling tablets |

---

## Safety Considerations

Singapore regulatory safety data is unavailable as capecitabine is not registered locally. The following reflects internationally established safety information critical for clinical use:

- **DPD Deficiency (Priority Warning)**: Patients with complete or partial dihydropyrimidine dehydrogenase (DPD) deficiency — due to DPYD gene variants — are at risk of severe, potentially fatal fluoropyrimidine toxicity. DPYD genotyping (at minimum testing for *2A, *13, HapB3, and c.2846A>T variants) is strongly recommended before initiation; dose reduction or avoidance is required for identified carriers.
- **Renal Impairment**: Capecitabine and its metabolites are renally excreted. Dose reduction to 75% is required for CrCl 30–50 mL/min; capecitabine is contraindicated when CrCl <30 mL/min.
- **Drug Interactions**: Clinically significant interactions include warfarin and oral anticoagulants (markedly elevated INR and hemorrhage risk — requires close INR monitoring if co-administered), phenytoin (elevated phenytoin plasma levels), and leucovorin (potentiation of 5-FU toxicity).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for capecitabine in gastric adenocarcinoma — particularly the tubular adenocarcinoma subtype — meets L1 criteria, supported by multiple completed Phase 3 RCTs (CLASSIC, RESOLVE, CheckMate 649, KEYNOTE-859, RATIONALE-305, GLOW, ORIENT-16) establishing CAPOX as a global standard-of-care chemotherapy backbone. The primary barriers to clinical translation in Singapore are not efficacy or safety gaps, but the drug's unregistered regulatory status and two formal data gaps requiring remediation before proceeding to safety screening.

**To proceed, the following is needed:**
- **Regulatory pathway**: Initiate HSA Special Access Route (SAR) application or evaluate feasibility of a formal product registration submission for Singapore
- **Safety data gap (DG001 — Blocking)**: Download and parse TFDA package insert PDF to formally document warnings and contraindications; this is a blocking requirement before S1 safety screening can proceed
- **MOA data gap (DG002 — High)**: Query DrugBank API (DB01101) to formally populate mechanism of action fields; required for mechanistic link analysis
- **DPD screening protocol**: Establish institutional DPYD genotyping pathway for all patients prior to capecitabine initiation
- **Oral chemotherapy infrastructure**: Confirm institutional pharmacy capacity for oral cytotoxic dispensing, patient education, and adherence monitoring
- **Biomarker testing plan**: Define patient selection pathway incorporating TP expression, HER2 status, PD-L1 (CPS), CLDN18.2, and MSI status to guide optimal combination therapy choice in individual patients