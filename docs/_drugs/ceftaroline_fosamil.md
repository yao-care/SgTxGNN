---
layout: default
title: Ceftaroline Fosamil
parent: Low Evidence (L5)
nav_order: 223
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ceftaroline Fosamil: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not stated in the Singapore license data (the approved indication tex…"
monitor_inn: "Ceftaroline fosamil"
predicted_indications: ["rheumatoid arthritis", "osteoarthritis", "osteoarthritis susceptibility", "gout", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "hemoglobinopathy", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis"]
---

# Ceftaroline Fosamil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Ceftaroline fosamil: From Bacterial Infection to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Ceftaroline fosamil is a cephalosporin antibiotic registered in Singapore as an injectable product. The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but the data compiled for this report contain **no clinical trials and no publications** for this prediction. The result is a computational association only, and the mechanistic review found no biological support for it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore license data (the approved indication text is empty) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 98.20% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ceftaroline fosamil is a cephalosporin antibiotic. It inhibits bacterial penicillin-binding proteins, including PBP2a in MRSA, and its role is to treat bacterial infections.

Rheumatoid arthritis is an autoimmune joint disease, and ceftaroline has no known immunomodulatory activity relevant to it. The high TxGNN score most likely reflects a knowledge-graph association, possibly through shared joint or bone infection or musculoskeletal links. It is not a biologically supported link. For this reason, the prediction should be treated as a hypothesis with no mechanistic backing.

Other predictions in the top 10 (osteoarthritis, gout, several rare skeletal dysplasias, hemoglobinopathy and myosclerosis) show the same pattern. The only related publication is a cohort study on osteoarticular **infection**, which is an antibacterial use and not degenerative osteoarthritis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for rheumatoid arthritis.

For reference, the nearest evidence found for the other top predictions is:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27530754](https://pubmed.ncbi.nlm.nih.gov/27530754/) | 2016 | Cohort | J Antimicrob Chemother | Matched cohort of outpatient ceftaroline vs vancomycin for osteoarticular infection (bone and joint infection, not osteoarthritis) |
| [21382815](https://pubmed.ncbi.nlm.nih.gov/21382815/) | 2011 | Review | J Am Pharm Assoc | New-drugs overview listing ceftaroline fosamil alongside pegloticase (a gout drug); co-mention only, no evidence for gout |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14268P | Zinforo Powder for Concentrate for Solution for Infusion 600mg/vial | Injection, powder, for solution | Not available |

## Safety Considerations

- **Drug Interactions**: 12 interactions were identified, all rated Moderate:
  - Aminoglycosides: kanamycin, neomycin, streptomycin, amikacin (including liposomal), gentamicin
  - Anticoagulants: warfarin, dicoumarol
  - Others: picosulfuric acid, chloramphenicol, ethinylestradiol, mycophenolic acid
- **Hematologic effects**: Beta-lactams may cause hemolytic anemia or a positive Coombs test. This is relevant if the drug were ever considered for hemoglobinopathy.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, and no plausible mechanism links an antibacterial cephalosporin to autoimmune joint inflammation. The evidence level is L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the Singapore license
- A credible biological rationale, supported by preclinical data, for an effect on rheumatoid arthritis
- A review of whether the model score reflects a knowledge-graph artefact related to bone and joint infection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

