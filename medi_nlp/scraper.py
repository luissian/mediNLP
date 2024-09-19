# medi_nlp/scraper.py
import requests
from bs4 import BeautifulSoup

class Scraper ():
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_articles(self, article_url):
        full_url = self.base_url + article_url
        response = requests.get(full_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.find_all('a', class_='css-glf3vc')
            article_data = [(article.get_text(), 'https://www.medicalnewstoday.com' + article['href']) for article in articles]
            return article_data
        else:
            raise Exception(f"Failed to fetch article from {full_url}")

    def _extract_text(sself, soup):
        """
        Extracts the main article text from the HTML soup.
        """
        # Assuming the main content is within <p> tags, adjust this based on actual structure
        paragraphs = soup.find_all('p')
        article_text = ' '.join([p.get_text() for p in paragraphs])
        return article_text                                                                                                                                                                             


