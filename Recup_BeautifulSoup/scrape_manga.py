import requests
from bs4 import BeautifulSoup
import time

base_url = "https://manga-scantrad.io/manga/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}

def fetch_and_parse_page(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def scrape_manga_titles():
    soup = fetch_and_parse_page(base_url)
    
    if soup:
        manga_titles = soup.find_all('h3', class_='h5 font-weight-semibold text-dark text-hover-primary mb-2')
        
        for index, title in enumerate(manga_titles):
            print(title.get_text(strip=True))
            
            if index < len(manga_titles) - 1:
                print("Waiting for 10 seconds to respect Crawl-delay...")
                time.sleep(10)

if __name__ == "__main__":
    scrape_manga_titles()
