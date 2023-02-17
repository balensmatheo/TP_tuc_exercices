from selenium import webdriver 
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
# Path: selenium/webdriver.py

chromedriver_autoinstaller.install()
# i want to add options
chrome_options = webdriver.ChromeOptions()    
options = [
    "--ignore-certificate-errors"
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    '--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(options = chrome_options)

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



