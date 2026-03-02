# Paper Writing Skills Progress

## Score Trend
| Iteration | Paper | Accuracy | Completeness | Logic | Readability | Structure | Clinical | Overall |
|-----------|-------|----------|--------------|-------|-------------|-----------|----------|---------|
| 1         | Lyu 2024 (Myopia/Referral) | 4.8 | 5.6 | 7.2 | 7.4 | 6.4 | 5.8 | **5.2** |
| 2         | TVC Study 11yr (Glaucoma Surgery) | 9.0 | 7.3 | 9.0 | 8.9 | 9.0 | 7.9 | **8.5** |
| 3         | DR-AMD Taiwan NHIRD (Retina) | 9.2 | 7.7 | 9.0 | 8.8 | 9.1 | 8.3 | **8.7** |

## Summary After 3 Iterations
- **Total improvement**: 5.2 -> 8.7 (+3.5 points, +67%)
- **Total rules accumulated**: 30 (15 from Iter1, 6 from Iter2, 9 from Iter3)
- **Numerical accuracy**: 0% (Iter1) -> 100% (Iter2) -> 100% (Iter3)
- **Primary bottleneck**: Web extraction completeness (tables, references), not drafting quality

## Iteration 1
- **Paper**: Lyu et al. (2024) "Impact of ophthalmic clinical service use in mitigating myopia onset and progression in preschool children" - BMC Ophthalmology 24, 221
- **Quality Score**: 5.2/10
- **Key Gaps**:
  - Critical numerical inaccuracies (group sizes wrong)
  - Data conflation between analytic subgroups
  - Under-developed Discussion, missing methodological detail
  - Fabricated references (22 AI-generated citations)
- **Strengths**: Strong Introduction structure, High readability
- **New Rules Added**: 15 (5 high, 9 medium, 1 low)
- **Key Lesson**: Prioritize data verification over stylistic polish.

## Iteration 2
- **Paper**: Verma-Fuehring et al. (2025) "Long-term outcomes of trabeculectomy versus canaloplasty in open-angle glaucoma – an 11-year follow-up" - BMC Ophthalmology
- **Quality Score**: 8.5/10 (+3.3 improvement)
- **Key Improvements**:
  - 100% numerical accuracy (34/34 data points correct)
  - No fabricated references
  - Instrument names and protocols included
  - Results kept strictly descriptive
  - Discussion with 6+ thematic paragraphs
- **Remaining Gaps**: Incomplete references, missing baseline demographics, limited international comparisons
- **New Rules Added**: 6
- **Key Lesson**: Web extraction limitations primarily affect reference completeness and table data.

## Iteration 3
- **Paper**: Lin et al. (2024) "The Association between Diabetic Retinopathy and Macular Degeneration: A Nationwide Population-Based Study" - Biomedicines (PMC11047965)
- **Quality Score**: 8.7/10 (+0.2 improvement)
- **Key Improvements**:
  - 100% numerical accuracy maintained (17/17 correct)
  - Discussion expanded to 7 thematic subsections (up from 6)
  - Better integration of verified prior literature (2018 Diabetes Care study, Kailuan Eye Study)
  - Comprehensive Limitations (5 points including surveillance bias)
  - Structured Abstract with quantitative results
  - Dedicated Ethics Statement subsection
- **Remaining Gaps**:
  - Incomplete Table 1 (exact comorbidity percentages not extractable)
  - Missing unadjusted hazard ratios
  - No formal numbered reference list
- **New Rules Added**: 9
- **Key Lesson**: Pipeline now reliably produces 100% accurate drafts across study designs. Score ceiling determined by extraction depth, not methodology.
