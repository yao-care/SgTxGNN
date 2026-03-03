#!/usr/bin/env python3
"""Singapore health news fetcher.

Fetches health-related news from Singapore news sources:
- Channel NewsAsia (CNA)
- The Straits Times
- TODAY Online

Usage:
    uv run python scripts/fetchers/sg_news.py

Output:
    data/news/sg_news_latest.json
"""

import json
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup


@dataclass
class NewsArticle:
    """Represents a news article."""

    title: str
    url: str
    source: str
    published_date: str | None = None
    summary: str | None = None
    keywords: list[str] = field(default_factory=list)
    fetched_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "url": self.url,
            "source": self.source,
            "published_date": self.published_date,
            "summary": self.summary,
            "keywords": self.keywords,
            "fetched_at": self.fetched_at,
        }


class SGNewsFetcher:
    """Fetches health news from Singapore news sources."""

    USER_AGENT = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    def __init__(self, keywords_path: Path | None = None):
        """Initialize the fetcher.

        Args:
            keywords_path: Path to keywords.json for filtering
        """
        self.keywords = self._load_keywords(keywords_path)
        self.client = httpx.Client(
            timeout=30.0,
            follow_redirects=True,
            headers={"User-Agent": self.USER_AGENT},
        )

    def _load_keywords(self, keywords_path: Path | None) -> dict:
        """Load keywords for filtering articles."""
        if keywords_path is None:
            base_dir = Path(__file__).parent.parent.parent
            keywords_path = base_dir / "data" / "news" / "keywords.json"

        if keywords_path.exists():
            with open(keywords_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def _extract_keywords_from_text(self, text: str) -> list[str]:
        """Extract matching keywords from text."""
        if not self.keywords:
            return []

        text_lower = text.lower()
        found = []

        # Check drug patterns
        for pattern in self.keywords.get("patterns", {}).get("drugs", []):
            for term in pattern.get("search_terms", []):
                if term.lower() in text_lower:
                    found.append(pattern.get("primary_term", term))
                    break

        # Check indication patterns
        for pattern in self.keywords.get("patterns", {}).get("indications", []):
            for term in pattern.get("search_terms", []):
                if term.lower() in text_lower:
                    found.append(pattern.get("primary_term", term))
                    break

        return list(set(found))

    def fetch_cna_health(self, limit: int = 20) -> list[NewsArticle]:
        """Fetch health news from Channel NewsAsia.

        Args:
            limit: Maximum number of articles to fetch

        Returns:
            List of NewsArticle objects
        """
        articles = []
        url = "https://www.channelnewsasia.com/singapore/health"

        try:
            response = self.client.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # Find article cards
            for card in soup.select("article, .card, .list-object")[:limit]:
                title_elem = card.select_one("h3, h2, .title, .headline")
                link_elem = card.select_one("a[href]")

                if not title_elem or not link_elem:
                    continue

                title = title_elem.get_text(strip=True)
                href = link_elem.get("href", "")

                if not href.startswith("http"):
                    href = urljoin("https://www.channelnewsasia.com", href)

                # Skip non-health articles
                if "/health" not in href and "/singapore" not in href:
                    continue

                summary_elem = card.select_one(".summary, .description, p")
                summary = summary_elem.get_text(strip=True) if summary_elem else None

                keywords = self._extract_keywords_from_text(f"{title} {summary or ''}")

                article = NewsArticle(
                    title=title,
                    url=href,
                    source="CNA",
                    summary=summary,
                    keywords=keywords,
                )
                articles.append(article)

        except httpx.HTTPError as e:
            print(f"Error fetching CNA: {e}")

        return articles

    def fetch_straitstimes_health(self, limit: int = 20) -> list[NewsArticle]:
        """Fetch health news from The Straits Times.

        Args:
            limit: Maximum number of articles to fetch

        Returns:
            List of NewsArticle objects
        """
        articles = []
        url = "https://www.straitstimes.com/singapore/health"

        try:
            response = self.client.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # Find article elements
            for card in soup.select("article, .card, .story-card, .views-row")[:limit]:
                title_elem = card.select_one("h3, h2, h5, .card-title")
                link_elem = card.select_one("a[href]")

                if not title_elem or not link_elem:
                    continue

                title = title_elem.get_text(strip=True)
                href = link_elem.get("href", "")

                if not href.startswith("http"):
                    href = urljoin("https://www.straitstimes.com", href)

                summary_elem = card.select_one(".card-body p, .summary")
                summary = summary_elem.get_text(strip=True) if summary_elem else None

                keywords = self._extract_keywords_from_text(f"{title} {summary or ''}")

                article = NewsArticle(
                    title=title,
                    url=href,
                    source="Straits Times",
                    summary=summary,
                    keywords=keywords,
                )
                articles.append(article)

        except httpx.HTTPError as e:
            print(f"Error fetching Straits Times: {e}")

        return articles

    def fetch_today_health(self, limit: int = 20) -> list[NewsArticle]:
        """Fetch health news from TODAY Online.

        Args:
            limit: Maximum number of articles to fetch

        Returns:
            List of NewsArticle objects
        """
        articles = []
        url = "https://www.todayonline.com/singapore"

        try:
            response = self.client.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            for card in soup.select("article, .card, .node")[:limit]:
                title_elem = card.select_one("h2, h3, .title")
                link_elem = card.select_one("a[href]")

                if not title_elem or not link_elem:
                    continue

                title = title_elem.get_text(strip=True)
                href = link_elem.get("href", "")

                if not href.startswith("http"):
                    href = urljoin("https://www.todayonline.com", href)

                # Filter for health-related articles
                health_terms = [
                    "health",
                    "medical",
                    "hospital",
                    "drug",
                    "medicine",
                    "doctor",
                    "patient",
                    "disease",
                    "treatment",
                    "cancer",
                    "diabetes",
                ]
                title_lower = title.lower()
                if not any(term in title_lower for term in health_terms):
                    continue

                keywords = self._extract_keywords_from_text(title)

                article = NewsArticle(
                    title=title, url=href, source="TODAY", keywords=keywords
                )
                articles.append(article)

        except httpx.HTTPError as e:
            print(f"Error fetching TODAY: {e}")

        return articles

    def fetch_all(self, limit_per_source: int = 20) -> list[NewsArticle]:
        """Fetch from all Singapore news sources.

        Args:
            limit_per_source: Maximum articles per source

        Returns:
            Combined list of NewsArticle objects
        """
        all_articles = []

        print("Fetching from CNA...")
        all_articles.extend(self.fetch_cna_health(limit_per_source))

        print("Fetching from Straits Times...")
        all_articles.extend(self.fetch_straitstimes_health(limit_per_source))

        print("Fetching from TODAY...")
        all_articles.extend(self.fetch_today_health(limit_per_source))

        return all_articles

    def filter_relevant(self, articles: list[NewsArticle]) -> list[NewsArticle]:
        """Filter articles to only those with matching keywords.

        Args:
            articles: List of articles

        Returns:
            Filtered list with keyword matches
        """
        return [a for a in articles if a.keywords]

    def close(self):
        """Close the HTTP client."""
        self.client.close()


def main():
    print("=" * 60)
    print("Singapore Health News Fetcher - SgTxGNN")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent.parent
    news_dir = base_dir / "data" / "news"
    news_dir.mkdir(parents=True, exist_ok=True)

    fetcher = SGNewsFetcher()

    try:
        # Fetch all articles
        print("1. Fetching articles from Singapore news sources...")
        articles = fetcher.fetch_all(limit_per_source=20)
        print(f"   Total fetched: {len(articles)}")

        # Filter relevant
        print("2. Filtering for relevant articles...")
        relevant = fetcher.filter_relevant(articles)
        print(f"   Relevant articles: {len(relevant)}")

        # Prepare output
        output = {
            "fetched_at": datetime.now().isoformat(),
            "statistics": {
                "total_fetched": len(articles),
                "relevant": len(relevant),
                "by_source": {},
            },
            "articles": {
                "all": [a.to_dict() for a in articles],
                "relevant": [a.to_dict() for a in relevant],
            },
        }

        # Count by source
        for article in articles:
            source = article.source
            output["statistics"]["by_source"][source] = (
                output["statistics"]["by_source"].get(source, 0) + 1
            )

        # Write output
        output_path = news_dir / "sg_news_latest.json"
        print(f"3. Writing to {output_path}...")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        print()
        print("=" * 60)
        print("News Fetch Complete!")
        print("=" * 60)
        print(f"  Total articles: {len(articles)}")
        print(f"  Relevant articles: {len(relevant)}")
        for source, count in output["statistics"]["by_source"].items():
            print(f"    - {source}: {count}")
        print(f"  Output: {output_path}")

    finally:
        fetcher.close()


if __name__ == "__main__":
    main()
