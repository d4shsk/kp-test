import requests
from bs4 import BeautifulSoup

url = "https://habr.com/ru/companies/gnivc/news/1037538/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("h1").get_text(strip=True)
author = soup.find("a", class_="tm-user-info__username").get_text(strip=True)
date = soup.find("time")["datetime"]

print(f"Название: {title}")
print(f"Автор: {author}")
print(f"Дата: {date}")
