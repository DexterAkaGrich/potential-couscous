'''
1. Парсер однопоточный.
2. Замер времени
3. Multiprocessing Pool
4. Замер времени
5. Экспорт в csv
'''
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from multiprocessing import Pool
import csv
import time


def get_html(url):
    r = requests.get(url) # Response
    return r.text # Возвращает HTML-код страницы(url)

def get_all_links(html):
    counter = 0

    soup = BeautifulSoup(html, 'lxml')

    tags_div = soup.find('div').find_all('div', class_="cmc-table__column-name sc-1kxikfi-0 eTVhdN")


    links = []
    for td in tags_div:
        a = td.find('a').get('href') #string
        link = "https://coinmarketcap.com" + a
        links.append(link)

    return links

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    try:
        name = soup.find("h1").text.strip()
    except:
        name = ""

    try:
        price = soup.find("span", class_="cmc-details-panel-price__price").text.strip()
    except:
        price = ""
    data = {'name': name, 'price': price}

    return data

def write_csv(data):
    with open('coinmarketcap.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['name'],
                         data['price']))

        print(data['name'], 'parsed')


def make_all(url):
    html = get_html(url)
    data = get_page_data(html)
    write_csv(data)
    # time.sleep(5)


def main():
    start = time.time()

    url = "https://coinmarketcap.com/all/views/all/"
    all_links = get_all_links(get_html(url))

    with Pool(40) as p:
        p.map(make_all, all_links)


    end = time.time()
    total = end - start
    print(str(total))

if __name__ == "__main__":
    main()

