# Draft Comparison & Skill Refinement (比較・スキル改善)

## Purpose
Compare the AI-generated draft with the original published paper, identify differences, and create/update writing skills to close the gap.

## Instructions

### Input
- Original paper: `papers/iteration_{N}/original/paper_fulltext.txt`
- Draft paper: `papers/iteration_{N}/draft/draft_paper.md`
- Current writing guidelines: `.claude/skills/writing-guidelines.md` (if exists)

### Step 1: Section-by-Section Comparison

For each section (Abstract, Introduction, Methods, Results, Discussion), evaluate:

#### A. Structure Analysis
- Paragraph count comparison
- Heading/subheading organization
- Overall flow and logical progression

#### B. Content Analysis
- Key points covered vs. missed
- Depth of discussion on each topic
- Accuracy of data presentation
- Appropriate vs. inappropriate inferences

#### C. Style Analysis
- Sentence length and complexity
- Use of transitions
- Hedging language usage
- Citation patterns (original cites literature; draft may not)
- Technical vocabulary usage
- Active vs. passive voice balance

#### D. Quality Metrics (score 1-10 for each)
- **Accuracy**: Are the facts and numbers correct?
- **Completeness**: Are all key findings discussed?
- **Logic**: Is the argumentation sound?
- **Readability**: Is it well-written and clear?
- **Structure**: Is the organization appropriate?
- **Clinical Relevance**: Are implications well-articulated?
- **Overall**: How close is it to publication quality?

### Step 2: Gap Analysis

Identify the top gaps between draft and original:
1. List specific weaknesses with examples
2. Categorize gaps as:
   - **Structural** (organization, section length, paragraph structure)
   - **Content** (missing context, insufficient background, weak discussion)
   - **Stylistic** (tone, vocabulary, sentence construction)
   - **Technical** (data presentation, statistical reporting, clinical terminology)

### Step 3: Generate Improvement Rules

For each identified gap, create a specific, actionable improvement rule:

```
Rule: [short name]
Category: [structural/content/stylistic/technical]
Problem: [what was wrong]
Example (Original): [excerpt from original]
Example (Draft): [excerpt from draft]
Fix: [specific instruction for improvement]
Priority: [high/medium/low]
```

### Step 4: Update Writing Guidelines

Read the current `.claude/skills/writing-guidelines.md` (create if doesn't exist).
Append new rules while keeping existing ones that are still relevant.
Remove or modify rules that proved unhelpful.

The writing-guidelines.md should have this structure:
```markdown
# Paper Writing Guidelines

## Iteration History
- Iteration N: [summary of changes]

## Structural Rules
[rules about paper structure]

## Content Rules
[rules about content depth and coverage]

## Style Rules
[rules about writing style]

## Technical Rules
[rules about technical/clinical writing]

## Lessons Learned
[accumulated insights from comparisons]
```

### Step 5: Save Comparison Report

Save to `papers/iteration_{N}/comparison/`:
- `comparison_report.md` - Full comparison analysis
- `gap_analysis.md` - Identified gaps and improvement rules
- `scores.json` - Numerical quality scores

### Output Format

Return a summary including:
- Overall quality score (average of all metrics)
- Top 3 strengths of the draft
- Top 3 areas for improvement
- Number of new rules added to writing guidelines
- Whether significant improvement was seen vs. previous iteration
