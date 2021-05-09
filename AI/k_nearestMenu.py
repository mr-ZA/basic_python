import numpy as np
import os
import time
import sys
import pandas
import re
from tir import Webapp
from pathlib import Path
from pprint import pprint
from datetime import date
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import tir.technologies.core.enumerations as enum
from selenium.webdriver.common.action_chains import ActionChains

class menu:
    def load_fromFile(self):
        path_to_json = os.path.join(Path(os.path.abspath(sys.modules[Webapp.__module__].__file__)).parent, 'technologies', 'core', 'data', 'helper')
        self.trained_rData_arrs = []

        for eachFile in os.listdir(path_to_json):
            data_fromFile = []
            self.loaded_data = []
            
            with open(os.path.join(path_to_json, eachFile), "r") as data_file:
                data_fromFile = data_file.read().split("\n")
                data_fromFile_copy = list(data_fromFile)
                flag = True
                length_fileData = len(data_fromFile)
                counter = 0

                while(flag):
                    # Last
                    if data_fromFile[counter - 1] == data_fromFile_copy[-2] and counter > 0:
                        flag = False
                        data_fromFile.pop(counter)      # remove last
                        continue
                    
                    # Cut empty elems = <' '>
                    if data_fromFile[counter] == "":
                        data_fromFile.pop(counter)
                        length_fileData -= 1
                    else:
                        # Mapping data 4om file (need to optimize in future)
                        self.loaded_data.append(data_fromFile[counter].split("->"))
                        self.loaded_data[counter][0] = self.loaded_data[counter][0].strip()
                        self.loaded_data[counter][1] = re.sub("[{}]", "", self.loaded_data[counter][1]).strip()
                        self.loaded_data[counter][1] = self.loaded_data[counter][1].split(", ")
                        
                        # coords [X:Y] of webelement saving for further calculations
                        self.loaded_data[counter].append("")
                        self.loaded_data[counter][2] = [int(self.loaded_data[counter][1][2].split(":")[1]), int(self.loaded_data[counter][1][3].split(":")[1])]

                        counter += 1
            exec(f"self.loaded_data_{eachFile[:-5].lower()} = {self.loaded_data}")          # every file for self-named list
            self.trained_rData_arrs.append(f"self.loaded_data_{eachFile[:-5].lower()}")     # list of knowledge

        return


    def save_inFile(self, data):
        path_to_json = os.path.join(Path(os.path.abspath(sys.modules[Webapp.__module__].__file__)).parent, 'technologies', 'core', 'data', 'helper')
        
        # Save data from DOM 4or learning
        synapse_file = os.path.join(path_to_json, f'{self.routine}.json')
        with open(synapse_file, "w") as data_file:
            for elem in data:
                if elem == "":
                    continue
                else:
                    for attr in range(len(elem) - 1):
                        data_file.write(f"\n{elem[attr]} -> {elem[attr+1]}\n")
            return

    def bin_search(self, value_r):
        # gap from 0..29 for values
        self.values = [x for x in range(30)]
        value_r = int(value_r)
        left_border = 0
        right_border = len(self.values) - 1
        founded = 0

        while left_border <= right_border:
            mid = (left_border + right_border) // 2
            guess = self.values[mid]
            if value_r > guess:
                left_border = mid + 1
            elif value_r < guess:
                right_border = mid - 1
            elif value_r == guess:
                founded += 1
                break
        if founded > 0:
            return True
        else:
            return False

    def click_menu(self, elements):
        memory = []
        el = elements()
        for label in range(len(el)):
            memory.append(["RECT_ELEMENT", elements()[label].rect])
            results = self.k_function(elements()[label])
            if results > 2:
                time.sleep(2)
                elements()[label].click()
                
                menu_child = lambda: self.ac.driver.find_element_by_xpath("(//div/label[contains(text(), \"•\")])[2]")
                time.sleep(2)
                menu_child().click()
                pass
            else:
                continue


    def dom_getTags(self, tag, flag, menu_learnlabel= ""):
        try:
            menu_detector = wait(self.ac.driver, 240).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(), \"Найт\")]"))
            )
        except:
            menu_detector = ""
        
        time.sleep(2)
        labels_screened = lambda: self.ac.driver.find_elements_by_xpath("//img/preceding::div/div[contains(@class, \"tmenu\")]//label")
        
        if flag:
            memory = []
            time.sleep(2)
            very_menu_label_4compare = self.ac.driver.find_element_by_xpath(f"//label[text() = \"{menu_learnlabel}\"]")   # mata010
            memory.append(["MENU_ELEMENT", very_menu_label_4compare.rect])
            self.save_inFile(data= memory)
        elif flag == False:
            return labels_screened
            

    def ma3_tearDown(self):
        time.sleep(2)
        ActionChains(self.ac.driver).send_keys(Keys.ESCAPE).perform()

        time.sleep(1)
        self.oHelper.TearDown()
        return

    def ma3_startEnv(self, lf, ll, **kwargs):
        self.oHelper = Webapp(autostart= True)
        self.ac = self.oHelper.GiveMeAccess()
        
        for m, r in kwargs.items():
            self.routine = r
            self.oHelper.Setup(m, str(date.today().strftime("%d/%m/%Y")), "00", "10", "01")
            self.oHelper.Program(r)
            time.sleep(15)
            
            if lf:
                time.sleep(2)
                labels = self.dom_getTags(tag= "label", menu_learnlabel= ll, flag= lf)
            elif not lf:
                time.sleep(2)
                labels = self.dom_getTags(tag= "label", flag= lf)
                self.click_menu(elements= labels)
            else:
                continue


    def k_function(self, label_compare):
        self.calc_knearest = []
        correct_counter = 0
        
        x_rCoord = label_compare.rect["x"]   # coord of menu in exec time
        y_rCoord = label_compare.rect["y"]
        for fileData in self.trained_rData_arrs:
            for elem in eval(fileData):
                x_mCoord = elem[2][0]
                y_mCoord = elem[2][1]
                current_distance = (pow(x_rCoord - x_mCoord, 2) + pow(y_rCoord - y_mCoord, 2))**0.5
                self.calc_knearest.append(current_distance)
            for ck in self.calc_knearest:
                if self.bin_search(ck):
                    correct_counter += 1
                    break
                else:
                    continue
        return correct_counter


    def initailize(self):
        # ----- LEARNING -----
        # memory = self.ma3_startEnv(lf= True, ll= "Управление закупками (1)", SIGACOM="MATA010")
        # time.sleep(1)
        # self.ma3_tearDown()
        
        # memory = self.ma3_startEnv(lf= True, ll= "Основные средства (1)", SIGAATF="ATFA025")
        # time.sleep(1)
        # self.ma3_tearDown()

        # memory = self.ma3_startEnv(lf= True, ll= "Управление закупками (1)", SIGACOM="MATA020")
        # time.sleep(1)
        # self.ma3_tearDown()

        # ----- EXECUTING -----
        self.load_fromFile()
        #self.ma3_startEnv(SIGACOM="MATA101N", lf= True, ll= "")       # for example execution of routine in test file
        #self.ma3_startEnv(SIGAFAT="MATA467N", lf= True, ll= "")       # for example execution of routine in test file
        
        self.ma3_startEnv(SIGAATF="ATFA050", lf= False, ll= "")       # for example execution of routine in test file
        self.ma3_tearDown()


mo = menu()
mo.initailize()