# from selenium import webdriver
# import pandas as pd
# from selenium.webdriver.common.by import By
  
# # for holding the resultant list
# readme_content = []
# commit_hist = []

# # lis = ["https://github.com/facebook/react", "https://github.com/facebook/react-native"]
# # for i in lis:
# page_url = "https://github.com/facebook/react"        #Add URL here
# # page_url = "https://github.com/facebook/react-native"        #Add URL here

# driver = webdriver.Chrome()
# keyword = "devang"
# driver.get(page_url)


# #Feature 1 - Readme content
# readC = driver.find_elements(By.CLASS_NAME,"Box-body")
# readme_content.append(readC[0].text)


# #Feature 2 - Commit messages
# page_commits_url = page_url + "/commits/main"
# driver1 = webdriver.Chrome()
# keyword = "devang"
# driver1.get(page_commits_url)
# commitH = driver1.find_elements(By.CLASS_NAME,"flex-auto min-width-0 js-details-container Details")
# vr = ""
# for i in range(len(commitH)):
#     vr=vr+str(commitH[i].text) + "$"   #$ acts as a separator between each commit msg
# print(vr)



# #closing the driver
# driver.close()

# dataDf = pd.DataFrame()
# dataDf["readme"] = readme_content
# dataDf["commits"] = commit_hist
# print(dataDf)

# #this will return a CSV file
# # dataDf.to_csv(r'xyz_dataset.csv', index=False) 


from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

commit_list= []

url='https://github.com/facebook/react/commits/main'

driver = webdriver.Chrome()

driver.get(url)

commits = driver.find_elements(By.CLASS_NAME,'Box-row')
print(len(commits))
v=''
for i in range(len(commits)):
    title = v + str(commits[i].text) + '$'
    # print('sss')/
    print(title)

    
driver.close()    