# Gap Analysis and Improvement Rules

## Paper: Impact of Ophthalmic Clinical Service Use in Mitigating Myopia Onset and Progression in Preschool Children

---

## Top Gaps Identified

### Structural Gaps

1. **Abstract over-length**: Draft abstract (~350 words) is ~75% longer than original (~200 words), exceeding typical journal limits of 250-300 words.
2. **Missing standalone Conclusions section**: The original has a separate Conclusions section; the draft folds it into the Discussion's final paragraph.
3. **Missing standalone Strengths and Limitations sections**: The original separates these clearly; the draft compresses them into the Discussion body.
4. **Methods sub-section consolidation**: The draft merges Vision Screening Protocol, Refraction Measurements, and Definitions into other sections, losing granularity.
5. **Discussion under-developed**: The draft Discussion (~600 words) is approximately half the length of the original (~1,100 words), missing several key thematic sections.

### Content Gaps

6. **Incorrect group sizes (critical)**: Tardily group reported as 1,012 (should be 1,215); Timely group reported as 315 (should be 112). This is the single most damaging error.
7. **Incorrect high-risk cohort N**: Draft reports 4,443; original reports 2,437 for the High-risk/Non-myopia group.
8. **SE progression data conflation**: Draft attributes "all children" SE values (+0.07, -0.06, -0.14 D/year) to the "high-risk group" analysis section. Actual high-risk values are -0.28, -0.32, -0.36 D/year.
9. **Missing screening protocol details**: No mention of paper referral notices, lack of follow-up reminders, annual screening schedule.
10. **Missing instrument specification**: Topcon KR-800 autorefractor not mentioned; logMAR chart not mentioned.
11. **Missing SE calculation formula**: SE = sphere + 0.5 x cylinder not provided.
12. **Missing non-cycloplegic refraction detail in Methods**: Only mentioned in Limitations.
13. **Missing international compliance rate comparisons**: Original compares to US (30-70%) and East Asian (15-40%) rates.
14. **Missing COVID-19 as potential confounder**: Original mentions pandemic influence during 2015-2020 follow-up.
15. **Missing prevalence discussion theme**: Original devotes a full section to the 35.08% prevalence finding.
16. **Missing policy implications section**: Original has dedicated recommendations for Shanghai's screening and referral systems.
17. **Missing unadjusted hazard ratios**: Draft only reports adjusted HRs; original reports both.
18. **Missing baseline prevalence in Results**: 35.08% visual abnormalities, 13.98% high-risk, 21.1% myopia.
19. **Missing follow-up statistics**: Mean 5.00 +/- 0.94 years, 4.17 +/- 1.25 examinations.
20. **Missing statistical software specification**: "Appropriate statistical software" vs. "R software (version 4.1.0)".

### Stylistic Gaps

21. **Introduction over-elaboration**: Draft Introduction adds extensive global context not in original; while valuable, it shifts the paper's tone from focused clinical study to broader review.
22. **Abstract lacks original's directness**: Original abstract is concise and data-focused; draft is discursive.
23. **Hypothesis statement insertion**: Draft adds "It was hypothesized that..." -- not present in original and atypical for retrospective cohort study reporting.
24. **Interpretive language in Results**: Draft includes interpretive phrases ("indicating relative refractive stability") in Results; original keeps Results purely descriptive.

### Technical Gaps

25. **Missing Schoenfeld residuals mention**: Original specifies proportional hazards assumption testing.
26. **Missing GAM rationale detail**: Original explains non-normal distribution and non-linear relationship justifying GAM; draft mentions it briefly.
27. **Missing annual SE change calculation method**: Original specifies "difference in SE between consecutive screenings divided by the time interval."
28. **Fabricated references**: Draft includes 22 numbered references that appear to be AI-generated, mixing real citations with potentially incorrect attributions and details.

---

## Improvement Rules

### Rule 1: Verify All Numerical Data
```
Rule: numerical-accuracy
Category: technical
Problem: The draft contains multiple incorrect group sizes (Tardily: 1,012 vs. correct 1,215; Timely: 315 vs. correct 112; High-risk: 4,443 vs. correct 2,437), propagated consistently throughout the paper.
Example (Original): "Never group: N = 4,184 (75.92%); Tardily group: N = 1,215 (22.05%); Timely group: N = 112 (2.03%)"
Example (Draft): "Tardily (n = 1,012; 18.36%) ... Timely (n = 315; 5.72%)"
Fix: Cross-check every numerical value in the draft against the source data. Verify that group sizes, percentages, incidence rates, and statistical test results are exactly correct. Never interpolate or estimate group sizes.
Priority: high
```

