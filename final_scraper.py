from selenium import webdriver

from selenium.webdriver.common.by import By
import re
import pandas as pd
import os
import requests
driver = webdriver.Chrome()

def login():
    driver.get("https://github.com/login")

    username_input = driver.find_elements(By.ID,"login_field")
    username_input[0].send_keys("maitreya.vaghulade@gmail.com")


    password_input = driver.find_elements(By.ID,"password")
    password_input[0].send_keys("maitreya1235")

    login_button = driver.find_elements(By.CLASS_NAME,"js-sign-in-button")
    login_button[0].click()
    
    
# pulls function
def get_pulls(url):
    global total_pulls
    pulls=[]
    url = str(url)
    driver.get(url)
    
    boxes = driver.find_elements(By.CLASS_NAME, 'Box-row')
    for box in boxes:
        try:
            svg = box.find_element(By.CLASS_NAME, 'color-fg-done')
            pulls.append(box.find_element(By.CLASS_NAME, 'markdown-title').text)
        except:
            pass
        try:
            svg = box.find_element(By.CLASS_NAME, 'color-fg-closed')
            anchor_tags = box.find_elements(By.CLASS_NAME, 'hx_IssueLabel')
            for anchor_tag in anchor_tags:
                if anchor_tag.get_attribute('data-name') == 'Merged':
                    pulls.append(box.find_element(By.CLASS_NAME, 'markdown-title').text)
                    break
        except:
            pass
    next_btn = driver.find_elements(By.CLASS_NAME, 'next_page')
    if len(next_btn) > 0:
        return pulls, next_btn[0].get_attribute('href')
    else:
        return pulls, None


#get open pulls
def get_open_pulls(url):
    global total_pulls
    pulls=[]
    url = str(url)
    driver.get(url)
    boxes = driver.find_elements(By.CLASS_NAME, 'Box-row')
    for box in boxes:
        try:
            svg = box.find_element(By.CLASS_NAME, 'color-fg-open')
            pulls.append(box.find_element(By.CLASS_NAME, 'markdown-title').text)
        except:
            pass
    next_btn = driver.find_elements(By.CLASS_NAME, 'next_page')
    if len(next_btn) > 0:
        return pulls, next_btn[0].get_attribute('href')
    else:
        return pulls, None

#release notes function
def get_release_notes(url):
    headers = {"Authorization": "token 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"}
    list_of_releases=[]
    response = requests.get(url,headers=headers)
    releases=''
    if response.status_code == 200:
        releases = response.json()

    for release in releases:
        list_of_releases.append(release["name"])
        list_of_releases.append(release["body"])
    return list_of_releases



# commit function
def get_commits(url):
    list_of_commits=[]
    page_num = 1
    while True:
        headers = {"Authorization": "token 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"}
        response = requests.get(url, params={'per_page': 100, 'page': page_num},headers=headers)
        if response.status_code == 200:
            response_json = response.json()
            if len(response_json) == 0:
                break
            for res in response_json:
                list_of_commits.append(res["commit"]["message"])
            page_num += 1
        else:
            break
    return list_of_commits


#readme code

def get_readme(url):
    driver.get(url)
    readme_text=''
    readC = driver.find_elements(By.CLASS_NAME, "Box-body")
    readme_text=readC[0].text
    return readme_text



# list_of_repos=['Microsoft/TypeScript','facebook/react-native','facebook/react','scikit-learn/scikit-learn','apple/swift']
list_of_repos=['tensorflow/tensorflow','google/guava','google/googletest','docker-library/python','keras-team/keras']
final_list_commits=[]
master_list_of_pulls = []
master_list_of_open_pulls = []
final_list_releases=[]
final_list_readmes=[]
final_repo_list=[]


print("Logging in")
login()
print("Logged in")


for repo in list_of_repos:
    

    list_of_pulls=[]
    list_of_open_pulls=[]
    new_url_pulls='https://github.com/{}/pulls?q=is%3Apr+is%3Aclosed'.format(repo)
    new_url_open_pulls='https://github.com/{}/pulls?q=is%3Aopen+is%3Apr'.format(repo)
    new_url_readme='https://github.com/{}'.format(repo)
    new_url_commits='https://api.github.com/repos/{}/commits'.format(repo)
    new_url_release_notes='https://api.github.com/repos/{}/releases'.format(repo)
    

    print("Extracting commits from {}".format(repo))
    final_list_commits.append(get_commits(new_url_commits))
    print("Length of commits: {}".format(len(final_list_commits)))
    
    # print("Extracting pulls from {}".format(repo))
    # while(new_url_pulls!=None):
    #     pulls, new_url_pulls = get_pulls(new_url_pulls)
    #     list_of_pulls += pulls
    # print("Length of pulls: {}".format(len(list_of_pulls)))
    # master_list_of_pulls.append(list_of_pulls)
    
    print("Extracting open pulls from {}".format(repo))
    while(new_url_open_pulls!=None):
        pulls, new_url_open_pulls = get_open_pulls(new_url_open_pulls)
        list_of_open_pulls += pulls
    print("Length of open pulls: {}".format(len(list_of_open_pulls)))
    master_list_of_open_pulls.append(list_of_open_pulls)
    
    print("Extracting release notes from {}".format(repo))
    final_list_releases.append(get_release_notes(new_url_release_notes))
    print("Length of releases: {}".format(len(final_list_releases)))
    
    # print("Extracting readmes from {}".format(repo))
    # final_list_readmes.append(get_readme(new_url_readme))
    # print("Length of readmes: {}".format(len(final_list_readmes)))
    
    
    final_repo_list.append(repo)



driver.close()

dataDf = pd.DataFrame()

dataDf['repository'] = final_repo_list
dataDf['commits'] = final_list_commits
dataDf["open_pulls"] = master_list_of_open_pulls
# dataDf["pulls"] = master_list_of_pulls
# dataDf['readme'] = final_list_readmes
dataDf['release_notes'] = final_list_releases

print(dataDf)

import os

current_dir = os.getcwd()

file_path = os.path.join(current_dir, 'urav.csv')

dataDf.to_csv(file_path)