import requests
from bs4 import BeautifulSoup
from anytree import Node, RenderTree


def process_article_links(article_url, visited_sites = set()):
    article_soup = get_article_soup(article_url)
    related_links = get_related_links(article_soup)
    pprint.pprint(visited_sites)
    for link in related_links:
        print("procesando link: " + link)
        if link in visited_sites:
            pass
        else:
            visited_sites.add(link)
            article_url = link
            return process_article_links(article_url, visited_sites)
        

def get_article_soup(article_url):
    response = requests.get(article_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_related_links(article_soup):
    related_articles_container = article_soup.find(id='wp_rp_first')
    related_articles_links = related_articles_container.find_all('a', class_='wp_rp_thumbnail')
    related_links = []
    for link in related_articles_links:
        related_links.append(link.attrs['href'])
    return related_links


if __name__ == "__main__":
    article_url = "https://www.jotdown.es/2019/05/la-ultima-palabra/"
    process_article_links(article_url)
    
