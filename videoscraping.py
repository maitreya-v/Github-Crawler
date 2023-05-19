from selenium import webdriver
import pandas as pd

from selenium.webdriver.common.by import By

url='https://www.youtube.com/@JohnWatsonRooney/videos'

driver = webdriver.Chrome()

driver.get(url)


video_list = []
# style-scope yt-horizontal-list-renderer
# //*[@id="video-title"]
# //*[@id="metadata-line"]/span[1]
# //*[@id="metadata-line"]/span[2]


# style-scope ytd-rich-grid-media
# //*[@id="video-title"]
# //*[@id="metadata-line"]/span[1]
# //*[@id="metadata-line"]/span[2]

videos = driver.find_elements(By.CLASS_NAME,'style-scope ytd-rich-grid-media')

for video in videos:
    title = video.find_element(By.XPATH,'.//*[@id="video-title"]').text
    views = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[1]').text
    when = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[2]').text
    print(title,views,when)
    video_obj = {
        'title':title,
        'views':views,
        'when':when
    }
    
    video_list.append(video_obj)
    
    
df = pd.DataFrame(video_list)
print(df)    