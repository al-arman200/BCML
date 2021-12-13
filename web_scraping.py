from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import os
import datetime


class WebScraping:
    def __init__(self, url):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(url)#'https://divar.ir/s/tehran-province/car'
    
    def save(self,txt,address): #for write link and post to file.txt
        date = datetime.datetime.now()
        sdate= str(date)
        if os.path.isfile(address):
            f = open(address, 'a', encoding="utf-8")
        else:
            f = open(address , 'w+', encoding="utf-8")
        f.write(txt)
        f.close()


    def get_thumbnails(self , tag):
        try:
            piclink=tag.contents[1].contents[0].contents[0].contents[1]
            pngsrc = piclink['src']
            if 'https' in  pngsrc :
                return pngsrc
            else:
                sleep(2)  
                self.get_thumbnails(tag)
        except:
            return 'null'

    def get_Link(self):
        linklist = list()
        for j in range(9999):
            soup = BeautifulSoup(self.driver.page_source)
            a=soup.find_all('a',attrs={'class':'kt-post-card kt-post-card--outlined kt-post-card--has-chat'})
            for i in a:
                link=i.attrs['href']
                name=i.contents[0].contents[0].text
                piclink = self.get_thumbnails(i)
                if not(name in  linklist):
                    linklist.append(name)
                    linkdes = '"%s","https://divar.ir%s","%s" \n'%(name, link, piclink)
                    self.save(linkdes,'links.csv')
                    print('https://divar.ir%s'%link)
            self.driver.execute_script("window.scrollTo(0,600*%s);"%j)
            sleep(1)
        print(linklist)

scraping = WebScraping('https://divar.ir/s/tehran-province/car')
scraping.get_Link()
