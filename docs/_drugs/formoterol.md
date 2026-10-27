---
layout: default
title: Formoterol
parent: Low Evidence (L5)
nav_order: 452
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Formoterol: predicted new indication Bronchitis (evidence level L5). Approved use: Pulmonary emphysema, intrinsic asthma, allergic asthma"
monitor_inn: "Formoterol"
predicted_indications: ["respiratory malformation", "bronchitis", "Rienhoff syndrome", "atopic eczema", "hyperlucent lung"]
---

# Formoterol
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

## Formoterol: From Pulmonary Emphysema and Asthma to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Formoterol is a long-acting beta2-agonist bronchodilator, originally used for pulmonary emphysema and asthma (intrinsic and allergic).
The TxGNN model predicts it may be effective for **Bronchitis** (chronic bronchitis within COPD), with **18 clinical trials** and **18 publications** currently supporting this direction.
Most of this evidence comes from COPD studies of formoterol-containing combinations, so it is strong but not specific to formoterol alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary emphysema, intrinsic asthma, allergic asthma (the Singapore licence records contain no approved-indication text) |
| Predicted New Indication | Bronchitis (top-ranked prediction by TxGNN: respiratory malformation; see the note below) |
| TxGNN Prediction Score | 99.92% (bronchitis); the top-ranked respiratory malformation scores 99.92% |
| Evidence Level | L1 (bronchitis) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 18 |
| Recommended Decision | Proceed with Guardrails |

**Note on prediction ranking:** The top-ranked prediction is *respiratory malformation* (score 99.92%). It has no clinical trials, and the literature concerns asthma and COPD rather than malformations. No plausible mechanism links formoterol to it, so the high score likely reflects graph proximity to respiratory disease. The first prediction with meaningful supporting evidence is *bronchitis* (rank 2), which this report focuses on.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, formoterol is a long-acting beta2-adrenoceptor agonist. It relaxes airway smooth muscle and produces rapid, sustained bronchodilation (onset within minutes, lasting around 12 hours). Its efficacy in asthma and emphysema is established, and mechanistically it may be applicable to airflow obstruction in chronic bronchitis.

Chronic bronchitis is a major COPD phenotype and shares airflow limitation with emphysema. The large COPD trials supporting this prediction, including Phase 3 studies of arformoterol and aclidinium/formoterol, show bronchodilator benefit. The evidence applies to chronic bronchitis within COPD, not to acute bronchitis or other subtypes. Much of it also comes from combination products or PK/safety designs, so the contribution of formoterol alone is not isolated.

Other predictions fall into two groups:
- **Obstructive lung disease** (score 99.90%, L1) and **asthma** (score 99.74%, L1) have strong Phase 3 and RCT support, but largely match the original indications, so they confirm existing use rather than represent true repurposing.
- **Rienhoff syndrome, asthma-related traits (susceptibility), atopic eczema, compensatory emphysema, interstitial emphysema and hyperlucent lung** have no clinical trial support and no credible mechanism. They are not recommended for further pursuit at this stage (Hold).

---

## Clinical Trial Evidence

