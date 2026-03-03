# Paper Writing Guidelines

## Iteration History
- Iteration 0: Initial guidelines (default)
- Iteration 1: Added 15 rules from myopia/ophthalmic clinical services cohort study comparison (2026-03-01)
- Iteration 2: Added 6 rules from TVC trabeculectomy vs canaloplasty 11-year RCT follow-up (2026-03-01)
- Iteration 3: Added 9 rules from DR-AMD Taiwan NHIRD retrospective cohort study (2026-03-02)

## Structural Rules
1. Follow IMRAD structure: Introduction, Methods, Results, And Discussion
2. Abstract should be structured: Purpose, Methods, Results, Conclusions
3. Introduction: 3-4 paragraphs (background -> gap -> objective)
4. Discussion: 4-5 paragraphs (summary -> comparison -> limitations -> implications -> conclusion)
5. Each paragraph should have a clear topic sentence
6. **[Iter1]** Keep abstracts within 250-300 words. Report only the most essential results (e.g., cumulative incidence by group, overall incidence rate). Save detailed effect estimates, survival times, and secondary outcomes for the Results section. Do not add epidemiological framing not present in the original.
7. **[Iter1]** Create a standalone Conclusions section after the Discussion, separate from the Discussion body. This matches standard journal structure and improves navigability.
8. **[Iter1]** The Discussion should be the longest and most developed section. Structure it with at least 5 thematic paragraphs: (1) summary of key findings, (2) comparison with prior literature, (3) explanation of unexpected or counterintuitive findings, (4) clinical/policy implications, (5) study strengths. Follow with a separate Limitations section.
9. **[Iter1]** Preserve all sub-sections present in the source Methods: if the original has separate Vision Screening Protocol, Refraction Measurements, Definitions, and Group Classification sections, the draft must include them as distinct subsections rather than consolidating.
10. **[Iter2]** For RCT and RCT follow-up studies, include an ethics/IRB approval statement and informed consent statement in the Methods section. Most journals require this, and omitting it is a structural gap.
11. **[Iter2]** For Kaplan-Meier survival analyses, describe censoring criteria and include number-at-risk at key time points in figure legends when this information is available in the source.
12. **[Iter3]** For database/claims studies, create a dedicated "Outcome Definition" subsection in Methods that explicitly lists all ICD codes used, the rationale for code selection, and how codes map to clinical entities. This enhances reproducibility and transparency.
13. **[Iter3]** When Table 1 data is incomplete (exact percentages unavailable), use directional indicators ("Significantly higher," "Matched") with p-values rather than leaving cells empty or fabricating values. Acknowledge the limitation in a table footnote.

## Content Rules
1. Introduction should establish clinical significance with epidemiological data
2. Methods should specify study design, participants, interventions, outcomes, and statistics
3. Results should present data in logical order: demographics -> primary -> secondary outcomes
4. Discussion should compare findings with at least 3-4 relevant prior studies
5. Limitations section should be balanced (acknowledge but not undermine findings)
6. **[Iter1]** Always include specific measurement instrument names and models (e.g., "Topcon KR-800 autorefractor"), measurement protocols, and calculation formulas (e.g., "SE = sphere + 0.5 x cylinder") in the Methods section. These are essential for reproducibility.
7. **[Iter1]** Include operational details of the screening/referral system that explain study findings, such as the type of referral notice, presence or absence of follow-up reminders, and screening frequency.
8. **[Iter1]** When the original paper compares findings to international benchmarks (e.g., compliance rates in other countries), include these comparisons in the Discussion to contextualize results.
9. **[Iter1]** Include ALL limitations mentioned in the original paper. Do not selectively omit limitations. Pay special attention to potential confounders from external events (e.g., COVID-19 pandemic effects during the study period).
10. **[Iter1]** Include separate Strengths enumeration in the Discussion. List specific methodological strengths (sample size, follow-up duration, statistical approaches, geographic representativeness).
11. **[Iter2]** When the full reference list is unavailable, structure the Discussion to explicitly note which comparisons come from the study's own prior publications versus general literature ranges. Acknowledge the citation limitation transparently rather than omitting context entirely.
12. **[Iter2]** For surgical comparison studies, include a dedicated Discussion paragraph comparing revision/reoperation rates and timing with published benchmarks from other surgical series.
13. **[Iter2]** When baseline characteristics show important between-group differences (e.g., visual field severity, disease stage), explicitly discuss these as potential confounders in the Limitations section, even if the original paper does not emphasize them.
14. **[Iter3]** For population-based database studies, the Discussion must include a paragraph specifically addressing surveillance/detection bias -- the possibility that the exposed group receives more frequent clinical encounters leading to higher detection of the outcome. This is a critical methodological consideration for claims-based research.
15. **[Iter3]** When comparing outcome subtypes (e.g., AMD subtypes), explicitly discuss biological plausibility for differential associations using shared pathogenic mechanisms (e.g., VEGF pathways for exudative AMD vs. DR neovascularization).
16. **[Iter3]** Include at least one quantitative comparison with prior literature in the Discussion (e.g., "A prior study reported HR 3.89 for nonexudative AMD"). Do not fabricate study details but reference verified findings from the search.