### Rule 2: Preserve Subgroup Data Distinctions
```
Rule: subgroup-data-fidelity
Category: technical
Problem: The draft conflates SE progression data from different analytic subgroups. Values for "all children" (+0.07, -0.06, -0.14 D/year) were attributed to the "high-risk group" analysis, whose actual values were -0.28, -0.32, -0.36 D/year.
Example (Original): "High-Risk Group: Never: -0.32; Tardily: -0.36; Timely: -0.28 D/year (P = 0.006)" and separately "All Children: Never: -0.06; Tardily: -0.14; Timely: +0.07 D/year (P = 0.005)"
Example (Draft): "Among the high-risk group... The Timely group exhibited the slowest rate of myopic shift, with a mean annual SE change of 0.07 +/- 0.60 D/year"
Fix: When a paper presents results for multiple analytic subgroups (e.g., all children, high-risk, myopia group), maintain strict separation. Label each subgroup's data clearly and never transpose values between groups.
Priority: high
```

### Rule 3: Include Measurement Instruments and Protocols
```
Rule: instrument-specification
Category: content
Problem: The draft omits all measurement instrument names, screening protocol details, and calculation formulas that are essential for methodological reproducibility.
Example (Original): "Non-cycloplegic autorefraction was performed using a table-top autorefractor (Topcon KR-800) by trained technicians. Uncorrected distance visual acuity (UDVA) was recorded using a logMAR visual acuity chart. The spherical equivalent (SE) was calculated as the sphere plus half the cylinder (SE = sphere + 0.5 x cylinder)."
Example (Draft): [No equivalent section exists]
Fix: Always include specific instrument names, measurement protocols, and calculation formulas in Methods. Include a Vision Screening Protocol subsection and a Refraction Measurements subsection when these are present in the source paper.
Priority: high
```

### Rule 4: Report Both Unadjusted and Adjusted Effect Estimates
```
Rule: dual-effect-estimates
Category: technical
Problem: The draft only reports adjusted hazard ratios, omitting the unadjusted analysis that the original includes for transparency.
Example (Original): "Unadjusted: Tardily HR = 1.31 (1.10-1.55); Timely HR = 0.67 (~0.33-0.93). Adjusted: Tardily HR = 1.31 (1.10-1.55); Timely HR = 0.55 (0.33-0.93; P = 0.026)"
Example (Draft): Only reports adjusted HRs.
Fix: When both unadjusted and adjusted models are reported in the source, include both in the draft. This demonstrates the impact of confounders and enhances transparency.
Priority: medium
```

### Rule 5: Maintain Abstract Conciseness
```
Rule: abstract-brevity
Category: structural
Problem: The draft abstract (~350 words) substantially exceeds the original's length (~200 words) and typical journal limits (250-300 words). It includes excessive quantitative detail and epidemiological framing not in the original.
Example (Original): "Of the 5,511 preschool children (mean age, 5.25 years; 52.24% male) who received a referral recommendation, 1,327 (24.08%) sought clinical services at an ophthalmic hospital."
Example (Draft): Includes 5+ additional statistical results (HRs, median survival times, SE progression, subgroup mention) beyond what the original abstract reports.
Fix: Keep abstracts within 250-300 words. Report only the most essential results in the abstract (cumulative incidence by group, overall incidence rate). Save detailed HRs, survival times, and secondary outcomes for the Results section.
Priority: medium
```

### Rule 6: Include Separate Conclusions Section
```
Rule: standalone-conclusions
Category: structural
Problem: The draft integrates conclusions into the final paragraph of the Discussion, whereas the original has a clearly delineated, standalone Conclusions section.
Example (Original): Separate "CONCLUSIONS" section with distinct content.
Example (Draft): "In conclusion, this study demonstrated that..." as the final Discussion paragraph.
Fix: Create a standalone Conclusions section after the Discussion, matching the original paper's structure. This is standard for many journals and improves navigability.
Priority: medium
```

### Rule 7: Develop Discussion Proportionally
```
Rule: discussion-depth
Category: structural
Problem: The draft Discussion (~600 words) is approximately half the length of the original (~1,100 words), missing several key thematic areas: prevalence discussion, international compliance comparisons, detailed policy implications, and comprehensive strengths enumeration.
Example (Original): 5 numbered thematic sections + separate Strengths + separate Limitations covering prevalence, effectiveness, tardily group paradox, low compliance context, and policy implications.
Example (Draft): 3 paragraphs covering main findings, literature comparison, and combined strengths/limitations.
Fix: The Discussion should be the longest section of the paper. Structure it with at least 5 thematic paragraphs: (1) summary of key findings, (2) comparison with prior literature, (3) explanation of unexpected findings (e.g., Tardily group paradox), (4) clinical/policy implications, (5) study strengths. Follow with a separate Limitations section covering all acknowledged limitations from the source.
Priority: high
```

### Rule 8: Include Screening System Context in Methods
```
Rule: screening-context
Category: content
Problem: The draft omits the screening system's operational details: paper referral notices, absence of follow-up reminders (no phone calls or text messages), and annual screening schedule. These details are essential for understanding compliance patterns.
Example (Original): "Students who failed the screening would receive a paper referral notice, but they were not compelled to do so, nor did they receive further phone calls or text message reminders."
Example (Draft): [No equivalent content]
Fix: Include operational details of the screening and referral system, especially factors that explain compliance patterns. These contextual details are critical for interpreting the study's findings about referral timing.
Priority: medium
```

