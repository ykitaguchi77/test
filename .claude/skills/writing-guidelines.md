# Paper Writing Guidelines

## Iteration History
- Iteration 0: Initial guidelines (default)
- Iteration 1: Added 15 rules from myopia/ophthalmic clinical services cohort study comparison (2026-03-01)
- Iteration 2: Added 6 rules from TVC trabeculectomy vs canaloplasty 11-year RCT follow-up (2026-03-01)
- Iteration 3: Added 9 rules from DR-AMD Taiwan NHIRD retrospective cohort study (2026-03-02)
- Iteration 4: Added 7 rules from anti-VEGF intravitreal injections and optic nerve head parameters cross-sectional study (2026-03-03)
- Iteration 5: Added 6 rules from DR progression in primary care longitudinal cohort study (2026-03-03)
- Iteration 6: Added 7 rules from keratoconus risk factors case-control study (All of Us database) (2026-03-03)

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
14. **[Iter4]** Keep the Abstract to 200-250 words. Include only essential elements: study design, sample size, primary outcomes, key instrument, and principal results. Reserve treatment protocol specifics (regimen type, paracentesis details), software version numbers, and sector enumeration for the Methods section.
15. **[Iter4]** Aim for the draft to be within 130-150% of the typical word count for the study type and journal. If the draft significantly exceeds this range, systematically review each section for redundant phrasing, repetitive concepts, and speculative content that could be consolidated.
16. **[Iter5]** After completing the Discussion, review for redundancy between the Discussion opening summary paragraph and the Conclusions. The Conclusions should synthesize implications and future directions, NOT repeat the same numerical findings already stated in the Discussion summary. If a finding appears in both, remove it from one location.
17. **[Iter6]** When the extracted data bundle indicates the study aims to identify novel risk factors or associations, consider leading the Discussion with the novel findings rather than the statistically strongest associations. If the study's stated purpose is to explore "new links" or "novel risk factors," the Discussion should foreground these novel contributions. Known confirmatory findings can be discussed subsequently as validation of the study methodology.

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
17. **[Iter4]** When introducing clinical facts from general field knowledge not present in the extracted data bundle, use hedging language and [REF] placeholders. Avoid citing specific numerical values from memory (e.g., ">40 mmHg," "0.05 mL") without a verifiable source. Prefer qualitative descriptions unless a cited source supports the number.
18. **[Iter4]** When specific study references are unavailable, organize Discussion literature comparisons by study design type, population characteristics, and finding direction (e.g., "The majority of cross-sectional studies in treatment-experienced patients found no RNFL reduction") rather than using vague "some studies" or "several studies" phrasing.
19. **[Iter4]** When a primary outcome shows a null result, the Discussion must explicitly address whether the exposure level in the study cohort (e.g., mean injection count, treatment duration) may be below a threshold needed to detect the effect. This is standard dose-response reasoning and strengthens the interpretation.
20. **[Iter5]** When the extracted data bundle references supplementary materials (supplementary tables, supplementary figures), include these references in the draft text at the appropriate locations, even if the supplementary content itself is not available. Use the format "(Supplementary Table X)" or "(Supplementary Fig. X)" as placeholders. This signals to the reader that additional data exists.
21. **[Iter5]** When the study analyzes natural history or progression rates, the Discussion should include a paragraph explicitly noting that sham/control arms of relevant clinical trials serve as important benchmarks for comparison. Frame this as: "Comparisons to progression rates observed in the control arms of clinical trials in similar patient populations could further contextualize these findings [REF]." This maintains scholarly completeness without fabricating specific citations.
22. **[Iter5]** When writing about screening or prevention studies, the Discussion/Conclusions should reference the relevant clinical guideline framework (e.g., AAO, ADA, ICO guidelines) using general knowledge, even without specific citations. For example: "Current guidelines recommend initial DR screening within 5 years of type 1 DM diagnosis and at diagnosis for type 2 DM [REF]." This anchors the study's findings in actionable clinical practice.
23. **[Iter5]** When the Discussion compares findings to prior literature and specific study data is unavailable, structure the comparison by noting the expected direction and magnitude from general field knowledge. For example: "Prior epidemiologic studies have consistently reported substantially higher prevalence of DR in type 1 compared with type 2 DM populations [REF]." This is more informative than simply stating results are "consistent with prior reports."
24. **[Iter6]** When the extracted data bundle provides details about the most common specific agent or indication within a grouped medication or exposure variable (e.g., "most common estrogen-containing medication was oral contraceptive pills"), include this detail in either the Results or Discussion. Such specifics enhance clinical interpretability and should not be omitted as minor detail.
25. **[Iter6]** When the extracted data bundle mentions that supplementary or appendix tables contain additional analyses (e.g., univariable results, ungrouped sensitivity analyses), reference these in the Results section using the format "Additional results are presented in Appendix Table X" even if the appendix data itself was not extractable. This complements the existing [Iter5] rule on supplementary material references and signals analytical completeness.
26. **[Iter6]** When the study population's average age or disease duration suggests participants are well past the typical onset/progression window for the condition under study, include this as a specific limitation. Note the implications for interpreting risk factor associations (e.g., factors may be correlates of established disease rather than drivers of onset/progression). This is clinically important for conditions with age-dependent natural history.
27. **[Iter6]** The Conclusions section must include at least one explicit clinical action statement (e.g., "Clinicians managing patients with [condition X] should be aware of [risk factor Y] to facilitate earlier screening and diagnosis"). Avoid purely academic conclusions that only call for "further investigation" without a concrete clinical takeaway.

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
14. **[Iter6]** Limit speculative mechanistic discussion to 2-3 sentences per topic. When introducing pathophysiological hypotheses from general knowledge, use one sentence to state the mechanism and one to note its limitations. Avoid multi-sentence elaborations on mechanisms that the study did not directly test. If the extracted data bundle does not provide cited evidence for a mechanism, keep it brief with a [REF] placeholder.