## Style Rules
1. Use formal academic English throughout
2. Past tense for Methods and Results
3. Present tense for established facts and Discussion generalizations
4. Use hedging language appropriately: "suggests", "may indicate", "appears to"
5. Avoid first person; use passive voice or "the present study"
6. Reference tables/figures as "Table 1", "Figure 1" in text
7. Report exact p-values when possible (e.g., P=0.003 not P<0.05)
8. Use standard ophthalmology abbreviations (VA, IOP, OCT, etc.) after first defining them
9. **[Iter1]** Keep Results strictly descriptive. Report numbers, statistical tests, P-values, and confidence intervals without interpretive commentary. Phrases like "indicating relative refractive stability" or "demonstrating a significant protective effect" belong in the Discussion, not Results.
10. **[Iter1]** For retrospective cohort studies, use aim/objective language (e.g., "The study aimed to investigate...") rather than hypothesis language (e.g., "It was hypothesized that..."). Formal hypothesis statements are appropriate for prospective experimental or interventional studies.
11. **[Iter2]** In the Results section, use ZERO interpretive language. Avoid phrases like "indicating that," "suggesting that," or "demonstrating that" when describing data. Simply report the numbers, tests, and P-values. All inference belongs in the Discussion.
12. **[Iter3]** In administrative database studies, always specify the exact database version used (e.g., "LHID 2000" not just "LHID") and describe the sampling methodology (random sampling from registry) in the Data Source section.
13. **[Iter3]** When reporting hazard ratios for multiple outcome subtypes, present a summary comparison paragraph or summary table in Results showing all aHRs side by side to facilitate pattern recognition across subtypes.

## Blind Writing / Anti-Cheating Rules
1. **[Iter4-pre]** The extracted data bundle is anonymized: it contains NO paper title, author names, journal name, DOI, or identifiers. The draft writer must write purely from the data provided.
2. **[Iter4-pre]** Do NOT attempt to identify the original paper from data patterns, sample sizes, effect sizes, or study design. Even if recognized, write as if the study is entirely novel.
3. **[Iter4-pre]** Use a descriptive working title based on the study content (e.g., "Association Between X and Y: A Retrospective Cohort Study"), NOT the original paper's title.
4. **[Iter4-pre]** Use placeholders for author names ("[Author et al.]") and institutions ("[Institution]"). Do NOT fabricate these.

## Technical Rules
1. Report confidence intervals alongside p-values when available
2. Specify units for all measurements (mmHg, logMAR, etc.)
3. Use consistent decimal places throughout
4. Report effect sizes when possible
5. Present baseline characteristics comprehensively in Table 1
6. **[Iter1]** CRITICAL: Cross-check every numerical value against the source data before finalizing. Verify group sizes, percentages, incidence rates, and all statistical test results are exactly correct. Never interpolate, estimate, or round group sizes. Numerical accuracy is the single most important quality criterion.
7. **[Iter1]** When a paper presents results for multiple analytic subgroups (e.g., "all children," "high-risk group," "myopia group"), maintain strict separation of their data. Label each subgroup clearly and never transpose values between groups. Create a verification checklist mapping each reported value to its correct subgroup.
8. **[Iter1]** Report BOTH unadjusted and adjusted effect estimates when both are present in the source. This demonstrates the impact of confounders and enhances analytical transparency.
9. **[Iter1]** Always name the specific statistical software and version number (e.g., "R software version 4.1.0"). Never use vague phrases like "appropriate statistical software."
10. **[Iter1]** When Cox proportional hazard models are used, always describe how the proportional hazards assumption was tested (e.g., Schoenfeld residuals). Include all model assumption verification procedures mentioned in the source.
11. **[Iter1]** CRITICAL: Never fabricate or generate references. Only include citations that are explicitly present in and extractable from the source paper. If the reference list is unavailable, acknowledge this limitation rather than generating plausible-looking citations.
12. **[Iter3]** For matched cohort studies, explicitly report both the matching variables (confirming balance via p-values) AND the unmatched covariates (showing where imbalances exist) in the baseline characteristics description. This dual reporting clarifies which confounders required statistical adjustment versus those controlled by design.
13. **[Iter3]** When unadjusted hazard ratios are available in the source but adjusted HRs are the primary result, report BOTH to show the impact of confounding adjustment. If unadjusted HRs are unavailable from extraction, note this explicitly rather than silently omitting them.

