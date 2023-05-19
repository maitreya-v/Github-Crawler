# commits

import requests

url='https://api.github.com/repos/scikit-learn/scikit-learn/commits?per_page=100&page=1'

response  = requests.get(url)

response = response.json()

for res in response:
    if "Co-authored-by" in str(res):
        continue
    else:
        print(res["commit"]["message"])
