# Association Between Cumulative Intravitreal Anti-VEGF Injections and Optic Nerve Head Parameters in Neovascular Age-Related Macular Degeneration: A Cross-Sectional Study

**Authors:** [Author et al.]

**Affiliations:** Department of Ophthalmology, [Institution], [City], [Country]

**Correspondence:** [Corresponding Author], [Institution]

---

## Abstract

**Purpose:** Intravitreal anti-vascular endothelial growth factor (anti-VEGF) injections are the standard of care for neovascular age-related macular degeneration (nAMD), yet their cumulative impact on optic nerve head structures remains incompletely understood. The present study aimed to investigate the association between the number of intravitreal anti-VEGF injections and retinal nerve fiber layer thickness (RNFL) and Bruch's membrane opening minimum rim width (MRW) in eyes with nAMD.

**Methods:** This cross-sectional study included 66 eyes of patients with choroidal neovascularization (CNV) secondary to nAMD treated at a tertiary ophthalmology department in a European center. All eyes had received intravitreal anti-VEGF injections administered without paracentesis according to a pro-re-nata (PRN) regimen. RNFL and MRW were measured using spectral-domain optical coherence tomography (Spectralis OCT, Heidelberg Engineering) and analyzed with Heyex 2 software. Seven sectors were evaluated: global, nasal, nasal-superior, nasal-inferior, temporal, temporal-superior, and temporal-inferior. Linear regression models were used to assess associations between optic nerve head parameters and both age and injection count. Analyses were performed using R (version 4.0.3).

**Results:** The mean patient age was 83.4 years, with a mean of 12.58 prior injections. Mean global RNFL was 90.62 micrometers. Both RNFL and MRW decreased with age (global RNFL: p = 0.005; global MRW: p = 0.019). No significant association was found between the number of injections and global RNFL (p = 0.642; age-adjusted p = 0.566). However, global MRW was significantly reduced with increasing injection count (p = 0.012; age-adjusted p = 0.023).

**Conclusions:** Cumulative intravitreal anti-VEGF injections were associated with reduced MRW but not RNFL in eyes with nAMD. MRW may be a more sensitive marker for detecting injection-related changes at the optic nerve head. These findings warrant further longitudinal investigation.

---

## Introduction

Age-related macular degeneration (AMD) is among the leading causes of irreversible vision loss in elderly populations worldwide [REF]. The neovascular form of AMD (nAMD), characterized by choroidal neovascularization (CNV), accounts for a substantial proportion of severe visual impairment attributable to AMD and is managed primarily through intravitreal injections of anti-vascular endothelial growth factor (anti-VEGF) agents [REF]. Since their introduction, anti-VEGF therapies have revolutionized the management of nAMD, offering significant improvements in visual acuity outcomes compared with prior treatment modalities [REF]. However, as treatment protocols frequently require repeated injections over many years, the cumulative effects of long-term intravitreal therapy on ocular structures beyond the macula have become an area of increasing clinical interest.

One concern that has emerged with repeated intravitreal injections is the potential for transient intraocular pressure (IOP) elevation following each injection, which could theoretically exert cumulative damage on the optic nerve head over time [REF]. Each intravitreal injection introduces a bolus of fluid into the vitreous cavity, causing an acute spike in IOP that typically resolves within minutes to hours. Nevertheless, whether repeated episodes of transient IOP elevation contribute to sustained structural changes at the optic nerve head remains a subject of debate [REF]. Several studies have investigated the relationship between anti-VEGF injection frequency and glaucoma-related parameters, with mixed findings reported across different measurement modalities and patient populations [REF].

Retinal nerve fiber layer (RNFL) thickness and Bruch's membrane opening minimum rim width (MRW) are two key optical coherence tomography (OCT)-derived parameters used to evaluate the structural integrity of the optic nerve head. RNFL thickness has long been established as a standard metric for detecting and monitoring glaucomatous damage [REF]. More recently, MRW has gained attention as a potentially more sensitive and anatomically precise marker of neuroretinal rim integrity, as it measures the minimum distance from the Bruch's membrane opening to the internal limiting membrane, thereby accounting for individual anatomical variation in optic disc morphology [REF]. Despite the availability of these sensitive OCT-based measures, limited data exist regarding their behavior in the context of cumulative anti-VEGF exposure in elderly patients with nAMD.

The present study aimed to investigate the association between the cumulative number of intravitreal anti-VEGF injections and optic nerve head parameters, specifically RNFL thickness and MRW, in a cohort of eyes with nAMD. A secondary objective was to evaluate the role of age as a confounding factor in these associations. Understanding whether repeated intravitreal injections are associated with structural optic nerve head changes is relevant for the long-term management and monitoring of patients receiving chronic anti-VEGF therapy.

