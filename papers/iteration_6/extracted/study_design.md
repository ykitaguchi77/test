# Study Design Summary

## Study Type
Retrospective matched case-control study

## Setting
Data from a large national health research database that collects health data from a diverse population across the United States. The database includes patients aged 18 years and older recruited within the period of May 2018 to January 2022. Volunteers completed health-related surveys and consented to sharing their electronic health records (EHRs).

## Participants
- **Cases**: All patients with at least one keratoconus (KC) diagnosis in their EHRs (n = 572), identified by standardized medical terminology codes (ICD codes)
- **Controls**: Matched 1:3 with cases based on age ±1 year, ethnicity, and sex (n = 1,716)
- **Total**: 2,288 participants
- **Female-only subanalysis**: 316 KC cases and 948 matched controls (for pregnancy and estrogen-containing medication analyses)

## Primary Outcomes
Association between KC and clinical factors:
- Ocular surface disease (dry eye, allergic/atopic conjunctivitis, eczema — grouped)
- Diabetes (Type I, Type II)
- Sleep apnea
- Obesity
- Smoking history
- Allergic rhinitis
- Pregnancy (female only)
- Estrogen-containing medications (female only)
- Tetracycline usage
- Vitamin C supplementation

## Statistical Analysis
- **Software**: R programming language (R Foundation for Statistical Computing, Vienna, Austria), using Jupyter Notebook
- **Packages**: "oddsratio()" from "epitools" package, "glm()" from "stats" package
- **Univariable ORs**: Each variable compared individually to KC status
- **Multivariable logistic regression**: All variables as covariates to calculate adjusted ORs
- **95% confidence intervals (CIs) and P values** calculated for all analyses

## Covariate Definitions
- **Ocular surface disease**: Grouped category including dry eye, allergic/atopic conjunctivitis, and eczema (due to significant overlap in pathophysiology and strong prior evidence)
- **Smoking**: Combination of survey data and ICD codes (>100 cigarettes lifetime, >5 years smoking, or smoked in last month)

## Ethics
Data were de-identified and made accessible to registered users for research purposes. Available to registered researchers of the database research workbench.
