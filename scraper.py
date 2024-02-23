# Adjusted from soup_test.py to make it easily callable from the api.py

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.error

def scrapeGlossary(url):
    try:
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        return scraper(soup)
    except urllib.error.HTTPError as e:
        raise Exception(f"HTTP Error: {e.code} {e.reason}")
    except urllib.error.URLError as e:
        raise Exception(f"URL Error: {e.reason}")
    
def scraper(soup):
    glossary = {}
    sections = soup.find_all('dl')

    for section in sections:
        words = section.find_all('dt')
        for word in words:
            check = word.find_next('dd')
            definition = check.text.strip()
            while check.find_next(['dt', 'dd']) is not None and (check.find_next(['dt', 'dd']).text.strip() == check.find_next('dd').text.strip()):
                # see if next item in section is another word or more definition
                check = check.find_next(['dd'])
                for item in check.ul.contents:
                    definition = definition + item.text.strip()
            glossary[word.text.strip().lower()] = definition.lower()
    return glossary