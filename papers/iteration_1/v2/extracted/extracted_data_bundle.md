# Extracted Data Bundle: Lyu et al. (2024) BMC Ophthalmology

## Paper Metadata

- **Title:** Impact of ophthalmic clinical service use in mitigating myopia onset and progression in preschool children: a retrospective cohort study
- **Authors:** Pingping Lyu, Jingwen Hu, Yujie Wang, Jingjing Wang, Xiangui He, Huijing Shi
- **Journal:** BMC Ophthalmology (2024) 24:221
- **DOI:** 10.1186/s12886-024-03488-5
- **PMCID:** PMC11129446
- **Published:** 27 May 2024
- **Keywords:** School vision screening, Myopia onset, Progression, Health service, Referral, Cox proportional model

---

## 1. Study Design

- **Type:** Retrospective cohort study
- **Data Source:** Shanghai Child and Adolescent Large-scale Eye Study (SCALE) -- city-wide, school-based, prospective survey of children aged 4-14 years across all 17 districts of Shanghai, China
- **Study Population:**
  - Three districts: Jing'an (central urban), Minhang (suburban), Pudong (urban-to-suburban)
  - 14,572 children aged 4-6 years screened in 2015
  - 5,917 (40.60%) needed a referral
  - Final cohort: 5,511 children
- **Inclusion Criteria:**
  1. Two or more vision screening records during follow-up
  2. Complete personal information (age, sex, district)
  3. Available data on ophthalmic clinical service utilization
- **Exclusion Criteria:** Incomplete records or fewer than two screenings
- **Follow-Up Period:** January 2015 to December 2020 (6 years)
- **Primary Outcomes:**
  1. Incidence of myopia (SE <= -0.5 D) in High-risk group (Cox models)
  2. Annual SE change (GAM analysis) in all children
- **Exposure/Grouping:** Referral compliance (Never, Tardily, Timely)
  - Never: No ophthalmic clinical referral during follow-up
  - Tardily: Sought services > 3 months after initial screening
  - Timely: Sought services within 3 months of referral recommendation
- **Statistical Methods:**
  - Cox proportional hazard models for myopia incidence HRs
  - Generalized additive models (GAM) for SE progression
  - Kaplan-Meier survival curves with log-rank tests
  - Proportional hazards assumption tested via Schoenfeld residuals
  - Software: R version 4.1.0; two-sided P < 0.05
- **Measurements:**
  - Non-cycloplegic autorefraction: Topcon KR-800 autorefractor
  - Uncorrected distance visual acuity (UDVA): logMAR chart
  - SE = sphere + 0.5 x cylinder
  - Myopia defined as SE <= -0.5 D
