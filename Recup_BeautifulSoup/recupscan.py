import requests
from bs4 import BeautifulSoup
import time

url = "https://manga-scantrad.io/manga/"

response = requests.get(url)
print(response)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    manga_elements = soup.find_all("h3", class_="manga-title")

    manga_names = [manga.get_text().strip() for manga in manga_elements]
    
    for name in manga_names:
        print(name)
        time.sleep(10)
else:
    print("Erreur")
