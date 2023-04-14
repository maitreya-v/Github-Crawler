from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

commit_list= []
# hello
new_url='https://github.com/facebook/react/commits/main'
# new_url='https://github.com/facebook/react-native/commits/main'
# new_url='https://github.com/angular/angular/commits/main'

driver = webdriver.Chrome()

# driver.get(url)

list_of_commits=[]
# new_url=None
# older_btn_href=older_btn.__getattribute__('href')
total_commits=0
page_number=0
def get_commits(url):
    global total_commits
    global page_number
    
    
    url=url
    driver.get(url)
    button = driver.find_elements(By.CLASS_NAME,'ellipsis-expander')

    for btn in button:
        # if btn.exists():
            btn.click()
        # else:
            # pass
    
    
        
        
    commits = driver.find_elements(By.CLASS_NAME,'ws-pre-wrap')
    page_number+=1
    print(page_number)
    # print(commits[0].text)
    for commit in commits:
        # if commit.exists():
            list_of_commits.append(commit.text)
        # else:
            # pass 

    
    all_btn=driver.find_elements(By.CLASS_NAME,'BtnGroup-item')
    for btn in all_btn:
        if btn.text=='Older':
            older_btn_link=btn.get_attribute('href')
    return older_btn_link
    # older_btn_url=driver.find_elements(By.TAG_NAME,'   
# new_url=get_commits(url)    

while(new_url!=None):
# for i in range(1):
    new_url=get_commits(new_url)
    
print(len(list_of_commits)) 
print(list_of_commits)   

    
driver.close()    


dataDf = pd.DataFrame()
dataDf["commits"] = list_of_commits
print(dataDf)

#this will return a CSV file
dataDf.to_csv(r'react_commits.csv', index=False) 