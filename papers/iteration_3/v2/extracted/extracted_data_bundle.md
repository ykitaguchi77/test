# Extracted Data Bundle (v2): DR and AMD Association (NHIRD Taiwan)

## Source
- **Title:** The Association between Diabetic Retinopathy and Macular Degeneration: A Nationwide Population-Based Study
- **Journal:** Biomedicines 2024, 12(4), 727
- **DOI:** 10.3390/biomedicines12040727
- **PMCID:** PMC11047965 | **PMID:** 38672083
- **Authors:** Lin H.-T., Zheng C.-M., Tsai C.-H., Chen C.-L., Chou Y.-C., Zheng J.-Q., Lin Y.-F., Lin C.-W., Chen Y.-C., Sun C.-A., et al.
- **License:** CC BY 4.0

---

## 1. Study Design

### Type
Retrospective population-based cohort study

### Database
Taiwan National Health Insurance Database (NHIRD), specifically the **Longitudinal Health Insurance Database (LHID) 2000**. Taiwan's National Health Insurance (NHI) was launched in 1995, covering 23,832,551 residents (~99% of the population). The LHID 2000 contains claims data for one million randomly sampled patients from the Registry for Beneficiaries. The database exhibits no statistically significant differences in age, sex, or healthcare costs compared to all NHI enrollees.

### Study Period
2000-2013

### Enrollment Period
2000-2006 (new DR diagnoses)

### Diagnostic Coding System
ICD-9-CM (International Classification of Diseases, Ninth Revision, Clinical Modification)
- **DR codes:** 362.01 (background DR), 362.02 (proliferative DR)
- **DM code:** 250
- **AMD codes:** 362.50 (senile/unspecified), 362.51 (non-exudative), 362.52 (exudative)

### Participants
- **DR group (study):** N = 3,413
- **Non-DR group (control):** N = 13,652
- **Matching ratio:** 1:4 (matched by age and sex)
- **Total:** 17,065 subjects

### Inclusion Criteria
- Age >=55 years
- Newly diagnosed with DR (ICD-9-CM 362.01, 362.02) between 2000 and 2006

### Exclusion Criteria
- Prior DR or DM diagnosis (ICD-9-CM 250) before 2000
- History of AMD before the index date (for controls)

### Follow-up
All subjects observed until: diagnosis of AMD, death, or 31 December 2013 (whichever occurred first)

### Primary Outcomes
1. Overall AMD (ICD-9 codes 362.50, 362.51, 362.52 combined)
2. Senile (unspecified) AMD (ICD-9 code 362.50)
3. Non-exudative AMD (ICD-9 code 362.51)
4. Exudative AMD (ICD-9 code 362.52)

### Covariates Adjusted
Age, sex, low income, hypertension, hyperlipidemia, coronary artery disease (CAD), stroke, chronic obstructive pulmonary disease (COPD), liver cirrhosis and chronic hepatitis

### Statistical Methods
- Chi-square tests: categorical variables (demographics, comorbidities)
- Two-sample t-tests: continuous variables
- Kaplan-Meier curves: cumulative AMD incidence
- Cox proportional hazards model: hazard ratios (HR) and adjusted hazard ratios (aHR)
- Stratification by age and sex
- Software: SAS 9.4 and SPSS 22.0
- Significance level: P < 0.05

### IRB
Institutional Review Board of Fu Jen Catholic University (FJU-IRB NO: C104014). Patient consent waived (retrospective database study).

### Funding
No external funding received.

---

## 2. Complete Results

### 2.1 Baseline Characteristics (Table 1)

| Variable | DR Group (N=3,413) | Non-DR Group (N=13,652) | P-value |
|----------|-------------------|------------------------|---------|
| Mean age (years) | 67.1 | 66.5 | <0.001 |
| Age distribution | Matched | Matched | 0.999 |
| Sex distribution | Matched | Matched | 0.999 |
| Low income | Significantly higher | Reference | <0.001 |
| Hypertension | Significantly higher | Reference | <0.001 |
| Hyperlipidemia | Significantly higher | Reference | <0.001 |
| CAD | Significantly higher | Reference | <0.001 |
| Stroke | Significantly higher | Reference | <0.001 |
| COPD | Significantly higher | Reference | <0.001 |
| Liver cirrhosis/chronic hepatitis | Significantly higher | Reference | <0.001 |

**Key observations:**
- Age and sex matched (P = 0.999); however mean age was slightly but significantly different (67.1 vs 66.5 years, P < 0.001)
- DR group had significantly higher rates of ALL comorbidities (all P < 0.001)
- Exact n (%) values not available from extraction; directional indicators used per Iter3 guidelines

### 2.2 Overall AMD Incidence and Hazard Ratios (Table 2)

**All types of AMD combined (ICD-9 codes 362.50 + 362.51 + 362.52):**

| Measure | DR Group | Non-DR Group |
|---------|----------|-------------|
| N | 3,413 | 13,652 |
| Incidence rate (per 10,000 PYs) | 16.77 | 5.36 |
| **aHR (95% CI)** | **3.50 (3.10-3.95)** | Reference |

