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
import os

def scrape_item():
    data = {}
    try:
        title = soup_prop.find('h1',{'class':'title'}).text
    except:
        try:
            title = soup_prop.find('h1').text.replace('\n','').strip()
        except:
            title = None

    try:
        address = soup_prop.find('p',{'class':'full-address__text'}).text
    except:
        try:
            address = soup_prop.find('div',{'class':'property-detail'}).text.replace('\n','').strip()
        except:
            address = None

    try:
        desc = soup_prop.find('div',{'class':'description'}).text
    except:
        try:
            desc = soup_prop.find('div',{'class':'listing-details-text compacted'}).text.replace('\n','').strip()
        except:
            desc = None

    try:
        price = soup_prop.find('h2',{'class':'amount'}).text
    except:
        try:
            price = soup_prop.find('div',{'class':'property-value'}).text.replace('\n','').strip()
        except:
            price = None

    try:
        prop_type = soup_prop.find('div',{'class':'meta-table__item__value-text'}).text
    except:
        try:
            prop_type = soup_prop.find('td',{'class':'value-block'}).text.replace('\n','').strip()
        except:
            prop_type = None

    try:
        agent_name = soup_prop.find('a',{'class':'actionable-link agent-name truncate-line'}).text
    except:
        agent_name = None

    try:
        agency = soup_prop.find('div',{'class':'agency'}).text
    except:
        try:
            agency = soup_prop.find('div',{'class':'dev-name'}).text.replace('\n','').strip()
        except:
            agency = None


    try:
        agent_phone = soup_prop.find('a',{'class':'actionable-link btn-outline-secondary btn'}).get('href')
    except:
        agent_phone = None

    try:
        prop_cat = soup_prop.find('div',{'class':'label'}).text
    except:
        prop_cat = None

    data['property_url'] = prop
    data['title'] = title
    data['address'] = address
    data['desc'] = desc
    data['price'] = price
    data['prop_type'] = prop_type
    data['prop_cat']= prop_cat
    data['agent_name'] = agent_name
    data['agency'] = agency


    return data

with open('agent/test.json') as f:
    out = json.load(f)

agent_ids = [i['agent_id'] for i in out]

## 2500 TO END
agent_ids = agent_ids[2500:]

chrome_options = uc.ChromeOptions() 
chrome_options.headless = False  # Set headless to False to run in non-headless mode

driver = uc.Chrome(options=chrome_options)
link_done = []
link_fail = []
datas = []

for agent_id in agent_ids:
    index_card = agent_ids.index(agent_id)
    agent_props = {'resident_sell':f'https://www.rumah.com/properti-dijual?agent_id={agent_id}&market=residential',
                    'resident_rent':f'https://www.rumah.com/properti-disewa?agent_id={agent_id}&market=residential',
                    'commercial_sell':f'https://www.rumah.com/properti-dijual?agent_id={agent_id}&market=commercial',
                    'commercial_rent':f'https://www.rumah.com/properti-disewa?agent_id={agent_id}&market=commercial'}


    for properties_link in agent_props.keys():
        driver.get(url=agent_props[properties_link])
        soup_page = BeautifulSoup(driver.page_source, 'html.parser')

        try:
            last_page = soup_page.find('ul',{'class':'pagination'}).find_all('li')[-2].text
            last_page = int(last_page)
            scrape = 0
            for page in range(1,last_page+1):
                try:
                    page_url = f'https://www.rumah.com/properti-dijual/{page}?agent_id={agent_id}'
                    driver.get(url=page_url)
                    soup_page_ = BeautifulSoup(driver.page_source, 'html.parser')
                    links_prop = soup_page.find_all('a',{'class':'nav-link'})
                    links_prop = [i.get('href') for i in links_prop]

                    
                    for prop in links_prop:
                        try:
                            scrape += 1
                            print(f"AGENT ID {agent_id}, n_AGENT {index_card}, CAT {properties_link}, PAGE {page}, SCRAPE {scrape}")
                            
                            driver.get(url=prop)
                            soup_prop = BeautifulSoup(driver.page_source, 'html.parser')

                            data = scrape_item()
                            
                            datas.append(data)

                            with open('agent/property2.json', 'w') as f:
                                json.dump(datas, f)
                        except:
                            pass
                except:
                    pass
        except:
            pass