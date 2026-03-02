# Extracted Data Bundle: DR and AMD Association (NHIRD Taiwan)

## Source
- Title: The Association between Diabetic Retinopathy and Macular Degeneration: A Nationwide Population-Based Study
- Journal: Biomedicines 2024, 12(4), 727
- PMCID: PMC11047965 | PMID: 38672083

---

## 1. Study Design

### Type
Retrospective population-based cohort study

### Database
Taiwan National Health Insurance Database (NHIRD), specifically the Longitudinal Health Insurance Database (LHID) 2000. Taiwan's National Health Insurance (NHI) was launched in 1995, covering 23,832,551 residents (~99% of Taiwan's population). The LHID contains data for one million randomly sampled patients. The database exhibits no statistically significant differences in age, sex, or healthcare costs compared to all NHI enrollees.

### Study Period
2000–2013

### Enrollment Period
2000–2006 (new DR diagnoses)

### Diagnostic Coding System
ICD-9-CM (International Classification of Diseases, Ninth Revision, Clinical Modification)
- DR codes: 362.01 (background diabetic retinopathy), 362.02 (proliferative diabetic retinopathy)
- DM code: 250
- AMD codes: 362.50 (senile/unspecified), 362.51 (non-exudative), 362.52 (exudative)

### Participants
- **DR group (study):** N = 3,413
- **Non-DR group (control):** N = 13,652
- **Matching ratio:** 1:4 (matched by age and sex)
- **Total:** 17,065 subjects

### Inclusion Criteria
- Age ≥55 years
- Newly diagnosed with DR (ICD-9-CM 362.01, 362.02) between 2000 and 2006

### Exclusion Criteria
- Prior DR or DM diagnosis (ICD-9-CM 250) before 2000
- History of AMD before the index date (for controls)

### Follow-up
All subjects observed until: diagnosis of AMD, death, or 31 December 2013 (whichever occurred first)

### Primary Outcomes
Development of:
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
- Significance level: p < 0.05

### IRB
Institutional Review Board of Fu Jen Catholic University (FJU-IRB NO: C104014). Patient consent waived (retrospective database study).

### Funding
No external funding received.

---

## 2. Complete Results

### 2.1 Baseline Characteristics (Table 1)

| Variable | DR Group (N=3,413) | Non-DR Group (N=13,652) | p-value |
|----------|-------------------|------------------------|---------|
| Mean age (years) | 67.1 | 66.5 | <0.001 |
| Age distribution | — | — | 0.999 (matched) |
| Sex distribution | — | — | 0.999 (matched) |
| Low income | Significantly higher | Reference | <0.001 |
| Hypertension | Significantly higher | Reference | <0.001 |
| Hyperlipidemia | Significantly higher | Reference | <0.001 |
| CAD | Significantly higher | Reference | <0.001 |
| Stroke | Significantly higher | Reference | <0.001 |
| COPD | Significantly higher | Reference | <0.001 |
| Liver cirrhosis/chronic hepatitis | Significantly higher | Reference | <0.001 |

**Key observations:**
- Age and sex matched (p = 0.999); however mean age was slightly but significantly different (67.1 vs 66.5 years, p < 0.001)
- DR group had significantly higher rates of ALL comorbidities (all p < 0.001)

### 2.2 Overall AMD Incidence and Hazard Ratios (Table 2)

**All types of AMD combined (ICD-9 codes 362.50 + 362.51 + 362.52):**

| Measure | DR Group | Non-DR Group |
|---------|----------|-------------|
| N | 3,413 | 13,652 |
| Incidence rate (per 10,000 PYs) | 16.77 | 5.36 |
| **aHR (95% CI)** | **3.50 (3.10–3.95)** | Reference |

**Stratified findings:**
- AMD incidence increased with age in both groups
- Association stronger in DR group across ALL age categories
- Highest risk in patients aged >85 years
- Both genders had higher rates in DR group; males showed slightly higher risk than females
- Significantly higher HR and aHR in DR group regardless of presence/absence of ANY comorbid condition (hypertension, CAD, hyperlipidemia, stroke, COPD, cirrhosis/chronic hepatitis)

### 2.3 Senile (Unspecified) AMD (Table 3)

**ICD-9 code 362.50:**

| Measure | DR Group | Non-DR Group |
|---------|----------|-------------|
| N | 3,413 | 13,652 |
| Incidence rate (per 10,000 PYs) | 14.65 | 4.78 |
| **aHR (95% CI)** | **3.45 (3.04–3.92)** | Reference |

- Incidence rate markedly higher with aging in DR group, particularly in 65–75 and ≥85 age groups
- DR is a significant predictor of senile AMD, independent of demographic factors and comorbid conditions

### 2.4 Non-Exudative AMD (Table 4)

**ICD-9 code 362.51:**

| Measure | DR Group | Non-DR Group |
|---------|----------|-------------|
| **aHR (95% CI)** | **2.92 (2.08–4.09)** | Reference |

