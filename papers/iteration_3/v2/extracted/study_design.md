# Study Design: DR and AMD Association (Lin et al., Biomedicines 2024)

## Study Type
Retrospective population-based cohort study

## Database
Taiwan National Health Insurance Database (NHIRD), specifically the **Longitudinal Health Insurance Database (LHID) 2000**. The LHID 2000 contains claims data for 1 million randomly sampled patients from the Registry for Beneficiaries of the NHIRD. The database exhibits no statistically significant differences in terms of age, sex, or healthcare costs compared to all NHI enrollees. Taiwan's NHI covers approximately 99% of the population (23,832,551 residents).

## Study Period
2000-2013

## Enrollment Period
2000-2006 (new DR diagnoses)

## Participants
- **DR group (study):** N = 3,413
- **Non-DR group (control):** N = 13,652
- **Matching:** 1:4 by age and sex
- **Total:** 17,065 subjects

## Inclusion Criteria
- Age >=55 years
- Newly diagnosed with DR (ICD-9-CM codes 362.01, 362.02) between 2000-2006

## Exclusion Criteria
- Prior DR or DM diagnosis (ICD-9-CM 250) before 2000
- History of AMD before the index date (controls only)

## ICD-9-CM Codes Used
- **Exposure (DR):** 362.01 (background DR), 362.02 (proliferative DR)
- **DM exclusion:** 250
- **Outcomes (AMD):** 362.50 (senile/unspecified), 362.51 (non-exudative), 362.52 (exudative)

## Primary Outcomes
1. Overall AMD (362.50 + 362.51 + 362.52 combined)
2. Senile (unspecified) AMD (362.50)
3. Non-exudative AMD (362.51)
4. Exudative AMD (362.52)

## Follow-up
All subjects observed until: diagnosis of AMD, death, or 31 December 2013 (whichever first)

## Covariates
Age, sex, low income, hypertension, hyperlipidemia, CAD, stroke, COPD, liver cirrhosis/chronic hepatitis

## Statistical Methods
- Chi-square tests (categorical variables)
- Two-sample t-tests (continuous variables)
- Kaplan-Meier curves (cumulative incidence) with log-rank test
- Cox proportional hazards model (HR and aHR with 95% CI)
- Stratification by age and sex
- Software: SAS 9.4, SPSS 22.0
- Significance: P < 0.05

## Ethics
- IRB: Fu Jen Catholic University (FJU-IRB NO: C104014)
- Patient consent waived (retrospective de-identified database study)
- Funding: None (no external funding)
