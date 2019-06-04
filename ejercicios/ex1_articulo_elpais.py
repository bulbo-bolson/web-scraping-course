import requests
from bs4 import BeautifulSoup



def get_article_title_text(soup):
    # el titulo del articulo esta en el id: articulo-titulo
    article_title = soup.find(id="articulo-titulo")
    article_title_text = article_title.get_text()
    return article_title_text

def get_paragraphs_contents(soup):
    # retorna en una lista cada parrafo
    paragraphs = soup.find_all('p')
    return paragraphs

if __name__ == "__main__":
    page_link = "https://elpais.com/politica/2019/06/03/actualidad/1559578563_330390.html"
    response = requests.get(page_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    print("titulo del articulo: " + get_article_title_text(soup))
    for p in get_paragraphs_contents(soup):
        print ("parrafo nuevo: " + p.get_text())
        print ("======================================")

