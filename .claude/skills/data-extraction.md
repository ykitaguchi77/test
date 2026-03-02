# Data Extraction Skill (論文データ抽出)

## Purpose
Extract structured information from the Results section, tables, and figures of a downloaded ophthalmology paper. This extracted data will be the ONLY information given to the draft-writing subagent.

## Instructions

### Input
- Path to the full-text paper (XML or text format) in `papers/iteration_{N}/original/`
- PMCID of the paper (from `paper_metadata.json`)

### Step 0: Download and Process PDF (NEW — PDF Pipeline)

Before text-based extraction, obtain the PDF for high-fidelity table and figure extraction.

#### 0a. Download PDF
**Primary method** (direct HTTP — works locally and in Colab):
```bash
python3 scripts/download_pdf.py {PMCID} papers/iteration_{N}/original/
```
This saves `papers/iteration_{N}/original/paper.pdf`.

**Fallback** (if script fails with network errors — e.g., sandboxed environments):
Use WebFetch to access the PMC HTML page directly for table extraction:
```
WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/{PMCID}/
Prompt: "Extract ALL tables with complete cell data, and extract the complete reference list"
```
If WebFetch also fails, skip PDF-based extraction and rely on the existing text file + WebSearch-based table verification (see Step 2 fallback).

#### 0b. Extract Tables from PDF (PyMuPDF)
```bash
python3 scripts/extract_tables_from_pdf.py papers/iteration_{N}/original/paper.pdf papers/iteration_{N}/extracted/
```
This produces:
- `papers/iteration_{N}/extracted/pdf_tables.md` — All tables in markdown format
- `papers/iteration_{N}/extracted/pdf_tables.json` — Structured table data

#### 0c. Convert PDF Pages to Images (Vision Fallback)
```bash
python3 scripts/pdf_to_images.py papers/iteration_{N}/original/paper.pdf papers/iteration_{N}/original/page_images/ --dpi 200
```
This produces PNG images for each page and a manifest at `page_images/page_images_manifest.json`.

#### 0d. Vision-Based Table Verification
If PyMuPDF table extraction produced tables, verify them against the page images:
1. Read the manifest to identify which pages contain tables
2. Use the Read tool on the corresponding page image PNGs
3. Compare the PyMuPDF-extracted table data against what is visible in the images
4. If discrepancies are found, use the image data as ground truth

If PyMuPDF extracted 0 tables or produced garbled output:
1. Read ALL page images that likely contain tables (look for pages with dense grid/cell structures)
2. Manually transcribe table data from the images into markdown tables
3. This is the PRIMARY extraction method when PyMuPDF fails

### Step 1: Extract Results Section

Parse the paper (text format) and extract the complete Results section, including:
- All statistical findings (p-values, confidence intervals, odds ratios, hazard ratios — both adjusted AND unadjusted)
- All numerical data points
- All comparisons between groups
- Sample sizes and demographics mentioned in Results
- Any subgroup analyses

**IMPORTANT**: For hazard ratios, odds ratios, and risk ratios, extract BOTH:
- Unadjusted (crude) estimates if present
- Adjusted estimates with the covariates used for adjustment

If the text-based extraction misses any numerical data, cross-reference with the PDF table data from Step 0b/0d.

### Step 2: Extract Tables

Use a **multi-source strategy** for maximum completeness:

1. **Primary source**: PDF-extracted tables from Step 0b (`pdf_tables.md`)
2. **Verification**: Cross-reference with text-based tables from the XML/text file
3. **Fallback**: If any table cells are missing or garbled, use page images (Step 0d) to fill in gaps

For each table, ensure:
- Table number and title/caption
- Column headers
- ALL data cells (preserve exact numbers — no rounding, no estimation)
- Footnotes and legends
- Statistical annotations
- Both adjusted and unadjusted effect estimates when present

Format each table as a structured markdown table.

### Step 3: Extract Figures

For each figure:
- Figure number and title/caption
- Legend text
- Any data labels visible in the description
- Type of figure (bar chart, scatter plot, Kaplan-Meier, forest plot, etc.)
- Key findings the figure illustrates

**NEW**: Use the PDF page images to read figure content:
1. Identify pages containing figures from the page images
2. Use the Read tool on those PNG files to view the actual figures
3. Extract any numerical data visible in the figures (axis labels, data points, annotations)
4. For Kaplan-Meier plots: extract number-at-risk tables if present below the plot
5. For forest plots: extract all effect estimates and confidence intervals

### Step 4: Extract Study Design Summary

Create a minimal summary containing ONLY:
- Study type (RCT, cohort, case-control, cross-sectional, etc.)
- Primary and secondary outcomes
- Number of participants/eyes
- Follow-up period
- Key inclusion/exclusion criteria

### Step 5: Extract Reference List (NEW)

Extract the reference list from the paper for later PubMed verification:
1. Parse the References/Bibliography section from the text/XML
2. For each reference, extract:
   - Reference number (as cited in the paper)
   - Author(s)
   - Title (if available)
   - Journal
   - Year
   - DOI (if available)
3. Save to `papers/iteration_{N}/extracted/references_raw.json`

This list will be passed to the reference-search skill for PubMed verification.

### Step 6: Save Extracted Data

Save to `papers/iteration_{N}/extracted/`:
- `results_section.md` - Full Results text
- `tables.md` - All tables in markdown format (merged from PDF + text sources)
- `figures.md` - Figure descriptions, captions, and extracted data from images
- `study_design.md` - Minimal study design summary
- `references_raw.json` - Raw reference list for PubMed verification
- `pdf_tables.md` - PyMuPDF-extracted tables (auto-generated by script)
- `pdf_tables.json` - Structured table data (auto-generated by script)
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
[markdown table — complete with ALL cells from PDF extraction]
...

## Figures
### Figure 1: [title]
[description, data extracted from images, number-at-risk if applicable]
...

## References (Raw)
[numbered list of references as extracted — to be verified via PubMed]
```

### CRITICAL RULES
1. Do NOT include the Introduction, Discussion, or Abstract in the extracted data
2. Do NOT include the authors' interpretation or conclusions
3. Do NOT include Methods details beyond the minimal study design summary
4. The goal is to give the draft writer ONLY the raw findings so they must construct the narrative independently
5. **NEW**: Always prefer PDF-extracted table data over text-parsed tables — PDF preserves cell alignment and completeness
6. **NEW**: When PyMuPDF table extraction fails or is incomplete, use vision (Read tool on page images) as the definitive source
7. **NEW**: Extract BOTH adjusted and unadjusted effect estimates — never silently omit one
