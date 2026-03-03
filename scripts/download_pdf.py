#!/usr/bin/env python3
"""Download PDF from Europe PMC given a PMCID.

Usage:
    python3 scripts/download_pdf.py <PMCID> <output_dir>

Example:
    python3 scripts/download_pdf.py PMC11193429 papers/iteration_3/original/
"""

import json
import sys
import urllib.request
import urllib.error
import time
from pathlib import Path


def resolve_pdf_url(pmcid: str) -> str:
    """Resolve the PDF download URL for a given PMCID."""
    return f"https://europepmc.org/backend/ptpmcrender.fcgi?accid={pmcid}&blobtype=pdf"


def download_with_retry(url: str, output_path: Path, max_retries: int = 4) -> bool:
    """Download a file with exponential backoff retry."""
    for attempt in range(max_retries + 1):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (research-paper-pipeline)"
            })
            with urllib.request.urlopen(req, timeout=60) as resp:
                content = resp.read()
                if len(content) < 1000:
                    print(f"Warning: Downloaded content is very small ({len(content)} bytes)")
                    print(f"Content preview: {content[:200]}")
                    return False
                output_path.write_bytes(content)
                print(f"Downloaded {len(content):,} bytes -> {output_path}")
                return True
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            if attempt < max_retries:
                wait = 2 ** (attempt + 1)
                print(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait}s...")
                time.sleep(wait)
            else:
                print(f"All {max_retries + 1} attempts failed: {e}")
                return False
    return False


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    pmcid = sys.argv[1]
    output_dir = Path(sys.argv[2])
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_url = resolve_pdf_url(pmcid)
    pdf_path = output_dir / "paper.pdf"

    print(f"Downloading PDF for {pmcid}")
    print(f"URL: {pdf_url}")

    if download_with_retry(pdf_url, pdf_path):
        result = {
            "pmcid": pmcid,
            "pdf_url": pdf_url,
            "pdf_path": str(pdf_path),
            "success": True,
        }
    else:
        result = {
            "pmcid": pmcid,
            "pdf_url": pdf_url,
            "pdf_path": None,
            "success": False,
        }

    result_json = json.dumps(result, indent=2)
    print(result_json)
    return 0 if result["success"] else 1


if __name__ == "__main__":
    sys.exit(main())
