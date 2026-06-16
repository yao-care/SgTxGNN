---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 356
evidence_level: L5
indication_count: 10
---

# Durvalumab
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

# Durvalumab: From Anti-PD-L1 Immunotherapy to Rare Urothelial & Gynecologic Malignancies

## One-Sentence Summary

Durvalumab (Imfinzi) is a human IgG1κ anti-PD-L1 monoclonal antibody approved globally for NSCLC, SCLC, biliary tract cancer, and hepatocellular carcinoma, currently **not registered in Singapore**.
The TxGNN model predicts it may be effective across **10 rare urothelial and gynecologic malignancies**, with prediction scores ranging from 99.90% to 99.98%.
Clinical evidence spans from L5 (model prediction only) to L3, with **endocervical carcinoma** (Rank 6) reaching the strongest actionable recommendation ("Proceed with Guardrails"), supported by **2 clinical trials** (including 1 completed Phase 1 and 1 ongoing Phase 2 with n=174) and **1 review publication**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | NSCLC (unresectable Stage III), ES-SCLC, biliary tract cancer, HCC — global approved uses; not registered in Singapore |
| Top-Ranked Predicted Indication | Prostatic urethra urothelial carcinoma (Rank 1, TxGNN 99.98%, L5) |
| Best Actionable Prediction | Endocervical carcinoma (Rank 6, TxGNN 99.91%, L3) |
| Evidence Level (Best Actionable) | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Proceed with Guardrails** (Endocervical carcinoma only); **Hold** for 7 of 10 predictions; **Research Question** for 2 of 10 |

---

## All 10 Predicted Indications at a Glance

| Rank | Disease | TxGNN Score | Clinical Trials | Evidence Level | Decision |
|------|---------|------------|----------------|---------------|---------|
| 1 | Prostatic urethra urothelial carcinoma | 99.98% | 0 | L5 | Hold |
| 2 | Kidney pelvis sarcomatoid transitional cell carcinoma | 99.98% | 1 | L3 | Research Question |
| 3 | Infiltrating bladder urothelial carcinoma, sarcomatoid variant | 99.98% | 2 | L3 | Research Question |
| 4 | Renal pelvis papillary urothelial carcinoma | 99.98% | 0 | L5 | Hold |
| 5 | Uterine ligament adenocarcinoma | 99.92% | 0 | L5 | Hold |
| 6 | **Endocervical carcinoma** | 99.91% | 2 | **L3** | **Proceed with Guardrails** |
| 7 | Adenoid cystic carcinoma of the cervix uteri | 99.91% | 0 | L5 | Hold |
| 8 | Uterine ligament serous adenocarcinoma | 99.91% | 0 | L5 | Hold |
| 9 | Signet ring cell variant cervical mucinous adenocarcinoma | 99.90% | 0 | L5 | Hold |
| 10 | Intestinal variant cervical mucinous adenocarcinoma | 99.90% | 0 | L5 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not captured in this Evidence Pack (Data Gap DG002). Based on well-established pharmacological knowledge, Durvalumab is a human IgG1κ monoclonal antibody that selectively blocks the binding of **PD-L1** to both PD-1 and CD80 receptors. This blockade releases inhibition of cytotoxic T-cell activity, restoring immune surveillance against tumor cells — without directly activating the T-cell receptor. It is currently approved for use in unresectable Stage III NSCLC (concurrent chemoradiotherapy followed by durvalumab maintenance), extensive-stage SCLC (with platinum/etoposide), biliary tract cancer, and hepatocellular carcinoma.

All 10 TxGNN-predicted indications share a mechanistic thread: they are carcinomas arising from epithelia with documented or biologically plausible PD-L1 expression, particularly under inflammatory or viral (HPV) conditions. The **urothelial cluster** (Ranks 1–4) is mechanistically supported by durvalumab's known activity in bladder and upper-tract UC, where PD-L1 overexpression is a recognized biomarker. The **sarcomatoid variants** (Ranks 2–3) are especially compelling because sarcomatoid transformation is associated with epithelial-mesenchymal transition (EMT), high TMB, and enriched immune cell infiltration — all predictors of checkpoint inhibitor response. The **gynecologic cluster** (Ranks 5–10) is driven by HPV-associated PD-L1 upregulation: viral oncoproteins E6 and E7 directly induce PD-L1 expression on cervical epithelial cells, creating a permissive immune-suppressive microenvironment that anti-PD-L1 therapy is designed to reverse.

