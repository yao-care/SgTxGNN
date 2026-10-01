---
layout: default
title: Tolterodine
parent: Medium Evidence (L3-L4)
nav_order: 994
evidence_level: L3
indication_count: 10
---

# Tolterodine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Tolterodine: From Overactive Bladder to Low Compliance Bladder

## One-Sentence Summary

Tolterodine is an antimuscarinic bladder drug, used for overactive bladder and neurogenic detrusor overactivity.
The TxGNN model predicts it may be effective for **low compliance bladder**.
Support is limited: **1 small clinical trial** (which tests a different drug) and **9 publications**, mostly reviews and small studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Overactive bladder / neurogenic detrusor overactivity (HSA registry entries carry no indication text) |
| Predicted New Indication | Low compliance bladder |
| TxGNN Prediction Score | 96.31% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Tolterodine blocks M2/M3 muscarinic receptors in the bladder detrusor muscle. This suppresses involuntary contractions, which can lower storage pressure and raise bladder capacity. Low bladder compliance mostly occurs in neurogenic bladder, where detrusor overactivity is often the driver. In that setting the drug's mechanism applies directly.

The new indication is close to the drug's existing use, so the repurposing novelty is low. The mechanism should work less well where compliance is lost to fibrosis or structural change, such as the malacoplakia case in the literature. A detailed mechanism record is not available in the current database entry. The reasoning above rests on tolterodine's known class pharmacology.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05745584](https://clinicaltrials.gov/study/NCT05745584) | NA | Unknown | 15 | Prospective paired comparison of mirabegron versus anticholinergics in patients with low bladder compliance. The listing does not confirm that tolterodine is the comparator, and no results are posted. |

This is a small, non-phased trial with no results, so it carries limited weight.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20969642](https://pubmed.ncbi.nlm.nih.gov/20969642/) | 2010 | Clinical study | Int J Urol | Assessed extended-release tolterodine 4 mg/day in neurogenic detrusor overactivity and/or low-compliance bladder, using urodynamic parameters. The most directly relevant paper; the abstract excerpt does not give results. |
| [26676394](https://pubmed.ncbi.nlm.nih.gov/26676394/) | 2011 | Pilot crossover trial | Lower Urin Tract Symptoms | Compared oxybutynin and tolterodine in spina bifida patients with neurogenic bladder. |
| [25656013](https://pubmed.ncbi.nlm.nih.gov/25656013/) | 2015 | Retrospective clinical study | Hinyokika Kiyo | Mirabegron added to anticholinergics in 7 neurogenic bladder patients with detrusor overactivity or low compliance despite treatment. Videourodynamic evaluation; indirect for tolterodine. |
| [26149965](https://pubmed.ncbi.nlm.nih.gov/26149965/) | 2015 | Review | Curr Urol Rep | Tolterodine in male storage LUTS; antimuscarinics are the gold-standard drug class for OAB/storage symptoms. |
| [16465186](https://pubmed.ncbi.nlm.nih.gov/16465186/) | 2006 | Review | Br J Pharmacol | Muscarinic receptors (M2/M3) in the bladder detrusor and their role in antimuscarinic therapy for OAB. |
| [17594185](https://pubmed.ncbi.nlm.nih.gov/17594185/) | 2007 | Review | Expert Opin Investig Drugs | Overview of OAB treatments in early-phase trials. |
| [15978301](https://pubmed.ncbi.nlm.nih.gov/15978301/) | 2005 | Review | Clin Ther | Trospium (a related drug) for OAB with urge incontinence. |
| [24703195](https://pubmed.ncbi.nlm.nih.gov/24703195/) | 2014 | Clinical safety study | Int J Clin Pract | Pooled safety analysis of mirabegron in OAB; indirect for tolterodine. |
| [32590783](https://pubmed.ncbi.nlm.nih.gov/32590783/) | 2020 | Case report | Medicine | Poor bladder compliance due to malacoplakia with xanthogranulomatous cystitis; not specific to tolterodine. |

## Singapore Market Information

The registry shows 10 registrations in total; five are listed here. No approved-indication text is recorded for these entries.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN09912P | DETRUSITOL TABLET 2 mg | Tablet, film coated | Pfizer Italia S.r.L. |
| SIN16313P | TOLTERODINE MEVON IR FILM-COATED TABLET 2 MG | Tablet, film coated | Pharmathen S.A. |
| SIN16433P | TOLTERODINE MEVON SR CAPSULE 2 MG | Capsule, extended release | Pharmathen International S.A. |
| SIN16597P | TOLCORD 2 FILM COATED TABLET 2 MG | Tablet, film coated | Intas Pharmaceuticals Limited |
| SIN16598P | TOLCORD 1 FILM COATED TABLET 1 MG | Tablet, film coated | Intas Pharmaceuticals Limited |

All listed products are oral formulations.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and sits close to the drug's established use. However, the supporting evidence is thin: one small trial with no results (which may not even involve tolterodine) and a few small clinical studies. The package insert safety review has not been done, so the candidate cannot yet pass safety screening. It is best treated as a research question rather than a deployment candidate.

The other nine predictions (ranks 2-10, such as polycystic kidney disease and thoracic malformation) have no plausible mechanism and no trial evidence. They rest only on knowledge-graph proximity and should stay on hold.

**To proceed, the following is needed:**
- Download and review the HSA package insert (warnings and contraindications)
- Detailed mechanism of action data from DrugBank
- Full-text review of PMID 20969642 and PMID 26676394 for urodynamic outcomes, especially bladder compliance
- Confirmation of whether tolterodine is the anticholinergic comparator in NCT05745584
- A comparison against current guideline therapy for low compliance bladder in neurogenic patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

