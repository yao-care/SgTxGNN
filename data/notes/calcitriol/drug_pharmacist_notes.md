# Calcitriol: From Hypoparathyroidism to Hereditary Hypophosphatemic Rickets

> **Multi-Indication Analysis Report** | Candidate ID: TW-DB00136-multi | Data Cutoff: 2026-04-05

---

## One-Sentence Summary

Calcitriol (1,25-dihydroxyvitamin D₃, DrugBank DB00136) is the biologically active terminal metabolite of the vitamin D activation pathway, globally established for managing hypocalcaemia in hypoparathyroidism and renal osteodystrophy, but currently **not registered in Singapore**.
The TxGNN model identifies **10 predicted indications** spanning genetic rickets syndromes, metabolic bone diseases, and renal tubular disorders — with **Hereditary Hypophosphatemic Rickets** (Rank 7) carrying the strongest actionable evidence: **7 clinical trials** (including a direct Phase 1 calcitriol monotherapy trial and a Phase 4 dosing comparison) and **20 publications** (including 2 Tier-1 clinical guidelines in *The Lancet* and *Calcified Tissue International*).
The highest TxGNN-scored prediction (Rank 1: **Vitamin D Deficiency**, 99.96%) uses an obsolete ontology term with no corresponding trial evidence, but the underlying clinical concept is inherently supported by calcitriol's mechanism of action.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; globally established for hypoparathyroidism, renal osteodystrophy (CKD), and vitamin D-dependent rickets type 1A |
| Predicted New Indication (Top-Ranked) | Vitamin D Deficiency (obsolete ontology term → ICD E55) |
| TxGNN Prediction Score | 99.96% (Rank 1) |
| Evidence Level | L4 (Rank 1: no trials or literature); **L2** (Rank 7 — Hereditary Hypophosphatemic Rickets: strongest actionable evidence) |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Proceed with Guardrails** (Hereditary Hypophosphatemic Rickets, Ranks 7–8) |

---

## Multi-Indication Summary

| Rank | Predicted Disease | TxGNN Score | Evidence Level | Decision |
|------|------------------|-------------|----------------|----------|
| 1 | Vitamin D Deficiency (obsolete term → ICD E55) | 99.96% | L4 | Research Question |
| 2 | Renal Tubular Acidosis | 99.93% | L3 | Research Question |
| 3 | Familial Isolated Hypoparathyroidism (impaired PTH secretion) | 99.81% | L4 | Research Question |
| 4 | Acromesomelic Dysplasia, Campailla-Martinelli type | 99.79% | L5 | Hold |
| 5 | Craniofacial Conodysplasia | 99.78% | L5 | Hold |
| 6 | Dahlberg-Borer-Newcomer Syndrome (HDR/Barakat) | 99.76% | L4 | Research Question |
| **7** | **Hereditary Hypophosphatemic Rickets** | **99.28%** | **L2** | **Proceed with Guardrails** |
| **8** | **Hypophosphatemic Rickets** | **98.08%** | **L2** | **Proceed with Guardrails** |
| 9 | Osteomalacia | 97.68% | L3 | Proceed with Guardrails |
| 10 | Vitamin D-Dependent Rickets | 97.42% | L3 | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Calcitriol is the biologically active form of vitamin D, produced in the proximal convoluted tubule of the kidney via CYP27B1 (1α-hydroxylase) acting on 25-hydroxyvitamin D. It binds the vitamin D receptor (VDR), a nuclear transcription factor expressed in intestinal epithelium, bone osteoblasts, renal tubular cells, and parathyroid gland chief cells. Through VDR activation, calcitriol enhances intestinal calcium absorption (from ~15% to 30–40%), promotes distal renal tubular calcium reabsorption, suppresses PTH synthesis, and enables adequate mineralisation of the osteoid bone matrix — making it a master regulator of calcium-phosphate homeostasis.

The 10 predicted indications cluster around two mechanistically coherent themes. The first is **conditions where endogenous calcitriol synthesis is impaired**: in hereditary hypophosphatemic rickets (particularly X-linked hypophosphataemia, XLH), FGF23 excess from PHEX mutations simultaneously drives renal phosphate wasting and suppresses CYP27B1 activity, creating a state of relative calcitriol deficiency; exogenous calcitriol directly restores VDR signalling and corrects the bone mineralisation deficit. The second theme is **conditions where PTH deficiency reduces CYP27B1 stimulation**: in hypoparathyroid syndromes (familial isolated hypoparathyroidism, HDR/Barakat syndrome), PTH-driven 1α-hydroxylation is lost, and calcitriol substitution functions as a precision enzyme-product replacement therapy.

