"""
Login via automate
    required: selenium, webdriver_Chrome
    website: https://github.com
    author: D3coy
"""

import selenium
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def wr_cred(driver, login = "", passw = ""):
    elem_login = driver.find_element_by_xpath("//*[@id=\"login_field\"]")  # fields search
    elem_passwd = driver.find_element_by_xpath("//*[@id=\"password\"]")

    action = ActionChains(driver)
    action.move_to_element(elem_login)
    action.perform()

    elem_login.clear()  # for next iter enter
    elem_login.send_keys (login)
    elem_login.send_keys (Keys.TAB)

    elem_passwd.send_keys (passw)
    elem_passwd.send_keys (Keys.RETURN)

def main():
    driver = selenium.webdriver.Chrome (r'drivers\chromedriver.exe')
    driver.get ('https://github.com/login')
    wr_cred (driver, "", "")    # login, passw params
    flag = True     # one time at least

    while flag:
        try:
            flag = driver.find_element_by_xpath("//*[@id=\"js-flash-container\"]/div")
        except:
            flag = False
            continue

        print("Wrong credentials, try again")
        login = input("Enter login: \n")
        passw = input("Enter password: \n")
        wr_cred(driver, login, passw)

    print("Authorization success")
    driver.close()

if __name__ == '__main__':
    main()
