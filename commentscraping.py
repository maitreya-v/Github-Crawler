from selenium import webdriver
import pandas as pd

from selenium.webdriver.common.by import By

url='https://www.youtube.com/watch?v=qX0jZqlmO2o'

driver = webdriver.Chrome()

driver.get(url)


comment_list = []


# style-scope ytd-comment-renderer
# //*[@id="author-text"]/span
# //*[@id="vote-count-middle"]
# //*[@id="header-author"]/yt-formatted-string/a

comments = driver.find_elements(By.CLASS_NAME,'style-scope ytd-comment-renderer')

for comment in comments:
    name = comment.find_element(By.XPATH,'.//*[@id="author-text"]/span').text
    likes = comment.find_element(By.XPATH,'.//*[@id="vote-count-middle"]').text
    when = comment.find_element(By.XPATH,'.//*[@id="header-author"]/yt-formatted-string/a').text
    print(name,likes,when)
    comment_obj = {
        'title':name,
        'views':likes,
        'when':when
    }
    
    comment_list.append(comment_obj)
    
    
df = pd.DataFrame(comment_list)
print(df)    