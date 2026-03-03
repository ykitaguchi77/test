# Study Design Summary

## Study Type
Retrospective cohort study

## Data Source
Shanghai Child and Adolescent Large-scale Eye Study (SCALE) -- a city-wide, school-based, prospective survey of children and adolescents aged 4-14 years from all 17 districts and counties of Shanghai, China.

## Population
- Three districts: Jing'an (central urban), Minhang (suburban), Pudong (urban-to-suburban)
- Initially 14,572 children aged 4-6 years screened in 2015
- 5,917 (40.60%) needed a referral
- Final cohort: 5,511 children

## Inclusion Criteria
1. Two or more vision screening records during follow-up
2. Complete personal information (age, sex, district)
3. Available data on ophthalmic clinical service utilization

## Exclusion Criteria
- Incomplete records
- Fewer than two screenings

## Follow-Up Period
January 2015 to December 2020 (6 years)

## Primary Outcomes
1. Incidence of myopia (defined as SE <= -0.5 D) in the High-risk group
2. Annual spherical equivalent (SE) change (progression) in all children

## Exposure/Grouping
Children categorized by referral compliance:
- Never: No ophthalmic clinical referral during follow-up
- Tardily: Sought services > 3 months after initial screening
- Timely: Sought services within 3 months of referral recommendation

## Key Statistical Methods
- Cox proportional hazard models for myopia incidence HRs
- Generalized additive models (GAM) for SE progression
- Kaplan-Meier survival curves with log-rank tests
- Software: R version 4.1.0; P < 0.05 two-sided

## Measurements
- Non-cycloplegic autorefraction: Topcon KR-800 autorefractor
- Uncorrected distance visual acuity (UDVA): logMAR chart
- SE = sphere + 0.5 x cylinder

## Ethics
Approved by the Ethics Committee of the School of Public Health, Fudan University (IRB#2020-07-0836). Conformed to the Declaration of Helsinki.
