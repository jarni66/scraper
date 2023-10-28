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

    

chrome_options = uc.ChromeOptions() 
chrome_options.headless = False  # Set headless to False to run in non-headless mode
driver = uc.Chrome(options=chrome_options)

link_done = []
link_fail = []
datas = []

with open('agent/agent_link.json') as f:
    out = json.load(f)

card_urls = [i['link'] for i in out]
scraped = 1
for card_url in card_urls:

    driver.get(url=card_url)
    soup_card = BeautifulSoup(driver.page_source, 'html.parser')

    agent_id = card_url.split('-')[-1]
    try:
        agent_name = soup_card.find('h1',{'class':'agent-fullname'}).text
    except:
        agent_name = None
    try:
        agency_name = soup_card.find('div',{'class':'agent-agency'}).text.replace('\n','').strip()
    except:
        agency_name = None
    try:
        aget_job_title = soup_card.find('div',{'class':'agent-job-title'}).text.replace('\n','').strip()
    except:
        aget_job_title = None
    try:
        agent_number = soup_card.find('span',{'class','agent-phone-number agent-phone-number-original visible-print'}).text
    except:
        agent_number = None
    try:
        whatsapp_url = soup_card.find('a',{'class','agent-whatsapp'}).get('href')
    except:
        whatsapp_url = None
    data = {'agent_id':agent_id,
            'agent_name':agent_name,
            'agency_name':agency_name,
            'aget_job_title':aget_job_title,
            'agent_number':agent_number,
            'whatsapp_url':whatsapp_url}
    datas.append(data)
    with open('agent/agent_info.json', 'w') as f:
        json.dump(datas, f)
    print(f"SCRAPED {scraped}")
    scraped += 1
