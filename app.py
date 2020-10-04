from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


print("INSTAGRAM BOT PARA CURTIR FOTOS")

class Instabot:
    def __init__(self, username, password):
        self.driver = webdriver.Firefox()
        self.username = username
        self.driver.get("https://instagram.com")
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
            .click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]")\
            .click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]")\
            .click()
    
    def like_photos(self, hastag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+hastag+"/?hl=en")
        time.sleep(2)
        
        
        for i in range(1,3):
            
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        
        hrefs= driver.find_elements_by_tag_name("a")
        pic_hrefs = [];
        for element in hrefs:
            tags = element.get_attribute('href')
            if  '.com/p/' in tags:
                pic_hrefs.append(tags) 
        for pic in pic_hrefs:
            driver.get(pic)
            time.sleep(3)
            like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Curtir"]').click()
            like_button().click()
            sleep(3)
            


        #pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        #pic_hrefs = [href for href in pic_hrefs if hastag in href]
        #print(pic_hrefs)

        #for pic_href in pic_hrefs:
           # driver.get(pic_href)
           # driver.execute_script("window.scroll(0, document.body.scrollHeight);")
            #try:
                #driver.find_elements_by_link_text('Curtir').click()
                #time.sleep(2)
           # except Exception as e:
               # time.sleep(2)

        

my_bot = Instabot('userame','password')
my_bot.like_photos("newyork")
