---
layout: default
title: Clavulanic Acid
parent: 僅模型預測 (L5)
nav_order: 234
evidence_level: L5
indication_count: 10
---

# Clavulanic Acid
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

# Clavulanic Acid: From β-Lactamase-Producing Bacterial Infections to Gonococcal Urethritis

## One-Sentence Summary

Clavulanic acid is a β-lactamase inhibitor, commercially used as part of Augmentin (with amoxicillin), designed to overcome antibiotic resistance in β-lactamase-producing bacterial infections.
The TxGNN model ranks **Gonococcal Urethritis** as the most mechanistically supported new indication (Rank 2), backed by **0 registered clinical trials** and **14 publications** — primarily comparative clinical studies from the 1980s.
The highest-scored TxGNN prediction (Rank 1: Ureaplasma urethritis) has been assessed as **mechanistically implausible** and is excluded from further development; this report focuses on Gonococcal Urethritis as the primary actionable candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | β-lactamase-producing bacterial infections (combination therapy component) |
| Predicted New Indication (Primary) | Gonococcal Urethritis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, clavulanic acid is a suicide inhibitor that irreversibly binds to and inactivates β-lactamase enzymes secreted by resistant bacteria. On its own, clavulanic acid has little direct antibacterial activity; its value lies in rescuing β-lactam antibiotics (particularly amoxicillin) that would otherwise be destroyed before reaching their target.

*Neisseria gonorrhoeae*, the causative organism of gonococcal urethritis, can acquire the ability to produce penicillinase (β-lactamase) — these strains are designated penicillinase-producing *N. gonorrhoeae* (PPNG). Amoxicillin alone fails completely against PPNG, but when clavulanic acid inhibits the β-lactamase, amoxicillin's bactericidal activity is restored. Multiple clinical studies conducted in the 1980s (including comparative trials across Malaysia, Nigeria, Zimbabwe, and Singapore) document cure rates of 85–97% in uncomplicated gonococcal urethritis, including PPNG strains, using single-dose Augmentin regimens. The mechanistic logic is therefore internally consistent and clinically demonstrated.

However, a critical caveat applies: since the 1990s, gonorrhoea treatment guidelines have shifted toward ceftriaxone due to the emergence of broader chromosomally mediated resistance that is not overcome by β-lactamase inhibition alone. The historical evidence — while mechanistically sound — predates modern global resistance surveillance. Before any clinical development can proceed, current susceptibility data for local *N. gonorrhoeae* populations must be obtained to determine whether the Augmentin regimen remains effective in contemporary practice.

---

## All Predicted Indications — Summary Table

This is a multi-candidate evaluation covering 10 predicted indications. The mechanistic validity and overall priority for each are summarised below:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Mechanistic Assessment |
|------|---------|-------------|----------------|----------------|------------------------|
| 1 | Ureaplasma urethritis | 99.93% | L4 | ❌ Terminate | Ureaplasma lacks a cell wall — intrinsically resistant to all β-lactams; clavulanic acid has no relevant mechanism |
| 2 | **Gonococcal urethritis** | **99.93%** | **L3** | **Hold (primary candidate)** | ✅ Sound — β-lactamase inhibition restores amoxicillin activity against PPNG; historical RCT-level data |
| 3 | Uterine inflammatory disease | 99.92% | L3 | Hold (secondary candidate) | ✅ Partial — amoxicillin-clavulanate cited in CNGOF postpartum endometritis guidelines; most supporting data from animals |
| 4 | Xanthogranulomatous pyelonephritis | 99.90% | L4 | Hold | ⚠️ Marginal — surgery is primary treatment; antibiotic role is ancillary only |
| 5 | Urogenital tuberculosis | 99.89% | L4 | Hold | ⚠️ Exploratory only — *M. tuberculosis* has BlaC β-lactamase but standard TB therapy is irreplaceable |
| 6 | Abdominal ectopic pregnancy | 99.80% | L5 | ❌ Terminate | No mechanistic basis — surgical/methotrexate condition |
| 7 | Celiac trunk compression syndrome | 99.80% | L5 | ❌ Terminate | No mechanistic basis — anatomical vascular compression |
| 8 | Abdominal cystic lymphangioma | 99.80% | L5 | ❌ Terminate | No mechanistic basis — congenital lymphatic malformation |
| 9 | Lymph node palisaded myofibroblastoma | 99.80% | L5 | ❌ Terminate | No mechanistic basis — rare benign mesenchymal tumour |
| 10 | Disease of uterine broad ligament | 99.79% | L5 | Hold | ⚠️ Conditional — plausible only if infectious aetiology; no supporting data |

