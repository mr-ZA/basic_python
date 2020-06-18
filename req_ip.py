import requests
import os
import re
from lxml import html
from platform import uname

def write_2_file(data):
    sys_info = (uname())

    #_______________CREATE DIR_________________________
    try:
        print("Platfom detected: %s_%s  " % (sys_info[0], sys_info[2]))
        if sys_info[0] == "Windows":
            dirc = ".\ip_response"
            os.makedirs(dirc)
        if sys_info[0] == "Linux":
            dirc = "./ip_response"
            os.makedirs(dirc)
    except FileExistsError:
        print("[INFO] Directory exists")

    # _______________CREATE FILE IN DIR________________
    try:
        with open(os.path.join(dirc, 'ip_router.txt'), 'w+', encoding='utf-8') as memory:
            print("\n")
            print("[INFO] Writing memory storage..")
            try:
                memory.write(data)
                print("[INFO] Written succesfully!")
            except Exception as e:
                print(e)
                print("[ERROR] Couldn't write to the file -> {}".format(e))

    except FileNotFoundError:
        print("[ERROR] No such file inside {}".format(dirc))
        print("[INFO] Creating file..")
        with open(os.path.join(dirc, 'ip_router.txt'), 'a', encoding='utf-8') as memory:
            memory.write('')  # Create file
        write_2_file(data)

# get from html -> xpath + re = ip
def parse_ip():
    www_data = html.fromstring(req_ip())
    ip_router = www_data.xpath("//p[text()]")
    ip_router = ip_router[0].text_content()
    ip_router = (re.search('(Result: )(\S*)', ip_router)).group(2)
    return(ip_router)

def req_ip():
    request = requests.Session()

    # update user-agent for requesting confidence
    request.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    })
    address = "http://iplookup.asus.com/nslookup.php"
    param = {"hostname": "wifi-1899092020"}
    result = request.post(address, data=param)


    return result.text

if __name__ == '__main__':
    ip_router = parse_ip()
    write_2_file(ip_router)