---
layout: default
title: Manganese
parent: 僅模型預測 (L5)
nav_order: 628
evidence_level: L5
indication_count: 10
---

# Manganese
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

# Manganese: From Essential Trace Element Supplementation to Predicted Association with Sclerosing Cholangitis

## One-Sentence Summary

> Manganese is an essential trace element with no approved therapeutic indication and no marketing authorization in Singapore — it is more commonly used as a trace-mineral component of parenteral nutrition (PN).
> The TxGNN model's top-ranked signal links manganese to **Sclerosing Cholangitis** (score **85.41%**),
> but the supporting evidence — **0 clinical trials** and **6 publications** — describes manganese *accumulation as a consequence* of cholestatic disease rather than a therapeutic effect, and the evidence pack itself flags this as a reverse-causality/toxicity signal warranting a **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — Manganese has no recorded approved indication and is not marketed in Singapore (0 licenses on file); traditionally used as an essential trace-mineral component in parenteral nutrition supplementation |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 85.41% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for manganese in this evidence pack. Based on known pharmacology, manganese is an essential trace element and cofactor for several metalloenzymes; its physiological role — rather than any established disease-modifying indication — has been the basis for its use as a supplementation component (e.g., in parenteral nutrition trace-mineral mixes).

The relationship between manganese and sclerosing cholangitis identified by TxGNN, however, does **not** appear to be a therapeutic association. The literature evidence consistently shows the opposite direction of causality: because the liver and biliary tree are the primary excretory route for manganese, cholestatic diseases such as primary sclerosing cholangitis (PSC) and primary biliary cirrhosis (PBC) impair manganese clearance, leading to its **accumulation** in blood and CNS tissue (basal ganglia), with at least one case report describing overt manganese-overload neurotoxicity in a patient with sclerosing cholangitis. In other words, the biological link uncovered by the model reflects manganese as a **biomarker/toxicity consequence** of the disease rather than manganese as a **treatment** for the disease.

Given this, the mechanistic plausibility for a genuine repurposing benefit is weak, and the signal should be interpreted primarily as a caution flag (risk of manganese toxicity in cholestatic patients) rather than a therapeutic hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33428478](https://pubmed.ncbi.nlm.nih.gov/33428478/) | 2021 | Cohort | Scandinavian Journal of Clinical and Laboratory Investigation | Blood Mn and Cu levels were elevated in PBC/PSC patients with long-term cholestasis, indicating trace-metal accumulation/toxicity rather than therapeutic benefit |
| [39815815](https://pubmed.ncbi.nlm.nih.gov/39815815/) | 2025 | Case report | Haematologica | Manganese overload identified as a contributing factor to neurological symptoms in a sclerosing cholangitis patient (Langerhans cell histiocytosis) — a toxicity signal |
| [10499363](https://pubmed.ncbi.nlm.nih.gov/10499363/) | 1999 | Cohort/Review | Neurotoxicology | Examined iron/manganese homeostasis in chronic liver disease and its correlation with pallidal T1-weighted MRI hyperintensity, linking Mn accumulation to hepatic dysfunction rather than treatment |
| [7944963](https://pubmed.ncbi.nlm.nih.gov/7944963/) | 1993 | Histopathology | Arkhiv Patologii | Histological/ultrastructural study of PSC liver morphology; unrelated to manganese as a therapeutic agent |
| [23917144](https://pubmed.ncbi.nlm.nih.gov/23917144/) | 2013 | Cohort | Free Radical Biology & Medicine | Studied inflammation-related DNA damage and CD133/Oct3/4 expression in cholangiocarcinoma; not related to manganese intervention (likely embedding mismatch) |
| [12612912](https://pubmed.ncbi.nlm.nih.gov/12612912/) | 2003 | In vitro (mechanistic) | Gastroenterology | Examined cytokine-stimulated nitric oxide effects on cholangiocyte cAMP-dependent secretion; no direct manganese linkage (likely embedding mismatch) |

---

## Singapore Market Information

Manganese currently has no marketing authorization or registered product license in Singapore (Market Status: **Not Marketed**, 0 registrations on file). No dosage forms or approved indication text are available for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-interaction data were not available in this evidence pack — HSA labeling data has been flagged in the underlying data-gap log as a Blocking item (DG001) required before any safety pre-assessment can proceed.)*

---

## Other Predicted Indications in This Evidence Pack (Context)

For completeness, note that Sclerosing Cholangitis is the *highest-scoring* TxGNN prediction but is **not** the *best-supported* one in this pack. Several lower-ranked predictions carry comparatively more coherent (though still early-stage) mechanistic rationale and were staged at S1 ("Research Question") rather than S0 ("Hold"):

- **Dry eye syndrome** (rank 3, score 81.82%, L4/S1) — Mn is a cofactor of MnSOD; several preclinical Mn-porphyrin SOD-mimetic models show reduced ocular-surface oxidative damage.
- **Drug-induced osteoporosis** (rank 4, score 80.61%, L4/S1) — Mn is a required cofactor for glycosyltransferases involved in bone matrix synthesis; supported by a single narrative review.
- **Vitamin/mineral deficiency disorder** (rank 8, score 74.30%, L3/S1) — reflects Mn's established role as a standard parenteral-nutrition/multi-mineral supplement component (a real but non-novel use); note literature also documents a narrow therapeutic window (manganese-induced parkinsonism at excess doses).

None of these reached a "Go" recommendation in the evidence pack; they are noted here only so the sclerosing cholangitis signal is not read as the strongest candidate in this drug's prediction set.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (Sclerosing Cholangitis) is supported only by observational/case-level literature describing manganese accumulation as a *consequence* of cholestatic disease, not a therapeutic signal — this is a reverse-causality/toxicity pattern rather than repurposing evidence, with zero clinical trials and no MOA data available.

**To proceed, the following is needed:**
- HSA (Singapore) label/warnings and contraindication data (currently a Blocking data gap, DG001)
- Manganese mechanism of action data from DrugBank or equivalent (currently a High-severity data gap, DG002)
- A mechanistic study specifically distinguishing therapeutic manganese supplementation from pathological manganese accumulation in cholestatic patients, before this candidate can be re-evaluated
- If pursuing an alternative indication from this pack, prioritize confirmatory preclinical/observational follow-up on dry eye syndrome, drug-induced osteoporosis, or vitamin deficiency disorder, which currently carry more plausible (if still preliminary) mechanistic support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

