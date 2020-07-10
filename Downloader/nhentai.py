from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import os
import urllib.request
import time

class Downloader:
    def __init__(self, path):
        self.path = path
        self.driver = webdriver.Chrome(self.path)

    def getPage(self):
        self.driver.get('https://nhentai.net/')
        self.driver.maximize_window()

    def randomStoryEng(self):
        random = self.driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[1]/a')
        random.click()
        eng = 'translated\n109K\nenglish\n69K'

        ok = False
        while True:
            langs = self.driver.find_elements_by_xpath('//*[@id="tags"]/div[6]/span')
            for lang in langs:
                if lang.text == eng:
                    ok = True
            if ok == True:
                break
            else:
                random = self.driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[1]/a')
                random.click()
    def randomStory(self):
        random = self.driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[1]/a')
        random.click()

    def getImage(self):
        title = random.randint(11111111,99999999)
        print(title)
        downloader = self.driver.find_element_by_xpath('//*[@id="thumbnail-container"]/div/div[1]/a/img')
        os.mkdir(str(title))
        downloader.click()
        count = 0
        while True:
            downloader = self.driver.find_element_by_xpath('//*[@id="image-container"]/a/img').get_attribute('src')
            urllib.request.urlretrieve(downloader, str(title)+'/'+str(count)+'.jpg')
            downloader = self.driver.find_element_by_xpath('//*[@id="content"]/section[4]/div[2]/a[3]')
            downloader.click()
            count +=1
