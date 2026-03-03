# Iteration Runner Guide

## How to Run an Iteration

Each iteration follows these 4 phases:

### Phase 1: Paper Search
```
Use Agent tool (subagent_type="general-purpose") with paper-search skill.
Input: iteration number, list of previously used papers
Output: papers/iteration_{N}/original/ files
```

### Phase 2: Data Extraction
```
Use Agent tool (subagent_type="general-purpose") with data-extraction skill.
Input: papers/iteration_{N}/original/paper_fulltext.txt
Output: papers/iteration_{N}/extracted/ files
```

### Phase 3: Draft Writing
```
Use Agent tool (subagent_type="general-purpose") with draft-writing skill.
CRITICAL: Only provide extracted_data_bundle.md and writing-guidelines.md
DO NOT provide original paper.
Input: papers/iteration_{N}/extracted/extracted_data_bundle.md
Output: papers/iteration_{N}/draft/ files
```

### Phase 4: Comparison & Skill Refinement
```
Use Agent tool (subagent_type="general-purpose") with draft-comparison skill.
Input: original paper + draft paper + current writing-guidelines.md
Output: papers/iteration_{N}/comparison/ files + updated writing-guidelines.md
```

## Iteration Tracking
- Progress logged to papers/progress_log.md
- Report to user every 3 iterations
- Quality scores tracked across iterations
