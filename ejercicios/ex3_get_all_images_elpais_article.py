import requests
from bs4 import BeautifulSoup
import os
import re

def get_all_images(soup):
    # retorna una lista con todos los links
    all_images = soup.find_all('img')
    return all_images

def get_image_url(img):
    url = ""
    if 'data-src' in img.attrs:
        url = get_absolute_path(img['data-src'])
    elif 'data-custom-lazyload-src' in img.attrs:
        url = get_absolute_path(img['data-custom-lazyload-src'])
    else:
        raise RuntimeError('Url no encontrada para la imagen' + img['alt'])
    return url

def get_absolute_path(url):
    if re.search("^/[a-z]", url):
        url = "https://elpais.com" + url
        return url
    if not url.startswith('http://'):
        url = "http://" + re.sub(r'^//', '', url)
        return url
    else:
        return url


if __name__ == "__main__":
    page_link = "https://elpais.com/politica/2019/06/03/actualidad/1559578563_330390.html"
    response = requests.get(page_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    dest_dir = 'imagenes_articulo'
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    counter = 1
    for img in get_all_images(soup):
        dest_file = dest_dir + "/" + str(counter) + ".jpg"
        print("downloading image in file " + dest_file)
        url = get_image_url(img)
        print("url: " + url)
        downloaded_image = requests.get(url)
        with open(dest_file, "wb") as f:
            f.write(downloaded_image.content)
            counter += 1




