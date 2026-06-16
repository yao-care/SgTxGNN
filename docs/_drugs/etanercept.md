---
layout: default
title: Etanercept
parent: 僅模型預測 (L5)
nav_order: 400
evidence_level: L5
indication_count: 10
---

# Etanercept
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

# Etanercept: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Etanercept (Enbrel) is a recombinant p75 TNF receptor fusion protein approved in the US and EU for rheumatoid arthritis, juvenile idiopathic arthritis, psoriatic arthritis, ankylosing spondylitis, and plaque psoriasis — but currently **not registered in Singapore**.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**, with **6 clinical trials** and **20 publications** informing this direction.
However, the available clinical data present a paradox: the most directly relevant trial (WGET, NCT00001901) demonstrated **failure** in ANCA-associated vasculitis, and multiple pharmacovigilance studies document that etanercept can itself **induce** vasculitis as an adverse effect — making the safety signal substantially stronger than any putative therapeutic benefit.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis / inflammatory arthritis (FDA/EMA approved; no Singapore HSA registration) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on the extensive published literature retrieved, etanercept is a dimeric fusion protein comprising two extracellular domains of the human p75 TNF receptor (TNFR2) linked to the Fc region of IgG1. It acts as a soluble decoy receptor, binding and neutralising both TNF-α and lymphotoxin-α (TNF-β), thereby preventing downstream pro-inflammatory signalling. This mechanism has proven efficacy across multiple immune-mediated diseases including synovitis, enthesitis, and plaque inflammation.

Rheumatoid vasculitis (RV) is a severe extra-articular manifestation of long-standing, typically seropositive rheumatoid arthritis. It primarily affects small- to medium-sized blood vessels and can present as digital infarcts, peripheral neuropathy, cutaneous ulcers, and systemic organ injury. Since TNF-α is a known driver of endothelial activation, neutrophil recruitment, and immune-complex deposition in vessel walls, blockade of this cytokine represents a mechanistically plausible intervention for RV. A 2021 systematic review (PMID 33058033) specifically evaluated biological agents — including TNF inhibitors — in RV treatment, confirming this rationale has been formally investigated.

