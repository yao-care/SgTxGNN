---
layout: default
title: Melphalan
parent: High Evidence (L1-L2)
nav_order: 640
evidence_level: L2
indication_count: 10
---

# Melphalan
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Melphalan: From an Unlisted Approved Use to Gonadal Germ Cell Tumor

## One-Sentence Summary

Melphalan is an alkylating chemotherapy drug marketed in Singapore as an injection and an oral tablet, but the registration records provided do not state its approved indication.
The TxGNN model predicts it may be effective for **gonadal germ cell tumor**, with **7 clinical trials** and **4 publications** linked to this prediction.
Only one linked trial targets germ cell tumors directly, and the literature is old and historical, so the evidence is early-stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records provided |
| Predicted New Indication | Gonadal germ cell tumor |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L2 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Melphalan is a bifunctional nitrogen mustard alkylating agent that causes DNA interstrand crosslinks. Germ cell tumors are generally chemosensitive to DNA-damaging agents. High-dose alkylator-based regimens with stem cell rescue are therefore biologically plausible.

The most relevant trial is NCT00936936, a completed Phase 2 study of high-dose chemotherapy in relapsed, poor-prognosis germ cell tumors. Its summary lists melphalan in the first cycle, alongside gemcitabine, docetaxel and carboplatin, but the study does not isolate melphalan's own contribution.

The very high TxGNN score is a graph-based prediction, not clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | Completed | 64 | Two cycles of high-dose chemotherapy (first cycle includes melphalan) in relapsed poor-prognosis germ-cell tumors. This is the most directly relevant trial. |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Completed | 451 | Eight high-dose chemotherapy regimens with autologous transplant for hematologic malignancy and selected solid tumors. Germ cell tumors are likely a small subset. |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | Completed | 25 | Escalating-dose melphalan with stem cell support and amifostine in mixed cancer patients. |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | Completed | 25 | Pilot of busulfan, melphalan and topotecan with autologous transplant in advanced and recurrent tumors. |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Terminated | 13 | Amifostine protection with autologous transplant in pediatric solid and brain tumors. Ended early, so of limited value. |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | N/A | Completed | 174 | Pilot of high-dose chemotherapy, with or without total-body irradiation, before autologous transplant in hematologic cancers and solid tumors. Not specific to germ cell tumors. |
| [NCT01272817](https://clinicaltrials.gov/study/NCT01272817) | N/A | Completed | 36 | Nonmyeloablative allogeneic transplant with melphalan and cladribine or total lymphoid irradiation. Different treatment setting. |

Only one trial (NCT00936936) targets germ cell tumors directly. The others are mixed-tumor transplant studies and offer indirect support at best.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24913](https://pubmed.ncbi.nlm.nih.gov/24913/) | 1977 | Review | Urologic Clinics of North America | Review of seminoma. No abstract available. |
| [4270380](https://pubmed.ncbi.nlm.nih.gov/4270380/) | 1973 | Review | Oncology | Review of chemotherapy for testicular germinal tumors. No abstract available. |
| [13392619](https://pubmed.ncbi.nlm.nih.gov/13392619/) | 1956 | Case series (historical) | Voprosy Onkologii | Early experience treating testicular seminoma and its metastases with sarcolysin (melphalan). |
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Preclinical/physiology | Acta - Unio Internationalis Contra Cancrum | Effects of hormonal and alkylating drugs on pituitary follicle-stimulating function. Likely off-target. |

All four publications are from 1956 to 1977, and none has an abstract in the record. They give only historical context.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN11873P | ALKERAN FOR INJECTION 50 mg/vial | Injection |
| SIN11822P | ALKERAN TABLET 2 mg (Revised formula) | Film-coated tablet |

Both injectable and oral forms are available locally. The approved indication text is not recorded for either license.

---

## Cytotoxicity

This assessment is based on general drug-class knowledge, because the Evidence Pack contains no toxicity data. Please refer to the package insert warnings and precautions for confirmation.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard class) |
| Myelosuppression Risk | High (dose-limiting; stem cell rescue is needed at high doses) |
| Emetogenicity Classification | Low to moderate for oral use; moderate or higher for intravenous and high-dose use |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. Retrieval of the local package insert is still outstanding.

No drug interaction records were found. High-dose regimens with stem cell support, as used in the linked trials, carry substantial toxicity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence for gonadal germ cell tumor rests on one completed Phase 2 trial in a multi-drug regimen, where melphalan's own contribution is unclear, plus historical literature. The local safety data are missing and block safety screening, so the prediction is best treated as a research question for now.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications from the HSA website (blocking gap)
- Mechanism of action data from DrugBank
- The approved indication for each Singapore license
- Results and melphalan-specific analysis of NCT00936936, plus a review of modern germ cell tumor literature
- Confirmation of the route and dose setting (intravenous high-dose versus oral) that would be relevant

**Other predicted indications:**
- **Female breast carcinoma** also reaches L2. It has Phase 1/2 and cohort studies of high-dose melphalan regimens, but no randomized evidence of benefit in the data provided.
- **Ovarian germ cell tumor** has only indirect trial evidence (L3). The remaining seven predictions, including choriocarcinoma of ovary and several mucinous adenocarcinomas, rest on the model prediction alone (L5) and are on hold.

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