### Rule 9: Specify Statistical Software and Version
```
Rule: software-specification
Category: technical
Problem: The draft uses the vague phrase "appropriate statistical software" instead of naming the actual software and version used.
Example (Original): "All statistical analyses were performed using R software (version 4.1.0)"
Example (Draft): "All statistical analyses were performed using appropriate statistical software."
Fix: Always name the specific statistical software and version number. This is a basic reproducibility requirement for all quantitative research papers.
Priority: medium
```

### Rule 10: Avoid Interpretive Language in Results
```
Rule: results-objectivity
Category: stylistic
Problem: The draft inserts interpretive phrases into the Results section, such as "indicating relative refractive stability" and "demonstrating a significant protective effect." Results should present data without interpretation; interpretation belongs in the Discussion.
Example (Original): Results section presents numbers, P-values, and confidence intervals without interpretive commentary.
Example (Draft): "The Timely group exhibited the slowest rate of myopic shift, with a mean annual SE change of 0.07 +/- 0.60 D/year, indicating relative refractive stability."
Fix: Keep Results strictly descriptive. Report numbers, statistical tests, P-values, and confidence intervals. Move all interpretive statements to the Discussion.
Priority: medium
```

### Rule 11: Do Not Insert Hypothesis Statements in Retrospective Studies
```
Rule: no-hypothesis-retrospective
Category: stylistic
Problem: The draft includes "It was hypothesized that timely utilization of ophthalmic clinical services would be associated with reduced myopia incidence and slower refractive progression." Formal hypothesis statements are atypical for retrospective cohort studies, which are exploratory/observational.
Example (Original): "The study aimed to investigate the impact of ophthalmic clinical services on the onset and progression of myopia..."
Example (Draft): "It was hypothesized that timely utilization of ophthalmic clinical services would be associated with..."
Fix: For retrospective cohort studies, use aim/objective language rather than hypothesis language. Reserve hypothesis statements for prospective experimental or interventional studies.
Priority: low
```

### Rule 12: Include Assumption Testing in Statistical Methods
```
Rule: assumption-testing
Category: technical
Problem: The draft omits the Schoenfeld residuals test for the proportional hazards assumption, a critical methodological detail for Cox models.
Example (Original): "The proportional hazards assumption was tested using Schoenfeld residuals."
Example (Draft): [No mention of assumption testing]
Fix: When Cox proportional hazard models are used, always mention how the proportional hazards assumption was tested (typically Schoenfeld residuals). This demonstrates methodological rigor.
Priority: medium
```

### Rule 13: Include International Context in Discussion
```
Rule: international-comparison
Category: content
Problem: The draft omits the original's comparison of referral compliance rates to international benchmarks, which contextualizes the study's findings.
Example (Original): "The overall compliance rate of 24.08% is comparable to reports from other countries. Studies in the United States have reported school vision screening referral compliance rates ranging from 30% to 70%, while studies in other East Asian countries have reported rates of 15% to 40%."
Example (Draft): [No international comparison of compliance rates]
Fix: When the original paper compares its findings to international benchmarks, include these comparisons in the Discussion. They provide important context for interpreting study-specific results.
Priority: medium
```

### Rule 14: Do Not Fabricate or Guess References
```
Rule: reference-authenticity
Category: technical
Problem: The draft includes 22 numbered references that appear to be generated rather than extracted from the original paper. Some citations may correspond to real papers but with potentially incorrect details; others may be fabricated entirely.
Example (Original): The original paper's reference list was not available for full extraction.
Example (Draft): 22 references with specific authors, titles, journals, years, and page numbers.
Fix: Only include references that are explicitly present in the source paper. If the reference list is unavailable, note this limitation rather than generating plausible-looking citations. Never fabricate bibliographic data.
Priority: high
```

### Rule 15: Mention All Listed Limitations
```
Rule: complete-limitations
Category: content
Problem: The original lists 8 specific limitations; the draft covers approximately 5 and omits COVID-19 as a potential confounder, absence of robust referral system, and confounding by indication as a separate limitation.
Example (Original): "During the follow-up period from 2015 to 2020, there might have been unknown influences (such as the COVID-19 pandemic) affecting the study results"
Example (Draft): [No mention of COVID-19]
Fix: Include all limitations mentioned in the original paper. These represent the authors' own critical assessment and should not be selectively omitted.
Priority: medium
```

---

## Priority Summary

| Priority | Count | Rules |
|----------|:-----:|-------|
| High | 5 | numerical-accuracy, subgroup-data-fidelity, instrument-specification, discussion-depth, reference-authenticity |
| Medium | 8 | dual-effect-estimates, abstract-brevity, standalone-conclusions, screening-context, software-specification, results-objectivity, assumption-testing, international-comparison, complete-limitations |
| Low | 1 | no-hypothesis-retrospective |
