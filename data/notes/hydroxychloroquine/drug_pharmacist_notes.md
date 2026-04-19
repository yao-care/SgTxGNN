# Hydroxychloroquine: From Autoimmune Diseases to Quinquaud's Folliculitis Decalvans

## One-Sentence Summary

Hydroxychloroquine (HCQ) is an established antimalarial and immunomodulatory agent widely used internationally for systemic lupus erythematosus (SLE), rheumatoid arthritis (RA), and malaria prevention, though it is currently not registered in Singapore.
The TxGNN model predicts it may be effective for **Quinquaud's Folliculitis Decalvans** — the most common primary neutrophilic scarring alopecia — with **no registered clinical trials** and **4 publications** supporting this direction.
Critically, the 2025 EADV Task Force on Hair Diseases has already incorporated HCQ as a formal adjuvant treatment option, grounding the prediction in expert clinical consensus.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; internationally used for malaria, SLE, and rheumatoid arthritis |
| Predicted New Indication | Quinquaud's Folliculitis Decalvans |
| TxGNN Prediction Score | 98.66% |
| Evidence Level | L3 (Observational study + Expert Consensus) |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Hydroxychloroquine belongs to the 4-aminoquinoline antimalarial class. Although formal MOA data is not available in this evidence pack, HCQ's anti-inflammatory mechanism is well established in clinical literature: it inhibits endosomal Toll-like receptor (TLR7/9) signalling and lysosomal acidification, thereby disrupting antigen presentation and suppressing downstream production of key inflammatory mediators — particularly IFN-γ, IL-1β, IL-6, and IL-17. These properties make HCQ a broad-spectrum immunomodulator with proven clinical utility across autoimmune and inflammatory conditions.

Quinquaud's folliculitis decalvans (FD) is a chronic, relapsing scarring alopecia driven primarily by neutrophilic infiltration of hair follicles. While *Staphylococcus aureus* colonisation has historically been implicated in its pathogenesis, an emerging body of evidence recognises a subset of patients with "lichen planopilaris-like" FD in which immune dysregulation — characterised by IL-1β/IL-17 axis activation and neutrophil-dominated follicular inflammation — plays the central pathogenic role. This mechanistic overlap with HCQ's TLR-inhibitory and cytokine-suppressive targets provides a direct and biologically plausible rationale for the TxGNN prediction.

