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
from fake_useragent import UserAgent
from prop_func import *



#LAST 1286
ua = UserAgent()
chrome_options = webdriver.ChromeOptions() 
chrome_options.add_argument("--headless")
chrome_options.add_argument(f'user-agent={ua.random}')
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=chrome_options)

with open('agent/agent_link.json') as f:
    out = json.load(f)
agent_ids = [i['link'] for i in out]
agent_ids = [i.split('-')[-1] for i in agent_ids]

datas = []
fail_agent = []
category_prop = ['resident_sell','resident_rent','commercial_sell','commercial_rent']
for cat in category_prop:
    for agent_id in agent_ids[1286:2000]:
        try:
            end_page = 2
            cur_page = 1
            scrape = 0
            while cur_page < end_page+1:
                url = pageurl(cat,cur_page,agent_id)
                driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": ua.random})
                driver.get(url=url)
                time.sleep(0.9)
                driver.set_page_load_timeout(20)    
                soup_page = BeautifulSoup(driver.page_source, 'html.parser')

                last_page = int(soup_page.find('ul',{'class':'pagination'}).find_all('li')[-2].text)
                end_page = last_page
                heads_prop = soup_page.find_all('h3',{'class':'h4 ellipsis text-transform-none'})            
                for prop_items in heads_prop:
                    time.sleep(0.5)
                    link = prop_items.find('a',{'class':'nav-link'}).get('href')
                    try:
                        driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": ua.random})
                        driver.get(url=link)
                        time.sleep(0.5)
                        soup_prop = BeautifulSoup(driver.page_source, 'html.parser')
                        data = scrape_item(soup_prop=soup_prop, prop=link)

                        datas.append(data)

                        with open('agent/output/agent_prop_1286.json', 'w') as f:
                            json.dump(datas, f)
                        scrape += 1
                        print(f"n_AGENT {agent_ids.index(agent_id)}, AGENT {agent_id}, {cat} SCRAPE {scrape} PAGE {cur_page}/{end_page}")
                    except:
                        scrape += 1
                        print(f"n_AGENT {agent_ids.index(agent_id)}, AGENT {agent_id}, {cat} SCRAPE {scrape} PAGE {cur_page}/{end_page} FAIL")
                    
                
                cur_page += 1
        except:
            fail_agent.append({'agent_id':agent_id, 'cat':cat,'cur':cur_page,'end':end_page})
            with open('agent/output/agent_fail_3.json', 'w') as f:
                json.dump(fail_agent, f)
            print(f"FAIL {cat} AGENT {agent_id}")







# # if links_prop != None:
# #     try:
# #         last_page = int(soup_page.find('ul',{'class':'pagination'}).find_all('li')[-2].text)
# #         for page in range(1,last_page+1):
# #             url_ = pageurl(properties_link)
# #             driver.get(url=url_)
# #             soup_page_ = BeautifulSoup(driver.page_source, 'html.parser')
# #             links_prop = soup_page_.find_all('a',{'class':'nav-link'})
# #             links_prop = list(set([i.get('href') for i in links_prop]))
# #             scrape = 1
# #             for prop in links_prop:
# #                 scrape += 1
                
# #                 try:
# #                     print(f"n_AGENT {agent_ids.index(agent_id)}, CAT {properties_link}, SCRAPE {scrape} {prop.split('/')[-1]}")
# #                     driver.get(url=prop)
# #                     soup_prop = BeautifulSoup(driver.page_source, 'html.parser')

# #                     data = scrape_item()
                    
# #                     datas.append(data)

# #                     with open('agent/agent_prop2.json', 'w') as f:
# #                         json.dump(datas, f)
# #                 except:
# #                     pass
# #     except:
# #         links_prop = soup_page.find_all('a',{'class':'nav-link'})
# #         links_prop = [i.get('href') for i in links_prop]
# #         scrape = 1
# #         for prop in links_prop:
# #             scrape += 1
# #             try:
# #                 print(f"n_AGENT {agent_ids.index(agent_id)}, CAT {properties_link}, SCRAPE {scrape}")
                
# #                 driver.get(url=prop)
# #                 soup_prop = BeautifulSoup(driver.page_source, 'html.parser')

# #                 data = scrape_item()
                
# #                 datas.append(data)

# #                 with open('agent/agent_prop2.json', 'w') as f:
# #                     json.dump(datas, f)

# #             except:
# #                 pass
