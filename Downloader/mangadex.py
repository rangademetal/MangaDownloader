from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import secrets
import time
import urllib.request
import random
import os

class Mangadex:
    def __init__(self, path):
        self.path = path
        self.driver = webdriver.Chrome(self.path)
        self.driver.get('https://mangadex.org/')
        self.driver.maximize_window()

    # serching manga
    def login(self):
        login = self.driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[2]/li[2]/a')
        login.click()
        login = self.driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[2]/li[2]/div/a[1]/span')
        login.click()
        # login access
        login = self.driver.find_element_by_xpath('//*[@id="login_username"]')
        login.click()
        login.send_keys('guest123qwe')
        login = self.driver.find_element_by_xpath('//*[@id="login_password"]')
        login.click()
        login.send_keys('guest123qwe')
        login = self.driver.find_element_by_xpath('//*[@id="login_button"]/span')
        login.click()

    def search(self, manga):
        # accesing and find with xpath
        time.sleep(2)
        search = self.driver.find_element_by_xpath('//*[@id="quick_search_input"]')
        search.click()

        # Enter your manga names on search bar and click it
        search.send_keys(manga)
        search = self.driver.find_element_by_xpath('//*[@id="quick_search_button"]/span')
        search.click()

        # click the first manga when the name is similar with manga parameter
        search = self.driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/div[1]/a/img')
        search.click()


        # Getting manga
    def DownloadSelectedChapter(self, link, path):

        self.driver.get(link)
        time.sleep(2)
        items = int(self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div[2]/div[8]/div[1]/span[2]').text)
        os.chdir(path)
        title = random.randint(11111111, 99999999)
        os.mkdir(str(title))
        for item in range(items):
            download = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div/img').get_attribute('src')
            urllib.request.urlretrieve(download, str(title) + '/' + str(item) + '.jpg')
            nextpage = self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div[2]/div[8]/a[2]/span')
            nextpage.click()
            print(item)

    def langselector(self):
        time.sleep(1)
        select = self.driver.find_element_by_xpath('//*[@id="quick_search_input"]')
        select.click()
        select.send_keys(' ')
        select = self.driver.find_element_by_xpath('//*[@id="quick_search_button"]/span')
        select.click()

        #
        select = self.driver.find_element_by_xpath('//*[@id="lang_id"]')
        print(select.text)
        select = self.driver.find_element_by_xpath('//*[@id="lang_id"]/option[3]')
        select.click()
        select = self.driver.find_element_by_xpath('/html/body')
        select.click()

    def download(self, path):
        time.sleep(4)
        title = random.randint(11111111, 99999999)
        count = 0
        os.chdir(path)
        os.mkdir(str(title))
        while True:
            time.sleep(2)
            download = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div/img').get_attribute('src')
            print(download)
            urllib.request.urlretrieve(download, str(title) + '/' + str(count) + '.jpg')
            nextpage = self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div[2]/div[8]/a[2]/span')
            nextpage.click()
            count +=1