## Blind Writing / Anti-Cheating Rules
1. **[Iter4-pre]** The extracted data bundle is anonymized: it contains NO paper title, author names, journal name, DOI, or identifiers. The draft writer must write purely from the data provided.
2. **[Iter4-pre]** Do NOT attempt to identify the original paper from data patterns, sample sizes, effect sizes, or study design. Even if recognized, write as if the study is entirely novel.
3. **[Iter4-pre]** Use a descriptive working title based on the study content (e.g., "Association Between X and Y: A Retrospective Cohort Study"), NOT the original paper's title.
4. **[Iter4-pre]** Use placeholders for author names ("[Author et al.]") and institutions ("[Institution]"). Do NOT fabricate these.
5. **[Iter4-pre]** Do NOT use WebSearch or WebFetch tools during draft writing. All literature context must come from the verified reference list or general field-level knowledge.
6. **[Iter4-pre]** Write the Introduction and Discussion in your OWN structure and words. Do NOT replicate the paragraph order, rhetorical structure, or phrasing of any known published paper. The comparison skill will evaluate originality alongside accuracy.

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
14. **[Iter4]** When tabulated results are incomplete for certain analyses (e.g., sector-level p-values available for one outcome but not another), include an explicit table footnote explaining the scope of available data rather than using summary rows that obscure the distinction between "not significant" and "not reported."
15. **[Iter4]** In the Study Strengths subsection, state methodological facts without evaluative adjectives or inferred quality claims. Write what was done (e.g., "Manual correction of segmentation errors was performed by a trained physician") rather than what it achieves (e.g., "enhances the reliability and accuracy"). Let the reader draw the quality inference.
16. **[Iter5]** When the extracted data bundle flags a numerical discrepancy between sources (e.g., text vs. table vs. figure), add a footnote or parenthetical note in the draft acknowledging the discrepancy. For example: "41,977 eyes (note: Figure 2 caption reports 41,997 eyes; Table 1 value used throughout)." Transparent handling of discrepancies is preferable to silent inconsistency.
17. **[Iter6]** When the extracted data bundle specifies the clinical terminology or classification system used for case identification (e.g., SNOMED-CT, ICD-10-CM, Read codes), name the system explicitly in the Methods. Do not generalize to "standardized medical terminology" if a specific coding system is named in the bundle.

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

### Iteration 4 (Anti-VEGF Injections and Optic Nerve Head Parameters Cross-Sectional Study)
**Key finding**: The draft scored 8.9/10 overall, continuing the upward trend (5.2 -> 8.5 -> 8.7 -> 8.9). Numerical accuracy remained at 100% (28/28 data points verified correct). First iteration with blind integrity testing: PASS.

**Top 3 Strengths of Draft:**
1. Perfect numerical accuracy (28/28 verified data points correct) -- maintains 100% accuracy streak for the 3rd consecutive iteration across a new study design (cross-sectional)
2. Superior structural organization compared to original: 6 Methods subsections, 5 formal tables in Results, and themed Discussion subsections with clear headings improve readability significantly
3. Clean blind integrity: zero knowledge leakage (0/18 original-specific items), zero verbatim phrase overlap (0/19 phrases tested), and substantially different organizational structure from original

**Top 3 Weaknesses:**
1. Limited Discussion depth -- unable to match the original's specific literature comparisons (5+ named studies) and VEGF mechanistic detail because these were not in the extracted data bundle (extraction-limited gap)
2. General-knowledge additions (lamina cribrosa, 0.05 mL bolus, >40 mmHg IOP spikes) are factually accurate but introduce unverifiable numerical claims that carry risk if wrong
3. Verbosity (60% longer than original at 2715 vs 1698 words) -- some sections could be more concise, particularly the Abstract (282 vs 210 words) and Conclusions (130 vs 60 words)

