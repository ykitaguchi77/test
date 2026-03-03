# Reference Discovery Skill (参考文献発見 — Phase 3.5)

## Purpose
After the draft paper is finalized (Phase 3), independently discover and attach references to support the claims made in the draft. The draft text MUST NOT be modified — only reference markers and a reference list are added.

This replaces the old "reference verification" approach (which extracted references from the original paper). The new approach ensures blind integrity: references are found based on the draft's claims, not copied from the original.

## Instructions

### CRITICAL CONSTRAINT — TEXT FREEZE
The draft paper text (`draft_paper.md`) is FROZEN. You MUST NOT change any sentences, paragraphs, or wording in the draft. You may ONLY:
1. Insert citation markers (e.g., `[1]`, `[2]`) at appropriate positions in existing sentences
2. Add a References section at the end of the document

### Input
- Path to `papers/iteration_{N}/draft/draft_paper.md` (finalized draft — text frozen)
- Iteration number N

### Step 1: Identify Claims Needing Citations

Read the draft paper and identify statements that require supporting references:
1. **Introduction**: Epidemiological facts, prevalence data, background claims
2. **Methods**: Statistical method choices (cite methodology papers only if non-standard)
3. **Discussion**: Comparisons with prior literature, general medical claims
4. **Discussion**: Biological mechanism explanations

For each claim, extract the key searchable terms (e.g., "AMD prevalence worldwide", "trabeculectomy vs canaloplasty long-term outcomes").

### Step 2: Search for Supporting References

For each identified claim, search PubMed for supporting literature:

#### Method A: WebSearch (Preferred)
```
WebSearch: PubMed {key terms from the claim} {relevant medical subject headings}
```

#### Method B: search_pubmed.py Script
```bash
python3 scripts/search_pubmed.py --query "{search terms}"
```

**Search Strategy:**
- Search for the CLAIM's topic, NOT for the specific paper being drafted
- Use general medical terms (e.g., "diabetic retinopathy AMD risk" not specific sample sizes)
- Prefer systematic reviews, meta-analyses, and large cohort studies as references
- Aim for 15-30 references total (typical for a research paper)

### Step 3: Verify Each Reference

For each candidate reference found via search:
1. Confirm it actually supports the claim (read the abstract/title carefully)
2. Extract full citation details:
   - PMID, DOI
   - Authors, title, journal, year, volume, issue, pages
3. Format in Vancouver style

### Step 4: Insert Citation Markers

Create a modified version of the draft with citation markers inserted:
- Save as `papers/iteration_{N}/draft/draft_paper_with_refs.md`
- Insert `[1]`, `[2]`, etc. at the end of sentences that the references support
- Do NOT change any other text — only add markers

Example:
```
Original: "AMD is the leading cause of blindness in the elderly."
With ref:  "AMD is the leading cause of blindness in the elderly [1]."
```

### Step 5: Generate Reference List

Append a numbered reference list at the end of `draft_paper_with_refs.md`:

```markdown
## References

1. Smith AB, Jones CD. Title of paper. J Name. 2020;45(3):123-130.
2. ...
```

### Step 6: Save Results

Save to `papers/iteration_{N}/draft/`:
- `draft_paper_with_refs.md` — Draft with citation markers and reference list (text unchanged)
- `references.json` — Structured reference data
- `reference_mapping.md` — Which claim maps to which reference(s)

### Output

Return a summary:
```json
{
  "total_claims_identified": 20,
  "references_found": 18,
  "references_not_found": 2,
  "total_unique_references": 15,
  "claims_without_refs": ["list of unsupported claims"]
}
```

### CRITICAL RULES
1. **TEXT FREEZE**: NEVER modify the draft text beyond inserting citation markers `[N]`
2. **NEVER fabricate references** — only use papers actually found via PubMed/WebSearch
3. **DO NOT search for the paper being drafted** — search for papers that SUPPORT its claims
4. **DO NOT read** the original paper (`papers/iteration_{N}/original/`) or `paper_identity.json`
5. Prefer recent, high-impact references (systematic reviews, large cohorts, RCTs)
6. If a claim cannot be supported by a found reference, leave it without a citation marker and note it in `reference_mapping.md`
