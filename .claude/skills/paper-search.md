# Paper Search Skill (論文検索)

## Purpose
Search for and download open-access ophthalmology papers from Europe PMC.

## Instructions

When invoked, this skill searches for open-access research articles in ophthalmology journals using the Europe PMC REST API.

### Step 1: Search for Open-Access Papers

Use WebFetch to query Europe PMC REST API:

```
https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=(JOURNAL:"ophthalmology" OR JOURNAL:"eye" OR JOURNAL:"JAMA ophthalmology" OR JOURNAL:"british journal of ophthalmology" OR JOURNAL:"investigative ophthalmology" OR JOURNAL:"BMJ open ophthalmology" OR JOURNAL:"retina" OR JOURNAL:"cornea" OR JOURNAL:"glaucoma") AND OPEN_ACCESS:y AND SRC:MED AND (PUB_TYPE:"research-article" OR PUB_TYPE:"Journal Article")&resultType=core&pageSize=25&format=json&sort=CITED desc
```

Extract from the results:
- PMCID (e.g., PMC1234567)
- Title
- Journal name
- Authors
- Publication date
- Citation count

### Step 2: Select a Paper

Choose a paper that:
1. Has a PMCID (required for full-text access)
2. Is a research article (not a review, editorial, or letter)
3. Preferably has tables and figures (check if `hasTextMinedTerms` or similar indicators exist)
4. Has reasonable citation count (indicates quality)

### Step 3: Download Full Text

Fetch the full-text XML from Europe PMC:

```
https://www.ebi.ac.uk/europepmc/webservices/rest/{PMCID}/fullTextXML
```

### Step 4: Save the Paper

Save the downloaded content to `papers/iteration_{N}/original/`:
- `paper_metadata.json` - Title, authors, journal, DOI, PMCID
- `paper_fulltext.xml` - Full XML content
- `paper_fulltext.txt` - Cleaned plain text version

### Output Format

Return a JSON object with:
```json
{
  "pmcid": "PMC...",
  "title": "...",
  "journal": "...",
  "authors": "...",
  "doi": "...",
  "year": "...",
  "sections_found": ["Introduction", "Methods", "Results", "Discussion"],
  "has_tables": true/false,
  "has_figures": true/false,
  "file_paths": {
    "metadata": "papers/iteration_N/original/paper_metadata.json",
    "fulltext_xml": "papers/iteration_N/original/paper_fulltext.xml",
    "fulltext_txt": "papers/iteration_N/original/paper_fulltext.txt"
  }
}
```
