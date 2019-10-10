import requests
from bs4 import BeautifulSoup
import os
import shutil

def mkdir_cmd():
    if not os.path.exists(r".\results"):
        os.mkdir(r".\results")
        print(r'Dir made')

def get_html(site):
    r = requests.get(site)
    return r.text

def get_page_data(html):                         #sources
    soup = BeautifulSoup(html, 'lxml')           #(format_in, parser)

    line = soup.find('table', id='theProxyList').find_all('tr')     #resolve table
    file = open('results\parsed.txt', 'w+')

    for tr in line:
        td = tr.find_all('td')
        if td == []:
            continue
        ip = td[1].text
        port = td[2].text
        country = td[3].text.replace('\xa0', '')
        anonym = td[4].text.replace('\r\n        ', '')
        types = td[5].text.replace('\r\n\t\t\t\t\t', '').replace('\r\n        ', '')
        time = td[6].text
        file.write('[ip: ' + ip + '] [Port: ' + port + '] [Country: ' + country + '] [Anonymize: ' + anonym + '] [Type: ' + types + '] [Time: ' + time + ']' +'\n')

        data = {'ip': ip,
                'Port': port,
                'Country': country,
                'Anonymize': anonym,
                'Type': types,
                'Time': time}
        print (data)
    file.close()



def main():
    url = 'http://foxtools.ru/Proxy'
    mkdir_cmd()
    get_page_data(get_html(url))

if __name__ == '__main__':
        main()
