# tests/test_scraper.py
from medi_nlp.scraper import fetch_articles

def test_fetch_articles():
    url = "https://www.medicalnewstoday.com/"
    articles = fetch_articles(url)
    assert len(articles) > 0, "No articles fetched from the homepage."
