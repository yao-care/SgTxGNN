#!/usr/bin/env python3
"""Process news and generate Jekyll pages for SgTxGNN.

Functions:
1. Load news from data/news/*.json source files
2. Load keywords.json for keyword matching
3. Deduplicate similar articles across sources
4. Generate docs/_news/*.md pages
5. Generate docs/data/news-index.json

Usage:
    uv run python scripts/process_news.py
"""

import json
import re
from datetime import datetime, timezone, timedelta
from difflib import SequenceMatcher
from pathlib import Path

# Project directories
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "news"
DOCS_DIR = PROJECT_ROOT / "docs"
NEWS_COLLECTION_DIR = DOCS_DIR / "_news"

# Settings
SIMILARITY_THRESHOLD = 0.8  # Title similarity threshold for deduplication
TIME_WINDOW_HOURS = 24  # Deduplication time window (hours)
MAX_NEWS_AGE_DAYS = 30  # Maximum news retention (days)


def load_json(path: Path) -> dict | list:
    """Load JSON file."""
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data: dict | list, path: Path):
    """Save JSON file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_all_sources() -> list[dict]:
    """Load news from all source files."""
    all_news = []
    excluded = {"keywords.json", "matched_news.json", "synonyms.json"}

    if not DATA_DIR.exists():
        print("  Warning: data/news directory not found")
        return []

    for json_file in DATA_DIR.glob("*.json"):
        if json_file.name in excluded:
            continue

        try:
            data = load_json(json_file)

            # Handle different formats
            if "articles" in data:
                # sg_news.py format
                articles = data.get("articles", {}).get("all", [])
                for item in articles:
                    item["id"] = item.get("url", "")[:100]
                    item["sources"] = [{
                        "name": item.get("source", "Unknown"),
                        "link": item.get("url", "")
                    }]
                    item["published"] = item.get("fetched_at", datetime.now().isoformat())
                    all_news.append(item)
                print(f"  - {json_file.name}: {len(articles)} articles")
            elif "news" in data:
                # Standard format
                news_items = data.get("news", [])
                for item in news_items:
                    all_news.append(item)
                print(f"  - {json_file.name}: {len(news_items)} articles")

        except Exception as e:
            print(f"  Warning: Cannot load {json_file.name} - {e}")

    return all_news


def filter_old_news(news_items: list[dict]) -> list[dict]:
    """Filter out news older than MAX_NEWS_AGE_DAYS."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=MAX_NEWS_AGE_DAYS)
    filtered = []

    for item in news_items:
        try:
            published_str = item.get("published", "") or item.get("fetched_at", "")
            if published_str:
                # Handle different datetime formats
                published_str = published_str.replace("Z", "+00:00")
                published = datetime.fromisoformat(published_str)
                if published.tzinfo is None:
                    published = published.replace(tzinfo=timezone.utc)
                if published >= cutoff:
                    filtered.append(item)
            else:
                filtered.append(item)
        except (ValueError, TypeError):
            filtered.append(item)

    removed = len(news_items) - len(filtered)
    if removed > 0:
        print(f"  Filtered old news: {removed} articles")

    return filtered


def title_similarity(title1: str, title2: str) -> float:
    """Calculate similarity between two titles."""
    clean1 = re.sub(r"\s*[-–—]\s*[^\s]+$", "", title1).strip().lower()
    clean2 = re.sub(r"\s*[-–—]\s*[^\s]+$", "", title2).strip().lower()
    return SequenceMatcher(None, clean1, clean2).ratio()


