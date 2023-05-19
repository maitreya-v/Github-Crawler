
from selenium import webdriver

from selenium.webdriver.common.by import By
import re
import pandas as pd
import os
import requests
driver = webdriver.Chrome()

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
                print(res)
                # if "Co-authored-by" in str(res):
                #     continue
                # elif "Signed-off-by" in str(res):
                #     continue
                # else:
                # list_of_commits.append(res["commit"]["message"])
            page_num += 1
        else:
            # print("Failed to fetch commits for page", page_num)
            break
    return list_of_commits
final_list_commits=[]
repo='facebook/react-native'
new_url_commits='https://api.github.com/repos/{}/commits'.format(repo)
final_list_commits.append(get_commits(new_url_commits))
print(final_list_commits)