However, each of these predictions represents a rare histological or anatomical sub-variant, and clinical evidence for most remains absent. The high TxGNN scores (99.88–99.98%) reflect shared structural features in the knowledge graph with parent indications that have established durvalumab data — they are not independent clinical signals. **Endocervical carcinoma** (Rank 6) has the strongest overall foundation, combining HPV-driven PD-L1 biology, a completed Phase 1 safety study (NCT03452332), and a large ongoing Phase 2 trial (NCT04065269, n=174). The sarcomatoid urothelial variants (Ranks 2–3) also have indirect Phase 1 data and a terminated-but-informative Phase 2 (NCT03912818), making them appropriate for further research question development.

---

## Clinical Trial Evidence

### Ranks 2 & 3 — Urothelial Sarcomatoid Variants (Kidney Pelvis & Bladder)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT03912818](https://clinicaltrials.gov/study/NCT03912818) | Phase 2 | Terminated | 7 | Durvalumab + neoadjuvant chemotherapy (MVAC/GC/carboplatin) in variant histology bladder cancer, explicitly including sarcomatoid subtype. Terminated early due to recruitment difficulty (n=7 vs target), but confirms concept feasibility and provides safety signal reference for this exact histology. |
| [NCT02812420](https://clinicaltrials.gov/study/NCT02812420) | Early Phase 1 | Active, Not Recruiting | 54 | Pre-surgical durvalumab + tremelimumab in muscle-invasive, high-risk urothelial carcinoma ineligible for cisplatin-based neoadjuvant chemotherapy. Covers both upper tract (renal pelvis) and bladder UC anatomy; no sarcomatoid-specific stratification, provides indirect Phase 1 safety basis. |

### Rank 6 — Endocervical Carcinoma

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Phase 1 | Completed | 20 | Hypofractionated SBRT + durvalumab + tremelimumab in recurrent/metastatic cervical, vaginal, or vulvar cancer. Directly within cervical cancer scope including endocervical anatomy. Completed — provides safety data for regulatory and protocol development purposes. Primary basis for S2 advancement. |
| [NCT04065269](https://clinicaltrials.gov/study/NCT04065269) | Phase 2 | Active, Not Recruiting | 174 | ATARI trial: ceralasertib (ATRi) alone or combined with olaparib or durvalumab in relapsed gynecologic cancers, stratified by ARID1A loss status. Largest enrollment in this therapeutic space; covers cervical cancer broadly with ARID1A biomarker stratification. Results expected 2026. |

---

## Literature Evidence

### Rank 6 — Endocervical Carcinoma

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Review | Biomedical Journal | Small cell neuroendocrine carcinoma of the cervix (SCNECC): molecular basis and therapeutic advances. Reviews HPV association, the near-absence of clinical trials for rare aggressive cervical histologies, and emerging immunotherapy potential. Contextualises the immunological rationale for checkpoint inhibition in uncommon cervical subtypes and highlights the unmet need that the endocervical carcinoma prediction addresses. |

---

## Singapore Market Information

Durvalumab (Imfinzi) is **not registered with the Health Sciences Authority (HSA) of Singapore**. No product authorization records are present in the Evidence Pack.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|------------|-------------------|
| — | Not registered | — | No HSA licenses found |

Physicians in Singapore requiring clinical access to durvalumab should explore HSA's Special Access Route (SAR) or refer patients to clinical trial sites where the drug is available under protocol.

---

## Cytotoxicity

Durvalumab is an antineoplastic immunotherapy agent. The cytotoxicity section applies, though its profile differs substantially from conventional chemotherapy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted Immunotherapy — anti-PD-L1 monoclonal antibody (IgG1κ); not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Low via direct mechanism; monitor for immune-related haematologic events (haemolytic anaemia, immune thrombocytopenia) |
| Emetogenicity Classification | Low (monoclonal antibodies have minimal direct emetic potential) |
| Monitoring Items | LFTs and bilirubin (immune hepatitis), thyroid panel (hypothyroidism/hyperthyroidism), CBC with differential (immune cytopenias), serum creatinine (immune nephritis), chest imaging (pneumonitis), HbA1c and fasting glucose (immune-mediated diabetes mellitus) |
| Handling Protection | Standard biologic/monoclonal antibody handling procedures; cytotoxic drug handling regulations not required (non-DNA-damaging mechanism) |

---

## Safety Considerations

TFDA package insert safety data was not available at the time of this report (Data Gap DG001 — Blocking severity). The following is based on the established global safety profile of durvalumab (Imfinzi):

- **Immune-related adverse events (irAEs)**: The primary safety concern class for all anti-PD-L1 agents. Includes pneumonitis, colitis, hepatitis, endocrinopathies (thyroid, adrenal, pituitary), nephritis, skin reactions, and myocarditis — any of which may be severe (Grade 3–4) or fatal. Management requires early recognition, systemic corticosteroids, and potential permanent drug discontinuation.
- **Embryo-fetal toxicity**: Durvalumab can cause fetal harm. Contraindicated in pregnancy. Patients of childbearing potential must use effective contraception during treatment and for at least 3 months after the last dose.
- **Drug interactions**: No DDI data was found in the Evidence Pack query. Anti-PD-L1 antibodies have no known CYP450-mediated pharmacokinetic interactions; however, concurrent use with immunosuppressants may attenuate efficacy, and combination with other immune-activating agents (e.g., tremelimumab, as in NCT02812420 and NCT03452332) significantly increases irAE risk.

---

## Conclusion and Next Steps

### Indication-Specific Decisions

---

**Ranks 1, 4 — Prostatic Urethra UC / Renal Pelvis Papillary UC: Hold**

Rationale: L5 evidence (model prediction only). These are extremely rare anatomical variants of urothelial carcinoma with no registered trials or published literature. TxGNN high scores reflect broad UC knowledge graph similarity, not independent clinical signals. Revisit when broad upper-tract UC immunotherapy datasets mature.

---

**Ranks 2 & 3 — Kidney Pelvis Sarcomatoid TC / Bladder UC Sarcomatoid Variant: Research Question**

Rationale: L3 evidence. The biological rationale is sound — sarcomatoid histology is associated with high PD-L1 expression, elevated TMB, and inflamed microenvironments. A terminated Phase 2 (NCT03912818) directly targeting bladder sarcomatoid variant confirms mechanistic plausibility and provides a safety reference. Evidence is insufficient for routine recommendation but sufficient to justify a formal research question.

**To advance Ranks 2–3:**
- Design investigator-initiated study with sarcomatoid variant stratification criteria
- Review final safety and pathological complete response data from NCT03912818 (n=7)
- Monitor results of NCT02812420 (completion date 2027)

---

**Ranks 5, 7, 8, 9, 10 — Uterine Ligament Adenocarcinoma / Cervical ACC / Uterine Ligament Serous Adenocarcinoma / Signet Ring Cell & Intestinal Variant Cervical: Hold**

Rationale: L5 evidence across all five. Biological rationale for PD-L1 inhibition is weak: cervical adenoid cystic carcinoma (ACC) has MYB-NFIB fusion-driven biology with historically low PD-L1 expression and poor immunotherapy response (<10%); serous histology is predominantly MSS/low-TMB; HPV-negative intestinal and signet-ring variants lack the viral PD-L1 induction seen in typical HPV(+) cervical cancer.

---

**Rank 6 — Endocervical Carcinoma: Proceed with Guardrails**

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 1 safety study (NCT03452332, n=20) and a large ongoing Phase 2 (NCT04065269, n=174) together with the strong HPV-driven PD-L1 biology provide sufficient foundation to advance endocervical carcinoma to a formal clinical evaluation stage.

**To proceed, the following is needed:**
- Await and review final efficacy and biomarker data from NCT04065269 (ATARI trial; expected 2026)
- Obtain sub-group analysis by HPV status from NCT03452332 final report — **critical guardrail**: HPV(−) endocervical carcinoma has substantially lower predicted PD-L1 response and must be stratified separately
- Resolve Data Gap DG001: obtain TFDA/HSA-equivalent package insert for complete contraindication and warning profile before clinical protocol submission
- Resolve Data Gap DG002: formally document MOA via DrugBank API for regulatory submission documentation
- Initiate HSA Singapore Special Access Route (SAR) application or identify active clinical trial site for Singapore patient access
- Define biomarker eligibility criteria (HPV status, PD-L1 CPS, ARID1A status) aligned with ATARI trial methodology

> **Clinical disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before clinical application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

