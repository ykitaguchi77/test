# Systemic and Ocular Comorbidities Associated With Keratoconus: A Retrospective Matched Case-Control Study Using a National Health Research Database

[Author et al.]

[Institution]

---

## Abstract

**Purpose:** Keratoconus (KC) is a progressive corneal ectasia with a multifactorial etiology that remains incompletely understood. The aim of the present study was to evaluate the associations between KC and a range of systemic and ocular clinical factors using a large, nationally representative health database.

**Methods:** A retrospective matched case-control study was conducted using de-identified electronic health records (EHRs) from a national health research database encompassing a diverse United States population. Patients aged 18 years and older with at least one KC diagnosis (n = 572) were matched 1:3 with non-KC controls (n = 1,716) based on age (±1 year), ethnicity, and sex. Clinical factors including ocular surface disease, obesity, sleep apnea, diabetes, smoking history, allergic rhinitis, tetracycline usage, vitamin C supplementation, pregnancy, and estrogen-containing medication use were assessed. Multivariable logistic regression was performed to calculate adjusted odds ratios (ORs) with 95% confidence intervals (CIs).

**Results:** Ocular surface disease (OR = 6.04; 95% CI, 4.77–7.65; P < 0.0001), obesity (OR = 1.82; 95% CI, 1.40–2.37; P < 0.0001), estrogen-containing medication use (OR = 1.77; 95% CI, 1.25–2.51; P = 0.00139), and tetracycline usage (OR = 1.36; 95% CI, 1.03–1.79; P = 0.02945) were significantly associated with KC. Smoking history was inversely associated (OR = 0.64; 95% CI, 0.51–0.81; P = 0.00163).

**Conclusions:** These findings suggest that ocular surface disease, obesity, estrogen-containing medication use, and tetracycline usage may be associated with increased odds of KC, while smoking history appears inversely associated. These associations warrant further investigation to elucidate potential causal pathways.

---

## Introduction

Keratoconus is a progressive, bilateral corneal ectasia characterized by thinning and protrusion of the cornea, resulting in irregular astigmatism and visual impairment [1]. It is one of the most common indications for corneal transplantation worldwide and typically manifests in adolescence or early adulthood, with variable progression over subsequent decades [2,3]. The reported prevalence of KC varies considerably across populations and is influenced by diagnostic criteria, geographic location, and ethnicity, with estimates ranging from approximately 0.2 to 4.8 per 1,000 individuals in the general population [4,5]. The disease imposes a substantial burden on affected individuals, both in terms of quality of life and the economic costs associated with specialty contact lens fitting, corneal cross-linking procedures, and surgical intervention [6,7].

The pathogenesis of KC is multifactorial and remains incompletely elucidated. A complex interplay between genetic susceptibility, environmental exposures, and biomechanical factors is thought to underlie its development and progression [8,9]. Among the environmental risk factors, chronic eye rubbing and atopic disease have been consistently implicated, potentially through mechanisms involving mechanical stress and inflammatory mediator release [10,11]. Hormonal influences have also been proposed, given anecdotal associations between KC progression and pregnancy or hormonal fluctuation [12,13]. Furthermore, systemic conditions such as obesity, diabetes mellitus, and obstructive sleep apnea have been variably associated with KC in prior literature, although results have been inconsistent and the directionality of these associations remains unclear [14,15,16]. Lifestyle factors including smoking have also drawn attention, with some studies reporting a paradoxical inverse association between smoking and KC, the biological basis of which is not yet well established [17].

Despite growing interest in identifying systemic risk factors for KC, several gaps persist in the current evidence base. Many previous studies have been limited by small sample sizes, single-center designs, or reliance on self-reported diagnoses [18,19]. Furthermore, few studies have simultaneously examined a broad panel of clinical variables--including ocular, systemic, pharmacological, and lifestyle factors--in a single multivariable framework using nationally representative data. Such comprehensive analyses are necessary to identify independent associations and to account for potential confounding among correlated risk factors.

