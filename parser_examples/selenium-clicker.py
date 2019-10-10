import requests
from bs4 import BeautifulSoup
import os
import shutil
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

def mkdir_cmd():
    if not os.path.exists(r".\results"):
        os.mkdir(r".\results")
        print(r'Dir made')

def get_html(site):
    r = requests.get(site)
    return r.text

def get_page_data(html):                         #sources
    soup = BeautifulSoup(html, 'lxml')           #(format_in, parser)
    file = open('results\parsed-4click.txt', 'w+')

    for link in soup.find_all("a", attrs={"title":"Подгузники Predo Baby Премиум 1 новорожденный"}):		#print(soup.find("a",attrs={"class":"tweet-timestamp js-permalink"})["title"])
    	print(link["href"])

    	driver = webdriver.Firefox(executable_path=r'./geckodriver')
    	driver.get('https://yandex.ru/')
    	driver.find_element_by_link_text("Новости").click()

    	#if (link[2] == "Подгузники Predo Baby Премиум 1 новорожденный"):
    	#	print (link.get('href'))


def main():
    url = 'http://predobaby.ru/?product_cat=%d0%bf%d0%be%d0%b4%d0%b3%d1%83%d0%b7%d0%bd%d0%b8%d0%ba%d0%b8'
    mkdir_cmd()
    get_page_data(get_html(url))

if __name__ == '__main__':
        main()


"""
---FOR FIREFOX--------------------------------------------------------------------------------
    Перейдите на страницу выпусков geckodriver . Найдите последнюю версию драйвера для своей платформы и загрузите его. Например:

     wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz 

    Извлеките файл с помощью:

     tar -xvzf geckodriver* 

    Сделайте его исполняемым:

     chmod +x geckodriver 

    Добавьте драйвер в свой PATH, чтобы другие инструменты могли его найти:

     export PATH=$PATH:/path-to-extracted-file/geckodriver 

Есть много способов сделать это, что будет работать. Вышеупомянутое работает для меня на Ubuntu 16.10 64-бит. 

+

from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'your\path\geckodriver.exe')
driver.get('http://inventwithpython.com')
--------------------------------------------------------------------------------------------
"""
