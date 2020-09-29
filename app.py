from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instabot:
    def __init__(self, username, password):
        self.driver = webdriver.Firefox()
        self.username = username
        self.driver.get("https://instagram.com")
        time.sleep(2)
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
            
    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        time.sleep(2)


my_bot = Instabot('johnyanastacio','johny@257310')
my_bot.get_unfollowers()