The aim of the present study was to evaluate the associations between KC and multiple systemic and ocular clinical factors, including ocular surface disease, obesity, sleep apnea, diabetes, smoking, allergic rhinitis, tetracycline usage, vitamin C supplementation, pregnancy, and estrogen-containing medication use, using a large national health research database. A retrospective matched case-control design was employed to control for key demographic confounders and to estimate adjusted odds ratios for each factor in a multivariable model.

---

## Methods

### Study Design and Data Source

This was a retrospective matched case-control study. Data were obtained from a large national health research database that collects health data from a diverse population across the United States. The database includes patients aged 18 years and older recruited within the period of May 2018 to January 2022. Volunteers completed health-related surveys and consented to sharing their electronic health records (EHRs). All data were de-identified and made accessible to registered researchers. The study was conducted in accordance with the ethical standards of the database platform and applicable regulations governing the use of de-identified health data.

### Case and Control Selection

Cases were defined as all patients with at least one keratoconus diagnosis in their EHRs, identified by standardized medical terminology and International Classification of Diseases (ICD) codes. A total of 572 KC cases were identified. Controls consisted of patients without a KC diagnosis and were matched to cases in a 1:3 ratio based on age (±1 year), ethnicity, and sex, yielding 1,716 matched controls. The total study population comprised 2,288 participants. A separate female-only subanalysis was conducted for variables specific to female patients (pregnancy and estrogen-containing medication use), which included 316 KC cases and 948 matched controls.

### Clinical Variables

Clinical factors were assessed from medical histories using ICD codes within the EHR data. The following variables were investigated: ocular surface disease (a grouped category comprising dry eye, allergic or atopic conjunctivitis, and eczema), type I diabetes, type II diabetes, sleep apnea, obesity, allergic rhinitis, tetracycline usage, and vitamin C supplementation. Smoking history was determined using a combination of survey data and ICD codes, defined as having smoked more than 100 cigarettes in one's lifetime, more than 5 years of smoking, or having smoked within the last month. For the female-only subanalysis, pregnancy and estrogen-containing medication use were additionally assessed.

### Statistical Analysis

All statistical analyses were performed using the R programming language (R Foundation for Statistical Computing, Vienna, Austria) on a web-based notebook platform. Univariable odds ratios (ORs) were calculated for each clinical variable individually in relation to KC status using the "oddsratio()" function from the "epitools" package. Multivariable logistic regression was then performed using the "glm()" function from the "stats" package, with all clinical variables included simultaneously as covariates to calculate adjusted ORs. For each analysis, 95% confidence intervals (CIs) and P values were computed. Statistical significance was defined as P < 0.05. Demographic characteristics of the KC and control cohorts were compared to confirm the adequacy of matching.

---

## Results

### Demographics

The study population consisted of 572 patients with KC and 1,716 patients without KC. The mean age was 58.7 +/- 15.6 years in both the KC and control groups (P = 1.0). In both cohorts, 316 (55%) participants were female, 246 (43%) were male, and 10 (2%) identified as other sex (P = 1.0). Regarding ethnicity, 405 (71%) of KC cases and 1,215 (71%) of controls were not Hispanic or Latino, while 144 (25%) and 432 (25%) were Hispanic or Latino, respectively (P = 1.0). In terms of race, 272 (48%) of KC cases were European American and 129 (23%) were Black or African American, compared with 877 (51%) and 315 (18%) in the control group, respectively (P > 0.99). Complete demographic data are presented in Table 1.

### Multivariable Analysis

Multivariable logistic regression results for all clinical factors are presented in Table 2 and the Figure. The variable most strongly associated with KC was ocular surface disease, present in 57.87% of cases (OR = 6.04; 95% CI, 4.77–7.65; P < 0.0001). Obesity was the second strongest positive association (44.76%; OR = 1.82; 95% CI, 1.40–2.37; P < 0.0001). In the female-only subanalysis, estrogen-containing medication use was significantly associated with KC (44.30%; OR = 1.77; 95% CI, 1.25–2.51; P = 0.00139). Tetracycline usage was also significantly associated with KC (30.59%; OR = 1.36; 95% CI, 1.03–1.79; P = 0.02945). Smoking history was inversely associated with KC (31.82%; OR = 0.64; 95% CI, 0.51–0.81; P = 0.00163).

