---
layout: default
title: Etoricoxib
parent: 僅模型預測 (L5)
nav_order: 406
evidence_level: L5
indication_count: 10
---

# Etoricoxib
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

# Etoricoxib: From Musculoskeletal Pain to Migraine Disorder

## One-Sentence Summary

Etoricoxib is a selective COX-2 inhibitor (NSAID) widely used for arthritis, ankylosing spondylitis, and acute pain conditions across international markets.
The TxGNN model predicts it may be effective for **Migraine Disorder**, with **no direct clinical trials or publications** currently supporting this specific indication.
However, a closely related TxGNN-predicted indication — headache disorder — is supported by **5 case reports and series** documenting Etoricoxib's efficacy in indomethacin-responsive headache subtypes, providing indirect biological and clinical support for the migraine prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Arthritis / musculoskeletal pain (inferred from clinical context; no Singapore HSA registration records found) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (migraine-specific); L4 for related indomethacin-responsive headache subtypes |
| Singapore Market Status | Not marketed (0 registered products) |
| Number of Registrations | 0 |
| Recommended Decision | Research Question (migraine disorder) / Proceed with Guardrails (indomethacin-responsive headache subtypes) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on its well-established pharmacological class, Etoricoxib is a **highly selective cyclooxygenase-2 (COX-2) inhibitor**. It reduces prostaglandin E2 (PGE2) and other pro-inflammatory prostanoids while largely sparing COX-1 — the isoform responsible for gastric mucosal protection and platelet aggregation. This selectivity gives it a more favorable gastrointestinal tolerability profile compared to traditional non-selective NSAIDs, making it potentially better suited for repeated or long-term headache management.

The mechanistic link to migraine is biologically plausible. PGE2 is a key sensitizer of trigeminal nociceptors, driving the neurogenic inflammation and central sensitization that underlie migraine pain amplification. Non-selective NSAIDs such as ibuprofen and naproxen are established first-line agents for acute migraine attacks, and their benefit is largely attributed to COX pathway inhibition. Selective COX-2 inhibitors like Etoricoxib share this core mechanism, and the reduced COX-1 burden may be advantageous for patients requiring frequent treatment.

The strongest indirect evidence comes from **indomethacin-responsive headache disorders** — a related group that includes primary stabbing headache, secondary cough headache, hemicrania continua, and paroxysmal hemicrania. Three direct case series/reports (PMID 35277974, 17883876, 18171381) and two additional case reports (PMID 36893522, 25229174) document Etoricoxib's clinical activity in these subtypes. Since indomethacin's efficacy in this group is mediated through COX inhibition, and Etoricoxib shares this mechanism with better tolerability, the TxGNN prediction for migraine carries meaningful biological credibility — though it remains an untested hypothesis for migraine specifically.

---

## Clinical Trial Evidence

Currently no clinical trials have been registered that directly evaluate Etoricoxib for migraine disorder.