**Meta-lesson**: This is the first iteration using blind writing with anonymized data bundles. The draft writer successfully produced an independently structured paper with no evidence of accessing the original. The key remaining improvement areas are: (1) controlling general-knowledge numerical claims that lack citations, (2) structuring literature comparisons more specifically even without named references, and (3) maintaining conciseness. The 7 new rules address these gaps. The overall pipeline now consistently produces high-quality, numerically accurate drafts across 4 different study designs (cohort, RCT follow-up, retrospective database, cross-sectional).

### Iteration 5 (DR Progression in Primary Care Longitudinal Cohort Study)
**Key finding**: The draft scored 9.0/10 overall, the highest score yet (5.2 -> 8.5 -> 8.7 -> 8.9 -> 9.0). Numerical accuracy was 100% (50/50 data points verified correct). Second iteration with blind integrity testing: PASS.

**Top 3 Strengths of Draft:**
1. Perfect numerical accuracy (50/50 verified data points correct) -- maintains 100% accuracy streak for the 4th consecutive iteration, with the largest number of data points verified to date
2. Excellent structural originality: Introduction expanded to 3 paragraphs (vs. original's 2), Methods reorganized into 7 subsections (vs. original's 4), Discussion structured into 9 themed subsections (vs. original's 3 paragraphs) -- all independently constructed
3. Clean blind integrity: zero knowledge leakage, zero suspicious phrasing overlap, independent organizational structure throughout. Second consecutive PASS on blind integrity testing.

**Top 3 Weaknesses:**
1. Verbosity (~35-40% longer than original) with redundancy between Discussion opening summary and Conclusions section -- the same numerical findings appear in both
2. Missing clinical trial benchmark comparisons (PANORAMA, DRCR Protocol W sham arm data) that would anchor the Discussion in therapeutic context -- extraction-limited but could have been addressed with general framing
3. Missing supplementary material references and clinical guideline framework connections in Conclusions that the original includes

**Meta-lesson**: The pipeline now achieves 9.0/10 with the 5th consecutive paper across 5 study designs (prospective cohort, RCT follow-up, retrospective database, cross-sectional, longitudinal observational). The 100% numerical accuracy streak is maintained for the 4th iteration. The primary improvement opportunities are: (1) controlling verbosity by eliminating Discussion-Conclusions redundancy, (2) anchoring natural history studies against clinical trial benchmarks even without specific citations, (3) consistently referencing supplementary materials and clinical guidelines. The 6 new rules address these specific gaps. The scoring ceiling is increasingly determined by Discussion depth and clinical contextualization rather than accuracy or structural issues.

### Iteration 6 (Keratoconus Risk Factors Case-Control Study, All of Us Database)
**Key finding**: The draft scored 9.1/10 overall, a new high score (5.2 -> 8.5 -> 8.7 -> 8.9 -> 9.0 -> 9.1). Numerical accuracy was 100% (50/50 data points verified correct). Third iteration with blind integrity testing: PASS.

**Top 3 Strengths of Draft:**
1. Perfect numerical accuracy (50/50 verified data points correct) -- maintains 100% accuracy streak for the 5th consecutive iteration, matching the record data point count from Iteration 5
2. Excellent structural organization: Introduction with 4 well-crafted paragraphs using epidemiology-first funnel structure, Methods with 4 formal subsections, Discussion with 7 themed subsections including dedicated Strengths and Limitations -- all independently structured from the original
3. Clean blind integrity for the third consecutive iteration: zero knowledge leakage, zero verbatim phrasing overlap, substantially different Discussion topic ordering (OSD-first vs. original's estrogen-first), and independent mechanistic reasoning throughout

**Top 3 Weaknesses:**
1. Discussion verbosity (~50-60% longer than original) with multi-sentence speculative mechanistic elaborations on topics the study did not directly test (AGEs, leptin, floppy eyelid syndrome) -- general knowledge used expansively rather than concisely
2. Missing clinically actionable Conclusions: draft calls only for "further investigation" whereas the original provides a direct clinical recommendation ("providers should be aware of all disease risk factors to aid in early diagnosis and intervention")
3. Missing fine-grained clinical details: specific medication identities within grouped variables (oral contraceptive pills as most common estrogen-containing medication), disease stage considerations for the older study population, and appendix/supplementary analysis references

**Meta-lesson**: The pipeline achieves 9.1/10 across 6 consecutive papers spanning 6 study designs (prospective cohort, RCT follow-up, retrospective database, cross-sectional, longitudinal observational, case-control). The 100% numerical accuracy streak is maintained for the 5th iteration. Three consecutive blind integrity PASSes confirm the blind writing protocol is robust. The primary remaining improvement targets are: (1) tighter mechanistic discussion -- brevity over elaboration when the study lacks direct mechanistic data, (2) clinically actionable conclusions rather than purely academic "further research needed" language, and (3) capturing fine-grained clinical details (specific agents, disease stage implications) that differentiate a thorough draft from a very good one. The 7 new rules address these gaps. The scoring improvement rate is slowing (0.1 per iteration), suggesting the pipeline is approaching its ceiling without fundamentally different extraction or contextual inputs.
