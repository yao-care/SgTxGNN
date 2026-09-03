---
layout: default
title: Nitrofurantoin
parent: 僅模型預測 (L5)
nav_order: 709
evidence_level: L5
indication_count: 10
---

# Nitrofurantoin
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

# Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis

## One-Sentence Summary

Nitrofurantoin (DB00698) is a nitrofuran-class antibacterial classically used to treat uncomplicated urinary tract infections. The TxGNN model's top prediction flags **Rheumatoid Arthritis** as a candidate new indication (score 99.89%), but the supporting evidence base consists of **0 clinical trials** and **12 publications**, most of which describe nitrofurantoin-associated pulmonary and hepatic toxicity in RA patients rather than therapeutic benefit — the model score is not corroborated by a coherent efficacy signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (UTI) — well-established public knowledge for nitrofurantoin; not present in the evidence pack (`original_indications` is empty) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa` = Data Gap). Nitrofurantoin is a nitrofuran antibacterial that is reduced by bacterial flavoproteins into reactive intermediates that damage bacterial DNA, ribosomal proteins, and metabolic enzymes; its established clinical use is limited to lower urinary tract infections.

The relationship between UTI and rheumatoid arthritis proposed by TxGNN has no established pharmacological basis in the evidence provided. One self-controlled case series (PMID 31222078) does suggest antibiotic exposure may correlate with timing of RA flares — but this describes an epidemiological association with antibiotics as a class in the context of infection-triggered flares, not a therapeutic effect of nitrofurantoin on RA disease activity.

Critically, the majority of the literature returned for this pairing runs in the **opposite direction** of a repurposing signal: it documents nitrofurantoin (alone or combined with methotrexate) as a **cause** of pulmonary fibrosis and interstitial lung disease specifically in RA patients (PMIDs 15195196, 35145797, 25362778, 3335140, 4608019). This means the high TxGNN score should be treated as a knowledge-graph artifact (RA and nitrofurantoin co-occur frequently in the toxicity literature) rather than a genuine repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Self-controlled Case Series | Scientific Reports | Nested SCCS in 31,992 newly diagnosed RA patients (UK CPRD GOLD) examining association between antibiotic exposure timing and RA flares |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Reviews drug-induced pulmonary fibrosis; lists nitrofurantoin among causative drugs and notes RA itself predisposes to pulmonary fibrosis |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du Praticien | Drug-induced interstitial lung disease review; nitrofurantoin listed among antibiotics implicated |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case Report | Cureus | 94-year-old RA patient on methotrexate developed irreversible pulmonary fibrosis after nitrofurantoin for UTI — drug-drug toxicity interaction |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | 57 RA patients hospitalized for interstitial lung fibrosis; poor prognosis reported |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case Report | Annales de Dermatologie et de Vénéréologie | Case of phenylbutazone-induced sialadenitis; nitrofurantoin noted among other drugs reported to cause sialadenitis |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Cohort | Acta Medica Scandinavica | Screening/short-term nitrofurantoin treatment of bacteriuria in middle-aged women, with 1-year follow-up (no RA-specific findings) |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case Report | Cureus | Autoimmune hepatitis differential diagnosis case; nitrofurantoin listed among drugs to rule out, RA noted as a differential autoimmune association |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case Report | Revue de Pneumologie Clinique | Gold salt-induced pneumonia with CD4 alveolitis (comparator DMARD toxicity, not nitrofurantoin-specific) |
| [4608019](https://pubmed.ncbi.nlm.nih.gov/4608019/) | 1974 | Review | Der Internist | General synopsis of alveolitis and pulmonary fibrosis etiologies |

---

## Singapore Market Information

Nitrofurantoin currently has no registered license in Singapore under this evidence pack (`total_licenses: 0`, `market_status: 未上市`/Not Marketed). No product records are available to list.

---

## Safety Considerations

The `safety` block in the evidence pack contains no usable data (key warnings, contraindications, and DDI query all returned Data Gap / not_found).

However, the literature gathered while evaluating predicted indications surfaced recurring adverse-event signals for nitrofurantoin that are directly relevant to risk-benefit assessment:
- **Pulmonary toxicity**: interstitial lung disease / pulmonary fibrosis, including a documented irreversible case when combined with methotrexate in an RA patient (PMID 35145797).
- **Methemoglobinemia**: reported via photoactivation and in neonatal drug-induced cases (from the "methemoglobinemia" candidate evidence).
- **Hepatotoxicity**: nitrofurantoin appears among drugs requiring exclusion in autoimmune hepatitis differential diagnosis (PMID 41635325).

These are toxicity signals, not formal labeling data — please refer to the official package insert for authoritative safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.89%), there are zero clinical trials and no RCT-level literature supporting nitrofurantoin for rheumatoid arthritis; the available literature largely documents nitrofurantoin-induced pulmonary and hepatic toxicity in RA patients rather than efficacy, pointing to a risk signal rather than a repurposing opportunity. The drug is also not currently marketed in Singapore, and all 10 TxGNN-predicted indications for this candidate (including several ultra-rare genetic syndromes with zero supporting literature, and two — methemoglobinemia and sclerosing cholangitis — where nitrofurantoin is a known causative/risk factor rather than a treatment) independently received a Hold recommendation.

**To proceed, the following is needed:**
- HSA/manufacturer package insert warnings and contraindications (currently a Blocking data gap, DG001)
- Verified mechanism of action data from DrugBank (High-severity data gap, DG002)
- A genuine pharmacological or preclinical rationale linking nitrofurantoin to RA pathophysiology, beyond epidemiological co-occurrence
- Reassessment of Singapore market/registration pathway given current non-marketed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