def deduplicate_news(news_items: list[dict]) -> list[dict]:
    """Deduplicate similar news articles."""
    if not news_items:
        return []

    # Sort by published date (newest first)
    def get_time(item):
        try:
            ts = item.get("published", "") or item.get("fetched_at", "")
            return ts
        except:
            return ""

    sorted_news = sorted(news_items, key=get_time, reverse=True)

    merged = []
    used_indices = set()

    for i, item in enumerate(sorted_news):
        if i in used_indices:
            continue

        similar_items = [item]

        for j, other in enumerate(sorted_news[i + 1:], start=i + 1):
            if j in used_indices:
                continue

            if title_similarity(item.get("title", ""), other.get("title", "")) >= SIMILARITY_THRESHOLD:
                similar_items.append(other)
                used_indices.add(j)

        # Merge sources
        all_sources = []
        seen_links = set()
        for sim_item in similar_items:
            for source in sim_item.get("sources", []):
                link = source.get("link", "")
                if link and link not in seen_links:
                    seen_links.add(link)
                    all_sources.append(source)

        merged_item = {
            "id": item.get("id", item.get("url", str(i))),
            "title": re.sub(r"\s*[-–—]\s*[^\s]+$", "", item.get("title", "")).strip(),
            "published": item.get("published", item.get("fetched_at", "")),
            "summary": item.get("summary", ""),
            "sources": all_sources if all_sources else [{"name": item.get("source", ""), "link": item.get("url", "")}],
            "matched_keywords": item.get("keywords", [])
        }
        merged.append(merged_item)
        used_indices.add(i)

    print(f"  After deduplication: {len(merged)} articles (merged {len(news_items) - len(merged)})")
    return merged


def match_keywords(news_items: list[dict], keywords: dict) -> list[dict]:
    """Match keywords to news articles."""
    patterns = keywords.get("patterns", {})
    drug_patterns = patterns.get("drugs", [])
    indication_patterns = patterns.get("indications", [])

    matched_count = 0

    for item in news_items:
        text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
        matches = []

        # Match drugs
        for pattern in drug_patterns:
            primary_term = pattern.get("primary_term", "")
            for term in pattern.get("search_terms", []):
                if term.lower() in text:
                    matches.append({
                        "type": "drug",
                        "name": primary_term,
                        "keyword": term
                    })
                    break

        # Match indications
        for pattern in indication_patterns:
            primary_term = pattern.get("primary_term", "")
            for term in pattern.get("search_terms", []):
                if term.lower() in text:
                    matches.append({
                        "type": "indication",
                        "name": primary_term,
                        "keyword": term
                    })
                    break

        # Use existing keywords if no matches
        if not matches and item.get("keywords"):
            matches = [{"type": "keyword", "name": k, "keyword": k} for k in item["keywords"]]

        item["matched_keywords"] = matches
        if matches:
            matched_count += 1

    print(f"  Matched keywords: {matched_count} articles")
    return news_items


def slugify(text: str) -> str:
    """Convert text to URL-safe slug."""
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    slug = re.sub(r"[\s_]+", "-", slug)
    return slug.strip("-")[:50]


def generate_news_pages(matched_news: list[dict]):
    """Generate Jekyll news pages."""
    NEWS_COLLECTION_DIR.mkdir(parents=True, exist_ok=True)

    # Clear old pages
    for old_file in NEWS_COLLECTION_DIR.glob("*.md"):
        old_file.unlink()

    # Group news by drug/indication
    drug_news = {}
    indication_news = {}

    for item in matched_news:
        for match in item.get("matched_keywords", []):
            name = match.get("name", "")
            if match.get("type") == "drug":
                if name not in drug_news:
                    drug_news[name] = []
                drug_news[name].append(item)
            elif match.get("type") == "indication":
                if name not in indication_news:
                    indication_news[name] = []
                indication_news[name].append(item)

    # Generate drug news pages
    for drug_name, items in drug_news.items():
        generate_drug_news_page(drug_name, items)

    # Generate indication news pages
    for ind_name, items in indication_news.items():
        generate_indication_news_page(ind_name, items)

    print(f"  Generated pages: {len(drug_news)} drugs + {len(indication_news)} indications")


