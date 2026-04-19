# Interferon beta-1a: From Multiple Sclerosis to Jeune Syndrome Situs Inversus

## One-Sentence Summary

Interferon beta-1a (IFN β-1a) is a recombinant biological immunomodulator globally approved for relapsing forms of Multiple Sclerosis (MS), though it holds no current Singapore market registration.
The TxGNN model ranks **Jeune syndrome situs inversus** as its top predicted new indication with a score of **97.47%**; however, this is supported by **0 clinical trials** and **0 publications** specifically addressing this drug–disease combination.
Across all 10 predicted indications — each a rare congenital structural or chromosomal disorder — the uniform evidence level is **L5** (model prediction only), and the recommended decision for every candidate is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; globally known for relapsing-remitting Multiple Sclerosis (RRMS) |
| Predicted New Indication | Jeune syndrome situs inversus |
| TxGNN Prediction Score | 97.47% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Interferon beta-1a is a type I interferon with well-characterised immunomodulatory and antiviral properties. In its approved indication of relapsing-remitting MS, IFN β-1a signals through the IFNAR1/IFNAR2 receptor complex, activating the JAK-STAT pathway to drive expression of hundreds of interferon-stimulated genes (ISGs). The downstream effects include suppression of autoreactive T-cell activation, reduction of pro-inflammatory cytokine production (TNF-α, IL-17), and stabilisation of the blood-brain barrier — collectively reducing relapse frequency and slowing disability accumulation. Formal MOA documentation could not be retrieved from the drug database at the time of this evaluation, and additional source verification is recommended.

Jeune syndrome situs inversus is a rare autosomal-recessive ciliopathy caused by mutations in cilia-related genes (e.g., *IFT80*, *DYNC2H1*, *CEP120*). The hallmark presentation is a severely restricted thoracic cage (asphyxiating thoracic dystrophy) combined with situs inversus (mirror-image positioning of thoracic and abdominal organs). The disease mechanism is rooted in dysfunctional primary cilia during embryonic development — entirely a structural and developmental failure, with no established immune dysregulation or interferon-axis involvement.

**No pharmacological bridge currently exists** between IFN β-1a's immunomodulatory mechanism and the pathophysiology of Jeune syndrome situs inversus. The high TxGNN score (97.47%) almost certainly reflects knowledge graph topology artefacts rather than a biologically actionable relationship. This pattern is consistent across all 10 predicted indications in this Evidence Pack, which span congenital skeletal anomalies, chromosomal deletions, Pierre Robin sequence variants, glycosylation disorders, and low-malignancy gynaecological tumours — none of which has a recognised immunomodulatory treatment axis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Interferon beta-1a in Jeune syndrome situs inversus.

---

## Literature Evidence

Currently no related literature available for Interferon beta-1a in Jeune syndrome situs inversus.

> **Note on Rank 4 literature:** The PubMed query for "disorder of fucoglycosan synthesis" returned 20 publications, but review of each record confirms they concern IFN β-1a in MS, COPD, and COVID-19 — not fucoglycosan synthesis disorders. These are search retrieval artefacts and do not constitute supportive evidence for that indication or any indication in this Evidence Pack.

---

## Singapore Market Information

Interferon beta-1a holds no current registrations with the Health Sciences Authority (HSA) of Singapore as of the data cutoff (2026-04-04). No product licence records were retrieved.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|--------------|-------------|---------------------|
| — | — | — | No HSA registrations on record |

For reference, IFN β-1a products (e.g., Avonex®, Rebif®) are licensed in major markets (USA, EU, Japan) for relapsing forms of MS. A formal HSA registration application would be required before any use in Singapore.

---

## Safety Considerations

Singapore-specific prescribing information, package insert warnings, and formal contraindications were not retrievable for this evaluation. Please refer to the originator package insert (e.g., Avonex® or Rebif® EU/US SmPC) for comprehensive safety information, including:

- Hepatotoxicity and elevated liver enzymes (monitoring of LFTs recommended)
- Depression and suicidal ideation (black box warning in some jurisdictions)
- Flu-like injection-site reactions
- Thyroid dysfunction and autoimmune events
- Embryo-fetal risk (contraindicated in pregnancy in some regulatory frameworks)

No drug–drug interaction data was found in the query database for this submission.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every one of the 10 TxGNN-predicted indications for Interferon beta-1a is rated L5 — model prediction only, with no supporting clinical trials or directly relevant published literature. All predicted target diseases are rare congenital structural, chromosomal, or developmental disorders for which IFN β-1a's immunomodulatory mechanism has no established or plausible therapeutic rationale. Combined with zero Singapore market presence and unresolved blocking safety data gaps, there is no evidence basis to advance any of these candidates at this time.

**To proceed, the following is needed:**

- **Resolve blocking data gap:** Retrieve the originator package insert (HSA, EMA, or FDA SmPC) to obtain complete warnings, contraindications, and special population guidance
- **Obtain MOA documentation:** Query DrugBank API (DB00060) to formally document the mechanism of action and enable rigorous mechanistic plausibility assessment
- **Re-evaluate TxGNN output quality:** The current top-10 predicted indications are uniformly congenital structural disorders with no immunological basis — consider applying disease-category post-filters or re-running prediction with IFN biology–relevant disease subsets (autoimmune, inflammatory, viral) to surface pharmacologically coherent repurposing candidates
- **Singapore regulatory pathway assessment:** If a viable new indication is identified after the above steps, engage HSA's regulatory affairs pathway early (e.g., Product Licence application under the Health Products Act) given current zero-registration status
- **Scientific advisory review:** Before investing additional evidence-gathering resources, a clinical pharmacologist or immunologist review of the TxGNN output for this drug is strongly recommended to triage candidates with genuine mechanistic plausibility

---

*This report is generated for research reference only and does not constitute medical advice. All repurposing candidates require clinical validation before any therapeutic application.*