Two trials were retrieved for the broader headache disorder category (TxGNN rank #9), but both involve Etoricoxib in an unrelated musculoskeletal context and do not address headache efficacy:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|--------------|-------|--------|------------|--------------|
| [NCT03542955](https://clinicaltrials.gov/study/NCT03542955) | N/A | Completed | 180 | Pulsed shortwave therapy vs. Etoricoxib in cervical osteoarthritis — Etoricoxib serves as the pharmacological comparator; neck pain outcome only, no headache endpoint |
| [NCT06967363](https://clinicaltrials.gov/study/NCT06967363) | N/A | Not yet recruiting | 360 | Neuroimaging and biospecimen collection in low back pain patients — observational cohort, no Etoricoxib intervention for headache |

Neither trial constitutes evidence for migraine or headache as a treatment indication.

---

## Literature Evidence

No publications directly evaluate Etoricoxib for migraine disorder. The following 5 publications from the related **headache disorder** (TxGNN rank #9) and **trigeminal autonomic cephalalgia** (TxGNN rank #10) indications provide the most clinically relevant indirect evidence:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35277974](https://pubmed.ncbi.nlm.nih.gov/35277974/) | 2022 | Case Series / Retrospective Review | *Headache* | Etoricoxib and celecoxib demonstrated efficacy in indomethacin-responsive headache disorders — including trigeminal autonomic cephalalgias and paroxysmal primary headaches — offering a better-tolerated COX-2-selective alternative to indomethacin |
| [18171381](https://pubmed.ncbi.nlm.nih.gov/18171381/) | 2008 | Case Series | *European Journal of Neurology* | Primary stabbing headache (an indomethacin-responsive syndrome) responded to Etoricoxib, confirming COX-2 as a viable therapeutic target in this condition |
| [17883876](https://pubmed.ncbi.nlm.nih.gov/17883876/) | 2007 | Case Report | *Journal of Medical Case Reports* | Earliest reported use of Etoricoxib in idiopathic stabbing headache — effective treatment in a patient intolerant to indomethacin |
| [36893522](https://pubmed.ncbi.nlm.nih.gov/36893522/) | 2023 | Case Report | *Clinical Neurology and Neurosurgery* | Secondary cough headache responded to Etoricoxib — first reported case of COX-2 inhibitor efficacy in this headache subtype; natural remission and treatment-independent course described |
| [25229174](https://pubmed.ncbi.nlm.nih.gov/25229174/) | 2014 | Case Report | *Clinical Neuropharmacology* | ⚠️ **Safety signal**: Reversible cerebral vasoconstriction syndrome (RCVS) possibly induced by Etoricoxib — critical caution when using this drug in headache patients, as RCVS itself presents with thunderclap headache |

---

## Singapore Market Information

Etoricoxib has no registered products with the Singapore Health Sciences Authority (HSA) in the current database. No authorization records are available to display.

> Note: Etoricoxib (brand name Arcoxia, MSD) is approved and marketed in numerous countries globally for osteoarthritis, rheumatoid arthritis, ankylosing spondylitis, acute gout, and postoperative pain. The absence of Singapore HSA records in this dataset warrants verification against the HSA product registry directly.

---

## Safety Considerations

Formal package insert warnings and contraindications are not available in the current evidence pack. Please refer to the package insert for complete safety information, including cardiovascular risk warnings (class effect shared by all selective COX-2 inhibitors).

The following signals were identified from literature evidence:

- **Cerebrovascular Risk**: A case of reversible cerebral vasoconstriction syndrome (RCVS) possibly triggered by Etoricoxib has been reported (PMID 25229174). This is especially relevant in the headache context, as RCVS presents with severe thunderclap headache and must be distinguished from the primary headache disorders being treated.
- **Renal and Electrolyte Risk**: Life-threatening hyperkalemia and acute kidney injury precipitated by Etoricoxib in a 75-year-old patient co-administered telmisartan and a low-sodium diet has been reported (PMID 21373319). Concurrent renin-angiotensin system blockers substantially increase this risk.
- **Contraindication Signal — Pulmonary Hypertension**: TxGNN also ranked pulmonary hypertension as a predicted indication (rank #6). This direction is potentially **harmful**: prostacyclin (PGI2), a key pulmonary vasodilator synthesized via COX-2, would be suppressed by Etoricoxib, potentially worsening pulmonary vasoconstriction. Etoricoxib should not be repurposed for pulmonary arterial hypertension.

---

## Conclusion and Next Steps

**Decision: Research Question** *(for migraine disorder as a primary indication)*
**Decision: Proceed with Guardrails** *(for indomethacin-responsive headache subtypes)*

**Rationale:**
Migraine disorder as a standalone indication is unsupported by any direct clinical trial or publication (L5), making it a model-generated hypothesis at this stage. However, the mechanistic basis is solid, and Etoricoxib has demonstrated direct efficacy in closely related COX-2-mediated headache subtypes through multiple case-level reports spanning 2007–2023. The optimal entry strategy is to validate the broader headache disorder signal first before targeting migraine specifically.

**To proceed, the following is needed:**

- **Verify Singapore HSA registration status** — Confirm whether Etoricoxib (Arcoxia) is currently registered with HSA Singapore; existing international approvals (EU, Asia-Pacific) may provide a regulatory pathway
- **Retrieve mechanism of action data** from DrugBank (DB01628) to formally document COX-2 selectivity ratio and PGE2 pathway pharmacology
- **Confirm literature search completeness** for migraine — run a targeted PubMed search combining "etoricoxib" AND "migraine" to ensure no direct publications were missed
- **Conduct a prospective pilot study in indomethacin-responsive headache subtypes** (hemicrania continua, paroxysmal hemicrania, primary stabbing headache) as a lower-risk, mechanistically cleaner entry point before expanding to migraine
- **Safety monitoring plan** addressing: cardiovascular (RCVS, MI risk), renal (hyperkalemia/AKI — especially with RAS blockers), and neurological adverse events
- **Explicitly exclude pulmonary hypertension** patients from any study population given the identified harmful mechanism signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

