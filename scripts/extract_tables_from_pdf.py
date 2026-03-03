#!/usr/bin/env python3
"""Extract tables from a PDF using PyMuPDF's built-in table detection.

Usage:
    python3 scripts/extract_tables_from_pdf.py <pdf_path> <output_dir>

Example:
    python3 scripts/extract_tables_from_pdf.py papers/iteration_3/original/paper.pdf papers/iteration_3/extracted/
"""

import json
import sys
from pathlib import Path

import fitz  # PyMuPDF


def extract_tables(pdf_path: str) -> list[dict]:
    """Extract all tables from a PDF file.

    Returns a list of dicts, each containing:
      - page: page number (0-indexed)
      - table_index: table index on that page
      - headers: list of column headers (first row)
      - rows: list of rows (each row is a list of cell strings)
      - markdown: the table formatted as markdown
    """
    doc = fitz.open(pdf_path)
    tables = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        try:
            page_tables = page.find_tables()
        except Exception as e:
            print(f"Warning: Table detection failed on page {page_num}: {e}")
            continue

        for t_idx, table in enumerate(page_tables.tables):
            try:
                extracted = table.extract()
            except Exception as e:
                print(f"Warning: Table extraction failed on page {page_num}, table {t_idx}: {e}")
                continue

            if not extracted or len(extracted) < 2:
                continue

            # Clean cells: replace None with empty string
            cleaned = []
            for row in extracted:
                cleaned.append([str(cell).strip() if cell is not None else "" for cell in row])

            headers = cleaned[0]
            rows = cleaned[1:]

            # Build markdown table
            md_lines = []
            md_lines.append("| " + " | ".join(headers) + " |")
            md_lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
            for row in rows:
                # Pad row if shorter than headers
                padded = row + [""] * (len(headers) - len(row))
                md_lines.append("| " + " | ".join(padded[:len(headers)]) + " |")

            tables.append({
                "page": page_num,
                "table_index": t_idx,
                "headers": headers,
                "rows": rows,
                "markdown": "\n".join(md_lines),
            })

    doc.close()
    return tables


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_dir = Path(sys.argv[2])
    output_dir.mkdir(parents=True, exist_ok=True)

    if not Path(pdf_path).exists():
        print(f"Error: PDF not found: {pdf_path}")
        sys.exit(1)

    print(f"Extracting tables from: {pdf_path}")
    tables = extract_tables(pdf_path)
    print(f"Found {len(tables)} tables")

    # Save individual tables and combined markdown
    combined_md = f"# Tables Extracted from PDF\n\nTotal tables found: {len(tables)}\n\n"

    for i, table in enumerate(tables):
        combined_md += f"## Table {i + 1} (Page {table['page'] + 1})\n\n"
        combined_md += table["markdown"] + "\n\n"

    # Save combined markdown
    md_path = output_dir / "pdf_tables.md"
    md_path.write_text(combined_md, encoding="utf-8")
    print(f"Saved combined tables -> {md_path}")

    # Save structured JSON
    json_path = output_dir / "pdf_tables.json"
    json_path.write_text(json.dumps(tables, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Saved structured data -> {json_path}")

    # Summary
    summary = {
        "pdf_path": pdf_path,
        "total_tables": len(tables),
        "tables_by_page": {},
    }
    for t in tables:
        pg = str(t["page"] + 1)
        summary["tables_by_page"][pg] = summary["tables_by_page"].get(pg, 0) + 1

    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
