# Data Extraction Skill (論文データ抽出)

## Purpose
Extract structured information from the Results section, tables, and figures of a downloaded ophthalmology paper. This extracted data will be the ONLY information given to the draft-writing subagent.

## Instructions

### Input
- Path to the full-text paper (XML or text format) in `papers/iteration_{N}/original/`

### Step 1: Extract Results Section

Parse the paper and extract the complete Results section, including:
- All statistical findings (p-values, confidence intervals, odds ratios, etc.)
- All numerical data points
- All comparisons between groups
- Sample sizes and demographics mentioned in Results
- Any subgroup analyses

### Step 2: Extract Tables

For each table in the paper:
- Table number and title/caption
- Column headers
- All data cells (preserve exact numbers)
- Footnotes and legends
- Statistical annotations

Format each table as a structured markdown table.

### Step 3: Extract Figures

For each figure:
- Figure number and title/caption
- Legend text
- Any data labels visible in the description
- Type of figure (bar chart, scatter plot, Kaplan-Meier, forest plot, etc.)
- Key findings the figure illustrates

Note: Since we may not have image access, extract all textual information associated with figures.

### Step 4: Extract Study Design Summary

Create a minimal summary containing ONLY:
- Study type (RCT, cohort, case-control, cross-sectional, etc.)
- Primary and secondary outcomes
- Number of participants/eyes
- Follow-up period
- Key inclusion/exclusion criteria

### Step 5: Save Extracted Data

Save to `papers/iteration_{N}/extracted/`:
- `results_section.md` - Full Results text
- `tables.md` - All tables in markdown format
- `figures.md` - Figure descriptions and captions
- `study_design.md` - Minimal study design summary
- `extracted_data_bundle.md` - Combined file with all extracted data

### Output Format

The `extracted_data_bundle.md` should follow this structure:

```markdown
# Extracted Paper Data

## Study Design
[study type, outcomes, participants, follow-up]

## Results
[full results text]

## Tables
### Table 1: [title]
[markdown table]
...

## Figures
### Figure 1: [title]
[description and data]
...
```

### CRITICAL RULES
1. Do NOT include the Introduction, Discussion, or Abstract in the extracted data
2. Do NOT include the authors' interpretation or conclusions
3. Do NOT include Methods details beyond the minimal study design summary
4. The goal is to give the draft writer ONLY the raw findings so they must construct the narrative independently
