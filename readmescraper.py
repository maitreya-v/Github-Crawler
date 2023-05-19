import requests
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
# driver = webdriver.Chrome()

# url = "https://api.github.com/repos/scikit-learn/scikit-learn/readme"
# html_url=''
# # Make a request to the API
# response = requests.get(url)
# readme = []
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
#     readme.append(readC[i].text)



# loggin in

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
# Create a WebDriver object.
driver = selenium.webdriver.Chrome()

# Navigate to the GitHub login page.
driver.get("https://github.com/login")

# Enter your username and password.
username_input = driver.find_elements(By.ID,"login_field")
username_input[0].send_keys("maitreya.vaghulade@gmail.com")

# for username in username_input:
    # print(username)

password_input = driver.find_elements(By.ID,"password")
password_input[0].send_keys("maitreya1235")

# Click the "Sign in" button.
login_button = driver.find_elements(By.CLASS_NAME,"js-sign-in-button")
login_button[0].click()

url = "https://api.github.com/repos/scikit-learn/scikit-learn/readme"
html_url=''
# Make a request to the API
response = requests.get(url)
readme = []
# Check the response status code
if response.status_code == 200:
    # The request was successful, so get the README
    read_me = response.json()

    # Print the README
    print(read_me['html_url'])
    html_url=str(read_me['html_url'])
else:
    # The request failed, so print the error message
    print(response.status_code, response.reason)



new_url_readme=html_url
print(new_url_readme)
driver.get(new_url_readme)
readC = driver.find_elements(By.CLASS_NAME, "Box-sc-g0xbh4-0")
print(readC)
# for i in range(len(readC)):
#     readme.append(readC[i].text)

# Close the browser.
driver.quit()
