# Extracted Paper Data

**IMPORTANT: This bundle has been anonymized. No paper title, author names, journal name, DOI, or other identifiers are included. Write the draft using ONLY the data below.**

## Study Design

- **Study type**: Retrospective matched case-control study
- **Setting**: Data from a large national health research database that collects health data from a diverse population across the United States. The database includes patients aged 18 years and older recruited within the period of May 2018 to January 2022. Volunteers completed health-related surveys and consented to sharing their electronic health records (EHRs). Data were de-identified and made accessible to registered researchers.
- **Cases**: All patients with at least one keratoconus (KC) diagnosis in their EHRs, identified by standardized medical terminology and ICD codes (n = 572)
- **Controls**: Matched 1:3 with cases based on age ±1 year, ethnicity, and sex (n = 1,716)
- **Total**: 2,288 participants
- **Female-only subanalysis**: 316 KC cases and 948 matched controls (for analyses of pregnancy and estrogen-containing medication)

### Variables Investigated
Clinical factors assessed from medical histories using ICD codes:
- Ocular surface disease (grouped category: dry eye, allergic/atopic conjunctivitis, eczema)
- Diabetes (Type I, Type II)
- Sleep apnea
- Obesity
- Smoking history (combination of survey data and ICD codes; defined as >100 cigarettes lifetime, >5 years smoking, or smoked in last month)
- Allergic rhinitis
- Pregnancy (female only)
- Estrogen-containing medications (female only)
- Tetracycline usage
- Vitamin C supplementation

### Statistical Analysis
- **Software**: R programming language (R Foundation for Statistical Computing, Vienna, Austria), performed on a web-based notebook platform
- **Packages**: "oddsratio()" from "epitools" package, "glm()" from "stats" package
- **Univariable ORs**: Each variable compared individually to KC status
- **Multivariable logistic regression**: All variables included as covariates to calculate adjusted ORs
- **95% confidence intervals (CIs) and P values** calculated for all analyses

---

## Results

### Demographics
The analyzed cohorts included 572 patients with KC and 1,716 patients without KC. The mean ages of participants were 58.7 ± 15.6 years for KC cases and 58.7 ± 15.6 years for controls. In both the KC and control cohorts, 55% of participants were female and 25% were Hispanic. In the KC cohort, 48% of participants were European American, 23% were Black or African American. In the control cohort, 51% were European American and 18% were Black or African American (Table 1).

### Multivariable Analysis
The strongest correlation to KC in the multivariable analysis was ocular surface disease (57.87%; OR = 6.04; 95% CI, 4.77–7.65). Additional variables showing a statistically significant correlation to participants with a diagnosis of KC in comparison to matched controls when accounting for all other tested variables were obesity (44.76%; OR = 1.82; 95% CI, 1.40–2.37), history of estrogen-containing medication (44.30%; OR = 1.77; 95% CI, 1.25–2.51), and tetracycline usage (30.59%; OR = 1.36; 95% CI, 1.03–1.79). In contrast, participants with KC were statistically significantly less likely to have a history of smoking (31.82%; OR = 0.64; 95% CI, 0.51–0.81) in the multivariable analysis.

### Non-Significant Associations
All other variables tested showed a positive correlation with KC but were not statistically significant: sleep apnea (32.52%; OR = 1.34; 95% CI, 1.00–1.80; P = 0.05247); type II diabetes (29.37%; OR = 1.33; 95% CI, 0.99–1.77; P = 0.05884); vitamin C supplementation (19.75%; OR = 1.31; 95% CI, 0.95–1.80; P = 0.09878); pregnancy (23.73%; OR = 1.30; 95% CI, 0.87–1.94; P = 0.2025); allergic rhinitis (33.57%; OR = 1.22; 95% CI, 0.93–1.61; P = 0.1465); and type I diabetes (4.72%; OR = 1.00; 95% CI, 0.52–1.95; P = 0.9923) (Table 2, Fig.).

### Additional Analyses
Univariable analysis results and analyses without grouping the ocular surface disease components are available in appendix tables but were not extractable from the available source.

---

## Tables

### Table 1: Demographics of the Study Populations

| Characteristic | KC (n = 572) | Non-KC (n = 1716) | P |
|---|---|---|---|
| Age, mean ± SD | 58.7 ± 15.6 | 58.7 ± 15.6 | 1.0 |
| **Sex, n (%)** | | | 1.0 |
| Female | 316 (55) | 948 (55) | |
| Male | 246 (43) | 738 (43) | |
| Other | 10 (2) | 30 (2) | |
| **Ethnicity, n (%)** | | | 1.0 |
| Not Hispanic or Latino | 405 (71) | 1215 (71) | |
| Hispanic or Latino | 144 (25) | 432 (25) | |
| Unknown | 23 (4) | 69 (4) | |
| **Race, n (%)** | | | >0.99 |
| White | 272 (48) | 877 (51) | |
| Black or African American | 129 (23) | 315 (18) | |
| Asian | 8 (1) | 42 (2) | |
| Middle Eastern or North African | 6 (1) | 7 (0) | |
| Native Hawaiian or Other Pacific Islander | 1 (0) | 3 (0) | |
| More than one population | 8 (1) | 27 (2) | |
| Unknown | 148 (26) | 445 (26) | |

### Table 2: Multivariable Analysis of Clinical Factors Associated With KC

| Variable | Multivariable OR | 95% CI | P |
|---|---|---|---|
| Ocular surface disease^a | 6.04 | 4.77–7.65 | <0.0001 |
| Obesity | 1.82 | 1.40–2.37 | <0.0001 |
| Estrogen-containing medication | 1.77 | 1.25–2.51 | 0.00139 |
| Tetracycline | 1.36 | 1.03–1.79 | 0.02945 |
| Sleep apnea | 1.34 | 1.00–1.80 | 0.05247 |
| Type II diabetes | 1.33 | 0.99–1.77 | 0.05884 |
| Vitamin C supplementation | 1.31 | 0.95–1.80 | 0.09878 |
| Pregnancy | 1.30 | 0.87–1.94 | 0.2025 |
| Allergic rhinitis | 1.22 | 0.93–1.61 | 0.1465 |
| Type I diabetes | 1.00 | 0.52–1.95 | 0.9923 |
| Smoking | 0.64 | 0.51–0.81 | 0.00163 |

^a Ocular surface disease includes participants with dry eye, allergic or atopic conjunctivitis, or eczema.

---

## Figures

### Figure: Multivariable Odds Ratios of the Association Between Keratoconus and Health History
- **Type**: Forest plot showing odds ratios with 95% confidence intervals
- **Content**: All 11 variables displayed with their multivariable ORs and 95% CIs
- **Key visual features**:
  - Ocular surface disease (OR = 6.04) far to the right of the reference line
  - Obesity (OR = 1.82) and estrogen-containing medication (OR = 1.77) clearly above 1.0
  - Tetracycline (OR = 1.36) modestly above 1.0
  - Smoking (OR = 0.64) is the only variable to the left of the reference line
  - Reference line at OR = 1.0