---

## Methods

### Study Design and Ethics

This was a cross-sectional study conducted at the Department of Ophthalmology of a tertiary hospital in a European center. The study protocol was approved by the local ethics committee and adhered to the tenets of the Declaration of Helsinki. Informed consent was waived due to the retrospective character of the study.

### Participants

A total of 66 eyes of patients diagnosed with choroidal neovascularization (CNV) secondary to neovascular age-related macular degeneration (nAMD) were included. All eyes had received intravitreal anti-VEGF injections applied without paracentesis, administered according to a pro-re-nata (PRN, as-needed) treatment regimen.

### Exclusion Criteria

Eyes were excluded if any of the following conditions were present: uncontrolled elevated intraocular pressure (IOP) exceeding 21 mmHg prior to the initiation of anti-VEGF injections, a history of ischemic optic atrophy, a diagnosis of glaucoma prior to the commencement of anti-VEGF treatment, the presence of a clinically significant epiretinal membrane, or high myopia.

### Outcome Measures

The primary outcome measures were:

1. **Retinal nerve fiber layer thickness (RNFL):** measured in micrometers across seven sectors (global, nasal, nasal-superior, nasal-inferior, temporal, temporal-superior, and temporal-inferior).
2. **Bruch's membrane opening minimum rim width (MRW):** measured across the same seven sectors.

### Measurement Protocol

All measurements were obtained using spectral-domain optical coherence tomography (Spectralis OCT, Heidelberg Engineering, Heidelberg, Germany) and analyzed with Heyex 2 software, utilizing age-matched reference values. Manual corrections of RNFL segmentation boundaries and Bruch's membrane opening delineation were performed by a trained physician when automatic segmentation was deemed inaccurate.

### Statistical Analysis

Linear regression models were used to assess the association between the primary outcome measures (RNFL and MRW) and two independent variables: (1) patient age, and (2) the total number of intravitreal anti-VEGF injections received. To address the potential confounding effect of age on the relationship between injection count and optic nerve head parameters, age-adjusted linear regression analyses were also performed. All analyses were conducted using R software (version 4.0.3). Statistical significance was defined as p < 0.05.

---

## Results

### Sample Characteristics

The study included 66 eyes of patients with CNV secondary to nAMD. The mean age of the study population was 83.4 years. The mean number of prior intravitreal anti-VEGF injections received was 12.58. The mean global RNFL thickness was 90.62 micrometers.

### Association of RNFL with Age

Linear regression analysis revealed a statistically significant negative association between age and RNFL thickness in four of the seven sectors analyzed (Table 1). Global RNFL was significantly associated with age (p = 0.005). Significant associations were also observed for the nasal-superior (p = 0.025), temporal-superior (p < 0.001), and temporal-inferior (p = 0.004) sectors. No significant associations were found for the nasal (p = 0.237), temporal (p = 0.216), or nasal-inferior (p = 0.862) sectors.

**Table 1. Association of RNFL Thickness with Age by Sector (Linear Regression)**

| RNFL Sector | p-value | Significant (p < 0.05) |
|---|---|---|
| Global | 0.005 | Yes |
| Nasal-superior | 0.025 | Yes |
| Temporal-superior | < 0.001 | Yes |
| Temporal-inferior | 0.004 | Yes |
| Nasal | 0.237 | No |
| Temporal | 0.216 | No |
| Nasal-inferior | 0.862 | No |

### Association of MRW with Age

Global MRW was significantly associated with age (p = 0.019). Significant associations were observed in five sectors: nasal-superior (p = 0.020), temporal-superior (p = 0.014), temporal (p = 0.004), and temporal-inferior (p = 0.019). No significant associations were found for the nasal (p = 0.272) or nasal-inferior (p = 0.103) sectors (Table 2).

**Table 2. Association of MRW with Age by Sector (Linear Regression)**

| MRW Sector | p-value | Significant (p < 0.05) |
|---|---|---|
| Global | 0.019 | Yes |
| Nasal-superior | 0.020 | Yes |
| Temporal-superior | 0.014 | Yes |
| Temporal | 0.004 | Yes |
| Temporal-inferior | 0.019 | Yes |
| Nasal | 0.272 | No |
| Nasal-inferior | 0.103 | No |

### Association of RNFL with Number of Injections

No statistically significant association was found between the total number of intravitreal anti-VEGF injections and RNFL thickness in any of the seven sectors analyzed. The global RNFL showed no significant association with injection count (p = 0.642). All remaining sectors were also non-significant (Table 3).