def generate_drug_news_page(drug_name: str, news_items: list[dict]):
    """Generate a drug news page."""
    slug = slugify(drug_name)

    content = f"""---
layout: default
title: "{drug_name} News"
parent: Health News
nav_exclude: true
description: "Health news related to {drug_name}"
permalink: /news/{slug}/
---

# {drug_name} Related News

[← Back to News Overview]({{{{ '/news/' | relative_url }}}})

---

**{len(news_items)} articles** related to {drug_name}.

---

"""

    for item in sorted(news_items, key=lambda x: x.get("published", ""), reverse=True):
        try:
            dt = datetime.fromisoformat(item.get("published", "").replace("Z", "+00:00"))
            date_str = dt.strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            date_str = "Unknown date"

        sources = item.get("sources", [])
        first_link = sources[0].get("link", "#") if sources else "#"
        sources_html = " · ".join(f'[{s.get("name", "Source")}]({s.get("link", "#")})' for s in sources)

        content += f"""### [{item.get("title", "Untitled")}]({first_link})

{date_str}

Source: {sources_html}

---

"""

    content += """
<div class="disclaimer">
<strong>Disclaimer</strong>: News articles are automatically collected for research purposes only. This does not constitute medical advice.
</div>
"""

    output_path = NEWS_COLLECTION_DIR / f"{slug}.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)


def generate_indication_news_page(ind_name: str, news_items: list[dict]):
    """Generate an indication news page."""
    slug = slugify(ind_name)

    content = f"""---
layout: default
title: "{ind_name} News"
parent: Health News
nav_exclude: true
description: "Health news related to {ind_name}"
permalink: /news/{slug}/
---

# {ind_name} Related News

[← Back to News Overview]({{{{ '/news/' | relative_url }}}})

---

**{len(news_items)} articles** related to {ind_name}.

---

"""

    for item in sorted(news_items, key=lambda x: x.get("published", ""), reverse=True):
        try:
            dt = datetime.fromisoformat(item.get("published", "").replace("Z", "+00:00"))
            date_str = dt.strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            date_str = "Unknown date"

        sources = item.get("sources", [])
        first_link = sources[0].get("link", "#") if sources else "#"
        sources_html = " · ".join(f'[{s.get("name", "Source")}]({s.get("link", "#")})' for s in sources)

        content += f"""### [{item.get("title", "Untitled")}]({first_link})

{date_str}

Source: {sources_html}

---

"""

    content += """
<div class="disclaimer">
<strong>Disclaimer</strong>: News articles are automatically collected for research purposes only. This does not constitute medical advice.
</div>
"""

    output_path = NEWS_COLLECTION_DIR / f"{slug}.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)


def generate_news_index(matched_news: list[dict]):
    """Generate news index JSON for frontend."""
    indexed_news = [
        {
            "id": item.get("id", ""),
            "title": item.get("title", ""),
            "published": item.get("published", ""),
            "sources": item.get("sources", []),
            "keywords": item.get("matched_keywords", [])
        }
        for item in matched_news
        if item.get("matched_keywords")
    ]

    output = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "count": len(indexed_news),
        "news": indexed_news
    }

    output_path = DOCS_DIR / "data" / "news-index.json"
    save_json(output, output_path)
    print(f"  Generated index: {output_path}")


def main():
    print("=" * 60)
    print("Processing News - SgTxGNN")
    print("=" * 60)
    print()

    # 1. Load all sources
    print("1. Loading source files:")
    all_news = load_all_sources()
    print(f"   Total: {len(all_news)} articles")

    if not all_news:
        print("\n   No news to process. Run sg_news.py first.")
        return

    # 2. Filter old news
    print("\n2. Filtering old news:")
    all_news = filter_old_news(all_news)

    # 3. Deduplicate
    print("\n3. Deduplicating:")
    all_news = deduplicate_news(all_news)

    # 4. Load keywords and match
    print("\n4. Keyword matching:")
    keywords_path = DATA_DIR / "keywords.json"
    if keywords_path.exists():
        keywords = load_json(keywords_path)
        all_news = match_keywords(all_news, keywords)
    else:
        print("   Warning: keywords.json not found. Run generate_news_keywords.py first.")

    # 5. Save matched news
    output = {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "total_count": len(all_news),
        "matched_count": sum(1 for n in all_news if n.get("matched_keywords")),
        "news": all_news
    }
    save_json(output, DATA_DIR / "matched_news.json")
    print(f"\n5. Saved: {DATA_DIR / 'matched_news.json'}")

    # 6. Generate pages
    print("\n6. Generating Jekyll pages:")
    generate_news_pages(all_news)

    # 7. Generate index
    print("\n7. Generating index:")
    generate_news_index(all_news)

    print("\n" + "=" * 60)
    print("News Processing Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
