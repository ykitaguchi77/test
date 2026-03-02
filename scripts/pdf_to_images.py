#!/usr/bin/env python3
"""Convert PDF pages to PNG images for Claude vision reading.

Usage:
    python3 scripts/pdf_to_images.py <pdf_path> <output_dir> [--pages PAGES] [--dpi DPI]

Arguments:
    pdf_path    Path to the PDF file
    output_dir  Directory to save PNG images
    --pages     Page range (e.g., "1-5", "2,4,6", "all"). Default: "all"
    --dpi       Resolution in DPI. Default: 200

Examples:
    python3 scripts/pdf_to_images.py paper.pdf images/
    python3 scripts/pdf_to_images.py paper.pdf images/ --pages 3-7 --dpi 300
"""

import argparse
import json
import sys
from pathlib import Path

import fitz  # PyMuPDF


def parse_page_range(page_spec: str, total_pages: int) -> list[int]:
    """Parse page specification into list of 0-indexed page numbers."""
    if page_spec == "all":
        return list(range(total_pages))

    pages = set()
    for part in page_spec.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-", 1)
            start = max(0, int(start) - 1)
            end = min(total_pages, int(end))
            pages.update(range(start, end))
        else:
            pg = int(part) - 1
            if 0 <= pg < total_pages:
                pages.add(pg)
    return sorted(pages)


def pdf_to_images(pdf_path: str, output_dir: Path, pages: list[int], dpi: int = 200) -> list[dict]:
    """Convert specified PDF pages to PNG images.

    Returns list of dicts with page info and file paths.
    """
    doc = fitz.open(pdf_path)
    results = []
    zoom = dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)

    for page_num in pages:
        if page_num >= len(doc):
            print(f"Warning: Page {page_num + 1} out of range (total: {len(doc)})")
            continue

        page = doc[page_num]
        pix = page.get_pixmap(matrix=mat)
        img_filename = f"page_{page_num + 1:03d}.png"
        img_path = output_dir / img_filename
        pix.save(str(img_path))

        results.append({
            "page": page_num + 1,
            "file": str(img_path),
            "width": pix.width,
            "height": pix.height,
        })
        print(f"Page {page_num + 1} -> {img_path} ({pix.width}x{pix.height})")

    doc.close()
    return results


def main():
    parser = argparse.ArgumentParser(description="Convert PDF pages to PNG images")
    parser.add_argument("pdf_path", help="Path to PDF file")
    parser.add_argument("output_dir", help="Directory to save PNG images")
    parser.add_argument("--pages", default="all", help="Page range: 'all', '1-5', '2,4,6'")
    parser.add_argument("--dpi", type=int, default=200, help="Resolution (default: 200)")
    args = parser.parse_args()

    pdf_path = Path(args.pdf_path)
    output_dir = Path(args.output_dir)

    if not pdf_path.exists():
        print(f"Error: PDF not found: {pdf_path}")
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(str(pdf_path))
    total_pages = len(doc)
    doc.close()

    pages = parse_page_range(args.pages, total_pages)
    print(f"PDF: {pdf_path} ({total_pages} pages)")
    print(f"Converting pages: {[p + 1 for p in pages]} at {args.dpi} DPI")

    results = pdf_to_images(str(pdf_path), output_dir, pages, args.dpi)

    summary = {
        "pdf_path": str(pdf_path),
        "total_pages": total_pages,
        "converted_pages": len(results),
        "dpi": args.dpi,
        "images": results,
    }
    summary_path = output_dir / "page_images_manifest.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"\nManifest saved -> {summary_path}")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