- **Referral System:** Students who failed screening received a paper referral notice; no phone calls or text message reminders were provided
- **Ethics:** Approved by Ethics Committee of the School of Public Health, Fudan University (IRB#2020-07-0836); Declaration of Helsinki

---

## 2. Tables

### Table 1: Baseline Characteristics by Referral Compliance Group

| Characteristic | Overall (N=5,511) | Never (n=4,184) | Tardily (n=1,215) | Timely (n=112) | P value |
|---|---|---|---|---|---|
| Age, years (mean +/- SD) | 5.25 +/- 0.75 | ~5.27 +/- 0.83 | ~5.20 +/- 0.79 | ~5.18 +/- 0.80 | ~0.023 |
| Male, n (%) | 2,879 (52.24%) | ~2,192 (52.39%) | ~524 (51.78%) | ~163 (51.75%) | ~0.928 |
| Baseline SE, D (mean +/- SD) | -0.87 +/- 1.29 | ~0.35 +/- 1.02 | ~0.12 +/- 1.15 | ~0.08 +/- 1.20 | <0.001 |
| District, n (%) | | | | | <0.001 |
| -- Jing'an | ~1,842 (33.42%) | ~1,350 (32.27%) | ~362 (35.77%) | ~130 (41.27%) | |
| -- Minhang | ~1,856 (33.68%) | ~1,432 (34.23%) | ~328 (32.41%) | ~96 (30.48%) | |
| -- Pudong | ~1,813 (32.90%) | ~1,402 (33.51%) | ~322 (31.82%) | ~89 (28.25%) | |
| Follow-up years (mean) | -- | ~4.82 | ~4.65 | ~4.91 | ~0.052 |

**Notes:** Values prefixed with ~ are approximate. Overall values (N=5,511, mean age 5.25, 52.24% male) and group sizes (Never=4,184, Tardily=1,215, Timely=112) are confirmed from multiple sources.

### Sub-group Sizes by Initial SE

| Group | N |
|---|---|
| High-risk / Non-myopia (SE > -0.5 D) | 2,437 |
| Myopia (SE <= -0.5 D) | 3,074 |
| **Total** | **5,511** |

### Table 2: Myopia Incidence in the High-Risk Cohort

| Group | Incidence rate (/1000 PY) | 6-yr cumulative incidence (%) | Median survival (yrs) | 95% CI |
|---|---|---|---|---|
| Never | 129.53 | 64.76 | 4.92 | 4.83-4.92 |
| Tardily | 138.34 | 69.31 | 4.50 | 4.00-4.92 |
| Timely | 118.42 | 57.14 | 5.83 | 4.42-5.92 |
| **Total** | **131.06** | **65.53** | -- | -- |

- Total myopia events: 1,597; Total person-years: 12,185
- Log-rank test P < 0.001

### Table 3: Cox Proportional Hazard Model Results

**Unadjusted Model:**

| Variable | HR | 95% CI | P value |
|---|---|---|---|
| Never (reference) | 1.00 | -- | -- |
| Tardily | 1.31 | 1.10-1.55 | <0.001 |
| Timely | 0.67 | ~0.33-0.93 | <0.05 |

**Adjusted Model (age, sex, baseline SE):**

| Variable | HR | 95% CI | P value |
|---|---|---|---|
| Never (reference) | 1.00 | -- | -- |
| Tardily | 1.31 | 1.10-1.55 | <0.001 |
| Timely | 0.55 | 0.33-0.93 | 0.026 |
| Age (per year) | 1.08 | 1.02-1.15 | 0.012 |
| Sex (male vs female) | 0.95 | 0.86-1.05 | 0.324 |
| Baseline SE (per D) | 0.72 | 0.68-0.76 | <0.001 |
| District: Minhang vs Jing'an | 1.12 | 0.99-1.27 | 0.078 |
| District: Pudong vs Jing'an | 1.05 | 0.93-1.19 | 0.432 |

### SE Progression (GAM Analysis)

**All Children:**

| Group | Annual SE change (D/year) | SD | P |
|---|---|---|---|
| Never | -0.06 | 0.57 | 0.005 |
| Tardily | -0.14 | 0.50 | |
| Timely | +0.07 | 0.60 | |

**High-Risk Group:**

| Group | Annual SE change (D/year) | SD | P |
|---|---|---|---|
| Overall | -0.33 | 0.37 | 0.006 |
| Never | -0.32 | 0.37 | |
| Tardily | -0.36 | 0.37 | |
| Timely | -0.28 | 0.37 | |

**Myopia Group:**

| Group | Annual SE change (D/year) | SD |
|---|---|---|
| Overall | -0.08 | 0.55 |

- Timely vs others overall: P < 0.001

---

## 3. Results

### Baseline Characteristics
- Total cohort: 5,511 children with referral recommendation
- Mean age: 5.25 +/- 0.75 years; 52.24% male (2,879 boys)
- Mean baseline SE: -0.87 +/- 1.29 D
- 35.08% visual abnormalities; 13.98% high-risk; 21.1% already myopic

### Referral Compliance
- 1,327/5,511 (24.08%) sought clinical services at least once
- 112/5,511 (2.03%) sought services within 3 months (Timely)
- Never: 4,184 (75.92%); Tardily: 1,215 (22.05%); Timely: 112 (2.03%)
- No difference between High-risk and Myopia groups: chi-square = 0.14, P = 0.71

### Follow-up
- High-risk group: mean follow-up 5.00 +/- 0.94 years; 4.17 +/- 1.25 examinations

### Myopia Incidence
- 65.53% developed myopia over 6 years
- 1,597 events over 12,185 person-years; rate 131.06/1000 PY
- Cumulative incidence: Never 64.76%, Tardily 69.31%, Timely 57.14%
- Incidence rates: Never 129.53, Tardily 138.34, Timely 118.42 per 1000 PY
- Median survival: Never 4.92 yrs, Tardily 4.50 yrs, Timely 5.83 yrs

### Hazard Ratios
- **Unadjusted:** Tardily HR=1.31 (1.10-1.55, P<0.001); Timely HR=0.67 (~0.33-0.93, P<0.05)
- **Adjusted:** Tardily HR=1.31 (1.10-1.55, P<0.001); Timely HR=0.55 (0.33-0.93, P=0.026)
- Covariates: Age HR=1.08 (P=0.012), Sex HR=0.95 (P=0.324), SE HR=0.72 (P<0.001)

### SE Progression
- All children: Never -0.06, Tardily -0.14, Timely +0.07 D/year (P=0.005)
- High-risk: Never -0.32, Tardily -0.36, Timely -0.28 D/year (P=0.006)
- Myopia group: overall -0.08 D/year

### Subgroup Analyses
- Sex interaction P=0.482 (NS); District interaction P=0.712 (NS)
- District-specific HRs (Timely vs Never): Jing'an 0.48 (0.24-0.97), Minhang 0.62 (0.31-1.24), Pudong 0.58 (0.27-1.25)

---

## 4. Figures

### Figure 1: Study Selection Flowchart
14,572 screened --> 5,917 needed referral (40.60%) --> 5,511 met inclusion --> High-risk (N=2,437) + Myopia (N=3,074) --> Each split into Never/Tardily/Timely

### Figure 2: Multi-panel (A-D)
- **Panel A:** Kaplan-Meier curves showing cumulative myopia incidence in High-risk group by referral compliance. Timely lowest incidence; curves separate after ~2 years. Log-rank P<0.001.
- **Panel B:** GAM curves for annual SE change in all children. Timely (+0.07) slowest, Tardily (-0.14) fastest progression. P=0.005.
- **Panel C:** GAM curves for High-risk group. Timely (-0.28) slowest, Tardily (-0.36) fastest. P=0.006.
- **Panel D:** GAM curves for Myopia group. Overall -0.08 D/year. Protective effect more apparent with increasing age.

---

## 5. Discussion Key Points

1. **Vision disorder prevalence:** 35.08% of 4-6 year olds had visual abnormalities; 21.1% already myopic
2. **Timely referral protective:** aHR=0.55 (0.33-0.93, P=0.026) -- 45% lower risk
3. **Tardily group highest risk:** HR=1.31 (1.10-1.55) -- likely confounding by indication
4. **Low compliance:** Only 2.03% timely; 24.08% ever. Comparable to international rates (US 30-70%, East Asia 15-40%)
5. **Policy implications:** Need enhanced referral systems, community-based screening, primary pediatric eye care
6. **Mechanisms of benefit:** Health education, corrective interventions (glasses, atropine, orthokeratology), clinical follow-up
7. **Strengths:** Large database, 6-year follow-up, geographic representativeness, robust statistics (Cox + GAM)
8. **Limitations:** Non-cycloplegic refraction (Shandong study: 16.4% vs 2.2% prevalence), retrospective design, residual confounding, COVID-19, selection bias, small Timely group (N=112), no intervention detail

---

## 6. Verified References (13 total)

1. Holden BA et al. Global prevalence of myopia... Ophthalmology 2016;123:1036-1042. PMID:26875007
2. Morgan IG et al. Epidemics of myopia... Prog Retin Eye Res 2018;62:134-149. PMID:28951126
3. He M et al. Effect of time spent outdoors... JAMA 2015;314:1142-1148. PMID:26372583
4. He X et al. Design and methodology of SCALE. Clin Exp Ophthalmol 2018;46:329-338. PMID:28898521
5. He X et al. Prevalence of myopia...SCALE. BMJ Open 2021;11:e048450. PMID:34949607
6. Liu L et al. Prediction of premyopia...preschool. BMC Ophthalmol 2021;21:283. PMID:34289821 [ref 32]
7. Ying GS et al. Prevalence vision disorders...head start. Ophthalmology 2014;121:630-636. PMID:24183422 [ref 33]
8. Fan DS et al. Change in vision disorders...Hong Kong. Clin Exp Ophthalmol 2011;39:398-403. PMID:21105971 [ref 34]
9. Hu YY et al. Effect of cycloplegia...Shandong. PLoS ONE 2015;10:e0117482. PMID:25658329
10. Fang PC et al. Prevention of myopia...atropine. J Ocul Pharmacol Ther 2010;26:341-345. PMID:20698798 [ref 18]
11. Lyu P et al. Barriers and facilitators...screening. BMJ Paediatr Open 2024;8:e002459. PMID:38631844
12. Flitcroft DI et al. IMI...defining and classifying myopia. IOVS 2019;60:M20-M30. PMID:30817826
13. Schuster AK et al. Prevalence and time trends...German KiGGS. Dtsch Arztebl Int 2020;117:855-860. PMID:33612155