**Stratified findings:**
- AMD incidence increased with age in both groups
- Association stronger in DR group across ALL age categories
- Highest risk in patients aged >85 years
- Both genders had higher rates in DR group; males showed slightly higher risk than females
- Significantly higher HR and aHR in DR group regardless of presence/absence of ANY comorbid condition

### 2.3 Senile (Unspecified) AMD (Table 3)

**ICD-9 code 362.50:**

| Measure | DR Group | Non-DR Group |
|---------|----------|-------------|
| N | 3,413 | 13,652 |
| Incidence rate (per 10,000 PYs) | 14.65 | 4.78 |
| **aHR (95% CI)** | **3.45 (3.04-3.92)** | Reference |

- Incidence rate markedly higher with aging in DR group, particularly in 65-75 and >=85 age groups

### 2.4 Non-Exudative AMD (Table 4)

**ICD-9 code 362.51:**

| Measure | DR Group | Non-DR Group |
|---------|----------|-------------|
| **aHR (95% CI)** | **2.92 (2.08-4.09)** | Reference |

- Male DR patients had higher incidence of non-exudative AMD compared to female DR patients
- Specific incidence rates per 10,000 PYs not extracted for this subtype

### 2.5 Exudative AMD (Table 5)

**ICD-9 code 362.52:**

| Measure | DR Group | Non-DR Group |
|---------|----------|-------------|
| Incidence rate (per 10,000 PYs) | 1.37 | 0.31 |
| **aHR (95% CI)** | **3.92 (2.51-6.14)** | Reference |

- Notably higher incidence rate in DR group
- aHR remained significantly elevated after adjusting for confounders
- Risks influenced by cardiovascular comorbidities (hypertension, hyperlipidemia, CAD)

### 2.6 Kaplan-Meier Analysis

- Significantly higher cumulative incidence of AMD in DR group vs non-DR group
- Log-rank test: P < 0.001
- Cumulative incidence curves diverge progressively over the follow-up period

### 2.7 Summary of All Adjusted Hazard Ratios

| AMD Subtype | aHR | 95% CI |
|-------------|-----|--------|
| Overall AMD (362.50+362.51+362.52) | 3.50 | 3.10-3.95 |
| Senile/unspecified (362.50) | 3.45 | 3.04-3.92 |
| Non-exudative (362.51) | 2.92 | 2.08-4.09 |
| Exudative (362.52) | 3.92 | 2.51-6.14 |

### 2.8 Summary of Incidence Rates (per 10,000 person-years)

| AMD Subtype | DR Group | Non-DR Group |
|-------------|----------|-------------|
| Overall AMD | 16.77 | 5.36 |
| Senile/unspecified (362.50) | 14.65 | 4.78 |
| Non-exudative (362.51) | Not extracted | Not extracted |
| Exudative (362.52) | 1.37 | 0.31 |

---

## 3. Table Data

### Table 1: Baseline Demographics and Comorbidities
See Section 2.1 above. Note: Exact n (%) values for individual comorbidities and age subgroups were not fully extractable from web sources. The direction and significance of all comparisons are confirmed.

### Table 2: Overall AMD -- All Types Combined
See Section 2.2 above. Stratified by: total, age groups, sex, and comorbidity presence/absence.

### Table 3: Senile (Unspecified) AMD (362.50)
See Section 2.3 above. Same stratification structure as Table 2.

### Table 4: Non-Exudative AMD (362.51)
See Section 2.4 above. Same stratification structure.

### Table 5: Exudative AMD (362.52)
See Section 2.5 above. Same stratification structure.

**Note on Tables 2-5 structure:** Each table is stratified by:
- Overall (total cohort)
- Age subgroups (55-64, 65-74, 75-84, >=85)
- Sex (Male, Female)
- Comorbidities present vs absent (hypertension, hyperlipidemia, CAD, stroke, COPD, liver cirrhosis/chronic hepatitis)

Each row contains: N, events, person-years, incidence rate per 10,000 PYs, HR, 95% CI, aHR, 95% CI.

**Note on Unadjusted HRs:** The original tables contain both HR and aHR columns. Only aHR values were extractable. The study reports both unadjusted and adjusted hazard ratios in the original publication.

---

## 4. Figure Descriptions

### Figure 1: Study Flow Chart
Patient selection diagram showing:
- Source: LHID 2000 (1 million randomly sampled patients)
- Selection of patients aged >=55 with new DR diagnosis (ICD-9 362.01, 362.02) between 2000-2006
- Exclusions: prior DR/DM diagnoses before 2000; prior AMD diagnosis
- Final: DR group (N = 3,413) matched 1:4 with Non-DR controls (N = 13,652)

### Figure 2: Kaplan-Meier Cumulative Incidence -- All Types of AMD
Cumulative risk of all types of macular degeneration (ICD-9 codes 362.50, 362.51, 362.52) in the DR group compared to the non-DR group. DR group shows significantly higher cumulative incidence (log-rank test, P < 0.001).

