from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
import requests
import undetected_chromedriver as uc 
import re
from selenium_stealth import stealth
from fake_useragent import UserAgent



ua = UserAgent()

chrome_options = uc.ChromeOptions() 
user = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
chrome_options.headless = False  # Set headless to False to run in non-headless mode
# chrome_options.add_argument('User-Agent={0}'.format(ua.chrome))
# chrome_options.add_argument("start-maximized")

driver = uc.Chrome(use_subprocess=True,options=chrome_options)
datas = []
link_done = []
link_fail = []
url_home = 'https://www.rumah.com/properti-disewa/' 

page_url = url_home + str(99) +'?'
driver.get(url=page_url)
time.sleep(5)
for page in range(99, 2217):
    try:
        # a = 'https://www.rumah.com/properti-disewa/103?&ajax=true'
        
        # driver.maximize_window()
        print(page,'page')
        next_but = driver.find_element(By.CLASS_NAME,"pagination-next").find_element(By.TAG_NAME, 'a')
        next_but.click()
        time.sleep(1)
        print(next_but.text)
        soup_page = BeautifulSoup(driver.page_source, 'html.parser')
        links_prop = soup_page.find_all('a',{'class':'nav-link'})
        links_prop = [i.get('href') for i in links_prop]
        datas  += links_prop
        with open('agent/property_disewa_links_100.json', 'w') as f:
            json.dump(datas, f)
        
    except:
        pass