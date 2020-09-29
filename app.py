from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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
    
    def search_hastags(self, hastag):
        self.driver.find_element_by_xpath("//input[@type=\"text\"]")\
            .send_keys(hastag)
   # def get_unfollowers(self):
       # self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
        #    .click()
        #time.sleep(2)
        #self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
         #   .click()
        #time.sleep(2)
        #sugs = self.driver.find_element_by_xpath("//h4[contains(text(), sugestões)]")
        #self.driver.execute_script("arguments[0].scrollIntoView")
        #time.sleep(2)
        #scroll_box =  self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        #last_ht, ht = 0,1
        #time.sleep(1)
        #ht = self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);
        #return arguments[0].scrollHeight;
        #""", scroll_box)


my_bot = Instabot('johnyanastacio','johny@257310')
my_bot.search_hastags("#python")