For the top-ranked indication (Rank 1: "obsolete vitamin D deficiency"), the ontology term is marked deprecated in current biomedical databases, which explains the absence of trial registrations under this label. The clinically equivalent current term — Vitamin D Deficiency (ICD E55) — is an area where calcitriol's role is theoretically complete, as it is the deficient product itself. Re-querying evidence databases under ICD E55 terminology is strongly recommended before drawing conclusions about evidence absence.

---

## Clinical Trial Evidence

*Focus: Hereditary Hypophosphatemic Rickets / Hypophosphatemic Rickets (Ranks 7–8 — highest evidence)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Early Phase 1 | Active, Not Recruiting | 20 | **Direct calcitriol monotherapy for XLH** — dose escalation over 3 months; primary hypothesis: calcitriol alone (without phosphate) will improve serum phosphate levels and skeletal mineralisation in children and adults without increasing kidney calcifications |
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | Unknown | 100 | Compares high vs. low dose active vitamin D (calcitriol/alfacalcidol) combined with neutral phosphate in children with XLH; aims to establish evidence-based weight-dependent dosing for routine clinical practice |
| [NCT04846647](https://clinicaltrials.gov/study/NCT04846647) | N/A (Observational) | Completed | 260 | Study of inappropriate FGF23 hypersecretion in hospitalised hypophosphataemia patients; confirms FGF23's dual role in suppressing renal phosphate reabsorption and inhibiting calcitriol synthesis — mechanistic underpinning for calcitriol supplementation |
| [NCT06046820](https://clinicaltrials.gov/study/NCT06046820) | Phase 3 | Active, Not Recruiting | 27 | ENERGY 3 Study — evaluates INZ-701 in ENPP1 deficiency; contextualises calcitriol's evolving position within the current treatment landscape of hereditary hypophosphataemia |
| [NCT01526304](https://clinicaltrials.gov/study/NCT01526304) | N/A (Cross-sectional) | Unknown | 150 | Cross-sectional study of FGF23, Klotho, and Sclerostin in kidney stone formers; provides background data on phosphate metabolism dysregulation relevant to calcitriol's role |
| [NCT00844740](https://clinicaltrials.gov/study/NCT00844740) | N/A | Withdrawn (n=0) | 0 | Cinacalcet in familial hypophosphatemic rickets — withdrawn; abstract explicitly identifies oral phosphate + 1,25(OH)₂D (calcitriol) as the current standard of care, validating calcitriol's benchmark status |
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | N/A (Diagnostic) | Not Yet Recruiting | 65 | ATP measurement by ³¹P-spectroscopy in phosphate diabetes (XLH); diagnostic study evaluating intracellular phosphate deficit, indirectly supporting rationale for calcitriol + phosphate supplementation |

---

## Literature Evidence

*Priority: Tier-1 guidelines and direct calcitriol treatment studies; selected from Ranks 7–10 evidence pools*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Systematic Review | *The Lancet* | XLH comprehensive review: PHEX mutation → FGF23 excess → renal phosphate wasting + decreased calcitriol synthesis → hypophosphataemic rickets and osteomalacia; first-line conventional treatment confirmed as phosphate + active vitamin D metabolites |
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Clinical Guideline | *Calcified Tissue International* | Current XLH diagnosis and therapy guideline; calcitriol confirmed as a core treatment component; discusses monitoring for hypercalcaemia and nephrocalcinosis |
| [2157942](https://pubmed.ncbi.nlm.nih.gov/2157942/) | 1990 | Clinical Trial (non-RCT) | *Metabolism* | **Direct calcitriol treatment evidence**: complete metabolic correction achieved in VDDR type 1 with physiological calcitriol doses; partial improvement in XLH with supraphysiological doses combined with phosphate |
| [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/) | 1985 | Clinical Trial (non-RCT) | *J Clin Investigation* | **Key historical study**: high-dose calcitriol (mean 68.2 ng/kg/day) induces and maintains healing of XLH-associated osteomalacia; conventional therapy heals rickets but fails to resolve osteomalacia without calcitriol |
| [40565034](https://pubmed.ncbi.nlm.nih.gov/40565034/) | 2025 | Review | *Int J Mol Sci* | Renal and extrarenal calcitriol synthesis regulation; low circulating calcitriol documented in nutritional rickets, osteomalacia, obesity, and preeclampsia; outlines clinical implications |
| [34492747](https://pubmed.ncbi.nlm.nih.gov/34492747/) | 2021 | Systematic Review + Case Series | *J Pediatr Endocrinol Metab* | VDDR1A (CYP27B1 mutations): genotype-phenotype spectrum; calcitriol is the definitive treatment, with complete clinical remission achievable at physiological replacement doses |
| [32204545](https://pubmed.ncbi.nlm.nih.gov/32204545/) | 2020 | Review | *Metabolites* | Vitamin D's protective role in renal tubulopathies; proximal tubule mitochondria identified as primary site of calcitriol production; documents anti-inflammatory and antioxidative functions relevant to tubular acidosis management |
| [7970647](https://pubmed.ncbi.nlm.nih.gov/7970647/) | 1994 | Clinical Study (non-RCT) | *Orvosi Hetilap* | Calcitriol improves osteomalacia complicating distal renal tubular acidosis; case report documenting bone disease progression and calcitriol response over 7 years of follow-up |
| [30454743](https://pubmed.ncbi.nlm.nih.gov/30454743/) | 2019 | Review | *Pediatric Clinics of North America* | Hypophosphatemic rickets: conventional PO₄ + calcitriol treatment reviewed; monitoring protocol for nephrocalcinosis and nephrolithiasis as treatment-emergent complications |
| [29292875](https://pubmed.ncbi.nlm.nih.gov/29292875/) | 2017 | Cohort Study | *Pediatric Endocrinology Reviews* | Spontaneous growth and effect of early calcitriol + phosphate therapy in 127 XLH patients from 49 centres; highlights importance of early initiation and consistent monitoring |

---

## Singapore Market Information

Calcitriol is currently **not registered** in Singapore. No licensed products or approved indication texts are available in the HSA regulatory database.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---|---|---|---|
| — | Not registered | — | No Singapore regulatory data available |

> **International reference**: Calcitriol is registered and commercially available in multiple markets under brand names including **Rocaltrol®** (Roche) in oral capsule form (0.25 µg, 0.5 µg) and intravenous solution for haemodialysis patients. Registration in Singapore would require a full product registration application to the Health Sciences Authority (HSA) under the Therapeutic Products Regulations.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Supplementary note from published literature** (not from Singapore regulatory records; formal review required):
> - **Hypercalcaemia**: The principal dose-limiting toxicity of calcitriol; requires routine monitoring of serum total and ionised calcium, especially during dose escalation
> - **Nephrocalcinosis / Nephrolithiasis**: Particularly relevant in hypophosphatemic rickets treatment contexts; renal ultrasound monitoring recommended every 6–12 months
> - **PTH over-suppression**: Excess calcitriol may cause adynamic bone disease via oversuppression of PTH; monitor intact PTH periodically
> - **Drug interaction consideration**: Thiazide diuretics may potentiate hypercalcaemia risk; corticosteroids may partially antagonise calcitriol effects on intestinal calcium absorption

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (Hereditary Hypophosphatemic Rickets, Ranks 7–8)

**Rationale:**
Calcitriol combined with phosphate supplementation is the established conventional treatment for hereditary hypophosphatemic rickets (particularly XLH), endorsed by multiple Tier-1 clinical guidelines including a 2024 *Lancet* systematic review; an active Phase 1 monotherapy trial (NCT03748966) and a Phase 4 dosing optimisation trial (NCT03820518) both directly evaluate calcitriol in this indication, confirming ongoing clinical relevance even in the era of burosumab.

**To proceed, the following is needed:**

- **[Blocking]** Obtain formal HSA-approved package insert data for Singapore market registration, including approved warnings, contraindications, and product monograph (currently absent — identified as a blocking data gap DG001)
- **[High Priority]** Complete DrugBank MOA documentation query for calcitriol (DB00136) to formally characterise VDR-mediated mechanism for regulatory submissions (data gap DG002)
- **[Evidence Gap]** Re-query clinical trial and literature databases for Rank 1 indication using current ICD E55 terminology ("Vitamin D deficiency") rather than the obsolete ontology term, to accurately capture existing evidence
- **[Regulatory]** Initiate HSA product registration application for calcitriol in Singapore (oral capsule and/or IV formulation); currently no locally registered product
- **[Safety Protocol]** Develop Singapore-specific monitoring protocol: serum calcium and phosphate (monthly during dose titration, then quarterly), intact PTH (every 6 months), renal ultrasound for nephrocalcinosis (every 12 months), 24-hour urinary calcium
- **[Dose Optimisation]** Await completion of NCT03748966 (calcitriol monotherapy, XLH) and NCT03820518 (dose comparison, Phase 4) results before finalising dosing recommendations for Singapore clinical practice

> **Research Priority Note**: Indications at Ranks 4 and 5 (acromesomelic dysplasia, craniofacial conodysplasia) are rated Hold (L5) and should not be advanced without new mechanistic or clinical evidence. Ranks 3 and 6 (familial isolated hypoparathyroidism, Dahlberg-Borer-Newcomer syndrome) represent mechanistically valid but evidence-sparse applications; these merit targeted literature searches under current disease terminology before further evaluation.

---

*This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*