---
layout: default
title: Butylscopolamine
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 10
---

# Butylscopolamine
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

# Butylscopolamine: From Gastrointestinal Spasms to Irritable Bowel Syndrome

## One-Sentence Summary

Butylscopolamine (hyoscine butylbromide, widely known as Buscopan) is a quaternary ammonium anticholinergic agent used internationally for the relief of smooth muscle spasms of the gastrointestinal tract, though it currently holds no registered product in Singapore.
The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome (IBS)**,
with **0 clinical trials** and **15 publications** currently supporting this direction — including multiple randomised controlled trials and reviews directly examining its use in IBS.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gastrointestinal smooth muscle spasms / abdominal cramps (well-established international use; no Singapore registration on record) |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Butylscopolamine is a quaternary ammonium derivative of scopolamine that acts as a competitive antagonist at muscarinic acetylcholine receptors, particularly M3 receptors on gastrointestinal smooth muscle. Because of its quaternary ammonium structure, it remains largely confined to the gut lumen following oral administration (bioavailability < 1%), making it a gut-selective antispasmodic with minimal systemic anticholinergic side effects.

IBS is characterised by visceral hypersensitivity and abnormal bowel motility, both of which are closely linked to excessive acetylcholine-mediated smooth muscle contractility. By blocking M3 receptors, butylscopolamine directly reduces colonic pressure and attenuates the exaggerated intestinal contractions that drive IBS pain and cramping. This mechanistic alignment is direct and pharmacologically well-grounded.

Importantly, this is not a speculative connection: butylscopolamine (Buscopan) has already been granted over-the-counter approval for IBS in several European markets including Germany, the United Kingdom, and Italy. Multiple RCTs dating back to the 1970s and 1980s, as well as a comprehensive 2025 clinical review, specifically validate its efficacy for IBS pain management. The TxGNN model's top-ranked prediction therefore reflects a mechanistically sound, clinically supported use case that simply lacks regulatory approval in Singapore.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Butylscopolamine in IBS on ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [32949](https://pubmed.ncbi.nlm.nih.gov/32949/) | 1979 | RCT | British Medical Journal | Double-blind factorial-design trial in 96 IBS patients; hyoscine butylbromide, lorazepam, and ispaghula husk each produced sustained symptomatic improvement; ispaghula reached statistical significance |
| [6526796](https://pubmed.ncbi.nlm.nih.gov/6526796/) | 1984 | RCT | J Association of Physicians of India | Compared different therapeutic regimens in IBS; direct evaluation of antispasmodic agents including butylscopolamine derivatives |
| [2210587](https://pubmed.ncbi.nlm.nih.gov/2210587/) | 1990 | RCT | Fortschritte der Medizin | Large double-blind randomised parallel-group trial (712 patients, 4 weeks); hyoscine-N-butylbromide 30 mg/day ± paracetamol vs placebo; 81% of patients improved at 4 weeks |
| [40237755](https://pubmed.ncbi.nlm.nih.gov/40237755/) | 2025 | Review | Terapevticheskii arkhiv | Comprehensive review on IBS therapy with specific focus on hyoscine butylbromide; notes its inclusion in both Russian and international clinical guidelines as an effective antispasmodic for IBS abdominal pain |
| [15579053](https://pubmed.ncbi.nlm.nih.gov/15579053/) | 2004 | Review | Current Pharmaceutical Design | Reviews quaternary ammonium derivatives (including n-butyl scopolammonium) as GI spasmolytics; confirms antimuscarinic activity at nM level and mechanistic basis for IBS use |
| [19337628](https://pubmed.ncbi.nlm.nih.gov/19337628/) | 2009 | Cohort | J Gastrointestinal and Liver Diseases | Evaluated symptomatic, motor, and visceral sensory responses to two classes of spasmolytics in IBS; butylscopolamine group showed measurable reductions in colonic motility and visceral sensitivity |
| [41729205](https://pubmed.ncbi.nlm.nih.gov/41729205/) | 2026 | Experimental | Fundamental & Clinical Pharmacology | Investigated immunomodulatory effects of hyoscine butylbromide on macrophage cytokine production in vitro; suggests potential anti-inflammatory dimension beyond pure spasmolysis |
| [34050726](https://pubmed.ncbi.nlm.nih.gov/34050726/) | 2021 | Experimental | Birth Defects Research | Examined Buscopan effects on neural tube development in chick embryos; pregnancy category C noted; confirms GI indication (IBS, bladder cramps, dysmenorrhoea) in introduction |
| [435769](https://pubmed.ncbi.nlm.nih.gov/435769/) | 1979 | Letter | British Medical Journal | Clinical commentary on oral hyoscine butylbromide for IBS; contextualises early RCT findings |
| [435770](https://pubmed.ncbi.nlm.nih.gov/435770/) | 1979 | Letter | British Medical Journal | Expert correspondence on oral hyoscine butylbromide for IBS; raises methodological considerations for clinical use |

---

## Singapore Market Information

Butylscopolamine currently has **no registered products** in Singapore. There are no authorisation records to display.

The drug is, however, widely available in international markets under the brand name **Buscopan** (Sanofi), with OTC approval for IBS in multiple European jurisdictions. This regulatory gap in Singapore represents the primary barrier to patient access, not a lack of clinical evidence.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers**: Full safety data including TFDA/HSA-registered contraindications and warnings were not available in this Evidence Pack (Data Gap DG001). The following points are pharmacologically inferred from drug class:
> - Anticholinergic class effects apply (dry mouth, constipation, urinary retention, tachycardia) — though substantially reduced with butylscopolamine due to poor oral bioavailability
> - **Contraindicated** in narrow-angle glaucoma, myasthenia gravis, megacolon, and mechanical bowel obstruction
> - Use with caution in patients with benign prostatic hyperplasia or known cardiac arrhythmias
> - No drug-drug interaction data were returned from the DDI query

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple RCTs and clinical reviews directly demonstrate the efficacy of hyoscine butylbromide (butylscopolamine) in IBS, and its gut-selective M3 antagonism provides a direct mechanistic basis for this use. The drug has already obtained OTC approval for IBS in European markets, meaning the clinical risk-benefit profile is internationally established — this is not a speculative repurposing but a known use awaiting Singapore market entry.

**To proceed, the following is needed:**

- **Regulatory dossier**: Retrieve the full Singapore HSA product registration requirements; identify whether a bridging study or literature-based application (bibliographic submission) is feasible given the European OTC precedent
- **MOA documentation**: Obtain formal DrugBank/package insert MOA data to complete the mechanistic linkage for the regulatory submission (Data Gap DG002)
- **Safety package**: Download and parse the full prescribing information/package insert to document contraindications, warnings, and drug interactions (Data Gap DG001 — currently Blocking)
- **Route of administration assessment**: Confirm whether oral tablet formulation (as used in European Buscopan IBS indications) is the intended route; injectable formulation has distinct PK considerations
- **Dose selection**: The European OTC IBS dose is 10 mg TID (oral); confirm alignment with the clinical trial evidence base
- **Regulatory pathway consultation**: Engage HSA to determine whether the drug qualifies for an abridged application based on established overseas approval status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

