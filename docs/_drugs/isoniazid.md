---
layout: default
title: Isoniazid
parent: 僅模型預測 (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
---

# Isoniazid
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

# Isoniazid: From Tuberculosis to Conjunctivitis

## One-Sentence Summary

Isoniazid (INH) is a cornerstone first-line antituberculosis drug, widely used for both active tuberculosis treatment and latent tuberculosis infection (LTBI) prophylaxis across the globe.
The TxGNN model predicts it may be effective for **Conjunctivitis**, with **1 clinical trial** and **20 publications** currently identified in support of this direction — though the preponderance of evidence pertains specifically to the tuberculosis-caused subtype of conjunctivitis, not general conjunctivitis.
Given this narrow mechanistic scope and the absence of Singapore regulatory registration, the current evidence supports a **Hold** decision.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Tuberculosis (active disease treatment and latent infection prophylaxis) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory data on file. Based on known pharmacological information, Isoniazid is a prodrug that is activated by the mycobacterial catalase-peroxidase enzyme (KatG). Once activated, it inhibits the InhA and KasA enzymes responsible for mycolic acid biosynthesis — a structural lipid unique to mycobacterial cell walls. This mechanism makes INH highly selective against *Mycobacterium tuberculosis* and closely related mycobacterial species, explaining why it has remained the backbone of anti-TB therapy for over seven decades.

The connection between INH and conjunctivitis is mechanistically coherent but anatomically narrow: it operates through **tuberculous conjunctivitis**, a rare but well-documented form of ocular tuberculosis in which *M. tuberculosis* directly infects conjunctival tissue. In such cases, INH — as the centerpiece of standard anti-TB regimens — would logically confer therapeutic benefit. Historical clinical series from the 1950s–1970s documented direct use of INH in ocular tuberculosis, and modern case reports continue to identify phlyctenular keratoconjunctivitis as a hypersensitivity manifestation of primary TB infection that responds to anti-TB therapy including INH. A 1965 Alaskan cohort study (PMID 14253168) specifically evaluated INH prophylaxis in Eskimo populations with high rates of this TB-associated conjunctivitis, providing the most direct human evidence in this niche indication.

The critical limitation is that **general conjunctivitis** — most commonly caused by adenoviruses, bacteria such as *Haemophilus influenzae* or *Streptococcus pneumoniae*, or allergic mechanisms — lies entirely outside INH's antimicrobial spectrum. The TxGNN model appears to have captured the TB–conjunctivitis disease overlap, which is mechanistically valid but represents an exceedingly rare and highly specific subtype. The high prediction score (99.36%) therefore likely reflects knowledge graph connectivity between tuberculosis and eye disease rather than a genuine broad repurposing opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04094012](https://clinicaltrials.gov/study/NCT04094012) | Phase 3 | Completed | 490 | Pragmatic RCT comparing systemic drug reactions under 3HP vs 1HP regimens for LTBI treatment in Taiwan. Research objective is regimen tolerability, not conjunctivitis as a treatment target. Relevance to conjunctivitis indication is indirect at best (Grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Cohort Study | Am Rev Respir Dis | **Most directly relevant.** INH prophylaxis for phlyctenular keratoconjunctivitis in Alaskan Eskimos with primary tuberculosis — direct human evidence of INH reducing TB-associated conjunctivitis incidence |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Clinical Series | Ann d'Oculistique | Local treatment of ocular tuberculosis with isoniazid — earliest direct application of INH in conjunctival and other ocular TB manifestations |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case Report | Medicine | Pediatric phlyctenular keratoconjunctivitis secondary to primary sinonasal tuberculosis; resolved with INH-containing anti-TB regimen |
| [17133069](https://pubmed.ncbi.nlm.nih.gov/17133069/) | 2006 | Case Report | Cornea | *M. tuberculosis* presenting as chronic red eye; histopathologically confirmed tuberculous conjunctivitis treated with INH-based therapy |
| [26692731](https://pubmed.ncbi.nlm.nih.gov/26692731/) | 2015 | Case Report | Middle East Afr J Ophthalmol | Tuberculous conjunctivitis in an anophthalmic socket in a 27-year-old; successfully treated with standard anti-TB regimen |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Case Series | Oftalmologia | 28 cases of tuberculous keratoconjunctivitis (13 in children with primary TB); all had positive tuberculin skin test and responded to anti-TB treatment |
| [25433746](https://pubmed.ncbi.nlm.nih.gov/25433746/) | 2014 | Case Report | Can J Ophthalmol | Conjunctival phlyctenulosis as the presenting sign of impending clinical tuberculosis — re-emphasises the sentinel role of ocular TB findings |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case Report | Arch Ophthalmol | Primary tuberculosis of the conjunctiva — among the earliest documentation of conjunctival TB as a distinct clinical entity |
| [32674602](https://pubmed.ncbi.nlm.nih.gov/32674602/) | 2020 | Case Report | Clin Pediatrics | Unexpected cause of conjunctivitis in an adolescent — illustrates how atypical/mycobacterial etiologies can mimic common conjunctivitis |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optom Clin | Systemic drugs and ocular side effects; contextualises the drug–eye relationship including conjunctivitis associations with multiple agents |

---

## Singapore Market Information

Isoniazid currently has **no registered products in Singapore**. No license records or approved indication text are available for this drug in the Singapore Health Sciences Authority (HSA) database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction captures a mechanistically coherent but extremely narrow indication — INH targets *M. tuberculosis*, so it is active against tuberculous conjunctivitis (a rare disease subtype) but has no biological plausibility for the vastly more common viral, bacterial, or allergic forms of conjunctivitis. All retrieved evidence is at the case report or historical cohort level (L4), no Singapore regulatory presence exists, and the drug already provides this effect as part of standard anti-TB therapy without requiring a formal new indication label.

**To proceed, the following is needed:**

- **Indication scoping**: Clearly define whether the repurposing target is *tuberculous conjunctivitis specifically* or general conjunctivitis; the former has biological rationale, the latter does not
- **Mechanism of action data**: Complete MOA profile from DrugBank (DrugBank ID: DB00951) to confirm or refute broader immunomodulatory activity that could explain a wider conjunctivitis effect
- **Singapore regulatory safety data**: Obtain TFDA or equivalent package insert to extract contraindications and key warnings before any safety assessment can proceed (currently Blocking data gap)
- **Unmet need assessment**: Epidemiological data on tuberculous conjunctivitis incidence in Singapore to evaluate whether a distinct repurposing label adds value beyond existing anti-TB prescribing practices
- **Expert ophthalmology input**: Consult with infectious disease ophthalmologists to assess whether an INH-specific ocular TB indication would change clinical management compared to standard TB treatment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

