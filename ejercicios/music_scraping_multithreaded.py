import requests
from bs4 import BeautifulSoup
import json
import multiprocessing
from itertools import product

## NO RULA


def scrap_page(results_url = "https://www.thomann.de/es/sets_de_bateria.html", pg = '1'):
    RESULT_LIMIT = 25
    page_params = {'pg' : pg, 'ls' : RESULT_LIMIT}
    print("results_url " + results_url)
    page = get_results_page_data(results_url, url_params=page_params)
    drums = []
    for drum_link in page['drum_link_list']:
        drum = get_drumset_data(drum_link)
        print(drum)
        drums.append(drum)
    return drums


def get_results_page_data(results_url, url_params = {}):
    page = {}
    print("[debug] parseando: " + results_url + str(url_params))
    soup = BeautifulSoup(requests.get(results_url, params=url_params).text, 'html.parser')
    articles_container = soup.find(id='defaultResultPage')
    page['drum_link_list'] = []
    for article in articles_container.find_all('div', class_='list-view'):
        page['drum_link_list'].append(article.find('a', class_='article-link').attrs['href'])
    last_next_button = soup.find(id='resultPageNavigation').find_all(class_='rs-btn')[-1]
    page['last_next_page'] = int(last_next_button.get_text())
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
    page_1 = get_results_page_data(results_url)
    counter = 1
    all_drums = []
    next_page_links = list(range(1, page_1['last_next_page']))
    next_page_links = map(str, next_page_links)
    print(next_page_links)
    with multiprocessing.Pool(processes=10) as pool:
        results = pool.starmap(scrap_page, results_url, product(next_page_links, repeat=2))
    # pool.map(lambda p: scrap_page(p, url_params={'pg': counter}), )
    # pool.map(lambda p: scrap_page(p, {'pg': counter}), range(1, page_1['last_next_page']))
    # print(json.dumps(all_drums))
'''
    while counter <= int(page_1['last_next_page']):
        proc = Process(target=scrap_page, args=({'pg': counter}))
        # all_drums.append(scrap_page(results_url, url_params={'pg': counter}))
        print(proc)
        proc.start()
        proc.join()
        counter += 1
'''
            
        
