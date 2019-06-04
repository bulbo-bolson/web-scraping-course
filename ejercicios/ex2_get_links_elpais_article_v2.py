import requests
from bs4 import BeautifulSoup


def get_all_links(soup):
    # retorna una lista con todos los links
    all_links = soup.find_all(href=True)
    return all_links


if __name__ == "__main__":
    page_link = "https://elpais.com/politica/2019/06/03/actualidad/1559578563_330390.html"
    response = requests.get(page_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in get_all_links(soup):
        print("=======================================================")
        print("texto: " + link.get_text())
        # los atributos estan en un diccionario
        # el href es uno de esos atributos
        # podemos acceder a los datos del diccionario asi:
        print("link:" + link['href'])