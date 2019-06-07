import requests
from bs4 import BeautifulSoup
import json


def get_results_page_data(results_url, url_params = {}):
    page = {}
    print("[debug] parseando: " + results_url + str(url_params))
    soup = BeautifulSoup(requests.get(results_url, params=url_params).text, 'html.parser')
    articles_container = soup.find(id='defaultResultPage')
    page['drum_link_list'] = []
    for article in articles_container.find_all('div', class_='list-view'):
        page['drum_link_list'].append(article.find('a', class_='article-link').attrs['href'])
    last_next_button = soup.find(id='resultPageNavigation').find_all(class_='rs-btn')[-1]
    page['last_next_page'] = last_next_button.get_text()
    print("[debug] nº de links en este result set: " + str(len(page['drum_link_list'])))
    return page


def get_drumset_data(drum_url):
    drum = {}
    soup = BeautifulSoup(requests.get(drum_url).text, 'html.parser')
    drum['name'] = soup.find('h1', attrs={"itemprop": "name"}).get_text()
    drum['price'] = soup.find('div', class_='prod-pricebox-price').find(class_='primary').get_text()
    return drum
    

if __name__ == "__main__":
    results_url = "https://www.thomann.de/es/sets_de_bateria.html"
    RESULT_LIMIT = 25
    page_1 = get_results_page_data(results_url)
    counter = 1
    all_drums = []
    while counter <= int(page_1['last_next_page']):
        next_page_params = {'pg' : counter, 'ls' : RESULT_LIMIT}
        next_page = get_results_page_data(results_url, url_params=next_page_params)
        for drum_link in next_page['drum_link_list']:
            drum = get_drumset_data(drum_link)
            print(drum)
            all_drums.append(drum)
        counter += 1
    print(json.dumps(all_drums))
            
        
