# Extracted Paper Data

**IMPORTANT: This bundle has been anonymized. No paper title, author names, journal name, DOI, or other identifiers are included. Write the draft using ONLY the data below.**

## Study Design

- **Study type**: Prospective, randomized, placebo-controlled, double-masked trial with crossover design
- **Setting**: A single university hospital eye center
- **Intervention**: Automated eyelid margin debridement using a commercially available micro-sponge device vs. sham treatment
- **Ethics**: Approved by the local ethics committee. Conformed to the Declaration of Helsinki. Trial retrospectively registered in a national clinical trials register.
- **Crossover note**: A crossover design was used as a recruitment aid (all participants eventually received active treatment). Only the pre-crossover data (baseline and 4-week follow-up) were analyzed to avoid carryover effects.

### Participants
- **Inclusion criteria**: Symptomatic blepharitis (at least Grade 2 on the Efron grading scale), age > 18 years, decimal visual acuity > 0.5, blepharitis refractory to eyelid margin care for ≥ 4 weeks, use of lubricating drops
- **Exclusion criteria**: Routine daily contact lens wear, other eyelid/ocular surface diseases, previous ocular surgery, previous treatment with cyclosporine A or steroids, pregnancy, autoimmune diseases (rheumatologic conjunctivitis, Sjögren's syndrome, endocrine orbitopathy), other immunological diseases, acute infections, trachoma, atopic dermatitis, diabetes mellitus, severe systemic diseases, graft-versus-host disease, antibiotics in last 4 weeks
- **Recruitment period**: December 2017 to June 2018
- **Total enrolled**: 42 patients
- **Analyzed**: 20 per group (2 patients lost to follow-up, 1 per arm)

### Interventions
- **Active treatment**: The device was used according to manufacturer's instructions after topical anesthesia. A cleaning head was placed on the device (one per eye), cleaning gel applied, then upper and lower lids of each eye treated for 2 minutes. The practitioner moved along the eyelid margin, removing debris.
- **Sham treatment**: Same temporal/spatial conditions. Cleaning head placed on device, cleaning gel applied, each eye treated for 2 minutes. However, the practitioner moved along the adjacent row of eyelashes on the eyelid skin (NOT along the eyelid margin), so no mechanical cleaning of the eyelid margin occurred. With topical anesthesia and anatomical proximity, patients could not distinguish between active and sham treatment.

### Outcomes
- **Primary**: Change in Ocular Surface Disease Index (OSDI) — quality of life measure for dry eye/blepharitis
- **Secondary**:
  - Efron grading scale (0-4, eyelid margin inflammation severity; assessed by two independent blinded examiners from photographs)
  - Tear break-up time (TBUT) — measured with 2% fluorescein solution, repeated 3× per eye
  - Schirmer's test II — after topical anesthesia (oxybuprocaine 0.4%), test strips on lateral lower lid for 10 minutes

### Randomization and Blinding
- Randomization: 1:1 ratio, generated using R "blockrand" package, allocation concealed electronically
- Blinding: Double-masked. Treatment performed by unmasked ophthalmologists. Diagnostics performed by a blinded doctoral fellow. Efron grading assessed by two independent blinded examiners. All patients blinded to treatment type.

### Sample Size
Exploratory study; no prior effect size estimates available, so formal sample size calculation was not performed.

### Statistical Analysis
- Categorical data: Chi-Square test (expected frequencies > 5) or Fisher's Exact Test (expected frequencies < 5)
- Continuous data: Shapiro-Wilk test for normality
  - Normally distributed (OSDI): paired t-test (within group), unpaired t-test (between groups)
  - Non-normally distributed (Efron, TBUT, Schirmer): Wilcoxon signed-rank test (within group), Mann-Whitney U test (between groups)
- Effect sizes: Cohen's d (normally distributed), Rank-Biserial Correlation (rbc, non-normally distributed)
  - Cohen's d thresholds: 0.2 small, 0.5 medium, 0.8 large
  - rbc thresholds: 0.10 small, 0.30 medium, 0.50 large
- Software: R version 4.3.1 and 4.4.1

---

## Results

### Participant Flow
42 patients enrolled. 2 lost to follow-up (1 per group). Final analysis: 20 per group (Fig. 2).

### Baseline Characteristics (Table 1)

| Characteristic | N | Active group | Sham group |
|---|---|---|---|
| Age at inclusion [years] (Q1/median/Q3) | 42 | 47.2 / 57.7 / 76.1 | 46.8 / 74.1 / 78.5 |
| Female, % (n) | 24 | 52% (11) | 62% (13) |
| Postmenopausal HRT, % (n) | 18 | 33% (7) | 52% (11) |
| Antidepressants, % (n) | 3 | 0% (0) | 14% (3) |
| Oral beta blocker, % (n) | 8 | 19% (4) | 19% (4) |
| Oral contraception | 0 | 0% (0) | 0% (0) |
| Contact lens wear during study, % (n) | 2 | 0% (0) | 10% (2)* |
| Number of medications (Q1/median/Q3) | 42 | 0.0 / 1.0 / 3.0 | 0.0 / 1.0 / 3.0 |
| BCVA OD [logMAR] (Q1/median/Q3) | 42 | -0.1 / -0.1 / 0.1 | -0.1 / 0 / 0.1 |
| BCVA OS [logMAR] (Q1/median/Q3) | 42 | -0.1 / -0.1 / 0 | -0.1 / -0.1 / 0 |
| Nicotine consumption, % (n) | 18 | 38% (8) | 48% (10) |
| Pack years (Q1/median/Q3) | 18 | 2.75 / 11.0 / 16.25 | 1.0 / 9.0 / 14.25 |
| Efron grading (Q1/median/Q3) | 42 | 2.0 / 3.0 / 3.0 | 2.0 / 2.5 / 3.0 |
| OSDI [points] (Q1/median/Q3)** | 42 | 10.4 / 15.6 / 28.7 | 18.8 / 33.3 / 41.7 |
| TBUT [s] (Q1/median/Q3) | 42 | 1.73 / 2.19 / 3.07 | 2.05 / 2.56 / 3.43 |
| Schirmer's test II [mm] (Q1/median/Q3) | 41 | 5.75 / 11.50 / 21.12 | 7.50 / 11.50 / 13.00 |

\* Only sporadic contact lens wearing for exercise reported during the study
\*\* Statistically significant difference between groups (P = 0.020), with higher score in sham group

No other statistically significant baseline differences between groups.

### Treatment Outcomes (Table 2)

| Outcome | Active Group (n=20) | Sham Group (n=20) | Between-group P | Effect size |
|---|---|---|---|---|
| **OSDI** | | | | |
| Mean change (95% CI) | -2.40 (-7.95 to 3.16) | -4.90 (-11.51 to 1.72) | 0.548 | 0.19 (Cohen's d) |
| Median change (IQR) | -2.09 (-7.29/3.12) | -5.21 (-13.54/1.04) | | |
| Within-group P | 0.378 | 0.138 | | |
| **Efron grading** | | | | |
| Mean change (95% CI) | -0.2 (-0.56 to 0.16) | -0.3 (-0.57 to -0.03) | 0.730 | -0.095 (rbc) |
| Median change (IQR) | 0 (-1.0/0) | 0 (-1.0/0) | | |
| Within-group P | 0.276 | 0.041 | | |
| **TBUT [s]** | | | | |
| Mean change (95% CI) | 0.81 (-0.9 to 2.52) | -0.20 (-1.21 to 0.81) | 0.277 | -0.205 (rbc) |
| Median change (IQR) | 0.22 (-0.13/0.76) | -0.01 (-0.55/0.59) | | |
| Within-group P | 0.240 | 0.808 | | |
| **Schirmer [mm]** | | | | |
| Mean change (95% CI) | 0.94 (-1.74 to 3.61) | 0.95 (-1.05 to 2.95) | 0.787 | -0.053 (rbc) |
| Median change (IQR) | 2.00 (-3.63/3.75) | 1.00 (-1.25/2.13) | | |
| Within-group P | 0.717 | 0.397 | | |

Key findings:
- Sham group showed statistically significant decrease in Efron grade (P = 0.041)
- No other within-group changes were statistically significant
- No between-group differences were statistically significant (all P > 0.05)
- All effect sizes were negligible to small

### Safety
- Visual acuity: No significant decrease in either group
- Adverse events:
  - Active group: 3 patients reported eye irritation for a few hours post-treatment; 1 patient had unilateral itching persisting until follow-up (started 1 week post-treatment)
  - Sham group: 2 patients reported eye irritation for a few hours post-treatment; 1 patient had epiphora starting upon treatment

---

## Figures

### Figure 1: Photographic Guide for Treatment Procedure
- **Type**: Procedural photograph
- **Description**: Shows the device cleaning head placement and treatment of eyelid margins

### Figure 2: Patient Flowchart
- **Type**: CONSORT-style flowchart
- **Key data**:
  - Enrolled: 42 patients
  - Randomized: 21 active, 21 sham
  - Lost to follow-up: 1 per group
  - Analyzed: 20 per group
  - Crossover after 4 weeks (not analyzed)