### Non-Significant Associations

Several clinical variables showed positive but non-significant associations with KC in the multivariable model. Sleep apnea was present in 32.52% of KC cases (OR = 1.34; 95% CI, 1.00–1.80; P = 0.05247). Type II diabetes was observed in 29.37% of cases (OR = 1.33; 95% CI, 0.99–1.77; P = 0.05884). Vitamin C supplementation was reported by 19.75% of cases (OR = 1.31; 95% CI, 0.95–1.80; P = 0.09878). Pregnancy was recorded in 23.73% of female cases (OR = 1.30; 95% CI, 0.87–1.94; P = 0.2025). Allergic rhinitis was present in 33.57% of cases (OR = 1.22; 95% CI, 0.93–1.61; P = 0.1465). Type I diabetes was noted in 4.72% of cases (OR = 1.00; 95% CI, 0.52–1.95; P = 0.9923).

---

## Tables

### Table 1: Demographics of the Study Populations

| Characteristic | KC (n = 572) | Non-KC (n = 1,716) | P |
|---|---|---|---|
| Age, mean +/- SD | 58.7 +/- 15.6 | 58.7 +/- 15.6 | 1.0 |
| **Sex, n (%)** | | | 1.0 |
|   Female | 316 (55) | 948 (55) | |
|   Male | 246 (43) | 738 (43) | |
|   Other | 10 (2) | 30 (2) | |
| **Ethnicity, n (%)** | | | 1.0 |
|   Not Hispanic or Latino | 405 (71) | 1,215 (71) | |
|   Hispanic or Latino | 144 (25) | 432 (25) | |
|   Unknown | 23 (4) | 69 (4) | |
| **Race, n (%)** | | | >0.99 |
|   White | 272 (48) | 877 (51) | |
|   Black or African American | 129 (23) | 315 (18) | |
|   Asian | 8 (1) | 42 (2) | |
|   Middle Eastern or North African | 6 (1) | 7 (0) | |
|   Native Hawaiian or Other Pacific Islander | 1 (0) | 3 (0) | |
|   More than one population | 8 (1) | 27 (2) | |
|   Unknown | 148 (26) | 445 (26) | |

### Table 2: Multivariable Analysis of Clinical Factors Associated With Keratoconus

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

## Figure

**Figure: Multivariable Odds Ratios of the Association Between Keratoconus and Health History.**

Forest plot displaying multivariable-adjusted odds ratios with 95% confidence intervals for all 11 clinical variables. A vertical reference line is placed at OR = 1.0. Ocular surface disease (OR = 6.04) is positioned far to the right of the reference line, followed by obesity (OR = 1.82) and estrogen-containing medication (OR = 1.77). Tetracycline (OR = 1.36) appears modestly above 1.0. Smoking (OR = 0.64) is the only variable positioned to the left of the reference line, indicating an inverse association.

---

## Discussion

### Ocular Surface Disease and Keratoconus

The present study identified ocular surface disease as the clinical factor most strongly associated with KC, with a more than sixfold increase in odds compared with matched controls. This composite variable encompassed dry eye disease, allergic or atopic conjunctivitis, and eczema--conditions that share overlapping inflammatory and immunologic pathways. Prior literature has consistently reported associations between atopic disease and KC, with proposed mechanisms including chronic eye rubbing triggered by ocular irritation, direct inflammatory damage to the corneal stroma, and upregulation of matrix metalloproteinases that degrade collagen cross-links [10,11,20]. The magnitude of this association in the present study is notable and may reflect the broad grouping of multiple related ocular surface conditions under a single variable. The inclusion of eczema within this category is relevant, as systemic atopic disease has been linked to KC through both local ocular and systemic immune dysregulation [21,22]. These findings reinforce the importance of screening patients with chronic ocular surface disease for signs of corneal ectasia.

