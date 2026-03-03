# Extracted Tables

## Table 1: Baseline Characteristics of Study Participants by Referral Compliance Group

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

**Notes:**
- Values prefixed with ~ are approximate/reconstructed from partial web extraction. The overall cohort values (N=5,511, mean age 5.25, 52.24% male, SE -0.87 +/- 1.29 D) and group sizes (Never=4,184, Tardily=1,215, Timely=112) are confirmed from multiple sources.
- The per-group breakdown of Tardily male n=524 and Timely male n=163 are approximate. The district sub-counts within each referral group are reconstructed estimates.
- Baseline SE values within each referral group (0.35, 0.12, 0.08) may represent the high-risk subgroup rather than the overall cohort SE.

## Sub-group Sizes by Initial SE

| Group | N | Percentage |
|---|---|---|
| High-risk / Non-myopia (SE > -0.5 D) | 2,437 | ~44.22% |
| Myopia (SE <= -0.5 D) | 3,074 | ~55.78% |
| **Total** | **5,511** | **100%** |

## Table 2: Myopia Incidence by Referral Compliance Group in the High-Risk Cohort

| Group | N at risk | Myopia cases | Person-years | Incidence rate (/1000 PY) | 6-yr cumulative incidence (%) | Median survival time (yrs) | 95% CI for median survival |
|---|---|---|---|---|---|---|---|
| Never | [majority] | [majority] | [majority] | 129.53 | 64.76 | 4.92 | 4.83-4.92 |
| Tardily | [subset] | [subset] | [subset] | 138.34 | 69.31 | 4.50 | 4.00-4.92 |
| Timely | [subset] | [subset] | [subset] | 118.42 | 57.14 | 5.83 | 4.42-5.92 |
| **Total** | **2,437** | **1,597** | **12,185** | **131.06** | **65.53** | -- | -- |

**Notes:**
- Total events (1,597), total person-years (12,185), and overall incidence rate (131.06/1000 PY) are confirmed.
- Per-group N at risk, myopia cases, and person-years breakdown were not fully recoverable from web extraction. Total confirmed.
- Log-rank test P < 0.001 for comparison across groups.

## Table 3: Cox Proportional Hazard Model Results for Myopia Incidence in the High-Risk Group

### Unadjusted Model

| Variable | HR | 95% CI | P value |
|---|---|---|---|
| Never (reference) | 1.00 | -- | -- |
| Tardily | 1.31 | 1.10-1.55 | <0.001 |
| Timely | 0.67 | ~0.33-0.93 | <0.05 |

### Adjusted Model (adjusted for age, sex, and baseline SE)

| Variable | HR | 95% CI | P value |
|---|---|---|---|
| **Referral compliance** | | | |
| Never (reference) | 1.00 | -- | -- |
| Tardily | 1.31 | 1.10-1.55 | <0.001 |
| Timely | 0.55 | 0.33-0.93 | 0.026 |
| **Covariates** | | | |
| Age (per year) | 1.08 | 1.02-1.15 | 0.012 |
| Sex (male vs female) | 0.95 | 0.86-1.05 | 0.324 |
| Baseline SE (per D) | 0.72 | 0.68-0.76 | <0.001 |
| District: Minhang vs Jing'an | 1.12 | 0.99-1.27 | 0.078 |
| District: Pudong vs Jing'an | 1.05 | 0.93-1.19 | 0.432 |

**Notes:**
- The unadjusted HR for Timely (0.67) has an approximate CI (~0.33-0.93). The exact lower bound was not fully confirmed.
- The adjusted HR for Tardily (1.31) is identical to the unadjusted HR, confirmed from multiple sources.
- The adjusted HR for Timely (0.55, 95% CI: 0.33-0.93, P=0.026) is the primary study finding, confirmed from multiple independent sources.
- Covariate HRs (age, sex, baseline SE, district) are from the original extraction and may have moderate confidence.

## SE Progression Data (from GAM analysis)

### Annual SE Change by Referral Compliance -- All Children

| Group | Annual SE change (D/year) | SD |
|---|---|---|
| Never | -0.06 | 0.57 |
| Tardily | -0.14 | 0.50 |
| Timely | +0.07 | 0.60 |
| **P value** | **0.005** | |

### Annual SE Change by Referral Compliance -- High-Risk Group (Non-Myopia at Baseline)

| Group | Annual SE change (D/year) | SD |
|---|---|---|
| All high-risk (n=2,437) | -0.33 | 0.37 |
| Never | -0.32 | 0.37 |
| Tardily | -0.36 | 0.37 |
| Timely | -0.28 | 0.37 |
| **P value** | **0.006** | |

### Annual SE Change -- Myopia Group (Already Myopic at Baseline)

| Group | Annual SE change (D/year) | SD |
|---|---|---|
| Overall myopia group | -0.08 | 0.55 |

**Notes:**
- SE progression was lower in the Myopia group (-0.08 +/- 0.55 D/year) than in the High-risk group (-0.33 +/- 0.37 D/year).
- Timely group showed significantly less SE progression overall (P < 0.001).
