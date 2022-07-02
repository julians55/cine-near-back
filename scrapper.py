from bs4 import BeautifulSoup
import requests

url = 'https://www.google.com/search?q=peliculas+en+cartelera+hoy'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


mov = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
movies = list()

for i in mov:
    if mov.index(i)<10:
        movies.append(i.text)

