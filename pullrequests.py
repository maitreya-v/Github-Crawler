
from selenium import webdriver

from selenium.webdriver.common.by import By
import re
import pandas as pd
import requests
import os
import urllib.request
import json
import ssl
import os
import time
driver = webdriver.Chrome()

url='https://github.com/facebook/react-native'

driver.get(url)
list_of_pulls=[]
total_pulls=0
def get_pulls(url):
    global total_pulls
    
    url = str(url)
    driver.get(url)
    
    boxes=driver.find_elements(By.CLASS_NAME,'Box-row')
    print(len(boxes))
    for box in boxes:
        try:
            svg=box.find_element(By.CLASS_NAME,'color-fg-done')
            list_of_pulls.append(box.find_element(By.CLASS_NAME,'markdown-title').text)
            print("horaha")
        except:
            pass
        try:
            svg=box.find_element(By.CLASS_NAME,'color-fg-closed')
            anchor_tags=box.find_elements(By.CLASS_NAME,'hx_IssueLabel')
            for anchor_tag in anchor_tags:
                if anchor_tag.get_attribute('data-name')=='Merged':
                    list_of_pulls.append(box.find_element(By.CLASS_NAME,'markdown-title').text)
                    break
        except:
            pass
    next_btn = driver.find_elements(By.CLASS_NAME,'next_page')
    return next_btn[0].get_attribute('href')

new_url_pulls=str(url)+'/pulls?q=is%3Apr+is%3Aclosed'
while(new_url_pulls!=None):
    print(new_url_pulls)
    new_url_pulls=get_pulls(new_url_pulls)
print(list_of_pulls)

driver.close()