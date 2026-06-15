---
layout: default
title: Carbamazepine
parent: 僅模型預測 (L5)
nav_order: 204
evidence_level: L5
indication_count: 10
---

# Carbamazepine
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

# Carbamazepine: From Epilepsy & Trigeminal Neuralgia to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Carbamazepine (CBZ) is a well-established anticonvulsant and analgesic, widely used as first-line treatment for epilepsy and trigeminal neuralgia.
The TxGNN model predicts it may be effective for **Trigeminal Nerve Neoplasm**,
with **1 clinical trial** and **20 publications** currently supporting this direction — primarily through its role in managing tumour-related neuropathic pain via sodium channel blockade.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Epilepsy; Trigeminal neuralgia (established pharmacological use; no Singapore registration found) |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on the pharmacological literature and repurposing rationale extracted from this evidence pack, Carbamazepine primarily blocks voltage-gated sodium channels (Nav1.1 / Nav1.2 / Nav1.6), suppressing repetitive neuronal firing and reducing ectopic impulse generation in trigeminal nerve fibres. This is the same mechanism underlying its established efficacy in idiopathic trigeminal neuralgia (TN).

Trigeminal nerve neoplasms — including schwannomas, primary lymphomas, dermoid cysts, meningiomas, and melanomas arising in or compressing the trigeminal nerve — frequently present with TN-like lancinating facial pain as a cardinal symptom, due to mechanical compression or perineural infiltration. Because CBZ is the pharmacological standard of care for TN pain regardless of aetiology, the TxGNN model's prediction that CBZ may apply to trigeminal nerve neoplasm reflects a well-grounded symptom-control extrapolation: the pain phenotype is identical, and the mechanistic intervention point (aberrant sodium channel-driven firing in the compressed nerve) is shared.