---

## Clinical Trial Evidence

### Gonococcal Urethritis (Rank 2 — Primary Candidate)

Currently no related clinical trials registered.

### Uterine Inflammatory Disease (Rank 3 — Secondary Candidate)

No directly relevant clinical trials registered. One trial retrieved (NCT04751500, HYMMN Trial) was assessed as **Grade C — not relevant**: it examines hysteroscopic management of miscarriage retained products and does not involve clavulanic acid or uterine inflammatory disease.

---

## Literature Evidence

### Gonococcal Urethritis (Rank 2 — Primary Candidate)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3533755](https://pubmed.ncbi.nlm.nih.gov/3533755/) | 1986 | Comparative Clinical Study | Genitourinary Medicine | Randomised comparison of cefuroxime axetil vs amoxicillin 3g + clavulanic acid 0.25g (single oral dose + probenecid) in 500 patients with urogenital and rectal gonorrhoea; both arms evaluated including PPNG strains |
| [4007860](https://pubmed.ncbi.nlm.nih.gov/4007860/) | 1985 | Dose-comparison Study | Genitourinary Medicine | Single oral dose Augmentin 3.125g + probenecid 1g cured 97/100 assessable patients with uncomplicated anogenital gonorrhoea; 85% cure in PPNG-infected patients (including one spectinomycin-resistant PPNG) |
| [6365235](https://pubmed.ncbi.nlm.nih.gov/6365235/) | 1984 | Comparative Clinical Trial | British Journal of Venereal Diseases | Oral amoxicillin 3g + clavulanic acid 250mg vs procaine penicillin IM in 121 men with uncomplicated gonococcal urethritis; Augmentin arm showed 90.6% cure vs 73.7% penicillin at 7 days |
| [3721514](https://pubmed.ncbi.nlm.nih.gov/3721514/) | 1986 | Comparative Clinical Trial | Genitourinary Medicine | Three penicillin regimens (including Augmentin 3.25g + probenecid) evaluated in men with uncomplicated gonorrhoea; cure rates reported for both penicillinase-producing and non-producing strains |
| [6428699](https://pubmed.ncbi.nlm.nih.gov/6428699/) | 1984 | Clinical Trial | British Journal of Venereal Diseases | Two-dose Augmentin (amoxicillin 3g + clavulanic acid 250mg, 4 hours apart) in 192 men with acute gonococcal urethritis; 95.9% cure vs 87.4% for kanamycin; effective against PPNG |
| [3004176](https://pubmed.ncbi.nlm.nih.gov/3004176/) | 1985 | Small Clinical Trial | African Journal of Medicine and Medical Sciences | Augmentin assessed in Ibadan, Nigeria, where PPNG constitutes ~80% of circulating strains; tested two formulations (amoxicillin 3g + clavulanic acid 125mg vs 250mg) |
| [6757686](https://pubmed.ncbi.nlm.nih.gov/6757686/) | 1982 | Small Clinical Trial | Medical Journal of Malaysia | Single-dose oral amoxicillin and clavulanic acid for gonococcal urethritis in males; one of the earliest published clinical evaluations |
| [3147528](https://pubmed.ncbi.nlm.nih.gov/3147528/) | 1988 | Clinical Study | Sexually Transmitted Diseases | Comparison of antibiotics available for β-lactamase-producing *N. gonorrhoeae*, including clavulanic acid combinations; reviews effectiveness for urethral, cervical, pharyngeal, and rectal infections |
| [7958383](https://pubmed.ncbi.nlm.nih.gov/7958383/) | 1994 | Open Study | Journal of International Medical Research | Procaine penicillin G + oral clavulanate-potentiated amoxicillin + probenecid in 55 acute gonorrhoea patients; 92.5% of pathogens were penicillinase-producing; discharge resolved in majority |
| [3898395](https://pubmed.ncbi.nlm.nih.gov/3898395/) | 1985 | Clinical Trial | Singapore Medical Journal | Treatment of uncomplicated gonococcal urethritis in males with two doses of Augmentin six hours apart (Singapore cohort) |

### Uterine Inflammatory Disease (Rank 3 — Secondary Candidate)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30890463](https://pubmed.ncbi.nlm.nih.gov/30890463/) | 2019 | Clinical Guideline (CNGOF/SPILF) | Gynécologie Obstétrique Fertilité & Sénologie | French national guideline on postpartum endometritis; amoxicillin-clavulanate cited as first-line antibiotic therapy option; caesarean section identified as primary risk factor |
| [7811001](https://pubmed.ncbi.nlm.nih.gov/7811001/) | 1994 | Animal Study (Murine) | Antimicrobial Agents and Chemotherapy | Murine model of genital infection with *Chlamydia trachomatis*; amoxicillin-clavulanic acid therapy compared to tetracyclines and azithromycin; upper tract inflammatory outcomes documented |
| [36268928](https://pubmed.ncbi.nlm.nih.gov/36268928/) | 2022 | Narrative Review | European Journal of Translational Myology | Antibiotic use in endodontic treatment during pregnancy; discusses amoxicillin-clavulanate use considerations in pregnant women; relevant to safety context for uterine disease population |
| [7857230](https://pubmed.ncbi.nlm.nih.gov/7857230/) | 1995 | Case Report | Australian and New Zealand Journal of Surgery | Chest wall actinomycosis associated with IUD use; pelvic infection confirmed on imaging; treated with prolonged amoxycillin/clavulanic acid after surgical drainage and IUD removal |

---

## Singapore Market Information

Clavulanic acid is **not currently registered as a standalone product** in Singapore (0 active licenses). In clinical practice, clavulanic acid is only available in fixed-dose combination formulations (e.g., amoxicillin/clavulanate = Augmentin), which are registered as separate combination products. A separate regulatory check of amoxicillin/clavulanate combination registrations (e.g., under "Augmentin," "Co-amoxiclav") would be needed to assess market access for any combination-based clinical development.

---

## Safety Considerations

Safety data for clavulanic acid as a standalone agent is not available in this evidence pack. Please refer to the Augmentin package insert for the safety profile of the amoxicillin/clavulanate combination, including:

- Hepatotoxicity risk (elevated liver enzymes, cholestatic jaundice — particularly associated with clavulanate component)
- Hypersensitivity / anaphylaxis risk (penicillin class)
- Gastrointestinal intolerance (nausea, diarrhoea)
- Clostridium difficile-associated diarrhoea

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Gonococcal urethritis (Rank 2) has the strongest mechanistic and historical clinical basis among all 10 predicted indications — the β-lactamase inhibition logic is sound, and multiple clinical studies from the 1980s demonstrate meaningful cure rates including against PPNG strains. However, all supporting evidence predates modern resistance surveillance, no trials are registered in contemporary databases, and current international guidelines recommend ceftriaxone as standard of care. The drug is also not marketed in Singapore, adding regulatory complexity. A "Hold" is appropriate pending resistance data review rather than a full "Terminate."

The top TxGNN-ranked indication (Ureaplasma urethritis) is recommended for **termination** due to fundamental mechanistic incompatibility: Ureaplasma species lack a cell wall and are intrinsically resistant to all β-lactam antibiotics, making clavulanic acid mechanistically irrelevant for this indication.

**To proceed with Gonococcal Urethritis, the following is needed:**

- **Resistance surveillance data**: Current MIC distributions for *N. gonorrhoeae* against amoxicillin-clavulanate in Singapore/Southeast Asia to determine if historical cure rates remain achievable
- **Guideline mapping**: Formal comparison with WHO and Singapore MOH gonorrhoea treatment guidelines to identify a clinical niche (e.g., ceftriaxone-intolerant patients, resource-limited settings)
- **Mechanism of action documentation**: Formal DrugBank API query to complete the MOA data gap (DG002)
- **Safety review**: TFDA/HSA package insert download for clavulanic acid combination products to complete safety data gap (DG001)
- **Regulatory pathway**: Assessment of whether amoxicillin-clavulanate combination products are registered in Singapore; standalone clavulanic acid registration is not applicable
- **Secondary candidate**: Uterine inflammatory disease (Rank 3) warrants a dedicated literature search for human RCT data on amoxicillin-clavulanate in postpartum endometritis before parallel assessment

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

