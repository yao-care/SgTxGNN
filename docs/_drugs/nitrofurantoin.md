---
layout: default
title: Nitrofurantoin
parent: Low Evidence (L5)
nav_order: 717
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Nitrofurantoin: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not stated in the Singapore licence data (nitrofurantoin is generally…"
---

# Nitrofurantoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis

## One-Sentence Summary

Nitrofurantoin is an oral urinary antibacterial. The singapore licence records compiled for this report do not list an approved indication, so the original use is inferred from the drug class.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are **0 clinical trials** and **no publications showing therapeutic benefit**. The retrieved literature mostly describes adverse effects.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence data (nitrofurantoin is generally used for urinary tract infections) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Nitrofurantoin is a urinary antibacterial, and its efficacy in urinary tract infection is established. No anti-rheumatic mechanism is known.

The high score (0.999) is likely driven by network associations in the knowledge graph, such as shared adverse-effect or comorbidity links. It is not driven by evidence of efficacy. The retrieved papers describe nitrofurantoin- and methotrexate-associated pulmonary fibrosis, drug-induced interstitial lung disease, and a study of antibiotic exposure and RA flares. They show harm or confounding in RA patients, not benefit. The prediction should be treated as a hypothesis only.

Other predicted indications were also reviewed. These include diabetic nephropathy, sclerosing cholangitis, methemoglobinemia, gout and several rare congenital syndromes. None has supporting trials or a plausible therapeutic mechanism. Where literature exists, it points to adverse effects: liver injury, methemoglobinemia, or teratogenicity signals.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohort (self-controlled case series) | Scientific Reports | Examined the association between antibiotic use and flares in newly diagnosed RA (n = 31,992). It concerns flare risk, not treatment benefit. |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | A 94-year-old woman with RA on methotrexate developed irreversible pulmonary fibrosis after nitrofurantoin. Describes a harmful interaction. |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Drug-induced pulmonary fibrosis. Lists nitrofurantoin as a cause and RA as a predisposing disease. |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du Praticien | Drug-induced interstitial lung diseases. Nitrofurantoin is among the implicated antibiotics. |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | RA patients hospitalised for interstitial lung fibrosis had a poor prognosis. No nitrofurantoin efficacy data. |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case report | Cureus | Autoimmune hepatitis versus drug-induced liver injury. Nitrofurantoin is listed as a possible cause that must be excluded. |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case report | Annales de Dermatologie et de Vénéréologie | Phenylbutazone-induced sialadenitis. Nitrofurantoin is only mentioned as another reported cause. |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case report | Revue de Pneumologie Clinique | Gold salt-induced pneumonitis. Not directly relevant to nitrofurantoin. |

None of these papers reports a therapeutic benefit of nitrofurantoin in rheumatoid arthritis.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00439P | AA PHARMA NITROFURANTOIN TABLET 50 mg | Tablet | Not stated in the data compiled |
| SIN00290P | AA PHARMA NITROFURANTOIN TABLET 100 mg | Tablet | Not stated in the data compiled |

Both licences are valid single-ingredient oral tablets from Apotex Inc.

## Safety Considerations

- **Contraindications and risk conditions (from knowledge-graph associations, not label text):**
  - Renal: impaired renal function, anuria.
  - Lung: interstitial lung disease, pulmonary fibrosis, postinflammatory pulmonary fibrosis.
  - Liver and biliary: drug-induced liver injury, hepatitis, obstructive jaundice, biliary tract disease.
  - Nerve and eye: peripheral neuropathy, peripheral nervous system disease, optic neuritis.
  - Blood and metabolic: G6PD deficiency, diabetes mellitus, diabetic ketoacidosis, vitamin B12 deficiency, vitamin B deficiency, beriberi, ariboflavinosis, glycogen storage disease, cystinuria, galactosemia.
  - Gut: Clostridium difficile colitis, perinatal necrotizing enterocolitis.
- **Drug Interactions:** The interaction check returned 100 records; 20 are shown here. Moderate-level interactions include balsalazide, metronidazole, picosulfuric acid, naltrexone, rosuvastatin and simvastatin. Minor-level interactions include several anticholinergics (atropine, hyoscyamine, glycopyrronium, dicyclomine, scopolamine and others) and magnesium-containing antacids.
- **Relevance to the predicted indications:** The literature supports nitrofurantoin causing pulmonary fibrosis, liver injury, and hemolysis or methemoglobinemia (especially in G6PD deficiency). Its use in RA is particularly concerning because RA patients often take methotrexate, which also carries pulmonary toxicity, and because RA itself can involve the lung. Reduced efficacy and greater toxicity with impaired renal function argue against use in diabetic nephropathy.

Please also refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials, and the literature shows adverse effects rather than benefit. No anti-rheumatic mechanism is known, and the drug's known toxicities (pulmonary, hepatic, hematologic) overlap with risks in RA patients. Evidence is L5 for rheumatoid arthritis.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible anti-inflammatory or immunomodulatory rationale
- Preclinical evidence of efficacy in an RA model
- The Singapore package insert, to confirm the approved indication, warnings and contraindications
- A benefit-risk assessment addressing pulmonary toxicity and the interaction with methotrexate before any clinical study is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