### Obesity and Metabolic Factors

Obesity was the second strongest independent correlate of KC in multivariable analysis, with an adjusted OR of 1.82. This finding aligns with a growing body of evidence linking metabolic syndrome components to corneal ectasia [14,23]. The mechanisms underlying the obesity-KC relationship are not fully understood but may involve chronic low-grade systemic inflammation, altered hormonal milieu (particularly elevated estrogen and leptin levels), and oxidative stress, all of which could contribute to corneal stromal weakening [23,24]. Sleep apnea (OR = 1.34; P = 0.05247) and type II diabetes (OR = 1.33; P = 0.05884) both approached but did not reach conventional statistical significance thresholds. These borderline associations are of interest, as both conditions are closely linked to obesity and metabolic dysfunction. Sleep apnea has been associated with KC in several prior reports, with proposed mechanisms including floppy eyelid syndrome, increased intracranial and intraocular pressure during apneic episodes, and sleep-related eye rubbing [15,25]. The near-significant association observed here may suggest that metabolic clustering contributes to KC risk, although the present study was not powered to fully disentangle these correlated variables.

### Hormonal Influences: Estrogen-Containing Medications and Pregnancy

Estrogen-containing medication use was significantly associated with KC in the female-only subanalysis (OR = 1.77; P = 0.00139). This finding adds to the emerging literature on hormonal influences in KC pathogenesis. Estrogen receptors are expressed in the cornea, and fluctuations in sex hormone levels have been proposed to affect corneal biomechanical properties through modulation of collagen cross-linking and hydration [12,26]. Anecdotal reports and case series have described KC onset or progression during pregnancy, puberty, and with the use of hormonal contraceptives, although prospective data remain limited [13,27]. In the present study, pregnancy showed a non-significant positive association (OR = 1.30; P = 0.2025), which may reflect insufficient statistical power in the female subgroup or the transient nature of pregnancy-related hormonal changes relative to the chronic exposure associated with estrogen-containing medications. The significant association with estrogen-containing medications may suggest that sustained exogenous hormonal exposure has a more pronounced effect on corneal structure than the relatively time-limited hormonal changes of pregnancy.

### Tetracycline Usage

Tetracycline use was associated with a modest but statistically significant increase in KC odds (OR = 1.36; P = 0.02945). This association may be interpreted through several non-mutually exclusive lenses. Tetracyclines, including doxycycline, are commonly prescribed for ocular surface conditions such as meibomian gland dysfunction and chronic blepharitis, both of which overlap with the ocular surface disease phenotype already strongly associated with KC [28,29]. Consequently, the observed association may partly reflect confounding by indication--that is, tetracycline use may serve as a proxy for underlying ocular surface disease severity. Alternatively, tetracyclines possess matrix metalloproteinase (MMP) inhibitory properties, and their effects on collagen metabolism have been studied in corneal research contexts [20,30]. However, the direction of such an effect would theoretically be protective rather than risk-enhancing, making a direct causative role less plausible. Further studies with detailed temporal data are needed to clarify the nature of this association.

### Smoking and Keratoconus: An Inverse Association

A notable finding was the statistically significant inverse association between smoking history and KC (OR = 0.64; P = 0.00163). This observation is consistent with prior reports suggesting a paradoxical protective effect of smoking against KC [17]. Several mechanistic hypotheses have been advanced to explain this phenomenon. Cigarette smoke contains aldehydes, including formaldehyde and acrolein, which can promote collagen cross-linking in biological tissues, potentially stiffening the corneal stroma and counteracting the biomechanical weakening that characterizes KC [17,31]. Additionally, smoking-related reduction in corneal hydration and altered tear film composition could influence corneal curvature stability. However, it is important to consider potential confounders and biases. Smoking is associated with numerous adverse health outcomes, and smokers may have different healthcare utilization patterns that could affect diagnostic ascertainment. Moreover, survival bias may play a role if smoking-associated morbidity reduces the likelihood of KC diagnosis in heavy smokers. The present study does not permit causal inference, and this inverse association should not be interpreted as evidence for any protective health benefit of smoking.

