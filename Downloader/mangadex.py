from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
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


    def login(self, username, password):
        login = self.driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[2]/li[2]/a')
        login.click()
        login = self.driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[2]/li[2]/div/a[1]/span')
        login.click()
        # login access
        login = self.driver.find_element_by_xpath('//*[@id="login_username"]')
        login.click()
        login.send_keys(username)
        login = self.driver.find_element_by_xpath('//*[@id="login_password"]')
        login.click()
        login.send_keys(password)
        login = self.driver.find_element_by_xpath('//*[@id="login_button"]/span')
        login.click()

    # serching manga
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

    def numberPages(self, link):
        self.driver.get(link)
        time.sleep(2)
        items = int(self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div[2]/div[8]/div[1]/span[2]').text)
        return items
    def createFolder(self, path):
        os.chdir(path)
        title = random.randint(11111111, 99999999)
        os.mkdir(str(title))
        os.chdir(str(title))
        return os.getcwd()+chr(92);
    def getLink(self, link):
        self.driver.get(link)
        time.sleep(3)
    def downloadSelectedChapter(self, items, path):
        time.sleep(2)
        for item in range(items):
            download = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div/img').get_attribute('src')
            urllib.request.urlretrieve(download, str(path)+ '/'+str(item) + '.jpg')
            nextpage = self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div[2]/div[8]/a[2]/span')
            nextpage.click()
            print(item)
            time.sleep(2)

    def numberPagesChapter(self, items):
        running = True
        while running:
            try:
                time.sleep(3)
                n = int(self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div[2]/div[8]/div[1]/span[2]').text)
                print(n)
                items.append(n)
                next = self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div[2]/div[2]/a[2]/span')
                next.click()
            except NoSuchElementException:
                running = False
        return items

    def downloadAllPages(self, arr, path):
        count = 1
        for items in arr:
            time.sleep(3)
            for item in range(items):
                download = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div/img').get_attribute('src')
                urllib.request.urlretrieve(download, str(path)+ '/'+str(count) + '.jpg')
                count +=1
                nextpage = self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div[2]/div[8]/a[2]/span')
                nextpage.click()
                print(item)

    def quit(self):
        self.driver.quit()
