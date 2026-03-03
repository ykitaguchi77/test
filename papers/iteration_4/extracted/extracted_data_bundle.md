# Extracted Paper Data

**IMPORTANT: This bundle has been anonymized. No paper title, author names, journal name, DOI, or other identifiers are included. Write the draft using ONLY the data below.**

## Study Design

- **Study type:** Cross-sectional study
- **Setting:** Department of Ophthalmology at a tertiary hospital in a European center
- **Ethics:** Approved by local ethics committee (adhered to Declaration of Helsinki); informed consent waived due to retrospective character
- **Participants:** 66 eyes of patients with choroidal neovascularization (CNV) secondary to neovascular age-related macular degeneration (nAMD)
  - Mean age: 83.4 years
  - Average number of prior intravitreal anti-VEGF injections: 12.58
- **Treatment regimen:** Intravitreal anti-VEGF injections applied without paracentesis, according to pro-re-nata (PRN / as-needed) regimen
- **Primary outcomes:**
  - Retinal nerve fiber layer thickness (RNFL)
  - Bruch's membrane opening minimum rim width (MRW)
- **Measurement instrument:** Optical coherence tomography (Spectralis OCT, Heidelberg Engineering) analyzed with Heyex 2 software, with age-matched reference values; manual corrections of RNFL segmentation and Bruch's membrane opening performed by a trained physician when necessary
- **Sectors analyzed:** Global, nasal, nasal-superior, nasal-inferior, temporal, temporal-superior, temporal-inferior
- **Statistical analysis:** Linear regression models performed in R (version 4.0.3)
- **Exclusion criteria:**
  - Uncontrolled elevated IOP > 21 mmHg prior to injections
  - History of ischemic optic atrophy
  - Diagnosis of glaucoma prior to anti-VEGF treatment
  - Clinically significant epiretinal membrane
  - High myopia
- **Limitations noted:** Lack of axial eye length measurements (mitigated by excluding high myopia patients)

## Results

### Sample Characteristics
- N = 66 eyes
- Mean age: 83.4 years
- Mean number of prior intravitreal injections: 12.58

### Primary Finding: RNFL
- Mean global RNFL: 90.62 micrometers

### Association of RNFL with Age (linear regression)
| RNFL Sector | p-value | Significant? |
|---|---|---|
| Global | p = 0.005 | Yes |
| Nasal-superior | p = 0.025 | Yes |
| Temporal-superior | p < 0.001 | Yes |
| Temporal-inferior | p = 0.004 | Yes |
| Nasal | p = 0.237 | No |
| Temporal | p = 0.216 | No |
| Nasal-inferior | p = 0.862 | No |

### Association of MRW with Age (linear regression)
| MRW Sector | p-value | Significant? |
|---|---|---|
| Global | p = 0.019 | Yes |
| Nasal-superior | p = 0.020 | Yes |
| Temporal-superior | p = 0.014 | Yes |
| Temporal | p = 0.004 | Yes |
| Temporal-inferior | p = 0.019 | Yes |
| Nasal | p = 0.272 | No |
| Nasal-inferior | p = 0.103 | No |

### Association of RNFL with Number of Injections (linear regression)
| RNFL Sector | p-value | Significant? |
|---|---|---|
| Global | p = 0.642 | No |
| All other sectors | Not significant (individual values not reported) | No |

**Key finding:** No significant impact of number of injections on RNFL globally or in any sector.

### Association of MRW with Number of Injections (linear regression)
| MRW Sector | p-value | Significant? |
|---|---|---|
| Global | p = 0.012 | Yes |
| Temporal | p = 0.011 | Yes |
| Temporal-inferior | p = 0.044 | Yes |
| Nasal | p = 0.079 | No |
| Nasal-superior | p = 0.099 | No |
| Temporal-superior | p = 0.065 | No |
| Nasal-inferior | p = 0.141 | No |

**Key finding:** Global MRW was significantly reduced with increasing number of intravitreal injections.

### Age-Adjusted Analysis (confounding factor adjustment)
| Parameter | p-value (age-adjusted) | Significant? |
|---|---|---|
| Global RNFL vs. injections | p = 0.566 | No |
| Global MRW vs. injections | p = 0.023 | Yes |

**Key finding:** After adjusting for the confounding factor of age, the significance was maintained: RNFL remained non-significant (p = 0.566) and MRW remained significant (p = 0.023).

### Summary of Key Numerical Findings
1. Mean global RNFL = 90.62 micrometers
2. Both RNFL and MRW significantly decreased with age (p = 0.005 and p = 0.019)
3. No significant effect of injection count on RNFL (global p = 0.642; age-adjusted p = 0.566)
4. Significant effect of injection count on MRW (global p = 0.012; age-adjusted p = 0.023)
5. MRW sectors significantly affected by injection count: temporal (p = 0.011), temporal-inferior (p = 0.044)

## Tables

**Note:** This paper contained no formal numbered tables. All quantitative data was reported in the text and via scatter plot figures. The numerical data has been extracted into structured tables in the Results section above.

## Figures

### Figure 1
- **Title:** Exemplary retinal nerve fiber layer (RNFL) measurement
- **Type:** Clinical image / OCT output example
- **Content:** Shows a representative RNFL measurement from Spectralis OCT with Heyex 2 software interface

### Figure 2
- **Title:** Exemplary minimum rim width (MRW) measurement
- **Type:** Clinical image / OCT output example
- **Content:** Shows a representative MRW measurement from Spectralis OCT with Heyex 2 software interface

### Figure 3
- **Title:** Age distribution and number of eyes
- **Type:** Bar chart / histogram
- **Content:** Displays the distribution of patient ages and corresponding number of eyes in the study (N = 66 eyes, mean age 83.4 years)

### Figure 4
- **Title:** Global retinal nerve fiber layer (RNFL) by age
- **Type:** Scatter plot with linear regression
- **Content:** Shows global RNFL (micrometers) plotted against age. Green dots = right eyes, red dots = left eyes. Demonstrates significant negative correlation (p = 0.005).

### Figure 5
- **Title:** Global minimum rim width (MRW) by age
- **Type:** Scatter plot with linear regression
- **Content:** Shows global MRW plotted against age. Green dots = right eyes, red dots = left eyes. Demonstrates significant negative correlation (p = 0.019).

### Figure 6
- **Title:** Global retinal nerve fiber layer (RNFL) by total number of intravitreal injections
- **Type:** Scatter plot with linear regression
- **Content:** Shows global RNFL plotted against total number of injections. No significant correlation found (p = 0.642).

### Figure 7
- **Title:** Global minimum rim width (MRW) by total number of intravitreal injections
- **Type:** Scatter plot with linear regression
- **Content:** Shows global MRW plotted against total number of injections. Significant negative correlation found (p = 0.012).

### Figure 8
- **Title:** Global retinal nerve fiber layer (RNFL) adjusted for age (residuals) and grouped by total number of intravitreal injections
- **Type:** Scatter plot (age-adjusted residuals)
- **Content:** Shows age-adjusted RNFL residuals plotted against injection count. Non-significant (p = 0.566).

### Figure 9
- **Title:** Global minimum rim width (MRW) adjusted for age (residuals) and grouped by total number of intravitreal injections
- **Type:** Scatter plot (age-adjusted residuals)
- **Content:** Shows age-adjusted MRW residuals plotted against injection count. Significant negative association maintained after age adjustment (p = 0.023).