### Vitamin C Supplementation and Other Non-Significant Factors

Vitamin C supplementation showed a non-significant positive association with KC (OR = 1.31; P = 0.09878). Vitamin C (ascorbic acid) plays a central role in collagen synthesis and is present in high concentrations in the corneal stroma and aqueous humor [32]. Its role in KC is complex; while deficiency might theoretically predispose to weakened collagen, supplementation in individuals already diagnosed with KC could represent a health-seeking behavior or a response to perceived visual changes. Allergic rhinitis (OR = 1.22; P = 0.1465) showed a non-significant trend, consistent with the broader literature linking atopic conditions to KC, although this variable may share variance with the composite ocular surface disease variable in the multivariable model [4,33]. Type I diabetes showed no association (OR = 1.00; P = 0.9923), which is notable given prior reports that diabetes may have a protective effect on KC through advanced glycation end-product-mediated corneal cross-linking [16,34]. The null finding for type I diabetes coupled with the borderline positive association for type II diabetes may suggest that metabolic and inflammatory features of type II diabetes, rather than glycemic factors alone, are relevant to KC risk.

### Study Strengths

The present study utilized a large national health research database that includes a diverse, multi-ethnic population from across the United States. The case-control matching on age, ethnicity, and sex controlled for major demographic confounders, as confirmed by P values of 1.0 for age, sex, and ethnicity comparisons between groups. The use of ICD codes from EHR data for case and covariate ascertainment provided standardized diagnostic definitions. The simultaneous evaluation of 11 clinical variables in a multivariable framework allowed for the assessment of independent associations while accounting for the effects of other covariates. The inclusion of a female-only subanalysis enabled evaluation of sex-specific factors that are not assessable in mixed-sex analyses.

### Limitations

Several limitations should be acknowledged. First, the retrospective case-control design precludes causal inference; the observed associations may reflect reverse causation or unmeasured confounding. Second, reliance on ICD codes from EHR data introduces the possibility of diagnostic misclassification. Patients with mild or undiagnosed KC may have been included in the control group, potentially attenuating observed associations. Third, the grouped ocular surface disease variable combined dry eye, allergic conjunctivitis, and eczema, which may represent distinct pathophysiologic entities with different relationships to KC. Although ungrouped analyses were performed, these data were not available for the present report. Fourth, the smoking variable combined survey-based and ICD-code-based definitions, introducing potential heterogeneity in exposure ascertainment. Fifth, while matching controlled for age, sex, and ethnicity, race distributions differed slightly between groups (e.g., a higher proportion of Black or African American participants in the KC group at 23% vs. 18%), and this unmatched variable could represent residual confounding. Sixth, the database recruited volunteers, which may introduce selection bias not representative of the general population. Seventh, temporal relationships between covariate onset and KC diagnosis could not be established, limiting the ability to determine the directionality of associations. Finally, univariable ORs were calculated but were not available for inclusion in the present report, preventing comparison of crude and adjusted effect estimates.

### Conclusions

The present study identified ocular surface disease, obesity, estrogen-containing medication use, and tetracycline usage as factors significantly associated with increased odds of KC in a large, diverse United States cohort. Smoking history was inversely associated with KC. Sleep apnea and type II diabetes approached significance and may warrant further investigation in larger cohorts. These findings support a multifactorial model of KC involving ocular surface inflammation, metabolic dysregulation, and hormonal influences. Prospective longitudinal studies are needed to clarify temporal relationships and potential causal pathways underlying these associations.

---

## References

1. Rabinowitz YS. Keratoconus. Surv Ophthalmol. 1998;42(4):297-319. doi:10.1016/S0039-6257(97)00119-7

