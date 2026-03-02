# Reference Search & Verification Skill (参考文献検索・検証)

## Purpose
Verify and complete the reference list extracted from a paper by searching PubMed for each reference individually. This skill is designed to be run by subagents — one reference at a time or in small batches.

## Instructions

### Input
- Path to `papers/iteration_{N}/extracted/references_raw.json` (raw reference list from data extraction)
- Iteration number N

### Step 1: Load Raw References

Read the `references_raw.json` file. Each reference entry should contain:
```json
{
  "ref_number": 1,
  "authors": "Smith AB, Jones CD",
  "title": "Example paper title",
  "journal": "Journal Name",
  "year": "2020",
  "doi": "10.1234/example"
}
```

Fields may be incomplete — that is expected and the purpose of this verification step.

### Step 2: Verify Each Reference via PubMed

For EACH reference, use one of the following methods (choose based on environment):

#### Method A: WebSearch (Preferred — works in all environments)

Use the WebSearch tool to search PubMed for each reference:

```
WebSearch: PubMed "{paper title}" {first author last name} {year} {journal}
```

From the search results, extract:
- PMID (from PubMed URL: pubmed.ncbi.nlm.nih.gov/{PMID}/)
- PMCID (from PMC URL if available)
- Full title, authors, journal, year, volume, issue, pages
- DOI

**Tip**: Include the paper title in quotes for exact matching. If not found, try with fewer search terms.

#### Method B: WebFetch on PubMed (For detailed extraction)

If WebSearch returns a PubMed URL, use WebFetch to get full citation details:

```
WebFetch: https://pubmed.ncbi.nlm.nih.gov/{PMID}/
Prompt: "Extract the complete citation: authors, title, journal, year, volume, issue, pages, DOI, PMCID"
```

#### Method C: search_pubmed.py Script (For environments with direct HTTP access)

```bash
# By DOI (most reliable):
python3 scripts/search_pubmed.py --doi "10.1234/example"

# By title:
python3 scripts/search_pubmed.py --title "exact paper title"

# By free-text query:
python3 scripts/search_pubmed.py --query "key words AND author AND journal"
```

**NOTE**: If the script fails with network errors, fall back to Method A (WebSearch).

#### Search Strategy (in priority order):
1. **Search by DOI** — most reliable, unique identifier
2. **Search by exact title** — very reliable for correctly extracted titles
3. **Search by title keywords + author + year** — for partially extracted references

### Step 3: Build Verified Reference List

For each successfully verified reference, create a complete citation record:

```json
{
  "ref_number": 1,
  "pmid": "12345678",
  "pmcid": "PMC1234567",
  "doi": "10.1234/example",
  "title": "Verified full paper title",
  "authors": ["Smith AB", "Jones CD", "Wang EF"],
  "author_str": "Smith AB, Jones CD, Wang EF",
  "journal": "Full Journal Name",
  "journal_abbrev": "J Name",
  "year": "2020",
  "volume": "45",
  "issue": "3",
  "pages": "123-130",
  "citation": "Smith AB, Jones CD, Wang EF. Verified full paper title. J Name. 2020;45(3):123-130.",
  "verified": true,
  "verification_method": "websearch"
}
```

For references that CANNOT be found on PubMed:
```json
{
  "ref_number": 5,
  "title": "Original extracted title",
  "verified": false,
  "verification_method": "not_found",
  "note": "Not found on PubMed - may be a book, report, website, or non-indexed journal"
}
```

### Step 4: Generate Formatted Reference List

Create a formatted reference list in Vancouver style (numbered, commonly used in medical journals):
```
1. Smith AB, Jones CD, Wang EF. Verified full paper title. J Name. 2020;45(3):123-130.
2. ...
```

### Step 5: Save Results

Save to `papers/iteration_{N}/extracted/`:
- `references_verified.json` — Full structured data for all references
- `references_formatted.md` — Formatted reference list (Vancouver style)
- `references_summary.md` — Summary: X/Y references verified, methods used

### Output

Return a summary:
```json
{
  "total_references": 30,
  "verified_count": 25,
  "not_found_count": 5,
  "verification_rate": "83%",
  "methods_used": {
    "websearch": 20,
    "webfetch": 3,
    "script": 2,
    "not_found": 5
  }
}
```

### Parallelization Strategy

To speed up verification, the orchestrator can launch MULTIPLE subagents:
- Split the reference list into batches of 5-10 references
- Launch one subagent per batch (up to 3 concurrent subagents)
- Each subagent processes its batch sequentially using WebSearch
- After all subagents complete, merge results into the final verified list

### CRITICAL RULES
1. NEVER fabricate citation details — only use data returned by PubMed/WebSearch
2. If a reference cannot be verified, mark it as unverified rather than guessing
3. Preserve the original reference numbers from the paper
4. For references to books, websites, or non-journal sources, mark as "not_applicable" for PubMed verification
5. When using WebSearch, verify that the returned paper actually matches (check title similarity, author overlap, year)