Top trials for bronchitis (COPD / chronic bronchitis population):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01462942](https://clinicaltrials.gov/study/NCT01462942) | Phase 3 | Completed | 2443 | Aclidinium/formoterol fixed-dose combinations vs individual components and placebo in stable COPD |
| [NCT01437397](https://clinicaltrials.gov/study/NCT01437397) | Phase 3 | Completed | 1692 | 24-week efficacy and safety of aclidinium/formoterol combinations vs monotherapies and placebo |
| [NCT01572792](https://clinicaltrials.gov/study/NCT01572792) | Phase 3 | Completed | 921 | 28-week extension: long-term safety and tolerability of aclidinium/formoterol combinations |
| [NCT00064415](https://clinicaltrials.gov/study/NCT00064415) | Phase 3 | Completed | 799 | 12-month chronic safety study of (R,R)-formoterol (arformoterol) in COPD |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Phase 3 | Completed | 741 | 12-week bronchodilator effect and safety of arformoterol vs placebo and active control |
| [NCT01437540](https://clinicaltrials.gov/study/NCT01437540) | Phase 3 | Completed | 590 | Long-term safety of aclidinium/formoterol vs formoterol in stable COPD |
| [NCT00250679](https://clinicaltrials.gov/study/NCT00250679) | Phase 3 | Completed | 443 | 6-month long-term safety and efficacy of arformoterol vs active control in COPD |
| [NCT00626522](https://clinicaltrials.gov/study/NCT00626522) | Phase 2 | Completed | 808 | Dose-finding of formoterol combined with aclidinium vs monotherapies in moderate to severe COPD |
| [NCT00680056](https://clinicaltrials.gov/study/NCT00680056) | Phase 4 | Completed | 33 | Formoterol plus tiotropium vs formoterol alone on breathlessness and hyperinflation |
| [NCT06571942](https://clinicaltrials.gov/study/NCT06571942) | Phase 4 | Unknown | 128 | Inhaled triple therapies on the small airway in COPD or chronic bronchitis without obstruction (biomass exposure) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31015757](https://pubmed.ncbi.nlm.nih.gov/31015757/) | 2019 | Meta-analysis | Int J Chron Obstruct Pulmon Dis | Comparative risks of budesonide/formoterol vs placebo or monotherapies in stable COPD |
| [20714376](https://pubmed.ncbi.nlm.nih.gov/20714376/) | 2010 | Review | Int J Chron Obstruct Pulmon Dis | Efficacy and safety of nebulized formoterol in COPD |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Review | Basic Clin Pharmacol Toxicol | Finnish guidelines on diagnosis and pharmacotherapy of stable COPD |
| [27143870](https://pubmed.ncbi.nlm.nih.gov/27143870/) | 2016 | Review | Int J Chron Obstruct Pulmon Dis | Scientific rationale for LAMA + LABA dual therapy in COPD |
| [28740376](https://pubmed.ncbi.nlm.nih.gov/28740376/) | 2017 | RCT | Int J Chron Obstruct Pulmon Dis | Fluticasone propionate/formoterol for COPD management |
| [27916620](https://pubmed.ncbi.nlm.nih.gov/27916620/) | 2017 | Trial (PINNACLE-1/2) | Chest | Glycopyrrolate/formoterol MDI improved efficacy and safety in COPD |
| [25835160](https://pubmed.ncbi.nlm.nih.gov/25835160/) | 2015 | Clinical study | Am J Respir Crit Care Med | Budesonide/formoterol for bronchiolitis obliterans after stem cell transplantation |
| [41654451](https://pubmed.ncbi.nlm.nih.gov/41654451/) | 2026 | Cohort | Clin Ther | Real-world pharmacovigilance safety analysis of budesonide/formoterol |
| [12236842](https://pubmed.ncbi.nlm.nih.gov/12236842/) | 2002 | Review | Br J Clin Pharmacol | Antagonism of long-acting beta2-agonism and effects on inhaled corticosteroid action |
| [25878387](https://pubmed.ncbi.nlm.nih.gov/25878387/) | 2015 | Case report | Indian J Pharmacol | Acebrophylline-induced angioedema in a patient taking budesonide/formoterol |

For the obstructive lung disease prediction, key RCTs include ETHOS (PMID 33252985 and 32579807, NEJM 2020) and KRONOS (PMID 30232048, Lancet Respir Med 2018), which support triple therapy containing formoterol in COPD.

---

## Singapore Market Information

There are 18 valid single-ingredient registrations. Approved-indication text is not available for any of them. The main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13761P | Atimos Pressurised Inhalation Solution 12mcg/inhalation | Metered aerosol | Not stated |
| SIN16056P | DuoResp Spiromax Dry Powder for Inhalation 160/4.5 mcg | Metered powder | Not stated |
| SIN11681P | Symbicort Turbuhaler 160/4.5 mcg/dose | Metered powder | Not stated |
| SIN13932P | Foster Pressurised Inhalation Solution 100/6 mcg per actuation | Metered aerosol | Not stated |
| SIN15924P | Trimbow Pressurised Inhalation Solution 100/6/12.5 μg per actuation | Metered aerosol | Not stated |

---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these are graph-derived associations, not label text): hypertension and hypertensive disorders, long QT syndrome (including the familial form), epilepsy, liver disease, gallbladder disease, measles, herpes simplex virus keratitis, and a group of pituitary and growth hormone deficiency or hypogonadotropic hypogonadism conditions.

**Drug Interactions:** The interaction screening returned 100 interactions in total. Examples from the 20 shown:
- **Moderate:** antidiabetic drugs (acarbose, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, empagliflozin, albiglutide, dulaglutide), QT-prolonging agents (cisapride, clarithromycin, dolasetron), sympathomimetics (ephedrine, isometheptene, diethylpropion), and famotidine.
- **Minor:** corticosteroids (beclomethasone, betamethasone, budesonide, dexamethasone).

Please refer to the package insert for warnings and contraindications. Guardrails from the evidence review:
- Do not use formoterol as LABA monotherapy in asthma; pair it with an inhaled corticosteroid.
- Monitor ICS-related pneumonia risk in COPD.
- Monitor cardiovascular and QT-related safety.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bronchitis (chronic bronchitis within COPD) has multiple completed Phase 3 trials and meta-analyses supporting formoterol-containing therapy, and formoterol is already marketed in Singapore in 18 products. However, the evidence comes mostly from combination products, and the indication largely overlaps with existing emphysema and asthma use, so this is more a confirmation than a true repurposing. The respiratory malformation, Rienhoff syndrome, atopic eczema, asthma susceptibility and rare emphysema predictions have no credible support and should remain on Hold.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (a blocking data gap for formal safety screening)
- Mechanism of action data (via DrugBank)
- Formoterol-specific efficacy data separated from combination partners
- Confirmation of the approved indication wording for the Singapore licences
- A monitoring plan for patients with cardiovascular disease, QT prolongation risk, diabetes or epilepsy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

