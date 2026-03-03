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
7. **TOOL RESTRICTION**: Do NOT use WebSearch or WebFetch tools at any point during draft writing. These tools could be used to identify the original paper from the data, which defeats the purpose of blind writing. All literature context for the Discussion must come from general medical/scientific knowledge (field-level facts, not specific paper recall). Do NOT cite specific papers — references will be added in a later phase (Phase 3.5).
8. **ORIGINALITY**: Write the Introduction and Discussion in your OWN words and structure. Do NOT replicate the structure, paragraph order, or phrasing of any known published paper. The goal is to test whether a good paper can be constructed independently from data alone — not to reproduce the original.

### Input
- Path to `papers/iteration_{N}/extracted/extracted_data_bundle.md` (anonymized — no identifying info)
- Current writing guidelines from `skills/writing-guidelines.md` (if it exists)

**DO NOT read**: `papers/iteration_{N}/original/` directory, `papers/iteration_{N}/extracted/paper_identity.json`, or any file containing the paper's title/authors/journal.

**NOTE**: No reference list is provided. Write the Discussion using general medical knowledge. Where you would normally cite a source, use placeholder markers like "[REF]". References will be independently discovered and added in Phase 3.5 after the draft text is finalized.

### Step 1: Analyze the Extracted Data

Read the extracted data bundle and identify:
- The main research question implied by the study design and results
- Key findings and their statistical significance
- The clinical/scientific significance of the results
- Logical flow for presenting the results

### Conciseness Rules (冗長性対策)
**The draft MUST be concise.** Published ophthalmology papers are typically tight and efficient. Follow these rules:
1. **Word count target**: Aim for a total word count within 95–115% of a typical published paper of this study type (~2,500–3,500 words). Do NOT exceed 115%.
2. **Introduction**: Maximum 3-4 paragraphs. Get to the study objective by paragraph 3. Do NOT over-elaborate general background.
3. **No redundancy**: Do NOT restate Results numbers in the Discussion unless you are interpreting or comparing them. Avoid repeating information across sections.
4. **Cut filler phrases**: Avoid "It is worth noting that", "It is important to mention that", "Interestingly,", "Of note,". Just state the fact directly.
5. **Hedging economy**: Use ONE hedging word per claim ("may suggest"), not chains ("it is possible that this could potentially suggest").
6. **Discussion**: Each paragraph should make ONE clear point. Combine related sub-points rather than giving each its own paragraph.

### Clinical Actionability Rules (臨床提言)
**The Conclusions MUST include specific, actionable clinical recommendations.**
1. **At least ONE concrete recommendation**: e.g., "Patients with [condition X] should undergo [screening Y] at [interval Z]" or "Clinicians should consider [intervention] when [threshold] is reached."
2. **Avoid vague endings**: Do NOT end with only "Further research is needed." If future research is mentioned, it must be in addition to (not instead of) a concrete clinical takeaway.
3. **Discussion clinical implications**: Include a dedicated paragraph in the Discussion that explicitly discusses how the findings should influence clinical practice, mentioning specific patient subgroups, screening intervals, or treatment decisions where the data supports it.

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

Write a Discussion section (5-6 paragraphs, each making ONE clear point) that:
1. Summarize the main findings (1 paragraph, concise)
2. Compare with previous literature using general knowledge (1-2 paragraphs)
3. Discuss strengths (factual, without evaluative adjectives) and limitations (1 paragraph)
4. **Clinical implications** (1 dedicated paragraph): Explicitly state how findings should influence clinical practice — mention specific patient subgroups, screening recommendations, or treatment considerations
5. **Conclusions** (standalone subsection): Include at least ONE specific, actionable clinical recommendation. Do NOT end with only "further research is needed"

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
