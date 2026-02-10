# crawl web pages
import requests
from bs4 import BeautifulSoup

def crawl_url(url):
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    for tag in soup.find_all(['script', 'style', 'nav', 'footer', 'header', 'aside']):
        tag.decompose()

    text = " ".join(soup.stripped_strings)
    return {
        "url": url,
        "text": text
    }