from selenium import webdriver

from selenium.webdriver.common.by import By
import re
import pandas as pd

# url = 'https://github.com/facebook/react/issues?page=1&q=is%3Aissue+is%3Aopen'
url='https://github.com/facebook/react/issues'
driver = webdriver.Chrome()

driver.get(url)

issues = driver.find_elements(By.CLASS_NAME,'markdown-title')

# list_of_repos = ['https://github.com/tensorflow/tensorflow','https://github.com/microsoft/vscode','https://github.com/facebook/react','https://github.com/aws/aws-sdk-java','https://github.com/cloudant/java-cloudant']

base_url = 'https://github.com/facebook/react/issues?page='
# pageination_links = driver.find_elements(By.CLASS_NAME,'')
links = [link.get_attribute('href') for link in driver.find_elements(By.TAG_NAME,'a') if link.get_attribute('href') and link.get_attribute('href').startswith(base_url)]
for link in links:
    print(link)
    
    
page_numbers = [int(re.search(r'page=(\d+)', url).group(1)) for url in links]
max_page_number = max(page_numbers)
print(max_page_number)    
list_of_issues=[]
total_issues=0
for i in range(1,max_page_number+1):
    url = f'https://github.com/facebook/react/issues?page={i}&q=is%3Aissue+is%3Aopen'
    driver.get(url)
    issues = driver.find_elements(By.CLASS_NAME,'markdown-title')
    total_issues = total_issues+len(issues)
    for i in range(len(issues)):
        list_of_issues.append(str(issues[i].text) + '$')
        
    
# print(v)
print(total_issues)
driver.close()

dataDf = pd.DataFrame()
print(list_of_issues)
# dataDf["readme"] = 
dataDf["issues"] = list_of_issues
print(dataDf)

# this will return a CSV file
dataDf.to_csv(r'react_issues.csv', index=False) 