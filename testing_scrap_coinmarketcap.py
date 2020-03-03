'''
1. Парсер однопоточный.
2. Замер времени
3. Multiprocessing Pool
4. Замер времени
5. Экспорт в csv
'''
import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url) # Response
    return r.text # Возвращает HTML-код страницы(url)

def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')

    tegs_td = soup.find('table').find_all('td', class_="cmc-table__cell") #td class="cmc-table__cell"

    links = []
    for td in tegs_td:
        a = td.find('a').get('href') #string
        links.append(a)

    return links


def main():
    url = "https://coinmarketcap.com/all/views/all/"
    all_links = get_all_links(get_html(url))

    for i in all_links:
        print(i)





if __name__ == "__main__":
    main()

