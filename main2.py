from selenium import webdriver 
from selenium.webdriver.common.by import By

# Path: selenium/webdriver.py

driver = webdriver.Chrome()
option = driver.create_options()
option.add_argument('--headless')
driver = webdriver.Chrome(options=option)


def get_random_wiki():
    driver.get('https://wikiroulette.co/')
    # get iframe with the id iframe
    iframe = driver.find_elements(by=By.TAG_NAME, value='iframe')
    src = iframe[0].get_attribute('src')
    driver.get(src)
    # get the title of the page
    title = driver.find_elements(by=By.CLASS_NAME, value='mw-page-title-main')
    return title[0].text


print(get_random_wiki())

driver.quit()



