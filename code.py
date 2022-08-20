from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

raw="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.chrome(u'C:/Users/pchit/Downloads/chromedriver_win32')
browser.get(raw)

def scrape():
    headers=["Proper_Name","Distance", "Mass","Radius"]
    data=[]
    # for i in range(0,204):
    soup=BeautifulSoup(browser.page_source,"html.parser")
    for ul in soup.find_all("ul",attrs={"class","mw-redirect"}):
        li=ul.find_all("li")
        temp=[]
        for index,lit in enumerate(li):
            if index==0:
                temp.append(lit.find_all("a")[0].contents[0])
            else:
                try:
                    temp.append(lit.contents[0])
                except:
                    temp.append("")
            data.append(temp)
        # browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("Output.csv","w",encoding="utf-8") as file:
        csvd=csv.writer(file)
        csvd.writerow(headers)
        csvd.writerows(data)

scrape()