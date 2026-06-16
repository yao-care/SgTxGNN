---
layout: default
title: Ethambutol
parent: 僅模型預測 (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
---

# Ethambutol
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

# Ethambutol: From Tuberculosis to Epiglottitis

## One-Sentence Summary

Ethambutol is a first-line antitubercular agent and a core component of the WHO-standard four-drug regimen (HRZE: isoniazid, rifampicin, pyrazinamide, ethambutol) for active tuberculosis.
The TxGNN model predicts it may be effective for **Epiglottitis**, with **0 clinical trials** and **2 publications** currently supporting this direction — both relating to laryngeal tuberculosis broadly rather than epiglottitis specifically.
The prediction reflects knowledge-graph proximity within TB-related diseases rather than a clearly distinct new therapeutic opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Tuberculosis (first-line HRZE regimen member) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the current dataset. Based on known pharmacology, Ethambutol inhibits arabinosyl transferase enzymes (EmbA, EmbB, EmbC) involved in the synthesis of arabinogalactan in the mycobacterial cell wall. This makes it bacteriostatic specifically against *Mycobacterium tuberculosis* and some non-tuberculous mycobacteria (NTM). It has no known activity against the bacteria that typically cause epiglottitis.

Epiglottitis in clinical practice is most commonly caused by *Haemophilus influenzae* type b, group A Streptococcus, or other pyogenic organisms — none of which are targets of Ethambutol. However, *Mycobacterium tuberculosis* can, in extremely rare cases, invade the epiglottis and produce tuberculous epiglottitis. In that narrow clinical scenario, Ethambutol would be deployed as part of the standard HRZE regimen rather than as a standalone novel therapy.

The two literature items supporting this prediction both focus on laryngeal tuberculosis in general, with the epiglottis mentioned as one of several anatomically affected subsites. The connection to epiglottitis is therefore indirect: the TxGNN model appears to have captured TB's capacity to involve epiglottic tissue through knowledge-graph adjacency, rather than identifying a genuinely novel repurposing use case for Ethambutol.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [14720571](https://pubmed.ncbi.nlm.nih.gov/14720571/) | 2004 | Case series / Clinical review | *The Lancet Infectious Diseases* | Review of laryngeal tuberculosis covering clinical features, diagnosis, and treatment; the epiglottis is cited as one of the anatomical subsites that TB can affect |
| [2806495](https://pubmed.ncbi.nlm.nih.gov/2806495/) | 1989 | Retrospective case series | *European Respiratory Journal* | Analysis of 41 laryngeal TB cases (1975–1985); epiglottis was the second most commonly involved laryngeal site after the true vocal cords; patients were treated with isoniazid, rifampicin, and ethambutol |

---

## Singapore Market Information

Ethambutol is **not registered** in Singapore. No product authorizations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for clinical use:** Ethambutol carries a well-documented risk of optic neuritis (dose- and duration-dependent), which can cause visual acuity loss and colour vision impairment. Baseline and periodic ophthalmological monitoring are standard of care. Renal impairment significantly increases drug accumulation and toxicity risk — dose adjustment is required. A case report (PMID 29776936) documents severe neurotoxicity in a peritoneal dialysis patient receiving standard anti-TB therapy including Ethambutol.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Tuberculous epiglottitis is an extremely rare clinical entity. Ethambutol's role in this setting is as a component of the standard HRZE regimen for TB — not as an independent new therapeutic indication. Current evidence consists solely of indirect laryngeal TB case series in which the epiglottis happens to be one of several involved sites, with no clinical trials and no epiglottitis-focused studies. The TxGNN high score most likely reflects knowledge-graph proximity among TB-related upper-airway disease nodes rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Retrieval of Ethambutol's full mechanism of action data from DrugBank (remediation for DG002 is already identified: DrugBank API query)
- Systematic review of tuberculous epiglottitis incidence data to quantify the addressable patient population
- Case reports or retrospective series specifically documenting Ethambutol use in confirmed tuberculous epiglottitis, distinct from general laryngeal TB
- Assessment of Singapore's epidemiological burden of extrapulmonary TB with upper-airway involvement before any local development pathway can be evaluated
- Resolution of the missing Singapore package insert data (DG001) to complete a safety assessment before any clinical positioning work begins
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