Despite this mechanistic logic, clinical evidence raises serious concerns. The WGET trial (NCT00001901, Phase I/II in Wegener's granulomatosis — an ANCA-associated vasculitis closely related to RV in pathophysiology) showed that etanercept was unable to maintain remission and was associated with excess adverse events. More critically, multiple case series (PMID 12209493, PMID 15853915) and registry cohort analyses (PMID 28123776) have documented that etanercept can **paradoxically induce** cutaneous and systemic vasculitis in RA patients — a phenomenon possibly driven by Type I interferon upregulation compensating for TNF-α blockade. The weight of evidence therefore favours a Hold decision, as the drug may worsen rather than treat this condition.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001901](https://clinicaltrials.gov/study/NCT00001901) | Phase I/II | Completed | 60 | Direct Phase I/II study of etanercept (TNFR:Fc) in Wegener's granulomatosis, a form of ANCA-associated vasculitis. This is the precursor to the landmark WGET trial, which subsequently demonstrated that etanercept was **ineffective** for ANCA vasculitis maintenance and was associated with increased severe adverse events. Provides the most mechanistically direct clinical evidence for this indication — and it argues against use. |
| [NCT01557322](https://clinicaltrials.gov/study/NCT01557322) | N/A | Completed | 1,754 | Real-world observational study comparing RA patients newly initiated on etanercept versus non-biologic DMARDs (BSRBR data). Not designed for vasculitis endpoints; provides general effectiveness and safety context only. |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large pharmacoepidemiological study assessing the risk of developing incident immune-mediated inflammatory diseases in patients treated with biologics for a single IMID. Safety and epidemiological context; no vasculitis efficacy data. |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completed | 808 | Cross-sectional study of biologic DMARD treatment patterns and demographics in Chinese RA patients. Not vasculitis-specific. |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Multi-national observational study of tocilizumab efficacy and safety in RA patients with inadequate response to non-biologic or biologic DMARDs. Provides context for second-line biologic sequencing but no RV-specific data. |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Phase 2 study assessing immunosuppressant management during elective total shoulder arthroplasty in rheumatology patients. Perioperative focus; no vasculitis efficacy endpoints. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | PRISMA-compliant systematic review of biological drug use in rheumatoid vasculitis. Confirms TNF inhibitors and other biologics have been evaluated in RV, but highlights the overall paucity of high-quality evidence and mixed results. |
| [28391344](https://pubmed.ncbi.nlm.nih.gov/28391344/) | 2017 | Review | Nephrology, Dialysis, Transplantation | Critical review of TNFα blockade in ANCA-associated vasculitis and glomerulonephritis. Summarises the mechanistic rationale and the clinical trial evidence for and against TNF inhibition in vasculitic kidney disease; concludes that current evidence does not support routine use. |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort | RMD Open | BSRBR-RA registry data comparing vasculitis-like event (VLE) rates in TNFi-treated RA patients vs those on non-biologic DMARDs. Quantifies drug-specific VLE risk — a key safety signal directly relevant to this repurposing question. |
| [24854356](https://pubmed.ncbi.nlm.nih.gov/24854356/) | 2014 | Cohort | Annals of the Rheumatic Diseases | Single-centre cohort evaluating whether serial ANA testing predicts bDMARD-induced ANA/dsDNA production and vasculitis in RA patients. Provides actionable monitoring guidance. |
| [15853915](https://pubmed.ncbi.nlm.nih.gov/15853915/) | 2005 | Case Series | Scandinavian Journal of Immunology | Immunological characterisation of cutaneous vasculitis occurring during etanercept and infliximab therapy; proposes immune-complex deposition and Type I IFN dysregulation as underlying mechanisms for TNFi-induced vasculitis. |
| [31668853](https://pubmed.ncbi.nlm.nih.gov/31668853/) | 2019 | Comparative Study | Biologicals | Real-world national cohort comparing original etanercept (ETN) vs biosimilar SB4 in active RA (n = large registry). Confirms comparable efficacy and safety profiles between originator and biosimilar; useful for Singapore context given non-registration status. |
| [12209493](https://pubmed.ncbi.nlm.nih.gov/12209493/) | 2002 | Case Series | Arthritis & Rheumatism | Early report documenting accelerated nodulosis **and** vasculitis following etanercept therapy in RA patients — one of the first safety alerts for paradoxical vascular inflammation under TNF blockade. |
| [11792895](https://pubmed.ncbi.nlm.nih.gov/11792895/) | 2002 | Case Series | Rheumatology (Oxford) | Case series documenting cutaneous vasculitis associated with both etanercept and infliximab, highlighting a class-level adverse effect signal for TNF inhibitors. |
| [38931826](https://pubmed.ncbi.nlm.nih.gov/38931826/) | 2024 | PK Study | Pharmaceutics | Population pharmacokinetic modelling of adalimumab and etanercept biosimilar dosing in RA; supports dose-interval optimisation strategies relevant to biosimilar access contexts like Singapore. |
| [31632872](https://pubmed.ncbi.nlm.nih.gov/31632872/) | 2019 | Case Report | Cureus | Etanercept-associated nephropathy via autoantibody formation and immune-complex deposition — illustrates this drug's broader propensity to trigger paradoxical autoimmune phenomena during TNF-α blockade. |

---

## Singapore Market Information

Etanercept is currently **not registered** with the Health Sciences Authority (HSA) of Singapore. No product licences are on record, and the drug is not available on the Singapore market.

For reference, etanercept (Enbrel) is authorised by the FDA (since 1998) and EMA for: rheumatoid arthritis, juvenile idiopathic arthritis, psoriatic arthritis, ankylosing spondylitis, non-radiographic axial spondyloarthritis, and moderate-to-severe plaque psoriasis (including paediatric formulation). Biosimilars (e.g., SB4/Benepali, GP2015/Erelzi) are authorised in multiple jurisdictions for the same indications.

---

## Safety Considerations

Detailed Singapore HSA-specific safety information is not available as etanercept is not registered with the HSA. Please refer to the international package insert (EMA SmPC / US Prescribing Information) for comprehensive safety information. Key internationally documented safety considerations include:

- **Serious infections**: Increased risk of bacterial, fungal, and opportunistic infections including tuberculosis (TB reactivation). TB screening is mandatory prior to initiation.
- **Paradoxical inflammatory reactions**: Drug-induced vasculitis and accelerated nodulosis have been reported in RA patients on etanercept — directly relevant to this repurposing question.
- **Neurological events**: Cases of demyelinating disease (e.g., multiple sclerosis, optic neuritis) have been reported.
- **Malignancy**: Lymphoma and other malignancies have been observed; causal relationship remains uncertain.
- **Cardiac events**: Use is contraindicated or requires caution in patients with New York Heart Association (NYHA) Class III/IV heart failure.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns etanercept a high prediction score for rheumatoid vasculitis (99.71%), reflecting the biological plausibility of TNF-α blockade in vascular inflammation, the clinical evidence landscape is strongly unfavourable: the most directly relevant trial (NCT00001901 / WGET lineage) demonstrated that etanercept was ineffective in ANCA-associated vasculitis, and converging pharmacovigilance data confirm that the drug can paradoxically *induce* vasculitis rather than resolve it. The safety signal clearly exceeds any evidence of therapeutic benefit for this specific indication.

**To proceed, the following is needed:**
- Retrieve formal MOA data from DrugBank API (Data Gap DG002) to precisely characterise etanercept's immune-modulatory profile in the context of RV pathophysiology
- Obtain Singapore HSA-equivalent package insert safety data (Data Gap DG001) before any local safety assessment can be completed
- Conduct a targeted systematic review distinguishing *therapeutic* use of etanercept in confirmed RV from adverse-effect reports — to determine whether any clinical sub-population (e.g., refractory RV failing conventional immunosuppression) might selectively benefit
- Benchmark against rituximab (anti-CD20), which has demonstrated superiority over conventional therapy in RV and would serve as the reference standard for any future comparative design
- If further development is pursued despite current evidence, a safety-monitored pilot study with early stopping rules and rigorous vasculitis biomarker tracking (ANCA, cryoglobulins, complement levels) would be the minimum requirement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