### Figure 3: Kaplan-Meier Cumulative Incidence -- Senile (Unspecified) AMD
Cumulative risk of senile (unspecified) AMD (ICD-9 code 362.50) comparing DR vs non-DR groups.

### Figure 4: Kaplan-Meier Cumulative Incidence -- Non-Exudative AMD
Cumulative risk of non-exudative AMD (ICD-9 code 362.51) comparing DR vs non-DR groups.

### Figure 5: Kaplan-Meier Cumulative Incidence -- Exudative AMD
Cumulative risk of exudative AMD (ICD-9 code 362.52) comparing DR vs non-DR groups.

---

## 5. Discussion Key Points (from original)

- DR is a significant risk factor for overall, senile, exudative, and non-exudative AMD
- Association persists after adjusting for demographic and comorbid conditions
- Shared pathological mechanisms: retinal edema, progressive inflammation, oxidative stress, vascular dysfunction
- Both genetic and non-genetic factors (aging, hyperglycemia, hypertension) disrupt retinal homeostasis
- DR patients had significantly higher AMD incidence regardless of comorbid conditions
- Risks influenced by cardiovascular comorbid conditions (hypertension, hyperlipidemia, CAD)
- Incidence increased with age; strongest in >85 years
- Early detection and treatment of AMD critically important among DR patients

## 6. Limitations (from original, all 5)

1. ICD-9-CM coding inconsistency: only 3 most commonly cited AMD codes selected; may result in coding variability
2. Administrative database coding errors: NHIRD relies on physician ICD-9-CM coding
3. Unmeasured confounders: smoking, BMI, genetic factors, diet, lifestyle variables
4. Lack of clinical details: no visual acuity, OCT, fundus, severity grading, or treatment data
5. Surveillance bias: DR patients may undergo more frequent eye exams, leading to higher AMD detection

## 7. Strengths (from original, all 7)

1. Large sample size: 3,413 DR + 13,652 non-DR controls
2. Population-based design: NHIRD covers ~99% of Taiwanese population
3. Long follow-up: 2000-2013
4. Matched cohort: 1:4 by age and sex
5. LHID representativeness: no significant differences vs all NHI enrollees
6. Qualified physician diagnoses: based on lab, imaging, pathological data
7. Comprehensive covariate adjustment: age, sex, low income, hypertension, hyperlipidemia, CAD, stroke, COPD, liver cirrhosis/chronic hepatitis

---

## 8. Verified Reference List (Top 10)

1. **He et al. (2018)** -- *Diabetes Care* 41(10):2202-2211. Taiwan LHID. DM with DR vs AMD. HR 3.89 nonexudative, 3.42 exudative. PMID: 30061321.
2. **Hahn et al. (2013)** -- *Retina* 33(5):911-919. US Medicare. NPDR: dry AMD HR 1.24, wet AMD HR 1.68; PDR: wet AMD HR 2.15. PMID: 23407352.
3. **Chen et al. (2014)** -- *PLoS One* 9(9):e108196. Meta-analysis. DM-AMD OR 1.05 (cohort). PMID: 25238063.
4. **Kailuan Eye Study (Wang et al., 2022)** -- *Front Public Health* 10:922289. DR risk factor for dry AMD (20.8% vs 16.0%).
5. **Wong et al. (2014)** -- *Lancet Global Health* 2(2):e106-e116. Global AMD burden: 196 million in 2020. PMID: 25104651.
6. **Yau et al. (2012)** -- *Diabetes Care* 35(3):556-564. Global DR prevalence. PMID: 22301125.
7. **Teo et al. (2021)** -- *Ophthalmology* 128(11):1580-1591. Global DR prevalence 22.27%. PMID: 33940045.
8. **Kauppinen et al. (2016)** -- *Cell Mol Life Sci* 73(9):1765-1786. Inflammation in AMD. PMID: 26852158.
9. **Donath & Shoelson (2011)** -- *Nat Rev Immunol* 11(2):98-107. Diabetes as inflammatory disease. PMID: 21233852.
10. **Adamis et al. (1994)** -- *Am J Ophthalmol* 118(4):445-450. VEGF in proliferative DR. PMID: 7943121.

---

## 9. Extraction Limitations (v2)

- Exact n (%) values for Table 1 comorbidities/age subgroups not available (~30% of Table 1 cells captured)
- Non-exudative AMD incidence rates (per 10,000 PYs) not extracted
- Unadjusted HR values not individually extracted (only aHR confirmed)
- Stratified cell values (events, person-years, HR/aHR by age/sex/comorbidity strata) not individually extracted
- Individual figure axis values and number-at-risk data not available
- Full reference list not individually extractable from web (estimated 25-35 total; 15 reconstructed, 10 verified)
- **Improvement over v1:** Added 15 reconstructed references with 10 verified via PubMed; added formatted reference list; identified specific comparator study data (He et al. HR values, Hahn et al. HR values) for quantitative Discussion comparisons
