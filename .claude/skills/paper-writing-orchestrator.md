# Paper Writing Orchestrator (論文執筆オーケストレータ)

## Purpose
Orchestrate the iterative paper-writing improvement loop. This is the main entry point for the paper writing skills system.

## Process Overview

```
┌─────────────────────────────────────────────────────┐
│                  Orchestrator Loop                    │
│                                                       │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐        │
│  │  Paper    │───>│  Data    │───>│  Draft   │        │
│  │  Search   │    │  Extract │    │  Writing │        │
│  └──────────┘    └──────────┘    └──────────┘        │
│                                       │               │
│                                       v               │
│  ┌──────────┐    ┌──────────────────────────┐        │
│  │  Update   │<──│  Compare Draft vs        │        │
│  │  Skills   │   │  Original Paper          │        │
│  └──────────┘    └──────────────────────────┘        │
│       │                                               │
│       └──── Next Iteration ──────────────>           │
│                                                       │
│  Report to user every 3 iterations                   │
└─────────────────────────────────────────────────────┘
```

## Instructions

### Initialization
1. Check current iteration number (look at existing `papers/iteration_*` directories)
2. Load current writing guidelines from `.claude/skills/writing-guidelines.md` if exists

### For Each Iteration

#### Phase 1: Paper Search (論文検索サブエージェント)
Launch a subagent (Agent tool, subagent_type="general-purpose") with the paper-search skill instructions:
- Search Europe PMC for an open-access ophthalmology paper
- Download and save to `papers/iteration_{N}/original/`
- Select a DIFFERENT paper than previous iterations

#### Phase 2: Data Extraction (データ抽出サブエージェント)
Launch a subagent with the data-extraction skill instructions:
- Extract Results, tables, figures from the downloaded paper
- Save to `papers/iteration_{N}/extracted/`
- Create the combined `extracted_data_bundle.md`

#### Phase 3: Draft Writing (ドラフト作成サブエージェント)
Launch a subagent with the draft-writing skill instructions:
- **CRITICAL**: This subagent must NOT have access to the original paper
- Provide ONLY the `extracted_data_bundle.md` and current `writing-guidelines.md`
- Save draft to `papers/iteration_{N}/draft/`

#### Phase 4: Comparison & Skill Refinement (比較・スキル改善サブエージェント)
Launch a subagent with the draft-comparison skill instructions:
- Compare draft with original paper
- Generate improvement rules
- Update `.claude/skills/writing-guidelines.md`
- Save comparison report to `papers/iteration_{N}/comparison/`

### Iteration Control

After each iteration:
1. Record iteration results in `papers/progress_log.md`
2. Check if iteration count is a multiple of 3
3. If yes: Report to user with:
   - Summary of last 3 iterations
   - Quality score trends
   - Key improvements made
   - Ask for user guidance on next steps
4. If no: Continue to next iteration automatically

### Progress Log Format

`papers/progress_log.md`:
```markdown
# Paper Writing Skills Progress

## Iteration 1
- Paper: [title]
- Journal: [journal]
- Quality Score: [X/10]
- Key Gaps: [list]
- New Rules Added: [count]

## Iteration 2
...

## Score Trend
| Iteration | Accuracy | Completeness | Logic | Readability | Structure | Clinical | Overall |
|-----------|----------|--------------|-------|-------------|-----------|----------|---------|
| 1         | X        | X            | X     | X           | X         | X        | X       |
```

### Stopping Criteria
- User requests stop
- Quality score reaches 8.0/10 or above consistently (3 consecutive iterations)
- Maximum 15 iterations unless user requests more