- Male DR patients had higher incidence of non-exudative AMD compared to female DR patients
- Model adjusted for same covariates

### 2.5 Exudative AMD (Table 5)

**ICD-9 code 362.52:**

| Measure | DR Group | Non-DR Group |
|---------|----------|-------------|
| Incidence rate (per 10,000 PYs) | 1.37 | 0.31 |
| **aHR (95% CI)** | **3.92 (2.51–6.14)** | Reference |

- Notably higher incidence rate in DR group
- aHR remained significantly elevated after adjusting for confounders
- Risks influenced by cardiovascular comorbidities (hypertension, hyperlipidemia, CAD)

### 2.6 Kaplan-Meier Analysis

- Significantly higher cumulative incidence of AMD in DR group vs non-DR group
- Log-rank test: p < 0.001
- Cumulative incidence curves diverge progressively over the follow-up period

### 2.7 Summary of All Adjusted Hazard Ratios

| AMD Subtype | aHR | 95% CI | Reference |
|-------------|-----|--------|-----------|
| Overall AMD (362.50+362.51+362.52) | 3.50 | 3.10–3.95 | Non-DR |
| Senile/unspecified (362.50) | 3.45 | 3.04–3.92 | Non-DR |
| Non-exudative (362.51) | 2.92 | 2.08–4.09 | Non-DR |
| Exudative (362.52) | 3.92 | 2.51–6.14 | Non-DR |

### 2.8 Summary of Incidence Rates (per 10,000 person-years)

| AMD Subtype | DR Group | Non-DR Group |
|-------------|----------|-------------|
| Overall AMD | 16.77 | 5.36 |
| Senile/unspecified (362.50) | 14.65 | 4.78 |
| Non-exudative (362.51) | Not extracted (specific rate not found in searches) | Not extracted |
| Exudative (362.52) | 1.37 | 0.31 |

---

## 3. Table Data

### Table 1: Baseline Demographics and Comorbidities
See Section 2.1 above. Note: Exact n (%) values for individual comorbidities and age subgroups were not fully extractable from web sources. The direction and significance of all comparisons are confirmed.

### Table 2: Overall AMD — All Types Combined
See Section 2.2 above. Stratified by: total, age groups, sex, and comorbidity presence/absence.

### Table 3: Senile (Unspecified) AMD (362.50)
See Section 2.3 above. Same stratification structure as Table 2.

### Table 4: Non-Exudative AMD (362.51)
See Section 2.4 above. Same stratification structure.

### Table 5: Exudative AMD (362.52)
See Section 2.5 above. Same stratification structure.

**Note on Tables 2–5 structure:** Each table is stratified by:
- Overall (total cohort)
- Age subgroups (55–64, 65–74, 75–84, ≥85)
- Sex (Male, Female)
- Comorbidities present vs absent (hypertension, hyperlipidemia, CAD, stroke, COPD, liver cirrhosis/chronic hepatitis)

Each row contains: N, events, person-years, incidence rate per 10,000 PYs, HR, 95% CI, aHR, 95% CI.

---

## 4. Figure Descriptions

### Figure 1: Study Flow Chart
Patient selection diagram showing:
- Source: LHID 2000 (1 million randomly sampled patients)
- Selection of patients aged ≥55 with new DR diagnosis (ICD-9 362.01, 362.02) between 2000–2006
- Exclusions: prior DR/DM diagnoses before 2000; prior AMD diagnosis
- Final: DR group (N = 3,413) matched 1:4 with Non-DR controls (N = 13,652)

### Figure 2: Kaplan-Meier Cumulative Incidence — All Types of AMD
Cumulative risk of all types of macular degeneration (ICD-9 codes 362.50, 362.51, 362.52) in the DR group compared to the non-DR group. DR group shows significantly higher cumulative incidence (log-rank test, p < 0.001).

### Figure 3: Kaplan-Meier Cumulative Incidence — Senile (Unspecified) AMD
Cumulative risk of senile (unspecified) AMD (ICD-9 code 362.50) comparing DR vs non-DR groups.

### Figure 4: Kaplan-Meier Cumulative Incidence — Non-Exudative AMD
Cumulative risk of non-exudative AMD (ICD-9 code 362.51) comparing DR vs non-DR groups.

### Figure 5: Kaplan-Meier Cumulative Incidence — Exudative AMD
Cumulative risk of exudative AMD (ICD-9 code 362.52) comparing DR vs non-DR groups.

---

## 5. Extraction Limitations

- Exact n (%) values for individual comorbidities in Table 1 were not fully accessible via web search
- Exact stratified HR/aHR values by age subgroup, sex, and comorbidity presence/absence for Tables 2–5 were not individually extractable
- Non-exudative AMD incidence rates (per 10,000 PYs) for DR and non-DR groups were not specifically found
- Exact unadjusted HR values for all AMD subtypes were not individually extracted (only aHR values confirmed)
- Individual figure image data (axis values, specific time points) not available from web searches
