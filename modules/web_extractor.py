import wikipedia
import requests
from bs4 import BeautifulSoup
import re

def extract_web_text(source):
    text = ""
    
    if not source.startswith("https"):
        try:
            wikipedia.set_lang("en")
            page = wikipedia.page(source)
            text = page.content
            print(f"Extracted Wikipedia article: {page.title()}")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Multitiple files found. Top option: {e.options[:5]}")
            return ""
        except wikipedia.exceptions.PageError:
            print(f"Wikipedia page not found for: {source}")
            return ""
        except Exception as e:
            print(f"Wikipedia error: {e}")
            return  ""
    else:
        try:
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(source, headers=header)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'lxml')

            for tag in soup(["script", "style", "nav", "header", "footer"]):
                tag.decompose()

            text_elements = soup.find_all(['p', 'article', 'div'], class_=re.compile(r"content|body|main|article"))
            for elements in text_elements:
                text += elements.get_text() + " "

            text = re.sub(r'\s', ' ', text).strip()

            print(f"Scraped text from URL: {source}")
        except requests.exceptions.RequestException as e:
            print(f"Web request error: {e}")
            return ""
        except Exception as e:
            print(f"Scraping error: {e}")
            return ""
    return text