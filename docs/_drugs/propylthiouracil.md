---
layout: default
title: Propylthiouracil
parent: Medium Evidence (L3-L4)
nav_order: 828
evidence_level: L4
indication_count: 10
---

# Propylthiouracil
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Propylthiouracil: From Hyperthyroidism to Resistance to Thyroid Hormone (THRB Mutation)

## One-Sentence Summary

Propylthiouracil (PTU) is an antithyroid drug that lowers thyroid hormone production. The TxGNN model predicts it may be effective for **resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta**, with a very high score (99.66%). However, there are **0 clinical trials** and only **6 publications** (case reports and mouse studies), and the mechanism points the wrong way. This prediction should be put on hold.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperthyroidism (inferred from the drug's mechanism; the Singapore registrations list no indication text) |
| Predicted New Indication | Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in DrugBank for this record. Based on known pharmacology, PTU inhibits thyroid peroxidase and so reduces thyroid hormone synthesis. Its efficacy in hyperthyroidism is well established.

In resistance to thyroid hormone (RTH), the defect is in the thyroid hormone receptor beta, not in hormone production. Lowering hormone levels therefore does not correct the problem. It may also push TSH higher and enlarge the goiter. The published cases support this concern: a Thai patient with a de novo L330S mutation was treated with PTU for suspected thyrotoxicosis, and her goiter became more enlarged (PMID 10724359). The high TxGNN score probably reflects proximity to thyroid-hormone nodes in the knowledge graph rather than a true therapeutic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18561095](https://pubmed.ncbi.nlm.nih.gov/18561095/) | 2009 | Case report (family) | Exp Clin Endocrinol Diabetes | P453A THRB mutation in a Turkish mother and son with RTH-pattern thyroid tests |
| [14684607](https://pubmed.ncbi.nlm.nih.gov/14684607/) | 2004 | Review/Preclinical | Endocrinology | Mutant TR-beta in the heart and its role in tissue resistance to thyroid hormone |
| [22919057](https://pubmed.ncbi.nlm.nih.gov/22919057/) | 2012 | Animal study (mouse) | Endocrinology | Role of TSH in thyroid carcinoma in mice carrying a THRB mutation |
| [12201835](https://pubmed.ncbi.nlm.nih.gov/12201835/) | 2002 | Case report | Clin Endocrinol | M313T THRB mutation: neonatal thyrotoxicosis and maternal infertility in one family |
| [10724359](https://pubmed.ncbi.nlm.nih.gov/10724359/) | 1999 | Case report | Endocr J | De novo L330S mutation in a Thai woman; her goiter enlarged after 9 months of PTU given for presumed thyrotoxicosis |
| [21909131](https://pubmed.ncbi.nlm.nih.gov/21909131/) | 2012 | Animal study (mouse) | Oncogene | Thyroid hormone drives tumor cell proliferation in a follicular thyroid carcinoma mouse model |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN00772P | PROPYLTHIOURACIL TABLETS BP 50 mg | Tablet | PT Actavis Indonesia |
| SIN11695P | PROPYL TABLET 50 mg | Tablet | Sriprasit Pharma Co Ltd |

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction records were retrieved for this drug.

The literature collected for other predicted indications also reports PTU-associated ANCA vasculitis and agranulocytosis (PMID 31917676, 15163328) and neonatal hepatitis after placental transfer (PMID 2090674). These come from case reports and cohorts, not from the safety dataset, and should be checked against the full label.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is limited to case reports and mouse studies (L4). The mechanism is weak and potentially counterproductive, because RTH is a receptor defect and PTU lowers hormone levels. The high TxGNN score likely reflects knowledge-graph proximity.

Among the other ten predictions in this pack, "autoimmune thyroid disease" (rank 5) carries the strongest evidence (L1, Phase 3 trials). It includes Graves' disease, which is probably an existing PTU indication rather than a true repurposing finding. The Phase 3 trials there study thionamides as a class, and the PTU-specific arms are unconfirmed.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text for the two Singapore registrations, and the original indication record
- Mechanism of action data from DrugBank
- For any further pursuit of this indication, an expert assessment of whether lowering thyroid hormone could ever be appropriate in RTH
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

