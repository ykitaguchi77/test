# Paper Writing Orchestrator (論文執筆オーケストレータ)

## Purpose
Orchestrate the iterative paper-writing improvement loop. This is the main entry point for the paper writing skills system.

## Process Overview

```
┌───────────────────────────────────────────────────────────────┐
│                    Orchestrator Loop                           │
│                                                               │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐                │
│  │  Paper    │───>│  Data    │───>│ Reference│                │
│  │  Search   │    │  Extract │    │  Search  │                │
│  └──────────┘    │ (PDF+    │    └──────────┘                │
│                  │  Vision) │         │                        │
│                  └──────────┘         │                        │
│                       │               v                        │
│                       └──────>┌──────────┐                    │
│                               │  Draft   │                    │
│                               │  Writing │                    │
│                               └──────────┘                    │
│                                    │                           │
│                                    v                           │
│  ┌──────────┐    ┌──────────────────────────┐                │
│  │  Update   │<──│  Compare Draft vs        │                │
│  │  Skills   │   │  Original Paper          │                │
│  └──────────┘    └──────────────────────────┘                │
│       │                                                       │
│       └──── Next Iteration ──────────────>                   │
│                                                               │
│  Report to user every 3 iterations                           │
└───────────────────────────────────────────────────────────────┘
```

## Prerequisites

Ensure the following are installed (see `requirements.txt`):
```bash
pip3 install -r requirements.txt
```

Scripts available in `scripts/`:
- `download_pdf.py` — Download PDF from Europe PMC
- `extract_tables_from_pdf.py` — Extract tables using PyMuPDF
- `pdf_to_images.py` — Convert PDF pages to PNG for vision reading
- `search_pubmed.py` — Search PubMed for reference verification

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

#### Phase 2: Data Extraction (データ抽出サブエージェント — PDF Enhanced)
Launch a subagent with the data-extraction skill instructions:
- **Step 0**: Download PDF and run PyMuPDF table extraction + page-to-image conversion
  ```bash
  python3 scripts/download_pdf.py {PMCID} papers/iteration_{N}/original/
  python3 scripts/extract_tables_from_pdf.py papers/iteration_{N}/original/paper.pdf papers/iteration_{N}/extracted/
  python3 scripts/pdf_to_images.py papers/iteration_{N}/original/paper.pdf papers/iteration_{N}/original/page_images/ --dpi 200
  ```
- **Step 1-4**: Extract Results, tables (from PDF + text), figures (from page images), study design
- **Step 5**: Extract raw reference list
- **Step 6**: Save all extracted data to `papers/iteration_{N}/extracted/`

#### Phase 2.5: Reference Verification (参考文献検証サブエージェント — NEW)
Launch a subagent with the reference-search skill instructions:
- Read `papers/iteration_{N}/extracted/references_raw.json`
- Verify each reference via PubMed using `scripts/search_pubmed.py`
- Save verified references to `papers/iteration_{N}/extracted/references_verified.json`
- Save formatted list to `papers/iteration_{N}/extracted/references_formatted.md`

**NOTE**: This can run IN PARALLEL with Phase 3 draft writing, since the draft writer
should first write the paper body, then incorporate verified references.
Alternatively, run it before Phase 3 and include `references_formatted.md` in the
draft writer's input.

#### Phase 3: Draft Writing (ドラフト作成サブエージェント)
Launch a subagent with the draft-writing skill instructions:
- **CRITICAL**: This subagent must NOT have access to the original paper
- Provide ONLY:
  - `extracted_data_bundle.md`
  - `writing-guidelines.md`
  - `references_formatted.md` (verified reference list from Phase 2.5)
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
- PDF Tables Extracted: [count]
- References Verified: [X/Y]

## Score Trend
| Iteration | Accuracy | Completeness | Logic | Readability | Structure | Clinical | Overall |
|-----------|----------|--------------|-------|-------------|-----------|----------|---------|
| 1         | X        | X            | X     | X           | X         | X        | X       |
```

### Stopping Criteria
- User requests stop
- Quality score reaches 8.0/10 or above consistently (3 consecutive iterations)
- Maximum 15 iterations unless user requests more
