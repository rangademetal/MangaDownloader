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

    # getting the page
    def getPageMangadex(self):
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

        # clik the first manga when the name is similar with manga parameter
        search = self.driver.find_element_by_xpath('//*[@id="content"]/div[4]/div/div[1]/a/img')
        search.click()
        # getting the last page
        search = self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/nav/ul/li[4]/a/span')
        search.click()

        # Getting manga
        search = self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div/div[2]/div/div/div[2]/a')
        search.click()
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