# Парсинг(скраппинг) сайта zakupki.gov.ru
# Цель работы: составление синонимов каталога закупки каталога компьютерного оборудования и программного обеспечения.
# Использовано в ходе работы: стандартные средства яп "python"

import os
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

def makedir():
    if not os.path.exists(r".\result_parse"):
        os.mkdir(r".\result_parse")
        print(r'Directory for results made...')

def send_request(url):
    # payload parameters = rubricatorIdSelected=373&morphology=on&pageNumber=1&sortDirection=true&recordsPerPage=_10&showLotsInfoHidden=false&sortBy=ITEM_CODE&active=on&consolidated_positions=on
    payload = {'rubricatorIdSelected': '373', 'morphology': 'on', 'pageNumber': '1', 'sortDirection': 'true', 'recordsPerPage': '_10', 'showLotsInfoHidden': 'false', 'sortBy': 'ITEM_CODE',\
               'active': 'on', 'consolidated_positions': 'on'}
    r = requests.get(url, payload)

    ###_DBG_###
    # print(r.url)
    # print(r.text)
    ###_DBG_###

    return r.text

def get_page_data(html):
    arr = []

    #target tag -> [class="d-flex registry-entry__header-mid align-items-center w-space-inherit"]
    soup = BeautifulSoup(html, 'lxml')
    line = soup.find_all('div', class_='d-flex registry-entry__header-mid align-items-center w-space-inherit')  # resolve table
    for l in line:
        print(l.text)
        arr.append(l.text.strip())

    print(arr)


def start():
    url = "https://zakupki.gov.ru/epz/ktru/search/results.html?"
    makedir()
    send_request(url)
    get_page_data(send_request(url))


if __name__ == '__main__':
    start()