# Draft Writing Skill (ドラフト作成)

## Purpose
Write a complete research paper draft using ONLY the extracted data provided. This skill simulates writing a paper from scratch given only the results and study design.

## Instructions

### CRITICAL CONSTRAINT — BLIND WRITING
You have NO access to the original paper. You must write the paper using ONLY the extracted data bundle provided. Do NOT attempt to read or reference any files in the `original/` directory.

**ANTI-CHEATING RULES:**
1. The extracted data bundle has been anonymized — it contains NO paper title, author names, journal name, DOI, or other identifiers.
2. You MUST NOT attempt to identify the original paper from the data patterns, study design, or numerical results.
3. You MUST NOT use any prior knowledge about specific published papers. Write as if this is an entirely novel, unpublished study.
4. If you recognize the study from its data, you MUST ignore that recognition and write purely from the extracted data.
5. Do NOT include any specific paper title in the draft — use a descriptive working title based on the study content (e.g., "Association Between X and Y: A Retrospective Cohort Study").
6. Do NOT fabricate author names or institutional affiliations — leave placeholders like "[Author et al.]" and "[Institution]".
7. **TOOL RESTRICTION**: Do NOT use WebSearch or WebFetch tools at any point during draft writing. These tools could be used to identify the original paper from the data, which defeats the purpose of blind writing. All literature context for the Discussion must come from:
   - The verified reference list (`references_formatted.md`) if provided
   - General medical/scientific knowledge (field-level facts, not specific paper recall)
8. **ORIGINALITY**: Write the Introduction and Discussion in your OWN words and structure. Do NOT replicate the structure, paragraph order, or phrasing of any known published paper. The goal is to test whether a good paper can be constructed independently from data alone — not to reproduce the original.

### Input
- Path to `papers/iteration_{N}/extracted/extracted_data_bundle.md` (anonymized — no identifying info)
- Current writing guidelines from `skills/writing-guidelines.md` (if it exists)
- Path to `papers/iteration_{N}/extracted/references_formatted.md` (verified reference list, if available)

**DO NOT read**: `papers/iteration_{N}/original/` directory, `papers/iteration_{N}/extracted/paper_identity.json`, or any file containing the paper's title/authors/journal.

### Step 1: Analyze the Extracted Data

Read the extracted data bundle and identify:
- The main research question implied by the study design and results
- Key findings and their statistical significance
- The clinical/scientific significance of the results
- Logical flow for presenting the results

### Step 2: Write the Introduction

Write an Introduction section (3-4 paragraphs) that:
1. Establishes the clinical/scientific background and importance
2. Identifies the gap in current knowledge
3. States the purpose/objective of the study
4. The introduction should logically lead to why this study was conducted

### Step 3: Write the Methods

Write a Methods section based on the study design summary:
1. Study design and setting
2. Participants (inclusion/exclusion criteria)
3. Interventions or exposures
4. Outcome measures
5. Statistical analysis approach (infer from the statistical tests mentioned in Results)

### Step 4: Write the Results

Reorganize and present the results:
1. Baseline characteristics/demographics
2. Primary outcome results
3. Secondary outcome results
4. Subgroup analyses (if applicable)
5. Reference tables and figures appropriately

### Step 5: Write the Discussion

Write a Discussion section (4-5 paragraphs) that:
1. Summarize the main findings
2. Compare with previous literature (use general knowledge)
3. Discuss strengths and limitations
4. Discuss clinical implications
5. Conclusion

### Step 6: Write the Abstract

Write a structured abstract:
- Purpose/Objective
- Methods
- Results (key numbers)
- Conclusions

### Step 7: Save the Draft

Save to `papers/iteration_{N}/draft/`:
- `draft_paper.md` - Complete paper draft
- `draft_metadata.md` - Notes on writing decisions and assumptions made

### Writing Style Guidelines

Default guidelines (updated by comparison skill over iterations):
- Use formal academic English
- Use past tense for methods and results
- Use present tense for established facts and discussion
- Be concise but thorough
- Use appropriate hedging language ("suggests", "may indicate")
- Reference tables and figures in the text as "Table 1", "Figure 1"
- Follow IMRAD structure (Introduction, Methods, Results, And Discussion)
- Target journal: general ophthalmology

### Output
The complete draft paper in markdown format.
