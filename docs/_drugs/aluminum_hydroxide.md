---
layout: default
title: Aluminum Hydroxide
parent: Low Evidence (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
---

# Aluminum Hydroxide
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

# Aluminum Hydroxide: From Antacid Use to Active Peptic Ulcer Disease

## One-Sentence Summary

Aluminum hydroxide is an acid-neutralizing antacid. Its original indication is not recorded in the source data.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, with **0 registered clinical trials** and **20 publications** supporting this direction.
The literature is mostly older (1949-2022), and the prediction is closer to correcting a label or data gap than to true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in source data (all 14 Singapore registrations have empty indication text; used as an antacid) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L3 (literature only, no registered trials; the pack's L2 is inferred from titles and not confirmed) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 14 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Aluminum hydroxide is a long-established antacid that neutralizes secreted gastric acid and raises intragastric pH. The retrieved literature also shows it inhibits pepsin activity and adsorbs pepsin (PMID 37146, 3929601).

Peptic ulcers are acid- and pepsin-driven, so acid neutralization fits the disease. Reviews and mechanistic studies also describe cytoprotective and ulcer-healing effects of aluminum-containing antacids. These are linked to endogenous prostaglandins and epidermal growth factor (PMID 22950493, 1769429, 2390927).

Peptic ulcer treatment is a classic antacid use. This is therefore mainly a gap in the source data, not a new therapeutic direction. The high TxGNN score is consistent with the established literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scand J Gastroenterol | 12-week double-blind trial in 72 duodenal/prepyloric ulcer patients. Cimetidine healed 67% at 3 weeks; antacid plus anticholinergic healed 50%. The placebo result is not in the retrieved text. |
| [37146](https://pubmed.ncbi.nlm.nih.gov/37146/) | 1979 | Review | Fortschr Med | Antacids work by neutralizing gastric acid and inhibiting pepsin. Dosing 1 and 3 hours after meals is needed for adequate neutralization. |
| [6086186](https://pubmed.ncbi.nlm.nih.gov/6086186/) | 1984 | Review | Clin Gastroenterol | Reviews antacids and anticholinergics in duodenal ulcer treatment. |
| [22950493](https://pubmed.ncbi.nlm.nih.gov/22950493/) | 2013 | Mechanistic review | Curr Pharm Des | Describes cellular and molecular mucosal-protective and ulcer-healing actions of antacids. |
| [1769429](https://pubmed.ncbi.nlm.nih.gov/1769429/) | 1991 | Mechanistic/Clinical | Digestion | Al(OH)3 and Maalox protected against experimentally induced gastric mucosal lesions. The study examines the role of intragastric pH. |
| [2390927](https://pubmed.ncbi.nlm.nih.gov/2390927/) | 1990 | Experimental | Dig Dis Sci | Al(OH)3 enhanced healing of chronic gastroduodenal ulcers in rats. The study examines the roles of prostaglandins and EGF. |
| [2401189](https://pubmed.ncbi.nlm.nih.gov/2401189/) | 1990 | Retrospective study | Drugs Exp Clin Res | 267 children with peptic symptoms, all endoscoped. Compares efficacy of several drug types in acute and relapse treatment. |
| [3018068](https://pubmed.ncbi.nlm.nih.gov/3018068/) | 1986 | Clinical pharmacology | J Clin Gastroenterol | Compares sodium bicarbonate with aluminum-magnesium hydroxide on postprandial gastric acid in duodenal ulcer patients. |
| [9334882](https://pubmed.ncbi.nlm.nih.gov/9334882/) | 1997 | In vitro | Jpn J Pharmacol | Al(OH)3 prevented acid- and pepsin-induced damage in rat gastric epithelial cells. |
| [9305482](https://pubmed.ncbi.nlm.nih.gov/9305482/) | 1997 | Clinical | Aliment Pharmacol Ther | Reports that antacids and H2 blockers had an aggravating effect on *H. pylori* gastritis in duodenal ulcer patients. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN02930P | ALU-TAB TABLET 600 mg | Film-coated tablet | Not stated in registration record |
| SIN03159P | ALUMAG TABLETS | Tablet | Not stated in registration record |
| SIN09499P | ALLUMAG M TABLET | Tablet | Not stated in registration record |
| SIN06592P | AXCEL EVILINE TABLET | Tablet | Not stated in registration record |
| SIN03406P | POLYSILIC III SUSPENSION | Suspension | Not stated in registration record |

Fourteen registrations exist in total; the five above are shown. Registered forms include tablets, suspension and granules.

---

## Safety Considerations

- **Key Warnings (from literature, not package insert)**:
  - Long-term or high-dose use can cause phosphate depletion and bone demineralization or osteomalacia (PMID 6293043, 7431592).
  - The clinical relevance of aluminum absorption in patients with normal renal function is uncertain (PMID 6293043).
- **Drug Interactions**: No interactions were found in the DrugBank query. One small study found no interaction with cimetidine in ulcer patients (PMID 6613216).

The HSA package insert has not been reviewed. Please refer to it for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Acid neutralization is a well-established mechanism, and older controlled studies and reviews support the use of antacids in peptic ulcer disease. However, there are no registered trials, the evidence is old, and package insert safety data are missing.

**To proceed, the following is needed:**
- Download and parse the HSA package insert for warnings and contraindications (blocking for safety screening)
- Retrieve DrugBank mechanism of action data
- Full-text check of the controlled ulcer studies (for example PMID 7034155) to confirm whether L1 or L2 applies
- Fill the empty approved-indication fields in the Singapore registrations
- Safety guardrails for long-term use: phosphate and bone monitoring, and caution in renal impairment

**Other predictions in this pack:** Gastroduodenitis and gastrojejunal ulcer are research questions with indirect, mostly historical evidence. Hiatus hernia is also a research question, supported only by indirect evidence. Peptic ulcer perforation, achlorhydria, pylorospasm, gastric dilatation, Dieulafoy lesion and cascade stomach are on Hold, with no supporting evidence or no plausible mechanism.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

