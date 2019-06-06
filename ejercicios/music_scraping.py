import requests
from bs4 import BeautifulSoup
import pprint


def get_results_page_data(results_url):
    page = {}
    soup = BeautifulSoup(requests.get(results_url).text, 'html.parser')
    articles_container = soup.find(id='defaultResultPage')
    page['drum_link_list'] = []
    for article in articles_container.find_all('div', class_='list-view'):
        page['drum_link_list'].append(article.find('a', class_='article-link').attrs['href'])
    last_next_button = soup.find(id='resultPageNavigation').find_all(class_='rs-btn')[-1]
    page['last_next_page'] = last_next_button.get_text()
    print("[debug] nº de links en este result: " + str(len(page['drum_link_list'])))
    return page


def get_drumset_data(drum_url):
    drum = {}
    soup = BeautifulSoup(requests.get(drum_url).text, 'html.parser')
    drum['name'] = soup.find('h1', attrs={"itemprop": "name"}).get_text()
    drum['price'] = soup.find('div', class_='prod-pricebox-price').find(class_='primary').get_text()
    return drum
    


if __name__ == "__main__":
    results_url = "https://www.thomann.de/es/sets_de_bateria.html"
    page = get_results_page_data(results_url)
    for drum_link in page['drum_link_list']:
        drum = get_drumset_data(drum_link)
        print(drum)

            
        
