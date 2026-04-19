# Benzbromarone: From Gout / Hyperuricemia to Renal Hypouricemia

## One-Sentence Summary

Benzbromarone is a potent uricosuric agent historically used for the treatment of gout and hyperuricemia, acting primarily by inhibiting URAT1 and other renal urate transporters to promote urinary uric acid excretion.
The TxGNN model predicts it may be relevant in **Renal Hypouricemia (hypouricemia, renal)**,
with **0 clinical trials** and **20 publications** currently supporting this direction — the majority describing benzbromarone's use as a diagnostic pharmacological probe for characterising tubular urate transport defects, rather than as a therapeutic agent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gout / Hyperuricemia (uricosuric agent) |
| Predicted New Indication | Hypouricemia, Renal |
| TxGNN Prediction Score | 99.07% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Benzbromarone is a potent uricosuric benzofuran derivative that works by inhibiting renal urate transporters — primarily **URAT1 (SLC22A12)**, as well as OAT4 and OAT10 — on the apical membrane of proximal renal tubular cells. By blocking these transporters, benzbromarone prevents urate reabsorption, driving urinary uric acid excretion and lowering serum urate levels. This is the established mechanism behind its historical use in gout and chronic hyperuricemia.

**Renal hypouricemia** is a heterogeneous inherited disorder defined by abnormally low serum urate (typically < 2 mg/dL) caused by excessive renal urate excretion, most commonly due to loss-of-function mutations in the gene encoding URAT1 (SLC22A12). The TxGNN model's prediction almost certainly reflects this direct mechanistic intersection: benzbromarone's primary molecular target is the same protein whose functional loss underlies the most prevalent genetic form of renal hypouricemia. In the knowledge graph, benzbromarone and URAT1/SLC22A12 are tightly coupled, and URAT1 dysfunction links directly to the disease node.

In clinical practice, however, the published literature describes benzbromarone not as a **treatment** for renal hypouricemia, but as a **diagnostic pharmacological probe**. The *benzbromarone/pyrazinamide suppression test* is a standard investigational procedure: benzbromarone (which would normally raise urate excretion further) is administered alongside pyrazinamide (which blocks tubular secretion) to map out whether the underlying tubular defect is presecretory reabsorption, postsecretory reabsorption, or enhanced secretion. Multiple case series in the retrieved literature confirm this diagnostic utility. A therapeutic role — for example, modulating excessive urate secretion — has not been established in controlled studies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia for rheumatologists; summarises diagnostic use of benzbromarone in tubular transport characterisation |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Clinical Study | J Am Soc Nephrol | SLC22A12 (URAT1) mutations in 32 Japanese patients; establishes molecular basis of renal hypouricemia Type 1 |
| [14747372](https://pubmed.ncbi.nlm.nih.gov/14747372/) | 2004 | Basic Research | J Am Soc Nephrol | Localisation and function of mouse URAT1; benzbromarone identified as inhibitor used to study transporter kinetics |
| [18670416](https://pubmed.ncbi.nlm.nih.gov/18670416/) | 2008 | Clinical Study | Am J Hypertension | Losartan's uricosuric action via URAT1 inhibition confirmed in hypertensive patients; contextualises URAT1 as pharmacological target |
| [8893184](https://pubmed.ncbi.nlm.nih.gov/8893184/) | 1996 | Case Report | Nephron | Benzbromarone/pyrazinamide test used to analyse urate transport in Fanconi syndrome with marked renal hypouricemia |
| [8863890](https://pubmed.ncbi.nlm.nih.gov/8863890/) | 1996 | Case Report | Acta Paediatrica | Benzbromarone/pyrazinamide test confirms presecretory tubular defect in patient with recurrent exercise-induced acute renal failure and hypouricemia |
| [9144014](https://pubmed.ncbi.nlm.nih.gov/9144014/) | 1997 | Case Report | Internal Medicine | Benzbromarone suppression test increases urate clearance in two patients with renal hypouricemia and nephrolithiasis, consistent with presecretory defect |
| [3380222](https://pubmed.ncbi.nlm.nih.gov/3380222/) | 1988 | Case Report | Nephron | Isolated renal urate transport defect; benzbromarone further elevated urate clearance while pyrazinamide had no effect, suggesting secretory-site abnormality |
| [8302413](https://pubmed.ncbi.nlm.nih.gov/8302413/) | 1993 | Case Report | Nephron | Renal hypouricemia due to enhanced tubular secretion with urolithiasis; benzbromarone/pyrazinamide interaction used to confirm diagnosis |
| [4009341](https://pubmed.ncbi.nlm.nih.gov/4009341/) | 1985 | Case Series | J Pediatrics | Four children with hereditary renal hypouricemia; benzbromarone and pyrazinamide did not affect clearance ratios in most patients, suggesting a secretory mechanism |

---

## Singapore Market Information

Benzbromarone currently has **no registered products** in Singapore (0 authorisations). It is not approved or marketed in the Singapore market.

> **Background note**: Benzbromarone was voluntarily withdrawn from European markets in 2003 following reports of severe fulminant hepatotoxicity. It continues to be available under restricted use in certain Asian markets (notably Japan and Taiwan), where liver function monitoring is mandatory during treatment.

---

## Safety Considerations

- **Hepatotoxicity Risk**: Benzbromarone is associated with severe, potentially fatal fulminant hepatitis. This safety concern directly prompted its European market withdrawal in 2003 and is the primary barrier to broader clinical use. Liver function monitoring (LFTs) is required in any jurisdiction where it remains in use.

> Detailed local product warnings and contraindications are not available for Singapore (no registered product). Please refer to the package insert of the originating market (e.g., Japanese or Taiwanese prescribing information) and relevant regulatory guidance on uricosuric agents for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Benzbromarone is not marketed in Singapore, carries a serious hepatotoxicity risk that led to its removal from multiple markets, and the available literature describes its use in renal hypouricemia as a **diagnostic tool** rather than a therapy — making the case for a novel therapeutic indication currently unsupported by clinical evidence.

**To proceed, the following is needed:**

- **Safety data**: Obtain full prescribing information (warnings, contraindications, hepatotoxicity monitoring protocols) from markets where benzbromarone remains authorised (Japan, Taiwan)
- **MOA clarification**: Retrieve complete DrugBank MOA data (DB12319) to verify URAT1/OAT4/OAT10 inhibition profile and confirm mechanistic basis for TxGNN prediction
- **Therapeutic intent definition**: Clarify whether any proposed use in renal hypouricemia would be diagnostic (probe testing) or therapeutic (modifying disease course or preventing complications such as exercise-induced acute renal failure)
- **Regulatory feasibility**: Assess whether a new drug application is viable in Singapore given the prior European withdrawal, and what additional safety studies would be required
- **Clinical evidence generation**: No interventional trials exist; if a therapeutic hypothesis is established, a prospective proof-of-concept study in patients with renal hypouricemia and complications (e.g., exercise-induced AKI, nephrolithiasis) would be the minimum requirement to advance to L2/L3 evidence