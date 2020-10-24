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
            like_button = driver.find_element_by_css_selector('.fr66n > button:nth-child(1) > div:nth-child(1) > span:nth-child(1) > svg:nth-child(1)').click()
            time.sleep(3)
            
        

my_bot = Instabot('username','password')
my_bot.like_photos("here goes the hastag without #")
