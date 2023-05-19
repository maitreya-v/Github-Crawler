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
readme = []
list_of_pulls=[]
total_pulls=0

new_url_pulls='https://github.com/facebook/react/pulls'
def get_open_pulls(url):
    global total_open_pulls
    
    url = str(url)
    driver.get(url)
    
    issues = driver.find_elements(By.CLASS_NAME,'markdown-title')
    total_open_pulls = total_open_pulls+len(issues)
    for issue in issues:
        list_of_pulls.append(issue.text)
    next_btn = driver.find_elements(By.CLASS_NAME,'next_page') 
    return next_btn[0].get_attribute('href')



href_list=[]

href=''
def get_closed_pulls(url):
    global total_closed_pulls
    
    url = str(url)
    driver.get(url)
    closed_href = driver.find_elements(By.CLASS_NAME,'btn-link')
    for href in closed_href:
        if href.get_attribute('href')!=None and "closed" in href.get_attribute('href'):
            href_list.append(href.get_attribute('href'))
        # if href.get_attribute('href')!=None:
        #      if "closed " in href.get_attribute('href'):
        #         print("True")
        # if "closed" in href.get_attribute('href'):
            # print(href)
    # issues = driver.find_elements(By.CLASS_NAME,'markdown-title')
    # total_closed_pulls = total_closed_pulls+len(issues)
    # for issue in issues:
    #     list_of_pulls.append(issue.text)
    # next_btn = driver.find_elements(By.CLASS_NAME,'next_page') 
    # return next_btn[0].get_attribute('href')
get_closed_pulls(new_url_pulls)
# print(href)
print(href_list)
# url = "https://api.github.com/repos/scikit-learn/scikit-learn/readme"
# html_url=''
# # Make a request to the API
# response = requests.get(url)

# # Check the response status code
# if response.status_code == 200:
#     # The request was successful, so get the README
#     read_me = response.json()

#     # Print the README
#     print(read_me['html_url'])
#     html_url=str(read_me['html_url'])
# else:
#     # The request failed, so print the error message
#     print(response.status_code, response.reason)



# new_url_readme=html_url
# print(new_url_readme)
# driver.get(new_url_readme)
# readC = driver.find_elements(By.CLASS_NAME, "Box-sc-g0xbh4-0")
# print(readC)
# for i in range(len(readC)):
    # readme.append(readC[i].text)
    
# while(new_url_pulls!=None):
# # for i in range(1):
#     new_url_pulls=get_open_pulls(new_url_pulls)

# print(readme)


driver.close()