A critical caveat must be stated: CBZ has no known direct antiproliferative or anti-tumour activity. Its utility in trigeminal nerve neoplasm is limited to **palliative management of associated neuropathic pain**, not treatment of tumour growth. In several case reports included in this evidence pack, CBZ provided initial pain relief but failed when tumour progression overwhelmed nerve compression (e.g., primary melanoma, malignant lymphoma). Definitive management of trigeminal nerve neoplasms requires surgical resection, radiotherapy, or oncological systemic therapy; CBZ serves as adjunct symptom control.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT06853119](https://clinicaltrials.gov/study/NCT06853119) | N/A | Not Yet Recruiting | 120 | MRI-based brain network analysis in trigeminal neuralgia patients; observational study evaluating structural plasticity and neural mechanisms. No CBZ intervention; provides mechanistic background on TN pathophysiology. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36824641](https://pubmed.ncbi.nlm.nih.gov/36824641/) | 2022 | Review | Acta Clinica Croatica | Comprehensive TN treatment overview; CBZ identified as primary first-line medical therapy; covers vascular compression and tumour-related TN aetiology |
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Review of Neurotherapeutics | TN treatment landscape review; CBZ highlighted for focal demyelination/ectopic discharge suppression; medical vs. surgical algorithm |
| [11286444](https://pubmed.ncbi.nlm.nih.gov/11286444/) | 2001 | Retrospective Survey | British Journal of Oral & Maxillofacial Surgery | UK survey of 254 oral-maxillofacial surgeons; CBZ monitoring practice patterns in secondary TN screening highlighted |
| [30741017](https://pubmed.ncbi.nlm.nih.gov/30741017/) | 2023 | Case Report | British Journal of Neurosurgery | Primary neurolymphomatosis of trigeminal nerve presenting as facial pain; CBZ prescribed but symptoms did not improve, MRI revealed mass in Meckel's cave — illustrates CBZ limitation in tumour-driven TN |
| [25142539](https://pubmed.ncbi.nlm.nih.gov/25142539/) | 2014 | Case Report | Rinsho Shinkeigaku | Malignant lymphoma with perineural spread along trigeminal nerve; initially diagnosed as classical TN and improved on CBZ; later relapsed with additional cranial nerve deficits |
| [9109911](https://pubmed.ncbi.nlm.nih.gov/9109911/) | 1997 | Case Report | Neurology | Post-irradiation neuromyotonia in facial and trigeminal nerve distribution; neuromyotonic discharges recorded; responded to CBZ therapy |
| [22647513](https://pubmed.ncbi.nlm.nih.gov/22647513/) | 2012 | Case Report | No Shinkei Geka | Combined glossopharyngeal and trigeminal neuralgia due to vascular compression; CBZ established as first-line medical treatment before MVD |
| [25433061](https://pubmed.ncbi.nlm.nih.gov/25433061/) | 2014 | Case Report | No Shinkei Geka | Cerebellopontine angle lipoma causing TN; CBZ initiated but pain not adequately controlled due to side effects; surgical lipoma debulking performed |
| [3181365](https://pubmed.ncbi.nlm.nih.gov/3181365/) | 1988 | Animal Study | Experimental Neurology | IV CBZ produced immediate inhibition of spontaneous ectopic discharges from surgical neuromas in rats at clinically relevant doses (2.5–11.2 mg/kg), supporting mechanistic basis for nerve-compression pain control |
| [15235745](https://pubmed.ncbi.nlm.nih.gov/15235745/) | 2004 | Case Report | Arquivos de Neuro-Psiquiatria | Primary melanoma of Meckel's cave presenting as TN; CBZ and MVD both failed; tumour discovered only on repeat MRI — underscores need to exclude neoplasm when CBZ-refractory TN is encountered |

---

## Singapore Market Information

Carbamazepine currently has **no registered products** with the Health Sciences Authority (HSA) of Singapore. Any clinical use would constitute off-label or compassionate-use access, requiring appropriate institutional and regulatory approval.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for clinical teams**: Although formal safety data was unavailable in this evidence pack, Carbamazepine carries well-documented population-level risks that are especially relevant in Singapore's predominantly Asian patient population:
> - **HLA-B\*15:02 screening** is strongly recommended prior to initiation in Han Chinese, Thai, and other Southeast Asian patients due to significantly elevated risk of Stevens-Johnson Syndrome / Toxic Epidermal Necrolysis (SJS/TEN).
> - Routine monitoring of **CBC, liver function, and serum electrolytes** is standard practice.
> - CBZ is a potent **CYP3A4 inducer** with extensive drug-drug interaction potential.
>
> These risks should be formally evaluated before initiating therapy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple reviews and case reports confirm that CBZ is the pharmacological standard of care for TN pain regardless of underlying aetiology, and animal data directly supports its mechanism of suppressing ectopic nerve discharge — making symptom-control use in trigeminal nerve neoplasm biologically plausible and clinically consistent with current practice. However, CBZ does not treat the tumour itself, evidence is Level L3, and Singapore has no registered product, requiring careful governance.

**To proceed, the following is needed:**

- **Clarify therapeutic goal**: Confirm whether the intended use is palliative pain control (symptom management) vs. tumour treatment — the evidence supports only the former
- **Regulatory pathway**: Identify HSA off-label access or Special Access Route (SAR) requirements given zero Singapore registrations
- **HLA-B\*15:02 genotyping**: Mandatory before initiation in Asian patients to assess SJS/TEN risk
- **Obtain and review full package insert**: Formal safety assessment including contraindications, drug interactions, and warnings (currently a blocking data gap per DG001)
- **Exclude tumour progression as CBZ failure cause**: Establish imaging baseline; refractory or worsening pain on CBZ should prompt urgent repeat MRI to rule out tumour growth rather than dose escalation
- **Prospective case registry**: Given absence of RCT data, systematic case documentation of CBZ use in trigeminal nerve neoplasm patients would strengthen the evidence base from L3 toward L2
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

