from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import os
import datetime


class WebScraping:
    def __init__(self), url:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)#'https://divar.ir/s/tehran-province/car'
    
    def save(self,txt,address): #for write link and post to file.txt
        date = datetime.datetime.now()
        sdate= str(date)
        if os.path.isfile(address):
            f = open(address, 'a', encoding="utf-8")
        else:
            f = open(address , 'w+', encoding="utf-8")
        f.write(txt)
        f.close()
