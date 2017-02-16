from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os
import time
import re
import sys

starturl = 'http://www.looperman.com/loops?page=1&keys=guitar&dir=d'
firsturl = 'http://www.looperman.com/loops?page='
posturl = '&keys=guitar&dir=d'

helpmsg = ''' 
                    usage :  python3 looperman_spider.py  <last_page_number>
                    by default it will scrapy the first 50 pages
                    '''

def Help():
    print(helpmsg)

'''
def findAndDownloadFiles():
    for i in range(13):
        cururl = firsturl + str(i+1) + posturl
        driver.get(cururl)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        divs = soup.findAll("a", { "class" : "btn-download" })
        for div in divs:
            if div['href']:
                driver.get(div.a['href'])
                html = driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                targetdiv = soup.find('a', attrs={'class' : 'btn-download'})
                audio_url = targetdiv['href']
                titlediv = soup.find('a', attrs={'class' : 'player-title'})
                filename = titlediv.text
                save_file(audio_url,filename)


def save_file( url, file_name):  ##保存图片
        print('开始请求图片地址，过程会有点长...')
        file = request(url)
        print('开始保存图片')
        f = open(file_name, 'ab')
        f.write(file.content)
        print(file_name, '图片保存成功！')
        f.close()       

def request(url):  # 封装的requests 请求
        r = requests.get(url)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        return r        
'''

def FindAndDownloadFilesByBrowserClick():
    for i in range(lastpage_num):
        cururl = firsturl + str(i) + posturl
        print('currenturl:' + cururl)
        driver.get(cururl)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        divs = soup.findAll("a", { "class" : "btn-download" })
        for div in divs:
            if div['href']:
                driver.get(div['href'])
                elem = driver.find_element_by_class_name('btn-download')
                elem.click()
                time.sleep(7)

def  rename(path):
    os.chdir(path)
    pat = re.compile('looperman-l-(\\w+-){3}')
    for name in os.listdir() :        
        if len(re.split(pat,name)) == 3:
            print('current name:' + name)
            newname = re.split(pat,name)[2]
            print('new name:' + newname)
            os.rename(name,newname)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        lastpage = 50
    else :
        try :
            lastpage = sys.argv[1]
            assert lastpage.isdigit() 
            lastpage_num = int(lastpage)           
        except :
            print('lastpage must by a number!')
            Help()
            exit()

    fp = webdriver.FirefoxProfile()

    fp.set_preference("browser.download.folderList",2)
    fp.set_preference("browser.download.manager.showWhenStarting",False)
    fp.set_preference("browser.download.dir", os.getcwd())
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-msdos-program")

    driver = webdriver.Firefox(firefox_profile=fp)
    driver.get(starturl)

    input('you must log in manually  , then  press anykey to continue...') 
    FindAndDownloadFilesByBrowserClick()

    
