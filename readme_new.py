from selenium import webdriver

from selenium.webdriver.common.by import By
import re
import pandas as pd
import os
import requests

driver = webdriver.Chrome()
url='https://github.com/facebook/react'
driver.get(url)
readme_text=''
readC = driver.find_elements(By.CLASS_NAME, "Box-body")
readme_text=readC[0].text
print(readme_text)
    
driver.close()