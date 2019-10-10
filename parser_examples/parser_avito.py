import requests   # получает html код и возвращает в функцию
from bs4 import BeautifulSoup
import csv

# получает ответа от сервера
def get_html(link_to_avtocatalog):
    r = requests.get(link_to_avtocatalog)   # ответ сервера
    return r.text   # возвращает html код страницы

def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        h3s = soup.find('div', class_='js-catalog_serp').find_all('h3', class_='title item-description-title')     # разница find и find_all
    except AttributeError:
        print(html)
    links = []
    for h3 in h3s:
        a = h3.find('a', class_="item-description-title-link").get('href')
        link = "https://www.avito.ru" + a
        links.append(link)
    return links

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    name = soup.find('span', class_="title-info-title-text").text

    price = soup.find('span', class_="js-item-price").text

    data = {'name': name, 'price': price}
    return data

def write_csv(data):
    with open('avitoauto.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['name'], data['price']))
        print(data['name'], data['price'])

def main():
    link_to_avtocatalog = "https://www.avito.ru/noyabrsk/avtomobili"
    all_links = get_all_links(get_html(link_to_avtocatalog))
    try:
        for link_to_avtocatalog in all_links:
            html = get_html(link_to_avtocatalog)
            data = get_page_data(html)
            write_csv(data)
    except:
        print("\n____________________Banned____________________")
        return


if __name__ == '__main__':
    main()
