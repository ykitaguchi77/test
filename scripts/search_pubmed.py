#!/usr/bin/env python3
"""Search PubMed for a reference and return structured citation data.

Uses NCBI E-utilities (no API key required, rate-limited to 3 requests/sec).

Usage:
    python3 scripts/search_pubmed.py --title "paper title"
    python3 scripts/search_pubmed.py --doi "10.1234/example"
    python3 scripts/search_pubmed.py --pmid "12345678"
    python3 scripts/search_pubmed.py --query "free text search"

Output: JSON with structured citation data.
"""

import argparse
import json
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
import xml.etree.ElementTree as ET

ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
RATE_LIMIT_DELAY = 0.34  # ~3 requests/sec without API key


def fetch_url(url: str, max_retries: int = 3) -> str:
    """Fetch URL content with retry logic."""
    for attempt in range(max_retries + 1):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "research-paper-pipeline/1.0"
            })
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read().decode("utf-8")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            if attempt < max_retries:
                wait = 2 ** (attempt + 1)
                time.sleep(wait)
            else:
                raise RuntimeError(f"Failed after {max_retries + 1} attempts: {e}")


def search_pubmed(query: str, max_results: int = 5) -> list[str]:
    """Search PubMed and return list of PMIDs."""
    params = urllib.parse.urlencode({
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json",
        "sort": "relevance",
    })
    url = f"{ESEARCH_URL}?{params}"
    data = json.loads(fetch_url(url))
    return data.get("esearchresult", {}).get("idlist", [])


def fetch_article_details(pmids: list[str]) -> list[dict]:
    """Fetch detailed article info for given PMIDs."""
    if not pmids:
        return []

    params = urllib.parse.urlencode({
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml",
    })
    url = f"{EFETCH_URL}?{params}"
    xml_text = fetch_url(url)

    articles = []
    root = ET.fromstring(xml_text)

    for article_elem in root.findall(".//PubmedArticle"):
        article = parse_article(article_elem)
        if article:
            articles.append(article)

    return articles


def parse_article(elem) -> dict:
    """Parse a single PubmedArticle XML element into a dict."""
    medline = elem.find(".//MedlineCitation")
    if medline is None:
        return {}

    pmid_elem = medline.find("PMID")
    pmid = pmid_elem.text if pmid_elem is not None else ""

    article = medline.find("Article")
    if article is None:
        return {}

    # Title
    title_elem = article.find("ArticleTitle")
    title = "".join(title_elem.itertext()) if title_elem is not None else ""

    # Journal
    journal_elem = article.find(".//Journal/Title")
    journal = journal_elem.text if journal_elem is not None else ""

    journal_abbrev_elem = article.find(".//Journal/ISOAbbreviation")
    journal_abbrev = journal_abbrev_elem.text if journal_abbrev_elem is not None else ""

    # Year
    year = ""
    pub_date = article.find(".//Journal/JournalIssue/PubDate")
    if pub_date is not None:
        year_elem = pub_date.find("Year")
        if year_elem is not None:
            year = year_elem.text
        else:
            medline_date = pub_date.find("MedlineDate")
            if medline_date is not None and medline_date.text:
                year = medline_date.text[:4]

    # Volume / Issue / Pages
    vol_elem = article.find(".//Journal/JournalIssue/Volume")
    volume = vol_elem.text if vol_elem is not None else ""
    issue_elem = article.find(".//Journal/JournalIssue/Issue")
    issue = issue_elem.text if issue_elem is not None else ""
    pages_elem = article.find(".//Pagination/MedlinePgn")
    pages = pages_elem.text if pages_elem is not None else ""

    # Authors
    authors = []
    for author_elem in article.findall(".//AuthorList/Author"):
        last = author_elem.find("LastName")
        first = author_elem.find("ForeName")
        initials = author_elem.find("Initials")
        if last is not None:
            name = last.text
            if initials is not None:
                name += " " + initials.text
            authors.append(name)

    # DOI
    doi = ""
    for id_elem in article.findall(".//ELocationID"):
        if id_elem.get("EIdType") == "doi":
            doi = id_elem.text
            break
    if not doi:
        article_ids = elem.findall(".//PubmedData/ArticleIdList/ArticleId")
        for aid in article_ids:
            if aid.get("IdType") == "doi":
                doi = aid.text
                break

    # PMCID
    pmcid = ""
    article_ids = elem.findall(".//PubmedData/ArticleIdList/ArticleId")
    for aid in article_ids:
        if aid.get("IdType") == "pmc":
            pmcid = aid.text
            break

    # Abstract
    abstract_parts = []
    for abs_text in article.findall(".//Abstract/AbstractText"):
        label = abs_text.get("Label", "")
        text = "".join(abs_text.itertext())
        if label:
            abstract_parts.append(f"{label}: {text}")
        else:
            abstract_parts.append(text)
    abstract = " ".join(abstract_parts)

    # Format citation string
    author_str = ""
    if len(authors) <= 3:
        author_str = ", ".join(authors)
    elif authors:
        author_str = f"{authors[0]}, et al."

    citation = f"{author_str}. {title} {journal_abbrev}. {year}"
    if volume:
        citation += f";{volume}"
        if issue:
            citation += f"({issue})"
    if pages:
        citation += f":{pages}"
    citation += "."

    return {
        "pmid": pmid,
        "pmcid": pmcid,
        "doi": doi,
        "title": title,
        "authors": authors,
        "author_str": author_str,
        "journal": journal,
        "journal_abbrev": journal_abbrev,
        "year": year,
        "volume": volume,
        "issue": issue,
        "pages": pages,
        "abstract": abstract[:500] if abstract else "",
        "citation": citation,
    }


def main():
    parser = argparse.ArgumentParser(description="Search PubMed for references")
    parser.add_argument("--title", help="Search by paper title")
    parser.add_argument("--doi", help="Search by DOI")
    parser.add_argument("--pmid", help="Fetch by PMID directly")
    parser.add_argument("--query", help="Free text search")
    parser.add_argument("--max-results", type=int, default=3, help="Max results (default: 3)")
    parser.add_argument("--output", help="Optional output file path (JSON)")
    args = parser.parse_args()

    if args.pmid:
        pmids = [args.pmid]
    else:
        if args.doi:
            query = f"{args.doi}[doi]"
        elif args.title:
            query = f"{args.title}[Title]"
        elif args.query:
            query = args.query
        else:
            print("Error: Provide --title, --doi, --pmid, or --query")
            sys.exit(1)

        print(f"Searching PubMed: {query}", file=sys.stderr)
        pmids = search_pubmed(query, args.max_results)
        time.sleep(RATE_LIMIT_DELAY)

    if not pmids:
        print(json.dumps({"results": [], "query": query if not args.pmid else args.pmid}))
        return

    print(f"Found PMIDs: {pmids}", file=sys.stderr)
    articles = fetch_article_details(pmids)

    output = {"results": articles, "count": len(articles)}
    output_json = json.dumps(output, indent=2, ensure_ascii=False)

    if args.output:
        Path(args.output).write_text(output_json, encoding="utf-8")
        print(f"Saved to {args.output}", file=sys.stderr)
    print(output_json)


if __name__ == "__main__":
    main()