**Table 3. Association of RNFL Thickness with Number of Injections by Sector (Linear Regression)**

| RNFL Sector | p-value | Significant (p < 0.05) |
|---|---|---|
| Global | 0.642 | No |
| All other sectors | Not significant | No |

### Association of MRW with Number of Injections

Global MRW was significantly associated with the number of intravitreal injections (p = 0.012). Sector-specific analysis revealed significant associations in the temporal (p = 0.011) and temporal-inferior (p = 0.044) sectors. No significant associations were observed in the nasal (p = 0.079), nasal-superior (p = 0.099), temporal-superior (p = 0.065), or nasal-inferior (p = 0.141) sectors (Table 4).

**Table 4. Association of MRW with Number of Injections by Sector (Linear Regression)**

| MRW Sector | p-value | Significant (p < 0.05) |
|---|---|---|
| Global | 0.012 | Yes |
| Temporal | 0.011 | Yes |
| Temporal-inferior | 0.044 | Yes |
| Nasal | 0.079 | No |
| Nasal-superior | 0.099 | No |
| Temporal-superior | 0.065 | No |
| Nasal-inferior | 0.141 | No |

### Age-Adjusted Analysis

After adjusting for the confounding effect of age, the association between injection count and global RNFL remained non-significant (p = 0.566). The association between injection count and global MRW remained statistically significant after age adjustment (p = 0.023) (Table 5).

**Table 5. Age-Adjusted Association of Optic Nerve Head Parameters with Number of Injections (Linear Regression)**

| Parameter | p-value (age-adjusted) | Significant (p < 0.05) |
|---|---|---|
| Global RNFL vs. injections | 0.566 | No |
| Global MRW vs. injections | 0.023 | Yes |

---

## Discussion

### Summary of Key Findings

The present study investigated the relationship between cumulative intravitreal anti-VEGF injection exposure and optic nerve head structural parameters in eyes with nAMD. The principal finding was a divergence between the two OCT-derived metrics: while RNFL thickness showed no significant association with the number of injections received (p = 0.642; age-adjusted p = 0.566), MRW was significantly reduced with increasing injection count (p = 0.012), and this association persisted after adjustment for age (p = 0.023). Both parameters demonstrated significant age-related decline, consistent with known patterns of physiological neuroretinal aging.

### Differential Sensitivity of MRW and RNFL

The dissociation between MRW and RNFL findings is of particular interest. MRW measures the minimum distance from the Bruch's membrane opening to the internal limiting membrane and has been proposed as a more anatomically precise indicator of neuroretinal rim tissue integrity compared with conventional RNFL thickness measurements [REF]. Several prior studies have reported that MRW may detect structural optic nerve head changes earlier than RNFL in the context of glaucoma and pre-perimetric glaucomatous damage [REF]. The present findings are consistent with this notion and suggest that MRW may also serve as a more sensitive marker for detecting subtle injection-related structural changes at the optic nerve head. The fact that the temporal and temporal-inferior sectors exhibited the strongest associations with injection count aligns with known patterns of vulnerability in the optic nerve head, as the temporal and inferior sectors are often the first to be affected in glaucomatous optic neuropathy [REF].

### Comparison with Prior Literature

The relationship between intravitreal anti-VEGF therapy and optic nerve head integrity has been examined in several prior investigations with varying results. Some studies have reported sustained IOP elevation and glaucomatous progression following repeated intravitreal injections [REF], while others have found no clinically meaningful long-term impact on IOP or optic nerve parameters [REF]. The discrepant findings across studies may relate to differences in injection protocols (including whether paracentesis was performed), the specific anti-VEGF agent used, cumulative injection burden, and the measurement parameters assessed. Notably, the present study specifically examined eyes treated without paracentesis, which may result in more pronounced transient IOP spikes compared with injection protocols that include anterior chamber paracentesis to normalize pressure [REF]. A prior investigation reported that MRW reductions were detectable in eyes receiving intravitreal injections even when RNFL remained within normal limits [REF], a finding that is consistent with the results of the present study.

### Mechanisms and Clinical Implications

The mechanism underlying the association between cumulative anti-VEGF injections and MRW reduction may involve repeated episodes of transient IOP elevation causing subclinical mechanical stress on the lamina cribrosa and adjacent neuroretinal rim tissue. Each intravitreal injection introduces approximately 0.05 mL of fluid into the vitreous cavity, which can cause IOP spikes exceeding 40 mmHg in the immediate post-injection period [REF]. While these episodes are typically self-limited, their cumulative effect over multiple injections spanning several years could plausibly contribute to structural remodeling of the optic nerve head tissues. This is of particular clinical relevance given the advanced age of the study population (mean 83.4 years), as aging is independently associated with reduced optic nerve head resilience to mechanical stress [REF]. These findings suggest that clinicians managing patients on long-term anti-VEGF therapy should consider incorporating MRW monitoring into their routine follow-up protocols, particularly in patients who have received a large cumulative number of injections.

