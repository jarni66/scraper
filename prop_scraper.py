
import undetected_chromedriver as uc
from fake_useragent import UserAgent
# from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
from prop_func import *

ua = UserAgent(browsers=['chrome'])
options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
options.add_argument('--headless')
# options.add_argument("--no-sandbox")
# options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument('--log-level=3')

driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 20)
datas = []
with open('agent/output/proplink_from1600to1700.json') as f:
    out = json.load(f)

for item in out:
    page = list(item.keys())[0]
    links = item[page]
    # print(links)
    scrape = 1
    for link in links:
        try:
            # driver.request_interceptor = interceptor
            driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": ua.random})
            driver.get(link)

            time.sleep(1)
            soup_prop = BeautifulSoup(driver.page_source, 'html.parser')
            data = scrape_item(soup_prop=soup_prop, prop=link)
            if data not in datas:
                datas.append(data)
                with open('agent/product/property_1.json', 'w') as f:
                    json.dump(datas, f)
            print(f"PAGE {page} ITEM {scrape} DONE")
            scrape += 1
        except:
            print(f"PAGE {page} ITEM {scrape} FAIL")
            scrape += 1

        