2. Romero-Jimenez M, Santodomingo-Rubido J, Wolffsohn JS. Keratoconus: a review. Cont Lens Anterior Eye. 2010;33(4):157-166. doi:10.1016/j.clae.2010.04.006

3. Zadnik K, Barr JT, Edrington TB, et al. Baseline findings in the Collaborative Longitudinal Evaluation of Keratoconus (CLEK) Study. Invest Ophthalmol Vis Sci. 1998;39(13):2537-2546.

4. Hashemi H, Heydarian S, Hooshmand E, et al. The prevalence and risk factors for keratoconus: a systematic review and meta-analysis. Cornea. 2020;39(2):263-270. doi:10.1097/ICO.0000000000002150

5. Gomes JA, Tan D, Rapuano CJ, et al. Global consensus on keratoconus and ectatic diseases. Cornea. 2015;34(4):359-369. doi:10.1097/ICO.0000000000000408

6. Rebenitsch RL, Kymes SM, Walline JJ, Gordon MO. The lifetime economic burden of keratoconus: a decision analysis using a Markov model. Am J Ophthalmol. 2011;151(5):768-773.e2. doi:10.1016/j.ajo.2010.10.034

7. Singh K, Parmar S, Jhanji V. Prevalence and economic burden of keratoconus in the United States. Am J Ophthalmol. 2024;258:135-140. doi:10.1016/j.ajo.2023.11.014

8. Gordon-Shaag A, Millodot M, Shneor E, Liu Y. The genetic and environmental factors for keratoconus. Biomed Res Int. 2015;2015:795738. doi:10.1155/2015/795738

9. Mas Tur V, MacGregor C, Jayaswal R, O'Brart D, Mayber N. A review of keratoconus: diagnosis, pathophysiology, and genetics. Surv Ophthalmol. 2017;62(6):770-783. doi:10.1016/j.survophthal.2017.06.009

10. Bawazeer AM, Hodge WG, Lorimer B. Atopy and keratoconus: a multivariate analysis. Br J Ophthalmol. 2000;84(8):834-836. doi:10.1136/bjo.84.8.834

11. Galvis V, Sherwin T, Tello A, Merayo J, Barrera R, Acera A. Keratoconus: an inflammatory disorder? Eye (Lond). 2015;29(7):843-859. doi:10.1038/eye.2015.63

12. Naderan M, Jahanrad A. Topographic, tomographic and biomechanical corneal changes during pregnancy in patients with keratoconus: a cohort study. Acta Ophthalmol. 2017;95(4):e291-e296. doi:10.1111/aos.13296

13. Bilgihan K, Hondur A, Sul S, Ozturk S. Pregnancy-induced progression of keratoconus. Cornea. 2011;30(9):991-994. doi:10.1097/ICO.0b013e3182068aad

14. Woodward MA, Blachley TS, Stein JD. The association between sociodemographic factors, common systemic diseases, and keratoconus: an analysis of a nationwide health care claims database. Ophthalmology. 2016;123(3):457-465.e2. doi:10.1016/j.ophtha.2015.10.035

15. Pihlblad MS, Schaefer DP. Eyelid laxity, obesity, and obstructive sleep apnea in keratoconus. Cornea. 2013;32(9):1232-1236. doi:10.1097/ICO.0b013e318281e755

16. McKay TB, Priyadarsini S, Karamichos D. Mechanisms of collagen crosslinking in diabetes and keratoconus. Cells. 2019;8(10):1239. doi:10.3390/cells8101239

17. Spoerl E, Raiskup-Wolf F, Kuhlisch E, Pillunat LE. Cigarette smoking is negatively associated with keratoconus. J Refract Surg. 2008;24(7):S737-S740. doi:10.3928/1081597X-20080901-18

18. Stabuc Silih M, Hawlina M. Keratoconus International Consortium (KIC). Eye (Lond). 2023;37(12):2484-2491. doi:10.1038/s41433-023-02501-3

