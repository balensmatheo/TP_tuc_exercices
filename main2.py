import selenium
from selenium import webdriver 
import time
from selenium.webdriver.common.by import By

# Path: selenium/webdriver.py

def get_random_wiki():
    driver = webdriver.Chrome() 
    driver.get('https://wikiroulette.co/')
    page_title = driver.title
    driver.quit()
    return page_title

get_random_wiki()