### Study Strengths

The present study has several methodological strengths. First, the use of both RNFL and MRW as complementary optic nerve head parameters provides a more comprehensive assessment than studies relying on a single metric. Second, measurement with Spectralis OCT (Heidelberg Engineering) and Heyex 2 software, with manual correction of segmentation errors by a trained physician, enhances the reliability and accuracy of the OCT data. Third, the age-adjusted analysis addresses a critical confounding variable in this elderly population, strengthening the inference that the observed MRW reduction is related to injection exposure rather than aging alone. Fourth, the exclusion of eyes with pre-existing glaucoma, uncontrolled IOP, ischemic optic atrophy, epiretinal membrane, and high myopia reduces the likelihood that the observed associations are attributable to these alternative pathologies. Finally, the systematic sector-by-sector analysis across seven optic nerve head regions provides granular topographic information about the pattern of structural change.

### Limitations

Several limitations should be acknowledged. First, the cross-sectional design precludes the establishment of causal relationships; the observed association between injection count and MRW reduction could be influenced by unmeasured confounders. A longitudinal study with baseline pre-treatment measurements would be required to confirm a causal link. Second, the sample size of 66 eyes, while sufficient to detect the observed associations, limits the statistical power for sector-specific analyses and may have been insufficient to detect small but clinically meaningful effects in certain sectors. Third, the study lacked axial eye length measurements, which could influence OCT-derived measurements due to magnification effects. This limitation was mitigated by excluding patients with high myopia, but residual confounding from variations in axial length among the remaining eyes cannot be entirely excluded. Fourth, the absence of data on specific anti-VEGF agents used, individual injection-to-injection IOP measurements, and duration of treatment prevents a more granular analysis of dose-response relationships. Fifth, the use of a cross-sectional design without pre-treatment baseline values means that inter-individual variability in optic nerve head anatomy could not be accounted for.

---

## Conclusions

In this cross-sectional study of 66 eyes with nAMD, cumulative intravitreal anti-VEGF injections administered without paracentesis were associated with reduced Bruch's membrane opening minimum rim width (MRW) but not retinal nerve fiber layer (RNFL) thickness. This association was maintained after adjusting for age as a confounding factor. These findings suggest that MRW may be a more sensitive parameter than RNFL for detecting subtle optic nerve head changes in the context of repeated intravitreal injections. Prospective longitudinal studies with larger sample sizes and pre-treatment baseline measurements are warranted to confirm these findings and to determine whether MRW reduction translates into clinically meaningful functional consequences. In the interim, the incorporation of MRW assessment into routine monitoring protocols for patients receiving long-term anti-VEGF therapy may be a prudent clinical consideration.

---

## References

[References not available. All citations marked with [REF] placeholders throughout the text. A formal reference list was not extractable from the source data.]

---

## Figures (Descriptions)

**Figure 1.** Exemplary retinal nerve fiber layer (RNFL) measurement obtained using Spectralis OCT with Heyex 2 software interface.

**Figure 2.** Exemplary minimum rim width (MRW) measurement obtained using Spectralis OCT with Heyex 2 software interface.

**Figure 3.** Distribution of patient ages and corresponding number of eyes in the study population (N = 66 eyes; mean age, 83.4 years).

**Figure 4.** Scatter plot with linear regression showing global RNFL (micrometers) plotted against patient age. Green dots represent right eyes; red dots represent left eyes (p = 0.005).

**Figure 5.** Scatter plot with linear regression showing global MRW plotted against patient age. Green dots represent right eyes; red dots represent left eyes (p = 0.019).

**Figure 6.** Scatter plot with linear regression showing global RNFL (micrometers) plotted against total number of intravitreal injections. No significant correlation was observed (p = 0.642).

**Figure 7.** Scatter plot with linear regression showing global MRW plotted against total number of intravitreal injections. A significant negative association was observed (p = 0.012).

**Figure 8.** Scatter plot showing global RNFL adjusted for age (residuals) plotted against total number of intravitreal injections. The association was non-significant (p = 0.566).

**Figure 9.** Scatter plot showing global MRW adjusted for age (residuals) plotted against total number of intravitreal injections. The significant negative association was maintained after age adjustment (p = 0.023).
