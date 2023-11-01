
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

ua = UserAgent()

options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument('--blink-settings=imagesEnabled=false')

email = 'jarni066@gmail.com'
pass_rumah = 'P$6bCxeAQr9iSDD'

url = "https://www.rumah.com"
url_jual = 'https://www.rumah.com/properti-dijual/1700?'


headers = {
  'authority': 'www.rumah.com',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9,ko;q=0.8,id;q=0.7,de;q=0.6,de-CH;q=0.5',
  'baggage': 'sentry-environment=prod,sentry-public_key=8db5c26f862f45d8b4b19c54da53dcd1,sentry-trace_id=d5b0f1fc565b4553a293e2eb35766ae6,sentry-sample_rate=0',
  'cache-control': 'no-cache',
  'cookie': 'ab.storage.sessionId.d6c8d2bf-78e5-46a1-a4f0-0b3b80d76f24=%7B%22g%22%3A%22306161c2-d61d-7743-466c-a1406e3269fc%22%2C%22e%22%3A1697978474636%2C%22c%22%3A1697976674636%2C%22l%22%3A1697976674636%7D; _fbp=fb.1.1697976674971.1072695973; ab.storage.deviceId.d6c8d2bf-78e5-46a1-a4f0-0b3b80d76f24=%7B%22g%22%3A%22483d4526-7cfc-791a-53be-56cefe925ba3%22%2C%22c%22%3A1697976689946%2C%22l%22%3A1697976689946%7D; _hjSessionUser_2945388=eyJpZCI6IjA5MTA0OTBlLTdhZDYtNTM3My05MjUyLWM2NDg5ZDgzZDE0NCIsImNyZWF0ZWQiOjE2OTc5NzY2ODg1MDAsImV4aXN0aW5nIjp0cnVlfQ==; sixpack_client_id=68194D64-3B08-E250-84BB-18C2D376C283; Visitor=c8398cec-ed65-48eb-9d94-6e0460173749; pgutid=3f681740-d78a-4caa-98d9-bcf99397aac7; _ga4_ga=GA1.2.207436936.1697976675; g_state={"i_p":1698927151954,"i_l":3}; pgutid=3f681740-d78a-4caa-98d9-bcf99397aac7; _gid=GA1.2.1740108019.1698722437; _clck=1b8zwfp|2|fgc|0|1390; __gpi=UID=00000c6e0df2312c:T=1698025889:RT=1698814889:S=ALNI_MZbTpIQ8RvYgsTWHxS66uyjIVHnDQ; _clsk=ig0jyq|1698860367144|1|1|y.clarity.ms/collect; _ga_EJ4T5TQC5C=GS1.1.1698860365.21.0.1698860368.0.0.0; PHPSESSID=cee026f91b010fa3de4491d1da215c60; _ga=GA1.2.207436936.1697976675; _gat=1; _gat_regionalTracker=1; isRedirectFromMapSearch=false; cf_chl_2=20a66ad20bc3e9f; __cf_bm=om7WJZ_UJ4r9CPdrMdrfzPKjUwt1OHtUZP7wcF5W7mo-1698862743-0-AfYuzLVCMv95YIQBA7NuOWuW4GuMFTMHa+qt8fGM9IuvrhiZ/fL01kz9ZWlzM8r/9p4keaRS+2HKBsKo7pKYSriqHgvBHqS10w3ty+iwuJ2p; cf_clearance=.Dnl5gSgC83fwBfa.15I0LhVacc9p0F_fZq31Cw6Nqw-1698862745-0-1-5ea85612.19d2d3a4.9a909f2-250.2.1698862745; __gads=ID=3bd135502187e6c3-22da119905e5004f:T=1697976713:RT=1698862748:S=ALNI_Ma2pf6LRpYg7uwnbUe51DNz_0k6xg; _ga4_ga_EJ4T5TQC5C=GS1.2.1698860369.37.1.1698862750.0.0.0; _ga_7RWB0F6NS6=GS1.2.1698860371.33.1.1698862750.46.0.0; __cf_bm=bKYNAOjtNt58Qk9aGXgdpmUTQuMJgEgzB6pXvIuafTU-1698862773-0-AeFloYW81yu7E2JZS0JWyBLSYSzvTZMdfJ8Ksjtk652pmuKBLMb5TdNxmtUxes2NZCKr2Q9KJrzCsojIk5qEPsaxT+TFove/6LRdGfGkjsxg',
  'pragma': 'no-cache',
  'referer': 'https://www.rumah.com/properti-dijual/1700?',
  'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sentry-trace': 'd5b0f1fc565b4553a293e2eb35766ae6-a93f55a48df95847-0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
  'x-ajax-search': 'true',
  'x-requested-with': 'XMLHttpRequest'
}




def interceptor(request):
    del request.headers  # Delete the header first
    request.headers = headers



driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)
driver.request_interceptor = interceptor
driver.get(url_jual)
time.sleep(1)
datas = []

# login_but = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/nav/div/div[2]/button')
# login_but.click()
# time.sleep(1)
# email_field = driver.find_element(By.CSS_SELECTOR,'input.generic-input.form-control')
# email_field.send_keys(email)
# time.sleep(1)
# email_field.send_keys(Keys.ENTER)
# time.sleep(1)
# pass_field = driver.find_element(By.CSS_SELECTOR,'input.generic-input.form-control')
# pass_field.send_keys(pass_rumah)
# pass_field.send_keys(Keys.ENTER)
# time.sleep(1)
# jual_tab = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/nav/div/div[1]/a[1]')
# jual_tab.click()
# time.sleep(1)


soup = BeautifulSoup(driver.page_source, 'html.parser')

paginations = soup.find('ul',{'class':'pagination'}).find_all('li')


next_but_class = paginations[-1].attrs['class']

while 'disabled' not in next_but_class:
    page_data = {}
    soup_page = BeautifulSoup(driver.page_source, 'html.parser')

    #GET DATA
    page_paginations = soup_page.find('ul',{'class':'pagination'})
    active_page = page_paginations.find('li',{'class':'active'}).find('a').text
    print(f"ACTIVE PAGE {active_page}")

    #ADD NEXT BUTTON CLASS UNTIL DISABLED
    next_but_class_page = page_paginations.find_all('li')[-1].attrs['class']
    next_but_class = next_but_class_page

    
    
    if int(active_page) > 1700:
        prop_head = soup_page.find_all('div',{'class':'header-container'})
        prop_links = [i.find('a').get('href') for i in prop_head]
        
        #APPENDING DATA
        page_data[active_page] = prop_links
        datas.append(page_data)

        with open('agent/output/proplink_from1700.json', 'w') as f:
            json.dump(datas, f)

        #DRIVER NEXT PAGE
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'pagination-next')))
        next_page_but = driver.find_element(By.CLASS_NAME,'pagination-next').find_element(By.TAG_NAME,'a')
        next_page_but.click()
        # time.sleep(0.8)
    else:
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'pagination-next')))
        next_page_but = driver.find_element(By.CLASS_NAME,'pagination-next').find_element(By.TAG_NAME,'a')
        next_page_but.click()
        # time.sleep(0.8)



driver.close()