The prediction is further supported by real-world clinical data: the 2025 EADV Task Force on Hair Diseases position statement (PMID 40230058) formally endorsed HCQ as an adjuvant treatment option for FD, and a dedicated 5-year retrospective cohort study (PMID 39340420, n=49) demonstrated clinical benefit in patients with immune-predominant FD phenotypes. This suggests the TxGNN model has correctly identified an emerging clinical niche, even in the absence of prospective controlled trial data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40230058](https://pubmed.ncbi.nlm.nih.gov/40230058/) | 2025 | Expert Consensus (EADV Position Statement) | J Eur Acad Dermatol Venereol | EADV Task Force on Hair Diseases formal position statement on FD management; HCQ endorsed as an adjuvant option to control inflammation and prevent further hair loss |
| [39893632](https://pubmed.ncbi.nlm.nih.gov/39893632/) | 2025 | Comprehensive Review | Expert Opin Drug Metab Toxicol | Systematic review of alopecia therapies (PubMed/MEDLINE, Embase, Cochrane, 2015–2024); covers both scarring and non-scarring types, including current FD treatment landscape |
| [39340420](https://pubmed.ncbi.nlm.nih.gov/39340420/) | 2025 | Retrospective Cohort (5-year, n=49) | Clin Exp Dermatol | **Direct evidence:** HCQ as adjuvant therapy for FD; demonstrates clinical benefit particularly in patients with less-active or "lichen planopilaris-like" FD phenotypes, supporting the immune-mediated subtype hypothesis |
| [32030059](https://pubmed.ncbi.nlm.nih.gov/32030059/) | 2019 | Case Report | Int J Trichology | Therapy-recalcitrant FD ultimately controlled with adalimumab; HCQ listed among prior treatment attempts, contextualising its role before biological escalation |

---

## Singapore Market Information

Hydroxychloroquine is currently **not registered in Singapore**. No product authorisations are on record with HSA.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Summary of All Predicted Indications

The TxGNN model identified 10 high-scoring repurposing candidates for Hydroxychloroquine spanning hair disorders and rheumatic diseases. Evidence strength and clinical recommendations vary substantially across predictions:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Key Evidence Basis |
|------|---------|------------|---------------|----------------|--------------------|
| 1 | Quinquaud's Folliculitis Decalvans | 98.66% | L3 | Research Question | EADV 2025 position statement; 5-year retrospective cohort (n=49) |
| 2 | Telogen Effluvium | 98.55% | L5 | **Hold** | 1 indirect case series (COVID-19 sequelae); no mechanistic link to HCQ |
| 3 | Alopecia Antibody Deficiency | 98.53% | L5 | **Hold** | 1 highly indirect case report (SLE+HAE); no direct evidence |
| 4 | Alopecia Mucinosa | 98.47% | L3 | Research Question | 2 case series + 2 case reports with direct HCQ use for follicular mucinosis |
| 5 | Hereditary Hypotrichosis with Recurrent Skin Vesicles | 98.40% | L5 | **Hold** | No literature; genetic aetiology with no immunologic rationale |
| 6 | Alopecia-Intellectual Disability-Hypergonadotropic Hypogonadism Syndrome | 98.37% | L5 | **Hold** | No literature; rare multi-system genetic syndrome |
| 7 | Alopecia Areata | 98.21% | L3 | Research Question | 1 Phase 4 open-label trial (n=16, completed); mixed retrospective data; **NEGATIVE result for alopecia totalis** (PMID 27051848) |
| 8 | RF+ Polyarticular Juvenile Idiopathic Arthritis | 98.04% | L4 | Research Question | 1 indirect case report; high mechanistic plausibility via HCQ's adult RA indication |
| 9 | Juvenile Chronic Polyarthritis | 97.75% | L3 | **✓ Proceed with Guardrails** | Multiple systematic reviews; dedicated paediatric safety data (PMID 33548956); EULAR/ACR-endorsed csDMARD |
| 10 | Rheumatoid Nodulosis | 97.75% | L4 | Research Question | 1 early case series (1993, PMID 8496880) reporting possible HCQ reversal of MTX-induced accelerated nodulosis |

> **Important note:** Rank 9 (Juvenile Chronic Polyarthritis) carries the strongest actionable recommendation ("Proceed with Guardrails"), supported by multiple systematic reviews, paediatric-specific safety data, and guideline endorsement — despite ranking lower by TxGNN score. A separate expedited evaluation for this indication is recommended.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
For the top-ranked indication (Quinquaud's Folliculitis Decalvans), Level 3 evidence exists — including a 2025 EADV expert consensus and a 5-year retrospective cohort study — supporting HCQ as adjuvant therapy in immune-predominant phenotypes. However, the absence of any registered clinical trials, the lack of Singapore product registration, and unresolved formal safety data prevent advancement beyond a structured research question at this stage.

**To proceed, the following is needed:**

- **Regulatory pathway:** Assess HSA special access scheme or expedited registration pathway for HCQ in Singapore, given the complete absence of current market authorisation
- **Formal safety review:** Obtain and parse the original package insert (EMA/FDA) for key warnings and contraindications — particularly mandatory retinal toxicity screening (ophthalmologic monitoring schedule) and QTc prolongation risk
- **MOA data:** Retrieve full mechanism of action from DrugBank API (DB01611) to complete the mechanistic justification
- **Study design:** Develop a protocol for a Phase 2 pilot RCT specifically enrolling patients with immune-predominant ("lichen planopilaris-like") FD phenotypes, with standardised outcome measures (e.g., Folliculitis Decalvans Activity and Severity Index)
- **Parallel fast-track for Rank 9:** Juvenile Chronic Polyarthritis should be evaluated under a separate, expedited review track given EULAR/ACR guideline support and available paediatric safety data

---

> **Disclaimer:** This report is intended for research reference only and does not constitute medical advice. All drug repurposing candidates require rigorous clinical validation before any therapeutic application.