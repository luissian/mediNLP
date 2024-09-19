# medi_nlp/cli.py

from medi_nlp.scraper import Scraper
from medi_nlp.analyzer import Analyzer
# from medi_nlp.utils import send_email

def main():
    base_url = "https://www.medicalnewstoday.com"
    article_url = "/articles/fever-causes"  # Example article URL path

    scraper = Scraper(base_url)
    analyzer = Analyzer()

    # Fetch and analyze article
    article_text = scraper.fetch_article(article_url)
    entities = analyzer.analyze_text(article_text)

    # Display results
    print("Patients Found:", entities['patients'])
    print("Illnesses Found:", entities['illnesses'])
    print("Fever Mentions:", entities['fever_mentions'])

    # Example condition for sending an email alert

    """ 
    if len(entities['patients']) > 5 or entities['fever_mentions'] > 10:
        send_email(
            subject="Alert: High Fever Mentions or Patients Found",
            body=f"Patients: {len(entities['patients'])}, Fever Mentions: {entities['fever_mentions']}",
            recipient_email="recipient@example.com"
        )
     """