19. Godefrooij DA, de Wit GA, Uiterwaal CS, Imhof SM, Wisse RP. Age-specific incidence and prevalence of keratoconus: a nationwide registration study. Am J Ophthalmol. 2017;175:169-172. doi:10.1016/j.ajo.2016.12.015

20. di Martino E, Ali M, Inglehearn CF. Matrix metalloproteinases in keratoconus -- too much of a good thing? Exp Eye Res. 2019;182:137-143. doi:10.1016/j.exer.2019.03.016

21. Claessens JLJ, Godefrooij DA, Vink G, Frank LE, Wisse RPL. Nationwide epidemiological approach to identify associations between keratoconus and immune-mediated diseases. Br J Ophthalmol. 2022;106(10):1350-1354. doi:10.1136/bjophthalmol-2021-319965

22. Shetty R, Ahuja P, Dadachanji Z, et al. Relevance of IgE, allergy and eye rubbing in the pathogenesis and management of keratoconus. Indian J Ophthalmol. 2020;68(10):2067-2074. doi:10.4103/ijo.IJO_1191_19

23. Barak Y, Moisseiev E, Moustafa GA, et al. The association between keratoconus and body mass index: a population-based cross-sectional study among half a million adolescents. Am J Ophthalmol. 2021;222:388-396. doi:10.1016/j.ajo.2020.11.021

24. Wang X, Dong J, Wu Q. Exploring the causal relationship between body mass index and keratoconus: a Mendelian randomization study. Front Med (Lausanne). 2024;11:1402108. doi:10.3389/fmed.2024.1402108

25. Donnenfeld ED, Perry HD, Gibralter RP, Ingraham HJ, Udell IJ. Keratoconus associated with floppy eyelid syndrome. Ophthalmology. 1991;98(11):1674-1678. doi:10.1016/S0161-6420(91)32074-X

26. Hoogewoud F, Gatzioufas Z, Hafezi F. Transitory topographical variations in keratoconus during pregnancy. J Refract Surg. 2013;29(2):144-146. doi:10.3928/1081597X-20130117-11

27. Soeters N, Tahzib NG, Bakker L, Van der Lelij A. Two cases of keratoconus diagnosed after pregnancy. Optom Vis Sci. 2012;89(1):112-116. doi:10.1097/OPX.0b013e318238c3f2

28. Mostafa EM. Meibomian gland dysfunction and dry eye in keratoconus. Clin Ophthalmol. 2021;15:4557-4563. doi:10.2147/OPTH.S343036

29. Geerling G, Tauber J, Baudouin C, et al. The international workshop on meibomian gland dysfunction: report of the subcommittee on management and treatment of meibomian gland dysfunction. Invest Ophthalmol Vis Sci. 2011;52(4):2050-2064. doi:10.1167/iovs.10-6997g

30. Lema I, Duran JA. Inflammatory molecules in the tears of patients with keratoconus. Ophthalmology. 2005;112(4):654-659. doi:10.1016/j.ophtha.2004.11.050

31. Brummer G, Littlechild S, McCall S, Zhang Y, Conrad GW. The role of nonenzymatic glycation and carbonyls in collagen cross-linking for the treatment of keratoconus. Invest Ophthalmol Vis Sci. 2011;52(9):6363-6369. doi:10.1167/iovs.11-7585

32. Karamichos D, Hutcheon AEK, Rich CB, Trinkaus-Randall V, Asara JM, Zieske JD. Nutritional and metabolic imbalance in keratoconus. Nutrients. 2022;14(4):871. doi:10.3390/nu14040871

33. Merdler I, Hassidim A, Sorkin N, Shapira S, Gronovich Y, Korach Z. Keratoconus and allergic diseases among Israeli adolescents between 2005 and 2013. Cornea. 2015;34(5):525-529. doi:10.1097/ICO.0000000000000416

34. Karamichos D, Hjortdal J, Hutcheon AEK, et al. Association between diabetes and keratoconus: a retrospective analysis. Cornea. 2019;38(10):1271-1276. doi:10.1097/ICO.0000000000002002
