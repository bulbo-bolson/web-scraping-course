import requests
from bs4 import BeautifulSoup

page_link = "http://elenq.tech"
file_dest = "elenq_tech.txt"
response = requests.get(page_link)
soup = BeautifulSoup(response.text, 'html.parser')
soup.find('p') # primer elemento p (parrafo)
# podemos anidar busquedas
soup.find('p').find('i') # primer elemento i (italica) dentro del primer p

img = soup.find('img')
# ctype = img.headers["Content-Type"]

