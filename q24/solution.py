import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quote = soup.find("span", class_="text").get_text(strip=True)
author = soup.find("small", class_="author").get_text(strip=True)

print(f'Цитата: "{quote}". Автор: {author}')