## Lessons Learned
### Iteration 1 (Myopia/Ophthalmic Services Cohort Study)
**Key finding**: The draft scored 5.2/10 overall. While prose quality and readability were strong (7.4/10), accuracy was the critical weakness (4.8/10).

**Top 3 Strengths of Draft:**
1. Well-structured Introduction with classic funnel progression
2. Strong sentence-level readability and coherent narrative flow
3. Good use of statistical terminology

**Top 3 Critical Failures:**
1. Systematic numerical errors in group sizes (Tardily: 1,012 vs. correct 1,215; Timely: 315 vs. correct 112), propagated through every section
2. Data conflation between analytic subgroups (SE progression "all children" values attributed to "high-risk group")
3. Missing methodological specificity (instruments, formulas, protocols, software) that undermines reproducibility

**Meta-lesson**: Prose fluency can mask factual inaccuracy. Always prioritize data verification over stylistic polish. A paper with correct numbers and plain prose is far better than an eloquent paper with wrong numbers.

### Iteration 2 (TVC Trabeculectomy vs Canaloplasty 11-Year RCT Follow-Up)
**Key finding**: The draft scored 8.5/10 overall, a major improvement from Iteration 1 (5.2/10). Numerical accuracy was 100% (34/34 data points verified correct).

**Top 3 Strengths of Draft:**
1. Perfect numerical accuracy -- zero errors across 34 verified data points (dramatic improvement from Iter1)
2. Comprehensive Results section covering all outcome domains with appropriate statistical detail
3. Well-structured Discussion with 6+ thematic paragraphs, separate Strengths and Limitations sections

**Top 3 Weaknesses:**
1. Incomplete reference list (only 1 of ~20-30 citations extractable) -- limits scholarly context in Discussion
2. Missing baseline demographics (age, sex) that were likely in original Table 1 but not extractable from web
3. Discussion lacks breadth of international comparisons beyond the original 2-year TVC data

**Meta-lesson**: The Iter1 rules on numerical verification and reference fabrication prevention worked extremely well. The remaining gaps are largely extraction-limited (incomplete web access to full tables and reference lists) rather than drafting errors. Future iterations should focus on deeper Discussion development and broader literature context when extraction permits.

### Iteration 3 (DR-AMD Taiwan NHIRD Retrospective Cohort Study)
**Key finding**: The draft scored 8.7/10 overall, a modest improvement from Iteration 2 (8.5/10). Numerical accuracy remained at 100% (17/17 data points verified correct).

**Top 3 Strengths of Draft:**
1. Perfect numerical accuracy (17/17 verified data points correct) -- maintains 100% accuracy record from Iteration 2 across a different study design
2. Well-developed Discussion with 7 thematic subsections exceeding the 5-paragraph guideline minimum, including verified prior literature comparisons and separate Strengths section
3. Comprehensive Limitations section faithfully covering all 5 original limitations with clinically specific expansions including surveillance bias

**Top 3 Weaknesses:**
1. Incomplete Table 1 data (exact comorbidity percentages unavailable from web extraction) -- uses directional descriptors instead
2. Missing unadjusted hazard ratios -- only adjusted HRs were extractable, preventing demonstration of confounding adjustment impact
3. No formal numbered reference list -- Discussion references studies by description only, limiting scholarly completeness

**Meta-lesson**: The pipeline now reliably produces 100% numerically accurate drafts across different study types (RCT follow-up in Iter2, retrospective cohort in Iter3). The ceiling on improvement is primarily determined by extraction completeness rather than drafting quality. Key advances in Iter3: (1) structured abstracts with quantitative results, (2) deeper Discussion with verified international comparisons, (3) surveillance bias addressed for database studies. The 9 new rules focus on database/claims study-specific considerations that were not covered by Iter1-2 rules, which were oriented toward prospective/screening studies and RCTs.
